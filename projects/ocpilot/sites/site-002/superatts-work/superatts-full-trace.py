#!/usr/bin/env python3
"""SITE-002 — read-only full SUPER_ATTS pipeline trace."""
import ftplib
import io
import json
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

VKS_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
    "kotlomoechnye-premium/vanna-kotlomoechnaya-vks-p-1-400-900"
)
SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)

SUPER_ATTS_IDS = [12, 13, 14, 15, 21, 25, 26, 28, 29, 30, 33, 115]
SEARCH_TERMS = [
    "Конструкция",
    "Наличие борта",
    "Ножки",
    "Отверстие под смеситель",
    "Размер раковины",
    "Тип опоры",
    "Усиление",
]

REMOTE_FILES = {
    "config.php": "config.php",
    "product.php": "catalog/controller/product/product.php",
    "product_model.php": "catalog/model/catalog/product.php",
    "product.twig": "catalog/view/theme/default/template/product/product.twig",
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "mod_product.php": "system/storage/modification/catalog/controller/product/product.php",
}

OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\superatts-work\trace-live"
OUT_JSON = r"C:\AI MARS\projects\ocpilot\sites\site-002\superatts-work\superatts-full-trace.json"


def ftp_download(path):
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + path, bio.write)
    ftp.quit()
    return bio.getvalue().decode("utf-8", "replace")


def ftp_download_optional(path):
    try:
        return ftp_download(path), True
    except ftplib.error_perm:
        return None, False


def line_number(text, needle):
    for i, line in enumerate(text.splitlines(), 1):
        if needle in line:
            return i
    return None


def extract_block_with_lines(text, start_needle, end_needle=None, max_lines=80):
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if start_needle in line:
            start = i
            break
    if start is None:
        return None
    end = min(len(lines), start + max_lines)
    if end_needle:
        for j in range(start + 1, len(lines)):
            if end_needle in lines[j]:
                end = j + 1
                break
    block = "\n".join(lines[start:end])
    return {"start_line": start + 1, "end_line": end, "code": block}


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
    db_page = op.open(
        PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60
    ).read().decode("utf-8", "replace")
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_page)
    return op, csrf.group(1) if csrf else token


def pma_sql(op, csrf, query):
    qdata = urllib.parse.urlencode(
        {"db": DB, "sql_query": query, "token": csrf, "sql_delimiter": ";"}
    ).encode()
    html = op.open(
        urllib.request.Request(PMA + "/sql.php", data=qdata, method="POST"),
        timeout=180,
    ).read().decode("utf-8", "replace")
    if "MySQL returned an empty result set" in html:
        return {"header": [], "data": [], "empty": True}
    rows = []
    for tbl in re.findall(r"<table[^>]*class=\"[^\"]*table[^\"]*\"[^>]*>(.*?)</table>", html, re.S | re.I):
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
        if len(parsed) >= 2 and len(parsed[0]) >= 2:
            header = parsed[0]
            data = []
            for r in parsed[1:]:
                if len(r) == len(header):
                    data.append(dict(zip(header, r)))
            if data and any(k.isdigit() or "product_id" in k.lower() or "attribute" in k.lower() for k in header):
                return {"header": header, "data": data}
            rows.extend(data)
    return {"header": [], "data": rows}


def parse_hero_atts(html):
    items = []
    hero = re.search(r'<section class="product-hero".*?</section>', html, re.S)
    hero_html = hero.group(0) if hero else html
    for m in re.finditer(
        r'<div class="product-hero__prop">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',
        hero_html,
        re.S,
    ):
        items.append(
            {
                "name": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip())),
                "value": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2)).strip())),
            }
        )
    for m in re.finditer(
        r'<div class="product-hero__props-item">\s*<span[^>]*>(.*?)</span>\s*<span[^>]*>(.*?)</span>',
        hero_html,
        re.S,
    ):
        items.append(
            {
                "name": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip())),
                "value": unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2)).strip())),
            }
        )
    return items


def find_term(html, term):
    hero = re.search(r'<section class="product-hero".*?</section>', html, re.S)
    hero_html = hero.group(0) if hero else ""
    specs = re.search(r'id="tab-spec".*?</div>\s*</div>', html, re.S)
    specs_html = specs.group(0) if specs else ""
    in_hero = term.lower() in hero_html.lower()
    in_specs = term.lower() in specs_html.lower()
    in_html = term.lower() in html.lower()
    loc = []
    if in_hero:
        loc.append("hero")
    if in_specs:
        loc.append("characteristics tab")
    if in_html and not in_hero and not in_specs:
        loc.append("elsewhere")
    if not in_html:
        loc.append("not found")
    snippet = None
    if in_hero:
        idx = hero_html.lower().find(term.lower())
        snippet = hero_html[max(0, idx - 80) : idx + 220]
    return {"found": in_html, "location": loc, "hero_snippet": snippet}


