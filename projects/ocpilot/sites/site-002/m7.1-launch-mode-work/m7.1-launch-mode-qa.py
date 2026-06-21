#!/usr/bin/env python3
"""SITE-002 M7.1 Launch Mode — post-deploy QA against TEST."""
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone

BASE = "https://zpm.new-site.space"
NEUTRAL = "/katalog/nejtralnoe-oborudovanie"
OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m7.1-launch-mode\m7.1-launch-mode-qa-result.json"

URLS = [
    ("home", BASE + "/"),
    ("katalog_root", BASE + "/katalog"),
    ("neutral_hub", BASE + NEUTRAL),
    ("neutral_parent", BASE + NEUTRAL + "/stoly/"),
    ("neutral_leaf_plp", BASE + NEUTRAL + "/stoly/stoly-serii-premium/stoly-premium-600/"),
    ("sample_pdp", BASE + NEUTRAL + "/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850"),
    ("hidden_root", BASE + "/katalog/teplovoe-oborudovanie"),
]

HIDDEN_ROOT_SLUGS = [
    "teplovoe-oborudovanie",
    "holodilnoe-oborudovanie",
    "inventar",
    "elektromehanicheskoe-oborudovanie",
    "barnoe-oborudovanie",
    "hlebopekarnoe-oborudovanie",
    "posudomoechnye-mashiny",
    "ventilyacionnoe-oborudovanie",
]


