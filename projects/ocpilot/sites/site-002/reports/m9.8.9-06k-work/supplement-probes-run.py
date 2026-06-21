#!/usr/bin/env python3
"""Supplement probes: price range + UI default combo."""
import json, re, ssl, urllib.parse, urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06k-work\supplement-probes.json")

CATS = {
    "stoly": BASE + "/katalog/nejtralnoe-oborudovanie/stoly/",
    "podtovarniki": BASE + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    "telezhki": BASE + "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
    "moechnye_vanny": BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    "zonty": BASE + "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
}

ctx = ssl.create_default_context()

def fetch(url):
    return urllib.request.urlopen(url, context=ctx, timeout=90).read().decode("utf-8", "replace")

def cards(html):
    return len(re.findall(r'<article class="p-card', html)) or len(re.findall(r'product-layout', html))

def probe(base, fs):
    url = base + "?" + "filters=" + urllib.parse.quote(fs, safe="[];=")
    h = fetch(url)
    return {"filter": fs, "cards": cards(h), "url": url}

def extract_price(html):
    out = {}
    for field in ("price", "len", "w", "h"):
        m = re.search(
            rf'data-range-field="{field}"[^>]*data-range-min="(\d+)"[^>]*data-range-max="(\d+)"',
            html,
        )
        if not m:
            m = re.search(
                rf'data-range-field="{field}".*?data-range-min[^>]*min="(\d+)"[^>]*max="(\d+)"',
                html,
                re.S,
            )
        if m:
            out[field] = {"min": int(m.group(1)), "max": int(m.group(2))}
    pf = re.search(r'name="price_from"[^>]*value="(\d+)"', html)
    pt = re.search(r'name="price_to"[^>]*value="(\d+)"', html)
    if not pf:
        pf = re.search(r'name="price_from"[^>]*placeholder="(\d+)"', html)
    if not pt:
        pt = re.search(r'name="price_to"[^>]*placeholder="(\d+)"', html)
    out["price_inputs"] = {
        "from": int(pf.group(1)) if pf else None,
        "to": int(pt.group(1)) if pt else None,
    }
    return out

def extract_filters(html):
    items = []
    for m in re.finditer(
        r'<fieldset[^>]*class="[^"]*flt__group[^"]*"[^>]*>.*?<legend[^>]*>(.*?)</legend>.*?</fieldset>',
        html,
        re.S,
    ):
        legend = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        block = m.group(0)
        keys = set()
        for inp in re.finditer(r'name="(attr\[[^\]]+\]\[\]|s\[\]|price_from|price_to|[^"]+)"', block):
            n = inp.group(1)
            if n.startswith("attr["):
                k = re.match(r"attr\[([^\]]+)\]", n).group(1)
                t = "numeric" if k.isdigit() else "slug"
                keys.add((k, t, n))
        for k, t, n in sorted(keys):
            items.append({"legend": legend, "filter_key": k, "key_type": t, "html_name": n})
    return items

results = {}
for name, url in CATS.items():
    html = fetch(url)
    price = extract_price(html)
    filters = extract_filters(html)
    probes = [
        probe(url, "(baseline)"),
        probe(url, f"price_from={price['price_inputs']['from']};price_to={price['price_inputs']['to']}") if price.get("price_inputs", {}).get("from") is not None else None,
        probe(url, f"price_from=1;price_to={price['price_inputs']['to']}") if price.get("price_inputs", {}).get("to") else None,
    ]
    # combo: attr + full price range (simulates UI submit)
    if name == "stoly":
        probes.append(probe(url, f"attr[51][]=Без полки;price_from={price['price_inputs']['from']};price_to={price['price_inputs']['to']}"))
        probes.append(probe(url, "attr[51][]=Без полки;only_with_price=1"))
    if name == "podtovarniki":
        probes.append(probe(url, "attr[51][]=600х400х300;only_with_price=1"))
    if name == "moechnye_vanny":
        probes.append(probe(url, "attr[shell-size][]=600х600х400;only_with_price=1"))
    if name == "zonty":
        probes.append(probe(url, "attr[construction][]=угловая, купольная;only_with_price=1"))
    results[name] = {
        "baseline_cards": cards(html),
        "price_meta": price,
        "sidebar_filter_inventory": filters,
        "probes": [p for p in probes if p],
    }

# save filter html excerpt for stoly
html = fetch(CATS["stoly"])
m = re.search(r'<form[^>]*filters-form[^>]*>.*?</form>', html, re.S)
if m:
    Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06k-work\stoly-filter-form.html").write_text(m.group(0), encoding="utf-8")

OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print("done", OUT)
