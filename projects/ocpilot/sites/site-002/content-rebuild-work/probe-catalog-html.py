#!/usr/bin/env python3
import re
import urllib.request

url = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
req = urllib.request.Request(url, headers={"Cookie": "beget=begetok"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
print("len", len(html))
print("product-hero count", html.count("product-hero"))
for pat in [r'href="([^"]*stol[^"]*)"', r'href="([^"]*katalog[^"]*)"', r'class="[^"]*product[^"]*"']:
    m = re.findall(pat, html)
    print(pat, len(m))
    for x in m[:8]:
        print(" ", x[:120])
