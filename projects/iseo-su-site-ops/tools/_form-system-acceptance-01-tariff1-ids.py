#!/usr/bin/env python3
import re
import urllib.request

html = urllib.request.urlopen(
    urllib.request.Request("https://i-seo.su/services/seo.html", headers={"User-Agent": "x"}),
    timeout=30,
).read().decode("utf-8", "replace")
print("popup hrefs", sorted(set(re.findall(r'href="(#[^"]*tariff_1[^"]*)"', html))))
print("form ids", sorted(set(re.findall(r'id="(tariff_1[^"]*)"', html))))
print("send buttons", sorted(set(re.findall(r'id="(tariff_1__FORM_send[^"]*)"', html))))
