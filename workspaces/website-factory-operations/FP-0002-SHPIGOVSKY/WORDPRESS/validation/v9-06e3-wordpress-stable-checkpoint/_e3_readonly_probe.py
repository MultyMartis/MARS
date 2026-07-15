#!/usr/bin/env python3
"""TEMPORARY E3 read-only probe — NOT FOR GIT."""
import hashlib
import json
import re
import urllib.request

import pymysql

BASE = "http://shpigovsky.test"
E2_HASHES = {
    "3": "588845cf73e2955656d3166e684c4f722b625aa929953a0821bba941f0502f28",
    "22": "47e15c92fb21ab0aa6fa0100190210af4637e08adc80ae65f26b5005b61b4e50",
    "23": "8ac8489399253c5d9e92dc46643a86289bfc27d32f7560af69df7bd8a689e866",
    "24": "a06f0209c5b3379941242a2550a623cadbeb998ef06485179b83e81eb5f8809d",
    "25": "0f00e812b2c40a8f0b3150e98b4ce744fc5b70fbc82989c455c28a248363c610",
}

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mars_wp_fp0002",
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)

cur.execute(
    "SELECT option_name, option_value FROM fp02_options "
    "WHERE option_name IN ('template','stylesheet','wp_page_for_privacy_policy',"
    "'classic-editor-replace','classic-editor-allow-users')"
)
opts = {r["option_name"]: r["option_value"] for r in cur.fetchall()}

cur.execute("SELECT option_value FROM fp02_options WHERE option_name='active_plugins'")
active_plugins_raw = cur.fetchone()["option_value"]
active_plugins = []
if active_plugins_raw:
    try:
        active_plugins = json.loads(active_plugins_raw)
    except json.JSONDecodeError:
        active_plugins = re.findall(r's:\d+:"([^"]+)"', active_plugins_raw)

cur.execute(
    "SELECT ID, post_title, post_name, post_status FROM fp02_posts "
    "WHERE ID IN (3,21,22,23,24,25) AND post_type='page'"
)
pages = []
for row in cur.fetchall():
    cur.execute("SELECT post_content FROM fp02_posts WHERE ID=%s", (row["ID"],))
    content = cur.fetchone()["post_content"]
    sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
    pages.append(
        {
            **row,
            "content_len": len(content),
            "content_sha256": sha,
            "e2_hash_match": sha == E2_HASHES.get(str(row["ID"])),
            "has_substantive_content": len(content.strip()) > 200,
        }
    )

cur.execute(
    "SELECT option_name, option_value FROM fp02_options "
    "WHERE option_name LIKE 'fp02-reviews_reviews_items_0_%' "
    "OR option_name LIKE 'options_reviews_items_0_%' ORDER BY option_name"
)
review_meta = cur.fetchall()
first_author = None
for m in review_meta:
    if m["option_name"].endswith(("review_author", "author_label")):
        first_author = m["option_value"]
        break

cur.execute(
    "SELECT option_value FROM fp02_options WHERE option_name='fp02-reviews_reviews_enabled'"
)
reviews_enabled_row = cur.fetchone()
if not reviews_enabled_row:
    cur.execute(
        "SELECT option_value FROM fp02_options WHERE option_name='options_reviews_enabled'"
    )
    reviews_enabled_row = cur.fetchone()

cur.execute(
    "SELECT COUNT(*) AS c FROM fp02_posts WHERE post_type='acf-field-group' "
    "AND post_status='publish' AND post_title LIKE '%reviews%'"
)
acf_review_groups = cur.fetchone()["c"]
cur.execute(
    "SELECT COUNT(*) AS c FROM fp02_posts WHERE post_type='acf-field-group' "
    "AND post_status='trash' AND post_title LIKE '%reviews%'"
)
acf_trashed_review_groups = cur.fetchone()["c"]

cur.execute(
    """
    SELECT p.ID, p.post_title, p.menu_order, pm_url.meta_value AS url,
           pm_obj.meta_value AS object_id, pm_type.meta_value AS type,
           tt.term_id AS menu_term_id, t.name AS menu_name, t.slug AS menu_slug
    FROM fp02_posts p
    JOIN fp02_term_relationships tr ON p.ID = tr.object_id
    JOIN fp02_term_taxonomy tt ON tr.term_taxonomy_id = tt.term_taxonomy_id AND tt.taxonomy='nav_menu'
    JOIN fp02_terms t ON tt.term_id = t.term_id
    LEFT JOIN fp02_postmeta pm_url ON p.ID = pm_url.post_id AND pm_url.meta_key='_menu_item_url'
    LEFT JOIN fp02_postmeta pm_obj ON p.ID = pm_obj.post_id AND pm_obj.meta_key='_menu_item_object_id'
    LEFT JOIN fp02_postmeta pm_type ON p.ID = pm_type.post_id AND pm_type.meta_key='_menu_item_type'
    WHERE p.post_type='nav_menu_item' AND p.post_status='publish'
    ORDER BY tt.term_id, p.menu_order
    """
)
items = cur.fetchall()
for item in items:
    if item.get("type") == "post_type" and item.get("object_id"):
        cur.execute(
            "SELECT post_name, post_title, post_status FROM fp02_posts WHERE ID=%s",
            (item["object_id"],),
        )
        pg = cur.fetchone()
        if pg:
            item["page_slug"] = pg["post_name"]
            item["page_title"] = pg["post_title"]
            item["page_status"] = pg["post_status"]

home = urllib.request.urlopen(BASE + "/").read().decode("utf-8", "replace")
nav = re.findall(
    r'class="site-header__nav-link[^"]*"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>',
    home,
)
footer_block = re.search(
    r'aria-label="[^"]*информация[^"]*"[\s\S]*?</nav>',
    home,
    re.I,
)
fb = footer_block.group(0) if footer_block else home
legal_links = re.findall(
    r'class="site-footer__nav-link"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>',
    fb,
)
otzyvy = urllib.request.urlopen(BASE + "/otzyvy/").read().decode("utf-8", "replace")
pp = urllib.request.urlopen(BASE + "/privacy-policy/").read().decode("utf-8", "replace")

# CSS width cap check via linked stylesheet
css_urls = re.findall(r'href="([^"]*v9-style[^"]*)"', pp)
css_has_900 = False
if css_urls:
    css = urllib.request.urlopen(css_urls[0]).read().decode("utf-8", "replace")
    css_has_900 = (
        "legal-document__container" in css
        and re.search(r"legal-document__container[\s\S]{0,400}max-width:\s*900px", css)
        is not None
    )

out = {
    "opts": opts,
    "active_plugins": active_plugins,
    "pages": pages,
    "first_review_author_meta": first_author,
    "reviews_enabled": reviews_enabled_row["option_value"] if reviews_enabled_row else None,
    "acf_review_groups_publish": acf_review_groups,
    "acf_trashed_review_groups": acf_trashed_review_groups,
    "primary_nav": [{"label": t.strip(), "url": u} for u, t in nav],
    "footer_legal_links": [{"label": t.strip(), "url": u} for u, t in legal_links],
    "hub_21_in_footer": any("pravovaya" in u for u, _ in legal_links),
    "footer_legal_count": len(legal_links),
    "reviews_home_andrey": "Андрей" in home and "Москва" in home,
    "reviews_otzyvy_andrey": "Андрей" in otzyvy and "Москва" in otzyvy,
    "legal_width_900_in_linked_css": css_has_900,
    "menu_items": items,
}
print(json.dumps(out, ensure_ascii=False, indent=2, default=str))
conn.close()
