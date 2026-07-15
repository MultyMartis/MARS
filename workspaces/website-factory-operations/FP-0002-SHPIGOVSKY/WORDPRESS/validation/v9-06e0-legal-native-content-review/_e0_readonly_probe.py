#!/usr/bin/env python3
"""V9-06E0 read-only DB + HTTP probe. Do not stage this helper."""
import hashlib
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone

import pymysql

DB = {
    "host": "127.0.0.1",
    "user": "mli_shpigovsky_app",
    "password": "9st4UPjdkc5MXyuNKEGTQaS0V7AD1ClR",
    "database": "mars_wp_fp0002",
    "charset": "utf8mb4",
}
IDS = [3, 6, 7, 8, 9, 10, 17, 19, 21, 22, 23, 24, 25]
HIDE_EDITOR = {4, 5, 11, 12, 13, 14, 15, 16, 18, 20, 22, 23, 24}
BASE = "http://shpigovsky.test"
OUT = __file__.replace("_e0_readonly_probe.py", "_e0_db_probe_raw.json")


def sample(text, n=220):
    if not text:
        return ""
    return re.sub(r"\s+", " ", text.strip())[:n]


def classify_content(pid, content, template):
    clen = len(content or "")
    if pid == 3 and clen > 1000:
        return "GARBLED_LEGAL_SEED"
    if pid in (22, 23, 24) and clen == 0 and template == "page-templates/legal.php":
        return "TEMPLATE_MANAGED_EMPTY_OK"
    if clen == 431:
        return "PLACEHOLDER_LOCAL_DEV"
    if clen == 0 and template:
        return "TEMPLATE_MANAGED_EMPTY_OK"
    return "OPERATOR_REVIEW_REQUIRED"


def http_probe(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "V9-06E0-readonly"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
            body = resp.read(12000).decode("utf-8", errors="replace")
            return {
                "http_status": resp.status,
                "body_length": len(body),
                "has_h1": "<h1" in body.lower(),
                "has_garbled_markers": "Предлагаемый текст" in body or "╨" in body,
                "has_placeholder_dev": "локальной разработки" in body,
                "has_demo_placeholder": "демонстрацион" in body.lower(),
                "title_in_body": bool(re.search(r"<title>([^<]+)</title>", body, re.I)),
            }
    except urllib.error.HTTPError as exc:
        return {"http_status": exc.code, "error": str(exc)[:200]}
    except Exception as exc:  # noqa: BLE001
        return {"http_status": "ERROR", "error": str(exc)[:200]}


def main():
    conn = pymysql.connect(**DB)
    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute(
        "SELECT option_name, option_value FROM fp02_options "
        "WHERE option_name IN ('wp_page_for_privacy_policy','page_on_front','show_on_front')"
    )
    opts = {r["option_name"]: r["option_value"] for r in cur.fetchall()}

    fmt = ",".join(str(i) for i in IDS)
    cur.execute(
        f"SELECT ID, post_title, post_name, post_status, post_content "
        f"FROM fp02_posts WHERE ID IN ({fmt})"
    )
    pages = {r["ID"]: r for r in cur.fetchall()}

    cur.execute(
        f"SELECT post_id, meta_value FROM fp02_postmeta "
        f"WHERE post_id IN ({fmt}) AND meta_key='_wp_page_template'"
    )
    templates = {r["post_id"]: r["meta_value"] for r in cur.fetchall()}

    legal_sql = """
        SELECT p.menu_order, pm_obj.meta_value AS object_id, pm_type.meta_value AS item_type,
               pm_url.meta_value AS custom_url, pm_title.meta_value AS menu_title
        FROM fp02_posts p
        JOIN fp02_term_relationships tr ON p.ID = tr.object_id
        JOIN fp02_term_taxonomy tt ON tr.term_taxonomy_id = tt.term_taxonomy_id
        JOIN fp02_terms t ON tt.term_id = t.term_id
        LEFT JOIN fp02_postmeta pm_obj ON p.ID = pm_obj.post_id AND pm_obj.meta_key='_menu_item_object_id'
        LEFT JOIN fp02_postmeta pm_type ON p.ID = pm_type.post_id AND pm_type.meta_key='_menu_item_type'
        LEFT JOIN fp02_postmeta pm_url ON p.ID = pm_url.post_id AND pm_url.meta_key='_menu_item_url'
        LEFT JOIN fp02_postmeta pm_title ON p.ID = pm_title.post_id AND pm_title.meta_key='_menu_item_title'
        WHERE tt.taxonomy='nav_menu' AND t.slug='legal'
        ORDER BY p.menu_order
    """
    cur.execute(legal_sql)
    legal_menu = cur.fetchall()

    inventory = []
    for pid in IDS:
        p = pages.get(pid, {})
        content = p.get("post_content") or ""
        tmpl = templates.get(pid, "")
        slug = p.get("post_name", "")
        route = f"/{slug}/" if slug else "/"
        http = http_probe(BASE + route)
        inv = {
            "page_id": pid,
            "title": p.get("post_title", ""),
            "slug": slug,
            "status": p.get("post_status", ""),
            "template": tmpl,
            "route_url": BASE + route,
            "frontend_http_status": http.get("http_status"),
            "frontend_probe": http,
            "native_post_content_length": len(content),
            "native_post_content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest()
            if content
            else "",
            "native_post_content_sample": sample(content),
            "is_garbled": pid == 3 and len(content) > 1000,
            "is_placeholder": len(content) == 431,
            "is_legal_system": pid in (3, 21, 22, 23, 24, 25),
            "is_template_managed": bool(tmpl) or pid in (22, 23, 24),
            "native_editor_hidden": pid in HIDE_EDITOR,
            "native_editor_retained": pid not in HIDE_EDITOR,
            "in_footer_legal_fallback": pid in (3, 22, 23, 24),
            "classification": classify_content(pid, content, tmpl),
        }
        if pid == 3 and p.get("post_status") == "draft":
            inv["exposes_garbled_on_frontend"] = False
            inv["notes"] = "Draft; public route may not serve garbled body"
        else:
            inv["exposes_garbled_on_frontend"] = inv["is_garbled"] and http.get("http_status") == 200
        inventory.append(inv)

    out = {
        "phase": "V9-06E0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "wp_options": opts,
        "privacy_page_setting_id": int(opts.get("wp_page_for_privacy_policy") or 0),
        "legal_menu_items": legal_menu,
        "pages": inventory,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    print(OUT)


if __name__ == "__main__":
    main()
