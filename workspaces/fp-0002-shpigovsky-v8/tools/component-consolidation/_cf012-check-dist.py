#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "dist"
for name in ["uslugi-v2.html", "usluga-konechnaya-v1.html", "usluga-podrazdel-v1.html"]:
    text = (ROOT / name).read_text(encoding="utf-8")
    m = re.search(r'<section class="(services-program-v2[^"]*)"', text)
    print(name, m.group(1) if m else "NOT FOUND")
