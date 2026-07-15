import pymysql
conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
cur.execute("SELECT ID, post_name, post_status, post_parent FROM fp02_posts WHERE ID IN (79,80) OR post_name LIKE '%ptsr%' OR post_name LIKE '%emot%'")
for r in cur.fetchall():
    print(r)
conn.close()
