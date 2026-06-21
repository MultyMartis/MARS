# -*- coding: utf-8 -*-
import ssl, urllib.parse, urllib.request, re

ctx = ssl.create_default_context()

def cards(fs, path):
    url = "https://zpm.new-site.space" + path + "?" + "filters=" + urllib.parse.quote(fs, safe="[];=")
    h = urllib.request.urlopen(url, context=ctx, timeout=60).read().decode("utf-8")
    return len(re.findall(r'<article class="p-card', h)), url

tests = [
    ("/katalog/nejtralnoe-oborudovanie/stoly/", "attr[51][]=Без полки"),
    ("/katalog/nejtralnoe-oborudovanie/stoly/", "attr[51][]=Без полки;price_from=5405;price_to=79010"),
    ("/katalog/nejtralnoe-oborudovanie/moechnye-vanny/", "attr[shell-size][]=600х600х400"),
    ("/katalog/nejtralnoe-oborudovanie/moechnye-vanny/", "attr[shell-size][]=600х600х400;price_from=5553;price_to=500000"),
    ("/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/", "attr[construction][]=угловая, купольная"),
    ("/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/", "attr[construction][]=угловая, купольная;price_from=19607;price_to=500000"),
]
for path, fs in tests:
    n, url = cards(fs, path)
    open(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06k-work\combo-probe-results.txt", "a", encoding="utf-8").write(f"{n}\t{fs}\n{url}\n\n")
