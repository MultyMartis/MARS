#!/usr/bin/env python3
import re
import urllib.request

html = urllib.request.urlopen(
    urllib.request.Request("https://i-seo.su/services/seo.html", headers={"User-Agent": "x"}),
    timeout=30,
).read().decode("utf-8", "replace")
print("count tariff_1 popup href", html.count("tariff_1__FORM_popup"))
print("modalbox count", html.count("modalbox"))
hrefs = re.findall(r'<a[^>]+href="#([^"]+)"[^>]*class="[^"]*modalbox[^"]*"[^>]*>', html)
print("modalbox hrefs sample", sorted(set(hrefs))[:40])
hrefs2 = re.findall(r'href="#(tariff_[^"]+)"', html)
print("tariff hrefs", hrefs2)
# maybe fancybox data-src
print("Заказать near tariff")
idx = html.find("tariff_1__FORM_popup")
print(html[max(0, idx - 800) : idx][-400:])
