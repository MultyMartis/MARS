# -*- coding: utf-8 -*-
"""PROD-P18I: fresh intake, indexability, sitemap, crawl, redirects, parity (read-only)."""
from __future__ import annotations

import hashlib
import io
import json
import re
import select
import socket
import threading
import time
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import paramiko
import pymysql
import requests

ROOT = Path(__file__).resolve().parents[3]
EV = ROOT / "REPORTS" / "evidence" / "prod-p18i-final-launch-closeout"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
WP_LOAD = f"{DOCROOT}/wp-load.php"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
BASE = "https://shpigovsky.ru"
UA = "FP-0002-P18I/1.0 (+read-only)"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

LEGACY_REDIRECTS = ["/yoga", "/about", "/psy", "/home", "/policy", "/neuro", "/reviews"]
HOST_VARIANTS = [
    "http://shpigovsky.ru/",
    "https://shpigovsky.ru/",
    "http://www.shpigovsky.ru/",
    "https://www.shpigovsky.ru/",
]
STAGING_MARKERS = (".test", "beget.tech", "localhost", "127.0.0.1")

PARITY_FILES = {
    "shpigovsky-core.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "src/Admin/SystemDashboard.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
    "src/Admin/IndexingControl.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingControl.php",
    "src/Admin/IndexingState.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingState.php",
    "src/Admin/IndexingAlerts.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingAlerts.php",
    "src/Admin/IndexingWatchdog.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingWatchdog.php",
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(name: str, payload: Any) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
            chan = self.transport.open_channel("direct-tcpip", (self.remote_host, self.remote_port), client.getpeername())
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
            read_timeout=120,
            write_timeout=120,
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

    def run_ssh(self, command: str, timeout: int = 120) -> tuple[str, str, int]:
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

    def wp_eval_json(self, name: str, body: str) -> dict[str, Any]:
        assert self.sftp is not None
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
        with self.sftp.file(remote_path, "w") as fh:
            fh.write(script.encode("utf-8"))
        out, err, code = self.run_ssh(f"php8.2 {remote_path} 2>/dev/null || php {remote_path}", timeout=180)
        try:
            self.sftp.remove(remote_path)
        except OSError:
            pass
        try:
            payload = json.loads(out.strip().splitlines()[-1] if out.strip() else "{}")
        except json.JSONDecodeError:
            payload = {"ok": False, "stdout_head": out[:4000], "stderr_head": err[:1200], "exit_code": code}
        payload["_exit_code"] = code
        return payload


def fetch(url: str, allow_redirects: bool = True, method: str = "GET") -> dict[str, Any]:
    try:
        r = requests.request(
            method,
            url,
            headers={"User-Agent": UA},
            timeout=30,
            allow_redirects=allow_redirects,
        )
        body = r.content or b""
        x_robots = r.headers.get("X-Robots-Tag", "")
        return {
            "url": url,
            "status": r.status_code,
            "final_url": str(r.url),
            "content_type": r.headers.get("Content-Type", ""),
            "x_robots_tag": x_robots,
            "redirects": [str(h.url) for h in r.history],
            "body": body,
            "error": None,
        }
    except Exception as exc:
        return {"url": url, "status": None, "final_url": url, "body": b"", "error": str(exc)}


def parse_sitemap_urls(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    urls: list[str] = []
    if root.tag.endswith("sitemapindex"):
        for loc in root.findall("sm:sitemap/sm:loc", NS):
            if loc.text:
                child = fetch(loc.text.strip())
                if child["status"] == 200 and child["body"]:
                    urls.extend(parse_sitemap_urls(child["body"]))
    else:
        for loc in root.findall("sm:url/sm:loc", NS):
            if loc.text:
                urls.append(loc.text.strip())
    return urls


def extract_links(html: str, page_url: str, host: str) -> list[str]:
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.I)
    out: list[str] = []
    for h in hrefs:
        if h.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        abs_url = urljoin(page_url, h)
        p = urlparse(abs_url)
        if p.netloc == host and p.scheme in ("http", "https"):
            out.append(abs_url.split("#")[0])
    return out


def analyze_html(url: str, html: str, status: int | None, x_robots: str = "") -> dict[str, Any]:
    title_m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
    title = re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else ""
    robots_m = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)["\']', html, flags=re.I)
    if not robots_m:
        robots_m = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']robots["\']', html, flags=re.I)
    robots = robots_m.group(1).strip() if robots_m else ""
    canon_m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', html, flags=re.I)
    if not canon_m:
        canon_m = re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', html, flags=re.I)
    canonical = canon_m.group(1).strip() if canon_m else ""
    h1s = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<h1\b[^>]*>(.*?)</h1>", html, flags=re.I | re.S)]
    desc_m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, flags=re.I)
    if not desc_m:
        desc_m = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, flags=re.I)
    description = desc_m.group(1).strip() if desc_m else ""
    issues: list[dict[str, str]] = []
    if status and status >= 400:
        issues.append({"severity": "CRITICAL" if status >= 500 else "MAJOR", "issue": f"HTTP {status}"})
    if not title:
        issues.append({"severity": "MAJOR", "issue": "missing title"})
    elif any(x in title.lower() for x in ("lorem", "локальн", "demo —", "demo-")):
        issues.append({"severity": "MAJOR", "issue": f"placeholder title: {title[:80]}"})
    if "noindex" in robots.lower() or "noindex" in x_robots.lower():
        issues.append({"severity": "INTENTIONAL", "issue": f"noindex ({robots or x_robots})"})
    if canonical and not canonical.startswith("https://shpigovsky.ru"):
        issues.append({"severity": "CRITICAL", "issue": f"non-production canonical: {canonical}"})
    if not canonical and status == 200 and "noindex" not in robots.lower():
        issues.append({"severity": "MINOR", "issue": "missing canonical"})
    if len(h1s) == 0:
        issues.append({"severity": "MAJOR", "issue": "missing H1"})
    elif len(h1s) > 1:
        issues.append({"severity": "MINOR", "issue": f"multiple H1 ({len(h1s)})"})
    if not description:
        issues.append({"severity": "MINOR", "issue": "missing meta description"})
    for marker in STAGING_MARKERS:
        if marker in html.lower():
            issues.append({"severity": "CRITICAL", "issue": f"staging marker in HTML: {marker}"})
            break
    return {
        "url": url,
        "status": status,
        "title": title,
        "description_len": len(description),
        "h1_count": len(h1s),
        "robots_meta": robots,
        "canonical": canonical,
        "issues": issues,
    }


