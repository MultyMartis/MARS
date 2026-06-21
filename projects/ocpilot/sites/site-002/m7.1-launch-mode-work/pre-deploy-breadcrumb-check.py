#!/usr/bin/env python3
import re
import ssl
import urllib.request

BASE = "https://zpm.new-site.space"
URLS = {
    "PLP leaf": BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/",
    "PLP parent": BASE + "/katalog/nejtralnoe-oborudovanie/stoly/",
    "PDP": BASE
    + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
}
ctx = ssl.create_default_context()

for name, url in URLS.items():
    req = urllib.request.Request(url, headers={"User-Agent": "pre-deploy-check"})
    with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
        html = r.read().decode("utf-8", "replace")
    block = re.search(r'<nav class="breadcrumbs".*?</nav>', html, re.S)
    block = block.group(0) if block else ""
    links = re.findall(r'breadcrumbs__link"[^>]*href="([^"]+)"[^>]*>([^<]+)', block)
    curr = re.findall(r"breadcrumbs__current[^>]*>([^<]+)", block)
    print("=== PRE-DEPLOY", name, "===")
    for href, text in links:
        print(" ", text.strip(), "->", href)
    for text in curr:
        print(" [current]", text.strip())
