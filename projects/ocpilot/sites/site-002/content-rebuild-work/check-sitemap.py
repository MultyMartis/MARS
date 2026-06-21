#!/usr/bin/env python3
import re
import urllib.request

BASE = "https://zpm.new-site.space"
req = urllib.request.Request(BASE + "/sitemap.xml", headers={"Cookie": "beget=begetok"})
xml = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
print("len", len(xml))
print(xml[:1500])
locs = re.findall(r"<loc>([^<]+)</loc>", xml)
print("locs", len(locs))
for u in locs[:10]:
    print(u)
