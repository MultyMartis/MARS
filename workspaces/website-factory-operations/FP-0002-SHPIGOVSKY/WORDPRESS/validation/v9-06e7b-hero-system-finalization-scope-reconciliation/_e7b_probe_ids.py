#!/usr/bin/env python3
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor()
cur.execute("SELECT ID, post_name, post_title FROM fp02_posts WHERE post_type='service' AND post_status='publish' ORDER BY ID")
print("SERVICES:")
for r in cur.fetchall():
    print(r)
print("HERO META:")
for oid in [4, 5, 73, 74, 77, 84]:
    cur.execute(
        "SELECT meta_key, LEFT(meta_value,80) FROM fp02_postmeta WHERE post_id=%s AND meta_key LIKE %s",
        (oid, "%hero%"),
    )
    rows = cur.fetchall()
    if rows:
        print(oid, rows)
conn.close()
