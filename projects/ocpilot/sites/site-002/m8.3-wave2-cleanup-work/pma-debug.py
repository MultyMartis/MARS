#!/usr/bin/env python3
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"

op = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),
    urllib.request.HTTPSHandler(context=ssl.create_default_context()),
)
lp = op.open(PMA + "/").read().decode("utf-8", "replace")
t = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
op.open(
    urllib.request.Request(
        PMA + "/index.php",
        data=urllib.parse.urlencode(
            {
                "pma_username": "polygonws_zpm",
                "pma_password": "VBCDry2bJ5P",
                "server": "1",
                "target": "index.php",
                "token": t,
            }
        ).encode(),
        method="POST",
    ),
    timeout=60,
)
db = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode(
    "utf-8", "replace"
)
csrf = re.search(r'name="token"\s+value="([^"]+)"', db).group(1)
sql = "SELECT attribute_id, name FROM oc_attribute_description WHERE language_id=1 AND attribute_id IN (43,44,45) ORDER BY attribute_id"
html = op.open(
    urllib.request.Request(
        PMA + "/sql.php",
        data=urllib.parse.urlencode(
            {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
        ).encode(),
        method="POST",
    ),
    timeout=240,
).read().decode("utf-8", "replace")
print("MySQL said:", "MySQL said:" in html)
print("empty:", "empty result set" in html.lower())
if "MySQL said:" in html:
    m = re.search(r"MySQL said:\s*<[^>]+>([^<]+)", html)
    print("ERR", m.group(1).strip() if m else "?")
tables = re.findall(r'<table[^>]*class="[^"]*table[^"]*"[^>]*>', html)
print("tables found:", len(tables))
open(r"C:\AI MARS\projects\ocpilot\sites\site-002\m8.3-wave2-cleanup-work\pma-debug.html", "w", encoding="utf-8").write(
    html[:12000]
)
