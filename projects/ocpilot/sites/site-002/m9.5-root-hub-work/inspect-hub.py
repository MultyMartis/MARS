import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
req = urllib.request.Request(
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie",
    headers={"User-Agent": "inspect"},
)
body = urllib.request.urlopen(req, timeout=60, context=ctx).read().decode("utf-8", "replace")
print("category--hub", "category--hub" in body)
print("zpm-cat-card count", body.count("zpm-cat-card"))
print("cert сертификат", "сертификат" in body.lower())
print("dealer дилер", "дилер" in body.lower())
print("Наши сертификаты", "Наши сертификаты" in body)
print("Дилерам", "Дилерам" in body)
for t in re.findall(r"zpm-cat-card__title\">([^<]+)", body):
    print("title:", t)
