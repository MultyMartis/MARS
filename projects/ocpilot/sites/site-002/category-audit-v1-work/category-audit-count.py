#!/usr/bin/env python3
import re

h = open(
    r"C:\AI MARS\projects\ocpilot\sites\site-002\category-audit-v1-work\category-live.html",
    encoding="utf-8",
).read()
print("p-cards", len(re.findall(r'<article class="p-card', h)))
print("old_price", h.count("p-card__old-price"))
print("order", h.count("p-card--order"))
print("in-stock", h.count("p-card--in-stock"))
