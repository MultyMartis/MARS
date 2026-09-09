#!/usr/bin/env python3
import re
import urllib.request

html = urllib.request.urlopen(
    urllib.request.Request("https://i-seo.su/career.html", headers={"User-Agent": "x"}),
    timeout=30,
).read().decode("utf-8", "replace")
ids = re.findall(r'id="(career[^"]*)"', html)
print("ids", ids)
print("has career__FORM ", 'id="career__FORM"' in html)
print("has popup", "career__FORM_popup" in html)
