#!/usr/bin/env python3
import re
import urllib.request

url = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
req = urllib.request.Request(url, headers={"Cookie": "beget=begetok"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
links = re.findall(r'href="(/katalog/[^"]+)"', html)
print("total", len(links))
deep = [l for l in links if l.count("/") >= 6]
print("deep", len(deep))
for l in deep[:15]:
    print(l)
