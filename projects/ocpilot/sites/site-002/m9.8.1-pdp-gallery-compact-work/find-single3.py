#!/usr/bin/env python3
import re
import urllib.request

BASE = "https://zpm.new-site.space"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "qa"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")

html = fetch(BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-standart")
links = []
for href in re.findall(r'href="([^"]+)"', html):
    if href.startswith("/"):
        href = BASE + href
    elif not href.startswith("http"):
        href = BASE + "/" + href.lstrip("/")
    if BASE in href and href.count("/") >= 6 and href not in links:
        links.append(href)

print("candidates", len(links))
for url in links:
    if "stoly-serii" in url and "?" not in url:
        try:
            pdp = fetch(url)
        except Exception:
            continue
        if "product-gallery" not in pdp:
            continue
        thumbs = len(re.findall(r"product-gallery__thumb", pdp))
        fancy = len(re.findall(r'data-fancybox="product"', pdp))
        if thumbs <= 1:
            print("candidate single-ish", thumbs, fancy, url[:120])
