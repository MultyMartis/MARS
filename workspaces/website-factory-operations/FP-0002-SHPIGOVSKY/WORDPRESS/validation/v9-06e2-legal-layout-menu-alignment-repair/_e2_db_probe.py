#!/usr/bin/env python3
"""TEMPORARY — DB probe for E2 baseline. NOT FOR GIT."""
import json
import pymysql

conn = pymysql.connect(
    host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4"
)
cur = conn.cursor(pymysql.cursors.DictCursor)

cur.execute(
    "SELECT ID, post_title, post_name, post_status FROM fp02_posts "
    "WHERE ID IN (3,21,22,23,24,25) AND post_type='page'"
)
pages = cur.fetchall()

cur.execute(
    "SELECT t.term_id, t.name, t.slug FROM fp02_terms t "
    "JOIN fp02_term_taxonomy tt ON t.term_id=tt.term_id WHERE tt.taxonomy='nav_menu'"
)
menus = cur.fetchall()

cur.execute("SELECT option_value FROM fp02_options WHERE option_name='theme_mods_shpigovsky'")
theme_mods = cur.fetchone()

cur.execute("SELECT option_value FROM fp02_options WHERE option_name='nav_menu_locations'")
locations = cur.fetchone()

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

cur.execute("SELECT option_value FROM fp02_options WHERE option_name='wp_page_for_privacy_policy'")
privacy = cur.fetchone()

# Resolve object_id to slug for post_type=page items
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

out = {
    "pages": pages,
    "menus": menus,
    "nav_menu_locations": locations,
    "menu_items": items,
    "privacy_policy_page_id": privacy,
}
print(json.dumps(out, ensure_ascii=False, indent=2, default=str))
conn.close()
