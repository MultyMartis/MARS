# -*- coding: utf-8 -*-
import re
import requests

UA = "FP-0002-PROD-MAINT-OLYA-ROBOTS/1.0"
css_urls = [
    "https://shpigovsky.ru/wp-content/themes/shpigovsky/assets/css/v9-style.css?ver=1787144758",
    "https://shpigovsky.ru/wp-content/themes/shpigovsky/assets/css/fp02-floating-header.css?ver=1786694333",
]
found = set()
for url in css_urls:
    text = requests.get(url, headers={"User-Agent": UA}, timeout=30).text
    for match in re.findall(r"url\(([^)]+)\)", text):
        cleaned = match.strip().strip("\"'")
        lower = cleaned.lower()
        if any(ext in lower for ext in (".woff", ".ttf", ".otf", ".eot", ".svg", ".webp", ".png")):
            found.add(cleaned)
print("count", len(found))
for item in sorted(found)[:50]:
    print(item)
