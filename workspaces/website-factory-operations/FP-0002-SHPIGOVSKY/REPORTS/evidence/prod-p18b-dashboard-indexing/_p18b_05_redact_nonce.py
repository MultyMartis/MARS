# -*- coding: utf-8 -*-
import re
from pathlib import Path

p = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing\dashboard-after-snippet.html")
t = p.read_text(encoding="utf-8")
t2 = re.sub(r'(name="_wpnonce" value=")[^"]+(")', r"\1REDACTED\2", t)
t2 = re.sub(r'(id="_wpnonce" name="_wpnonce" value=")[^"]+(")', r"\1REDACTED\2", t2)
p.write_text(t2, encoding="utf-8")
print("changed", t != t2)
