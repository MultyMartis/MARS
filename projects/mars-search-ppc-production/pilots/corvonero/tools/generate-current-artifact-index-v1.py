#!/usr/bin/env python3
"""Generate Corvonero current artifact index with checksums."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
STORAGE = Path(r"X:\AI MARS STORAGE")
BACKUP = STORAGE / "backups" / "search-ppc" / "CORVONERO-POST-PROJECT-CLOSURE-PRECHANGE-2026-07-01-200834"

def sha(p: Path) -> str | None:
    if not p.exists():
        return None
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()

entries = []

def add(**kw):
    p = Path(kw.pop("physical_path"))
    if p.is_file():
        kw["checksum"] = sha(p)
    else:
        kw["checksum"] = None
    kw["physical_path"] = str(p).replace("\\", "/")
    entries.append(kw)

# Authority
add(
    artifact_id="CORVONERO-SEMANTIC-AUTHORITY-V2.6",
    project_id="corvonero", artifact_family="SEMANTIC_AUTHORITY", version="V2.6",
    status="CURRENT", audience="OPERATOR", repository_reference="pilots/corvonero/CORVONERO-CAMPAIGN-V2.6-FINAL-PHRASE-AUTHORITY-v1.json",
    physical_path=REPO / "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CAMPAIGN-V2.6-FINAL-PHRASE-AUTHORITY-v1.json",
    current=True, protected=True, manual_stable=False, safe_to_send=False, safe_to_import=False, safe_to_publish=False,
    supersedes="V2.1-V2.5", superseded_by=None,
    notes="Semantic authority frozen; operator approved 2026-06-30",
)

# Deployable
pkg = STORAGE / "exports/corvonero/CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30"
add(
    artifact_id="CORVONERO-DEPLOYABLE-V2.6.2",
    project_id="corvonero", artifact_family="DEPLOYABLE_COMMANDER_PACKAGE", version="V2.6.2",
    status="CURRENT", audience="OPERATOR",
    repository_reference="pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.2-RELEASE-GATE-RESULT-v1.json",
    physical_path=pkg,
    current=True, protected=True, manual_stable=False, safe_to_send=False, safe_to_import=True, safe_to_publish=False,
    supersedes="V2.6.1", superseded_by=None,
    notes="Release gate PASS; Commander import not yet executed",
)

# Client pack files
client = STORAGE / "exports/corvonero/CORVONERO-CLIENT-APPROVAL-PACK-2026-07-01"
for fn, fam, sent in [
    ("01-CORVONERO-ADS-FOR-CLIENT-APPROVAL-v1.xlsx", "CLIENT_APPROVAL_PACK", True),
    ("02-CORVONERO-CAMPAIGN-STRATEGY-AND-RESEARCH-v1.html", "CLIENT_APPROVAL_PACK", True),
    ("03-CORVONERO-SEMANTIC-APPENDIX-v1.xlsx", "CLIENT_APPROVAL_PACK", True),
]:
    manual = "MANUAL_STABLE" if fn.endswith(".html") else "CLIENT_SENT"
    add(
        artifact_id=f"CORVONERO-CLIENT-{fn[:30]}",
        project_id="corvonero", artifact_family=fam, version="v1",
        status=manual, audience="CLIENT",
        repository_reference=None,
        physical_path=client / fn,
        current=True, protected=True, manual_stable=fn.endswith(".html"),
        safe_to_send=False, safe_to_import=False, safe_to_publish=False,
        supersedes=None, superseded_by=None,
        notes="SENT — FEEDBACK PENDING" if sent else "",
    )

# Final landing texts
final = STORAGE / "exports/corvonero/CORVONERO-FINAL-LANDING-PAGES-TEXT-DOCX-PACK-2026-07-01"
for fn in sorted(final.glob("*.docx")):
    add(
        artifact_id=f"CORVONERO-FINAL-{fn.stem[:40]}",
        project_id="corvonero", artifact_family="FINAL_PAGE_COPY", version="v1",
        status="CLIENT_SENT", audience="CLIENT",
        repository_reference=None, physical_path=fn,
        current=True, protected=True, manual_stable=False,
        safe_to_send=False, safe_to_import=False, safe_to_publish=False,
        supersedes=None, superseded_by=None, notes="SENT — FEEDBACK PENDING",
    )

# Roman briefs
roman = STORAGE / "exports/corvonero/CORVONERO-ROMAN-LANDING-PAGES-DOCX-PACK-2026-07-01"
for fn in sorted(roman.glob("*.docx")):
    add(
        artifact_id=f"CORVONERO-ROMAN-{fn.stem[:40]}",
        project_id="corvonero", artifact_family="IMPLEMENTATION_PRODUCTION_BRIEF", version="v1",
        status="ROMAN_SENT", audience="DEVELOPER",
        repository_reference=None, physical_path=fn,
        current=True, protected=True, manual_stable=False,
        safe_to_send=False, safe_to_import=False, safe_to_publish=False,
        supersedes=None, superseded_by=None, notes="SENT — FEEDBACK PENDING",
    )

# Historical superseded packages
for ver in ["V2.6.1", "V2.6", "V2.5", "V2.4", "V2.3", "V2.2", "V2.1"]:
    d = STORAGE / "exports/corvonero" / f"CORVONERO-CAMPAIGN-{ver}-FINAL-2026-06-30"
    if d.exists():
        entries.append({
            "artifact_id": f"CORVONERO-HISTORICAL-{ver}",
            "project_id": "corvonero", "artifact_family": "DEPLOYABLE_COMMANDER_PACKAGE", "version": ver,
            "status": "HISTORICAL_SUPERSEDED", "audience": "OPERATOR",
            "physical_path": str(d).replace("\\", "/"),
            "repository_reference": None, "current": False, "protected": True, "manual_stable": False,
            "safe_to_send": False, "safe_to_import": False, "safe_to_publish": False,
            "supersedes": None, "superseded_by": "V2.6.2" if ver != "V2.6.2" else None,
            "checksum": None, "notes": "DO NOT IMPORT",
        })

entries.append({
    "artifact_id": "CORVONERO-PRE-CLOSURE-BACKUP",
    "project_id": "corvonero", "artifact_family": "BACKUP", "version": "v1",
    "status": "CURRENT", "audience": "OPERATOR",
    "physical_path": str(BACKUP).replace("\\", "/"),
    "repository_reference": None, "current": True, "protected": True, "manual_stable": False,
    "safe_to_send": False, "safe_to_import": False, "safe_to_publish": False,
    "supersedes": None, "superseded_by": None, "checksum": None,
    "notes": "BACKUP_VERIFIED true — 2026-07-01",
})

doc = {
    "schema_version": "corvonero-current-artifact-index-v1",
    "project_id": "corvonero",
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "semantic_authority": "V2.6",
    "deployable_package": "V2.6.2",
    "client_state": "CLIENT_FEEDBACK_PENDING",
    "totals": {"campaigns": 10, "groups": 71, "ads": 71, "phrase_slots": 926, "keep": 487, "reject": 271, "move": 2},
    "entries": entries,
}

out_json = REPO / "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CURRENT-ARTIFACT-INDEX-v1.json"
out_md = REPO / "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CURRENT-ARTIFACT-INDEX-v1.md"
out_json.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

lines = [
    "# Corvonero current artifact index v1",
    "",
    f"**Updated:** {doc['updated_at']}",
    f"**Authority:** V2.6 | **Deployable:** V2.6.2 | **Client state:** CLIENT_FEEDBACK_PENDING",
    "",
    "| Artifact | Version | Status | Path | Safe import | Safe publish |",
    "|----------|---------|--------|------|-------------|--------------|",
]
for e in entries:
    if e.get("current"):
        lines.append(
            f"| {e['artifact_id']} | {e['version']} | {e['status']} | `{e['physical_path']}` | "
            f"{e.get('safe_to_import', False)} | {e.get('safe_to_publish', False)} |"
        )
lines += ["", "## Historical / superseded", ""]
for e in entries:
    if not e.get("current"):
        lines.append(f"- **{e['artifact_id']}** ({e['version']}): {e['notes']}")
out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Wrote {len(entries)} entries")
