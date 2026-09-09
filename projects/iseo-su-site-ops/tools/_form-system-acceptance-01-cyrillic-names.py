#!/usr/bin/env python3
import re
import urllib.request

UA = {"User-Agent": "ISEO-SU-FSA-01"}
urls = [
    "https://i-seo.su/career.html",
    "https://i-seo.su/reviews.html",
    "https://i-seo.su/partners.html",
    "https://i-seo.su/bonuses.html",
    "https://i-seo.su/contacts.html",
]
cyr_s = "\u0441"  # Cyrillic es
for url in urls:
    html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode(
        "utf-8", "replace"
    )
    names = re.findall(r'name="([^"]+)"', html)
    bad = [n for n in names if cyr_s in n or any(ord(ch) > 127 for ch in n)]
    print(url, "non_ascii_names", bad)
