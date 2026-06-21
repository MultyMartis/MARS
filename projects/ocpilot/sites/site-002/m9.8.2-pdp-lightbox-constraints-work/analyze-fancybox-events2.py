#!/usr/bin/env python3
import re

path = r"C:\AI MARS\projects\ocpilot\sites\site-002\m9.8.2-pdp-lightbox-constraints-work\fancybox.umd.js"
t = open(path, encoding="utf-8").read()
for name in ["reveal", "done", "init", "ready", "destroy", "loading"]:
    print(name, t.count(name))
# find on: handlers pattern in defaults
idx = t.find("on:{}")
print("defaults on", t[idx : idx + 80])
