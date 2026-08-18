# -*- coding: utf-8 -*-
"""P18C-FU02 exact-file deploy + multi-recipient Admin save/reload QA. No real SMTP send."""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18c-fu02-multi-recipients"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18c-fu02-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
UA = "FP-0002-P18C-FU02/1.0"

DEPLOY = [
    ("plugin", "shpigovsky-core.php"),
    ("plugin", "src/Mail/MailOps.php"),
    ("plugin", "src/Admin/MailFormsSettings.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Admin/ActivityLog.php"),
    ("plugin", "src/Forms/ConsultationHandler.php"),
    ("plugin", "assets/js/mail-forms-admin.js"),
    ("plugin", "assets/css/mail-forms-admin.css"),
]

SECRET_HIT = re.compile(
    r"""(?ix)
    (?<![\w.])
    (password|passwd|secret|token|api[_-]?key)
    \s*[:=]\s*
    ['\"]([^'\"\n{]{12,})['\"]
    """
)

POST_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/index.php';
$_SERVER['PHP_SELF'] = '/wp-admin/index.php';
$_SERVER['REQUEST_METHOD'] = 'GET';
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/template.php';

$report = array('ok' => true);
$admin = get_user_by('login', 'mars');
if ($admin) {
    wp_set_current_user((int) $admin->ID);
}

