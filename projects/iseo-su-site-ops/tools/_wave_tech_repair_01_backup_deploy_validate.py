#!/usr/bin/env python3
"""ISEO-SU TECH REPAIR WAVE 01: backup, deploy page-home.php + blog.html, validate."""
from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SITE = "https://i-seo.su"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
SRC = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source")
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_tech-repair-wave-01")
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_wave_tech_repair_01_deploy_validate.json")

MAP = [
    (
        SRC / "theme/iseoblog/page-home.php",
        f"{DOC}/wp-content/themes/iseoblog/page-home.php",
    ),
    (
        SRC / "static-html/blog.html",
        f"{DOC}/blog.html",
    ),
]

AUTHORS = ["admin", "denis", "ilya", "manager3", "mars", "olya"]
SMOKE = [
    f"{SITE}/",
    f"{SITE}/blog/",
    f"{SITE}/blog.html",
    f"{SITE}/blog/category/seo/",
]
INTENDED_CSS = [
    f"{SITE}/css/normalize.css",
    f"{SITE}/css/main.css",
    f"{SITE}/css/media.css",
    f"{SITE}/libs/owl/owl.carousel.min.css",
    f"{SITE}/libs/owl/owl.theme.default.min.css",
    f"{SITE}/libs/fancybox/jquery.fancybox.min.css",
]
BAD_CSS_PREFIX = f"{SITE}/blog/author/css/"
BAD_LIBS_PREFIX = f"{SITE}/blog/author/libs/"


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sftp_connect():
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"], password=secrets["ftp_or_sftp_password"]
    )
    return paramiko.SFTPClient.from_transport(transport), transport


def read_remote_bytes(sftp, path: str) -> bytes:
    with sftp.open(path, "r") as f:
        return f.read()


def write_remote_bytes(sftp, path: str, data: bytes) -> None:
    with sftp.open(path, "w") as f:
        f.write(data)


def http_get(url: str, follow: bool = True) -> tuple[int, bytes, str]:
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    handlers = [] if follow else [NoRedirect()]
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(
        url, headers={"User-Agent": "ISEO-SU-TECH-REPAIR-WAVE-01/1.0"}
    )
    try:
        with opener.open(req, timeout=45) as resp:
            final = resp.geturl()
            return resp.status, resp.read(), final
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        loc = e.headers.get("Location", "")
        return e.code, body, loc or url


def extract_stylesheet_hrefs(html: str) -> list[str]:
    return re.findall(
        r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\']',
        html,
        flags=re.I,
    ) + re.findall(
        r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']stylesheet["\']',
        html,
        flags=re.I,
    )


def extract_logo_srcs(html: str) -> list[str]:
    return [
        m
        for m in re.findall(r'src=["\']([^"\']*logo[^"\']*)["\']', html, flags=re.I)
    ]


