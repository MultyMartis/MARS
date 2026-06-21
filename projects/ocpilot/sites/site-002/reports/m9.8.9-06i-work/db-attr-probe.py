import re, urllib.parse, urllib.request, ssl, http.cookiejar
from html import unescape

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"

def pma_session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(urllib.request.Request(PMA + "/index.php", data=urllib.parse.urlencode({"pma_username": DB_USER, "pma_password": DB_PASS, "server": "1", "target": "index.php", "token": token}).encode(), method="POST"), timeout=60)
    db_html = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode("utf-8", "replace")
    return op, re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)

def pma_sql(op, csrf, sql):
    html = op.open(urllib.request.Request(PMA + "/sql.php", data=urllib.parse.urlencode({"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}).encode(), method="POST"), timeout=120).read().decode("utf-8", "replace")
    for tbl in re.findall(r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S):
        parsed = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S):
            cells = [unescape(re.sub(r"<[^>]+>", " ", c).strip()) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells: parsed.append(cells)
        if len(parsed) >= 2:
            h = [x.lower() for x in parsed[0]]
            return [dict(zip(h, r)) for r in parsed[1:] if len(r)==len(h)]
    return []

op, csrf = pma_session()
for sql in [
    "SELECT attribute_id, name, filter_name, IF(filter_name IS NULL OR filter_name='', 'EMPTY', 'SET') AS fn_state FROM oc_attribute_description WHERE attribute_id IN (47,51) AND language_id=1",
    "SELECT pa.text, COUNT(*) cnt FROM oc_product_attribute pa INNER JOIN oc_product_to_category p2c ON pa.product_id=p2c.product_id INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id=322 WHERE pa.attribute_id=51 GROUP BY pa.text LIMIT 10",
]:
    print('SQL:', sql[:80])
    print(pma_sql(op, csrf, sql))
    print()
