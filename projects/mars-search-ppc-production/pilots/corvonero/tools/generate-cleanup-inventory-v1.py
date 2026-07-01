#!/usr/bin/env python3
"""Generate Corvonero cleanup candidate inventory (plan only — no deletion)."""
import json
from datetime import datetime, timezone
from pathlib import Path

EXPORTS = Path(r"X:\AI MARS STORAGE\exports\corvonero")
REPO = Path(r"X:\AI MARS")

CURRENT = {
    "CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30",
    "CORVONERO-CLIENT-APPROVAL-PACK-2026-07-01",
    "CORVONERO-FINAL-LANDING-PAGES-TEXT-DOCX-PACK-2026-07-01",
    "CORVONERO-ROMAN-LANDING-PAGES-DOCX-PACK-2026-07-01",
}
HISTORICAL_KEEP = {
    "CORVONERO-CAMPAIGN-V2.6-FINAL-2026-06-30",
    "CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30",
}
SUPERSEDED = {
    "CORVONERO-CAMPAIGN-V2.1-FINAL-2026-06-30",
    "CORVONERO-CAMPAIGN-V2.5-CURATED-CORE-REVIEW-2026-06-30",
    "CORVONERO-CAMPAIGN-V2.4-FINAL-AUTHORITY-REVIEW-2026-06-30",
    "CORVONERO-CAMPAIGN-V2.3-CORRECTED-AUDIT-REVIEW-2026-06-30",
    "CORVONERO-CAMPAIGN-V2.2-STRICT-AUDIT-REVIEW-2026-06-30",
    "CORVONERO-CAMPAIGN-V2-PASS1-REVIEW-2026-06-30",
    "CORVONERO-CAMPAIGN-V2-PASS2-OPERATOR-REVIEW-2026-06-30",
    "CORVONERO-CAMPAIGN-V2-FINAL-2026-06-30",
}

candidates = []
for p in sorted(EXPORTS.iterdir()):
    if not p.is_dir():
        if p.name.startswith("_") or p.suffix in (".mjs", ".txt", ".py"):
            candidates.append({
                "path": str(p).replace("\\", "/"),
                "classification": "DELETE_CANDIDATE",
                "reason": "Debug/temp file at exports root",
                "superseding_artifact": None,
                "risk": "low",
                "operator_approval_required": True,
            })
        continue
    name = p.name
    if name in CURRENT:
        cls = "KEEP_CURRENT_DELIVERY"
    elif name in HISTORICAL_KEEP:
        cls = "KEEP_HISTORICAL"
    elif name in SUPERSEDED or "V2." in name and name not in CURRENT:
        cls = "ARCHIVE_LATER"
    elif "COMMANDER-CT" in name or "IMPORT-CANDIDATE" in name or "REVIEW" in name or "ADS-" in name:
        cls = "ARCHIVE_LATER"
    elif "EXPORT-WAVE" in name or "LANDING-PAGES-ROMAN-2026-06" in name:
        cls = "ARCHIVE_LATER"
    else:
        cls = "UNKNOWN_REVIEW"
    candidates.append({
        "path": str(p).replace("\\", "/"),
        "classification": cls,
        "reason": f"Storage export directory — {'current delivery' if cls == 'KEEP_CURRENT_DELIVERY' else 'superseded or review wave'}",
        "superseding_artifact": "CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30" if cls == "ARCHIVE_LATER" else None,
        "risk": "medium" if cls == "DELETE_CANDIDATE" else "low",
        "operator_approval_required": cls in ("DELETE_CANDIDATE", "ARCHIVE_LATER"),
    })

# Repo debug outputs
for rel in [
    "projects/mars-search-ppc-production/.tools-test-output",
    "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-V2.6.1-MISSING-SLOTS.csv",
]:
    fp = REPO / rel
    if fp.exists():
        candidates.append({
            "path": str(fp).replace("\\", "/"),
            "classification": "DELETE_CANDIDATE",
            "reason": "Debug/reconciliation temp output — evidence captured in JSON reports",
            "superseding_artifact": "CORVONERO-CAMPAIGN-V2.6.2-PHRASE-SLOT-RECONCILIATION-v1.json",
            "risk": "low",
            "operator_approval_required": True,
        })

doc = {
    "schema_version": "corvonero-cleanup-candidate-inventory-v1",
    "project_id": "corvonero",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "note": "PLAN ONLY — no deletion/move/archive executed in closure task",
    "candidate_count": len(candidates),
    "candidates": candidates,
}

out_json = REPO / "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CLEANUP-CANDIDATE-INVENTORY-v1.json"
out_md = REPO / "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CLEANUP-CANDIDATE-INVENTORY-v1.md"
out_json.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

by_cls = {}
for c in candidates:
    by_cls.setdefault(c["classification"], []).append(c)

lines = [
    "# Corvonero cleanup candidate inventory v1",
    "",
    "**PLAN ONLY** — no deletion performed.",
    "",
    f"**Candidates:** {len(candidates)}",
    "",
]
for cls, items in sorted(by_cls.items()):
    lines.append(f"## {cls} ({len(items)})")
    lines.append("")
    for i in items[:15]:
        lines.append(f"- `{i['path']}` — {i['reason']}")
    if len(items) > 15:
        lines.append(f"- ... and {len(items) - 15} more")
    lines.append("")
out_md.write_text("\n".join(lines), encoding="utf-8")
print(len(candidates))
