# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
import re

UA = {"User-Agent": "QA"}


def get(url):
    return urlopen(Request(url, headers=UA), timeout=45).read().decode("utf-8", "replace")


h = get("https://shpigovsky.ru/")
print("home slider", "data-specialists-slider" in h, "cards", h.count("specialists__card"))
u = get("https://shpigovsky.ru/uslugi/")
links = re.findall(r'href="(https://shpigovsky.ru/uslugi/[^"#]+)"', u)
uniq = []
for link in links:
    if link.rstrip("/") == "https://shpigovsky.ru/uslugi":
        continue
    if link not in uniq:
        uniq.append(link)
found = 0
for url in uniq[:12]:
    try:
        b = get(url)
    except Exception as exc:
        print("ERR", url, exc)
        continue
    if "data-specialists-slider" in b or "specialists__card" in b:
        print("HAS_SPECIALISTS", url, "cards", b.count("specialists__card"))
        found += 1
        if found >= 2:
            break
print("done found", found)
