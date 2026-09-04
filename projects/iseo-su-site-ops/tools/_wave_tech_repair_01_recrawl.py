#!/usr/bin/env python3
"""Bounded targeted recrawl after TECH REPAIR WAVE 01."""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from pathlib import Path

SITE = "https://i-seo.su"
UA = {"User-Agent": "ISEO-SU-TECH-REPAIR-WAVE-01-RECRAWL/1.0"}
OUT = Path(__file__).resolve().parent / "_wave_tech_repair_01_recrawl.json"


def fetch(url: str, follow: bool = True):
    class NR(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None

    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NR())
    req = urllib.request.Request(url, headers=UA)
    try:
        with opener.open(req, timeout=45) as r:
            return r.status, r.read(), dict(r.headers), r.geturl()
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        return e.code, body, dict(e.headers), e.headers.get("Location", "")


def abs_url(base: str, href: str) -> str:
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        return SITE + href
    return base.rstrip("/") + "/" + href.lstrip("./")


def seo(html: str) -> dict:
    title_m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    h1_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    canon = re.search(
        r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
        html,
        re.I,
    ) or re.search(
        r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']',
        html,
        re.I,
    )
    desc = re.search(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']',
        html,
        re.I,
    ) or re.search(
        r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']',
        html,
        re.I,
    )
    robots = re.search(
        r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']*)["\']',
        html,
        re.I,
    )

    def strip_tags(s: str | None) -> str | None:
        if s is None:
            return None
        return re.sub(r"<[^>]+>", "", s).strip()

    return {
        "title": strip_tags(title_m.group(1) if title_m else None),
        "h1": strip_tags(h1_m.group(1) if h1_m else None),
        "canonical": canon.group(1) if canon else None,
        "description": desc.group(1) if desc else None,
        "robots": robots.group(1) if robots else None,
    }


def main() -> int:
    broken_css = []
    nested_css = []
    broken_img = []
    stale_logo = []
    author_rows = []

    for slug in ["admin", "denis", "ilya", "manager3", "mars", "olya"]:
        url = f"{SITE}/blog/author/{slug}"
        code, body, _, final = fetch(url, True)
        html = body.decode("utf-8", "replace")
        hrefs = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', html, re.I)
        css = [h for h in hrefs if ".css" in h.lower()]
        row = {"url": url, "http": code, "final": final, "css": [], "nested": []}
        for h in css:
            if "fonts.googleapis" in h:
                continue
            absu = abs_url(final or SITE + "/", h)
            if "/blog/author/css" in absu or "/blog/author/libs" in absu:
                nested_css.append({"page": url, "asset": absu})
                row["nested"].append(absu)
            c, _, _, _ = fetch(absu)
            row["css"].append({"href": h, "abs": absu, "http": c})
            if c != 200 and ("/css/" in absu or "/libs/" in absu or absu.endswith(".css")):
                broken_css.append({"page": url, "asset": absu, "http": c})
        author_rows.append(row)

    logo_pages = {}
    for path in ["/", "/blog.html", "/blog/", "/blog/category/seo/"]:
        url = SITE + path
        code, body, _, final = fetch(url, True)
        html = body.decode("utf-8", "replace")
        logos = re.findall(r'src=["\']([^"\']*logo[^"\']*)["\']', html, re.I)
        resolved = []
        for src in logos:
            absu = abs_url(final or SITE + "/", src)
            c, _, _, _ = fetch(absu)
            resolved.append({"src": src, "abs": absu, "http": c})
            if absu.rstrip("/").endswith("/img/logo.svg"):
                stale_logo.append({"page": url, "asset": absu})
            if c != 200:
                broken_img.append({"page": url, "asset": absu, "http": c})
        logo_pages[path] = {
            "http": code,
            "final": final,
            "seo": seo(html),
            "logos": resolved,
            "menu_has_blog": bool(re.search(r'href=["\']/blog/?["\']', html, re.I)),
        }

    assets = {}
    for path in [
        "/img/logo.svg",
        "/img/logo-intl.svg",
        "/css/main.css",
        "/css/normalize.css",
        "/css/media.css",
        "/sitemap.xml",
        "/sitemap-static.xml",
    ]:
        c, _, _, _ = fetch(SITE + path)
        assets[path] = c

    # blog post smoke
    blog_code, blog_body, _, _ = fetch(f"{SITE}/blog/", True)
    blog_html = blog_body.decode("utf-8", "replace")
    post = None
    m = re.search(r'href=["\'](https://i-seo\.su/blog/[^"\']+\.html)["\']', blog_html)
    if m:
        post = m.group(1)
        pc, pb, _, pf = fetch(post, True)
        post_html = pb.decode("utf-8", "replace")
        post_css_bad = [
            h
            for h in re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', post_html, re.I)
            if h.startswith("css/") or h.startswith("./css/")
        ]
    else:
        pc, pf, post_css_bad = None, None, []

    out = {
        "author_pages": author_rows,
        "nested_author_css_count": len(nested_css),
        "nested_author_css": nested_css,
        "broken_css_count": len(broken_css),
        "broken_css": broken_css,
        "broken_img_count": len(broken_img),
        "broken_img": broken_img,
        "stale_logo_svg_refs": stale_logo,
        "logo_pages": logo_pages,
        "assets": assets,
        "blog_post_smoke": {
            "url": post,
            "http": pc,
            "final": pf,
            "relative_css_hrefs": post_css_bad,
        },
        "summary": {
            "AUTHOR_CSS_BROKEN_AFTER": len(broken_css) + len(nested_css),
            "LOGO_STALE_REFS_AFTER": len(stale_logo),
            "BROKEN_IMG_AFTER": len(broken_img),
            "logo_svg_http": assets.get("/img/logo.svg"),
            "logo_intl_http": assets.get("/img/logo-intl.svg"),
            "sitemap_http": assets.get("/sitemap.xml"),
        },
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out["summary"], ensure_ascii=False, indent=2))
    print("wrote", OUT)
    return 0 if out["summary"]["AUTHOR_CSS_BROKEN_AFTER"] == 0 and out["summary"]["LOGO_STALE_REFS_AFTER"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
