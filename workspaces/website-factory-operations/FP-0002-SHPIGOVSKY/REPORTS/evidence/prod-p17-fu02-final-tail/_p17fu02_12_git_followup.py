# -*- coding: utf-8 -*-
"""Follow-up git checkpoint: dashboard SHA evidence. No reset. Dirty main untouched."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

SRC = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = SRC / "REPORTS/evidence/prod-p17-fu02-final-tail"
REPO = Path(r"X:\AI MARS STORAGE\git-sync-fp0002-p14-20260816-173714\repo")
REL_ROOT = "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"

FOLLOW = [
    "REPORTS/BASELINE-FP-0002-PRODUCTION-POST-P13.md",
    "REPORTS/REPORT-FP-0002-PROD-P17-FU02-FINAL-PRE-CUTOVER-TAIL.md",
    "REPORTS/evidence/prod-p17-fu02-final-tail/GIT-CHECKPOINT.json",
    "REPORTS/evidence/prod-p17-fu02-final-tail/METACODE-META-AFTER-GIT.json",
    "REPORTS/evidence/prod-p17-fu02-final-tail/_p17fu02_11_meta_git.py",
    "REPORTS/evidence/prod-p17-fu02-final-tail/_p17fu02_12_git_followup.py",
]

REAL_SECRET = re.compile(
    r"""(?ix)
    (?<![\w.])
    (password|passwd|secret|token|api[_-]?key|wordpress_password|db_password|ssh_password|ftp_or_sftp_password)
    \s*[:=]\s*
    ['\"]([^'\"\n{]{12,})['\"]
    """
)


def run(cmd, cwd=None, check=True):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and p.returncode != 0:
        raise RuntimeError((p.stderr or "")[-2000:] + (p.stdout or "")[-2000:])
    return p


def main() -> int:
    dest_root = REPO / REL_ROOT
    copied = []
    hits = []
    for rel in FOLLOW:
        src = SRC / Path(*rel.split("/"))
        if not src.exists():
            print("MISSING", rel)
            return 2
        text = src.read_text(encoding="utf-8", errors="replace")
        for m in REAL_SECRET.finditer(text):
            hits.append({"path": rel, "key": m.group(1)})
        dest = dest_root / Path(*rel.split("/"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.resolve() != dest.resolve():
            shutil.copy2(src, dest)
        copied.append(rel)
        run(["git", "add", "--", f"{REL_ROOT}/{rel}"], cwd=str(REPO))

    scan = {
        "pass": not hits,
        "hits": hits,
        "staged_count": len(copied),
        "utc": datetime.now(timezone.utc).isoformat(),
        "token": "P17-FU02 FOLLOWUP SECRET SCAN = PASS" if not hits else "P17-FU02 FOLLOWUP SECRET SCAN = FAIL",
    }
    (EV / "GIT-SECRET-SCAN-FOLLOWUP.json").write_text(json.dumps(scan, indent=2) + "\n", encoding="utf-8")
    dest_scan = dest_root / "REPORTS/evidence/prod-p17-fu02-final-tail/GIT-SECRET-SCAN-FOLLOWUP.json"
    shutil.copy2(EV / "GIT-SECRET-SCAN-FOLLOWUP.json", dest_scan)
    run(
        ["git", "add", "--", f"{REL_ROOT}/REPORTS/evidence/prod-p17-fu02-final-tail/GIT-SECRET-SCAN-FOLLOWUP.json"],
        cwd=str(REPO),
    )
    if hits:
        print("SECRET SCAN FAIL", hits)
        return 3

    staged = run(["git", "diff", "--cached", "--name-only"], cwd=str(REPO)).stdout.strip().splitlines()
    print("STAGED", len(staged))
    for s in staged:
        print(" ", s)
    if not staged:
        print("nothing to commit")
        return 0

    run(["git", "commit", "-m", "docs(fp-0002): record P17-FU02 git checkpoint"], cwd=str(REPO))
    sha = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    run(["git", "push", "origin", "HEAD:mars/canonical-post-recovery"], cwd=str(REPO))
    remote = run(["git", "rev-parse", "origin/mars/canonical-post-recovery"], cwd=str(REPO)).stdout.strip()
    follow_ev = {
        "commit": sha,
        "remote": remote,
        "message": "docs(fp-0002): record P17-FU02 git checkpoint",
        "parent": "16706398f03825b054ce75c56e8af48ec4349329",
        "secret_scan": "PASS",
        "dirty_main_untouched": True,
        "utc": datetime.now(timezone.utc).isoformat(),
        "ns_switched": False,
    }
    (EV / "GIT-CHECKPOINT-FOLLOWUP.json").write_text(json.dumps(follow_ev, indent=2) + "\n", encoding="utf-8")
    print("FOLLOWUP", sha, remote)
    return 0 if sha == remote else 2


if __name__ == "__main__":
    raise SystemExit(main())