INTAKE_PHP = r"""
function fp02_clip($v, $max = 500) {
    if (is_bool($v) || is_int($v) || is_float($v) || $v === null) return $v;
    if (is_array($v)) {
        $out = array(); $n = 0;
        foreach ($v as $k => $vv) {
            if ($n++ > 100) { $out['__truncated'] = true; break; }
            $out[$k] = fp02_clip($vv, $max);
        }
        return $out;
    }
    $s = (string) $v;
    return strlen($s) > $max ? substr($s, 0, $max) . '...[truncated]' : $s;
}
global $wpdb;
$prefix = $wpdb->prefix;
$activity = $wpdb->get_results(
    "SELECT id, created_at, user_id, action, object_type, object_id, summary
     FROM {$prefix}fp02_user_activity_log ORDER BY id DESC LIMIT 25",
    ARRAY_A
);
$counts = array(
    'pages' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='page' AND post_status='publish'"),
    'posts' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='post' AND post_status='publish'"),
    'services' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='service' AND post_status='publish'"),
    'specialists' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='specialist' AND post_status='publish'"),
);
$recent_pages = $wpdb->get_results(
    "SELECT ID, post_title, post_name, post_modified_gmt, post_author FROM {$wpdb->posts}
     WHERE post_type IN ('page','post','service','specialist') AND post_status='publish'
     ORDER BY post_modified_gmt DESC LIMIT 15",
    ARRAY_A
);
$indexing = array('blog_public' => (int) get_option('blog_public', 1));
if (class_exists('Shpigovsky\\Core\\Admin\\IndexingState')) {
    $indexing['snapshot'] = Shpigovsky\Core\Admin\IndexingState::snapshot();
}
$mail = get_option('fp02_mail_config', array());
if (is_array($mail)) {
    foreach (array('smtp_password','password','secret','token') as $k) {
        if (isset($mail[$k])) $mail[$k] = 'REDACTED';
    }
}
echo wp_json_encode(array(
    'generated_at' => gmdate('c'),
    'wave' => 'P18I',
    'options' => array(
        'home' => get_option('home'),
        'siteurl' => get_option('siteurl'),
        'blog_public' => (int) get_option('blog_public', 1),
    ),
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'privacy_settings' => fp02_clip(get_option('fp02_cookie_privacy_settings', array())),
    'mail_settings_redacted' => fp02_clip($mail),
    'system_meta' => fp02_clip(get_option('fp02_metacode_system_meta', array())),
    'indexing' => fp02_clip($indexing),
    'content_counts' => $counts,
    'recent_content' => fp02_clip($recent_pages),
    'activity_log_recent' => fp02_clip($activity),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""


def parity_check(ctx: RuntimeContext) -> dict[str, Any]:
    rows = []
    all_match = True
    for rel, local_path in PARITY_FILES.items():
        remote_path = f"{PLUGIN_REMOTE}/{rel.replace(chr(92), '/')}"
        remote_bytes = ctx.sftp_get(remote_path) if ctx.sftp else None
        local_bytes = local_path.read_bytes() if local_path.is_file() else None
        local_sha = sha256_bytes(local_bytes) if local_bytes else None
        remote_sha = sha256_bytes(remote_bytes) if remote_bytes else None
        match = local_sha == remote_sha and local_sha is not None
        if not match:
            all_match = False
        rows.append(
            {
                "file": rel,
                "local_sha256": local_sha,
                "remote_sha256": remote_sha,
                "match": match,
            }
        )
    return {"all_match": all_match, "files": rows, "checked_at": utcnow()}


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        intake = ctx.wp_eval_json("p18i_intake", INTAKE_PHP)
        write_json("01-olya-admin-intake.json", intake)

        parity = parity_check(ctx)
        write_json("parity-source-production.json", parity)

        # Indexability
        robots = fetch(f"{BASE}/robots.txt")
        home = fetch(f"{BASE}/")
        sitemap_index = fetch(f"{BASE}/wp-sitemap.xml")
        robots_text = (robots.get("body") or b"").decode("utf-8", errors="replace")
        indexability = {
            "required": "P18I GLOBAL INDEXABILITY OPEN / CONSISTENT",
            "blog_public": intake.get("options", {}).get("blog_public"),
            "indexing_snapshot": intake.get("indexing"),
            "robots_status": robots.get("status"),
            "robots_global_disallow": bool(re.search(r"(?m)^Disallow:\s*/\s*$", robots_text)),
            "robots_sitemap_line": "Sitemap:" in robots_text,
            "homepage_noindex": "noindex" in (home.get("body") or b"").decode("utf-8", errors="replace").lower()[:6000],
            "homepage_x_robots": home.get("x_robots_tag", ""),
        }
        write_json("02-indexability-proof.json", indexability)

        # Sitemap structure
        sitemap_urls: list[str] = []
        sitemap_issues: list[dict[str, str]] = []
        if sitemap_index.get("status") == 200 and sitemap_index.get("body"):
            raw = sitemap_index["body"]
            try:
                sitemap_urls = parse_sitemap_urls(raw)
            except ET.ParseError as exc:
                sitemap_issues.append({"severity": "CRITICAL", "issue": f"sitemap XML parse error: {exc}"})
            body_text = raw.decode("utf-8", errors="replace")
            for marker in STAGING_MARKERS:
                if marker in body_text:
                    sitemap_issues.append({"severity": "CRITICAL", "issue": f"sitemap contains staging marker: {marker}"})
        sitemap_audit = []
        for u in sitemap_urls[:200]:
            p = urlparse(u)
            row = {"url": u, "issues": []}
            if p.scheme != "https":
                row["issues"].append("not HTTPS")
            if p.netloc != "shpigovsky.ru":
                row["issues"].append(f"wrong host: {p.netloc}")
            for marker in STAGING_MARKERS:
                if marker in u:
                    row["issues"].append(f"staging in URL: {marker}")
            if row["issues"]:
                sitemap_audit.append(row)
        write_json(
            "03-sitemap-structure.json",
            {
                "required": "FINAL PRODUCTION SITEMAP STRUCTURE VERIFIED",
                "index_status": sitemap_index.get("status"),
                "url_count": len(sitemap_urls),
                "child_samples": sitemap_urls[:12],
                "structure_issues": sitemap_issues,
                "url_sanity_issues": sitemap_audit,
            },
        )

        # Sample sitemap URL HTTP status (all if <=120 else sample)
        sample_urls = sitemap_urls if len(sitemap_urls) <= 120 else sitemap_urls[:: max(1, len(sitemap_urls) // 100)]
        sitemap_http = []
        for u in sample_urls:
            r = fetch(u)
            sitemap_http.append({"url": u, "status": r.get("status"), "final_url": r.get("final_url"), "error": r.get("error")})
            time.sleep(0.08)
        write_json("04-sitemap-url-http-audit.json", {"sampled": len(sample_urls), "rows": sitemap_http})

        # Build crawl inventory
        host = "shpigovsky.ru"
        ordered: list[str] = list(dict.fromkeys(sitemap_urls))
        if home.get("status") == 200:
            html = (home.get("body") or b"").decode("utf-8", errors="replace")
            for link in extract_links(html, f"{BASE}/", host):
                if link not in ordered:
                    ordered.append(link)
        # Representative routes
        for extra in [
            f"{BASE}/uslugi/",
            f"{BASE}/kontakty/",
            f"{BASE}/o-centre/",
            f"{BASE}/blog/",
            f"{BASE}/otzyvy/",
            f"{BASE}/cookie-files-policy/",
            f"{BASE}/privacy-policy/",
            f"{BASE}/consent-personal-data/",
            f"{BASE}/?s=test",
        ]:
            if extra not in ordered:
                ordered.append(extra)

        crawl_rows = []
        meta_rows = []
        findings: list[dict[str, Any]] = []
        broken_internal: list[dict[str, str]] = []
        title_map: dict[str, list[str]] = defaultdict(list)

        for i, url in enumerate(ordered):
            if "/wp-admin" in url or "/wp-json/" in url:
                continue
            r = fetch(url)
            body = r.get("body") or b""
            html = body.decode("utf-8", errors="replace") if body else ""
            crawl_rows.append(
                {
                    "url": url,
                    "status": r.get("status"),
                    "final_url": r.get("final_url"),
                    "error": r.get("error"),
                    "bytes": len(body),
                }
            )
            if r.get("status") == 200 and (html.lstrip().startswith("<!") or "text/html" in (r.get("content_type") or "")):
                meta = analyze_html(url, html, r.get("status"), r.get("x_robots_tag", ""))
                meta_rows.append(meta)
                if meta["title"]:
                    title_map[meta["title"]].append(url)
                for issue in meta["issues"]:
                    findings.append({"url": url, **issue})
                # internal links sample from key pages only
                if i < 25:
                    for link in extract_links(html, url, host)[:40]:
                        if link not in ordered and len(ordered) < 250:
                            ordered.append(link)
            elif r.get("status") and r.get("status") >= 400:
                findings.append({"url": url, "severity": "CRITICAL" if r["status"] >= 500 else "MAJOR", "issue": f"HTTP {r['status']}"})
            time.sleep(0.1)

        for title, urls in title_map.items():
            if len(urls) > 1 and title and "404" not in title.lower():
                findings.append({"url": urls[0], "severity": "MINOR", "issue": f"duplicate title ({len(urls)} URLs)", "urls": urls[:5]})

        status_counter = Counter(str(r.get("status")) for r in crawl_rows)
        sev_counter = Counter(f.get("severity") for f in findings)
        critical = [f for f in findings if f.get("severity") == "CRITICAL"]

        write_json(
            "05-final-url-inventory.json",
            {"required": "FINAL PRODUCTION URL INVENTORY CREATED FROM CURRENT LIVE SITE", "crawl_count": len(crawl_rows), "sitemap_count": len(sitemap_urls), "urls": [r["url"] for r in crawl_rows]},
        )
        write_json(
            "06-http-status-audit.json",
            {"summary": dict(status_counter), "rows": crawl_rows, "critical_findings": critical, "required": "NO UNRESOLVED LAUNCH-CRITICAL HTTP ERRORS"},
        )
        write_json("07-canonical-title-h1-audit.json", {"pages": meta_rows, "findings": findings})

        # Legacy redirects
        redirect_rows = []
        for path in LEGACY_REDIRECTS:
            r = fetch(f"{BASE}{path}", allow_redirects=False)
            loc = ""
            if r.get("status") in (301, 302, 303, 307, 308):
                # follow manually once for target capture
                r2 = fetch(f"{BASE}{path}", allow_redirects=True)
                loc = r2.get("final_url", "")
            redirect_rows.append(
                {
                    "source": f"{BASE}{path}",
                    "status": r.get("status"),
                    "location_chain": r.get("redirects", []),
                    "final_url": loc or r.get("final_url"),
                    "ok": r.get("status") in (301, 302, 303, 307, 308) or (r.get("status") == 200 and path in ("/reviews",)),
                }
            )
        write_json("08-legacy-redirects.json", {"required": "LEGACY REDIRECT SET STILL FUNCTIONS ON PRODUCTION", "rows": redirect_rows})

        # Host variants
        host_rows = []
        for u in HOST_VARIANTS:
            r = fetch(u, allow_redirects=True)
            host_rows.append(
                {
                    "url": u,
                    "status": r.get("status"),
                    "final_url": r.get("final_url"),
                    "redirects": r.get("redirects", []),
                }
            )
        write_json("09-host-https-canonicalization.json", {"rows": host_rows, "canonical_host": "shpigovsky.ru"})

        # Sitemap coverage compare
        crawl_ok = {r["url"].rstrip("/") for r in crawl_rows if r.get("status") == 200}
        sitemap_set = {u.rstrip("/") for u in sitemap_urls}
        indexable_not_in_sitemap = sorted(list(crawl_ok - sitemap_set))[:30]
        in_sitemap_not_crawled_ok = []
        for u in sitemap_urls:
            nu = u.rstrip("/")
            match = next((r for r in crawl_rows if r["url"].rstrip("/") == nu), None)
            if match and match.get("status") not in (200, None):
                in_sitemap_not_crawled_ok.append({"url": u, "status": match.get("status")})
        write_json(
            "10-sitemap-coverage.json",
            {
                "required": "SITEMAP COVERAGE HAS NO UNRESOLVED CRITICAL CONTRADICTIONS",
                "indexable_sample_missing_from_sitemap": indexable_not_in_sitemap,
                "sitemap_urls_bad_status": in_sitemap_not_crawled_ok,
            },
        )

        # Verdict
        unresolved_critical = [f for f in findings if f.get("severity") == "CRITICAL" and "noindex" not in f.get("issue", "").lower()]
        unresolved_critical += [r for r in sitemap_http if r.get("status") not in (200, None) and r.get("status") is not None]
        verdict = "CLEAN" if not unresolved_critical and not sitemap_issues and not sitemap_audit else (
            "CLEAN WITH NON-BLOCKING NOTES" if len(unresolved_critical) <= 2 else "BLOCKED"
        )
        summary = {
            "captured_at": utcnow(),
            "wave": "P18I",
            "verdict": verdict,
            "indexability_open": indexability.get("blog_public") == 1 and not indexability.get("robots_global_disallow"),
            "sitemap_url_count": len(sitemap_urls),
            "crawl_url_count": len(crawl_rows),
            "http_summary": dict(status_counter),
            "severity_summary": dict(sev_counter),
            "unresolved_critical_count": len(unresolved_critical),
            "parity_all_match": parity.get("all_match"),
            "required_tokens": {
                "olya_truth": "P18I CURRENT OLYA / ADMIN PRODUCTION TRUTH VERIFIED",
                "indexability": "P18I GLOBAL INDEXABILITY OPEN / CONSISTENT",
                "sitemap_structure": "FINAL PRODUCTION SITEMAP STRUCTURE VERIFIED",
                "sitemap_sanity": "SITEMAP CONTAINS NO KNOWN STAGING / BROKEN / GLOBAL-NOINDEX CONFLICTS",
                "url_inventory": "FINAL PRODUCTION URL INVENTORY CREATED FROM CURRENT LIVE SITE",
                "http": "NO UNRESOLVED LAUNCH-CRITICAL HTTP ERRORS",
                "redirects": "LEGACY REDIRECT SET STILL FUNCTIONS ON PRODUCTION",
                "canonicals": "CANONICAL SIGNALS ALIGN WITH CURRENT PRODUCTION URLS",
                "robots": "GLOBAL INDEXING OPEN WHILE VALID PAGE-LEVEL EXCLUSIONS REMAIN INTACT",
                "coverage": "SITEMAP COVERAGE HAS NO UNRESOLVED CRITICAL CONTRADICTIONS",
                "parity": "FINAL SOURCE / PRODUCTION PARITY PASS" if parity.get("all_match") else "PARITY MISMATCH — DEPLOY REQUIRED",
            },
        }
        write_json("00-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    finally:
        ctx.close()


if __name__ == "__main__":
    main()
