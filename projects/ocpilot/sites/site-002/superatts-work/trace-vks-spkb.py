#!/usr/bin/env python3
import json
import re
import urllib.request
from html import unescape

VKS_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
    "kotlomoyki-premium/vanna-kotlomoechnaya-vks-p-1-400-900-1000h500h850"
)
SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)
WRONG_VKS = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
    "kotlomoechnye-premium/vanna-kotlomoechnaya-vks-p-1-400-900"
)

TERMS = [
    "Конструкция",
    "Наличие борта",
    "Ножки",
    "Отверстие под смеситель",
    "Размер раковины",
    "Тип опоры",
    "Усиление",
]


def fetch(url):
    try:
        r = urllib.request.urlopen(url, timeout=60)
        return r.read().decode("utf-8", "replace"), r.status
    except Exception as e:
        return None, str(e)


def parse_hero(html):
    hero = re.search(r'<section class="product-hero".*?</section>', html, re.S)
    scope = hero.group(0) if hero else html
    primary, additional = [], []
    prim = re.search(
        r'<dl class="product-hero__props product-hero__props--primary">(.*?)</dl>',
        scope,
        re.S,
    )
    add = re.search(
        r'<dl class="product-hero__props product-hero__props--additional">(.*?)</dl>',
        scope,
        re.S,
    )
    for block, dest in [(prim, primary), (add, additional)]:
        if not block:
            continue
        for m in re.finditer(
            r'<div class="product-hero__prop">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',
            block.group(1),
            re.S,
        ):
            dest.append(
                {
                    "name": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip())),
                    "value": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2)).strip())),
                }
            )
    return primary, additional


def find_term(html, term):
    hero = re.search(r'<section class="product-hero".*?</section>', html, re.S)
    hero_html = hero.group(0) if hero else ""
    specs = re.search(r'id="tab-spec".*?</div>\s*</div>', html, re.S)
    specs_html = specs.group(0) if specs else ""
    loc = []
    if term.lower() in hero_html.lower():
        loc.append("hero")
    if term.lower() in specs_html.lower():
        loc.append("characteristics tab")
    if term.lower() in html.lower() and not loc:
        loc.append("elsewhere")
    if term.lower() not in html.lower():
        loc.append("not found")
    snippet = None
    if "hero" in loc:
        idx = hero_html.lower().find(term.lower())
        snippet = hero_html[max(0, idx - 60) : idx + 240]
    return {"found": term.lower() in html.lower(), "location": loc, "hero_snippet": snippet}


def probe(label, url):
    html, status = fetch(url)
    if html is None:
        return {"url": url, "error": status}
    primary, additional = parse_hero(html)
    return {
        "url": url,
        "status": status,
        "hero_primary": primary,
        "hero_additional": additional,
        "hero_total": len(primary) + len(additional),
        "has_split": "product-hero__specs--split" in html,
        "has_additional_dl": "product-hero__props--additional" in html,
        "terms": {t: find_term(html, t) for t in TERMS},
    }


out = {
    "wrong_vks_url": probe("WRONG", WRONG_VKS),
    "vks": probe("VKS", VKS_URL),
    "spkb": probe("SPKB", SPKB_URL),
}
path = r"C:\AI MARS\projects\ocpilot\sites\site-002\superatts-work\trace-vks-spkb.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(json.dumps(out, ensure_ascii=False, indent=2))
