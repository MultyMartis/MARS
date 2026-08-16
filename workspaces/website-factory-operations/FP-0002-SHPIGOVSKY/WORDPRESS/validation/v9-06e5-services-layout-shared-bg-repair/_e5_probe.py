#!/usr/bin/env python3
"""TEMPORARY E5 post-repair probe — NOT FOR GIT."""
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
    req = urllib.request.Request(url, headers={"User-Agent": "E5-probe"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except Exception as exc:
        return 0, str(exc)


def head(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "E5-probe"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


out = {"routes": {}, "css_urls": {}, "css_rule_check": {}}

for route in ROUTES:
    status, html = fetch(BASE + route)
    entry = {
        "http_status": status,
        "php_fatal": "Fatal error" in html or "Parse error" in html,
        "has_services_inner_hero_v2": "services-inner-hero-v2" in html,
        "has_wrong_home_hero": "hero hero--inner" in html,
        "has_page_uslugi_v2_main": "page-uslugi-v2__main" in html,
        "has_page_service_subdivision_main": "page-service-subdivision-v1__main" in html,
        "services_hero_img": "services-hero.webp" in html,
        "subdivision_hero_img": "service-subdivision-hero.webp" in html,
        "has_services_category_section_v2": "services-category-section-v2" in html,
        "has_service_subdivision_nature": "service-subdivision-nature-v1" in html,
        "has_service_subdivision_team_stats": "service-subdivision-team-stats-v1" in html,
        "has_program_cta_band": "program-cta-band" in html,
        "has_final_form_band": "final-form__band" in html,
        "first_review_author": None,
    }
    if route == "/otzyvy/":
        match = re.search(r'review-archive-card__author[^>]*>([^<]+)', html)
        if match:
            entry["first_review_author"] = match.group(1).strip()
    out["routes"][route] = entry

for path in [
    "/assets/img/content/home-final-form/home-final-form-background.webp",
    THEME + "/assets/img/content/home-final-form/home-final-form-background.webp",
    THEME + "/assets/img/content/services/services-hero.webp",
    THEME + "/assets/img/content/services/service-subdivision-hero.webp",
]:
    out["css_urls"][path] = head(path if path.startswith("http") else BASE + path)

css_status, css_body = fetch(THEME + "/assets/css/v9-style.css")
out["css_rule_check"] = {
    "http_status": css_status,
    "root_absolute_assets_remaining": css_body.count('url("/assets/') if css_status == 200 else None,
    "theme_relative_home_final_form": '../img/content/home-final-form/home-final-form-background.webp' in css_body,
}

print(json.dumps(out, ensure_ascii=False, indent=2))
