# -*- coding: utf-8 -*-
"""Live QA for specialists canonical URL migration."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OUT = Path(__file__).resolve().parent
BASE = "https://shpigovsky.ru"
SLUGS = [
    "shpigovsky",
    "kazakov",
    "kostyuk",
    "hanikova",
    "shapiguzova",
    "litvinov",
    "poverinov",
    "filippov",
    "filippova",
]


def fetch(url: str, allow_redirects: bool = False, method: str = "GET"):
    req = Request(url, method=method, headers={"User-Agent": "FP02-URL-Migration-QA/1.0"})

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: N802
            return None

    if allow_redirects:
        opener = urllib.request.build_opener()
    else:
        opener = urllib.request.build_opener(NoRedirect)

    try:
        with opener.open(req, timeout=30) as resp:
            body = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "location": headers.get("location"),
                "body": body.decode("utf-8", "replace"),
                "headers": headers,
            }
    except HTTPError as e:
        headers = {k.lower(): v for k, v in e.headers.items()} if e.headers else {}
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        return {
            "url": url,
            "status": e.code,
            "final_url": url,
            "location": headers.get("location"),
            "body": body,
            "headers": headers,
        }


def follow_once(url: str):
    """Expect exactly one 301 then a 200 on Location target (no chain)."""
    first = fetch(url, allow_redirects=False)
    loc = first.get("location") or ""
    second = None
    if first["status"] in (301, 302, 303, 307, 308) and loc:
        if loc.startswith("/"):
            loc_abs = BASE + loc
        else:
            loc_abs = loc
        second = fetch(loc_abs, allow_redirects=False)
    return {"first": first, "second": second}


def canonical(html: str) -> str:
    m = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', html, re.I)
    if not m:
        m = re.search(r'href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', html, re.I)
    return m.group(1) if m else ""


def h1(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    if not m:
        return ""
    return re.sub(r"<[^>]+>", "", m.group(1)).strip()


def main() -> None:
    report: dict = {"new_hub": {}, "new_singles": [], "old_hub": {}, "old_singles": [], "seo": {}, "internal": {}}

    # New hub
    hub = fetch(f"{BASE}/specialisty/")
    report["new_hub"] = {
        "status": hub["status"],
        "canonical": canonical(hub["body"]),
        "h1": h1(hub["body"]),
        "has_internal_page_nav": "internal-page-nav" in hub["body"],
        "has_old_path_links": bool(re.search(r"/specyalisty/", hub["body"])),
        "has_specialist_cards": "specialists__card" in hub["body"] or "home-feature-grid__card" in hub["body"],
        "len": len(hub["body"]),
    }

    for slug in SLUGS:
        r = fetch(f"{BASE}/specialisty/{slug}/")
        report["new_singles"].append(
            {
                "slug": slug,
                "status": r["status"],
                "canonical": canonical(r["body"]),
                "has_old_path": bool(re.search(r"/specyalisty/", r["body"])),
                "is_redirect": r["status"] in (301, 302),
            }
        )

    # Old hub redirect
    old_hub = follow_once(f"{BASE}/specyalisty/")
    report["old_hub"] = {
        "first_status": old_hub["first"]["status"],
        "location": old_hub["first"].get("location"),
        "second_status": old_hub["second"]["status"] if old_hub["second"] else None,
        "second_url": old_hub["second"]["url"] if old_hub["second"] else None,
        "second_canonical": canonical(old_hub["second"]["body"]) if old_hub["second"] else None,
        "chain_ok": (
            old_hub["first"]["status"] == 301
            and old_hub["second"] is not None
            and old_hub["second"]["status"] == 200
            and (old_hub["first"].get("location") or "").rstrip("/").endswith("/specialisty")
        ),
    }

    for slug in SLUGS:
        o = follow_once(f"{BASE}/specyalisty/{slug}/")
        loc = o["first"].get("location") or ""
        report["old_singles"].append(
            {
                "slug": slug,
                "first_status": o["first"]["status"],
                "location": loc,
                "second_status": o["second"]["status"] if o["second"] else None,
                "chain_ok": (
                    o["first"]["status"] == 301
                    and o["second"] is not None
                    and o["second"]["status"] == 200
                    and f"/specialisty/{slug}" in loc.replace(BASE, "")
                ),
            }
        )

    # Sitemap / robots / home / services
    sm_pages = fetch(f"{BASE}/wp-sitemap-posts-page-1.xml")
    sm_specs = fetch(f"{BASE}/wp-sitemap-specialists-1.xml")
    robots = fetch(f"{BASE}/robots.txt")
    home = fetch(f"{BASE}/")
    uslugi = fetch(f"{BASE}/uslugi/")

    report["seo"] = {
        "pages_sitemap_has_new": "/specialisty/" in sm_pages["body"] and sm_pages["body"].count("/specialisty/") >= 1,
        "pages_sitemap_has_old": "/specyalisty/" in sm_pages["body"],
        "specialists_sitemap_new_count": len(re.findall(r"https://shpigovsky.ru/specialisty/[^<]+", sm_specs["body"])),
        "specialists_sitemap_old_count": sm_specs["body"].count("/specyalisty/"),
        "blog_public_open_probe": "noindex" not in (re.search(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)', home["body"], re.I).group(1).lower() if re.search(r'name=["\']robots["\'][^>]*content=["\']([^"\']+)', home["body"], re.I) else ""),
        "robots_unchanged_markers": "Disallow: /privacy-policy/" in robots["body"] and "User-agent: Yandex" in robots["body"],
        "hub_canonical_expected": report["new_hub"]["canonical"] == f"{BASE}/specialisty/",
    }

    # Internal old-link audit on key pages
    pages = {
        "home": home["body"],
        "hub": hub["body"],
        "uslugi": uslugi["body"],
    }
    # also sample one specialist
    pages["single_kostyuk"] = fetch(f"{BASE}/specialisty/kostyuk/")["body"]

    live_old = {}
    for name, html in pages.items():
        # count hrefs to old path (not in comments ideally)
        hrefs = re.findall(r'href=["\']([^"\']*specyalisty[^"\']*)["\']', html, re.I)
        live_old[name] = hrefs

    report["internal"] = {
        "old_hrefs_by_page": live_old,
        "LIVE_INTERNAL_LINKS_TO_specyalisty": sum(len(v) for v in live_old.values()),
        "home_has_specialisty": bool(re.search(r"/specialisty/", home["body"])),
    }

    # Acceptance rollup
    singles_ok = all(x["status"] == 200 and x["canonical"].endswith(f"/specialisty/{x['slug']}/") for x in report["new_singles"])
    old_ok = report["old_hub"]["chain_ok"] and all(x["chain_ok"] for x in report["old_singles"])
    seo_ok = (
        report["seo"]["pages_sitemap_has_new"]
        and not report["seo"]["pages_sitemap_has_old"]
        and report["seo"]["specialists_sitemap_new_count"] == 9
        and report["seo"]["specialists_sitemap_old_count"] == 0
        and report["seo"]["hub_canonical_expected"]
    )
    report["verdict"] = {
        "new_hub_200": report["new_hub"]["status"] == 200,
        "singles_ok": singles_ok,
        "old_redirects_ok": old_ok,
        "seo_ok": seo_ok,
        "internal_old_zero": report["internal"]["LIVE_INTERNAL_LINKS_TO_specyalisty"] == 0,
        "PASS": (
            report["new_hub"]["status"] == 200
            and singles_ok
            and old_ok
            and seo_ok
            and report["internal"]["LIVE_INTERNAL_LINKS_TO_specyalisty"] == 0
        ),
    }

    OUT.joinpath("05-live-qa.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report["verdict"], ensure_ascii=False, indent=2))
    print("old_hub", report["old_hub"])
    print("internal", report["internal"]["LIVE_INTERNAL_LINKS_TO_specyalisty"], report["internal"]["old_hrefs_by_page"])
    print("seo specs", report["seo"]["specialists_sitemap_new_count"], "old", report["seo"]["specialists_sitemap_old_count"])


if __name__ == "__main__":
    main()
