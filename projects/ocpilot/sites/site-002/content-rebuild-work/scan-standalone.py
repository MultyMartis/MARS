#!/usr/bin/env python3
import json
import re
import urllib.request
from urllib.parse import urljoin

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def extract_links(html, base_url):
    links = set()
    for href in re.findall(r'href="([^"]+)"', html):
        if "katalog" not in href:
            continue
        if href.startswith("/"):
            href = BASE + href
        elif not href.startswith("http"):
            href = urljoin(base_url, href)
        if "zpm.new-site.space" not in href:
            continue
        links.add(href.split("?")[0].rstrip("/"))
    return links


def main():
    queue = [BASE + "/katalog/"]
    seen = set()
    standalone = []
    scanned = 0

    while queue and scanned < 600:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            html = fetch(url)
        except Exception:
            continue
        scanned += 1

        if "product-hero" in html and 'class="product-content"' in html:
            wrapper = "product-content__specs-docs" in html
            standalone_specs = (
                "product-content__specifications" in html and not wrapper
            )
            if standalone_specs:
                standalone.append({
                    "url": url,
                    "has_desc": "product-content__description" in html,
                    "has_docs": "product-content__documents" in html,
                })

        for link in extract_links(html, url):
            if link not in seen and link.startswith(BASE + "/katalog"):
                queue.append(link)

        if len(standalone) >= 5:
            break

    out = {"scanned": scanned, "standalone": standalone}
    path = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\scan-standalone-result.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
