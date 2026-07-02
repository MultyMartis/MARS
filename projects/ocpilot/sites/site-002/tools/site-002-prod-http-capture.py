#!/usr/bin/env python3
"""SITE-002 Production HTTP-only capture when FTP unavailable."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

CAPTURE_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01"
)
PRODUCTION_URL = "https://bzpm.ru/"
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-INITIAL-CAPTURE-01 (read-only)"

HTTP_URLS = [
    "/",
    "/robots.txt",
    "/sitemap.xml",
    "/katalog/",
    "/delivery",
    "/payment-methods",
    "/dealers",
    "/guarantee",
    "/custom-equipment",
    "/about",
]


class TitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def http_fetch(url: str) -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            status = resp.status
            final_url = resp.geturl()
            content_type = resp.headers.get("Content-Type")
            content_length = resp.headers.get("Content-Length")
            body = resp.read()
    except urllib.error.HTTPError as exc:
        status = exc.code
        final_url = exc.geturl() if hasattr(exc, "geturl") else url
        content_type = exc.headers.get("Content-Type") if exc.headers else None
        body = exc.read() if exc.fp else b""
        content_length = str(len(body))
    except Exception as exc:
        return {"requested_url": url, "error": str(exc), "timestamp": utc_now()}

    title = canonical = robots_meta = None
    h1_count = 0
    if body and "html" in (content_type or "").lower():
        text = body.decode("utf-8", errors="replace")
        p = TitleParser()
        p.feed(text)
        title = p.title.strip() or None
        m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', text, re.I)
        if m:
            canonical = m.group(1)
        m = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)', text, re.I)
        if m:
            robots_meta = m.group(1)
        h1_count = len(re.findall(r"<h1\b", text, re.I))

    return {
        "requested_url": url,
        "final_url": final_url,
        "status_code": status,
        "redirect_chain": [],
        "content_type": content_type,
        "content_length": int(content_length) if content_length and str(content_length).isdigit() else len(body),
        "title": title,
        "canonical_url": canonical,
        "robots_meta": robots_meta,
        "h1_count": h1_count,
        "body_checksum": sha256_hex(body) if body else None,
        "timestamp": utc_now(),
        "_body": body,
    }


def main() -> None:
    http_dir = CAPTURE_ROOT / "http"
    html_dir = http_dir / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    results = []
    theme_paths: set[str] = set()
    for path in HTTP_URLS:
        url = PRODUCTION_URL.rstrip("/") + path
        r = http_fetch(url)
        body = r.pop("_body", b"")
        if body and "html" in (r.get("content_type") or "").lower():
            name = path.strip("/").replace("/", "_") or "home"
            (html_dir / f"{name}.html").write_bytes(body)
            text = body.decode("utf-8", errors="replace")
            for m in re.finditer(r"/catalog/view/theme/([^/]+)/", text):
                theme_paths.add(m.group(1))
        results.append(r)

    (http_dir / "http-checks.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    with (http_dir / "http-checks.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(results[0].keys()) if results else ["requested_url"])
        w.writeheader()
        for row in results:
            w.writerow(row)

    theme = {
        "active_theme": "default" if "default" in theme_paths else (sorted(theme_paths)[0] if theme_paths else "SAFE UNKNOWN"),
        "theme_root": "catalog/view/theme/default/" if "default" in theme_paths else "SAFE UNKNOWN",
        "confidence": "CONFIRMED" if theme_paths else "SAFE UNKNOWN",
        "evidence": {"html_asset_paths": sorted(theme_paths)},
    }
    manifests = CAPTURE_ROOT / "manifests"
    manifests.mkdir(parents=True, exist_ok=True)
    (manifests / "active-theme-identification.md").write_text(
        f"# Active theme identification\n\n- Active theme: {theme['active_theme']}\n- Confidence: {theme['confidence']}\n- HTML paths: {theme['evidence']['html_asset_paths']}\n",
        encoding="utf-8",
    )

    # Platform from public HTML generator meta
    home = (html_dir / "home.html").read_bytes().decode("utf-8", errors="replace") if (html_dir / "home.html").exists() else ""
    version = None
    for pat in [r"OpenCart\s*([\d.]+)", r"ocStore\s*([\d.]+)", r"generator\" content=\"[^\"]*?([\d.]+)"]:
        m = re.search(pat, home, re.I)
        if m:
            version = m.group(1)
            break
    platform = {
        "platform": "OpenCart / ocStore",
        "distribution": "ocStore" if "ocstore" in home.lower() else "SAFE UNKNOWN",
        "exact_version": version or "SAFE UNKNOWN",
        "confidence": "PROBABLE" if version else "SAFE UNKNOWN",
        "evidence": [{"path": "http/html/home.html", "note": "public HTML metadata"}],
    }
    (manifests / "platform-identification.md").write_text(
        "\n".join(
            [
                "# Platform identification",
                f"- Platform: {platform['platform']}",
                f"- Distribution: {platform['distribution']}",
                f"- Exact version: {platform['exact_version']}",
                f"- Confidence: {platform['confidence']}",
            ]
        ),
        encoding="utf-8",
    )
    (manifests / "platform-identification.json").write_text(json.dumps(platform, indent=2), encoding="utf-8")
    print(f"HTTP checks: {len(results)} URLs")


if __name__ == "__main__":
    main()
