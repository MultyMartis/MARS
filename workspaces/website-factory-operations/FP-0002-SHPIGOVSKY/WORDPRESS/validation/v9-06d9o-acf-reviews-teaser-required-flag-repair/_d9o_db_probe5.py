"""TEMPORARY HELPER — NOT FOR GIT COMMIT"""
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor()

# search all postmeta for reviews teaser field key
cur.execute("""
SELECT pm.post_id, pm.meta_key, LEFT(pm.meta_value, 200)
FROM fp02_postmeta pm
WHERE pm.meta_value LIKE '%field_fp02_home_reviews_teaser%'
   OR pm.meta_key LIKE '%reviews_teaser%'
ORDER BY pm.post_id, pm.meta_key
LIMIT 50
""")
for row in cur.fetchall():
    print(row)

# acfe validation options
cur.execute("SELECT option_name, LEFT(option_value, 300) FROM fp02_options WHERE option_name LIKE '%acf%' AND option_value LIKE '%reviews%' LIMIT 20")
print('OPTIONS', cur.fetchall())

conn.close()
