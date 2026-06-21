import re
import ssl
import urllib.request
from pathlib import Path

url = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
ctx = ssl.create_default_context()
html = urllib.request.urlopen(
    urllib.request.Request(url, headers={"User-Agent": "qa"}),
    context=ctx,
    timeout=60,
).read().decode("utf-8", "replace")

out = []
for m in re.finditer(r".{0,80}Подкатегории.{0,80}", html):
    out.append(m.group(0).replace("\n", " "))

# filter sidebar marker
idx = html.find("data-filter-sidebar")
if idx >= 0:
    chunk = html[idx : idx + 12000]
    out.append("--- sidebar chunk ---")
    out.append("s[] in sidebar: " + str('name="s[]"' in chunk))
    out.append("Подкатегории in sidebar: " + str("Подкатегории" in chunk))
    titles = re.findall(r"flt__group-title[^>]*>([^<]+)", chunk)
    out.append("sidebar titles: " + " | ".join(titles))

Path(__file__).with_name("probe-out.txt").write_text("\n".join(out), encoding="utf-8")
