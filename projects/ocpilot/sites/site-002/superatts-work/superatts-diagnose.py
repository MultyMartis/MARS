#!/usr/bin/env python3
"""SITE-002 SUPER_ATTS diagnostic — read-only FTP + DB + live PDP probe."""
import ftplib
import io
import json
import os
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from html import unescape
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DU = "polygonws_zpm"
DP = "VBCDry2bJ5P"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups")
OUT = os.path.join(BASE, "superatts-work", "superatts-diagnose.json")

REMOTE = {
    "config.php": "config.php",
    "admin_config.php": "admin/config.php",
    "product.php": "catalog/controller/product/product.php",
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "producttabs.twig": "catalog/view/theme/default/template/product/producttabs.twig",
}

BACKUP_NAMES = {
    "config.php": "config.php.pre-superatts-fix.bak",
    "product.php": "product.php.pre-superatts-fix.bak",
    "producthero.twig": "producthero.twig.pre-superatts-fix.bak",
    "producttabs.twig": "producttabs.twig.pre-superatts-fix.bak",
}

SUPER_ATTS_IDS = [12, 13, 14, 15, 21, 25, 26, 28, 29, 30, 33, 115]
EXPECTED_DEFINE = "define('SUPER_ATTS', array(12,13,14,15,21,25,26,28,29,30,33,115))"

BATH_SEARCH = "ВМЦ-П3-2/500"
TABLE_PDP = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path):
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def pma_login():
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
                    "pma_username": DU,
                    "pma_password": DP,
                    "server": "1",
                    "target": "index.php",
                    "token": token,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    db_page = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode(
        "utf-8", "replace"
    )
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_page)
    return op, csrf.group(1) if csrf else token


def pma_sql(op, csrf, query):
    qdata = urllib.parse.urlencode(
        {"db": DB, "sql_query": query, "token": csrf, "sql_delimiter": ";"}
    ).encode()
    html = op.open(
        urllib.request.Request(PMA + "/sql.php", data=qdata, method="POST"), timeout=180
    ).read().decode("utf-8", "replace")
    return parse_pma_table(html)


