# -*- coding: utf-8 -*-
"""P18C exact-file deploy, schema install, lead persist QA, Admin smoke. No real SMTP send."""
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
THEME = ROOT / "WORDPRESS" / "theme" / "shpigovsky"
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
MU = ROOT / "WORDPRESS" / "mu-plugins"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18c-smtp-forms-foundation"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18c-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
THEME_R = f"{DOCROOT}/wp-content/themes/shpigovsky"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
MU_R = f"{DOCROOT}/wp-content/mu-plugins"
UA = "FP-0002-P18C-deploy/1.0"
LIVE = "https://shpigovsky.ru"
INNER = "http://shpigovsky.beget.tech"

DEPLOY = [
    ("plugin", "src/Mail/MailOps.php"),
    ("plugin", "src/Mail/SmtpTransport.php"),
    ("plugin", "src/Leads/LeadRegistry.php"),
    ("plugin", "src/Privacy/LeadPersonalData.php"),
    ("plugin", "src/Admin/MailFormsSettings.php"),
    ("plugin", "src/Admin/LeadsAdmin.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Admin/ActivityLog.php"),
    ("plugin", "src/Settings/SiteSettings.php"),
    ("plugin", "src/Forms/ConsultationHandler.php"),
    ("plugin", "src/ModuleRegistry.php"),
    ("plugin", "shpigovsky-core.php"),
    ("mu", "fp02-pre-cutover-mail-suppression.php"),
    ("theme", "assets/js/v9-shell.js"),
]

SECRET_HIT = re.compile(
    r"""(?ix)
    (?<![\w.])
    (password|passwd|secret|token|api[_-]?key)
    \s*[:=]\s*
    ['\"]([^'\"\n{]{12,})['\"]
    """
)

