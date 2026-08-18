# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path
import requests

EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing")
UA = "FP-0002-P18B-reprobe/1.0"
rows = []
for i in range(5):
    r = requests.get("https://shpigovsky.ru/", timeout=25, allow_redirects=True, headers={"User-Agent": UA})
    body = r.text or ""
    gm = re.search(r'<meta name=["\']generator["\'] content=["\']([^"\']+)', body, re.I)
    rm = re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', body, re.I)
    tm = re.search(r"<title>([^<]+)", body, re.I)
    rows.append({
        "i": i,
        "status": r.status_code,
        "server": r.headers.get("Server"),
        "bytes": len(r.content or b""),
        "has_wp": ("wp-content" in body) or ("WordPress" in body),
        "generator": gm.group(1) if gm else None,
        "robots_meta": rm.group(1) if rm else None,
        "title": tm.group(1) if tm else None,
        "head": body[:160],
    })
rr = requests.get("https://shpigovsky.ru/robots.txt", timeout=20, headers={"User-Agent": UA})
rb = requests.get("https://shpigovsky.ru/privacy-policy/", timeout=25, headers={"User-Agent": UA})
pb = rb.text or ""
out = {
    "home_x5": rows,
    "robots": {
        "status": rr.status_code,
        "server": rr.headers.get("Server"),
        "text": (rr.content or b"")[:220].decode("utf-8", "replace"),
    },
    "privacy": {
        "status": rb.status_code,
        "server": rb.headers.get("Server"),
        "has_wp": "wp-content" in pb,
        "robots_meta": (m.group(1) if (m := re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', pb, re.I)) else None),
        "title": (m.group(1) if (m := re.search(r"<title>([^<]+)", pb, re.I)) else None),
    },
}
(EV / "PUBLIC-REPROBE.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2, ensure_ascii=False))
