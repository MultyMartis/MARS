#!/usr/bin/env python3
import re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape

PMA='https://bruma.beget.com/phpMyAdmin'; DB='polygonws_zpm'; DU='polygonws_zpm'; DP='VBCDry2bJ5P'
IDS=[12,13,14,15,21,25,26,28,29,30,33,115]
TABLE='https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850'

def pma(q):
    ctx=ssl.create_default_context(); cj=http.cookiejar.CookieJar()
    op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPSHandler(context=ctx))
    lp=op.open(PMA+'/',timeout=60).read().decode('utf-8','replace')
    token=re.search(r'name="token"\s+value="([^"]+)"',lp).group(1)
    op.open(urllib.request.Request(PMA+'/index.php',data=urllib.parse.urlencode({'pma_username':DU,'pma_password':DP,'server':'1','target':'index.php','token':token}).encode(),method='POST'),timeout=60)
    return op.open(urllib.request.Request(PMA+'/sql.php',data=urllib.parse.urlencode({'db':DB,'sql_query':q,'token':token,'sql_delimiter':';'}).encode(),method='POST'),timeout=180).read().decode('utf-8','replace')

def rows(html):
    out=[]
    for m in re.finditer(r'<td[^>]*>(\d+)</td>\s*<td[^>]*>([^<]+)</td>', html):
        out.append((m.group(1), unescape(m.group(2).strip())))
    return out

def hero(html):
    b=re.search(r'<dl class="product-hero__props">(.*?)</dl>', html, re.S)
    if not b: return []
    r=[]
    for m in re.finditer(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', b.group(1), re.S):
        r.append((unescape(re.sub(r'\s+',' ',m.group(1).strip())), unescape(re.sub(r'\s+',' ',m.group(2).strip()))))
    return r

# attribute id names
html=pma('SELECT a.attribute_id, ad.name FROM oc_attribute a JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1 WHERE a.attribute_id IN ('+','.join(map(str,IDS))+') ORDER BY a.attribute_id')
idmap={int(a):n for a,n in rows(html)}
print('ID NAMES', idmap)

# find bath
for q in [
    "SELECT p.product_id,pd.name FROM oc_product p JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1 WHERE pd.name LIKE '%ВМЦ%' AND p.status=1 LIMIT 15",
    "SELECT p.product_id,pd.name FROM oc_product p JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1 WHERE pd.name LIKE '%моечн%ванн%' AND p.status=1 LIMIT 15",
    "SELECT p.product_id,pd.name FROM oc_product p JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1 WHERE pd.name LIKE '%500%' AND pd.name LIKE '%П3%' AND p.status=1 LIMIT 15",
]:
    html=pma(q)
    prods=rows(html)
    if prods:
        print('PRODS', q[:60], prods[:5])
        break

# table product id
html=pma("SELECT p.product_id,pd.name FROM oc_product p JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1 WHERE pd.name LIKE '%SP-P-18-6%' AND p.status=1 LIMIT 1")
table_pid=rows(html)[0][0] if rows(html) else None
print('TABLE PID', table_pid)

def report(pid, url, label):
    ids=','.join(map(str,IDS))
    html=pma(f"""SELECT a.attribute_id, IFNULL(pa.text,'') val FROM oc_attribute a
LEFT JOIN oc_product_attribute pa ON pa.attribute_id=a.attribute_id AND pa.product_id={pid} AND pa.language_id=1
WHERE a.attribute_id IN ({ids}) ORDER BY a.attribute_id""")
    vals={int(a):v.strip() for a,v in re.findall(r'<td[^>]*>(\d+)</td>\s*<td[^>]*>([^<]*)</td>', html)}
    page=urllib.request.urlopen(url,timeout=60).read().decode('utf-8','replace')
    h=hero(page)
    print(f'\n{label} {url}')
    print('HERO', h)
    for i in IDS:
        name=idmap.get(i,'?')
        val=vals.get(i,'')
        on='YES' if val else 'NO'
        ih='YES' if any(name.lower() in x[0].lower() or x[0].lower() in name.lower() for x in h) else 'NO'
        print(f'ID={i} name={name!r} val={val!r} on_product={on} in_hero={ih}')

if table_pid:
    report(table_pid, TABLE, 'TABLE')

if prods:
    pid=prods[0][0]
    html=pma(f"SELECT keyword FROM oc_seo_url WHERE query='product_id={pid}' AND store_id=0 LIMIT 1")
    kw=re.search(r'<td[^>]*>([^<]+)</td>', html)
    if kw:
        url='https://zpm.new-site.space/'+kw.group(1).strip().lstrip('/')
        report(pid, url, 'BATH')
