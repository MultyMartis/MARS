#!/usr/bin/env python3
import re
import urllib.request

html = urllib.request.urlopen(
    urllib.request.Request("https://i-seo.su/career.html", headers={"User-Agent": "x"}),
    timeout=30,
).read().decode("utf-8", "replace")
# career forms
for m in re.finditer(r'<form[^>]*id="([^"]*career[^"]*)"[^>]*>', html, re.I):
    print("FORM", m.group(1), m.group(0)[:200])
idx = html.find('id="career__FORM_info"')
print("--- snippet ---")
print(html[idx : idx + 2500])