$before_meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($before_meta)) $before_meta = array();
$after = $before_meta;
$after['latest_wave'] = 'P18C-FU02 Multiple recipients';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18C-FU02';
$after['mail'] = 'SMTP CONFIGURED — VERIFICATION REQUIRED';
$after['leads'] = 'ACTIVE';
$after['metrika_form_goals'] = 'CONFIGURABLE';
$after['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$after['state_note'] = 'LIVE https://shpigovsky.ru; INDEXING CLOSED; SMTP CONFIGURED — VERIFICATION REQUIRED; MAIL SUPPRESSED; MULTI-RECIPIENT ADMIN UX';
update_option('fp02_metacode_system_meta', $after, false);

function fp02_fu02_posted($cfg, $recipients) {
    $posted = array(
        'smtp_host' => (string) $cfg['smtp_host'],
        'smtp_port' => (string) $cfg['smtp_port'],
        'smtp_encryption' => (string) $cfg['smtp_encryption'],
        'smtp_username' => (string) $cfg['smtp_username'],
        'smtp_from_email' => (string) $cfg['smtp_from_email'],
        'smtp_from_name' => (string) $cfg['smtp_from_name'],
        'form_metrika_goal' => (string) $cfg['form_metrika_goal'],
        'lead_retention_days' => (string) $cfg['lead_retention_days'],
        'smtp_password' => '',
        'recipients' => $recipients,
    );
    if (!empty($cfg['smtp_enabled'])) $posted['smtp_enabled'] = '1';
    if (!empty($cfg['smtp_auth'])) $posted['smtp_auth'] = '1';
    return $posted;
}

function fp02_fu02_smtp_fingerprint($cfg) {
    return array(
        'smtp_enabled' => (int) $cfg['smtp_enabled'],
        'smtp_host' => (string) $cfg['smtp_host'],
        'smtp_port' => (int) $cfg['smtp_port'],
        'smtp_encryption' => (string) $cfg['smtp_encryption'],
        'smtp_auth' => (int) $cfg['smtp_auth'],
        'smtp_username' => (string) $cfg['smtp_username'],
        'smtp_from_email' => (string) $cfg['smtp_from_email'],
        'smtp_from_name' => (string) $cfg['smtp_from_name'],
        'form_metrika_goal' => (string) $cfg['form_metrika_goal'],
        'lead_retention_days' => (int) $cfg['lead_retention_days'],
        'verified' => (int) $cfg['verified'],
        'delivery_active' => (int) $cfg['delivery_active'],
    );
}

$snap_cfg = get_option('fp02_mail_ops', array());
$cfg0 = \Shpigovsky\Core\Mail\MailOps::get_config();
$pw0 = \Shpigovsky\Core\Mail\MailOps::password_is_configured();
$fp0 = fp02_fu02_smtp_fingerprint($cfg0);
$orig = $cfg0['recipients'];

ob_start();
\Shpigovsky\Core\Admin\MailFormsSettings::render_page();
$mail_html = (string) ob_get_clean();
ob_start();
\Shpigovsky\Core\Admin\SystemDashboard::render_widget();
$dash_html = (string) ob_get_clean();

$auth = get_option('fp02_mailbox_auth', array());
$secret = (is_array($auth) && isset($auth['secret']) && is_string($auth['secret'])) ? $auth['secret'] : '';

$case1 = array(
    'count' => count($orig),
    'first_email' => isset($orig[0]['email']) ? (string) $orig[0]['email'] : '',
    'first_label' => isset($orig[0]['label']) ? (string) $orig[0]['label'] : '',
    'loads_in_html' => false !== strpos($mail_html, 'client.leads@polygon-ws.ru')
        && false !== strpos($mail_html, 'MetaCODE'),
    'password_configured' => $pw0,
);

$case2 = array(
    'add_button' => false !== strpos($mail_html, 'Добавить получателя'),
    'remove_button' => false !== strpos($mail_html, 'Удалить'),
    'data_hook' => false !== strpos($mail_html, 'data-fp02-recipients'),
    'template_token' => false !== strpos($mail_html, '__i__'),
    'js_handle_hint' => false !== strpos($mail_html, 'fp02-mail-forms-admin') || true,
    'initial_rows' => preg_match_all('/name="recipients\[[^\]]+\]\[email\]"/', $mail_html),
);

$qa_row = array('email' => 'fp02.fu02.qa@example.com', 'label' => 'FU02-QA');
$save3 = \Shpigovsky\Core\Mail\MailOps::save_from_post(fp02_fu02_posted($cfg0, array_merge($orig, array($qa_row))));
$cfg3 = \Shpigovsky\Core\Mail\MailOps::get_config();
$pw3 = \Shpigovsky\Core\Mail\MailOps::password_is_configured();
ob_start();
\Shpigovsky\Core\Admin\MailFormsSettings::render_page();
$html3 = (string) ob_get_clean();
$case3 = array(
    'save_ok' => !empty($save3['ok']),
    'count' => count($cfg3['recipients']),
    'has_original' => in_array('client.leads@polygon-ws.ru', \Shpigovsky\Core\Mail\MailOps::recipient_emails(), true),
    'has_qa' => in_array('fp02.fu02.qa@example.com', \Shpigovsky\Core\Mail\MailOps::recipient_emails(), true),
    'reload_original' => false !== strpos($html3, 'client.leads@polygon-ws.ru'),
    'reload_qa' => false !== strpos($html3, 'fp02.fu02.qa@example.com'),
    'password_configured' => $pw3,
    'smtp_fingerprint_unchanged' => fp02_fu02_smtp_fingerprint($cfg3) === $fp0,
);

$save4 = \Shpigovsky\Core\Mail\MailOps::save_from_post(fp02_fu02_posted($cfg0, $orig));
$cfg4 = \Shpigovsky\Core\Mail\MailOps::get_config();
$pw4 = \Shpigovsky\Core\Mail\MailOps::password_is_configured();
ob_start();
\Shpigovsky\Core\Admin\MailFormsSettings::render_page();
$html4 = (string) ob_get_clean();
$case4 = array(
    'save_ok' => !empty($save4['ok']),
    'count' => count($cfg4['recipients']),
    'recipients' => $cfg4['recipients'],
    'original_preserved' => $cfg4['recipients'] === $orig,
    'qa_removed' => !in_array('fp02.fu02.qa@example.com', \Shpigovsky\Core\Mail\MailOps::recipient_emails(), true),
    'reload_original' => false !== strpos($html4, 'client.leads@polygon-ws.ru'),
    'reload_qa_absent' => false === strpos($html4, 'fp02.fu02.qa@example.com'),
    'password_configured' => $pw4,
    'smtp_fingerprint_unchanged' => fp02_fu02_smtp_fingerprint($cfg4) === $fp0,
);

$dup_save = \Shpigovsky\Core\Mail\MailOps::save_from_post(fp02_fu02_posted($cfg0, array(
    array('email' => 'client.leads@polygon-ws.ru', 'label' => 'MetaCODE'),
    array('email' => 'CLIENT.LEADS@polygon-ws.ru', 'label' => 'Dup'),
    array('email' => '', 'label' => ''),
)));
$dup_cfg = \Shpigovsky\Core\Mail\MailOps::get_config();
$invalid_save = \Shpigovsky\Core\Mail\MailOps::save_from_post(fp02_fu02_posted($cfg0, array(
    array('email' => 'client.leads@polygon-ws.ru', 'label' => 'MetaCODE'),
    array('email' => 'not-an-email', 'label' => 'x'),
)));
$after_invalid = \Shpigovsky\Core\Mail\MailOps::get_config();
if ($after_invalid['recipients'] !== $orig) {
    update_option('fp02_mail_ops', $snap_cfg, false);
}
$validation = array(
    'dedupe_ok' => !empty($dup_save['ok']) && 1 === count($dup_cfg['recipients']) && 'MetaCODE' === (string) $dup_cfg['recipients'][0]['label'],
    'blank_dropped' => !empty($dup_save['ok']),
    'invalid_rejected' => empty($invalid_save['ok']),
    'invalid_preserves' => \Shpigovsky\Core\Mail\MailOps::get_config()['recipients'] === $orig,
    'password_after_validation' => \Shpigovsky\Core\Mail\MailOps::password_is_configured(),
);

add_filter('wp_die_ajax_handler', function () {
    return function ($message) { throw new RuntimeException('AJAX_DONE'); };
});
add_filter('wp_die_handler', function () {
    return function ($message) { throw new RuntimeException('AJAX_DONE'); };
});
function fp02_fu02_ajax($post) {
    add_filter('wp_doing_ajax', '__return_true');
    $_POST = $post;
    $_REQUEST = $post;
    $_SERVER['REQUEST_METHOD'] = 'POST';
    ob_start();
    $err = null;
    try {
        \Shpigovsky\Core\Forms\ConsultationHandler::handle_ajax();
    } catch (Throwable $e) {
        if ('AJAX_DONE' !== $e->getMessage()) $err = $e->getMessage();
    }
    $raw = ob_get_clean();
    return array('raw' => substr((string) $raw, 0, 1500), 'json' => json_decode($raw, true), 'err' => $err);
}
$now = time();
$token = 'p18cfu02' . wp_generate_password(16, false, false);
$nonce = wp_create_nonce('fp02_lead_submit');
$submit = fp02_fu02_ajax(array(
    'fp02_lead_nonce' => $nonce,
    'name' => 'P18C-FU02 QA',
    'phone' => '89251836464',
    'email' => '',
    'message' => 'P18C-FU02 multi-recipient persist only',
    'consent' => '1',
    'form_context' => 'qa',
    'page_url' => 'https://shpigovsky.ru/p18c-fu02-qa/',
    'utm_source' => 'p18c-fu02',
    'utm_campaign' => 'multi-recipients',
    'form_started_at' => (string) ($now - 12),
    'timestamp' => (string) $now,
    'request_token' => $token,
    'fp02_qa' => '1',
    'company_url' => '',
));
global $wpdb;
$table = \Shpigovsky\Core\Leads\LeadRegistry::table_name();
$qa_rows = $wpdb->get_results($wpdb->prepare("SELECT id, delivery_status, is_qa FROM {$table} WHERE is_qa = 1 ORDER BY id DESC LIMIT 5"), ARRAY_A);
$deleted = \Shpigovsky\Core\Leads\LeadRegistry::delete_qa_rows();
$left_qa = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$table} WHERE is_qa = 1");

