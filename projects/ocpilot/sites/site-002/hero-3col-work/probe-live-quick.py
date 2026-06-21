#!/usr/bin/env python3
import re
import urllib.request

url = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)
req = urllib.request.Request(url, headers={"Cookie": "beget=begetok"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")

for pat in [
    "fontawesome",
    "all.min.css",
    "fa-arrows",
    "product-hero__props--primary",
    "fas fa-",
]:
    print(pat, ":", pat in html)

for m in re.findall(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*>', html):
    if "font" in m.lower() or "awesome" in m.lower():
        print("LINK:", m)

hero = re.search(r"product-hero__props--primary.*?</dl>", html, re.S)
if hero:
    print("PRIMARY BLOCK:", hero.group(0)[:800])
