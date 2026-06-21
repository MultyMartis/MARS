import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
urls = [
    "https://zpm.new-site.space/zonty-vytyazhnye/?filters=attr[construction][]=%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D0%B0%D1%8F",
    "https://zpm.new-site.space/zonty-vytyazhnye/?filters=attr[construction][]=%D1%81%D0%B2%D0%B0%D1%80%D0%BD%D0%B0%D1%8F%20%28%D0%BD%D0%B5%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%29",
]
for u in urls:
    req = urllib.request.Request(u, headers={"User-Agent": "probe"})
    html = urllib.request.urlopen(req, timeout=60, context=ctx).read().decode("utf-8", "replace")
    cards = len(re.findall(r'class="[^"]*product-card[^"]*"', html))
    print(cards, u)
