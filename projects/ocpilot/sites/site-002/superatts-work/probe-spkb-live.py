#!/usr/bin/env python3
import json
import re
import urllib.request
from html import unescape

URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)

html = urllib.request.urlopen(URL, timeout=60).read().decode("utf-8")

debug = re.search(r'<pre[^>]*data-debug="super-atts"[^>]*>(.*?)</pre>', html, re.S)
debug_text = unescape(re.sub(r"<[^>]+>", "", debug.group(1))).strip() if debug else None

props_block = re.search(r'<dl class="product-hero__props">(.*?)</dl>', html, re.S)
props = []
if props_block:
    for m in re.finditer(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", props_block.group(1), re.S):
        props.append(
            {
                "name": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip())),
                "value": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2)).strip())),
            }
        )

out = {"url": URL, "debug_text": debug_text, "hero_props": props, "hero_count": len(props)}
print(json.dumps(out, ensure_ascii=False, indent=2))
