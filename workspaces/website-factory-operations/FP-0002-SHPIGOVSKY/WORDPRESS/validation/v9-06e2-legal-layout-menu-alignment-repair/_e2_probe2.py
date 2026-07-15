#!/usr/bin/env python3
"""TEMPORARY probe — NOT FOR GIT."""
import json
import pymysql

conn = pymysql.connect(
    host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4"
)
cur = conn.cursor(pymysql.cursors.DictCursor)

cur.execute(
    "SELECT option_name, option_value FROM fp02_options WHERE option_name LIKE '%nav_menu%' OR option_name='theme_mods_shpigovsky'"
)
opts = cur.fetchall()

cur.execute(
    "SELECT ID, post_title, post_name, post_status, post_parent FROM fp02_posts "
    "WHERE post_type='page' AND (post_name LIKE '%zavisim%' OR post_name='uslugi' OR post_parent=5) "
    "ORDER BY post_parent, menu_order"
)
pages = cur.fetchall()

cur.execute(
    "SELECT ID, post_title, post_name FROM fp02_posts WHERE post_type='page' AND post_status='publish' ORDER BY ID"
)
all_pages = cur.fetchall()

print(json.dumps({"options": opts, "uslugi_tree": pages, "all_page_count": len(all_pages)}, ensure_ascii=False, indent=2, default=str))
conn.close()
