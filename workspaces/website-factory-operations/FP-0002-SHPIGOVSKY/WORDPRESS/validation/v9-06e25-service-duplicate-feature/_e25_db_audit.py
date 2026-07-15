#!/usr/bin/env python3
"""E25 DB audit helper — NOT FOR GIT."""
import json
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mars_wp_fp0002",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
cur = conn.cursor()
cur.execute(
    "SELECT ID, post_title, post_name, post_status, post_parent, menu_order, post_author "
    "FROM fp02_posts WHERE post_type='service' ORDER BY post_parent, menu_order, ID"
)
services = cur.fetchall()

def meta_for(post_id):
    cur.execute(
        "SELECT meta_key, meta_value FROM fp02_postmeta WHERE post_id=%s ORDER BY meta_key",
        (post_id,),
    )
    return cur.fetchall()

def thumb(post_id):
    cur.execute(
        "SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key='_thumbnail_id'",
        (post_id,),
    )
    r = cur.fetchone()
    return r["meta_value"] if r else None

def terms(post_id):
    cur.execute(
        "SELECT t.slug, tt.taxonomy FROM fp02_term_relationships tr "
        "JOIN fp02_term_taxonomy tt ON tr.term_taxonomy_id=tt.term_taxonomy_id "
        "JOIN fp02_terms t ON tt.term_id=t.term_id "
        "WHERE tr.object_id=%s",
        (post_id,),
    )
    return cur.fetchall()

out = {"service_count": len(services), "services": services}
for slug in ("zavisimosti", "lechenie-alkogolnoy-zavisimosti"):
    cur.execute(
        "SELECT ID, post_title, post_name, post_status, post_parent, menu_order "
        "FROM fp02_posts WHERE post_type='service' AND post_name=%s LIMIT 1",
        (slug,),
    )
    row = cur.fetchone()
    if row:
        pid = row["ID"]
        out[slug] = {
            "post": row,
            "thumbnail_id": thumb(pid),
            "taxonomy_terms": terms(pid),
            "meta_keys": [m["meta_key"] for m in meta_for(pid)],
            "meta": meta_for(pid),
        }

cur.execute(
    "SELECT option_name FROM fp02_options WHERE option_name LIKE '%hero%' "
    "AND option_name NOT LIKE '%\\_hero\\_%'"
)
out["global_hero_options"] = [r["option_name"] for r in cur.fetchall()]
conn.close()
print(json.dumps(out, ensure_ascii=False, indent=2, default=str))
