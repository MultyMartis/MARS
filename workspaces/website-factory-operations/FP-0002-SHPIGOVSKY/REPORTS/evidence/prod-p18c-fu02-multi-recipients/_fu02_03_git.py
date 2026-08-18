# -*- coding: utf-8 -*-
"""P18C-FU02 git checkpoint via isolated worktree. Dirty main untouched. Commit + push."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DIRTY = Path(r"X:\AI MARS")
SRC = DIRTY / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"
EV = SRC / "REPORTS/evidence/prod-p18c-fu02-multi-recipients"
REPO = Path(r"X:\AI MARS STORAGE\git-sync-fp0002-p14-20260816-173714\repo")
REL_FP = "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"
REL_FW = "projects/mars-website-factory/subsystems/forge-wordpress"

FP_FILES = [
    "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Mail/MailOps.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Admin/MailFormsSettings.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Admin/ActivityLog.php",
    "WORDPRESS/plugins/shpigovsky-core/src/Forms/ConsultationHandler.php",
    "WORDPRESS/plugins/shpigovsky-core/assets/js/mail-forms-admin.js",
    "WORDPRESS/plugins/shpigovsky-core/assets/css/mail-forms-admin.css",
    "PROJECT-STATUS.md",
    "REPORTS/REPORT-FP-0002-PROD-P18C-FU02-MULTI-RECIPIENTS.md",
    "REPORTS/OPEN-ITEMS-FP-0002-AFTER-P18C-FU02.md",
    "REPORTS/BASELINE-FP-0002-PRODUCTION-POST-P13.md",
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

FORMS_NEEDLE = "*FW-S-13 v1.3 — P18C lead registry + Admin SMTP owner; P18C-FU01 discoverability.*"
FORMS_INSERT = """
## 13. MULTI-RECIPIENT MAIL SETTINGS

Canonical pattern (not CRM routing):

- Recipients are a **bounded repeating configuration list** (practical cap e.g. 20).
- Each row: email + optional label.
- Admin **Add** / **Remove** controls; do not expose raw JSON/serialized storage.
- Server-side validation: trim, `is_email`, drop blank rows, reject invalid non-empty emails.
- Deduplicate case-insensitively; keep the first occurrence and its label.
- First recipient = primary; additional recipients are copies of the same mail operation.
- Configuration readiness requires **≥1 valid recipient** plus required SMTP fields and a configured password.
- Recipient editing must **never** touch the SMTP secret (blank password keeps the existing secret).
- One form submission remains **one internal lead**, regardless of recipient count. One `wp_mail()` with a recipient array.

Evidence: FP-0002 P18C-FU02.

---

*FW-S-13 v1.4 — P18C-FU02 multi-recipient Admin UX.*
"""

UX_NEEDLE = "*Admin UX standard v1.2 — curated editor + production dashboard/SoT + discoverability DoD. CMS pack: [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md).*"
UX_INSERT = """
### 10.8 Repeating configuration lists (mail recipients)

For bounded business lists such as form email recipients:

- Render rows (value + optional label) with **Add** and **Remove**.
- New rows get unique input indexes and remain keyboard-usable before save.
- Do not ask the operator to edit serialized/JSON blobs.
- Save/reload must persist the resulting list without wiping unrelated secrets.

| # | Check |
|---|--------|
| 17 | Repeating settings lists have Add/Remove, server validation, and do not expose raw storage |

---

*Admin UX standard v1.3 — curated editor + production dashboard/SoT + discoverability DoD + repeating mail recipients. CMS pack: [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md).*
"""

AP_NEEDLE = "## CMS modeling namespace (`AP-CMS-*`)"
AP_INSERT = """## AP-030 — FORM-008 recipient list edits wipe the SMTP secret

| | |
|--|--|
| Symptom | Saving recipients or adding a row clears the stored mailbox password |
| Cause | Shared save handler treats a blank write-only password as “set empty”; or recipient POST omits SMTP fields and overwrites them |
| Risk | Silent mail failure; operator must re-enter the secret |
| Prevention | Blank password keeps existing secret; recipient save must not call password clear; never render the secret |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §7 and §13 |
| Evidence | FP-0002 P18C-FU02 |

---

