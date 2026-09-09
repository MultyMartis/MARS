#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js")
text = p.read_text(encoding="utf-8")
text, n1 = re.subn(r": '([a-z0-9_]+__FORM\.php)'", r": '/\1'", text)
text, n2 = re.subn(
    r"url:\s*root \? '(/[a-z0-9_]+__FORM\.php)' : '\1'",
    r"url: '\1'",
    text,
)
p.write_text(text, encoding="utf-8")
print("else_root", n1)
print("simplified_ternary", n2)
print("remaining_unrooted", re.findall(r"'[a-z0-9_]+__FORM\.php'", text))
