# -*- coding: utf-8 -*-
"""Re-validate WAVE 02 live pages without redeploy."""
from __future__ import annotations

import json
from pathlib import Path

import importlib.util

SPEC = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_wave02_backup_deploy_validate.py")
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_wave02_deploy_validate.json")

spec = importlib.util.spec_from_file_location("wave02", SPEC)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

SITE = mod.SITE
CITY_SLUGS = mod.CITY_SLUGS
CITY_META = mod.CITY_META
SMOKE = mod.SMOKE
http_get = mod.http_get
extract_title = mod.extract_title
extract_meta = mod.extract_meta
extract_canonical = mod.extract_canonical
extract_h1 = mod.extract_h1

import xml.etree.ElementTree as ET

hub_back = "https://i-seo.su/services/seo/b-regionakh.html"
manifest = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
manifest["pages"] = {}
pages_ok = True
for slug, meta in CITY_META.items():
    url = f"{SITE}/services/seo/{slug}"
    status, body, _ = http_get(url)
    html = body.decode("utf-8", "replace")
    robots = extract_meta(html, "robots").lower()
    canon = extract_canonical(html)
    title = extract_title(html)
    desc = extract_meta(html, "description")
    h1 = extract_h1(html)
    consent_n = html.count('name="personal_data_consent"')
    privacy_n = html.count("/privacy-policy.html")
    calc_has = 'id="callback__FORM_tariff_calc"' in html
    calc_consent_field = 'id="personal_data_consent_callback__FORM_tariff_calc"' in html
    row = {
        "url": url,
        "http": status,
        "title_ok": title == meta["title"],
        "title": title,
        "description_ok": desc == meta["description"],
        "h1_ok": h1 == meta["h1"],
        "h1": h1,
        "intro_ok": meta["intro_needle"] in html,
        "main_title_ok": meta["main_title"] in html,
        "faq4_ok": meta["faq4"] in html,
        "canonical": canon,
        "canonical_ok": canon == url,
        "indexable": status == 200 and "noindex" not in robots and ("index" in robots or robots == ""),
        "robots": robots,
        "hub_backlink": hub_back in html,
        "consent_count": consent_n,
        "privacy_count": privacy_n,
        "consent_ok": consent_n >= 1 and privacy_n >= 1,
        "calc_present": calc_has,
        "calc_consent_ok": (not calc_has) or calc_consent_field,
    }
    row["PASS"] = all(
        [
            row["http"] == 200,
            row["title_ok"],
            row["description_ok"],
            row["h1_ok"],
            row["intro_ok"],
            row["main_title_ok"],
            row["faq4_ok"],
            row["canonical_ok"],
            row["indexable"],
            row["hub_backlink"],
            row["consent_ok"],
            row["calc_consent_ok"],
        ]
    )
    pages_ok = pages_ok and row["PASS"]
    manifest["pages"][slug] = row
    print(slug, "PASS" if row["PASS"] else "FAIL", "consent", consent_n, "calc_consent", row["calc_consent_ok"])

st, body, _ = http_get(f"{SITE}/services/seo/b-regionakh.html")
hub_html = body.decode("utf-8", "replace")
hub_links = {slug: f"{SITE}/services/seo/{slug}" in hub_html for slug in CITY_SLUGS}
manifest["hub"] = {
    "http": st,
    "city_block": "Выберите ваш город" in hub_html and 'id="city-seo-pages"' in hub_html,
    "links": hub_links,
    "links_ok": all(hub_links.values()),
    "consent_count": hub_html.count('name="personal_data_consent"'),
    "consent_ok": hub_html.count('name="personal_data_consent"') >= 1,
}
print("HUB", manifest["hub"])

st, body, _ = http_get(f"{SITE}/sitemap-static.xml")
root = ET.fromstring(body)
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
locs = [el.text.strip() for el in root.findall("sm:url/sm:loc", ns) if el.text]
city_urls = [f"{SITE}/services/seo/{s}" for s in CITY_SLUGS]
city_in = {u: locs.count(u) for u in city_urls}
manifest["sitemap"].update(
    {
        "http": st,
        "xml_valid": True,
        "url_count": len(locs),
        "city_in_sitemap": city_in,
        "city_present_5": all(city_in[u] == 1 for u in city_urls),
        "duplicates": len(locs) - len(set(locs)),
    }
)
consent_pages = sum(1 for r in manifest["pages"].values() if r.get("consent_ok"))
manifest["consent"] = {
    "city_pages_covered": f"{consent_pages}/5",
    "hub_consent_ok": manifest["hub"].get("consent_ok"),
    "calc_consent_covered": all(r.get("calc_consent_ok") for r in manifest["pages"].values()),
}
manifest["final"] = {
    "CITY_PAGES_CREATED": 5,
    "pages_pass": pages_ok,
    "hub_pass": manifest["hub"]["http"] == 200
    and manifest["hub"]["city_block"]
    and manifest["hub"]["links_ok"],
    "sitemap_pass": manifest["sitemap"]["http"] == 200
    and manifest["sitemap"]["xml_valid"]
    and manifest["sitemap"]["city_present_5"]
    and manifest["sitemap"]["duplicates"] == 0,
    "STATIC_SITEMAP_URL_COUNT_AFTER": manifest["sitemap"]["url_count"],
}
OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("FINAL", json.dumps(manifest["final"], ensure_ascii=False))
print("CONSENT", manifest["consent"])
