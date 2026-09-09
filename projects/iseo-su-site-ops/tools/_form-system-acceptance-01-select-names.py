#!/usr/bin/env python3
import re
import urllib.request

UA = {"User-Agent": "ISEO-SU-FSA-01"}
for url in [
    "https://i-seo.su/career.html",
    "https://i-seo.su/reviews.html",
    "https://i-seo.su/partners.html",
    "https://i-seo.su/contacts.html",
    "https://i-seo.su/guarantees.html",
]:
    html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode(
        "utf-8", "replace"
    )
    names = sorted(set(re.findall(r'<select[^>]*name="([^"]+)"', html, flags=re.I)))
    print(url, names)
