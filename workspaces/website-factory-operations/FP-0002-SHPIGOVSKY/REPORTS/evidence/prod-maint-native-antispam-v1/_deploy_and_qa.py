# -*- coding: utf-8 -*-
"""PROD-MAINT native anti-spam v1: intake, exact deploy, QA. Never closes indexing."""
from __future__ import annotations

import hashlib
import io
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import paramiko

ROOT = Path(
    r"X:\AI MARS\worktrees\fp-0002-prod-maint-antispam\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY"
)
EV = ROOT / "REPORTS" / "evidence" / "prod-maint-native-antispam-v1"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
WP_LOAD = f"{DOCROOT}/wp-load.php"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
THEME_REMOTE = f"{DOCROOT}/wp-content/themes/shpigovsky"

DEPLOY_MAP = {
    "shpigovsky-core.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "src/Forms/AntiSpam.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Forms/AntiSpam.php",
    "src/Forms/ConsultationHandler.php": ROOT
    / "WORDPRESS/plugins/shpigovsky-core/src/Forms/ConsultationHandler.php",
    "src/Admin/MailFormsSettings.php": ROOT
    / "WORDPRESS/plugins/shpigovsky-core/src/Admin/MailFormsSettings.php",
    "theme:template-parts/components/final-form.php": ROOT
    / "WORDPRESS/theme/shpigovsky/template-parts/components/final-form.php",
    "theme:template-parts/layout/global-consultation-modal.php": ROOT
    / "WORDPRESS/theme/shpigovsky/template-parts/layout/global-consultation-modal.php",
    "theme:assets/js/v9-shell.js": ROOT / "WORDPRESS/theme/shpigovsky/assets/js/v9-shell.js",
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if match:
            pairs[match.group(1)] = match.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(name: str, payload: Any) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class RuntimeContext:
    def __init__(self) -> None:
        self.pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
        self.client: paramiko.SSHClient | None = None
        self.sftp: paramiko.SFTPClient | None = None

    def connect(self) -> None:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=getf(self.pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
            port=int(getf(self.pairs, "ssh_port", "sftp_port") or "22"),
            username=getf(self.pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
            password=getf(
                self.pairs,
                "ssh_password_or_key_reference",
                "ssh_password",
                "sftp_password",
                "ftp_or_sftp_password",
                "ftp_password",
            ),
            timeout=60,
            allow_agent=False,
            look_for_keys=False,
        )
        self.client = client
        self.sftp = client.open_sftp()

    def close(self) -> None:
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()

    def sftp_get(self, remote_path: str) -> bytes | None:
        assert self.sftp is not None
        buf = io.BytesIO()
        try:
            self.sftp.getfo(remote_path, buf)
            return buf.getvalue()
        except OSError:
            return None

    def sftp_put_bytes(self, remote_path: str, data: bytes) -> None:
        assert self.sftp is not None
        parent = remote_path.rsplit("/", 1)[0]
        self.run_ssh(f"mkdir -p {parent}")
        self.sftp.putfo(io.BytesIO(data), remote_path)

    def run_ssh(self, command: str, timeout: int = 120) -> tuple[str, str, int]:
        assert self.client is not None
        _stdin, stdout, stderr = self.client.exec_command(command, timeout=timeout)
        return (
            stdout.read().decode("utf-8", errors="replace"),
            stderr.read().decode("utf-8", errors="replace"),
            stdout.channel.recv_exit_status(),
        )

    def ensure_alive(self) -> None:
        try:
            transport = self.client.get_transport() if self.client else None
            if transport is None or not transport.is_active():
                raise OSError("ssh inactive")
            self.run_ssh("true", timeout=15)
        except Exception:  # noqa: BLE001
            self.close()
            self.connect()

    def run_php_remote(self, php: str, label: str) -> dict[str, Any]:
        self.ensure_alive()
        # Beget open_basedir: CLI harness must live under DOCROOT, not /tmp.
        remote = f"{DOCROOT}/_fp02_as_{label}.php"
        assert self.sftp is not None
        self.sftp.putfo(io.BytesIO(php.encode("utf-8")), remote)
        out, err, code = self.run_ssh(
            f"cd {DOCROOT} && (php8.2 {remote} || /usr/local/bin/php8.2 {remote} || php {remote}); ec=$?; rm -f {remote}; exit $ec",
            timeout=240,
        )
        text = (out or "").strip()
        # Prefer last top-level JSON object if PHP notices precede it.
        decoded = None
        if text:
            try:
                decoded = json.loads(text)
            except json.JSONDecodeError:
                marker = "FP02_AS_RESULTS:"
                if marker in text:
                    chunk = text.split(marker, 1)[1].strip()
                    try:
                        decoded = json.loads(chunk)
                    except json.JSONDecodeError:
                        decoded = None
                if decoded is None:
                    # Walk backward for a balanced top-level object.
                    for i in range(len(text) - 1, -1, -1):
                        if text[i] != "{":
                            continue
                        try:
                            decoded = json.loads(text[i:])
                            break
                        except json.JSONDecodeError:
                            continue
        if isinstance(decoded, (dict, list)):
            return {"ok": True, "data": decoded, "exit_code": code, "stderr_head": (err or "")[:1500]}
        return {
            "ok": False,
            "stdout_head": (out or "")[:8000],
            "stderr_head": (err or "")[:4000],
            "exit_code": code,
        }


def remote_for(rel: str) -> str:
    if rel.startswith("theme:"):
        return f"{THEME_REMOTE}/{rel[6:]}"
    return f"{PLUGIN_REMOTE}/{rel}"


INTAKE_PHP = r"""<?php
chdir('{docroot}');
require '{wp_load}';
$out = array(
  'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'blog_public' => (int) get_option('blog_public'),
  'handler' => class_exists('\\Shpigovsky\\Core\\Forms\\ConsultationHandler'),
  'antispam' => class_exists('\\Shpigovsky\\Core\\Forms\\AntiSpam'),
  'ajax_action' => \\Shpigovsky\\Core\\Forms\\ConsultationHandler::AJAX_ACTION,
  'mail_state' => method_exists('\\Shpigovsky\\Core\\Mail\\MailOps','state') ? \\Shpigovsky\\Core\\Mail\\MailOps::state() : null,
  'metrika_goal' => \\Shpigovsky\\Core\\Mail\\MailOps::metrika_goal(),
  'recipients_count' => count(\\Shpigovsky\\Core\\Mail\\MailOps::recipient_emails()),
);
if (class_exists('\\Shpigovsky\\Core\\Admin\\IndexingState')) {
  $out['indexing'] = \\Shpigovsky\\Core\\Admin\\IndexingState::snapshot();
}
if (class_exists('\\Shpigovsky\\Core\\Admin\\IndexingWatchdog')) {
  $out['watchdog_enabled'] = true;
}
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
"""

QA_PHP = r"""<?php
chdir('{docroot}');
if (!defined('DOING_AJAX')) { define('DOING_AJAX', true); }
require '{wp_load}';
nocache_headers();

add_filter('wp_die_ajax_handler', static function () {
  return static function ($message = '', $title = '', $args = array()) {
    // Keep multi-case CLI harness alive after wp_send_json().
  };
});
add_filter('wp_die_handler', static function () {
  return static function ($message = '', $title = '', $args = array()) {
  };
});

function fp02_as_post($fields) {
  $_POST = $fields;
  $_REQUEST = array_merge($_REQUEST, $fields);
  $_SERVER['REQUEST_METHOD'] = 'POST';
  ob_start();
  try {
    \\Shpigovsky\\Core\\Forms\\ConsultationHandler::handle_ajax();
  } catch (Throwable $e) {
    $buf = ob_get_clean();
    return array('caught'=>true,'error'=>$e->getMessage(),'buf'=>substr($buf,0,500));
  }
  $buf = ob_get_clean();
  $json = json_decode($buf, true);
  return is_array($json) ? $json : array('raw'=>substr((string)$buf,0,800));
}

$_SERVER['REMOTE_ADDR'] = '198.51.100.50';
\\Shpigovsky\\Core\\Forms\\AntiSpam::clear_rate_state_for_current_source();

$results = array();
$lead_ids = array();

function fp02_as_base($token, $fs, $extra = array()) {
  return array_merge(array(
    'action' => 'fp02_lead_submit',
    'fp02_lead_nonce' => wp_create_nonce('fp02_lead_submit'),
    'request_token' => $token,
    'fp02_fs' => $fs,
    'company_url' => '',
    'name' => 'Антиспам QA',
    'phone' => '+7 (925) 183-64-64',
    'email' => '',
    'message' => 'Синтетическая проверка антиспама FP-0002.',
    'consent' => '1',
    'form_context' => 'final',
    'lead_source' => 'antispam-qa',
    'page_url' => 'https://shpigovsky.ru/',
    'page_title' => 'QA',
    'utm_source'=>'','utm_medium'=>'','utm_campaign'=>'','utm_content'=>'','utm_term'=>'','referrer'=>'',
    'fp02_qa' => '1',
  ), $extra);
}

// Valid human (wait past MIN_ELAPSED).
$fs = \\Shpigovsky\\Core\\Forms\\AntiSpam::issue_token('consultation','final');
sleep(3);
$tok = 'qaok' . wp_generate_password(28, false, false);
$valid = fp02_as_post(fp02_as_base($tok, $fs));
$results['valid_human'] = array(
  'ok' => !empty($valid['ok']) && !empty($valid['accepted']),
  'mail_accepted' => $valid['mail_accepted'] ?? null,
  'mail_status' => $valid['mail_status'] ?? null,
  'message' => $valid['message'] ?? null,
);
if (!empty($valid['accepted'])) {
  global $wpdb;
  $table = \\Shpigovsky\\Core\\Leads\\LeadRegistry::table_name();
  $id = (int) $wpdb->get_var("SELECT id FROM {$table} WHERE is_qa=1 ORDER BY id DESC LIMIT 1");
  if ($id > 0) { $lead_ids[] = $id; }
}

// Honeypot
$fs2 = \\Shpigovsky\\Core\\Forms\\AntiSpam::issue_token('consultation','final');
sleep(3);
$hp = fp02_as_post(fp02_as_base('qahp'.wp_generate_password(28,false,false), $fs2, array('company_url'=>'http://spam.example')));
$results['honeypot'] = array(
  'rejected' => empty($hp['ok']),
  'accepted' => !empty($hp['accepted']),
  'message' => $hp['message'] ?? null,
);

// Too fast
$fs3 = \\Shpigovsky\\Core\\Forms\\AntiSpam::issue_token('consultation','final');
$fast = fp02_as_post(fp02_as_base('qafast'.wp_generate_password(28,false,false), $fs3));
$results['too_fast'] = array(
  'rejected' => empty($fast['ok']),
  'accepted' => !empty($fast['accepted']),
  'message' => $fast['message'] ?? null,
);

// Tampered token
$fs4 = \\Shpigovsky\\Core\\Forms\\AntiSpam::issue_token('consultation','final');
sleep(3);
$tampered = $fs4 . 'x';
$tamp = fp02_as_post(fp02_as_base('qatamp'.wp_generate_password(28,false,false), $tampered));
$results['tampered_token'] = array(
  'rejected' => empty($tamp['ok']),
  'accepted' => !empty($tamp['accepted']),
);

// Expired token via reflection of payload age — craft expired by issuing then rewriting is hard without private API.
// Use verify path: temporarily issue then call evaluate with forged old token using signing.
$expired_payload = array('iat'=>time()-10000,'ft'=>'consultation','fc'=>'final','n'=>'expiredqa01');
$body = rtrim(strtr(base64_encode(wp_json_encode($expired_payload)),'+/','-_'),'=');
$key = (defined('AUTH_KEY') && AUTH_KEY) ? (AUTH_KEY.'|fp02-form-antispam-v1') : (wp_salt('auth').'|fp02-form-antispam-v1');
$sig = rtrim(strtr(base64_encode(hash_hmac('sha256',$body,$key,true)),'+/','-_'),'=');
$expired_tok = $body.'.'.$sig;
$exp = fp02_as_post(fp02_as_base('qaexp'.wp_generate_password(28,false,false), $expired_tok));
$results['expired_token'] = array(
  'rejected' => empty($exp['ok']),
  'accepted' => !empty($exp['accepted']),
  'message' => $exp['message'] ?? null,
);

// Replay accepted token
\\Shpigovsky\\Core\\Forms\\AntiSpam::clear_rate_state_for_current_source();
$fs5 = \\Shpigovsky\\Core\\Forms\\AntiSpam::issue_token('consultation','final');
sleep(3);
$replay_tok = 'qareplay'.wp_generate_password(24,false,false);
$first = fp02_as_post(fp02_as_base($replay_tok, $fs5, array('message'=>'Повторный тест idempotency.')));
$second = fp02_as_post(fp02_as_base($replay_tok, $fs5, array('message'=>'Повторный тест idempotency.')));
$results['replay'] = array(
  'first_accepted' => !empty($first['accepted']),
  'second_rejected' => empty($second['ok']),
  'second_message' => $second['message'] ?? null,
  'first_message' => $first['message'] ?? null,
);
if (!empty($first['accepted'])) {
  global $wpdb;
  $table = \\Shpigovsky\\Core\\Leads\\LeadRegistry::table_name();
  $id = (int) $wpdb->get_var("SELECT id FROM {$table} WHERE is_qa=1 ORDER BY id DESC LIMIT 1");
  if ($id > 0) { $lead_ids[] = $id; }
}

// Heuristics matrix (no persist for rejects; one soft pass without persist via evaluate only)
$heur = array();
$cases = array(
  'A_normal_ru' => array('name'=>'Иван Петров','message'=>'Нужна консультация по разводу и опеке.'),
  'B_multiline' => array('name'=>'Мария','message'=>"Здравствуйте,\nнужна помощь.\nСпасибо."),
  'C_one_url' => array('name'=>'Олег','message'=>'Смотрел информацию на https://shpigovsky.ru/uslugi/ — хочу записаться.'),
  'D_spam_urls' => array('name'=>'Bot','message'=>"http://a.com http://b.com http://c.com http://d.com http://e.com"),
  'E_giant' => array('name'=>'Bot','message'=>str_repeat('СПАМ ', 900)),
  'F_script' => array('name'=>'Bot','message'=>'<script>alert(1)</script> купите аптеку'),
  'G_cyrillic' => array('name'=>'Екатерина Смирнова','message'=>'Интересует лечение зависимости, сроки и стоимость.'),
  'H_intl_phone_ok' => array('name'=>'Alex','phone'=>'+79251836464','message'=>'Please call back tomorrow.'),
);
foreach ($cases as $cid => $c) {
  $payload = array(
    'name' => $c['name'],
    'phone' => $c['phone'] ?? '+7 (925) 183-64-64',
    'email' => '',
    'message' => $c['message'],
    'consent' => '1',
    'form_context' => 'final',
    'lead_source' => 'heur',
    'page_url' => 'https://shpigovsky.ru/',
    'page_title' => 'h',
    'utm_source'=>'','utm_medium'=>'','utm_campaign'=>'','utm_content'=>'','utm_term'=>'','referrer'=>'',
    'is_qa' => true,
  );
  $ev = \\Shpigovsky\\Core\\Forms\\AntiSpam::evaluate(array('company_url'=>''), $payload);
  $heur[$cid] = array('ok'=>$ev['ok'], 'reason'=>$ev['reason']);
}
$results['heuristics'] = $heur;

// Direct POST missing token
$direct = fp02_as_post(fp02_as_base('qadir'.wp_generate_password(28,false,false), ''));
$results['direct_missing_token'] = array(
  'rejected' => empty($direct['ok']),
  'accepted' => !empty($direct['accepted']),
);

// Count leads created by QA markers then delete exact QA rows
$deleted = (int) \\Shpigovsky\\Core\\Leads\\LeadRegistry::delete_qa_rows();
$results['cleanup'] = array('deleted'=>$deleted);
$results['indexing'] = array(
  'blog_public' => (int) get_option('blog_public'),
  'effective' => class_exists('\\Shpigovsky\\Core\\Admin\\IndexingState') ? (\\Shpigovsky\\Core\\Admin\\IndexingState::snapshot()['effective'] ?? null) : null,
);
$results['core'] = defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null;
$results['antispam_admin'] = \\Shpigovsky\\Core\\Forms\\AntiSpam::admin_status();
$results['smtp_recipients'] = count(\\Shpigovsky\\Core\\Mail\\MailOps::recipient_emails());
$results['mail_state'] = \\Shpigovsky\\Core\\Mail\\MailOps::state();

echo 'FP02_AS_RESULTS:';
echo wp_json_encode($results, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
"""

RATE_PHP = r"""<?php
chdir('{docroot}');
require '{wp_load}';
$_SERVER['REMOTE_ADDR'] = '203.0.113.77';
$_SERVER['REQUEST_METHOD'] = 'POST';
$fs = \\Shpigovsky\\Core\\Forms\\AntiSpam::issue_token('consultation','final');
sleep(3);
$out = array('bursts'=>array());
for ($i=0; $i<10; $i++) {
  if ($i > 0) {
    \\Shpigovsky\\Core\\Forms\\AntiSpam::bump_attempt();
  }
  $ev = \\Shpigovsky\\Core\\Forms\\AntiSpam::evaluate(array(
    'company_url'=>'',
    'fp02_fs'=>$fs,
  ), array());
  $out['bursts'][] = array('i'=>$i,'ok'=>$ev['ok'],'reason'=>$ev['reason']);
}
$key = (defined('AUTH_KEY')&&AUTH_KEY)?(AUTH_KEY.'|fp02-form-antispam-v1'):(wp_salt('auth').'|fp02-form-antispam-v1');
$fp = substr(hash_hmac('sha256','203.0.113.77', $key),0,32);
delete_transient('fp02_as_s_'.$fp);
delete_transient('fp02_as_m_'.$fp);
$out['cleaned'] = true;
$out['saw_rate_limit'] = false;
foreach ($out['bursts'] as $b) {
  if (!$b['ok'] && $b['reason']==='RATE_LIMIT') { $out['saw_rate_limit']=true; }
}
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
"""


def fill_php(template: str) -> str:
    # Templates are Python raw strings; namespace FQCNs therefore contain doubled
    # backslashes. Collapse pairs so PHP sees valid \Namespace\Class references
    # and class_exists('...') strings still resolve to a leading backslash.
    text = template.replace("{wp_load}", WP_LOAD).replace("{docroot}", DOCROOT)
    while "\\\\" in text:
        text = text.replace("\\\\", "\\")
    return text


def http_form_probe() -> dict[str, Any]:
    urls = [
        "https://shpigovsky.ru/",
        "https://shpigovsky.ru/kontakty/",
        "https://shpigovsky.ru/uslugi/",
    ]
    out = {}
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "FP02-AntispamQA/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            out[url] = {
                "status": getattr(resp, "status", 200),
                "has_lead_form": 'data-lead-form' in html,
                "has_fp02_fs": 'name="fp02_fs"' in html or "name='fp02_fs'" in html,
                "has_company_url": 'name="company_url"' in html,
                "has_g_recaptcha_field": "g-recaptcha-response" in html,
                "has_form_started_at": "form_started_at" in html,
                "has_google_recaptcha_script": "google.com/recaptcha" in html,
            }
        except Exception as exc:  # noqa: BLE001
            out[url] = {"error": str(exc)}
    return out


def deploy_files(ctx: RuntimeContext) -> list[dict[str, Any]]:
    results = []
    for rel, local in DEPLOY_MAP.items():
        remote = remote_for(rel)
        local_bytes = local.read_bytes()
        before = ctx.sftp_get(remote)
        ctx.sftp_put_bytes(remote, local_bytes)
        after = ctx.sftp_get(remote)
        results.append(
            {
                "rel": rel,
                "remote": remote,
                "local_sha256": sha256_bytes(local_bytes),
                "before_sha256": sha256_bytes(before) if before else None,
                "after_sha256": sha256_bytes(after) if after else None,
                "match": after == local_bytes,
            }
        )
    return results


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        pre = ctx.run_php_remote(fill_php(INTAKE_PHP), "intake_pre")
        write_json("01-pre-intake.json", pre)

        # Pre hashes
        pre_hashes = {}
        for rel, local in DEPLOY_MAP.items():
            remote = remote_for(rel)
            remote_bytes = ctx.sftp_get(remote)
            pre_hashes[rel] = {
                "local_sha256": sha256_bytes(local.read_bytes()),
                "prod_sha256": sha256_bytes(remote_bytes) if remote_bytes else None,
            }
        write_json("01b-pre-hashes.json", pre_hashes)

        deploy = deploy_files(ctx)
        write_json("02-deploy-manifest.json", deploy)

        post = ctx.run_php_remote(fill_php(INTAKE_PHP), "intake_post")
        write_json("03-post-intake.json", post)

        qa = ctx.run_php_remote(fill_php(QA_PHP), "qa_matrix")
        write_json("04-qa-matrix.json", qa)

        rate = ctx.run_php_remote(fill_php(RATE_PHP), "rate")
        write_json("05-rate-limit-qa.json", rate)

        probes = http_form_probe()
        write_json("06-public-form-probe.json", probes)

        parity_ok = all(x["match"] for x in deploy)
        qa_data = qa.get("data") if isinstance(qa.get("data"), dict) else {}
        indexing = qa_data.get("indexing") or {}
        indexing_open = (int(indexing.get("blog_public") or 0) == 1) or (
            indexing.get("effective") == "OPEN"
        )

        valid_ok = bool((qa_data.get("valid_human") or {}).get("ok"))
        honey_ok = bool((qa_data.get("honeypot") or {}).get("rejected")) and not bool(
            (qa_data.get("honeypot") or {}).get("accepted")
        )
        fast_ok = bool((qa_data.get("too_fast") or {}).get("rejected"))
        tamp_ok = bool((qa_data.get("tampered_token") or {}).get("rejected"))
        exp_ok = bool((qa_data.get("expired_token") or {}).get("rejected"))
        replay_ok = bool((qa_data.get("replay") or {}).get("first_accepted")) and bool(
            (qa_data.get("replay") or {}).get("second_rejected")
        )
        direct_ok = bool((qa_data.get("direct_missing_token") or {}).get("rejected"))
        heur = qa_data.get("heuristics") or {}
        heur_ok = (
            bool((heur.get("A_normal_ru") or {}).get("ok"))
            and bool((heur.get("B_multiline") or {}).get("ok"))
            and bool((heur.get("C_one_url") or {}).get("ok"))
            and bool((heur.get("G_cyrillic") or {}).get("ok"))
            and bool((heur.get("H_intl_phone_ok") or {}).get("ok"))
            and not bool((heur.get("D_spam_urls") or {}).get("ok"))
            and not bool((heur.get("E_giant") or {}).get("ok"))
            and not bool((heur.get("F_script") or {}).get("ok"))
        )

        no_captcha = all(
            (not isinstance(v, dict))
            or (
                not v.get("has_g_recaptcha_field")
                and not v.get("has_google_recaptcha_script")
                and not v.get("has_form_started_at")
            )
            for v in probes.values()
        )

        core = (post.get("data") or {}).get("core") if post.get("ok") else qa_data.get("core")
        summary = {
            "captured_at": utcnow(),
            "parity_ok": parity_ok,
            "core": core,
            "indexing_open_ok": indexing_open,
            "valid_human_ok": valid_ok,
            "honeypot_ok": honey_ok,
            "too_fast_ok": fast_ok,
            "tampered_ok": tamp_ok,
            "expired_ok": exp_ok,
            "replay_ok": replay_ok,
            "direct_ok": direct_ok,
            "heuristics_ok": heur_ok,
            "no_external_captcha_ok": no_captcha,
            "cleanup_deleted": (qa_data.get("cleanup") or {}).get("deleted"),
        }
        write_json("00-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        ok = all(
            [
                parity_ok,
                indexing_open,
                valid_ok,
                honey_ok,
                fast_ok,
                tamp_ok,
                exp_ok,
                replay_ok,
                direct_ok,
                heur_ok,
                no_captcha,
                core == "0.3.24-antispam",
            ]
        )
        return 0 if ok else 2
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())
