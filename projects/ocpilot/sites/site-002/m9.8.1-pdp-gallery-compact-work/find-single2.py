#!/usr/bin/env python3
import re
import urllib.request

BASE = "https://zpm.new-site.space"
cat = fetch = lambda url: urllib.request.urlopen(
    urllib.request.Request(url, headers={"User-Agent": "qa"}), timeout=45
).read().decode("utf-8", "replace")

html = fetch(BASE + "/index.php?route=product/category&path=301")
print("len", len(html))
hrefs = re.findall(r'href="([^"]+)"', html)
print("sample", [h for h in hrefs if "stol" in h.lower()][:10])
print("pcard", "p-card" in html)
