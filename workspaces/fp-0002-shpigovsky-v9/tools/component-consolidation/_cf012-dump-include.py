#!/usr/bin/env python3
import re
import subprocess
import sys

commit = "4d98d6fbc273bd1bd4cf4555d973f2b978bef0fa"
page = sys.argv[1]
text = subprocess.check_output(
    ["git", "-C", r"X:\AI MARS", "show", f"{commit}:workspaces/fp-0002-shpigovsky-v8/src/pages/{page}"],
    text=True,
    encoding="utf-8",
)
for pat in ["services-program-v2.html", "hideCtaBand"]:
    if pat in text:
        idx = text.find(pat)
        print(text[max(0, idx - 50) : idx + 800])
        print("---")