"""

AP_FOOTER_OLD = "*FW-S-21 v1.5 — 29 operational anti-patterns (AP-022–028 = FORM-001–007; AP-029 Admin discoverability) + AP-CMS-001–016 index. Add IDs; do not reuse numbers.*"
AP_FOOTER_NEW = "*FW-S-21 v1.6 — 30 operational anti-patterns (AP-022–028 = FORM-001–007; AP-029 Admin discoverability; AP-030 recipient save vs SMTP secret) + AP-CMS-001–016 index. Add IDs; do not reuse numbers.*"


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


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"needle missing in {path}: {old[:80]}")
    if text.count(old) != 1:
        raise RuntimeError(f"needle not unique in {path}: {old[:80]}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def insert_before(path: Path, needle: str, block: str) -> None:
    replace_once(path, needle, block + needle)


def patch_fw(repo: Path) -> list[str]:
    base = repo / REL_FW
    changed = []

    forms = base / "standards/FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md"
    replace_once(forms, FORMS_NEEDLE, FORMS_INSERT.strip() + "\n")
    changed.append(f"{REL_FW}/standards/FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md")

    ux = base / "standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md"
    replace_once(ux, UX_NEEDLE, UX_INSERT.strip() + "\n")
    changed.append(f"{REL_FW}/standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md")

    ap = base / "standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md"
    insert_before(ap, AP_NEEDLE, AP_INSERT)
    replace_once(ap, AP_FOOTER_OLD, AP_FOOTER_NEW)
    changed.append(f"{REL_FW}/standards/FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md")

    idx = base / "knowledge/FP-0002-KNOWLEDGE-ASSIMILATION-INDEX.md"
    replace_once(
        idx,
        "| P18C-FU01 | Menu discoverability: Почта и формы visible under ACF Site Settings parent | `REPORT-FP-0002-PROD-P18C-FU01-ADMIN-MENU.md` |",
        "| P18C-FU01 | Menu discoverability: Почта и формы visible under ACF Site Settings parent | `REPORT-FP-0002-PROD-P18C-FU01-ADMIN-MENU.md` |\n"
        "| P18C-FU02 | Multi-recipient mail settings Add/Remove UX; SMTP secret preserved | `REPORT-FP-0002-PROD-P18C-FU02-MULTI-RECIPIENTS.md` |",
    )
    changed.append(f"{REL_FW}/knowledge/FP-0002-KNOWLEDGE-ASSIMILATION-INDEX.md")

    harvest = base / "knowledge/FP-0002-KNOWLEDGE-HARVEST-MAP.md"
    replace_once(
        harvest,
        "| Final | Persist lead before mail; Admin SMTP owner; suppress until VERIFIED+ACTIVE; `noreply@<domain>` |\n"
        "| Lesson | Email is transport, not the record that a form submission existed. Saving SMTP fields ≠ verified. Password never rendered/logged/Git. |\n"
        "| Class | D |\n"
        "| Evidence | P15; P17-FU02; P18C |",
        "| Final | Persist lead before mail; Admin SMTP owner; suppress until VERIFIED+ACTIVE; `noreply@<domain>`; bounded multi-recipient list with Add/Remove |\n"
        "| Lesson | Email is transport, not the record that a form submission existed. Saving SMTP fields ≠ verified. Password never rendered/logged/Git. Recipient edits must not wipe the SMTP secret. One submission = one lead. |\n"
        "| Class | D |\n"
        "| Evidence | P15; P17-FU02; P18C; P18C-FU02 |",
    )
    changed.append(f"{REL_FW}/knowledge/FP-0002-KNOWLEDGE-HARVEST-MAP.md")

    readme = base / "knowledge/README.md"
    text = readme.read_text(encoding="utf-8")
    marker = "*WP Forge knowledge hub — 2026-08-18."
    if marker in text:
        readme.write_text(
            text.replace(
                marker,
                "*WP Forge knowledge hub — 2026-08-19 (P18C-FU02 multi-recipient mail settings).",
                1,
            ),
            encoding="utf-8",
        )
        changed.append(f"{REL_FW}/knowledge/README.md")

    return changed


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
        rel = f"REPORTS/evidence/prod-p18c-fu02-multi-recipients/{src.name}"
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
        copy_file(EV / extra, dest_fp / "REPORTS/evidence/prod-p18c-fu02-multi-recipients" / extra)
        run(
            ["git", "add", "--", f"{REL_FP}/REPORTS/evidence/prod-p18c-fu02-multi-recipients/{extra}"],
            cwd=str(REPO),
        )

    run(
        ["git", "commit", "-m", "FP-0002: support multiple form email recipients"],
        cwd=str(REPO),
    )
    sha1 = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    print("COMMIT1", sha1)

    fw_copied = patch_fw(REPO)
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
            ["git", "commit", "-m", "WP Forge: define multi-recipient mail settings pattern"],
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
            "FP-0002: support multiple form email recipients",
            "WP Forge: define multi-recipient mail settings pattern",
        ],
        "secret_scan": "PASS",
        "dirty_main_untouched": True,
        "worktree": str(REPO),
        "base_before": base,
        "utc": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
    }
    (EV / "GIT-CHECKPOINT.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    copy_file(EV / "GIT-CHECKPOINT.json", dest_fp / "REPORTS/evidence/prod-p18c-fu02-multi-recipients/GIT-CHECKPOINT.json")
    run(
        ["git", "add", "--", f"{REL_FP}/REPORTS/evidence/prod-p18c-fu02-multi-recipients/GIT-CHECKPOINT.json"],
        cwd=str(REPO),
    )
    run(["git", "commit", "-m", "FP-0002: record P18C-FU02 git checkpoint"], cwd=str(REPO))
    sha3 = run(["git", "rev-parse", "HEAD"], cwd=str(REPO)).stdout.strip()
    run(["git", "push", "origin", "HEAD:mars/canonical-post-recovery"], cwd=str(REPO))
    remote = run(["git", "rev-parse", "origin/mars/canonical-post-recovery"], cwd=str(REPO)).stdout.strip()
    evidence["commits"] = [sha1, sha2, sha3]
    evidence["remote"] = remote
    evidence["messages"].append("FP-0002: record P18C-FU02 git checkpoint")
    (EV / "GIT-CHECKPOINT.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print("REMOTE", remote)
    print("COMMITS", sha1, sha2, sha3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