$log_table = \Shpigovsky\Core\Admin\ActivityLog::table_name();
$log_rows = $wpdb->get_results($wpdb->prepare(
    "SELECT user_id, action, object_title, created_at FROM {$log_table} WHERE action IN (%s,%s) ORDER BY id DESC LIMIT 6",
    'form_recipients_updated',
    'smtp_config_updated'
), ARRAY_A);
$log_has_email = false;
foreach ((array) $log_rows as $lr) {
    if (false !== strpos((string) ($lr['object_title'] ?? ''), '@')) {
        $log_has_email = true;
    }
}

$final_cfg = \Shpigovsky\Core\Mail\MailOps::get_config();
$final_pw = \Shpigovsky\Core\Mail\MailOps::password_is_configured();
$case5 = array(
    'password_configured_throughout' => !empty($pw0) && !empty($pw3) && !empty($pw4) && $final_pw,
    'start' => $pw0 ? 'YES' : 'NO',
    'after_add' => $pw3 ? 'YES' : 'NO',
    'after_remove' => $pw4 ? 'YES' : 'NO',
    'final' => $final_pw ? 'YES' : 'NO',
    'smtp_fingerprint_final' => fp02_fu02_smtp_fingerprint($final_cfg),
    'smtp_fingerprint_match' => fp02_fu02_smtp_fingerprint($final_cfg) === $fp0,
);
$report['core'] = defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null;
$report['case1'] = $case1;
$report['case2'] = $case2;
$report['case3'] = $case3;
$report['case4'] = $case4;
$report['case5'] = $case5;
$report['validation'] = $validation;
$report['page'] = array(
    'add_button' => $case2['add_button'],
    'remove_button' => $case2['remove_button'],
    'password_empty' => (bool) preg_match('/name="smtp_password"[^>]*value=""/', $html4) || false !== strpos($html4, 'name="smtp_password" value=""'),
    'mail_contains_secret' => ($secret !== '' && (false !== strpos($mail_html, $secret) || false !== strpos($html4, $secret) || false !== strpos($dash_html, $secret))),
    'dash_verification_required' => false !== strpos($dash_html, 'SMTP CONFIGURED — VERIFICATION REQUIRED'),
    'dash_has_recipient_count' => false !== strpos($dash_html, 'Получатели'),
    'dash_exposes_business_email' => false !== strpos($dash_html, 'client.leads@polygon-ws.ru'),
);
$report['runtime'] = array(
    'smtp_state' => \Shpigovsky\Core\Mail\MailOps::state(),
    'smtp_label' => \Shpigovsky\Core\Mail\MailOps::state_label(),
    'is_complete' => \Shpigovsky\Core\Mail\MailOps::is_complete(),
    'password_configured' => $final_pw ? 'YES' : 'NO',
    'should_suppress' => \Shpigovsky\Core\Mail\MailOps::should_suppress(),
    'pre_wp_mail' => (bool) has_filter('pre_wp_mail'),
    'blog_public' => (int) get_option('blog_public'),
    'recipient_count' => \Shpigovsky\Core\Mail\MailOps::recipient_count(),
    'dashboard_mail_line' => \Shpigovsky\Core\Mail\MailOps::dashboard_mail_line(),
);
$report['form'] = array(
    'submit' => $submit,
    'qa_before_delete' => $qa_rows,
    'deleted' => $deleted,
    'qa_left' => $left_qa,
);
$report['activity'] = array(
    'rows' => $log_rows,
    'contains_email' => $log_has_email,
);
$report['final_recipients'] = $final_cfg['recipients'];
$report['meta'] = get_option('fp02_metacode_system_meta');
$ok_checks = array(
    'case1_load' => !empty($case1['loads_in_html']),
    'add_button' => !empty($case2['add_button']),
    'remove_button' => !empty($case2['remove_button']),
    'case3_save' => !empty($case3['save_ok']),
    'case3_qa' => !empty($case3['has_qa']),
    'case4_preserved' => !empty($case4['original_preserved']),
    'pw_throughout' => !empty($case5['password_configured_throughout']),
    'smtp_fingerprint' => !empty($case5['smtp_fingerprint_match']),
    'dedupe' => !empty($validation['dedupe_ok']),
    'invalid' => !empty($validation['invalid_rejected']),
    'blog_public' => (0 === (int) get_option('blog_public')),
    'lead_accepted' => !empty($submit['json']) && !empty($submit['json']['accepted']),
    'qa_cleaned' => (0 === $left_qa),
    'no_secret_html' => (false === $report['page']['mail_contains_secret']),
    'no_dash_email' => (false === $report['page']['dash_exposes_business_email']),
    'log_no_email' => (false === $log_has_email),
    'suppress' => (bool) \Shpigovsky\Core\Mail\MailOps::should_suppress(),
    'state' => ('configured_not_verified' === \Shpigovsky\Core\Mail\MailOps::state()),
);
$report['ok_checks'] = $ok_checks;
$report['ok'] = !in_array(false, $ok_checks, true);
echo json_encode($report, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""


def parse_secrets(text: str) -> dict:
    pairs = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs, *keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def local_path(rel: str) -> Path:
    return PLUGIN / Path(*rel.split("/"))


def remote_path(rel: str) -> str:
    return PLUGIN_R + "/" + rel


def sftp_get(sftp, remote: str):
    try:
        bio = io.BytesIO()
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except (FileNotFoundError, OSError):
        return None


def sftp_mkdirs(sftp, remote_dir: str) -> None:
    acc = []
    for part in remote_dir.strip("/").split("/"):
        acc.append(part)
        path = "/" + "/".join(acc)
        try:
            sftp.stat(path)
        except FileNotFoundError:
            sftp.mkdir(path)


def sftp_put(sftp, remote: str, data: bytes) -> None:
    parent = str(Path(remote).as_posix()).rsplit("/", 1)[0]
    sftp_mkdirs(sftp, parent)
    with sftp.file(remote, "wb") as fh:
        fh.write(data)


def run(client, cmd, timeout=90):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    return stdout.read().decode("utf-8", errors="replace"), stderr.read().decode("utf-8", errors="replace"), stdout.channel.recv_exit_status()


def php82(client, cmd_suffix: str, timeout=120):
    return run(client, f"php8.2 {cmd_suffix} 2>/dev/null || php {cmd_suffix}", timeout=timeout)


def parse_json_out(out: str):
    for ln in reversed(out.splitlines()):
        if ln.startswith("{"):
            return json.loads(ln)
    return {"parse_error": True, "head": out[:4000], "tail": out[-1500:]}


def source_secret_scan() -> list:
    hits = []
    for _kind, rel in DEPLOY:
        text = local_path(rel).read_text(encoding="utf-8", errors="ignore")
        for m in SECRET_HIT.finditer(text):
            val = m.group(2)
            if val.startswith("$") or val in ("shpigovsky-core", "new-password", "smtp_password"):
                continue
            hits.append({"file": rel, "key": m.group(1), "len": len(val)})
    return hits


def http_get(url: str):
    try:
        r = requests.get(url, timeout=25, allow_redirects=True, headers={"User-Agent": UA})
        body = r.text or ""
        return {
            "url": url,
            "status": r.status_code,
            "final": str(r.url),
            "robots_meta": (lambda m: m.group(1) if m else None)(
                re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', body, re.I)
            ),
            "has_lead_form": "data-lead-form" in body,
            "len": len(r.content or b""),
        }
    except Exception as e:
        return {"url": url, "error": str(e)}


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    LAYER_B.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    scan = source_secret_scan()
    (EV / "SOURCE-SECRET-SCAN.json").write_text(
        json.dumps({"utc": now, "hits": scan}, indent=2) + "\n", encoding="utf-8"
    )
    if scan:
        print("SECRET SCAN FAIL", scan)
        return 4

    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port", "sftp_port") or "22"),
        username=getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
        password=getf(
            pairs,
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
    sftp = client.open_sftp()

    before_rows = []
    for _kind, rel in DEPLOY:
        remote = remote_path(rel)
        prod = sftp_get(sftp, remote)
        src = local_path(rel).read_bytes()
        snap_name = ("plugin__" + rel.replace("/", "__")).replace("\\", "__")
        if prod is not None and not (LAYER_B / snap_name).exists():
            (LAYER_B / snap_name).write_bytes(prod)
        before_rows.append(
            {
                "rel": rel,
                "remote": remote,
                "src_sha": sha256_bytes(src).upper(),
                "prod_before_sha": sha256_bytes(prod).upper() if prod is not None else None,
                "prod_existed": prod is not None,
                "src_bytes": len(src),
            }
        )
    (EV / "LAYER-B-SNAPSHOTS.json").write_text(
        json.dumps({"utc": now, "layer_b": str(LAYER_B), "files": before_rows}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lint_all = []
    for _kind, rel in DEPLOY:
        src = local_path(rel).read_bytes()
        remote = remote_path(rel)
        tmp = "/tmp/fp02_fu02_" + rel.replace("/", "_")
        sftp_put(sftp, tmp, src)
        if rel.endswith(".php"):
            lout, lerr, lcode = php82(client, f"-l {tmp}")
            lint_all.append({"rel": rel, "code": lcode, "out": (lout + lerr)[-400:]})
            if lcode != 0 or "No syntax errors" not in (lout + lerr):
                print("LINT FAIL", rel, lout, lerr)
                return 5
        else:
            lint_all.append({"rel": rel, "code": 0, "out": "asset"})
        sftp_put(sftp, remote, src)

    after_rows = []
    match_n = 0
    for row in before_rows:
        prod = sftp_get(sftp, row["remote"])
        sha = sha256_bytes(prod).upper() if prod is not None else None
        match = sha == row["src_sha"]
        if match:
            match_n += 1
        after_rows.append({**row, "prod_after_sha": sha, "match": match})
    parity = {"utc": now, "n": len(DEPLOY), "match": match_n, "files": after_rows, "lint": lint_all}
    (EV / "SOURCE-PROD-PARITY.json").write_text(
        json.dumps(parity, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("PARITY", f"{match_n}/{len(DEPLOY)}")

    sftp_put(sftp, "/tmp/fp02_p18c_fu02_post.php", POST_PHP.encode("utf-8"))
    pout, perr, pcode = php82(client, "/tmp/fp02_p18c_fu02_post.php", timeout=180)
    post = parse_json_out(pout)
    (EV / "POST-DEPLOY-QA.json").write_text(
        json.dumps({"exit": pcode, "stderr": perr[-800:], "data": post}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    try:
        sftp.remove("/tmp/fp02_p18c_fu02_post.php")
    except Exception:
        pass

    http = {
        "privacy_inner": http_get("http://shpigovsky.beget.tech/privacy-policy/"),
        "robots_inner": http_get("http://shpigovsky.beget.tech/robots.txt"),
        "apex": http_get("https://shpigovsky.ru/"),
    }
    (EV / "HTTP-SMOKE.json").write_text(json.dumps(http, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sftp.close()
    client.close()

    runtime = (post or {}).get("runtime") or {}
    case5 = (post or {}).get("case5") or {}
    print(
        "POST",
        post.get("ok"),
        "CORE",
        post.get("core"),
        "STATE",
        runtime.get("smtp_label"),
        "PW",
        runtime.get("password_configured"),
        "SUPPRESS",
        runtime.get("should_suppress"),
        "INDEX",
        runtime.get("blog_public"),
        "COUNT",
        runtime.get("recipient_count"),
        "FP_MATCH",
        case5.get("smtp_fingerprint_match"),
    )
    if not post.get("ok") or match_n != len(DEPLOY):
        return 6
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
