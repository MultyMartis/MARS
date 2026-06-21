#!/usr/bin/env python3
"""Live PDP hero probe for bath + table."""
import re
import urllib.request
from html import unescape

BATH = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850"
TABLE = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850"

# from site-002-w1b-db-final.json all_attributes
ID_NAMES = {
    12: "Габариты нетто (мм)",
    13: "Габариты брутто (мм)",
    14: "?",  # need lookup
    15: "Гарантия",
    21: "Конструкция",
    25: "Наличие борта",
    26: "Ножки",
    28: "?", 
    29: "?",
    30: "Материал",
    33: "Тип опоры",
    115: "?",
}


def fetch(url):
    return urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")


def hero(html):
    b = re.search(r'<dl class="product-hero__props">(.*?)</dl>', html, re.S)
    if not b:
        return []
    out = []
    for m in re.finditer(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', b.group(1), re.S):
        out.append(
            (
                unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip())),
                unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2)).strip())),
            )
        )
    return out


def specs(html):
    tab = re.search(r'id="tab-spec"[^>]*>(.*?)(?:</section>|id="tab-)', html, re.S)
    scope = tab.group(1) if tab else html
    out = {}
    for m in re.finditer(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", scope, re.S):
        n = unescape(re.sub(r"<[^>]+>", "", m.group(1)).strip())
        v = unescape(re.sub(r"<[^>]+>", "", m.group(2)).strip())
        if n:
            out[n.lower()] = v
    return out


def probe(label, url):
    html = fetch(url)
    h = hero(html)
    s = specs(html)
    print(f"\n=== {label} ===")
    print("URL:", url)
    print("PHP error:", "Fatal error" in html or "Parse error" in html)
    print("Hero count:", len(h))
    for n, v in h:
        print(f"  HERO: {n} = {v}")
    print("Specs sample (first 20):")
    for i, (k, v) in enumerate(list(s.items())[:20]):
        print(f"  SPEC: {k} = {v[:60]}")
    # match SUPER_ATTS names from specs
    print("\nSUPER_ATTS ID check (by name match in specs/hero):")
    for aid, aname in sorted(ID_NAMES.items()):
        if aname == "?":
            continue
        in_specs = "YES" if any(aname.lower() in k or k in aname.lower() for k in s) else "NO"
        spec_val = next((s[k] for k in s if aname.lower() in k or k in aname.lower()), "")
        in_hero = "YES" if any(aname.lower() in x[0].lower() or x[0].lower() in aname.lower() for x in h) else "NO"
        print(f"  ID {aid} {aname}: on_product={'YES' if spec_val else 'NO'} val={spec_val!r} in_specs={in_specs} in_hero={in_hero}")


if __name__ == "__main__":
    probe("BATH", BATH)
    probe("TABLE", TABLE)
