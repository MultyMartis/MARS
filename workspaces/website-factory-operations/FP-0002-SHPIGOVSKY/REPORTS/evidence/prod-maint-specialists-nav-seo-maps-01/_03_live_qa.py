# -*- coding: utf-8 -*-
"""Live QA — specialists nav + SEO meta + contacts maps wave."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

OUT = Path(__file__).resolve().parent
BASE = "https://shpigovsky.ru"

URLS = [
    ("homepage", f"{BASE}/"),
    ("contacts", f"{BASE}/kontakty/"),
    ("specialists_hub", f"{BASE}/specialisty/"),
    ("specialist_single", f"{BASE}/specialisty/shpigovsky/"),
    ("services_hub", f"{BASE}/uslugi/"),
    ("service_single", f"{BASE}/uslugi/lechenie-alkogolizma/"),
    ("article", f"{BASE}/blog/"),
    ("o_centre", f"{BASE}/o-centre/"),
    ("reviews", f"{BASE}/otzyvy/"),
    ("privacy", f"{BASE}/politika-konfidencialnosti/"),
    ("breadcrumb_regression", f"{BASE}/o-centre/"),
]


def fetch(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "FP02-Nav-SEO-Maps-QA/1.0"})
    try:
        with urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8", "replace")
            return {"url": url, "status": resp.status, "body": body}
    except HTTPError as e:
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        return {"url": url, "status": e.code, "body": body}


def title_tag(html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def meta_descriptions(html: str) -> list[str]:
    return re.findall(
        r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']',
        html,
        re.I,
    )


def has_breadcrumb_nav(html: str) -> bool:
    if "internal-page-nav" in html:
        return True
    if re.search(r'class=["\'][^"\']*breadcrumb', html, re.I):
        return True
    if re.search(r"Главная\s*</a>\s*/?\s*Специалисты", html, re.I | re.S):
        return True
    return False


def yandex_constructor_scripts(html: str) -> list[str]:
    return re.findall(
        r'<script[^>]+src=["\'](https://api-maps\.yandex\.ru/services/constructor/[^"\']+)["\']',
        html,
        re.I,
    )


def main() -> None:
    intake = json.loads(OUT.joinpath("01-prod-intake.json").read_text(encoding="utf-8"))
    seo_admin = intake.get("seo", {})

    robots_before = OUT.joinpath("01-robots-before.txt").read_bytes()
    robots_after_resp = fetch(f"{BASE}/robots.txt")
    robots_after = robots_after_resp["body"].encode("utf-8")
    robots_preserved = hashlib.sha256(robots_before).hexdigest() == hashlib.sha256(
        robots_after
    ).hexdigest()

    report: dict = {
        "robots": {
            "before_sha256": hashlib.sha256(robots_before).hexdigest(),
            "after_sha256": hashlib.sha256(robots_after).hexdigest(),
            "preserved": robots_preserved,
            "status": robots_after_resp["status"],
        },
        "pages": [],
        "specialists_hub_nav": {},
        "contacts_maps": {},
        "old_redirect": {},
    }

    for key, url in URLS:
        r = fetch(url)
        html = r["body"]
        titles = title_tag(html)
        descs = meta_descriptions(html)
        entry = {
            "key": key,
            "url": url,
            "status": r["status"],
            "title": titles,
            "meta_description_count": len(descs),
            "meta_descriptions": descs,
            "duplicate_meta_description": len(descs) > 1,
        }

        admin_key_map = {
            "homepage": "front_page",
            "contacts": "contacts",
            "specialists_hub": "specialists_hub_1030",
            "specialist_single": "specialist_sample",
            "services_hub": "services_hub",
            "service_single": "service_sample",
            "article": "article_sample",
            "o_centre": "o_centre",
            "reviews": "reviews",
            "privacy": "privacy",
        }
        ak = admin_key_map.get(key)
        if ak and ak in seo_admin and seo_admin[ak]:
            admin = seo_admin[ak]
            admin_title = (admin.get("fp02_seo_title") or "").strip()
            admin_desc = (admin.get("fp02_seo_description") or "").strip()
            entry["admin_seo_title"] = admin_title
            entry["admin_seo_description"] = admin_desc
            if admin_title:
                entry["title_matches_admin"] = admin_title in titles
            if admin_desc:
                entry["desc_matches_admin"] = admin_desc in descs or any(
                    admin_desc[:40] in d for d in descs
                )

        if key == "specialists_hub":
            report["specialists_hub_nav"] = {
                "has_internal_page_nav": "internal-page-nav" in html,
                "has_breadcrumb_nav": has_breadcrumb_nav(html),
                "pass": "internal-page-nav" not in html and not has_breadcrumb_nav(html),
            }
            entry["has_internal_page_nav"] = "internal-page-nav" in html
            entry["has_breadcrumb_nav"] = has_breadcrumb_nav(html)

        if key == "breadcrumb_regression":
            entry["has_internal_page_nav"] = "internal-page-nav" in html
            entry["breadcrumb_regression_pass"] = "internal-page-nav" in html

        if key == "contacts":
            scripts = yandex_constructor_scripts(html)
            scroll_values = []
            for src in scripts:
                m = re.search(r"[?&]scroll=(true|false)", src, re.I)
                scroll_values.append(m.group(1).lower() if m else "missing")
            report["contacts_maps"] = {
                "constructor_script_count": len(scripts),
                "scroll_params": scroll_values,
                "has_fallback_only": "contacts-location__map-fallback" in html
                and len(scripts) == 0,
                "pass": len(scripts) >= 1 and "contacts-location__map-embed--constructor" in html,
            }
            entry["yandex_constructor_scripts"] = len(scripts)
            entry["scroll_params"] = scroll_values

        entry["seo_pass"] = (
            r["status"] == 200
            and not entry.get("duplicate_meta_description", False)
            and bool(titles)
        )
        report["pages"].append(entry)

    # old redirect check
    req = Request(
        f"{BASE}/specyalisty/",
        method="GET",
        headers={"User-Agent": "FP02-Nav-SEO-Maps-QA/1.0"},
    )
    class NoRedirect:
        pass

    import urllib.request

    class Handler(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: N802
            return None

    opener = urllib.request.build_opener(Handler)
    try:
        with opener.open(req, timeout=30) as resp:
            report["old_redirect"] = {"status": resp.status}
    except HTTPError as e:
        report["old_redirect"] = {
            "status": e.code,
            "location": e.headers.get("Location") if e.headers else None,
        }

    OUT.joinpath("05-live-qa.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2)[:16000])
    print("LIVE_QA_OK")


if __name__ == "__main__":
    main()