def parse_pma_table(html):
    rows = []
    for tbl in re.findall(r"<table[^>]*>(.*?)</table>", html, re.S | re.I):
        trs = re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S | re.I)
        if len(trs) < 2:
            continue
        parsed = []
        for tr in trs:
            cells = [
                unescape(re.sub(r"<[^>]+>", " ", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S | re.I)
            ]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2:
            header = [h.lower() for h in parsed[0]]
            data = []
            for r in parsed[1:]:
                if len(r) == len(header):
                    data.append(dict(zip(header, r)))
            if data:
                return {"header": parsed[0], "data": data}
    return {"header": [], "data": []}


def extract_super_atts_define(text):
    m = re.search(r"define\s*\(\s*['\"]SUPER_ATTS['\"]\s*,\s*array\s*\(([^)]+)\)", text)
    if not m:
        return None
    ids = [int(x) for x in re.findall(r"\d+", m.group(1))]
    return {"raw": m.group(0), "ids": ids}


def analyze_controller(text):
    return {
        "has_super_atts_constant_usage": "SUPER_ATTS" in text,
        "has_super_atts_array_build": "data['super_atts']" in text or '$data[\'super_atts\']' in text,
        "in_array_super_atts": bool(re.search(r"in_array\s*\(\s*\$a\s*\[\s*['\"]attribute_id['\"]\s*\]\s*,\s*SUPER_ATTS", text)),
        "dimension_rows": bool(re.search(r"Длина, мм", text)),
        "snippet": None,
    }


def analyze_twig(text):
    return {
        "uses_super_atts_loop": "super_atts" in text and "for a in super_atts" in text,
        "hardcoded_dims_only": not bool(re.search(r"for a in super_atts", text)),
        "product_hero_props": "product-hero__props" in text,
        "product_hero_props_item": "product-hero__prop" in text or "product-hero__props-item" in text,
    }


def parse_hero_atts(html):
    block = re.search(r'<dl class="product-hero__props">(.*?)</dl>', html, re.S)
    if not block:
        return []
    items = []
    for m in re.finditer(
        r'<div class="product-hero__prop">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',
        block.group(1),
        re.S,
    ):
        items.append({"name": unescape(re.sub(r"\s+", " ", m.group(1).strip())), "value": unescape(re.sub(r"\s+", " ", m.group(2).strip()))})
    return items


def parse_full_specs(html):
    names = set()
    for m in re.finditer(r'<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>', html, re.S):
        name = unescape(re.sub(r"<[^>]+>", "", m.group(1)).strip())
        val = unescape(re.sub(r"<[^>]+>", "", m.group(2)).strip())
        if name and val:
            names.add(name.lower())
    return names


def check_modification_cache():
    cleared = []
    try:
        ftp = ftp_connect()
        mod_path = "system/storage/modification/catalog/controller/product/product.php"
        try:
            data = io.BytesIO()
            ftp.retrbinary("RETR " + mod_path, data.write)
            cleared.append({"path": mod_path, "exists": True, "size": len(data.getvalue())})
        except ftplib.error_perm:
            cleared.append({"path": mod_path, "exists": False})
        ftp.quit()
    except Exception as e:
        cleared.append({"error": str(e)})
    return cleared


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out = {"timestamp": datetime.now(timezone.utc).isoformat(), "backups": {}}

    # Task 1 + backup
    for key, remote in REMOTE.items():
        if key == "admin_config.php":
            continue
        try:
            raw = ftp_download(remote)
            text = raw.decode("utf-8", "replace")
            if key in BACKUP_NAMES:
                bak_path = os.path.join(BACKUP_DIR, BACKUP_NAMES[key])
                with open(bak_path, "wb") as f:
                    f.write(raw)
                out["backups"][key] = bak_path
            out[f"remote_{key}"] = {"size": len(raw), "text_preview": text[:500]}
        except Exception as e:
            out[f"remote_{key}"] = {"error": str(e)}

    # admin config reference only
    try:
        admin_raw = ftp_download(REMOTE["admin_config.php"])
        out["admin_config_super_atts"] = extract_super_atts_define(admin_raw.decode("utf-8", "replace"))
    except Exception as e:
        out["admin_config_super_atts"] = {"error": str(e)}

    cfg_text = ftp_download(REMOTE["config.php"]).decode("utf-8", "replace")
    out["config_super_atts"] = extract_super_atts_define(cfg_text)
    out["config_has_expected"] = EXPECTED_DEFINE.replace(" ", "") in cfg_text.replace(" ", "")

    prod_text = ftp_download(REMOTE["product.php"]).decode("utf-8", "replace")
    out["controller_analysis"] = analyze_controller(prod_text)
    m = re.search(r"(\$data\['super_atts'\][\s\S]{0,800})", prod_text)
    if m:
        out["controller_analysis"]["snippet"] = m.group(1)[:800]

    hero_text = ftp_download(REMOTE["producthero.twig"]).decode("utf-8", "replace")
    out["twig_analysis"] = analyze_twig(hero_text)

    out["modification_cache"] = check_modification_cache()

    # DB: find bath product + attribute table
    op, csrf = pma_login()
    prod_q = pma_sql(
        op,
        csrf,
        f"""
SELECT p.product_id, pd.name, p.length, p.width, p.height, p.weight
FROM oc_product p
JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1
WHERE pd.name LIKE '%{BATH_SEARCH}%' AND p.status=1
LIMIT 5
""",
    )
    out["bath_products"] = prod_q

    product_id = None
    bath_url = None
    if prod_q["data"]:
        product_id = prod_q["data"][0].get("product_id")
        # resolve seo url
        seo = pma_sql(
            op,
            csrf,
            f"""
SELECT keyword FROM oc_seo_url
WHERE query='product_id={product_id}' AND store_id=0 AND language_id=1
LIMIT 1
""",
        )
        out["bath_seo"] = seo
        if seo["data"]:
            row0 = seo["data"][0]
            kw = row0.get("keyword") or row0.get("Keyword") or list(row0.values())[-1]
            if kw:
                bath_url = "https://zpm.new-site.space/" + kw.lstrip("/")
        out["bath_url"] = bath_url

    attr_table = []
    if product_id:
        ids_csv = ",".join(str(i) for i in SUPER_ATTS_IDS)
        attrs = pma_sql(
            op,
            csrf,
            f"""
SELECT a.attribute_id, ad.name AS attribute_name,
  pa.text AS product_value,
  CASE WHEN pa.text IS NOT NULL AND TRIM(pa.text)!='' THEN 'YES' ELSE 'NO' END AS on_product
FROM oc_attribute a
JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1
LEFT JOIN oc_product_attribute pa ON pa.attribute_id=a.attribute_id
  AND pa.product_id={product_id} AND pa.language_id=1
WHERE a.attribute_id IN ({ids_csv})
ORDER BY FIELD(a.attribute_id, {ids_csv})
""",
        )
        out["attribute_query"] = attrs

        all_prod_attrs = pma_sql(
            op,
            csrf,
            f"""
SELECT a.attribute_id, ad.name, pa.text
FROM oc_product_attribute pa
JOIN oc_attribute_description ad ON ad.attribute_id=pa.attribute_id AND ad.language_id=1
WHERE pa.product_id={product_id} AND pa.language_id=1 AND TRIM(pa.text)!=''
ORDER BY ad.name
""",
        )
        out["all_product_attrs_count"] = len(all_prod_attrs.get("data", []))

    # Live PDP probes
    for label, url in [("bath", bath_url), ("table", TABLE_PDP)]:
        if not url:
            continue
        try:
            html = urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")
            hero = parse_hero_atts(html)
            specs = parse_full_specs(html)
            out[f"live_{label}"] = {
                "url": url,
                "hero_atts": hero,
                "hero_count": len(hero),
                "has_php_error": "Fatal error" in html or "Parse error" in html,
            }
            if product_id and label == "bath" and "attribute_query" in out:
                for row in out["attribute_query"]["data"]:
                    name = row.get("attribute_name", "")
                    on_prod = row.get("on_product") == "YES"
                    in_specs = any(name.lower() in s or s in name.lower() for s in specs) if name else False
                    in_hero = any(
                        name.lower() in h["name"].lower() or h["name"].lower() in name.lower()
                        for h in hero
                    ) if name else False
                    attr_table.append(
                        {
                            "id": row.get("attribute_id"),
                            "name": name,
                            "value": row.get("product_value") or "",
                            "on_product": on_prod,
                            "in_full_specs": in_specs,
                            "in_hero": in_hero,
                        }
                    )
        except Exception as e:
            out[f"live_{label}"] = {"url": url, "error": str(e)}

    out["attribute_table"] = attr_table

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(json.dumps({k: v for k, v in out.items() if k not in ("remote_config.php", "remote_product.php")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
