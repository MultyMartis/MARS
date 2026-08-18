# -*- coding: utf-8 -*-
"""PROD-P18B phase 1: current production reality. Read-only. No secrets in output."""
from __future__ import annotations

import hashlib
import io
import json
import re
import socket
import ssl
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
PLUGIN_SRC = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18b-dashboard-indexing"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
UA = "FP-0002-P18B-reality/1.0"

HOSTS = [
    "shpigovsky.ru",
    "www.shpigovsky.ru",
    "shpigovsky.beget.tech",
]
URLS = [
    "http://shpigovsky.ru/",
    "https://shpigovsky.ru/",
    "http://www.shpigovsky.ru/",
    "https://www.shpigovsky.ru/",
    "http://shpigovsky.beget.tech/",
    "https://shpigovsky.beget.tech/",
]
SMOKE = [
    "/",
    "/uslugi/",
    "/kontakty/",
    "/privacy-policy/",
    "/robots.txt",
    "/wp-sitemap.xml",
    "/wp-json/",
    "/wp-admin/",
    "/wp-login.php",
]

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
$meta = get_option('fp02_metacode_system_meta', array());
echo json_encode(array(
    'ok' => true,
    'home' => get_option('home'),
    'siteurl' => get_option('siteurl'),
    'blog_public' => (int) get_option('blog_public'),
    'blogname' => get_option('blogname'),
    'wp_version' => get_bloginfo('version'),
    'php' => PHP_VERSION,
    'env_fn' => function_exists('wp_get_environment_type') ? wp_get_environment_type() : null,
    'env_const' => defined('WP_ENVIRONMENT_TYPE') ? WP_ENVIRONMENT_TYPE : null,
    'debug' => defined('WP_DEBUG') && WP_DEBUG,
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'mail_suppressed' => (bool) has_filter('pre_wp_mail'),
    'pre_wp_mail_callbacks' => has_filter('pre_wp_mail'),
    'smtp_like_plugins' => $smtpish,
    'wpilot_version' => defined('METACODE_WPILOT_VERSION') ? METACODE_WPILOT_VERSION : (defined('WPILOT_VERSION') ? WPILOT_VERSION : null),
    'wpilot_write' => $write,
    'dashboard_meta' => is_array($meta) ? $meta : array(),
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


def run_cmd(cmd, timeout=25):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        return {"cmd": cmd, "code": p.returncode, "out": (p.stdout or "")[:4000], "err": (p.stderr or "")[:800]}
    except Exception as e:
        return {"cmd": cmd, "error": str(e)}


def dns_host(host: str) -> dict:
    out = {"host": host, "nslookup": {}, "socket": {}}
    for q in ("NS", "A", "AAAA", "CNAME"):
        out["nslookup"][q] = run_cmd(["nslookup", f"-type={q}", host, "8.8.8.8"])
    try:
        infos = socket.getaddrinfo(host, None)
        out["socket"]["addrs"] = sorted({x[4][0] for x in infos})
    except Exception as e:
        out["socket"]["error"] = str(e)
    return out


def ssl_info(host: str, port: int = 443) -> dict:
    rec = {"host": host, "port": port}
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=12) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                rec["ok"] = True
                rec["tls"] = ssock.version()
                rec["subject"] = dict(x[0] for x in cert.get("subject", ()))
                rec["issuer"] = dict(x[0] for x in cert.get("issuer", ()))
                rec["notAfter"] = cert.get("notAfter")
                rec["notBefore"] = cert.get("notBefore")
                rec["san"] = [x[1] for x in cert.get("subjectAltName", ()) if x[0] == "DNS"]
    except Exception as e:
        rec["ok"] = False
        rec["error"] = str(e)
    return rec


def http_probe(url: str, follow: bool = False) -> dict:
    try:
        r = requests.get(url, timeout=25, allow_redirects=follow, headers={"User-Agent": UA})
        body = r.text or ""
        return {
            "url": url,
            "follow": follow,
            "status": r.status_code,
            "final_url": str(r.url),
            "location": r.headers.get("Location"),
            "server": r.headers.get("Server"),
            "x_robots": r.headers.get("X-Robots-Tag"),
            "content_type": r.headers.get("Content-Type"),
            "has_wp": ("wp-content" in body) or ("WordPress" in body) or ("wp-includes" in body),
            "generator": (lambda m: m.group(1) if m else None)(re.search(r'<meta name=["\']generator["\'] content=["\']([^"\']+)', body, re.I)),
            "robots_meta": (lambda m: m.group(1) if m else None)(re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', body, re.I)),
            "canonical": (lambda m: m.group(1) if m else None)(
                re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', body, re.I)
                or re.search(r'href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', body, re.I)
            ),
            "body_bytes": len(r.content or b""),
            "body_head": body[:500],
            "legacy_markers": {
                "beget_abs": body.count("shpigovsky.beget.tech"),
                "live_abs": body.count("shpigovsky.ru"),
            },
        }
    except Exception as e:
        return {"url": url, "follow": follow, "error": str(e)}


def ssh_connect(pairs):
    host = getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech"
    user = getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user")
    password = getf(pairs, "ssh_password_or_key_reference", "ssh_password", "sftp_password", "ftp_or_sftp_password", "ftp_password")
    port = int(getf(pairs, "ssh_port", "sftp_port") or "22")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, port=port, username=user, password=password, timeout=30, allow_agent=False, look_for_keys=False)
    return client


def run_ssh(client, cmd, timeout=90):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    return stdout.read().decode("utf-8", errors="replace"), stderr.read().decode("utf-8", errors="replace"), stdout.channel.recv_exit_status()


def sftp_get(sftp, remote: str):
    try:
        bio = io.BytesIO()
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except (FileNotFoundError, OSError):
        return None


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    utc = datetime.now(timezone.utc).isoformat()
    dns = {h: dns_host(h) for h in HOSTS}
    (EV / "DNS-LOOKUPS.json").write_text(json.dumps(dns, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    ssls = {h: ssl_info(h) for h in HOSTS}
    (EV / "SSL-STATE.json").write_text(json.dumps(ssls, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    http = []
    for u in URLS:
        http.append(http_probe(u, follow=False))
        http.append(http_probe(u, follow=True))
    (EV / "HTTP-PROBES.json").write_text(json.dumps(http, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    smoke = {}
    for base in ("https://shpigovsky.ru", "http://shpigovsky.beget.tech"):
        smoke[base] = [http_probe(base + p, follow=False) for p in SMOKE]
    (EV / "FRONTEND-SMOKE.json").write_text(json.dumps(smoke, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    robots = {
        "https": http_probe("https://shpigovsky.ru/robots.txt", follow=True),
        "beget": http_probe("http://shpigovsky.beget.tech/robots.txt", follow=True),
    }
    (EV / "ROBOTS-HTTP.json").write_text(json.dumps(robots, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
    client = ssh_connect(pairs)
    sftp = client.open_sftp()

    remote_php = "/tmp/fp02_p18b_intake.php"
    with sftp.file(remote_php, "w") as fh:
        fh.write(INTAKE_PHP)
    out, err, code = run_ssh(client, f"php {remote_php}", timeout=60)
    wp = {}
    try:
        wp = json.loads(out.strip().splitlines()[-1] if out.strip() else "{}")
    except json.JSONDecodeError:
        wp = {"ok": False, "raw": out[:4000], "err": err[:800], "code": code}
    (EV / "WP-INTAKE.json").write_text(json.dumps(wp, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    files = {
        "robots.txt": sftp_get(sftp, f"{DOCROOT}/robots.txt"),
        "dashboard": sftp_get(sftp, f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/SystemDashboard.php"),
        "core_boot": sftp_get(sftp, f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php"),
        "mu_mail": sftp_get(sftp, f"{DOCROOT}/wp-content/mu-plugins/fp02-pre-cutover-mail-suppression.php"),
        "htaccess": sftp_get(sftp, f"{DOCROOT}/.htaccess"),
    }
    file_meta = {}
    for k, data in files.items():
        if data is None:
            file_meta[k] = {"exists": False}
            continue
        text = data.decode("utf-8", errors="replace")
        file_meta[k] = {
            "exists": True,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "head": text[:1200],
        }
    src_dash = (PLUGIN_SRC / "src/Admin/SystemDashboard.php").read_bytes()
    src_boot = (PLUGIN_SRC / "shpigovsky-core.php").read_bytes()
    parity = {
        "dashboard_src_sha": sha256_bytes(src_dash),
        "dashboard_prod_sha": file_meta.get("dashboard", {}).get("sha256"),
        "dashboard_match": sha256_bytes(src_dash) == file_meta.get("dashboard", {}).get("sha256"),
        "core_src_sha": sha256_bytes(src_boot),
        "core_prod_sha": file_meta.get("core_boot", {}).get("sha256"),
        "core_match": sha256_bytes(src_boot) == file_meta.get("core_boot", {}).get("sha256"),
    }
    (EV / "FS-INDEXING-OWNERS.json").write_text(
        json.dumps({"files": file_meta, "pre_wave_parity": parity}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    ls_out, ls_err, ls_code = run_ssh(
        client,
        f"ls -la {DOCROOT}/robots.txt {DOCROOT}/wp-content/mu-plugins 2>/dev/null; "
        f"php -v | head -1; "
        f"test -f {DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/SystemDashboard.php && echo DASHBOARD_OK",
    )
    (EV / "SSH-LS.txt").write_text(ls_out + "\n---stderr---\n" + ls_err, encoding="utf-8")

    sftp.remove(remote_php)
    sftp.close()
    client.close()

    https_ok = bool(ssls.get("shpigovsky.ru", {}).get("ok"))
    wp_html = any(p.get("has_wp") and p.get("status") == 200 for p in smoke.get("https://shpigovsky.ru", []))
    apex = next((p for p in http if p.get("url") == "https://shpigovsky.ru/" and p.get("follow") is True), {})
    summary = {
        "utc": utc,
        "required": "P18B CURRENT PRODUCTION REALITY VERIFIED",
        "live_domain": "https://shpigovsky.ru/",
        "home": wp.get("home"),
        "siteurl": wp.get("siteurl"),
        "blog_public": wp.get("blog_public"),
        "mail_suppressed": wp.get("mail_suppressed"),
        "smtp_like_plugins": wp.get("smtp_like_plugins"),
        "core": wp.get("core"),
        "wp_version": wp.get("wp_version"),
        "php": wp.get("php"),
        "https_cert_ok": https_ok,
        "https_san": ssls.get("shpigovsky.ru", {}).get("san"),
        "https_issuer": ssls.get("shpigovsky.ru", {}).get("issuer"),
        "https_notAfter": ssls.get("shpigovsky.ru", {}).get("notAfter"),
        "public_https_is_wordpress": wp_html,
        "public_https_status": apex.get("status"),
        "public_https_final": apex.get("final_url"),
        "robots_https_head": (robots.get("https") or {}).get("body_head"),
        "dashboard_meta": wp.get("dashboard_meta"),
        "backup": "FRESH BEGET BACKUP CONFIRMED BY OPERATOR",
        "smtp_mailbox": "noreply@shpigovsky.ru (operator: created; WP SMTP PENDING)",
        "pre_wave_dashboard_parity": parity,
        "admin_logins_present": wp.get("users_admin_logins"),
    }
    (EV / "REALITY-SUMMARY.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in (
        "home", "siteurl", "blog_public", "https_cert_ok", "public_https_is_wordpress",
        "public_https_status", "core", "mail_suppressed", "pre_wave_dashboard_parity",
    ) if k in summary}, indent=2, ensure_ascii=False))
    return 0 if wp.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
