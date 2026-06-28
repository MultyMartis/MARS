#!/usr/bin/env python3
"""Generate V8 tracking inventory for bootstrap reconciliation."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
AUDIT_DIR = WORKSPACE / "audits" / "bootstrap-reconciliation"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

EXCLUDE_DIRS = {"node_modules", "dist", "temp", "logs", ".cache", "coverage"}
EXCLUDE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".zip", ".log"}
REJECTED_PATTERNS = ("o-centre-v1.html", "o-centre", "about-page")


def classify(path: Path) -> dict:
    rel = path.relative_to(WORKSPACE).as_posix()
    parts = rel.split("/")
    excluded = False
    reason = ""

    for part in parts:
        if part in EXCLUDE_DIRS:
            excluded = True
            reason = f"runtime dir: {part}"
            break

    if not excluded and path.suffix.lower() in EXCLUDE_SUFFIXES:
        excluded = True
        reason = f"excluded extension: {path.suffix.lower()}"

    if any(p in rel for p in REJECTED_PATTERNS):
        excluded = True
        reason = reason or "rejected about pattern"

    if rel.startswith("src/"):
        ftype = "source"
    elif rel.startswith("foundation/"):
        ftype = "foundation"
    elif rel.startswith("docs/"):
        ftype = "docs"
    elif rel.startswith("audits/"):
        ftype = "audit"
    elif rel.startswith("plans/"):
        ftype = "plan"
    elif rel.startswith("tools/"):
        ftype = "tool"
    elif path.name in {"package.json", "package-lock.json", "gulpfile.js", ".gitignore"}:
        ftype = "build-config"
    elif rel == "README.md":
        ftype = "docs"
    else:
        ftype = "other"

    generated = path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"} or "dist/" in rel
    runtime = excluded and ("node_modules" in rel or "dist/" in rel or path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"})

    return {
        "path": rel,
        "type": ftype,
        "bytes": path.stat().st_size,
        "tracked_candidate": not excluded,
        "excluded": excluded,
        "exclusion_reason": reason or None,
        "generated": generated,
        "sensitive_runtime": runtime,
        "expected_git_status": "ignored" if excluded else "tracked",
    }


def main() -> None:
    entries = []
    for path in sorted(WORKSPACE.rglob("*")):
        if not path.is_file():
            continue
        entries.append(classify(path))

    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workspace": str(WORKSPACE),
        "total_files": len(entries),
        "source_files": sum(1 for e in entries if e["type"] == "source" and e["tracked_candidate"]),
        "foundation_docs": sum(1 for e in entries if e["type"] in {"foundation", "docs"} and e["tracked_candidate"]),
        "audits": sum(1 for e in entries if e["type"] == "audit" and e["tracked_candidate"]),
        "plans": sum(1 for e in entries if e["type"] == "plan" and e["tracked_candidate"]),
        "tools": sum(1 for e in entries if e["type"] == "tool" and e["tracked_candidate"]),
        "build_config": sum(1 for e in entries if e["type"] == "build-config"),
        "excluded_dist_files": sum(1 for e in entries if "dist/" in e["path"]),
        "excluded_node_modules_files": sum(1 for e in entries if "node_modules/" in e["path"]),
        "excluded_screenshot_files": sum(1 for e in entries if e["path"].lower().endswith((".png", ".jpg", ".jpeg", ".webp"))),
        "excluded_temp_log_files": sum(1 for e in entries if any(x in e["path"] for x in ("temp/", "logs/", ".cache/"))),
        "rejected_about_files": [e["path"] for e in entries if "o-centre-v1.html" in e["path"]],
        "tracked_candidates": sum(1 for e in entries if e["tracked_candidate"]),
    }

    payload = {"summary": summary, "files": entries}
    json_path = AUDIT_DIR / "V8-TRACKING-INVENTORY.json"
    md_path = AUDIT_DIR / "V8-TRACKING-INVENTORY.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# V8 Tracking Inventory",
        "",
        f"Generated: {summary['generated_at']}",
        "",
        "## Summary",
        "",
        f"- Total files scanned: {summary['total_files']}",
        f"- Tracked candidates: {summary['tracked_candidates']}",
        f"- Source files: {summary['source_files']}",
        f"- Foundation/docs: {summary['foundation_docs']}",
        f"- Audits: {summary['audits']}",
        f"- Plans: {summary['plans']}",
        f"- Tools: {summary['tools']}",
        f"- Build/config: {summary['build_config']}",
        f"- Excluded dist: {summary['excluded_dist_files']}",
        f"- Excluded node_modules: {summary['excluded_node_modules_files']}",
        f"- Excluded screenshots: {summary['excluded_screenshot_files']}",
        f"- Rejected About files: {len(summary['rejected_about_files'])}",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
