# -*- coding: utf-8 -*-
"""P18C-FU02 phase 1: production SMTP/recipient intake. Read-only. Password never printed."""
from __future__ import annotations

import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import re

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = ROOT / "REPORTS" / "evidence" / "prod-p18c-fu02-multi-recipients"
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"

INTAKE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/index.php';
$_SERVER['PHP_SELF'] = '/wp-admin/index.php';
$_SERVER['REQUEST_METHOD'] = 'GET';
error_reporting(E_ALL);
ini_set('display_errors', '0');
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

function fp02_fu02_emit($payload) {
    echo 'FP02_FU02_JSON:' . wp_json_encode($payload) . "\n";
}

try {

$report = array('ok' => true);
$mail_ops = class_exists('Shpigovsky\\Core\\Mail\\MailOps');

$cfg = $mail_ops ? \Shpigovsky\Core\Mail\MailOps::get_config() : array();
unset($cfg['smtp_password'], $cfg['password'], $cfg['secret']);

$raw = get_option('fp02_mail_ops', null);
$raw_copy = $raw;
if (is_array($raw_copy)) {
    unset($raw_copy['smtp_password'], $raw_copy['password'], $raw_copy['secret']);
}

$auth = get_option('fp02_mailbox_auth', array());
$auth_safe = array(
    'is_array' => is_array($auth),
    'has_configured_key' => is_array($auth) && array_key_exists('configured', $auth),
    'configured_flag' => is_array($auth) && !empty($auth['configured']) ? 1 : 0,
    'has_secret_key' => is_array($auth) && array_key_exists('secret', $auth),
    'secret_is_string' => is_array($auth) && isset($auth['secret']) && is_string($auth['secret']),
    'secret_nonempty' => is_array($auth) && isset($auth['secret']) && is_string($auth['secret']) && '' !== $auth['secret'],
    'secret_len' => (is_array($auth) && isset($auth['secret']) && is_string($auth['secret'])) ? strlen($auth['secret']) : 0,
);
unset($auth);

$raw_recipients = (is_array($raw) && isset($raw['recipients'])) ? $raw['recipients'] : null;
$raw_type = 'missing';
if (is_string($raw_recipients)) {
    $raw_type = 'string';
} elseif (is_array($raw_recipients)) {
    $assoc = array_keys($raw_recipients) !== range(0, max(0, count($raw_recipients) - 1)) && !isset($raw_recipients[0]);
    $first = reset($raw_recipients);
    if (isset($raw_recipients['email']) && !isset($raw_recipients[0])) {
        $raw_type = 'single_associative_row';
    } elseif (is_array($first) && (isset($first['email']) || isset($first['recipient_email']))) {
        $raw_type = 'serialized_array_of_rows';
    } elseif (is_string($first)) {
        $raw_type = 'array_of_strings';
    } else {
        $raw_type = 'array_other';
    }
}

$report['wp'] = array(
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'home' => get_option('home'),
    'siteurl' => get_option('siteurl'),
    'blog_public' => (int) get_option('blog_public'),
    'blogname' => get_option('blogname'),
);

$report['smtp_settings'] = array(
    'smtp_enabled' => isset($cfg['smtp_enabled']) ? (int) $cfg['smtp_enabled'] : null,
    'smtp_host' => isset($cfg['smtp_host']) ? (string) $cfg['smtp_host'] : '',
    'smtp_port' => isset($cfg['smtp_port']) ? (int) $cfg['smtp_port'] : 0,
    'smtp_encryption' => isset($cfg['smtp_encryption']) ? (string) $cfg['smtp_encryption'] : '',
    'smtp_auth' => isset($cfg['smtp_auth']) ? (int) $cfg['smtp_auth'] : null,
    'smtp_username' => isset($cfg['smtp_username']) ? (string) $cfg['smtp_username'] : '',
    'password_configured' => $mail_ops ? (\Shpigovsky\Core\Mail\MailOps::password_is_configured() ? 'YES' : 'NO') : 'UNKNOWN',
    'smtp_from_email' => isset($cfg['smtp_from_email']) ? (string) $cfg['smtp_from_email'] : '',
    'smtp_from_name' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::from_name() : '',
    'form_metrika_goal' => isset($cfg['form_metrika_goal']) ? (string) $cfg['form_metrika_goal'] : '',
    'lead_retention_days' => isset($cfg['lead_retention_days']) ? (int) $cfg['lead_retention_days'] : null,
    'verified' => isset($cfg['verified']) ? (int) $cfg['verified'] : 0,
    'delivery_active' => isset($cfg['delivery_active']) ? (int) $cfg['delivery_active'] : 0,
    'last_test_status' => isset($cfg['last_test_status']) ? (string) $cfg['last_test_status'] : '',
);

$report['runtime'] = array(
    'smtp_state' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::state() : null,
    'smtp_label' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::state_label() : null,
    'is_complete' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::is_complete() : null,
    'should_suppress' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::should_suppress() : null,
    'pre_wp_mail' => (bool) has_filter('pre_wp_mail'),
    'dashboard_mail_line' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::dashboard_mail_line() : null,
);

$report['recipient_storage'] = array(
    'owner_option' => 'fp02_mail_ops',
    'auth_option' => 'fp02_mailbox_auth',
    'owner_class' => 'Shpigovsky\\Core\\Mail\\MailOps',
    'raw_recipients_type' => $raw_type,
    'raw_recipients' => $raw_recipients,
    'normalized_recipients' => isset($cfg['recipients']) ? $cfg['recipients'] : array(),
    'normalized_count' => isset($cfg['recipients']) ? count($cfg['recipients']) : 0,
    'recipient_emails' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::recipient_emails() : array(),
    'auth_safe' => $auth_safe,
    'raw_top_keys' => is_array($raw_copy) ? array_keys($raw_copy) : array(),
);

$admin = get_user_by('login', 'mars');
if ($admin) {
    wp_set_current_user((int) $admin->ID);
}
if (defined('ABSPATH')) {
    require_once ABSPATH . 'wp-admin/includes/admin.php';
    require_once ABSPATH . 'wp-admin/includes/template.php';
}
$mail_html = '';
if (class_exists('Shpigovsky\\Core\\Admin\\MailFormsSettings')) {
    ob_start();
    \Shpigovsky\Core\Admin\MailFormsSettings::render_page();
    $mail_html = (string) ob_get_clean();
}

$report['admin_ui_before'] = array(
    'h1' => false !== strpos($mail_html, 'Почта и формы'),
    'recipients_heading' => false !== strpos($mail_html, 'Получатели'),
    'add_button' => false !== strpos($mail_html, 'Добавить получателя'),
    'remove_button' => false !== strpos($mail_html, 'Удалить'),
    'password_empty' => (bool) preg_match('/name="smtp_password"[^>]*value=""/', $mail_html) || false !== strpos($mail_html, 'name="smtp_password" value=""'),
    'password_configured_label' => false !== strpos($mail_html, '>CONFIGURED<'),
    'row_count' => preg_match_all('/name="recipients\[\d+\]\[email\]"/', $mail_html),
    'mail_bytes' => strlen($mail_html),
    'state_configured_not_verified' => false !== strpos($mail_html, 'CONFIGURED / NOT VERIFIED'),
);

fp02_fu02_emit($report);
} catch (Throwable $e) {
    fp02_fu02_emit(array(
        'ok' => false,
        'error' => $e->getMessage(),
        'file' => $e->getFile(),
        'line' => $e->getLine(),
        'partial' => isset($report) ? $report : null,
    ));
}
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


