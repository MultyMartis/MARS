import ssl, urllib.parse, urllib.request, re

BASE = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/"
ctx = ssl.create_default_context()

def cards(url):
    h = urllib.request.urlopen(url, context=ctx, timeout=60).read().decode()
    return len(re.findall(r'<article class="p-card', h))

def probe(path, fs):
    url = BASE + path + "?" + "filters=" + urllib.parse.quote(fs, safe="[];=")
    return fs, cards(url)

tests = [
    ("stoly/", "price_from=5405;price_to=79010"),
    ("stoly/", "attr[51][]=Без полки;price_from=5405;price_to=79010"),
    ("stoly/", "attr[51][]=Без полки"),
    ("podtovarniki-i-podstavki/", "price_from=4313;price_to=500000"),
    ("podtovarniki-i-podstavki/", "attr[51][]=600х400х300;price_from=4313;price_to=500000"),
    ("moechnye-vanny/", "price_from=5553;price_to=500000"),
    ("moechnye-vanny/", "attr[shell-size][]=600х600х400"),
    ("moechnye-vanny/", "attr[shell-size][]=600х600х400;price_from=5553;price_to=500000"),
    ("telezhki-servirovochnye/", "price_from=12416;price_to=500000"),
    ("zonty-vytyazhnye/", "attr[construction][]=угловая, купольная"),
    ("zonty-vytyazhnye/", "price_from=19607;price_to=500000"),
]
for path, fs in tests:
    fs, n = probe(path, fs)
    print(f"{path:35} {n:3}  {fs}")
