"""TEMPORARY HELPER — NOT FOR GIT COMMIT"""
import json
import re
import sys

import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mars_wp_fp0002",
    charset="utf8mb4",
)
cur = conn.cursor()

cur.execute(
    """
SELECT p.ID, p.post_name, p.post_title, p.post_status, p.post_modified
FROM fp02_posts p
WHERE p.post_type='acf-field-group'
  AND (p.post_name=%s OR p.post_title LIKE %s)
""",
    ("group_fp02_page_home", "%Home%"),
)
rows = cur.fetchall()
print("GROUP_POSTS", json.dumps(rows, default=str))

for row in rows:
    pid = row[0]
    cur.execute("SELECT post_content FROM fp02_posts WHERE ID=%s", (pid,))
    content = cur.fetchone()[0] or ""
    text = content if isinstance(content, str) else content.decode("utf-8", "replace")
    print("POST_ID", pid, "CONTENT_LEN", len(text))
    m2 = re.search(
        r'"name";s:19:"home_reviews_teaser".{0,1200}?"required";i:(\d+)',
        text,
        re.S,
    )
    m3 = re.search(
        r'"name";s:19:"home_reviews_teaser".{0,1200}?"min";i:(\d+)',
        text,
        re.S,
    )
    print("REGEX_REQUIRED", m2.group(1) if m2 else None)
    print("REGEX_MIN", m3.group(1) if m3 else None)

cur.execute(
    "SELECT meta_value FROM fp02_postmeta WHERE post_id=4 AND meta_key='home_reviews_teaser'"
)
print("HOME_VALUE", cur.fetchone())
cur.execute(
    "SELECT meta_value FROM fp02_postmeta WHERE post_id=4 AND meta_key='_home_reviews_teaser'"
)
print("HOME_FIELD_KEY", cur.fetchone())

cur.execute(
    "SELECT post_name, post_title FROM fp02_posts WHERE post_type='acf-field-group' ORDER BY post_title"
)
print("ALL_GROUPS", cur.fetchall())

conn.close()
