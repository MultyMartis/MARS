# -*- coding: utf-8 -*-
import ssl, urllib.parse, urllib.request, re

ctx = ssl.create_default_context()

def probe(url, fs=None):
    if fs:
        url = url + "?" + "filters=" + urllib.parse.quote(fs, safe="[];=")
    h = urllib.request.urlopen(url, context=ctx, timeout=60).read().decode("utf-8")
    cards = len(re.findall(r'<article class="p-card', h))
    attrs = re.findall(r'name="attr\[([^\]]+)\]\[\]"[^>]*value="([^"]+)"', h)
    return cards, attrs[:5], url

for base in [
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
    "https://zpm.new-site.space/zonty-vytyazhnye/",
]:
    c, attrs, _ = probe(base)
    print("BASE", c, base)
    print("attrs sample", attrs)
    if attrs:
        k, v = attrs[0]
        c2, _, u2 = probe(base, f"attr[{k}][]={v}")
        print("FIRST ATTR FILTER", c2, u2)
