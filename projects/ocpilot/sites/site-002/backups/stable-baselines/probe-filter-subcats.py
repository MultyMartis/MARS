#!/usr/bin/env python3
import re, ssl, urllib.request, json

BASE = 'https://zpm.new-site.space'
paths = [
    '/katalog/nejtralnoe-oborudovanie/stoly/',
    '/katalog/nejtralnoe-oborudovanie/moechnye-vanny/',
    '/',
]

ctx = ssl.create_default_context()
for path in paths:
    html = urllib.request.urlopen(urllib.request.Request(BASE+path, headers={'User-Agent':'probe'}), context=ctx, timeout=60).read().decode('utf-8','replace')
    subcats = re.findall(r'flt__check-text">([^<]+)</span>', html)
    chips = re.findall(r'zpm-sub-cat-chip__text">\s*([^<]+?)\s*</span>', html)
    home_cards = re.findall(r'zpm-cat-card__title">([^<]+)</div>', html)
    print('PATH', path)
    print('  filter_subcats', len(subcats), subcats[:15])
    print('  chips', len(chips), chips[:10])
    print('  home/hub cards', home_cards[:10])
