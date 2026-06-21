#!/usr/bin/env python3
import json
import urllib.request

URLS = [
    ("spkb", "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"),
    ("spp", "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850"),
    ("vms", "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-svarnye-premium/vanna-moechnaya-vms-p-2-600-1400h700h850"),
    ("pp", "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/podtovarniki-premium/podtovarnik-pp-p-12-6-1200h600h300"),
]


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": "beget=begetok"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")


def classify(html):
    has_desc = "product-content__description" in html
    has_docs = "product-content__documents" in html and "docs-list__item" in html
    wrapper = "product-content__specs-docs" in html
    standalone = "product-content__specifications" in html and not wrapper
    return {
        "has_desc": has_desc,
        "has_docs": has_docs,
        "specs_docs_wrapper": wrapper,
        "standalone_specs": standalone,
        "help": "product-help" in html,
        "related": "rel-products" in html,
        "php_ok": "Fatal error" not in html,
    }


out = {}
for name, url in URLS:
    out[name] = {"url": url, **classify(fetch(url))}

path = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\check-known-urls-result.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(json.dumps(out, ensure_ascii=False, indent=2))