def ssh_connect(pairs):
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
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    return client


def run_ssh(client, cmd, timeout=90):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    code = stdout.channel.recv_exit_status()
    return out, err, code


def sftp_get(sftp, remote: str):
    bio = io.BytesIO()
    try:
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except Exception:
        return None


def parse_json_out(out: str):
    marker = "FP02_FU02_JSON:"
    for ln in reversed(out.splitlines()):
        if marker in ln:
            return json.loads(ln.split(marker, 1)[1])
        if ln.startswith("{"):
            return json.loads(ln)
    return {"parse_error": True, "head": out[:4000], "tail": out[-1500:]}


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = ssh_connect(pairs)
    sftp = client.open_sftp()

    rels = [
        "shpigovsky-core.php",
        "src/Mail/MailOps.php",
        "src/Mail/SmtpTransport.php",
        "src/Admin/MailFormsSettings.php",
        "src/Admin/SystemDashboard.php",
        "src/Admin/LeadsAdmin.php",
        "src/Admin/ActivityLog.php",
        "src/Forms/ConsultationHandler.php",
    ]
    hashes = {}
    for rel in rels:
        remote = sftp_get(sftp, f"{PLUGIN_R}/{rel}")
        local = (PLUGIN / Path(*rel.split("/"))).read_bytes() if (PLUGIN / Path(*rel.split("/"))).exists() else b""
        hashes[rel] = {
            "prod": sha256_bytes(remote).upper() if remote else None,
            "source": sha256_bytes(local).upper() if local else None,
            "match": bool(remote) and sha256_bytes(remote) == sha256_bytes(local),
            "prod_bytes": len(remote) if remote else 0,
        }

    remote_php = "/tmp/fp02_p18c_fu02_intake.php"
    sftp.putfo(io.BytesIO(INTAKE_PHP.encode("utf-8")), remote_php)
    out, err, code = run_ssh(client, f"php8.2 {remote_php} 2>/dev/null || php {remote_php}", timeout=90)
    try:
        sftp.remove(remote_php)
    except Exception:
        pass

    wp = parse_json_out(out)
    if "parse_error" in wp:
        wp["stderr"] = err[-1200:]
        wp["code"] = code

    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "required": "CURRENT OPERATOR SMTP SETTINGS PRESERVED / RECIPIENT STORAGE OWNER IDENTIFIED",
        "wp": wp,
        "source_prod_hashes_before": hashes,
        "notes": {
            "password_never_printed": True,
            "no_real_smtp_test": True,
            "no_indexing_change": True,
        },
    }
    (EV / "INTAKE-BEFORE.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    smtp = ((wp or {}).get("smtp_settings") or {})
    rec = ((wp or {}).get("recipient_storage") or {})
    runtime = ((wp or {}).get("runtime") or {})
    print(
        "INTAKE",
        wp.get("ok"),
        "CORE",
        ((wp.get("wp") or {}).get("core")),
        "HOST",
        smtp.get("smtp_host"),
        "PORT",
        smtp.get("smtp_port"),
        "ENC",
        smtp.get("smtp_encryption"),
        "AUTH",
        smtp.get("smtp_auth"),
        "USER",
        smtp.get("smtp_username"),
        "PW",
        smtp.get("password_configured"),
        "FROM",
        smtp.get("smtp_from_email"),
        "STATE",
        runtime.get("smtp_label"),
        "COMPLETE",
        runtime.get("is_complete"),
        "SUPPRESS",
        runtime.get("should_suppress"),
        "BLOG_PUBLIC",
        ((wp.get("wp") or {}).get("blog_public")),
        "OWNER",
        rec.get("owner_option"),
        "TYPE",
        rec.get("raw_recipients_type"),
        "COUNT",
        rec.get("normalized_count"),
        "ADD_BTN",
        ((wp.get("admin_ui_before") or {}).get("add_button")),
    )
    sftp.close()
    client.close()
    return 0 if wp.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
