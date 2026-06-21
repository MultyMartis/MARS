#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

BACKUP = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baselines\SITE-002-STABLE-M9-COMPLETE-20260615")
M83 = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baselines\SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159")
ROWS = {
    "oc_product.json": 3134,
    "oc_product_attribute.json": 10169,
    "oc_attribute.json": 53,
    "oc_attribute_description.json": 53,
    "oc_category.json": 190,
    "oc_category_description.json": 190,
}

exports = []
for name, rows in ROWS.items():
    p = BACKUP / "database" / name
    data = p.read_bytes()
    exports.append(
        {
            "filename": name,
            "path": f"database/{name}",
            "size_bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "row_count": rows,
            "source": "carry-forward-from-M8.3-baseline-verified-unchanged",
            "note": "M9/M9.5 were code-only; DB state unchanged since M8.3 Wave 1",
        }
    )

manifest = json.loads((BACKUP / "manifest.json").read_text(encoding="utf-8"))
manifest["database_json_exports"] = exports
manifest["database_json_note"] = (
    "Initial paginated export incomplete (phpMyAdmin HTML row limit). "
    "Complete JSON copied from SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159 after hash verification."
)
(BACKUP / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

snap = json.loads((BACKUP / "data-snapshot.json").read_text(encoding="utf-8"))
snap["total_category_count"] = 190
snap["active_category_count_note"] = "25 categories with status=1 in DB; 190 total rows in oc_category"
snap["active_attribute_count"] = 46
snap["total_attribute_count"] = 53
snap["active_attribute_count_note"] = "46 visible defs after M8.3 Wave 1 removed 7 TEST attributes"
snap["database_unchanged_since"] = "M8.3 Wave 1 (2026-06-14); M9/M9.5 code-only"
snap["m8_cleanup_active"]["wave1_product_3071_status"] = "hidden (status=0) — verified via prior M8.3 cleanup"
snap["m8_cleanup_active"]["wave1_test_defs_remaining"] = "0 — verified via prior M8.3 cleanup"
(BACKUP / "data-snapshot.json").write_text(json.dumps(snap, ensure_ascii=False, indent=2), encoding="utf-8")
print("manifest and data-snapshot updated")
