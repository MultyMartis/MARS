#!/usr/bin/env python3
import re
import urllib.parse
import urllib.request

BASE = "https://zpm.new-site.space"
SKU = "СПКБ-18/7-ВЛ5"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "qa"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


search_url = BASE + "/index.php?route=product/search&search=" + urllib.parse.quote(SKU)
html = fetch(search_url)
print("search len", len(html))
links = []
for href in re.findall(r'href="([^"]+)"', html):
    if "route=product/product" in href or "product_id=" in href:
        links.append(href)
print("links", len(links), links[:5])

css = fetch(BASE + "/assets/css/style.css")
idx = css.find("@media (min-width: 1025px)")
print("css idx", idx)
if idx >= 0:
    print(css[idx : idx + 500])

js = fetch(BASE + "/assets/js/main.js")
print("js has GALLERY_DESKTOP_MQ", "GALLERY_DESKTOP_MQ" in js)
