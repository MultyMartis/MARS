#!/usr/bin/env python3
import re
import urllib.request

BASE = "https://zpm.new-site.space"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "qa"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


cat = fetch(BASE + "/index.php?route=product/category&path=301")
links = []
for href in re.findall(r'href="([^"]+)"', cat):
    if "route=product/product" in href or "/katalog/" in href:
        if href.startswith("/"):
            href = BASE + href
        elif not href.startswith("http"):
            href = BASE + "/" + href.lstrip("/")
        if href not in links and "product" in href:
            links.append(href)

print("links", len(links))
for url in links[:30]:
    try:
        pdp = fetch(url)
    except Exception as e:
        print("fail", url, e)
        continue
    if "product-gallery" not in pdp:
        continue
    thumbs = len(re.findall(r"product-gallery__thumb", pdp))
    fancy = len(re.findall(r'data-fancybox="product"', pdp))
    print(thumbs, fancy, url)
    if thumbs == 0 and fancy >= 1:
        print("SINGLE:", url)
        break
