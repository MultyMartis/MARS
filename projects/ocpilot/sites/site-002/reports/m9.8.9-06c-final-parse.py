#!/usr/bin/env python3
import json, re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape
from pathlib import Path

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06c-audit-data")


def pma_session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPSHandler(context=ctx),
    )
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(
        urllib.request.Request(
            PMA + "/index.php",
            data=urllib.parse.urlencode(
                {
                    "pma_username": DB_USER,
                    "pma_password": DB_PASS,
                    "server": "1",
                    "target": "index.php",
                    "token": token,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    db_html = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode(
        "utf-8", "replace"
    )
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)
    return op, csrf


def run_sql(op, csrf, sql):
    return op.open(
        urllib.request.Request(
            PMA + "/sql.php",
            data=urllib.parse.urlencode(
                {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
            ).encode(),
            method="POST",
        ),
        timeout=300,
    ).read().decode("utf-8", "replace")


def parse_grid(html):
    """PMA 5.x grid: find thead th texts then tbody tr td texts."""
    grids = []
    for table_html in re.findall(r"<table[^>]*>(.*?)</table>", html, re.S):
        if "column_name" in table_html or "Browse" in table_html[:200]:
            continue
        headers = [
            unescape(re.sub(r"<[^>]+>", "", h).strip())
            for h in re.findall(r"<th[^>]*>(.*?)</th>", table_html, re.S)
        ]
        headers = [re.sub(r"\s+", " ", h) for h in headers if h.strip()]
        if not headers:
            continue
        body_rows = []
        tbody = re.search(r"<tbody[^>]*>(.*?)</tbody>", table_html, re.S)
        src = tbody.group(1) if tbody else table_html
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", src, re.S):
            cells = [
                unescape(re.sub(r"<[^>]+>", " ", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)
            ]
            cells = [re.sub(r"\s+", " ", c) for c in cells]
            if len(cells) == len(headers):
                body_rows.append(dict(zip([h.lower() for h in headers], cells)))
        if body_rows:
            grids.append({"headers": headers, "rows": body_rows})
    return grids


def main():
    op, csrf = pma_session()

    cron_html = run_sql(op, csrf, "SELECT * FROM cron ORDER BY id")
    OUT_DIR.joinpath("cron_raw.html").write_text(cron_html[:200000], encoding="utf-8")
    cron_grids = parse_grid(cron_html)

    cols_html = run_sql(op, csrf, "SHOW FULL COLUMNS FROM cron")
    cols_grids = parse_grid(cols_html)

    variant = []
    for offset in range(0, 450, 50):
        sql = f"""
        SELECT p.product_id, p.model, p.sku, pd.name, p.price,
               IF(ppi.product_id IS NULL, 'no', 'yes') AS has_price_index_group_2
        FROM oc_product p
        INNER JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
        INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
        INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
        INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
        LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
        WHERE p.status = 1 AND p.date_available <= NOW()
        ORDER BY p.product_id
        LIMIT {offset}, 50
        """
        html = run_sql(op, csrf, sql)
        grids = parse_grid(html)
        for g in grids:
            variant.extend(g["rows"])

    out = {
        "cron_columns": cols_grids,
        "cron_rows": cron_grids,
        "variant_c_301": variant,
        "variant_c_count": len(variant),
        "html_snippets": {
            "cron_has_import0": "import0_1" in cron_html.lower(),
            "cron_has_offers0": "offers0_1" in cron_html.lower(),
            "cron_has_1c": "1c" in cron_html.lower(),
        },
    }
    OUT_DIR.joinpath("final-audit-payload.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("cron_grids", len(cron_grids), "rows", sum(len(g["rows"]) for g in cron_grids))
    print("cols_grids", sum(len(g["rows"]) for g in cols_grids))
    print("variant_c", len(variant))


if __name__ == "__main__":
    main()
