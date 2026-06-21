#!/usr/bin/env python3
"""Cross-check filter sidebar subcategories vs DB active product counts."""
import json, re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape
from pathlib import Path

BASE = 'https://zpm.new-site.space'
PMA = 'https://bruma.beget.com/phpMyAdmin'
DB = 'polygonws_zpm'
DB_USER = 'polygonws_zpm'
DB_PASS = 'VBCDry2bJ5P'
OUT = Path(r'C:\AI MARS\projects\ocpilot\sites\site-002\reports\filter-subcategory-crosscheck.json')

BRANCHES = [
    ('301', 'stoly', '/katalog/nejtralnoe-oborudovanie/stoly/'),
    ('80', 'vanny', '/katalog/nejtralnoe-oborudovanie/moechnye-vanny/'),
    ('322', 'podtovarniki', '/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/'),
    ('207', 'zonty', '/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/'),
    ('326', 'telezhki', '/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/'),
]


def pma_session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
    lp = op.open(PMA + '/', timeout=60).read().decode('utf-8', 'replace')
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(urllib.request.Request(PMA + '/index.php', data=urllib.parse.urlencode({
        'pma_username': DB_USER, 'pma_password': DB_PASS, 'server': '1', 'target': 'index.php', 'token': token,
    }).encode(), method='POST'), timeout=60)
    db_html = op.open(PMA + '/db_structure.php?db=' + urllib.parse.quote(DB), timeout=60).read().decode('utf-8', 'replace')
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)
    return op, csrf


def pma_sql(op, csrf, sql):
    html = op.open(urllib.request.Request(PMA + '/sql.php', data=urllib.parse.urlencode({
        'db': DB, 'sql_query': sql, 'token': csrf, 'sql_delimiter': ';',
    }).encode(), method='POST'), timeout=240).read().decode('utf-8', 'replace')
    rows = []
    for tbl in re.findall(r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S):
        if 'Browse' in tbl and 'Drop' in tbl:
            continue
        parsed = []
        for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', tbl, re.S):
            cells = [unescape(re.sub(r'<[^>]+>', ' ', c).strip()) for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, re.S)]
            cells = [re.sub(r'\s+', ' ', c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2:
            rows = parsed
            break
    if len(rows) < 2:
        return []
    h = [x.lower() for x in rows[0]]
    return [dict(zip(h, r)) for r in rows[1:] if len(r) == len(h)]


def val(row, *keys):
    for k in keys:
        if k in row:
            return row[k]
    for k, v in row.items():
        for want in keys:
            if want in k.lower():
                return v
    return None


def fetch_filter_subcats(path):
    ctx = ssl.create_default_context()
    html = urllib.request.urlopen(urllib.request.Request(BASE + path, headers={'User-Agent': 'x'}), context=ctx, timeout=60).read().decode('utf-8', 'replace')
    m = re.search(r'Подкатегории[\s\S]*?flt__group-body[\s\S]*?</div>\s*</div>', html)
    block = m.group(0) if m else ''
    return re.findall(r'flt__check-text">([^<]+)</span>', block)


def fetch_chips(path):
    ctx = ssl.create_default_context()
    html = urllib.request.urlopen(urllib.request.Request(BASE + path, headers={'User-Agent': 'x'}), context=ctx, timeout=60).read().decode('utf-8', 'replace')
    return re.findall(r'zpm-sub-cat-chip__text">\s*([^<]+?)\s*</span>', html)


op, csrf = pma_session()
results = []
for parent_id, key, path in BRANCHES:
    db_children = pma_sql(op, csrf, f"""
        SELECT c.category_id, cd.name,
               (SELECT COUNT(DISTINCT p.product_id)
                FROM oc_product p
                JOIN oc_product_to_category p2c ON p2c.product_id = p.product_id
                JOIN oc_category_path cp ON cp.category_id = p2c.category_id
                WHERE cp.path_id = c.category_id AND p.status = 1) AS subtree_active
        FROM oc_category c
        JOIN oc_category_description cd ON cd.category_id = c.category_id AND cd.language_id = 1
        WHERE c.parent_id = {parent_id} AND c.status = 1
        ORDER BY cd.name
    """)
    live_filter = fetch_filter_subcats(path)
    live_chips = fetch_chips(path)
    db_by_name = {val(r, 'name', 'cd.name'): int(val(r, 'subtree_active') or 0) for r in db_children}
    empty_in_db = [n for n, c in db_by_name.items() if c == 0]
    empty_in_filter = [n for n in live_filter if db_by_name.get(n.strip(), -1) == 0]
    empty_in_chips = []
    for chip in live_chips:
        base = re.sub(r'\s*\(\d+\)\s*$', '', chip).strip()
        if db_by_name.get(base, -1) == 0:
            empty_in_chips.append(chip)
    missing_from_filter = [n for n, c in db_by_name.items() if c > 0 and n not in live_filter]
    results.append({
        'branch': key,
        'parent_id': parent_id,
        'db_children_total': len(db_children),
        'db_empty_subtree': len(empty_in_db),
        'live_filter_count': len(live_filter),
        'live_chips_count': len(live_chips),
        'empty_visible_in_filter': empty_in_filter,
        'empty_visible_in_chips': empty_in_chips,
        'active_missing_from_filter': missing_from_filter[:10],
        'db_empty_names_sample': empty_in_db[:15],
    })

OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
for r in results:
    print(r['branch'], 'filter', r['live_filter_count'], 'empty_in_filter', len(r['empty_visible_in_filter']), 'empty_in_chips', len(r['empty_visible_in_chips']))
