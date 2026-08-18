# -*- coding: utf-8 -*-
"""P17-FU02 git checkpoint via isolated worktree. Dirty main untouched."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DIRTY = Path(r"X:\AI MARS")
SRC = DIRTY / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"
EV = SRC / "REPORTS/evidence/prod-p17-fu02-final-tail"
REPO = Path(r"X:\AI MARS STORAGE\git-sync-fp0002-p14-20260816-173714\repo")
REL_ROOT = "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"

ALLOW_FIXED = [
    "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Forms/ConsultationHandler.php",
    "PROJECT-STATUS.md",
    "REPORTS/REPORT-FP-0002-PROD-P17-FU02-FINAL-PRE-CUTOVER-TAIL.md",
    "REPORTS/OPEN-ITEMS-FP-0002-AFTER-P17-FU02.md",
    "REPORTS/BASELINE-FP-0002-PRODUCTION-POST-P13.md",
    "REPORTS/RUNBOOK-FP-0002-PRE-CUTOVER-FREEZE.md",
    "REPORTS/RUNBOOK-FP-0002-MANUAL-NS-SWITCH-HANDOFF.md",
    "REPORTS/RUNBOOK-FP-0002-PROD-P18-FINAL-DOMAIN-CUTOVER.md",
    "DOCS/PRODUCTION/FP-0002-DNS-CUTOVER-STATUS-v1.md",
    "REPORTS/evidence/prod-p17-precutover/CUTOVER-RUNBOOK-P17.md",
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
    print("+", " ".join(cmd[:14]), ("..." if len(cmd) > 14 else ""))
    p = subprocess.run(
        cmd,
        cwd=cwd or str(DIRTY),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and p.returncode != 0:
        raise RuntimeError(f"fail\n{p.stdout[-2000:]}\n{p.stderr[-2000:]}")
    return p


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    if not (REPO / ".git").exists():
        raise RuntimeError(f"missing worktree {REPO}")

    run(["git", "remote", "get-url", "origin"], cwd=str(REPO))
    run(["git", "fetch", "origin", "mars/canonical-post-recovery"], cwd=str(REPO))
    run(["git", "reset", "--hard", "origin/mars/canonical-post-recovery"], cwd=str(REPO))
    base = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    print("BASE", base)

    dest_root = REPO / REL_ROOT
    copied = []
    for rel in ALLOW_FIXED:
        src = SRC / Path(*rel.split("/"))
        if not src.exists():
            print("MISSING", rel)
            continue
        dest = dest_root / Path(*rel.split("/"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied.append(rel)
        print("COPY", rel)

    for src in EV.iterdir():
        if not src.is_file():
            continue
        rel = f"REPORTS/evidence/prod-p17-fu02-final-tail/{src.name}"
        dest = dest_root / Path(*rel.split("/"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied.append(rel)
        print("COPY", rel)

    paths = [f"{REL_ROOT}/{rel}" for rel in copied]
    run(["git", "add", "--"] + paths, cwd=str(REPO))

    staged = [
        x.replace("\\", "/")
        for x in run(["git", "diff", "--cached", "--name-only"], cwd=str(REPO)).stdout.splitlines()
        if x
    ]
    bad = [p for p in staged if not p.startswith(REL_ROOT + "/")]
    if bad:
        run(["git", "reset", "HEAD", "--"] + bad, cwd=str(REPO), check=False)
        staged = [
            x.replace("\\", "/")
            for x in run(["git", "diff", "--cached", "--name-only"], cwd=str(REPO)).stdout.splitlines()
            if x
        ]

    (EV / "GIT-STAGED-PATHS.txt").write_text("\n".join(staged) + "\n", encoding="utf-8")

    hits = []
    for rel in staged:
        fp = REPO / rel
        if not fp.is_file():
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for m in REAL_SECRET.finditer(text):
            val = m.group(2)
            if any(
                x in val.lower()
                for x in ("operator", "example", "changeme", "xxxx", "***", "redacted", "placeholder")
            ):
                continue
            hits.append({"path": rel, "key": m.group(1), "value_len": len(val)})

    scan = {
        "pass": len(hits) == 0,
        "hits": hits,
        "staged_count": len(staged),
        "base": base,
        "utc": datetime.now(timezone.utc).isoformat(),
        "token": "P17-FU02 SECRET SCAN = PASS" if not hits else "P17-FU02 SECRET SCAN = FAIL",
    }
    (EV / "GIT-SECRET-SCAN.json").write_text(json.dumps(scan, indent=2) + "\n", encoding="utf-8")
    print("SECRET", "PASS" if scan["pass"] else "FAIL", "staged", len(staged))
    if hits:
        print(hits[:20])
        return 3
    if not staged:
        print("NO STAGED")
        return 4

    for extra in ("GIT-SECRET-SCAN.json", "GIT-STAGED-PATHS.txt"):
        src = EV / extra
        dest = dest_root / "REPORTS/evidence/prod-p17-fu02-final-tail" / extra
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        run(
            ["git", "add", "--", str(Path(REL_ROOT) / "REPORTS/evidence/prod-p17-fu02-final-tail" / extra)],
            cwd=str(REPO),
        )

    staged = [
        x.replace("\\", "/")
        for x in run(["git", "diff", "--cached", "--name-only"], cwd=str(REPO)).stdout.splitlines()
        if x
    ]
    (EV / "GIT-STAGED-PATHS.txt").write_text("\n".join(staged) + "\n", encoding="utf-8")

    msg = "FP-0002: close final pre-cutover tails"
    run(["git", "commit", "-m", msg], cwd=str(REPO))
    sha = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    run(["git", "push", "origin", "HEAD:mars/canonical-post-recovery"], cwd=str(REPO))
    remote = run(["git", "rev-parse", "origin/mars/canonical-post-recovery"], cwd=str(REPO)).stdout.strip()

    evidence = {
        "commit": sha,
        "remote": remote,
        "message": msg,
        "staged_count": len(staged),
        "secret_scan": "PASS",
        "dirty_main_untouched": True,
        "worktree": str(REPO),
        "base_before": base,
        "utc": datetime.now(timezone.utc).isoformat(),
        "ns_switched": False,
    }
    (EV / "GIT-CHECKPOINT.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print("COMMIT", sha)
    print("REMOTE", remote)
    return 0 if sha == remote else 2


if __name__ == "__main__":
    raise SystemExit(main())
