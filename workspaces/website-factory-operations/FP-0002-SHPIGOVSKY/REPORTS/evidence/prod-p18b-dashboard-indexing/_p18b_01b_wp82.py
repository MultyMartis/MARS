# -*- coding: utf-8 -*-
"""P18B: WP options via php8.2 + REST + NS. Read-only."""
from __future__ import annotations

import io
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing")
REMOTE_PHP = "/tmp/fp02_p18b_wp82.php"
UA = "FP-0002-P18B-wp82/1.0"

PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$active = (array) get_option('active_plugins', array());
$smtpish = array();
foreach ($active as $p) {
    if (preg_match('/mail|smtp|fluent|post.?smtp|wp.?mail/i', (string) $p)) $smtpish[] = $p;
}
$wpilot = get_option('metacode_wpilot', get_option('wpilot', array()));
$write = false;
if (is_array($wpilot) && array_key_exists('write_enabled', $wpilot)) $write = (bool) $wpilot['write_enabled'];
$admins = $wpdb->get_col("SELECT user_login FROM {$wpdb->users} u INNER JOIN {$wpdb->usermeta} m ON u.ID=m.user_id AND m.meta_key='{$wpdb->prefix}capabilities' AND m.meta_value LIKE '%administrator%' ORDER BY user_login");
$opt_keys = array('siteurl','home','blogname','permalink_structure','blog_public','WPLANG');
$options = array();
foreach ($opt_keys as $k) { $options[$k] = get_option($k); }
echo json_encode(array(
    'ok'=>true,
    'php'=>PHP_VERSION,
    'wp_version'=>get_bloginfo('version'),
    'home_url'=>home_url('/'),
    'site_url'=>site_url('/'),
    'options'=>$options,
    'blog_public'=>(int)get_option('blog_public'),
    'mail_suppressed'=>(bool)has_filter('pre_wp_mail'),
    'smtp_like_plugins'=>$smtpish,
    'wpilot_version'=>defined('METACODE_WPILOT_VERSION')?METACODE_WPILOT_VERSION:(defined('WPILOT_VERSION')?WPILOT_VERSION:null),
    'wpilot_write'=>$write,
    'env_fn'=>function_exists('wp_get_environment_type')?wp_get_environment_type():null,
    'WP_ENVIRONMENT_TYPE'=>defined('WP_ENVIRONMENT_TYPE')?WP_ENVIRONMENT_TYPE:null,
    'WP_DEBUG'=>defined('WP_DEBUG')?WP_DEBUG:null,
    'SHPIGOVSKY_CORE_VERSION'=>defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:null,
    'dashboard_meta'=>get_option('fp02_metacode_system_meta', array()),
    'admin_logins'=>$admins,
    'robots_file_exists'=>is_file(ABSPATH.'robots.txt'),
    'robots_file'=>is_file(ABSPATH.'robots.txt')?file_get_contents(ABSPATH.'robots.txt'):null,
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
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


def main() -> int:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ns = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Resolve-DnsName shpigovsky.ru -Type NS -Server 8.8.8.8 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty NameHost"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30,
    )
    (EV / "DNS-NS.txt").write_text((ns.stdout or "") + "\n---stderr---\n" + (ns.stderr or ""), encoding="utf-8")

    rest = {}
    try:
        jr = requests.get("https://shpigovsky.ru/wp-json/", timeout=30, allow_redirects=True, headers={"User-Agent": UA})
        payload = jr.json()
        rest = {
            "status": jr.status_code,
            "name": payload.get("name"),
            "url": payload.get("url"),
            "home": payload.get("home"),
            "namespaces_sample": (payload.get("namespaces") or [])[:12],
        }
    except Exception as exc:
        rest = {"error": str(exc)}
    (EV / "REST-LIVE.json").write_text(json.dumps(rest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

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
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), REMOTE_PHP)
    stdin, stdout, stderr = client.exec_command(
        f"php8.2 {REMOTE_PHP} 2>/dev/null || /usr/local/bin/php8.2 {REMOTE_PHP}", timeout=90
    )
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    code = stdout.channel.recv_exit_status()
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    (EV / "WP-INTAKE-RAW.txt").write_text(out + "\n---stderr---\n" + err + f"\nexit={code}\n", encoding="utf-8")
    data = None
    for ln in out.splitlines():
        if ln.startswith("{"):
            data = json.loads(ln)
            break
    if data is None:
        data = {"parse_error": True, "head": out[:2000], "stderr": err[-2000:], "exit": code}
    payload = {"generated_at": now, "php_exit": code, "data": data, "rest": rest, "ns_stdout": (ns.stdout or "").strip()}
    (EV / "WP-INTAKE.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("exit", code)
    if isinstance(data, dict) and not data.get("parse_error"):
        print("HOME", data.get("home_url"), (data.get("options") or {}).get("home"))
        print("SITEURL", data.get("site_url"), (data.get("options") or {}).get("siteurl"))
        print("blog_public", data.get("blog_public"), "mail", data.get("mail_suppressed"))
        print("core", data.get("SHPIGOVSKY_CORE_VERSION"), "php", data.get("php"), "wp", data.get("wp_version"))
        print("admins", data.get("admin_logins"))
        print("wpilot", data.get("wpilot_version"), "write", data.get("wpilot_write"))
        print("smtp_plugins", data.get("smtp_like_plugins"))
    print("REST", rest)
    print("NS", (ns.stdout or "").strip())
    sftp.close()
    client.close()
    return 0 if code == 0 and isinstance(data, dict) and data.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
