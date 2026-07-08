#!/usr/bin/env python3
"""SITE-002 post-1C strict garbage marker fixture regression (Run 4.228)."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(r"X:\AI MARS")
MONITOR_SCRIPT = REPO_ROOT / "projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py"
DEFAULT_OUT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01\verification\garbage-marker-fixture-results.json"
)


def main() -> int:
    parser = argparse.ArgumentParser(description="SITE-002 garbage marker fixture regression")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(MONITOR_SCRIPT), "--fixture-garbage-test", "--fixture-output", str(args.output)]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, encoding="utf-8")
    if proc.stdout:
        print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)
    if proc.returncode != 0:
        return proc.returncode
    payload = json.loads(args.output.read_text(encoding="utf-8"))
    md_path = args.output.with_suffix(".md")
    lines = [
        "# Garbage marker fixture regression",
        "",
        f"- Fixtures: **{payload['fixture_count']}**",
        f"- Passed: **{payload['passed']}**",
        f"- Failed: **{payload['failed']}**",
        "",
    ]
    for row in payload.get("results", []):
        status = "PASS" if row.get("pass") else "FAIL"
        lines.append(f"- `{row['id']}`: **{status}** (expect={row['expect_strict_hit']}, got={row['got_strict_hit']})")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0 if payload.get("failed", 1) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
