import pymysql
conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute("SELECT ID, post_name, post_parent, post_title FROM fp02_posts WHERE post_type='service' AND post_status='publish' ORDER BY ID")
for r in cur.fetchall():
    print(r["ID"], r["post_name"], "parent", r["post_parent"], "|", r["post_title"][:60])
conn.close()
