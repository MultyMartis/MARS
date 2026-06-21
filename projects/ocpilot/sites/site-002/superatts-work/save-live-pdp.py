#!/usr/bin/env python3
import urllib.request, re, json
from html import unescape

URLS = {
    "bath": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
    "table": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
}

def parse(url):
    html = urllib.request.urlopen(url, timeout=60).read().decode("utf-8")
    hero = []
    b = re.search(r'product-hero__props">(.*?)</dl>', html, re.S)
    if b:
        for m in re.finditer(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', b.group(1), re.S):
            n = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip()))
            v = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2)).strip()))
            hero.append({"name": n, "value": v})
    specs = []
    spec_block = re.search(r'id="tab-spec"[^>]*>(.*?)</div>\s*</div>\s*</div>', html, re.S)
    if spec_block:
        for m in re.finditer(r'spec-table__key">(.*?)</div>\s*<div class="spec-table__val">(.*?)</div>', spec_block.group(1), re.S):
            specs.append(
                {
                    "name": unescape(re.sub(r"\s+", " ", m.group(1).strip())),
                    "value": unescape(re.sub(r"\s+", " ", m.group(2).strip())),
                }
            )
    return hero, specs

out = {}
for k,u in URLS.items():
    hero, specs = parse(u)
    out[k] = {"url": u, "hero": hero, "specs_count": len(specs), "specs": specs[:30]}
with open(r"C:\AI MARS\projects\ocpilot\sites\site-002\superatts-work\live-pdp-data.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("written")