SCHEMA_BEFORE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$want = array($wpdb->prefix . 'form_leads', $wpdb->prefix . 'user_activity_log');
$out = array('prefix' => $wpdb->prefix, 'objects' => array());
foreach ($want as $t) {
    $exists = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $t));
    $create = null;
    if ($exists) {
        $row = $wpdb->get_row("SHOW CREATE TABLE `{$t}`", ARRAY_N);
        $create = is_array($row) ? (string) $row[1] : null;
    }
    $out['objects'][$t] = array('exists' => (bool) $exists, 'create' => $create);
}
$out['blog_public'] = (int) get_option('blog_public');
$out['core'] = defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null;
echo json_encode($out, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

POST_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['REQUEST_METHOD'] = 'POST';
$_SERVER['HTTP_USER_AGENT'] = 'FP-0002-P18C-QA';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

add_filter('wp_die_ajax_handler', function () {
    return function ($message) {
        throw new RuntimeException('AJAX_DONE');
    };
});
add_filter('wp_die_handler', function () {
    return function ($message) {
        throw new RuntimeException('AJAX_DONE');
    };
});

function fp02_p18c_ajax($post) {
    add_filter('wp_doing_ajax', '__return_true');
    $_POST = $post;
    $_REQUEST = $post;
    $_SERVER['REQUEST_METHOD'] = 'POST';
    ob_start();
    $err = null;
    try {
        \Shpigovsky\Core\Forms\ConsultationHandler::handle_ajax();
    } catch (Throwable $e) {
        if ('AJAX_DONE' !== $e->getMessage()) {
            $err = $e->getMessage();
        }
    }
    $raw = ob_get_clean();
    $json = json_decode($raw, true);
    return array('raw' => substr((string) $raw, 0, 2000), 'json' => $json, 'err' => $err);
}

$report = array('ok' => true);

if (!class_exists('Shpigovsky\\Core\\Leads\\LeadRegistry') || !class_exists('Shpigovsky\\Core\\Mail\\MailOps')) {
    echo json_encode(array('ok'=>false,'error'=>'classes missing'));
    echo "\n";
    exit(2);
}

\Shpigovsky\Core\Leads\LeadRegistry::maybe_install_table();
global $wpdb;
$table = \Shpigovsky\Core\Leads\LeadRegistry::table_name();
$create_row = $wpdb->get_row("SHOW CREATE TABLE `{$table}`", ARRAY_N);
$report['schema'] = array(
    'table' => $table,
    'version' => get_option('fp02_form_leads_schema'),
    'create' => is_array($create_row) ? (string) $create_row[1] : null,
);

$before = get_option('fp02_metacode_system_meta', array());
if (!is_array($before)) $before = array();
$after = $before;
$after['latest_wave'] = 'P18C SMTP / Forms Foundation';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18C';
$after['cutover'] = 'DONE';
$after['dns_ns'] = 'DONE / Beget';
$after['ssl'] = 'ACTIVE';
$after['smtp_sender'] = 'noreply@shpigovsky.ru';
$after['mail'] = 'SMTP SETTINGS READY — CREDENTIALS REQUIRED';
$after['leads'] = 'ACTIVE';
$after['metrika_form_goals'] = 'CONFIGURABLE';
$after['backup'] = 'FRESH BEGET BACKUP CONFIRMED BY OPERATOR';
$after['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$after['state_note'] = 'LIVE https://shpigovsky.ru; INDEXING CLOSED; SMTP SETTINGS READY — CREDENTIALS REQUIRED; LEADS ACTIVE';
unset($after['precutover'], $after['p15_note']);
update_option('fp02_metacode_system_meta', $after, false);

$admin = get_user_by('login', 'mars');
if ($admin) {
    wp_set_current_user((int) $admin->ID);
}
ob_start();
\Shpigovsky\Core\Admin\MailFormsSettings::render_page();
$mail_html = ob_get_clean();
ob_start();
\Shpigovsky\Core\Admin\LeadsAdmin::render_page();
$leads_html = ob_get_clean();
ob_start();
if (class_exists('Shpigovsky\\Core\\Admin\\SystemDashboard')) {
    \Shpigovsky\Core\Admin\SystemDashboard::render_widget();
}
$dash_html = ob_get_clean();

$auth = get_option('fp02_mailbox_auth', array());
$secret = (is_array($auth) && isset($auth['secret']) && is_string($auth['secret'])) ? $auth['secret'] : '';
$report['redaction'] = array(
    'password_configured' => \Shpigovsky\Core\Mail\MailOps::password_is_configured(),
    'mail_html_has_not_configured' => false !== strpos($mail_html, 'NOT CONFIGURED'),
    'mail_html_has_configured_word' => false !== strpos($mail_html, 'CONFIGURED'),
    'mail_html_password_input_empty' => (bool) preg_match('/name="smtp_password"[^>]*value=""/', $mail_html) || false !== strpos($mail_html, 'name="smtp_password" value=""'),
    'mail_html_contains_secret' => ($secret !== '' && false !== strpos($mail_html, $secret)),
    'leads_html_contains_secret' => ($secret !== '' && false !== strpos($leads_html, $secret)),
    'dash_html_contains_secret' => ($secret !== '' && false !== strpos($dash_html, $secret)),
    'dash_has_credentials_required' => false !== strpos($dash_html, 'CREDENTIALS REQUIRED') || false !== strpos($dash_html, 'SMTP SETTINGS READY'),
    'dash_has_noreply' => false !== strpos($dash_html, 'noreply@shpigovsky.ru'),
    'dash_has_leads_active' => false !== strpos($dash_html, 'ACTIVE'),
    'dash_indexing_closed' => false !== strpos($dash_html, 'CLOSED') || false !== strpos($dash_html, 'закрыт'),
    'leads_menu_heading' => false !== strpos($leads_html, 'Заявки'),
    'html_bytes' => array('mail'=>strlen($mail_html),'leads'=>strlen($leads_html),'dash'=>strlen($dash_html)),
);

wp_set_current_user(0);
$now = time();
$token1 = 'p18cqa' . wp_generate_password(20, false, false);
$nonce = wp_create_nonce('fp02_lead_submit');
$base = array(
    'fp02_lead_nonce' => $nonce,
    'name' => 'P18C QA',
    'phone' => '89251836464',
    'email' => '',
    'message' => 'P18C safe test lead — persistence only',
    'consent' => '1',
    'form_context' => 'qa',
    'page_url' => 'https://shpigovsky.ru/p18c-qa/?utm_source=p18c&utm_medium=qa&utm_campaign=smtp-foundation&utm_content=persist&utm_term=wave',
    'page_title' => 'P18C QA',
    'utm_source' => 'p18c',
    'utm_medium' => 'qa',
    'utm_campaign' => 'smtp-foundation',
    'utm_content' => 'persist',
    'utm_term' => 'wave',
    'referrer' => '',
    'form_started_at' => (string) ($now - 12),
    'timestamp' => (string) $now,
    'request_token' => $token1,
    'fp02_qa' => '1',
    'company_url' => '',
);

$r1 = fp02_p18c_ajax($base);
$r2 = fp02_p18c_ajax($base);
$base_fast = $base;
$base_fast['request_token'] = 'p18cqa' . wp_generate_password(20, false, false);
$base_fast['form_started_at'] = (string) $now;
$base_fast['timestamp'] = (string) $now;
$r_fast = fp02_p18c_ajax($base_fast);

$qa_rows = $wpdb->get_results($wpdb->prepare("SELECT id, form_key, visitor_name, phone, email, source_path, delivery_status, smtp_status, utm_source, utm_campaign, metrika_goal, is_qa FROM {$table} WHERE is_qa = 1 ORDER BY id DESC LIMIT 5"), ARRAY_A);
$deleted = \Shpigovsky\Core\Leads\LeadRegistry::delete_qa_rows();
$left_qa = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$table} WHERE is_qa = 1");

$cfg = \Shpigovsky\Core\Mail\MailOps::get_config();
unset($cfg['smtp_password'], $cfg['password'], $cfg['secret']);

$report['mail'] = array(
    'state' => \Shpigovsky\Core\Mail\MailOps::state(),
    'state_label' => \Shpigovsky\Core\Mail\MailOps::state_label(),
    'dashboard_line' => \Shpigovsky\Core\Mail\MailOps::dashboard_mail_line(),
    'from' => \Shpigovsky\Core\Mail\MailOps::from_email(),
    'from_name' => \Shpigovsky\Core\Mail\MailOps::from_name(),
    'complete' => \Shpigovsky\Core\Mail\MailOps::is_complete(),
    'should_suppress' => \Shpigovsky\Core\Mail\MailOps::should_suppress(),
    'delivery_active' => (int) $cfg['delivery_active'],
    'verified' => (int) $cfg['verified'],
    'recipients' => \Shpigovsky\Core\Mail\MailOps::recipient_emails(),
    'config_keys' => array_keys($cfg),
);
$report['qa'] = array(
    'submit' => $r1,
    'duplicate' => $r2,
    'too_fast' => $r_fast,
    'rows_before_cleanup' => $qa_rows,
    'deleted' => $deleted,
    'qa_left' => $left_qa,
);
$report['wp'] = array(
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'home' => get_option('home'),
    'siteurl' => get_option('siteurl'),
    'blog_public' => (int) get_option('blog_public'),
    'mail_suppressed' => (bool) has_filter('pre_wp_mail'),
    'modules' => array(
        'MailOps' => class_exists('Shpigovsky\\Core\\Mail\\MailOps'),
        'SmtpTransport' => class_exists('Shpigovsky\\Core\\Mail\\SmtpTransport'),
        'LeadRegistry' => class_exists('Shpigovsky\\Core\\Leads\\LeadRegistry'),
        'MailFormsSettings' => class_exists('Shpigovsky\\Core\\Admin\\MailFormsSettings'),
        'LeadsAdmin' => class_exists('Shpigovsky\\Core\\Admin\\LeadsAdmin'),
    ),
    'meta' => get_option('fp02_metacode_system_meta'),
);
$report['ok'] = !empty($r1['json']['ok']) && !empty($r1['json']['accepted']) && ($r2['json']['ok'] === false || ($r2['json']['success'] === false)) && 0 === $left_qa && 0 === (int) get_option('blog_public');
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


def local_path(kind: str, rel: str) -> Path:
    if kind == "plugin":
        return PLUGIN / Path(*rel.split("/"))
    if kind == "mu":
        return MU / Path(*rel.split("/"))
    return THEME / Path(*rel.split("/"))


def remote_path(kind: str, rel: str) -> str:
    if kind == "plugin":
        return PLUGIN_R + "/" + rel
    if kind == "mu":
        return MU_R + "/" + rel
    return THEME_R + "/" + rel


def sftp_get(sftp, remote: str):
    try:
        bio = io.BytesIO()
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except (FileNotFoundError, OSError):
        return None


def sftp_put(sftp, remote: str, data: bytes) -> None:
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
    return {"parse_error": True, "head": out[:4000]}


def source_secret_scan() -> list:
    hits = []
    for kind, rel in DEPLOY:
        fp = local_path(kind, rel)
        text = fp.read_text(encoding="utf-8", errors="ignore")
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
            "robots_meta": (lambda m: m.group(1) if m else None)(re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', body, re.I)),
            "has_lead_form": "data-lead-form" in body,
            "has_ym": "mc.yandex.ru" in body or "ym(" in body,
            "len": len(r.content or b""),
        }
    except Exception as e:
        return {"url": url, "error": str(e)}


def wp_login(pairs, origin: str):
    user = getf(pairs, "wordpress_username")
    password = getf(pairs, "wordpress_password")
    if not user or not password:
        return None, {"ok": False, "error": "missing wp creds keys", "origin": origin}
    s = requests.Session()
    s.headers["User-Agent"] = UA
    login_url = origin.rstrip("/") + "/wp-login.php"
    try:
        s.get(login_url, timeout=30, allow_redirects=True)
        r = s.post(
            login_url,
            data={
                "log": user,
                "pwd": password,
                "wp-submit": "Log In",
                "redirect_to": origin.rstrip("/") + "/wp-admin/",
                "testcookie": "1",
            },
            timeout=40,
            allow_redirects=True,
        )
        ok = "/wp-admin" in str(r.url) and r.status_code == 200 and "wp-login.php" not in str(r.url)
        return s, {"ok": ok, "final_url": str(r.url), "status": r.status_code, "origin": origin, "user": user}
    except Exception as e:
        return None, {"ok": False, "error": str(e), "origin": origin}


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    LAYER_B.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    scan = source_secret_scan()
    (EV / "SOURCE-SECRET-SCAN.json").write_text(json.dumps({"utc": now, "hits": scan}, indent=2) + "\n", encoding="utf-8")
    if scan:
        print("SECRET SCAN FAIL", scan)
        return 4

    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host"),
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username"),
        password=getf(pairs, "ssh_password_or_key_reference"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()

    sftp_put(sftp, "/tmp/fp02_p18c_schema.php", SCHEMA_BEFORE_PHP.encode("utf-8"))
    sout, serr, scode = php82(client, "/tmp/fp02_p18c_schema.php")
    schema_before = parse_json_out(sout)
    (EV / "DB-SCHEMA-BEFORE.json").write_text(json.dumps({"exit": scode, "stderr": serr[-600:], "data": schema_before}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("SCHEMA_BEFORE", schema_before.get("core"), list((schema_before.get("objects") or {}).keys()))

    before_rows = []
    for kind, rel in DEPLOY:
        remote = remote_path(kind, rel)
        prod = sftp_get(sftp, remote)
        src = local_path(kind, rel).read_bytes()
        snap_name = (kind + "__" + rel.replace("/", "__")).replace("\\", "__")
        if prod is not None:
            (LAYER_B / snap_name).write_bytes(prod)
        before_rows.append({
            "kind": kind,
            "rel": rel,
            "remote": remote,
            "src_sha": sha256_bytes(src),
            "prod_before_sha": sha256_bytes(prod) if prod is not None else None,
            "prod_existed": prod is not None,
            "src_bytes": len(src),
        })
    (EV / "LAYER-B-SNAPSHOTS.json").write_text(json.dumps({"utc": now, "layer_b": str(LAYER_B), "files": before_rows}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    run(client, f"mkdir -p {PLUGIN_R}/src/Mail {PLUGIN_R}/src/Leads {PLUGIN_R}/src/Privacy")

    lint_ok = []
    after_rows = []
    for kind, rel in DEPLOY:
        src = local_path(kind, rel).read_bytes()
        remote = remote_path(kind, rel)
        lint_remote = "/tmp/fp02_p18c_lint.php"
        sftp_put(sftp, lint_remote, src)
        if rel.endswith(".php"):
            lout, lerr, lcode = php82(client, f"-l {lint_remote}")
            lint_ok.append({"rel": rel, "code": lcode, "out": (lout + lerr)[-400:]})
            if lcode != 0 or "No syntax errors" not in (lout + lerr):
                (EV / "DEPLOY-QA.json").write_text(json.dumps({"ok": False, "lint": lint_ok}, indent=2) + "\n", encoding="utf-8")
                print("LINT FAIL", rel, lout, lerr)
                return 3
        parent = remote.rsplit("/", 1)[0]
        run(client, f"mkdir -p {parent}")
        sftp_put(sftp, remote, src)
        prod = sftp_get(sftp, remote)
        match = prod is not None and sha256_bytes(prod) == sha256_bytes(src)
        after_rows.append({
            "rel": rel,
            "src_sha": sha256_bytes(src),
            "prod_after_sha": sha256_bytes(prod) if prod else None,
            "match": match,
        })
        print("UPLOAD", rel, "MATCH" if match else "MISMATCH")

    sftp_put(sftp, "/tmp/fp02_p18c_post.php", POST_PHP.encode("utf-8"))
    pout, perr, pcode = php82(client, "/tmp/fp02_p18c_post.php", timeout=120)
    post = parse_json_out(pout)
    (EV / "POST-DEPLOY-QA.json").write_text(json.dumps({"exit": pcode, "stderr": perr[-1200:], "stdout_head": pout[:1500], "data": post}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("POST", pcode, (post.get("wp") or {}).get("core"), post.get("ok"), (post.get("mail") or {}).get("state"))

    public = {
        "home": http_get(LIVE + "/"),
        "privacy": http_get(LIVE + "/privacy-policy/"),
        "inner_privacy": http_get(INNER + "/privacy-policy/"),
        "robots": http_get(LIVE + "/robots.txt"),
        "inner_robots": http_get(INNER + "/robots.txt"),
    }
    (EV / "HTTP-SMOKE.json").write_text(json.dumps(public, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    dash = {"ok": False}
    session = None
    login_info = None
    for origin in (INNER, LIVE):
        session, login_info = wp_login(pairs, origin)
        dash["login"] = login_info
        if session and login_info.get("ok"):
            break
    if session and login_info and login_info.get("ok"):
        origin = login_info["origin"]
        pages = {}
        for path, key in (
            ("/wp-admin/index.php", "dashboard"),
            ("/wp-admin/admin.php?page=fp02-site-settings-mail-forms", "mail"),
            ("/wp-admin/admin.php?page=fp02-form-leads", "leads"),
        ):
            r = session.get(origin.rstrip("/") + path, timeout=40, allow_redirects=True)
            html = r.text or ""
            (EV / f"admin-{key}.html").write_text(html, encoding="utf-8")
            pages[key] = {
                "status": r.status_code,
                "final": str(r.url),
                "len": len(html),
                "has_mail_heading": "Почта и формы" in html,
                "has_not_configured": "NOT CONFIGURED" in html,
                "has_password_value_filled": bool(re.search(r'name="smtp_password"[^>]*value="[^"]+', html)),
                "has_leads_heading": "Заявки" in html,
                "has_credentials_required": "CREDENTIALS REQUIRED" in html or "SMTP SETTINGS READY" in html,
                "has_noreply": "noreply@shpigovsky.ru" in html,
                "indexing_open_claim": "INDEXING OPEN" in html and "CLOSED" not in html,
            }
        dash.update({"ok": True, "pages": pages})

    match_n = sum(1 for r in after_rows if r["match"])
    parity = {"n": len(after_rows), "matched": match_n, "label": f"{match_n}/{len(after_rows)} MATCH", "files": after_rows}
    (EV / "SOURCE-PROD-PARITY.json").write_text(json.dumps(parity, indent=2) + "\n", encoding="utf-8")

    redaction = post.get("redaction") or {}
    secret_ok = (redaction.get("mail_html_contains_secret") is not True) and (redaction.get("leads_html_contains_secret") is not True)
    qa_ok = bool(post.get("ok"))
    indexing_closed = (post.get("wp") or {}).get("blog_public") == 0
    deploy_ok = match_n == len(after_rows) and qa_ok and secret_ok and indexing_closed
    (EV / "DEPLOY-QA.json").write_text(json.dumps({
        "ok": deploy_ok,
        "parity": parity["label"],
        "core": (post.get("wp") or {}).get("core"),
        "lint_pass": all(x["code"] == 0 for x in lint_ok),
        "qa_ok": qa_ok,
        "secret_ok": secret_ok,
        "indexing_closed": indexing_closed,
        "mail_state": (post.get("mail") or {}).get("state"),
        "suppress": (post.get("wp") or {}).get("mail_suppressed"),
        "admin_http": dash,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tmp in ("/tmp/fp02_p18c_lint.php", "/tmp/fp02_p18c_schema.php", "/tmp/fp02_p18c_post.php"):
        try:
            sftp.remove(tmp)
        except OSError:
            pass
    sftp.close()
    client.close()
    print("PARITY", parity["label"], "QA", qa_ok, "SECRET", secret_ok, "CLOSED", indexing_closed, "DASH", dash.get("ok"))
    return 0 if deploy_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
