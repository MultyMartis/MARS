"""TEMPORARY HELPER — NOT FOR GIT COMMIT"""
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor()

cur.execute("SELECT post_content FROM fp02_posts WHERE ID=128")
print(cur.fetchone()[0])

print("--- META ---")
cur.execute("SELECT meta_key, meta_value FROM fp02_postmeta WHERE post_id=128 ORDER BY meta_key")
for k, v in cur.fetchall():
    print(k, "=>", v[:200] if v else v)

# Check all required=1 fields in home group
cur.execute("SELECT ID, post_excerpt, post_title, post_content FROM fp02_posts WHERE post_type='acf-field' AND post_parent=114")
for row in cur.fetchall():
    pid, excerpt, title, content = row
    if '"required";i:1' in (content or ""):
        print("REQUIRED_FIELD", pid, excerpt, title)

conn.close()
