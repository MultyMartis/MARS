#!/usr/bin/env python3
"""Supplement M9.7D checkpoint: assets CSS + filter subcategory audit."""
import ftplib, hashlib, io, json, re, ssl, urllib.request
from pathlib import Path

BASE = 'https://zpm.new-site.space'
HOST = 'polygonws.beget.tech'
FTP_USER = 'polygonws_zpm'
FTP_PASS = 'RT4uK7VKr&c'
BACKUP = Path(r'C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baselines\SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI')
M9 = Path(r'C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baselines\SITE-002-STABLE-M9-COMPLETE-20260615\files')

CSS_REMOTE = [
    'assets/css/style.css',
    'assets/css/style.min.css',
    'assets/css/sd.css',
]

BRANCHES = [
    ('stoly', '/katalog/nejtralnoe-oborudovanie/stoly/'),
    ('vanny', '/katalog/nejtralnoe-oborudovanie/moechnye-vanny/'),
    ('podtovarniki', '/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/'),
    ('zonty', '/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/'),
    ('telezhki', '/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/'),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fetch(path):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(BASE + path, headers={'User-Agent': 'M9.7D-supplement'})
    with urllib.request.urlopen(req, context=ctx, timeout=90) as r:
        return r.read().decode('utf-8', 'replace')


def extract_filter_subcats(html):
    m = re.search(r'data-filter-sidebar[\s\S]*?</aside>', html)
    block = m.group(0) if m else html
    items = []
    for label in re.findall(r'filter-subcat[^>]*>[\s\S]*?<span[^>]*>([^<]+)</span>', block):
        items.append(label.strip())
    # fallback checkbox labels
    if not items:
        for label in re.findall(r'class="flt__subcat[^"]*"[^>]*>[\s\S]*?>([^<]+)<', block):
            items.append(re.sub(r'\s+', ' ', label).strip())
    return items


def extract_category_grid_subcats(html):
    return re.findall(r'class="category-card[^"]*"[\s\S]*?<a[^>]+href="([^"]+)"[\s\S]*?>([^<]+)<', html)


ftp = ftplib.FTP(HOST, timeout=120)
ftp.login(FTP_USER, FTP_PASS)
css_entries = []
for remote in CSS_REMOTE:
    bio = io.BytesIO()
    try:
        ftp.retrbinary('RETR ' + remote, bio.write)
        data = bio.getvalue()
        local = BACKUP / 'files' / remote.replace('/', '\\')
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(data)
        css_entries.append({'remote': remote, 'bytes': len(data), 'sha256': sha(data)})
        print('CSS captured', remote, len(data))
    except Exception as e:
        print('CSS missing', remote, e)
ftp.quit()

# hash diff vs M9
diffs = []
for rel in [
    'catalog/view/theme/default/template/common/megamenu.twig',
    'catalog/view/theme/default/template/product/category.twig',
    'catalog/view/theme/default/template/sections/offcanvasmenu.twig',
    'catalog/controller/common/header.php',
    'system/library/zpm/category_visibility.php',
    'catalog/view/theme/default/stylesheet/stylesheet.css',
]:
    new_p = BACKUP / 'files' / rel.replace('/', '\\')
    old_p = M9 / rel.replace('/', '\\')
    if new_p.exists() and old_p.exists():
        nh, oh = sha(new_p.read_bytes()), sha(old_p.read_bytes())
        if nh != oh:
            diffs.append({'file': rel, 'm9_sha256': oh[:16], 'm9.7d_sha256': nh[:16], 'changed': True})
        else:
            diffs.append({'file': rel, 'changed': False})

branch_audit = {}
for name, path in BRANCHES:
    html = fetch(path)
    branch_audit[name] = {
        'filter_subcategories': extract_filter_subcats(html),
        'category_cards': extract_category_grid_subcats(html)[:10],
        'subcat_chips': re.findall(r'zpm-sub-cat-chips[\s\S]*?<a[^>]+>([^<]+)</a>', html)[:10],
    }

out = {
    'css_captured': css_entries,
    'hash_diff_vs_m9_complete': diffs,
    'branch_subcategory_audit': branch_audit,
}
out_path = BACKUP / 'supplement-audit.json'
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in out.items()}, ensure_ascii=False))
