#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops")
hub = (ROOT / "production-source/static-html/services/seo.html").read_text(encoding="utf-8")
files = [
    "prodvizhenie-sajta-pitomnika.html",
    "prodvizhenie-sajta-smi.html",
    "prodvizhenie-sajta-restorana.html",
    "prodvizhenie-internet-magazina-zapchastej.html",
    "prodvizhenie-sajta-internet-provajdera.html",
    "prodvizhenie-internet-magazina-kosmetiki.html",
    "prodvizhenie-internet-magazina-czvetov.html",
]
labels = [
    "SEO продвижение сайта питомника",
    "SEO продвижение сайта СМИ",
    "SEO продвижение сайта ресторана",
    "SEO продвижение Интернет-магазина запчастей",
    "SEO продвижение сайта интернет-провайдера",
    "SEO продвижение Интернет-магазина косметики",
    "SEO продвижение Интернет-магазина цветов",
]
print("file present:")
for f in files:
    print(f, f"/services/seo/{f}" in hub)
print("labels:")
for lab in labels:
    print(lab, lab in hub)
# show last part of navigations
m = re.search(r"more_landing_pages__navigations([\s\S]{0,30000}?)</div>", hub, re.I)
if m:
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', m.group(1), re.S)
    print("count", len(links))
    for href, label in links[-10:]:
        text = re.sub(r"<[^>]+>", "", label).replace("\xa0", " ").strip()
        print(href, "|", text)
else:
    print("NO NAV BLOCK")
