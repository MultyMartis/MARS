#!/usr/bin/env python3
"""E14 baseline probe — NOT FOR GIT."""
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
    """
    SELECT p.ID, p.post_title, p.post_name, p.post_parent, p.post_status, p.menu_order, p.post_type
    FROM fp02_posts p
    WHERE p.post_type IN ('service', 'page')
      AND p.post_status != 'auto-draft'
    ORDER BY p.post_type, p.post_parent, p.menu_order, p.ID
    """
)
rows = cur.fetchall()

service_ids = [r["ID"] for r in rows if r["post_type"] == "service"]
meta_by_id = {sid: {} for sid in service_ids}
if service_ids:
    fmt = ",".join(["%s"] * len(service_ids))
    cur.execute(
        f"""
        SELECT post_id, meta_key, meta_value
        FROM fp02_postmeta
        WHERE post_id IN ({fmt})
          AND (
            meta_key IN (
              'service_layout_variant', 'hero_lead', 'intro_text', 'hero_title_override',
              'service_short_description'
            )
          )
        """,
        service_ids,
    )
    for m in cur.fetchall():
        if not m["meta_key"].startswith("_"):
            meta_by_id.setdefault(m["post_id"], {})[m["meta_key"]] = m["meta_value"]

cur.execute(
    "SELECT post_id, meta_value FROM fp02_postmeta WHERE meta_key = 'services_hub_query_mode'"
)
hub_mode = cur.fetchall()

cur.execute(
    "SELECT ID, post_title, post_name, post_parent, post_status, post_type FROM fp02_posts WHERE post_name = 'specialistam'"
)
spec = cur.fetchall()

cur.execute(
    """
    SELECT p.ID, p.post_title, p.post_name, p.menu_order, p.post_status
    FROM fp02_posts p
    JOIN fp02_posts parent ON p.post_parent = parent.ID
    WHERE parent.post_name = 'zavisimosti' AND p.post_type = 'service'
    ORDER BY p.menu_order, p.ID
    """
)
zav_children = cur.fetchall()

cur.execute(
    """
    SELECT p.ID, p.post_title, p.post_name, p.post_status, pm.meta_value AS layout_variant
    FROM fp02_posts p
    LEFT JOIN fp02_postmeta pm ON pm.post_id = p.ID AND pm.meta_key = 'service_layout_variant'
    WHERE p.post_name IN ('zavisimosti', 'psihicheskoe-zdorovie', 'rasstroystva-pischevogo-povedeniya')
      AND p.post_type = 'service'
    """
)
subdivisions = cur.fetchall()

out = {
    "services_and_pages": rows,
    "service_meta": meta_by_id,
    "hub_query_mode": hub_mode,
    "specialistam_objects": spec,
    "zavisimosti_children": zav_children,
    "subdivision_parents": subdivisions,
}
print(json.dumps(out, ensure_ascii=False, default=str, indent=2))
