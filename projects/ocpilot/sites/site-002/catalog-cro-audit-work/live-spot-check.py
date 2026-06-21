#!/usr/bin/env python3
import json
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
OUT = Path(__file__).resolve().parent / "live-spot-check.json"
urls = {
    "stoly": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/",
    "vanny": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    "table_pdp": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
    "sink_pdp": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
}
result = {}
for k, u in urls.items():
    html = urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "spot-check"}), context=ctx, timeout=60
    ).read().decode("utf-8", "replace")
    card_m = re.search(r'class="p-card[^"]*".*?(?=class="p-card|$)', html, re.S)
    card = card_m.group(0)[:2000] if card_m else ""
    rel_m = re.search(r"Похожие товары.*?(?=</section>)", html, re.S | re.I)
    rel = rel_m.group(0) if rel_m else ""
    result[k] = {
        "p_card_count": len(re.findall(r'class="p-card', html)),
        "card_has_mm": bool(re.search(r"\d+\s*[×xх]\s*\d+", card)),
        "card_has_price": "p-card__price" in card,
        "card_has_article": "p-card__article" in card or "Арт" in card,
        "placeholder_subtitle": "мини-описанием" in html.lower() or "надо сделать" in html.lower(),
        "related_titles": re.findall(r"p-card__title[^>]*>([^<]+)", rel)[:6],
        "filter_empty_subcats": len(re.findall(r'flt__checkbox.*?0\s*шт', html, re.S)),
        "subcat_chips": len(re.findall(r"zpm-sub-cat-chip", html)),
        "product_count_label": bool(re.search(r"\d+\s*товар", html, re.I)),
    }
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