def main() -> int:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak_dir = BAK_ROOT / ts
    bak_dir.mkdir(parents=True, exist_ok=True)

    report: dict = {
        "timestamp_utc": ts,
        "backup_dir": str(bak_dir),
        "files": [],
        "validation": {},
    }

    sftp, transport = sftp_connect()
    try:
        for local, remote in MAP:
            before = read_remote_bytes(sftp, remote)
            before_sha = sha256_bytes(before)
            local_bytes = local.read_bytes()
            local_sha = sha256_bytes(local_bytes)
            bak_name = remote.replace("/", "__").lstrip("_")
            bak_path = bak_dir / bak_name
            bak_path.write_bytes(before)

            entry = {
                "local": str(local),
                "remote": remote,
                "backup": str(bak_path),
                "sha256_before": before_sha,
                "sha256_local": local_sha,
                "action": "UPDATE",
            }
            write_remote_bytes(sftp, remote, local_bytes)
            after = read_remote_bytes(sftp, remote)
            after_sha = sha256_bytes(after)
            entry["sha256_after"] = after_sha
            entry["remote_matches_local"] = after_sha == local_sha
            report["files"].append(entry)
            print(f"DEPLOY {remote} match={entry['remote_matches_local']}")
    finally:
        sftp.close()
        transport.close()

    # Live validation
    val: dict = {
        "authors": [],
        "intended_css_http": {},
        "legacy_author_css_http": {},
        "logo": {},
        "smoke": [],
        "seo_markers": {},
    }

    for css in INTENDED_CSS:
        code, _, _ = http_get(css)
        val["intended_css_http"][css] = code

    for slug in AUTHORS:
        url = f"{SITE}/blog/author/{slug}"
        code_nr, _, loc = http_get(url, follow=False)
        code, body, final = http_get(url, follow=True)
        html = body.decode("utf-8", "replace")
        hrefs = extract_stylesheet_hrefs(html)
        bad = [
            h
            for h in hrefs
            if "blog/author/css" in h
            or "blog/author/libs" in h
            or h.startswith("css/")
            or h.startswith("libs/")
        ]
        good = [h for h in hrefs if h.startswith("/css/") or h.startswith("/libs/") or h.startswith("https://i-seo.su/css/") or h.startswith("https://i-seo.su/libs/")]
        # title/canonical/h1 markers for SEO mutation check vs homepage
        title_m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
        canon_m = re.search(
            r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
            html,
            re.I,
        )
        h1_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
        val["authors"].append(
            {
                "url": url,
                "http_no_follow": code_nr,
                "location": loc,
                "http_follow": code,
                "final_url": final,
                "stylesheet_hrefs": hrefs,
                "bad_relative_or_nested": bad,
                "root_relative_css_libs": good,
                "title": title_m.group(1).strip() if title_m else None,
                "canonical": canon_m.group(1) if canon_m else None,
                "h1_snippet": re.sub(r"\s+", " ", h1_m.group(1))[:120] if h1_m else None,
            }
        )
        print(f"AUTHOR {slug} follow={code} bad={len(bad)} good_css={len(good)}")

    # Prove legacy nested CSS URLs still 404 (expected — no longer referenced)
    for path in [
        "/blog/author/css/main.css",
        "/blog/author/css/media.css",
        "/blog/author/css/normalize.css",
        "/blog/author/libs/owl/owl.carousel.min.css",
        "/blog/author/libs/owl/owl.theme.default.min.css",
        "/blog/author/libs/fancybox/jquery.fancybox.min.css",
    ]:
        code, _, _ = http_get(SITE + path)
        val["legacy_author_css_http"][SITE + path] = code

    # Logo
    code404, _, _ = http_get(f"{SITE}/img/logo.svg")
    code_ok, _, _ = http_get(f"{SITE}/img/logo-intl.svg")
    blog_code, blog_body, _ = http_get(f"{SITE}/blog.html")
    blog_html = blog_body.decode("utf-8", "replace")
    logos = extract_logo_srcs(blog_html)
    val["logo"] = {
        "img_logo_svg_http": code404,
        "img_logo_intl_svg_http": code_ok,
        "blog_html_http": blog_code,
        "blog_html_logo_srcs": logos,
        "blog_html_has_stale_logo_svg": any(
            s.endswith("/img/logo.svg") or s.endswith("img/logo.svg") for s in logos
        ),
        "blog_html_has_logo_intl": any("logo-intl.svg" in s for s in logos),
    }
    print("LOGO blog refs:", logos, "stale=", val["logo"]["blog_html_has_stale_logo_svg"])

    # Homepage markers for SEO unchanged check
    home_code, home_body, _ = http_get(f"{SITE}/")
    home_html = home_body.decode("utf-8", "replace")
    home_title = re.search(r"<title>(.*?)</title>", home_html, re.I | re.S)
    home_canon = re.search(
        r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
        home_html,
        re.I,
    )
    home_h1 = re.search(r"<h1[^>]*>(.*?)</h1>", home_html, re.I | re.S)
    home_desc = re.search(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']',
        home_html,
        re.I,
    )
    home_hrefs = extract_stylesheet_hrefs(home_html)
    val["seo_markers"]["home"] = {
        "http": home_code,
        "title": home_title.group(1).strip() if home_title else None,
        "canonical": home_canon.group(1) if home_canon else None,
        "description": home_desc.group(1) if home_desc else None,
        "h1_snippet": re.sub(r"\s+", " ", home_h1.group(1))[:120] if home_h1 else None,
        "stylesheet_hrefs": home_hrefs,
        "bad_relative_css": [
            h for h in home_hrefs if h.startswith("css/") or h.startswith("libs/")
        ],
    }

    for url in SMOKE:
        code, body, final = http_get(url)
        html = body.decode("utf-8", "replace")
        hrefs = extract_stylesheet_hrefs(html)
        bad = [
            h
            for h in hrefs
            if "blog/author/css" in h
            or h.startswith("css/")
            or (url.endswith("/blog/") is False and "blog/author/libs" in h)
        ]
        # for WP blog pages expect absolute or root-relative
        val["smoke"].append(
            {
                "url": url,
                "http": code,
                "final": final,
                "stylesheet_count": len(hrefs),
                "has_author_nested_css": any("blog/author/css" in h for h in hrefs),
            }
        )
        print(f"SMOKE {url} http={code}")

    # Summary counters
    author_bad_total = sum(len(a["bad_relative_or_nested"]) for a in val["authors"])
    val["summary"] = {
        "author_css_bad_hrefs_total": author_bad_total,
        "intended_css_all_200": all(v == 200 for v in val["intended_css_http"].values()),
        "logo_stale_ref_gone": not val["logo"]["blog_html_has_stale_logo_svg"],
        "logo_intl_200": val["logo"]["img_logo_intl_svg_http"] == 200,
        "all_files_aligned": all(f["remote_matches_local"] for f in report["files"]),
    }
    report["validation"] = val
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("WROTE", OUT)
    print("SUMMARY", json.dumps(val["summary"], ensure_ascii=False))
    return 0 if (
        author_bad_total == 0
        and val["summary"]["intended_css_all_200"]
        and val["summary"]["logo_stale_ref_gone"]
        and val["summary"]["all_files_aligned"]
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
