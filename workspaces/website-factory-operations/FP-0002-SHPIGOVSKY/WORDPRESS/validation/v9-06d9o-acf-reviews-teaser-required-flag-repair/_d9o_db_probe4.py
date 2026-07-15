"""TEMPORARY HELPER — NOT FOR GIT COMMIT"""
import json
import re
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor()

cur.execute("SELECT ID, post_excerpt, post_title, post_content FROM fp02_posts WHERE post_type='acf-field' AND post_parent=114 ORDER BY menu_order")
rows = cur.fetchall()
required_fields = []
for row in rows:
    pid, excerpt, title, content = row
    text = content or ""
    req = re.search(r'"required";i:(\d+)', text)
    mn = re.search(r'"min";i:(\d+)', text)
    r = int(req.group(1)) if req else None
    m = int(mn.group(1)) if mn else None
    if r == 1 or (m and m > 0):
        required_fields.append({"id": pid, "name": excerpt, "title": title, "required": r, "min": m})

print("BLOCKING_FIELDS", json.dumps(required_fields, ensure_ascii=False))

cur.execute("SELECT post_content FROM fp02_posts WHERE ID=114")
print("GROUP_CONTENT", cur.fetchone()[0])

cur.execute("SELECT meta_key, meta_value FROM fp02_postmeta WHERE post_id=114")
print("GROUP_META", cur.fetchall())

conn.close()
