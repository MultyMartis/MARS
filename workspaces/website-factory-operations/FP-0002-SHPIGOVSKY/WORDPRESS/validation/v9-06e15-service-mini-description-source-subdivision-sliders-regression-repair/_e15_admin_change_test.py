#!/usr/bin/env python3
"""Admin change propagation test — TEMP, NOT FOR GIT."""
import pymysql
import urllib.request

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mars_wp_fp0002",
    charset="utf8mb4",
)
cur = conn.cursor()

tests = [(74, "E15-ADMIN-MARKER-74"), (75, "E15-ADMIN-MARKER-75")]
for post_id, marker in tests:
    cur.execute(
        "UPDATE fp02_postmeta SET meta_value=%s WHERE post_id=%s AND meta_key='service_short_description'",
        (marker, post_id),
    )
    conn.commit()
    html = urllib.request.urlopen("http://shpigovsky.test/uslugi/").read().decode("utf-8", "replace")
    print(post_id, "marker_in_html", marker in html)
