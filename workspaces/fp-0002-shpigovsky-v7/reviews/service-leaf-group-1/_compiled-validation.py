"""Compiled validation + regression hash probe for SERVICE LEAF GROUP 1."""
import hashlib
import json
import re
from pathlib import Path

ws = Path(__file__).resolve().parents[2]
dist = ws / "dist"
leaf = (dist / "usluga-konechnaya-v1.html").read_text(encoding="utf-8")

checks = {
    "page_class": leaf.count('class="page-service-leaf-v1"'),
    "header": leaf.count("<header"),
    "hero": leaf.count("services-inner-hero-v2"),
    "breadcrumbs": leaf.count('class="breadcrumbs"'),
    "subnav": leaf.count("services-page-subnav"),
    "intro": leaf.count("service-leaf-intro-v1"),
    "bordered_info": leaf.count("service-leaf-bordered-info-v1"),
    "bordered_subsections": leaf.count("service-leaf-bordered-info-v1__subsection"),
    "cta_01": leaf.count("service-leaf-cta-01-v1"),
    "boundary": leaf.count("<!-- SERVICE-LEAF-GROUP-1-BOUNDARY -->"),
    "footer": leaf.count("<footer"),
    "modal": leaf.count('data-modal="consultation"'),
    "hero_asset": leaf.count("service-leaf-alcohol-hero.webp"),
    "lifebuoy_markup": len(re.findall(r"lifebuoy", leaf, re.I)),
    "lifebuoy_refs": len(re.findall(r"lifebuoy|13030403", leaf, re.I)),
    "template_garbage": sum(
        leaf.count(x)
        for x in ["else {", "@@if", "@@else", "undefined", "null", "[object Object]"]
    ),
    "duplicate_ids": 0,
}

ids = re.findall(r'id="([^"]+)"', leaf)
seen = {}
for i in ids:
    seen[i] = seen.get(i, 0) + 1
checks["duplicate_ids"] = sum(1 for c in seen.values() if c > 1)

refs = [
    ("index.html", dist / "index.html"),
    ("uslugi.html", dist / "uslugi.html"),
    ("uslugi-v2.html", dist / "uslugi-v2.html"),
    ("usluga-podrazdel-v1.html", dist / "usluga-podrazdel-v1.html"),
]
regression = {}
for name, path in refs:
    regression[name] = hashlib.sha256(path.read_bytes()).hexdigest()

out = {"checks": checks, "regression_sha256": regression}
out_path = Path(__file__).parent / "qa-results.json"
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(out, ensure_ascii=False, indent=2))
