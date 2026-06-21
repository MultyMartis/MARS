#!/usr/bin/env python3
import re
import urllib.request

URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)
req = urllib.request.Request(
    URL, headers={"User-Agent": "check", "Cookie": "beget=begetok"}
)
html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
for pat in [
    "relproducts",
    "product-related",
    "related",
    "rel-products",
    "p-card",
    "Сопутств",
    "Похож",
    "Аналог",
]:
    print(pat, pat.lower() in html.lower())
for m in re.finditer(r'class="([^"]{0,80})"', html):
    c = m.group(1)
    if "rel" in c.lower() or "similar" in c.lower() or "related" in c.lower():
        print("class:", c)
