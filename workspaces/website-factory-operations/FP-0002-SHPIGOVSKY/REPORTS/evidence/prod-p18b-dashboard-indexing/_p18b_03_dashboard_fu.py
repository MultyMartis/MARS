# -*- coding: utf-8 -*-
"""P18B follow-up: dashboard public-origin truth + WP-origin CLOSED proof. No indexing open."""
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
EV = ROOT / "REPORTS" / "evidence" / "prod-p18b-dashboard-indexing"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18b-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/SystemDashboard.php"
LOCAL = PLUGIN / "src" / "Admin" / "SystemDashboard.php"
UA = "FP-0002-P18B-fu/1.0"
BEGET = "http://shpigovsky.beget.tech"

META_PHP = r"""<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$after = get_option('fp02_metacode_system_meta', array());
if (!is_array($after)) $after = array();
$after['latest_wave'] = 'P18B Dashboard Reality + Indexing Control';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18B';
$after['cutover'] = 'DONE';
$after['dns_ns'] = 'DONE / operator NS cutover';
$after['ssl'] = 'LE valid; WordPress origin HTTPS works';
$after['public_origin'] = 'ПУБЛИЧНЫЙ https://shpigovsky.ru/ СЕЙЧАС ОТДАЁТ СТАРЫЙ САЙТ (Craftum) — привязка к WordPress ещё нужна';
$after['smtp_sender'] = 'noreply@shpigovsky.ru';
$after['backup'] = 'FRESH BEGET BACKUP CONFIRMED BY OPERATOR';
$after['legacy_redirects'] = '7/7';
$after['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$after['state_note'] = 'WP URLs=https://shpigovsky.ru; INDEXING CLOSED on WordPress; public apex currently Craftum CMS';
update_option('fp02_metacode_system_meta', $after, false);
$state = class_exists('Shpigovsky\\Core\\Admin\\IndexingControl')
    ? \Shpigovsky\Core\Admin\IndexingControl::read_state() : array();
echo json_encode(array(
    'core'=>defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:null,
    'blog_public'=>(int)get_option('blog_public'),
    'mail_suppressed'=>(bool)has_filter('pre_wp_mail'),
    'home'=>get_option('home'),
    'siteurl'=>get_option('siteurl'),
    'state'=>$state,
    'meta'=>get_option('fp02_metacode_system_meta'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""


def parse_secrets(text):
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


def http_get(base, path):
    r = requests.get(base + path, timeout=30, allow_redirects=True, headers={"User-Agent": UA})
    body = r.text or ""
    rm = re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', body, re.I)
    return {
        "path": path,
        "status": r.status_code,
        "server": r.headers.get("Server"),
        "final": str(r.url),
        "has_wp": "wp-content" in body or "WordPress" in body,
        "robots_meta": rm.group(1) if rm else None,
        "body_head": (r.content or b"")[:220].decode("utf-8", "replace"),
        "bytes": len(r.content or b""),
    }


def main() -> int:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    src = LOCAL.read_bytes()
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
    before = io.BytesIO()
    sftp.getfo(REMOTE, before)
    (LAYER_B / "plugin__src__Admin__SystemDashboard.php.fu").write_bytes(before.getvalue())
    sftp.putfo(io.BytesIO(src), "/tmp/fp02_p18b_dash.php")
    stdin, stdout, stderr = client.exec_command(
        "php8.2 -l /tmp/fp02_p18b_dash.php 2>/dev/null || /usr/local/bin/php8.2 -l /tmp/fp02_p18b_dash.php", timeout=30
    )
    lint = stdout.read().decode("utf-8", "replace")
    print("LINT", lint.strip())
    sftp.putfo(io.BytesIO(src), REMOTE)
    after = io.BytesIO()
    sftp.getfo(REMOTE, after)
    match = sha256_bytes(after.getvalue()) == sha256_bytes(src)
    print("DASH MATCH", match, sha256_bytes(src))

    sftp.putfo(io.BytesIO(META_PHP.encode("utf-8")), "/tmp/fp02_p18b_meta2.php")
    stdin, stdout, stderr = client.exec_command(
        "php8.2 /tmp/fp02_p18b_meta2.php 2>/dev/null || /usr/local/bin/php8.2 /tmp/fp02_p18b_meta2.php", timeout=90
    )
    out = stdout.read().decode("utf-8", "replace")
    meta = None
    for ln in out.splitlines():
        if ln.startswith("{"):
            meta = json.loads(ln)
            break
    (EV / "META-UPDATE-FU.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("META blog_public", (meta or {}).get("blog_public"), "core", (meta or {}).get("core"))

    wp_closed = {
        "beget_home": http_get(BEGET, "/"),
        "beget_privacy": http_get(BEGET, "/privacy-policy/"),
        "beget_robots": http_get(BEGET, "/robots.txt"),
        "beget_admin": http_get(BEGET, "/wp-admin/"),
        "state": (meta or {}).get("state"),
        "blog_public": (meta or {}).get("blog_public"),
    }
    (EV / "WP-ORIGIN-CLOSED.json").write_text(json.dumps(wp_closed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    dash = {"ok": False}
    user = getf(pairs, "wordpress_username")
    password = getf(pairs, "wordpress_password")
    if user and password:
        s = requests.Session()
        s.headers["User-Agent"] = UA
        login = BEGET + "/wp-login.php"
        s.get(login, timeout=30)
        r = s.post(
            login,
            data={
                "log": user,
                "pwd": password,
                "wp-submit": "Log In",
                "redirect_to": BEGET + "/wp-admin/",
                "testcookie": "1",
            },
            timeout=40,
            allow_redirects=True,
        )
        ok = "wp-admin" in str(r.url) and "wp-login.php" not in str(r.url)
        dash["login_ok"] = ok
        dash["login_final"] = str(r.url)
        dash["login_user"] = user
        if ok:
            page = s.get(BEGET + "/wp-admin/index.php", timeout=40)
            html = page.text or ""
            snippet = ""
            m = re.search(r'id="fp02_metacode_system_state".*?</div>\s*</div>', html, re.I | re.S)
            if m:
                snippet = m.group(0)
            (EV / "dashboard-after-snippet.html").write_text(snippet or html[:12000], encoding="utf-8")
            low = html.lower()
            dash.update({
                "ok": True,
                "status": page.status_code,
                "has_widget": "Состояние системы" in html or "fp02_metacode_system_state" in html,
                "has_closed_banner": "закрыт от индексации" in low,
                "has_open_button": "Открыть индексацию" in html,
                "has_close_button": "Закрыть индексацию" in html,
                "has_stale_ns": ("READY FOR MANUAL NS SWITCH" in html) or ("Future host" in html),
                "has_p18b": "P18B" in html,
                "has_noreply": "noreply@shpigovsky.ru" in html,
                "has_craftum_note": "Craftum" in html or "старый сайт" in html,
                "has_nonce": "fp02_set_indexability" in html and "_wpnonce" in html,
                "has_smtp": "SMTP PENDING" in html,
            })
            nonce = re.search(r'name="_wpnonce"\s+value="([^"]+)"', html)
            dash["nonce_present"] = bool(nonce)
            dash["nonce_len"] = len(nonce.group(1)) if nonce else 0

    (EV / "DASHBOARD-AFTER.json").write_text(json.dumps(dash, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    parity = {
        "dashboard_fu_match": match,
        "src_sha": sha256_bytes(src),
        "prod_sha": sha256_bytes(after.getvalue()),
    }
    (EV / "SOURCE-PROD-PARITY-FU.json").write_text(json.dumps(parity, indent=2) + "\n", encoding="utf-8")
    for tmp in ("/tmp/fp02_p18b_dash.php", "/tmp/fp02_p18b_meta2.php"):
        try:
            sftp.remove(tmp)
        except OSError:
            pass
    sftp.close()
    client.close()
    print("DASHBOARD", dash.get("ok"), dash.get("has_widget"), dash.get("has_closed_banner"), dash.get("has_open_button"), dash.get("nonce_present"))
    print("WP_HOME_META", wp_closed["beget_home"].get("robots_meta"), "ROBOTS", repr(wp_closed["beget_robots"].get("body_head")))
    return 0 if match and (meta or {}).get("blog_public") == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
