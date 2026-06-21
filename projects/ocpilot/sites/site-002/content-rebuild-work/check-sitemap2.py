#!/usr/bin/env python3
import re
import urllib.request

for sm in [
    "https://zpm.new-site.space/sitemap.xml",
    "https://zpm.new-site.space/index.php?route=extension/feed/google_sitemap",
]:
    try:
        req = urllib.request.Request(sm, headers={"Cookie": "beget=begetok"})
        body = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
        locs = re.findall(r"<loc>([^<]+)</loc>", body)
        print(sm, "len", len(body), "locs", len(locs))
        if locs:
            print(" first", locs[0])
            deep = [u for u in locs if u.count("/") >= 6]
            print(" deep", len(deep))
    except Exception as e:
        print(sm, "ERR", e)