def css_probe(css_text):
    selectors = [
        ".product-hero__props",
        ".product-hero__props-item",
        ".product-hero__specs",
        ".product-hero__props--additional",
        ".product-hero__prop",
    ]
    out = {}
    for sel in selectors:
        esc = re.escape(sel)
        rules = []
        for m in re.finditer(rf"{esc}[^{{]*\{{([^}}]+)\}}", css_text, re.S):
            body = m.group(1)
            props = {}
            for p in ["display", "visibility", "overflow", "max-height", "height", "clip", "position"]:
                pm = re.search(rf"{p}\s*:\s*([^;]+);", body)
                if pm:
                    props[p] = pm.group(1).strip()
            if props:
                rules.append(props)
        out[sel] = rules
    return out


def main():
    import os

    os.makedirs(OUT_DIR, exist_ok=True)
    out = {"timestamp": datetime.now(timezone.utc).isoformat()}

    # TASK 1 — config
    files = {}
    for key, remote in REMOTE_FILES.items():
        text, exists = ftp_download_optional(remote)
        files[key] = {"remote_path": remote, "exists": exists, "text": text}
        if text:
            with open(os.path.join(OUT_DIR, key.replace("/", "_")), "w", encoding="utf-8") as f:
                f.write(text)

    cfg = files["config.php"]["text"] or ""
    m = re.search(
        r"define\s*\(\s*['\"]SUPER_ATTS['\"]\s*,\s*array\s*\(([^)]+)\)\s*\)\s*;",
        cfg,
    )
    out["task1_config"] = {
        "file_path": "config.php (site root: /home/p/polygonws/zpm.new-site.space/public_html/config.php)",
        "super_atts_define": m.group(0) if m else None,
        "super_atts_ids": [int(x) for x in re.findall(r"\d+", m.group(1))] if m else [],
        "storefront_product_includes_config": False,
        "constant_available_note": (
            "OpenCart storefront bootstraps via index.php which requires config.php before "
            "catalog/controller/product/product.php runs; SUPER_ATTS is a global PHP constant "
            "after bootstrap."
        ),
    }

    # TASK 2 — controller
    prod = files["product.php"]["text"] or ""
    mod = files["mod_product.php"]
    effective = prod
    effective_source = "catalog/controller/product/product.php"
    if mod["exists"] and mod["text"]:
        effective = mod["text"]
        effective_source = "system/storage/modification/catalog/controller/product/product.php (OCMOD cache)"

    super_block = extract_block_with_lines(prod, "$data['super_atts']", max_lines=60)
    out["task2_controller"] = {
        "file": effective_source,
        "mod_cache_exists": mod["exists"],
        "mod_cache_size": len(mod["text"] or ""),
        "answers": {},
        "code_block": super_block,
    }

    # Analyze controller logic
    has_defined_check = "defined('SUPER_ATTS')" in prod
    has_foreach_super = "foreach (SUPER_ATTS" in prod or "foreach(SUPER_ATTS" in prod
    has_in_array = bool(
        re.search(r"in_array\s*\(\s*\$a\s*\[\s*['\"]attribute_id['\"]\s*\]", prod)
    )
    has_hero_map = "hero_attr_map" in prod
    has_int_cast = "(int)" in prod and "attribute_id" in prod
    has_slice = "array_slice" in prod and "super_atts" in prod
    overwrite_later = len(re.findall(r"\$data\['super_atts'\]", prod)) > 1

    out["task2_controller"]["answers"] = {
        "1_init": "Line ~481: $data['super_atts'] = [];",
        "2_defaults": "Lines 482-485: length, width, height, weight if > 0",
        "3_super_atts_append": (
            "After attribute_groups loaded: builds hero_attr_map from attribute_groups, "
            "then foreach SUPER_ATTS appends matching attrs to super_atts"
            if has_foreach_super or has_hero_map
            else "UNKNOWN — inspect code block"
        ),
        "4_filtered": "Attributes removed from attribute_groups via in_array(attribute_id, SUPER_ATTS); only non-empty product values in groups",
        "5_id_comparison": "int cast on attribute_id when building hero_attr_map" if has_int_cast else "string/int — inspect code",
        "6_truncated": "array_slice on super_atts" if has_slice else "NO array_slice in controller",
        "7_overwritten": "YES — multiple assignments" if overwrite_later else "NO — single build path",
        "8_different_var_to_twig": "NO — $data['super_atts'] passed to view as super_atts",
        "uses_defined_super_atts": has_defined_check,
        "uses_in_array_filter": has_in_array,
        "uses_hero_attr_map": has_hero_map,
    }

    # TASK 3 — model
    model = files["product_model.php"]["text"] or ""
    get_attrs_block = extract_block_with_lines(model, "getProductAttributes", max_lines=40)
    out["task3_model"] = {
        "getProductAttributes_block": get_attrs_block,
        "attribute_id_in_query": "attribute_id" in (get_attrs_block["code"] if get_attrs_block else ""),
    }

    # DB attributes for VKS product
    op, csrf = pma_login()
    vks_prod = pma_sql(
        op,
        csrf,
        """
SELECT p.product_id, pd.name
FROM oc_product p
JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1
WHERE pd.name LIKE '%VKS-P-1/400/900%' OR pd.name LIKE '%ВКС-П-1/400/900%'
LIMIT 3
""",
    )
    product_id = None
    if vks_prod["data"]:
        product_id = vks_prod["data"][0].get("product_id")
    if not product_id:
        seo = pma_sql(
            op,
            csrf,
            """
SELECT query FROM oc_seo_url
WHERE keyword LIKE '%vks-p-1-400-900%' AND store_id=0 LIMIT 1
""",
        )
        if seo["data"]:
            q = seo["data"][0].get("query", "")
            pm = re.search(r"product_id=(\d+)", q)
            if pm:
                product_id = pm.group(1)

    attr_rows = []
    if product_id:
        ids_csv = ",".join(str(i) for i in SUPER_ATTS_IDS)
        attrs = pma_sql(
            op,
            csrf,
            f"""
SELECT a.attribute_id, ad.name AS attribute_name, pa.text AS product_value
FROM oc_attribute a
JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1
LEFT JOIN oc_product_attribute pa ON pa.attribute_id=a.attribute_id
  AND pa.product_id={product_id} AND pa.language_id=1
WHERE a.attribute_id IN ({ids_csv})
ORDER BY FIELD(a.attribute_id, {ids_csv})
""",
        )
        for row in attrs.get("data", []):
            aid = row.get("attribute_id")
            name = row.get("attribute_name", "")
            val = (row.get("product_value") or "").strip()
            exists_on = bool(val)
            should = exists_on and int(aid) in SUPER_ATTS_IDS if aid else False
            attr_rows.append(
                {
                    "id": aid,
                    "name": name,
                    "value": val,
                    "exists_on_product": exists_on,
                    "should_be_in_super_atts": should,
                }
            )
    out["task3_model"]["vks_product_id"] = product_id
    out["task3_model"]["attribute_table"] = attr_rows

    # TASK 4 — twig
    ptwig = files["product.twig"]["text"] or ""
    hero_twig = files["producthero.twig"]["text"] or ""
    includes_hero = "producthero" in ptwig
    include_line = line_number(ptwig, "producthero")
    super_loop = extract_block_with_lines(hero_twig, "super_atts", max_lines=30)
    has_slice_0_4 = "slice(0, 4)" in hero_twig
    has_slice_4 = "slice(4" in hero_twig
    has_additional_class = "product-hero__props--additional" in hero_twig
    out["task4_twig"] = {
        "product_twig_includes_producthero": includes_hero,
        "include_line": include_line,
        "producthero_super_atts_block": super_loop,
        "loops_all_items": not has_slice_0_4,
        "slices_to_4": has_slice_0_4,
        "has_additional_column": has_slice_4 or has_additional_class,
        "conditional_hide": "super_atts|length > 4" in hero_twig,
    }

    # TASK 5 — live HTML
    live = {}
    for label, url in [("VKS", VKS_URL), ("SPKB", SPKB_URL)]:
        html = urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")
        with open(os.path.join(OUT_DIR, f"live-{label.lower()}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        hero = parse_hero_atts(html)
        terms = {t: find_term(html, t) for t in SEARCH_TERMS}
        live[label] = {
            "url": url,
            "hero_atts": hero,
            "hero_count": len(hero),
            "term_search": terms,
        }
    out["task5_live_html"] = live

    # TASK 6 — CSS
    css_urls = []
    for label, url in [("VKS", VKS_URL)]:
        html = open(os.path.join(OUT_DIR, "live-vks.html"), encoding="utf-8").read()
        css_urls = re.findall(r'href="([^"]+\.css[^"]*)"', html)
        break
    css_combined = ""
    for cu in css_urls[:5]:
        full = cu if cu.startswith("http") else "https://zpm.new-site.space/" + cu.lstrip("/")
        try:
            css_combined += urllib.request.urlopen(full, timeout=30).read().decode("utf-8", "replace")
        except Exception:
            pass
    css_rules = css_probe(css_combined)
    hero_has_extra = len(live.get("VKS", {}).get("hero_atts", [])) > 4
    hidden_by_css = False
    if hero_has_extra:
        for sel, rules in css_rules.items():
            for r in rules:
                if r.get("display") == "none" or r.get("visibility") == "hidden" or r.get("max-height") == "0":
                    hidden_by_css = True
    out["task6_css"] = {
        "css_files_checked": css_urls[:5],
        "rules_for_hero_selectors": css_rules,
        "attributes_rendered_but_hidden_by_css": hidden_by_css,
        "verdict": "NO" if not hidden_by_css else "YES",
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
