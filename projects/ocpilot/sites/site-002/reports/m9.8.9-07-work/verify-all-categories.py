import re
import ssl
import urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space"
CATS = {
    "stoly": "/katalog/nejtralnoe-oborudovanie/stoly/",
    "moechnye": "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    "podtovarniki": "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    "telezhki": "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
    "zonty": "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
}
ctx = ssl.create_default_context()
lines = []
for name, path in CATS.items():
    html = urllib.request.urlopen(
        urllib.request.Request(BASE + path, headers={"User-Agent": "qa"}),
        context=ctx,
        timeout=60,
    ).read().decode("utf-8", "replace")
    idx = html.find("data-filter-sidebar")
    chunk = html[idx : idx + 15000] if idx >= 0 else ""
    titles = re.findall(r"flt__group-title[^>]*>([^<]+)", chunk)
    lines.append(
        f"{name}: sidebar_s[]={('name=\"s[]\"' in chunk)} "
        f"sidebar_subcat_title={('Подкатегории' in titles)} "
        f"groups={len(titles)} titles={titles[:6]}"
    )

Path(__file__).with_name("qa-sidebar-verify.txt").write_text("\n".join(lines), encoding="utf-8")
