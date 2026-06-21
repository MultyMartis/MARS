#!/usr/bin/env python3
"""Read-only probe: category cards vs PDP primary specs."""
import re
import urllib.request

CAT_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/"
    "stoly/stoly-serii-premium/stoly-premium-600/"
)


def fetch(url):
    return urllib.request.urlopen(url, timeout=30).read().decode("utf-8", "replace")


def primary_specs(html):
    block = re.search(r"product-hero__props--primary.*?</dl>", html, re.S)
    if not block:
        return []
    return re.findall(r"<dt>([^<]+)</dt>\s*<dd>([^<]+)</dd>", block.group())


def main():
    html = fetch(CAT_URL)
    hrefs = re.findall(r'class="p-card__title" href="([^"]+)"', html)
    print("category_cards", len(hrefs))
    print("card_has_specs_markup", "p-card__spec" in html or "product-hero__prop" in html)

    sample = hrefs[:5]
    coverage = []
    for href in sample:
        pdp = fetch(href)
        specs = primary_specs(pdp)
        coverage.append({"href": href, "spec_count": len(specs), "specs": specs})
        print("PDP", href.split("/")[-1], "specs", specs)

    with open(
        r"C:\AI MARS\projects\ocpilot\sites\site-002\category-v2.1-discovery-work\probe-live-specs-result.json",
        "w",
        encoding="utf-8",
    ) as f:
        import json

        json.dump(
            {
                "category_url": CAT_URL,
                "card_count": len(hrefs),
                "card_has_specs_markup": "p-card__spec" in html,
                "sample_pdps": coverage,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )


if __name__ == "__main__":
    main()
