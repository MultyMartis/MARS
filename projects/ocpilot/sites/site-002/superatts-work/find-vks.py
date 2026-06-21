#!/usr/bin/env python3
import re
import urllib.parse
import urllib.request

def search(q):
    url = "https://zpm.new-site.space/index.php?route=product/search&search=" + urllib.parse.quote(q)
    html = urllib.request.urlopen(url, timeout=30).read().decode("utf-8", "replace")
    links = set()
    for m in re.finditer(r'href="([^"]+)"', html):
        h = m.group(1)
        if "vks" in h.lower() or "400-900" in h.lower() or "400" in h.lower() and "vks" in h.lower():
            links.add(h)
    return sorted(links)

for q in ["VKS-P-1", "VKS", "ВКС-П-1", "400-900", "kotlomoechnaya"]:
    print("Q:", q)
    for l in search(q)[:10]:
        print(" ", l)

# try category page
cat = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/kotlomoechnye-premium/"
html = urllib.request.urlopen(cat, timeout=30).read().decode("utf-8", "replace")
for m in re.finditer(r'href="([^"]*vks[^"]*)"', html, re.I):
    print("CAT:", m.group(1))
