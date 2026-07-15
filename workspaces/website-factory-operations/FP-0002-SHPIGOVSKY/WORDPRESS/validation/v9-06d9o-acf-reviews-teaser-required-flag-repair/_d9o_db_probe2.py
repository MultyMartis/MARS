"""TEMPORARY HELPER — NOT FOR GIT COMMIT"""
import json
import re

import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor()

# Field posts for home group
cur.execute(
    """
SELECT p.ID, p.post_excerpt, p.post_name, p.post_content
FROM fp02_posts p
WHERE p.post_type='acf-field'
  AND (p.post_excerpt='home_reviews_teaser' OR p.post_content LIKE %s OR p.post_name LIKE %s)
""",
    ("%home_reviews_teaser%", "%home_reviews_teaser%"),
)
rows = cur.fetchall()
print("FIELD_POSTS", len(rows))
for row in rows:
    pid, excerpt, name, content = row
    text = content or ""
    req = re.search(r'"required";i:(\d+)', text)
    mn = re.search(r'"min";i:(\d+)', text)
    fkey = re.search(r'"key";s:\d+:"([^"]+)"', text)
    print(json.dumps({
        "id": pid,
        "excerpt": excerpt,
        "post_name": name,
        "field_key": fkey.group(1) if fkey else None,
        "required": int(req.group(1)) if req else None,
        "min": int(mn.group(1)) if mn else None,
        "content_len": len(text),
    }))

# Parent relationship via post_parent
cur.execute(
    """
SELECT p.ID, p.post_excerpt, p.post_parent, pm.meta_value AS parent_key
FROM fp02_posts p
LEFT JOIN fp02_postmeta pm ON pm.post_id=p.ID AND pm.meta_key='field_group_key'
WHERE p.post_type='acf-field' AND p.post_excerpt='home_reviews_teaser'
"""
)
print("PARENT_ROWS", cur.fetchall())

# Group 114 children
cur.execute("SELECT ID, post_excerpt, post_title FROM fp02_posts WHERE post_type='acf-field' AND post_parent=114 ORDER BY menu_order")
children = cur.fetchall()
print("GROUP114_CHILDREN", len(children))
for c in children:
    if c[1] == 'home_reviews_teaser' or (c[2] and 'review' in c[2].lower()):
        cur.execute("SELECT post_content FROM fp02_posts WHERE ID=%s", (c[0],))
        text = cur.fetchone()[0] or ""
        req = re.search(r'"required";i:(\d+)', text)
        mn = re.search(r'"min";i:(\d+)', text)
        print("TARGET", c[0], c[1], c[2], "required", req.group(1) if req else None, "min", mn.group(1) if mn else None)

# All home meta keys for post 4 related to reviews
cur.execute("SELECT meta_key, LEFT(meta_value,120) FROM fp02_postmeta WHERE post_id=4 AND meta_key LIKE '%review%' ORDER BY meta_key")
print("HOME_REVIEW_META", cur.fetchall())

conn.close()
