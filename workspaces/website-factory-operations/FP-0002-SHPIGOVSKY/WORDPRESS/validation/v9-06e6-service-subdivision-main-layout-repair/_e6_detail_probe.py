#!/usr/bin/env python3
"""TEMPORARY E6 detailed markup probe — NOT FOR GIT."""
import json
import re
import urllib.request

BASE = "http://shpigovsky.test"


def fetch(route):
    req = urllib.request.Request(BASE + route, headers={"User-Agent": "E6-detail"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


_, z_html = fetch("/uslugi/zavisimosti/")
_, o_html = fetch("/otzyvy/")

z_checks = {
    "body_page_service_subdivision_v1": "page-service-subdivision-v1" in z_html,
    "main_wrapper": "page-service-subdivision-v1__main" in z_html,
    "hero_type": "services-inner-hero-v2" in z_html,
    "hero_image": "service-subdivision-hero.webp" in z_html,
    "dependencies_marker": "services-category-section-v2__marker" in z_html,
    "dependencies_footer_text": "service-subdivision-dependencies-v1__footer-text" in z_html,
    "dependencies_heading": "Зависимости, которые мы лечим" in z_html,
    "nature_section": "service-subdivision-nature-v1" in z_html,
    "program_images": "program-genotyping.webp" in z_html,
    "program_modifiers": "services-program-v2--media-frame-fixed" in z_html,
    "program_intro_continued": "services-program-v2__intro--continued" in z_html,
    "stages_section": "service-subdivision-stages-v1" in z_html,
    "team_stats_section": "service-subdivision-team-stats-v1" in z_html,
    "program_cta_band": "program-cta-band" in z_html,
    "no_article_wrapper": "shpigovsky-service--subdivision" not in z_html,
    "final_form_band": "final-form__band" in z_html,
}

section_ids = [
    "service-subdivision-dependencies",
    "service-subdivision-nature",
    "service-subdivision-start",
    "service-subdivision-program",
    "service-subdivision-stages",
    "service-subdivision-approach",
    "service-subdivision-specialists",
    "service-subdivision-comfort",
    "service-subdivision-faq",
]
z_checks["section_ids_present"] = {sid: (f'id="{sid}"' in z_html) for sid in section_ids}

out = {
    "zavisimosti_markup": z_checks,
    "reviews_first_author_andrey": "Андрей, Москва" in o_html,
    "reviews_contains_andrey": "Андрей" in o_html,
}

print(json.dumps(out, ensure_ascii=False, indent=2))
