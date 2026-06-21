#!/usr/bin/env python3
import re
import urllib.request

URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)

req = urllib.request.Request(URL, headers={"Cookie": "beget=begetok"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")

ids = sorted(set(re.findall(r'id="(zpmFb[^"]+)"', html)))
print("FB ids:", ids)

for pat in ["Быстрый заказ", "быстрый заказ", "Заказать звонок", "Задать вопрос"]:
    print(f"{pat!r}: {pat in html}")

for m in re.finditer(
    r'<button[^>]*data-fancybox[^>]*data-src="([^"]+)"[^>]*>.*?</button>',
    html,
    re.S,
):
    text = re.sub(r"\s+", " ", m.group(0))
    if any(x in text.lower() for x in ("заказ", "вопрос", "звонок", "price", "callback")):
        print("BTN:", text[:220])

hero = re.search(
    r'<div class="product-hero__col product-hero__col--commerce">(.*?)</div>\s*</div>\s*</div>',
    html,
    re.S,
)
if hero:
    print("\nCOMMERCE COL:\n", hero.group(0)[:2000])
