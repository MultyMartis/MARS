#!/usr/bin/env python3
import re
import urllib.request

BASE = "https://zpm.new-site.space"
html = urllib.request.urlopen(
    urllib.request.Request(BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-standart", headers={"User-Agent": "qa"}),
    timeout=45,
).read().decode("utf-8", "replace")

for href in re.findall(r'href="(https://zpm\.new-site\.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-standart/[^"]+)"', html):
    pdp = urllib.request.urlopen(urllib.request.Request(href, headers={"User-Agent": "qa"}), timeout=45).read().decode("utf-8", "replace")
    thumbs = len(re.findall(r"product-gallery__thumb", pdp))
    if thumbs == 0 and "product-gallery" in pdp:
        print(href)
        break
