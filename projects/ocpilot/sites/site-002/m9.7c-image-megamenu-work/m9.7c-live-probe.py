#!/usr/bin/env python3
"""Quick live TEST probe for M9.7C."""
import re
import urllib.request

BASE = "https://zpm.new-site.space"


def fetch(path):
    url = BASE + path
    req = urllib.request.Request(url, headers={"User-Agent": "M9.7C-probe"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")


def neutral_megamenu(html):
    m = re.search(
        r'data-cat-pane="Нейтральное оборудование".*?zpm-catalog__grid(.*?)zpm-catalog__last-block',
        html,
        re.S,
    )
    if not m:
        return []
    block = m.group(1)
    items = []
    for tile in re.findall(r'<a class="zpm-catalog__tile".*?</a>', block, re.S):
        title_m = re.search(r'zpm-catalog__tile-title">([^<]+)</span>', tile)
        count_m = re.search(r'<span>(\d+) шт\.</span>', tile)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', tile)
        if title_m:
            items.append(
                {
                    "name": title_m.group(1).strip(),
                    "count": int(count_m.group(1)) if count_m else None,
                    "img": img_m.group(1) if img_m else None,
                }
            )
    return items


def hub_cards(html):
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', html, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', card)
        if title_m:
            cards.append({"name": title_m.group(1).strip(), "img": img_m.group(1) if img_m else None})
    return cards


def php_warnings(html):
    return bool(re.search(r"(Notice:|Warning:|Fatal error:)", html))


def main():
    home = fetch("/")
    hub = fetch("/katalog/nejtralnoe-oborudovanie")
    print("=== MEGAMENU NEUTRAL (before fix baseline) ===")
    for item in neutral_megamenu(home):
        print(f"{item['name']}: count={item['count']} img={item['img']}")
    print("=== HUB CARDS ===")
    for card in hub_cards(hub):
        print(f"{card['name']}: img={card['img']}")
    print("PHP warnings home:", php_warnings(home))
    print("PHP warnings hub:", php_warnings(hub))


if __name__ == "__main__":
    main()
