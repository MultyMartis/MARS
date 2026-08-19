from __future__ import annotations

import hashlib
import io
import json
import re
import select
import socket
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import paramiko
import pymysql
import requests

ROOT = Path(r"X:\AI MARS STORAGE\worktrees\fp0002-p18e-ab-consent-foundation\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = ROOT / "REPORTS" / "evidence" / "prod-p18e-ab-consent-foundation"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
WP_LOAD = f"{DOCROOT}/wp-load.php"
UA = "FP-0002-P18E-AB-intake/1.0"

PUBLIC_PAGES = {
    "home": "https://shpigovsky.ru/",
    "contacts": "https://shpigovsky.ru/kontakty/",
    "privacy": "https://shpigovsky.ru/policy/",
    "cookie_policy": "https://shpigovsky.ru/cookie-files-policy/",
    "consent_personal_data": "https://shpigovsky.ru/consent-personal-data/",
}

REMOTE_FILES = {
    "theme_seo_integrations": f"{DOCROOT}/wp-content/themes/shpigovsky/inc/seo-integrations.php",
    "theme_shell_js": f"{DOCROOT}/wp-content/themes/shpigovsky/assets/js/v9-shell.js",
    "theme_footer": f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/layout/footer.php",
    "core_options_page": f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php",
    "core_dashboard": f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
    "core_activity_log": f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/ActivityLog.php",
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


def write_text(name: str, text: str) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(text, encoding="utf-8")


class LocalForward:
    def __init__(self, transport: paramiko.Transport, remote_host: str, remote_port: int):
        self.transport = transport
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(4)
        self.local_port = self.sock.getsockname()[1]
        self._stop = False
        threading.Thread(target=self._accept, daemon=True).start()

    def _accept(self) -> None:
        while not self._stop:
            ready, _, _ = select.select([self.sock], [], [], 0.5)
            if not ready:
                continue
            try:
                client, _ = self.sock.accept()
            except OSError:
                return
            threading.Thread(target=self._forward, args=(client,), daemon=True).start()

    def _forward(self, client: socket.socket) -> None:
        try:
            chan = self.transport.open_channel(
                "direct-tcpip",
                (self.remote_host, self.remote_port),
                client.getpeername(),
            )
        except Exception:
            client.close()
            return
        try:
            while True:
                ready, _, _ = select.select([client, chan], [], [], 30)
                if client in ready:
                    data = client.recv(65536)
                    if not data:
                        break
                    chan.sendall(data)
                if chan in ready:
                    data = chan.recv(65536)
                    if not data:
                        break
                    client.sendall(data)
        finally:
            client.close()
            chan.close()

    def close(self) -> None:
        self._stop = True
        try:
            self.sock.close()
        except OSError:
            pass


class RuntimeContext:
    def __init__(self) -> None:
        self.pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
        self.client: paramiko.SSHClient | None = None
        self.sftp: paramiko.SFTPClient | None = None
        self.db_conn: pymysql.Connection | None = None
        self.db_fwd: LocalForward | None = None

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
        fwd = LocalForward(client.get_transport(), "127.0.0.1", 3306)
        time.sleep(0.3)
        self.db_conn = pymysql.connect(
            host="127.0.0.1",
            port=fwd.local_port,
            user=getf(self.pairs, "db_user"),
            password=getf(self.pairs, "db_password"),
            database=getf(self.pairs, "db_name"),
            charset="utf8mb4",
            autocommit=True,
            connect_timeout=30,
            read_timeout=90,
            write_timeout=90,
        )
        self.db_fwd = fwd

    def close(self) -> None:
        if self.db_conn:
            self.db_conn.close()
        if self.db_fwd:
            self.db_fwd.close()
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()

    def run_ssh(self, command: str, timeout: int = 90) -> tuple[str, str, int]:
        assert self.client is not None
        stdin, stdout, stderr = self.client.exec_command(command, timeout=timeout)
        return (
            stdout.read().decode("utf-8", errors="replace"),
            stderr.read().decode("utf-8", errors="replace"),
            stdout.channel.recv_exit_status(),
        )

    def sftp_get(self, remote_path: str) -> bytes | None:
        assert self.sftp is not None
        try:
            buffer = io.BytesIO()
            self.sftp.getfo(remote_path, buffer)
            return buffer.getvalue()
        except (FileNotFoundError, OSError):
            return None

    def sftp_put_bytes(self, remote_path: str, payload: bytes) -> None:
        assert self.sftp is not None
        with self.sftp.file(remote_path, "wb") as fh:
            fh.write(payload)

    def sftp_remove(self, remote_path: str) -> None:
        assert self.sftp is not None
        self.sftp.remove(remote_path)

    def wp_eval_json(self, name: str, body: str) -> dict[str, Any]:
        remote_path = f"/tmp/fp02_{name}_{int(time.time())}.php"
        script = f"""<?php
error_reporting(E_ALL);
ini_set('display_errors', '0');
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['HTTPS'] = 'on';
require '{WP_LOAD}';
header('Content-Type: application/json; charset=utf-8');
{body}
"""
        self.sftp_put_bytes(remote_path, script.encode("utf-8"))
        out, err, code = self.run_ssh(f"php8.2 {remote_path} 2>/dev/null || php {remote_path}", timeout=120)
        try:
            self.sftp_remove(remote_path)
        except OSError:
            pass
        try:
            payload = json.loads(out.strip().splitlines()[-1] if out.strip() else "{}")
        except json.JSONDecodeError:
            payload = {
                "ok": False,
                "stdout_head": out[:4000],
                "stderr_head": err[:1200],
                "exit_code": code,
            }
        if err.strip():
            payload["_stderr_head"] = err[:1200]
        payload["_exit_code"] = code
        return payload


def summarize_markers(text: str) -> dict[str, Any]:
    lower = text.lower()
    return {
        "yandex_metrika": "mc.yandex.ru" in lower or "ym(" in lower,
        "google_tag_manager": "googletagmanager.com" in lower or "gtm-" in lower,
        "google_analytics": "gtag/js" in lower or "google-analytics.com" in lower,
        "google_fonts": "fonts.googleapis.com" in lower or "fonts.gstatic.com" in lower,
        "facebook_pixel": "connect.facebook.net" in lower or "fbq(" in lower,
        "vk_pixel": "vk.com/js/api/openapi.js" in lower or "vk.com/rtrg" in lower,
        "calltracking": "calltouch" in lower or "callibri" in lower or "calltracking" in lower,
        "cookiebot": "cookiebot" in lower,
        "onetrust": "onetrust" in lower,
        "recaptcha": "www.google.com/recaptcha" in lower or "grecaptcha" in lower,
        "yandex_map": "api-maps.yandex.ru" in lower or "constructor" in lower and "yandex" in lower,
        "youtube": "youtube.com" in lower or "youtu.be" in lower,
        "rutube": "rutube.ru" in lower,
        "vimeo": "player.vimeo.com" in lower,
    }


def public_probe(url: str) -> dict[str, Any]:
    try:
        response = requests.get(
            url,
            timeout=30,
            allow_redirects=True,
            headers={"User-Agent": UA, "Accept-Language": "ru-RU,ru;q=0.9"},
        )
        body = response.text or ""
        scripts = sorted(set(re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', body, flags=re.I)))
        iframes = sorted(set(re.findall(r'<iframe[^>]+src=["\']([^"\']+)["\']', body, flags=re.I)))
        links = sorted(set(re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', body, flags=re.I)))
        return {
            "url": url,
            "status": response.status_code,
            "final_url": str(response.url),
            "content_type": response.headers.get("Content-Type"),
            "x_robots": response.headers.get("X-Robots-Tag"),
            "body_bytes": len(response.content or b""),
            "script_srcs": scripts,
            "iframe_srcs": iframes,
            "link_hrefs": links,
            "markers": summarize_markers(body),
            "contains_fp02_utm": "fp02_utm" in body,
            "contains_cookie_policy_phrase": "cookie" in body.lower(),
            "contains_demo_phrase": "demo" in body.lower() or "баннер" in body.lower(),
            "body_head": body[:2000],
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "error": type(exc).__name__, "detail": str(exc)}


def collect_public_runtime() -> dict[str, Any]:
    return {name: public_probe(url) for name, url in PUBLIC_PAGES.items()}


def collect_db_state(ctx: RuntimeContext) -> dict[str, Any]:
    assert ctx.db_conn is not None
    prefix = getf(ctx.pairs, "db_table_prefix") or "fp02_"
    activity_table = f"{prefix}user_activity_log"
    posts_table = f"{prefix}posts"
    postmeta_table = f"{prefix}postmeta"
    out: dict[str, Any] = {"utc": utcnow()}

    with ctx.db_conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT l.id, l.created_at, l.action, l.object_type, l.object_id, l.object_title, l.object_status,
                   COALESCE(u.user_login, 'system') AS user_login
            FROM {activity_table} l
            LEFT JOIN {prefix}users u ON u.ID = l.user_id
            ORDER BY l.id DESC
            LIMIT 100
            """
        )
        out["activity_recent"] = [
            {
                "id": int(row[0]),
                "created_at": str(row[1]),
                "action": row[2],
                "object_type": row[3],
                "object_id": int(row[4]),
                "object_title": row[5],
                "object_status": row[6],
                "user_login": row[7],
            }
            for row in cur.fetchall()
        ]

        cur.execute(
            f"""
            SELECT ID, post_name, post_title, post_status, post_modified_gmt
            FROM {posts_table}
            WHERE post_type = 'page'
              AND post_name IN ('policy', 'cookie-files-policy', 'consent-personal-data')
            ORDER BY FIELD(post_name, 'policy', 'cookie-files-policy', 'consent-personal-data')
            """
        )
        out["legal_pages"] = [
            {
                "id": int(row[0]),
                "slug": row[1],
                "title": row[2],
                "status": row[3],
                "modified_gmt": str(row[4]),
            }
            for row in cur.fetchall()
        ]

        cur.execute(
            f"""
            SELECT p.ID, p.post_title, p.post_status
            FROM {posts_table} p
            INNER JOIN {postmeta_table} pm ON pm.post_id = p.ID
            WHERE pm.meta_key = '_wp_page_template'
              AND pm.meta_value LIKE '%contacts%'
            ORDER BY p.ID ASC
            LIMIT 20
            """
        )
        out["contacts_page_candidates"] = [
            {"id": int(row[0]), "title": row[1], "status": row[2]}
            for row in cur.fetchall()
        ]
    return out


def collect_wp_state(ctx: RuntimeContext) -> dict[str, Any]:
    php = r"""
$pages = array();
foreach (array('policy', 'cookie-files-policy', 'consent-personal-data') as $slug) {
    $page = get_page_by_path($slug, OBJECT, 'page');
    if ($page instanceof WP_Post) {
        $content = (string) $page->post_content;
        $pages[$slug] = array(
            'id' => (int) $page->ID,
            'title' => get_the_title($page),
            'status' => (string) $page->post_status,
            'modified_gmt' => (string) $page->post_modified_gmt,
            'content_length' => strlen($content),
            'contains_demo' => (false !== stripos($content, 'demo')) || (false !== stripos($content, 'placeholder')),
            'contains_banner_not_implemented' => (false !== stripos($content, 'не реализован')) || (false !== stripos($content, 'не implemented')),
        );
    }
}
$custom_head = (string) get_option('options_custom_head_code', '');
$custom_body = (string) get_option('options_custom_body_open_code', '');
$custom_footer = (string) get_option('options_custom_footer_code', '');
$counter = function_exists('get_field') ? get_field('yandex_metrica_counter_id', 'option') : '';
$meta = get_option('fp02_metacode_system_meta', array());
if (! is_array($meta)) {
    $meta = array();
}
echo wp_json_encode(array(
    'ok' => true,
    'home' => get_option('home'),
    'siteurl' => get_option('siteurl'),
    'blog_public' => (int) get_option('blog_public'),
    'counter_id' => preg_replace('/\D+/', '', (string) $counter),
    'custom_code' => array(
        'head_length' => strlen($custom_head),
        'body_open_length' => strlen($custom_body),
        'footer_length' => strlen($custom_footer),
        'head_sha256' => hash('sha256', $custom_head),
        'body_open_sha256' => hash('sha256', $custom_body),
        'footer_sha256' => hash('sha256', $custom_footer),
        'head_markers' => array(
            'yandex' => false !== stripos($custom_head, 'yandex'),
            'google' => false !== stripos($custom_head, 'google'),
            'gtm' => false !== stripos($custom_head, 'GTM-'),
            'facebook' => false !== stripos($custom_head, 'facebook'),
        ),
        'body_markers' => array(
            'yandex' => false !== stripos($custom_body, 'yandex'),
            'google' => false !== stripos($custom_body, 'google'),
            'gtm' => false !== stripos($custom_body, 'GTM-'),
            'facebook' => false !== stripos($custom_body, 'facebook'),
        ),
        'footer_markers' => array(
            'yandex' => false !== stripos($custom_footer, 'yandex'),
            'google' => false !== stripos($custom_footer, 'google'),
            'gtm' => false !== stripos($custom_footer, 'GTM-'),
            'facebook' => false !== stripos($custom_footer, 'facebook'),
        ),
    ),
    'dashboard_meta' => $meta,
    'pages' => $pages,
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""
    return ctx.wp_eval_json("p18eab_wp_state", php)


def collect_file_reality(ctx: RuntimeContext) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, remote_path in REMOTE_FILES.items():
        data = ctx.sftp_get(remote_path)
        if data is None:
            out[key] = {"exists": False, "remote_path": remote_path}
            continue
        text = data.decode("utf-8", errors="replace")
        out[key] = {
            "exists": True,
            "remote_path": remote_path,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "markers": summarize_markers(text),
            "contains_fp02_utm": "fp02_utm" in text,
            "contains_reach_goal": "reachGoal" in text,
            "contains_cookie_consent": "cookie_consent" in text or "PrivacyConsent" in text or "CookieConsent" in text,
            "head": text[:1600],
        }
    return out


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        public = collect_public_runtime()
        wp_state = collect_wp_state(ctx)
        db_state = collect_db_state(ctx)
        file_reality = collect_file_reality(ctx)

        write_json("01-public-runtime.json", public)
        write_json("02-wp-state.json", wp_state)
        write_json("03-db-state.json", db_state)
        write_json("04-file-reality.json", file_reality)

        summary = {
            "utc": utcnow(),
            "required_olya_truth": "P18E-A CURRENT OLYA / ADMIN PRODUCTION TRUTH VERIFIED",
            "required_tracker_truth": "P18E-A TRACKER / STORAGE REALITY RECONFIRMED",
            "counter_id": wp_state.get("counter_id"),
            "blog_public": wp_state.get("blog_public"),
            "public_home_status": public.get("home", {}).get("status"),
            "public_home_yandex_metrika": public.get("home", {}).get("markers", {}).get("yandex_metrika"),
            "public_contacts_yandex_map": public.get("contacts", {}).get("markers", {}).get("yandex_map"),
            "public_any_recaptcha_marker": any(
                page.get("markers", {}).get("recaptcha")
                for page in public.values()
                if isinstance(page, dict)
            ),
            "custom_code_lengths": wp_state.get("custom_code"),
            "activity_rows": len(db_state.get("activity_recent", [])),
            "legal_pages": wp_state.get("pages", {}),
            "theme_metrika_owner_present": file_reality.get("theme_seo_integrations", {}).get("markers", {}).get("yandex_metrika"),
            "theme_utm_owner_present": file_reality.get("theme_shell_js", {}).get("contains_fp02_utm"),
            "theme_goal_owner_present": file_reality.get("theme_shell_js", {}).get("contains_reach_goal"),
        }
        write_json("00-summary.json", summary)

        human = [
            "# P18E-A Read-only Intake Summary",
            "",
            f"- UTC: {summary['utc']}",
            f"- Counter ID: {summary['counter_id']}",
            f"- Indexing (`blog_public`): {summary['blog_public']}",
            f"- Homepage Yandex Metrika detected: {summary['public_home_yandex_metrika']}",
            f"- Contacts Yandex map markers detected: {summary['public_contacts_yandex_map']}",
            f"- Public reCAPTCHA markers detected: {summary['public_any_recaptcha_marker']}",
            f"- Theme Metrika owner present: {summary['theme_metrika_owner_present']}",
            f"- Theme UTM owner present: {summary['theme_utm_owner_present']}",
            f"- Theme goal owner present: {summary['theme_goal_owner_present']}",
            "",
            "Required:",
            "- P18E-A CURRENT OLYA / ADMIN PRODUCTION TRUTH VERIFIED",
            "- P18E-A TRACKER / STORAGE REALITY RECONFIRMED",
        ]
        write_text("SUMMARY.md", "\n".join(human) + "\n")
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())
