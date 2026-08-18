# -*- coding: utf-8 -*-
"""P18C-FU01 git checkpoint via isolated worktree. Dirty main untouched. Two commits + push."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DIRTY = Path(r"X:\AI MARS")
SRC = DIRTY / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"
EV = SRC / "REPORTS/evidence/prod-p18c-fu01-admin-menu"
REPO = Path(r"X:\AI MARS STORAGE\git-sync-fp0002-p14-20260816-173714\repo")
REL_FP = "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"
REL_FW = "projects/mars-website-factory/subsystems/forge-wordpress"

FP_FILES = [
    "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Admin/MailFormsSettings.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Admin/OptionsPage.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
    "PROJECT-STATUS.md",
    "REPORTS/REPORT-FP-0002-PROD-P18C-FU01-ADMIN-MENU.md",
    "REPORTS/OPEN-ITEMS-FP-0002-AFTER-P18C-FU01.md",
    "REPORTS/BASELINE-FP-0002-PRODUCTION-POST-P13.md",
    "REPORTS/RUNBOOK-FP-0002-PROD-P18-FINAL-DOMAIN-CUTOVER.md",
]

FW_FILES = [
    "standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md",
    "standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md",
    "standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md",
    "standards/FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md",
    "standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md",
    "standards/FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md",
    "knowledge/FP-0002-KNOWLEDGE-ASSIMILATION-INDEX.md",
    "knowledge/FP-0002-KNOWLEDGE-HARVEST-MAP.md",
    "knowledge/README.md",
    "OPERATIONAL-INDEX.md",
]

SKIP_EV_PREFIXES = ("GIT-CHECKPOINT",)
SKIP_EV_NAMES = {"GIT-STAGED-PATHS-FP.txt", "GIT-STAGED-PATHS-FW.txt"}

REAL_SECRET = re.compile(
    r"""(?ix)
    (?<![\w.])
    (password|passwd|secret|token|api[_-]?key|wordpress_password|db_password|ssh_password|ftp_or_sftp_password)
    \s*[:=]\s*
    ['\"]([^'\"\n{]{12,})['\"]
    """
)


def run(cmd, cwd=None, check=True):
    print("+", " ".join(cmd[:16]), ("..." if len(cmd) > 16 else ""))
    p = subprocess.run(
        cmd,
        cwd=cwd or str(DIRTY),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and p.returncode != 0:
        raise RuntimeError(f"fail\n{p.stdout[-2500:]}\n{p.stderr[-2500:]}")
    return p


def secret_scan(repo: Path, staged: list[str]) -> list[dict]:
    hits = []
    for rel in staged:
        fp = repo / rel
        if not fp.is_file():
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for m in REAL_SECRET.finditer(text):
            val = m.group(2)
            low = val.lower()
            if any(
                x in low
                for x in (
                    "operator",
                    "example",
                    "changeme",
                    "xxxx",
                    "***",
                    "redacted",
                    "placeholder",
                    "new-password",
                    "smtp_password",
                )
            ):
                continue
            if "пароль" in low or "укажите" in low:
                continue
            hits.append({"path": rel, "key": m.group(1), "value_len": len(val)})
    return hits


def copy_file(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    if not (REPO / ".git").exists():
        raise RuntimeError(f"missing worktree {REPO}")

    run(["git", "remote", "get-url", "origin"], cwd=str(REPO))
    run(["git", "fetch", "origin", "mars/canonical-post-recovery"], cwd=str(REPO))
    run(["git", "reset", "--hard", "origin/mars/canonical-post-recovery"], cwd=str(REPO))
    base = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    print("BASE", base)

    dest_fp = REPO / REL_FP
    copied = []
    for rel in FP_FILES:
        src = SRC / Path(*rel.split("/"))
        if not src.exists():
            print("MISSING", rel)
            continue
        copy_file(src, dest_fp / Path(*rel.split("/")))
        copied.append(rel)
        print("COPY", rel)

    for src in EV.iterdir():
        if not src.is_file():
            continue
        if src.name.startswith(SKIP_EV_PREFIXES):
            continue
        if src.name in SKIP_EV_NAMES:
            continue
        rel = f"REPORTS/evidence/prod-p18c-fu01-admin-menu/{src.name}"
        copy_file(src, dest_fp / Path(*rel.split("/")))
        copied.append(rel)

    paths = [f"{REL_FP}/{rel}" for rel in copied]
    run(["git", "add", "--"] + paths, cwd=str(REPO))
    staged = [
        x.replace("\\", "/")
        for x in run(["git", "diff", "--cached", "--name-only"], cwd=str(REPO)).stdout.splitlines()
        if x
    ]
    bad = [p for p in staged if not p.startswith(REL_FP + "/")]
    if bad:
        run(["git", "reset", "HEAD", "--"] + bad, cwd=str(REPO), check=False)
        staged = [
            x.replace("\\", "/")
            for x in run(["git", "diff", "--cached", "--name-only"], cwd=str(REPO)).stdout.splitlines()
            if x
        ]
    (EV / "GIT-STAGED-PATHS-FP.txt").write_text("\n".join(staged) + "\n", encoding="utf-8")
    hits = secret_scan(REPO, staged)
    scan1 = {"pass": len(hits) == 0, "hits": hits, "staged_count": len(staged), "wave": "fp-0002"}
    (EV / "GIT-SECRET-SCAN.json").write_text(json.dumps({"fp": scan1}, indent=2) + "\n", encoding="utf-8")
    print("SECRET1", "PASS" if scan1["pass"] else "FAIL", len(staged))
    if hits:
        print(hits[:20])
        return 3
    if not staged:
        return 4

    for extra in ("GIT-SECRET-SCAN.json", "GIT-STAGED-PATHS-FP.txt"):
        copy_file(EV / extra, dest_fp / "REPORTS/evidence/prod-p18c-fu01-admin-menu" / extra)
        run(
            ["git", "add", "--", f"{REL_FP}/REPORTS/evidence/prod-p18c-fu01-admin-menu/{extra}"],
            cwd=str(REPO),
        )

    run(
        ["git", "commit", "-m", "FP-0002: expose SMTP and forms settings in Admin"],
        cwd=str(REPO),
    )
    sha1 = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    print("COMMIT1", sha1)

    fw_copied = []
    dest_fw = REPO / REL_FW
    fw_src = DIRTY / REL_FW
    for rel in FW_FILES:
        src = fw_src / Path(*rel.split("/"))
        if not src.exists():
            print("MISSING FW", rel)
            continue
        copy_file(src, dest_fw / Path(*rel.split("/")))
        fw_copied.append(f"{REL_FW}/{rel}")
        print("COPY FW", rel)
    run(["git", "add", "--"] + fw_copied, cwd=str(REPO))
    staged2 = [
        x.replace("\\", "/")
        for x in run(["git", "diff", "--cached", "--name-only"], cwd=str(REPO)).stdout.splitlines()
        if x
    ]
    (EV / "GIT-STAGED-PATHS-FW.txt").write_text("\n".join(staged2) + "\n", encoding="utf-8")
    hits2 = secret_scan(REPO, staged2)
    scan = {"fp": scan1, "fw": {"pass": len(hits2) == 0, "hits": hits2, "staged_count": len(staged2)}}
    (EV / "GIT-SECRET-SCAN.json").write_text(json.dumps(scan, indent=2) + "\n", encoding="utf-8")
    print("SECRET2", "PASS" if not hits2 else "FAIL", len(staged2))
    if hits2:
        print(hits2[:20])
        return 3
    sha2 = sha1
    if staged2:
        run(
            ["git", "commit", "-m", "WP Forge: require Admin feature discoverability in acceptance"],
            cwd=str(REPO),
        )
        sha2 = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    print("COMMIT2", sha2)

    run(["git", "push", "origin", "HEAD:mars/canonical-post-recovery"], cwd=str(REPO))
    remote = run(["git", "rev-parse", "origin/mars/canonical-post-recovery"], cwd=str(REPO)).stdout.strip()

    evidence = {
        "commits": [sha1, sha2],
        "remote": remote,
        "messages": [
            "FP-0002: expose SMTP and forms settings in Admin",
            "WP Forge: require Admin feature discoverability in acceptance",
        ],
        "secret_scan": "PASS",
        "dirty_main_untouched": True,
        "worktree": str(REPO),
        "base_before": base,
        "utc": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
    }
    (EV / "GIT-CHECKPOINT.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    copy_file(EV / "GIT-CHECKPOINT.json", dest_fp / "REPORTS/evidence/prod-p18c-fu01-admin-menu/GIT-CHECKPOINT.json")
    run(
        ["git", "add", "--", f"{REL_FP}/REPORTS/evidence/prod-p18c-fu01-admin-menu/GIT-CHECKPOINT.json"],
        cwd=str(REPO),
    )
    run(["git", "commit", "-m", "FP-0002: record P18C-FU01 git checkpoint"], cwd=str(REPO))
    sha3 = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    run(["git", "push", "origin", "HEAD:mars/canonical-post-recovery"], cwd=str(REPO))
    remote = run(["git", "rev-parse", "origin/mars/canonical-post-recovery"], cwd=str(REPO)).stdout.strip()
    evidence["commits"] = [sha1, sha2, sha3]
    evidence["remote"] = remote
    evidence["messages"].append("FP-0002: record P18C-FU01 git checkpoint")
    (EV / "GIT-CHECKPOINT.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print("REMOTE", remote)
    print("COMMITS", sha1, sha2, sha3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
