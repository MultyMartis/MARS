import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
html = urllib.request.urlopen(
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/",
    context=ctx,
    timeout=20,
).read().decode("utf-8", "replace")
links = sorted(set(re.findall(r'href="(https://zpm\.new-site\.space/katalog/[^"]+)"', html)))
prod = [u for u in links if u.count("/") >= 6]
for u in prod[:5]:
    try:
        print(urllib.request.urlopen(u, context=ctx, timeout=20).status, u)
    except Exception as exc:
        print("ERR", u, exc)
