#!/usr/bin/env python3
import re
import urllib.request

UA = "ISEO-SU-FORM-SYSTEM-ACCEPTANCE-01-ACCEPT/1.0"
for url in [
    "https://i-seo.su/career.html",
    "https://i-seo.su/partners.html",
    "https://i-seo.su/reviews.html",
    "https://i-seo.su/bonuses.html",
    "https://i-seo.su/services/seo.html",
]:
    html = urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30
    ).read().decode("utf-8", "replace")
    ids = re.findall(r'id="([^"]*FORM[^"]*)"', html)
    print(url)
    for i in ids:
        print(" ", i)
    print()
