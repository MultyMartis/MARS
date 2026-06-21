#!/usr/bin/env python3
import re, ssl, urllib.request

BASE = 'https://zpm.new-site.space'
ctx = ssl.create_default_context()

for path in ['/katalog/nejtralnoe-oborudovanie/stoly/', '/katalog/nejtralnoe-oborudovanie/moechnye-vanny/']:
    html = urllib.request.urlopen(urllib.request.Request(BASE+path, headers={'User-Agent':'x'}), context=ctx, timeout=60).read().decode('utf-8','replace')
    m = re.search(r'Подкатегории[\s\S]*?flt__group-body[\s\S]*?</div>\s*</div>', html)
    block = m.group(0) if m else ''
    names = re.findall(r'flt__check-text">([^<]+)</span>', block)
    print(path, 'filter subcategory names:', len(names))
    for n in names[:20]:
        print(' ', n)
