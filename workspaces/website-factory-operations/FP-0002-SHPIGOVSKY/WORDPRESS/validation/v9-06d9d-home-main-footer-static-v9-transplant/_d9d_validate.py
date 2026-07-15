#!/usr/bin/env python3
"""D9-D post-repair validation — TEMP HELPER."""
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

EVIDENCE = Path(__file__).resolve().parent
RUNTIME_URL = "http://shpigovsky.test"
ROUTES = [
    ("/", "home"),
    ("/uslugi/", "services-hub"),
    ("/uslugi/zavisimosti/", "service-73"),
    ("/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "service-74"),
    ("/uslugi/psihicheskoe-zdorovie/", "service-77"),
    ("/uslugi/rasstroystva-pischevogo-povedeniya/", "service-84"),
    ("/kontakty/", "contacts"),
]

EXPECTED_SECTIONS = [
    "home-recovery-intro",
    "founder-quote",
    "home-treatment-prevention",
    "home-gallery",
    "home-why-us",
    "home-staff-photo",
    "home-feature-grid",
    "clinic-landscape",
    "home-recovery-life",
    "reviews",
    "home-rehabilitation-requirements",
    "home-rehabilitation-program",
    "home-genotyping",
    "comfort",
    "home-videos",
    "specialists",
    "home-articles",
    "faq",
    "final-form",
]


def fetch(url: str) -> tuple[int, str]:
    req = Request(url, headers={"User-Agent": "D9D-Validate/1.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", "ignore")


def main() -> None:
    smoke = []
    for path, key in ROUTES:
        code, body = fetch(RUNTIME_URL + path)
        smoke.append(
            {
                "route": path,
                "key": key,
                "status": code,
                "has_header": "site-header" in body,
                "has_footer": "site-footer" in body,
                "has_v9_css": "v9-style" in body,
                "php_fatal": "Fatal error" in body or "Parse error" in body,
                "ok": code == 200 and "site-footer" in body and "site-header" in body,
            }
        )

    home_code, home = fetch(RUNTIME_URL + "/")
    found = []
    for cls in EXPECTED_SECTIONS:
        found.append({"section": cls, "present": cls in home})

    hero_cta = ("Записаться на консультацию" in home) or ("Записаться на&nbsp;консультацию" in home)

    (EVIDENCE / "post-repair-route-smoke.json").write_text(
        json.dumps(smoke, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (EVIDENCE / "post-repair-home-main-dom-section-check.json").write_text(
        json.dumps(
            {
                "expected_count": len(EXPECTED_SECTIONS),
                "found": found,
                "all_present": all(x["present"] for x in found),
                "home_status": home_code,
                "has_main": "<main" in home,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (EVIDENCE / "post-repair-footer-check.json").write_text(
        json.dumps(
            {
                "has_site_footer": "site-footer" in home,
                "has_privacy_block": "site-footer__privacy" in home,
                "has_credit": "Overseo" in home,
                "has_scroll_to_top": "scroll-to-top" in home,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (EVIDENCE / "post-repair-hero-cta-check.json").write_text(
        json.dumps(
            {
                "static_label": "Записаться на консультацию",
                "runtime_match": hero_cta,
                "result": "PASS" if hero_cta else "FAIL",
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    verdict = {
        "route_smoke": "ALL_200" if all(r["status"] == 200 for r in smoke) else "PARTIAL",
        "route_chrome": "PASS" if all(r["ok"] for r in smoke) else "PARTIAL",
        "home_sections": "PASS" if all(x["present"] for x in found) else "PARTIAL",
        "hero_cta": "PASS" if hero_cta else "FAIL",
        "verdict": "PASS",
    }
    if verdict["route_chrome"] != "PASS" or verdict["home_sections"] != "PASS" or not hero_cta:
        verdict["verdict"] = "PARTIAL PASS"
    (EVIDENCE / "final-verdict.json").write_text(json.dumps(verdict, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(verdict, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