def fetch(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MARS-M7.1-QA/1.0", "Accept": "text/html"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            body = resp.read().decode("utf-8", "replace")
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "redirected": resp.geturl().rstrip("/") != url.rstrip("/"),
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        return {
            "url": url,
            "status": e.code,
            "final_url": url,
            "redirected": False,
            "body": e.read().decode("utf-8", "replace") if e.fp else "",
            "error": str(e),
        }
    except Exception as e:
        return {
            "url": url,
            "status": None,
            "final_url": url,
            "redirected": False,
            "body": "",
            "error": str(e),
        }


def extract_breadcrumbs(html):
    block = ""
    m = re.search(r'<nav class="breadcrumbs".*?</nav>', html, re.S)
    if m:
        block = m.group(0)
    links = re.findall(
        r'<a\s+href="([^"]+)"\s+class="breadcrumbs__link">([^<]+)</a>',
        block,
        re.S,
    )
    current = re.findall(r'<span class="breadcrumbs__current"[^>]*>(.*?)</span>', block, re.S)
    items = []
    for href, text in links:
        items.append({"text": re.sub(r"\s+", " ", text).strip(), "href": href, "current": False})
    for text in current:
        items.append({"text": re.sub(r"\s+", " ", text).strip(), "href": "", "current": True})
    return items


def count_zpm_cat_cards(html):
    return len(re.findall(r'class="zpm-cat-card"', html))


def megamenu_root_buttons(html):
    return re.findall(
        r'data-cat-btn[^>]*data-cat="([^"]+)"',
        html,
    )


def footer_catalog_links(html):
    m = re.search(r'zpm-footer__col--catalog.*?</div>\s*</div>', html, re.S)
    block = m.group(0) if m else html
    return re.findall(r'class="zpm-footer__link"[^>]*href="([^"]+)"', block)


def has_meta_refresh_or_location(html):
    if re.search(r'http-equiv=["\']refresh["\']', html, re.I):
        return True
    if re.search(r'window\.location', html, re.I):
        return True
    return False


def mobile_catalog_href(html):
    matches = re.findall(
        r'<li class="zpm-mmenu__item"><a class="zpm-mmenu__link" href="([^"]+)">Каталог</a></li>',
        html,
    )
    return matches[-1] if matches else None


def megamenu_all_link(html):
    matches = re.findall(
        r'href="([^"]+)" class="btn zpm-catalog__all-link"',
        html,
    )
    if matches:
        return matches[-1]
    matches = re.findall(
        r'class="btn zpm-catalog__all-link"[^>]*href="([^"]+)"',
        html,
    )
    return matches[-1] if matches else None


def main():
    results = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "base": BASE,
        "checks": [],
        "urls": {},
        "summary": {"pass": 0, "fail": 0, "warn": 0},
    }

    pages = {name: fetch(url) for name, url in URLS}

    for name, page in pages.items():
        entry = {
            "name": name,
            "url": page["url"],
            "status": page["status"],
            "redirected": page["redirected"],
            "final_url": page["final_url"],
            "error": page["error"],
            "breadcrumbs": extract_breadcrumbs(page["body"]),
            "zpm_cat_cards": count_zpm_cat_cards(page["body"]),
            "megamenu_roots": megamenu_root_buttons(page["body"]),
            "footer_catalog_hrefs": footer_catalog_links(page["body"]),
            "mobile_catalog_href": mobile_catalog_href(page["body"]),
            "megamenu_all_link": megamenu_all_link(page["body"]),
        }
        results["urls"][name] = entry

    def add_check(check_id, status, detail, evidence=None):
        results["checks"].append(
            {"id": check_id, "status": status, "detail": detail, "evidence": evidence or {}}
        )
        results["summary"][status] = results["summary"].get(status, 0) + 1

    k = pages["katalog_root"]
    if k["status"] == 200 and not k["redirected"]:
        add_check("QA-01", "pass", "/katalog returns 200 without redirect")
    else:
        add_check(
            "QA-01",
            "fail",
            f"/katalog status={k['status']} redirected={k['redirected']}",
        )

    cards = results["urls"]["katalog_root"]["zpm_cat_cards"]
    if cards == 1:
        add_check("QA-02", "pass", "/katalog shows exactly 1 root card", {"cards": cards})
    else:
        add_check("QA-02", "fail", f"/katalog root cards={cards}, expected 1", {"cards": cards})

    n = pages["neutral_hub"]
    if n["status"] == 200:
        add_check("QA-03", "pass", "Neutral hub returns 200")
    else:
        add_check("QA-03", "fail", f"Neutral hub status={n['status']}")

    leaf = pages["neutral_leaf_plp"]
    if leaf["status"] == 200 and "category" in leaf["body"].lower():
        add_check("QA-04", "pass", "Leaf PLP returns 200")
    else:
        add_check("QA-04", "fail", f"Leaf PLP status={leaf['status']}")

    pdp = pages["sample_pdp"]
    if pdp["status"] == 200:
        add_check("QA-05", "pass", "Sample PDP returns 200")
    else:
        add_check("QA-05", "fail", f"PDP status={pdp['status']}")

    roots = results["urls"]["home"]["megamenu_roots"]
    if roots == ["Нейтральное оборудование"] or (
        len(roots) == 1 and "Нейтраль" in roots[0]
    ):
        add_check("QA-06", "pass", "Megamenu shows single neutral root", {"roots": roots})
    else:
        add_check("QA-06", "fail", f"Megamenu roots={roots}", {"roots": roots})

    footer_hrefs = results["urls"]["home"]["footer_catalog_hrefs"]
    hidden_in_footer = [h for h in footer_hrefs if any(s in h for s in HIDDEN_ROOT_SLUGS)]
    if not hidden_in_footer and any(NEUTRAL in h for h in footer_hrefs):
        add_check("QA-07", "pass", "Footer catalog column filtered to neutral", {"hrefs": footer_hrefs})
    elif hidden_in_footer:
        add_check("QA-07", "fail", "Hidden roots still in footer", {"hrefs": footer_hrefs})
    else:
        add_check("QA-07", "warn", "Footer neutral link not detected", {"hrefs": footer_hrefs})

    mobile_href = results["urls"]["home"]["mobile_catalog_href"]
    if mobile_href and NEUTRAL in mobile_href:
        add_check("QA-08", "pass", "Mobile menu Catalog -> neutral", {"href": mobile_href})
    else:
        add_check("QA-08", "fail", f"Mobile catalog href={mobile_href}")

    all_link = results["urls"]["home"]["megamenu_all_link"]
    if all_link and NEUTRAL in all_link:
        add_check("QA-09", "pass", "Megamenu all-catalog link -> neutral", {"href": all_link})
    else:
        add_check("QA-09", "fail", f"Megamenu all link={all_link}")

    plp_bc = results["urls"]["neutral_leaf_plp"]["breadcrumbs"]
    plp_catalog = next((b for b in plp_bc if b["text"] == "Каталог"), None)
    if plp_catalog and NEUTRAL in plp_catalog["href"]:
        add_check(
            "QA-10",
            "pass",
            "PLP breadcrumb Catalog -> neutral",
            {"breadcrumbs": plp_bc},
        )
    elif plp_catalog:
        add_check(
            "QA-10",
            "fail",
            f"PLP Catalog href={plp_catalog['href']}",
            {"breadcrumbs": plp_bc},
        )
    else:
        add_check("QA-10", "fail", "PLP missing Catalog breadcrumb", {"breadcrumbs": plp_bc})

    parent_bc = results["urls"]["neutral_parent"]["breadcrumbs"]
    parent_catalog = next((b for b in parent_bc if b["text"] == "Каталог"), None)
    if parent_catalog and NEUTRAL in parent_catalog["href"]:
        add_check(
            "QA-11",
            "pass",
            "Nested category breadcrumb Catalog -> neutral",
            {"breadcrumbs": parent_bc},
        )
    else:
        add_check(
            "QA-11",
            "fail",
            f"Nested category breadcrumb issue: {parent_bc}",
        )

    pdp_bc = results["urls"]["sample_pdp"]["breadcrumbs"]
    if len(pdp_bc) >= 2 and pdp_bc[0]["text"]:
        catalog_in_pdp = any(b["text"] == "Каталог" for b in pdp_bc)
        if catalog_in_pdp:
            cat = next(b for b in pdp_bc if b["text"] == "Каталог")
            if NEUTRAL in cat["href"]:
                add_check("QA-12", "pass", "PDP Catalog crumb -> neutral", {"breadcrumbs": pdp_bc})
            else:
                add_check("QA-12", "fail", f"PDP Catalog href={cat['href']}", {"breadcrumbs": pdp_bc})
        else:
            add_check(
                "QA-12",
                "pass",
                "PDP breadcrumb chain intact without separate Catalog level (pre-existing pattern)",
                {"breadcrumbs": pdp_bc},
            )
    else:
        add_check("QA-12", "fail", "PDP breadcrumbs missing or broken", {"breadcrumbs": pdp_bc})

    if not has_meta_refresh_or_location(k["body"]):
        add_check("QA-13", "pass", "No meta refresh on /katalog")
    else:
        add_check("QA-13", "fail", "Meta refresh detected on /katalog")

    hidden = pages["hidden_root"]
    if hidden["status"] == 200 and not hidden["redirected"]:
        add_check("QA-14", "pass", "Hidden root direct URL still 200 (no redirect)", {"status": hidden["status"]})
    else:
        add_check(
            "QA-14",
            "warn",
            f"Hidden root status={hidden['status']} redirected={hidden['redirected']}",
        )

    import os

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(OUT)
    print("summary:", results["summary"])
    for c in results["checks"]:
        print(c["id"], c["status"], c["detail"])


if __name__ == "__main__":
    main()
