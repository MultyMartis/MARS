# -*- coding: utf-8 -*-
"""PROD-P18C phase 1: current forms/mail production reality. Read-only. No secrets in output."""
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
EV = ROOT / "REPORTS" / "evidence" / "prod-p18c-smtp-forms-foundation"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
UA = "FP-0002-P18C-intake/1.0"

INTAKE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['HTTPS'] = 'on';
error_reporting(E_ALL);
ini_set('display_errors','0');
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
global $wpdb;
$active = (array) get_option('active_plugins', array());
$smtpish = array();
foreach ($active as $p) {
    if (preg_match('/mail|smtp|fluent|post.?smtp|wp.?mail/i', (string) $p)) {
        $smtpish[] = $p;
    }
}
$wpilot = get_option('metacode_wpilot', get_option('wpilot', array()));
$write = false;
if (is_array($wpilot) && array_key_exists('write_enabled', $wpilot)) {
    $write = (bool) $wpilot['write_enabled'];
}
$tables = $wpdb->get_col('SHOW TABLES');
$lead_like = array();
foreach ((array) $tables as $t) {
    if (preg_match('/lead|form|mail|smtp/i', (string) $t)) {
        $lead_like[] = $t;
    }
}
$schema = array();
foreach ($lead_like as $t) {
    $row = $wpdb->get_row("SHOW CREATE TABLE `{$t}`", ARRAY_N);
    $schema[$t] = is_array($row) ? (string) $row[1] : null;
}
$opt_names = $wpdb->get_col("SELECT option_name FROM {$wpdb->options} WHERE option_name LIKE '%smtp%' OR option_name LIKE '%mail%' OR option_name LIKE 'fp02_mail%' OR option_name LIKE 'fp02_mailbox%' LIMIT 50");
$safe_opts = array();
foreach ((array) $opt_names as $n) {
    if (preg_match('/pass|secret|auth|token/i', (string) $n)) {
        $safe_opts[$n] = 'REDACTED_NAME_MATCH';
        continue;
    }
    $v = get_option($n);
    if (is_array($v)) {
        $copy = $v;
        foreach (array('secret','password','smtp_password','passwd') as $k) {
            if (isset($copy[$k])) $copy[$k] = 'REDACTED';
        }
        $safe_opts[$n] = $copy;
    } else {
        $safe_opts[$n] = is_string($v) ? substr($v, 0, 80) : $v;
    }
}
echo json_encode(array(
    'ok' => true,
    'home' => get_option('home'),
    'siteurl' => get_option('siteurl'),
    'blogname' => get_option('blogname'),
    'blog_public' => (int) get_option('blog_public'),
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'mail_suppressed' => (bool) has_filter('pre_wp_mail'),
    'pre_wp_mail_callbacks' => has_filter('pre_wp_mail'),
    'smtp_like_plugins' => $smtpish,
    'wpilot_write' => $write,
    'organisation_name' => function_exists('get_field') ? get_field('organisation_name', 'option') : null,
    'yandex_metrica_counter_id' => function_exists('get_field') ? get_field('yandex_metrica_counter_id', 'option') : null,
    'handler_exists' => class_exists('Shpigovsky\\Core\\Forms\\ConsultationHandler'),
    'future_recipient_constant' => class_exists('Shpigovsky\\Core\\Forms\\ConsultationHandler') ? \Shpigovsky\Core\Forms\ConsultationHandler::FUTURE_RECIPIENT : null,
    'mail_ops_exists' => class_exists('Shpigovsky\\Core\\Mail\\MailOps'),
    'lead_tables' => $lead_like,
    'lead_schema' => $schema,
    'mailish_options_redacted' => $safe_opts,
    'users_admin_logins' => $wpdb->get_col("SELECT user_login FROM {$wpdb->users} u INNER JOIN {$wpdb->usermeta} m ON u.ID=m.user_id AND m.meta_key='{$wpdb->prefix}capabilities' AND m.meta_value LIKE '%administrator%' ORDER BY user_login"),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
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


def ssh_connect(pairs):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port", "sftp_port") or "22"),
        username=getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
        password=getf(pairs, "ssh_password_or_key_reference", "ssh_password", "sftp_password", "ftp_or_sftp_password", "ftp_password"),
        timeout=30,
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
    except Exception as e:
        return None


def http_get(url: str, timeout=20):
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": UA}, allow_redirects=True)
        body = r.text or ""
        return {
            "url": url,
            "status": r.status_code,
            "final": str(r.url),
            "len": len(r.content or b""),
            "has_lead_form": "data-lead-form" in body,
            "has_ym": "mc.yandex.ru" in body or "ym(" in body,
            "robots_meta": ("noindex" in body.lower()),
            "title_head": re.search(r"<title>(.*?)</title>", body, re.I | re.S),
        }
    except Exception as e:
        return {"url": url, "error": str(e)}


def main():
    EV.mkdir(parents=True, exist_ok=True)
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = ssh_connect(pairs)
    sftp = client.open_sftp()

    remote_php = "/tmp/fp02_p18c_intake.php"
    sftp.putfo(io.BytesIO(INTAKE_PHP.encode("utf-8")), remote_php)
    out, err, code = run_ssh(client, f"php8.2 {remote_php} 2>/dev/null || php {remote_php}", timeout=60)
    try:
        sftp.remove(remote_php)
    except Exception:
        pass

    wp = {}
    try:
        wp = json.loads(out.strip().splitlines()[-1])
    except Exception:
        wp = {"ok": False, "raw": out[-4000:], "err": err[-800:], "code": code}

    grep_out, grep_err, grep_code = run_ssh(
        client,
        f"grep -RIn --include='*.php' --include='*.js' -E '\\\\bmail\\\\s*\\\\(|wp_mail\\\\s*\\\\(|pre_wp_mail|phpmailer_init' {DOCROOT}/wp-content/plugins/shpigovsky-core {DOCROOT}/wp-content/themes/shpigovsky {DOCROOT}/wp-content/mu-plugins 2>/dev/null | head -200",
        timeout=60,
    )

    files = {
        "handler": sftp_get(sftp, f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Forms/ConsultationHandler.php"),
        "mu_mail": sftp_get(sftp, f"{DOCROOT}/wp-content/mu-plugins/fp02-pre-cutover-mail-suppression.php"),
        "dashboard": sftp_get(sftp, f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/SystemDashboard.php"),
        "core_boot": sftp_get(sftp, f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php"),
        "shell_js": sftp_get(sftp, f"{DOCROOT}/wp-content/themes/shpigovsky/assets/js/v9-shell.js"),
        "modal": sftp_get(sftp, f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/layout/global-consultation-modal.php"),
    }
    hashes = {k: (sha256_bytes(v).upper() if v else None) for k, v in files.items()}

    public = {
        "home": http_get("https://shpigovsky.ru/"),
        "beget": http_get("http://shpigovsky.beget.tech/"),
        "beget_privacy": http_get("http://shpigovsky.beget.tech/privacy-policy/"),
    }
    for rec in public.values():
        t = rec.get("title_head")
        if t:
            rec["title"] = re.sub(r"\s+", " ", t.group(1)).strip()[:180]
            rec["title_head"] = True

    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "required": "P18C CURRENT FORMS / MAIL REALITY VERIFIED",
        "wp": wp,
        "file_sha256": hashes,
        "grep_mail": {"code": grep_code, "out": grep_out[-8000:], "err": grep_err[-400:]},
        "http": public,
        "notes": {
            "smtp_not_configured": True,
            "mail_suppression_on": bool(wp.get("mail_suppressed")),
            "indexing_must_stay_closed": True,
            "password_not_requested": True,
        },
    }
    (EV / "CURRENT-FORMS-MAIL-REALITY.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    sftp.close()
    client.close()
    print("INTAKE", wp.get("ok"), "CORE", wp.get("core"), "SUPPRESS", wp.get("mail_suppressed"), "SMTP_PLUGINS", wp.get("smtp_like_plugins"))


if __name__ == "__main__":
    main()
