#!/usr/bin/env python3
import json
import re
import urllib.request

URLS = {
    "hub": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie",
    "katalog": "https://zpm.new-site.space/katalog",
    "stoly": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly",
    "vanny": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny",
    "podtov": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki",
}

results = {}
for name, url in URLS.items():
    html = urllib.request.urlopen(url, timeout=30).read().decode("utf-8", errors="replace")
    intro_match = re.search(r'<section class="page-intro">.*?</section>', html, re.S)
    results[name] = {
        "url": url,
        "has_page_intro__description": "page-intro__description" in html,
        "page_intro_snippet": (intro_match.group(0) if intro_match else "NO page-intro")[:400],
    }

print(json.dumps(results, indent=2, ensure_ascii=False))
