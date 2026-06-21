import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
req = urllib.request.Request(
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie",
    headers={"User-Agent": "inspect"},
)
body = urllib.request.urlopen(req, timeout=60, context=ctx).read().decode("utf-8", "replace")
for needle in ["certificates", "blockdealers", "zpm-cert", "сертифик", "Дилерам", "оптовик"]:
    idx = body.lower().find(needle.lower() if needle.isascii() else needle)
    print(needle, idx)
# snippet around certificates section if any
m = re.search(r".{0,80}сертифик.{0,80}", body, re.I)
if m:
    print("snippet:", m.group(0))
