#!/usr/bin/env python3
"""E8 runtime route probe — not for git commit."""
import json
import re
import urllib.request

BASE = "http://shpigovsky.test"
ROUTES = [
    "/",
    "/uslugi/",
    "/kontakty/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/uslugi/psihicheskoe-zdorovie/",
    "/uslugi/rasstroystva-pischevogo-povedeniya/",
    "/otzyvy/",
    "/privacy-policy/",
    "/user-agreement/",
    "/consent-personal-data/",
    "/cookie-files-policy/",
]

out = {}
for route in ROUTES:
    try:
        req = urllib.request.Request(BASE + route, headers={"User-Agent": "E8-probe"})
        resp = urllib.request.urlopen(req, timeout=20)
        html = resp.read().decode("utf-8", "replace")
        main_m = re.search(r'<main[^>]*class="([^"]*)"', html)
        body_m = re.search(r'<body[^>]*class="([^"]*)"', html)
        out[route] = {
            "http_status": resp.status,
            "main_class": main_m.group(1) if main_m else None,
            "body_class": body_m.group(1) if body_m else None,
            "has_program_cta_container": bool(
                re.search(
                    r'<div class="container">\s*<div class="program-cta-band"',
                    html,
                )
            ),
            "has_contacts_map_image": "contacts-map-mo-region.png" in html,
            "has_contacts_photo": "contacts-rehabilitation-interior.png" in html,
            "has_service_leaf_corridor": "service-leaf-corridor-v1" in html,
            "has_bordered_info_panel": "service-leaf-bordered-info-v1__panel" in html,
            "has_alcohol_intro_v9": "Алкогольная зависимость" in html
            and "не персональный выбор" in html,
            "has_hub_v9_cta_label": html.count("Записаться на консультацию") >= 1,
            "has_uznat_bolshe": "узнать больше" in html,
            "php_fatal": "Fatal error" in html or "Parse error" in html,
        }
    except Exception as exc:
        out[route] = {"error": str(exc)}

print(json.dumps(out, ensure_ascii=False, indent=2))
