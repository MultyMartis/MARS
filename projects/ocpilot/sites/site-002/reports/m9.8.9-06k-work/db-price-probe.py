import re, ssl, urllib.parse, urllib.request, http.cookiejar
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

queries = {
    "ppi_zero_special_cat301": """
SELECT COUNT(*) AS cnt FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id=301
INNER JOIN oc_product_price_index ppi ON p.product_id=ppi.product_id AND ppi.customer_group_id=2
WHERE p.status=1 AND ppi.special=0 AND ppi.price>0
""",
    "ppi_price_zero_cat301": """
SELECT COUNT(*) AS cnt FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id=301
INNER JOIN oc_product_price_index ppi ON p.product_id=ppi.product_id AND ppi.customer_group_id=2
WHERE p.status=1 AND ppi.price=0
""",
    "filter_sim_ifnull": """
SELECT COUNT(DISTINCT p.product_id) AS cnt_ifnull_logic
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id=301
INNER JOIN oc_product_price_index ppi ON p.product_id=ppi.product_id AND ppi.customer_group_id=2
WHERE p.status=1 AND IFNULL(ppi.special, ppi.price) >= 5405 AND IFNULL(ppi.special, ppi.price) <= 79010
""",
    "filter_sim_correct": """
SELECT COUNT(DISTINCT p.product_id) AS cnt_correct_logic
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id=301
INNER JOIN oc_product_price_index ppi ON p.product_id=ppi.product_id AND ppi.customer_group_id=2
WHERE p.status=1 AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) >= 5405
  AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) <= 79010
""",
    "cat80_same": """
SELECT COUNT(DISTINCT p.product_id) AS cnt_ifnull,
  SUM(CASE WHEN IFNULL(ppi.special, ppi.price) >= 5553 THEN 1 ELSE 0 END) AS pass_ifnull,
  SUM(CASE WHEN IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) >= 5553 THEN 1 ELSE 0 END) AS pass_correct
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id=80
INNER JOIN oc_product_price_index ppi ON p.product_id=ppi.product_id AND ppi.customer_group_id=2
WHERE p.status=1
""",
    "attr47_51_filter_name": """
SELECT attribute_id, name, filter_name FROM oc_attribute_description
WHERE attribute_id IN (47,51) AND language_id=1
""",
}

for k, sql in queries.items():
    print(k, pma_sql(op, csrf, sql))
