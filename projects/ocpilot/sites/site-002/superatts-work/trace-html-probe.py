#!/usr/bin/env python3
"""Fetch live HTML for VKS + SPKB and analyze hero attrs."""
import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from html import unescape

SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)
VKS_URL_GUESS = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
    "kotlomoechnye-premium/vanna-kotlomoechnaya-vks-p-1-400-900"
)

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DU = "polygonws_zpm"
DP = "VBCDry2bJ5P"

TERMS = [
    "Конструкция",
    "Наличие борта",
    "Ножки",
    "Отверстие под смеситель",
    "Размер раковины",
    "Тип опоры",
    "Усиление",
]

SUPER_ATTS_IDS = [12, 13, 14, 15, 21, 25, 26, 28, 29, 30, 33, 115]


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
        if len(parsed) >= 2 and len(parsed[0]) >= 2:
            header = parsed[0]
            data = [dict(zip(header, r)) for r in parsed[1:] if len(r) == len(header)]
            if data and not any("navigation" in str(k).lower() for k in header):
                return header, data
    return [], []


def fetch(url):
    return urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")


def parse_hero(html):
    hero = re.search(r'<section class="product-hero".*?</section>', html, re.S)
    scope = hero.group(0) if hero else html
    primary = []
    additional = []
    prim = re.search(
        r'<dl class="product-hero__props product-hero__props--primary">(.*?)</dl>',
        scope,
        re.S,
    )
    add = re.search(
        r'<dl class="product-hero__props product-hero__props--additional">(.*?)</dl>',
        scope,
        re.S,
    )
    for block, dest in [(prim, primary), (add, additional)]:
        if not block:
            continue
        for m in re.finditer(
            r'<div class="product-hero__prop">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',
            block.group(1),
            re.S,
        ):
            dest.append(
                {
                    "name": unescape(
                        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip())
                    ),
                    "value": unescape(
                        re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(2)).strip())
                    ),
                }
            )
    if not primary and not additional:
        for m in re.finditer(
            r'<dl class="product-hero__props">(.*?)</dl>', scope, re.S
        ):
            for item in re.finditer(
                r'<div class="product-hero__prop">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',
                m.group(1),
                re.S,
            ):
                primary.append(
                    {
                        "name": unescape(
                            re.sub(
                                r"\s+", " ", re.sub(r"<[^>]+>", "", item.group(1)).strip()
                            )
                        ),
                        "value": unescape(
                            re.sub(
                                r"\s+", " ", re.sub(r"<[^>]+>", "", item.group(2)).strip()
                            )
                        ),
                    }
                )
    return primary, additional


def find_term(html, term):
    hero = re.search(r'<section class="product-hero".*?</section>', html, re.S)
    hero_html = hero.group(0) if hero else ""
    specs = re.search(r'id="tab-spec".*?</div>\s*</div>', html, re.S)
    specs_html = specs.group(0) if specs else ""
    loc = []
    if term.lower() in hero_html.lower():
        loc.append("hero")
    if term.lower() in specs_html.lower():
        loc.append("characteristics tab")
    if term.lower() in html.lower() and not loc:
        loc.append("elsewhere")
    if term.lower() not in html.lower():
        loc.append("not found")
    snippet = None
    if "hero" in loc:
        idx = hero_html.lower().find(term.lower())
        snippet = hero_html[max(0, idx - 60) : idx + 240]
    return {"found_in_html": term.lower() in html.lower(), "location": loc, "hero_snippet": snippet}


def resolve_vks_url(op, csrf):
    _, rows = pma_sql(
        op,
        csrf,
        """
SELECT query, keyword FROM oc_seo_url
WHERE keyword LIKE '%vks%' OR keyword LIKE '%400-900%'
ORDER BY keyword LIMIT 20
""",
    )
    for row in rows:
        kw = row.get("keyword") or row.get("Keyword") or ""
        if "vks" in kw.lower() or "400" in kw:
            return "https://zpm.new-site.space/" + kw.lstrip("/"), row
    _, rows = pma_sql(
        op,
        csrf,
        """
SELECT p.product_id, pd.name FROM oc_product p
JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1
WHERE pd.name LIKE '%VKS-P-1%' OR pd.name LIKE '%ВКС-П-1%'
LIMIT 5
""",
    )
    if rows:
        pid = rows[0].get("product_id")
        _, seo = pma_sql(
            op,
            csrf,
            f"SELECT keyword FROM oc_seo_url WHERE query='product_id={pid}' AND store_id=0 LIMIT 1",
        )
        if seo:
            kw = seo[0].get("keyword") or list(seo[0].values())[-1]
            return "https://zpm.new-site.space/" + str(kw).lstrip("/"), rows[0]
    return None, rows


