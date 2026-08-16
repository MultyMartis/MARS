#!/usr/bin/env python3
"""TEMPORARY E6 probe — NOT FOR GIT."""
import json
import re
import urllib.error
import urllib.request

BASE = "http://shpigovsky.test"
THEME = BASE + "/wp-content/themes/shpigovsky"
ROUTES = [
    "/",
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/kontakty/",
    "/otzyvy/",
    "/privacy-policy/",
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "E6-probe"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except Exception as exc:
        return 0, str(exc)


def head(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "E6-probe"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def extract_sections(html):
    main = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
    if not main:
        return []
    sections = []
    for m in re.finditer(
        r"<(section|article|nav|aside)[^>]*?(?:id=\"([^\"]*)\")?[^>]*?(?:class=\"([^\"]*)\")?[^>]*>",
        main.group(1),
        re.I,
    ):
        tag, sid, cls = m.group(1), m.group(2) or "", m.group(3) or ""
        sections.append({"tag": tag, "id": sid, "class": cls[:200]})
    return sections


out = {"routes": {}, "css_rule_check": {}}

for route in ROUTES:
    status, html = fetch(BASE + route)
    body_m = re.search(r'<body[^>]*class="([^"]+)"', html)
    main_m = re.search(r'<main[^>]*class="([^"]+)"', html)
    entry = {
        "http_status": status,
        "php_fatal": "Fatal error" in html or "Parse error" in html,
        "body_class": body_m.group(1) if body_m else None,
        "main_class": main_m.group(1) if main_m else None,
        "has_page_service_subdivision_v1_body": bool(
            body_m and "page-service-subdivision-v1" in body_m.group(1)
        ),
        "has_services_inner_hero_v2": "services-inner-hero-v2" in html,
        "has_page_uslugi_v2_main": "page-uslugi-v2__main" in html,
        "has_page_service_subdivision_main": "page-service-subdivision-v1__main" in html,
        "subdivision_hero_img": "service-subdivision-hero.webp" in html,
        "sections": extract_sections(html) if route == "/uslugi/zavisimosti/" else None,
        "first_review_author": None,
    }
    if route == "/otzyvy/":
        match = re.search(r"review-archive-card__author[^>]*>([^<]+)", html)
        if match:
            entry["first_review_author"] = match.group(1).strip()
    out["routes"][route] = entry

css_status, css_body = fetch(THEME + "/assets/css/v9-style.css")
out["css_rule_check"] = {
    "http_status": css_status,
    "root_absolute_assets_remaining": css_body.count('url("/assets/') if css_status == 200 else None,
}

print(json.dumps(out, ensure_ascii=False, indent=2))
