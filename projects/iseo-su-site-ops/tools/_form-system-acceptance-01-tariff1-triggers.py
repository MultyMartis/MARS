#!/usr/bin/env python3
import re
import urllib.request

html = urllib.request.urlopen(
    urllib.request.Request("https://i-seo.su/services/seo.html", headers={"User-Agent": "x"}),
    timeout=30,
).read().decode("utf-8", "replace")
# context around FORM_popup
for m in re.finditer(r".{0,120}tariff_1__FORM_popup.{0,120}", html):
    print("---")
    print(m.group(0).replace("\n", " ")[:400])
print("data-src", re.findall(r'data-src="[^"]*tariff_1[^"]*"', html)[:10])
print("data-fancybox tariff", re.findall(r'data-fancybox[^>]{0,80}tariff_1[^>]{0,40}', html)[:10])
# tariff CTA buttons
print("cta snippets")
for m in re.finditer(r"<a[^>]{0,200}тариф[^>]{0,80}>|<button[^>]{0,200}тариф[^>]{0,80}>", html, re.I):
    print(m.group(0)[:250])
    if m.start() > 5:
        break
