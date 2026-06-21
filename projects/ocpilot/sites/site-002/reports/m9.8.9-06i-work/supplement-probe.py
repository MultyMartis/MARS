import re, urllib.parse, urllib.request, ssl

def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "06I-sup"})
    return urllib.request.urlopen(req, timeout=90, context=ctx).read().decode("utf-8", "replace")

def cards(html):
    return len(re.findall(r'<article class="p-card', html))

STOLY = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
POD = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/"

tests = [
    ("stoly", STOLY, "attr[table-top-material][]=бук толщиной 40 мм"),
    ("stoly", STOLY, "attr[max-load][]=150"),
    ("stoly", STOLY, "price_from=5405;price_to=20000"),
    ("stoly", STOLY, "price_from=5405;price_to=72630"),
    ("pod", POD, "attr[max-load][]=200"),
]
for label, base, fs in tests:
    url = base + "?filters=" + urllib.parse.quote(fs, safe="[];=")
    print(label, fs[:60], "->", cards(fetch(url)))

# extract attr key types from stoly HTML
html = fetch(STOLY)
keys = sorted(set(re.findall(r'name="attr\[([^\]]+)\]\[\]"', html)))
print("stoly attr keys:", keys)
numeric = [k for k in keys if k.isdigit()]
slug = [k for k in keys if not k.isdigit()]
print("numeric:", numeric, "slug:", slug)

html2 = fetch(POD)
keys2 = sorted(set(re.findall(r'name="attr\[([^\]]+)\]\[\]"', html2)))
print("podtovarniki attr keys:", keys2)
