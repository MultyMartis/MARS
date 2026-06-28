import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
url = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-standart/"
html = urllib.request.urlopen(url, context=ctx, timeout=20).read().decode("utf-8", "replace")
patterns = [
    r'href="(https://zpm\.new-site\.space/katalog/[^"]+)"',
    r'href="(/katalog/[^"]+)"',
    r'data-product-id="(\d+)"',
]
for pat in patterns:
    found = sorted(set(re.findall(pat, html)))
    print(pat, len(found))
    for item in found[:8]:
        print(" ", item)