def attribute_table(op, csrf, product_id):
    ids_csv = ",".join(str(i) for i in SUPER_ATTS_IDS)
    _, rows = pma_sql(
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
    table = []
    for row in rows:
        aid = row.get("attribute_id")
        val = (row.get("product_value") or "").strip()
        table.append(
            {
                "id": aid,
                "name": row.get("attribute_name"),
                "value": val,
                "exists_on_product": bool(val),
                "should_be_in_super_atts": bool(val) and int(aid) in SUPER_ATTS_IDS,
            }
        )
    return table


def css_check(html):
    css_urls = re.findall(r'href="([^"]+\.css[^"]*)"', html)
    combined = ""
    for cu in css_urls:
        full = cu if cu.startswith("http") else "https://zpm.new-site.space/" + cu.lstrip("/")
        try:
            combined += fetch(full)
        except Exception:
            pass
    selectors = [
        ".product-hero__props--additional",
        ".product-hero__specs--split",
        ".product-hero__props",
        ".product-hero__specs",
    ]
    rules = {}
    for sel in selectors:
        esc = re.escape(sel)
        hits = []
        for m in re.finditer(rf"{esc}[^{{]*\{{([^}}]+)\}}", combined, re.S):
            body = m.group(1)
            props = {}
            for p in [
                "display",
                "visibility",
                "overflow",
                "max-height",
                "height",
                "clip",
                "position",
                "opacity",
            ]:
                pm = re.search(rf"{p}\s*:\s*([^;]+);", body)
                if pm:
                    props[p] = pm.group(1).strip()
            if props:
                hits.append(props)
        rules[sel] = hits
    return rules, css_urls


def probe_label(label, url, op=None, csrf=None):
    html = fetch(url)
    primary, additional = parse_hero(html)
    terms = {t: find_term(html, t) for t in TERMS}
    css_rules, css_urls = css_check(html)
    out = {
        "url": url,
        "http_ok": True,
        "hero_primary": primary,
        "hero_additional": additional,
        "hero_total": len(primary) + len(additional),
        "has_split_markup": "product-hero__specs--split" in html,
        "has_additional_dl": "product-hero__props--additional" in html,
        "debug_pre": bool(re.search(r'data-debug="super-atts"', html)),
        "terms": terms,
        "css_rules": css_rules,
        "css_files": css_urls[:8],
    }
    if op and csrf:
        m = re.search(r"product_id=(\d+)", html)
        if not m:
            _, seo = pma_sql(
                op,
                csrf,
                f"SELECT query FROM oc_seo_url WHERE keyword='{url.split('.space/')[-1]}' LIMIT 1",
            )
            if seo:
                m = re.search(r"product_id=(\d+)", seo[0].get("query", ""))
        if m:
            out["product_id"] = m.group(1)
            out["attribute_table"] = attribute_table(op, csrf, m.group(1))
    return out, html


def main():
    op, csrf = pma_login()
    vks_url, vks_meta = resolve_vks_url(op, csrf)

    result = {"vks_url_resolution": {"url": vks_url, "meta": vks_meta}}

    urls = []
    if vks_url:
        urls.append(("VKS", vks_url))
    else:
        urls.append(("VKS", VKS_URL_GUESS))
    urls.append(("SPKB", SPKB_URL))

    for label, url in urls:
        try:
            data, html = probe_label(label, url, op, csrf)
            result[label] = data
            path = rf"C:\AI MARS\projects\ocpilot\sites\site-002\superatts-work\trace-live\live-{label.lower()}.html"
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
        except Exception as e:
            result[label] = {"url": url, "error": str(e)}

    out_path = r"C:\AI MARS\projects\ocpilot\sites\site-002\superatts-work\trace-html-result.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
