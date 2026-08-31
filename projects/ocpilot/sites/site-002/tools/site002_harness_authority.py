"""SITE-002 harness authority resolution (shared helper).

Authority model (2026-08-31 reconciliation):
- Canonical source/docs: ``X:\\AI MARS`` — read-only git/filesystem OK with foreign WIP.
- Git mutation / scoped canonicalization: requires an explicit **clean** worktree via
  ``--repo-root`` (fresh ``X:\\AI MARS STORAGE\\git-sync-<label>\\repo``); never hardcode
  a disposable sync contour name.
- Runtime scheduled jobs: ``X:\\AI MARS STORAGE\\runtime-checkouts\\...``
- Production deploy authority: Beget/server-side runtime (not local temp Git worktrees).

See ``client-ops/storage-hygiene/LEGACY-HARNESS-AUTHORITY-RECONCILIATION-2026-08-31.md``.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

CANONICAL_MONOREPO = Path(r"X:\AI MARS")
SITE002_REL = Path("projects/ocpilot/sites/site-002")
RUNTIME_CHECKOUTS_ROOT = Path(r"X:\AI MARS STORAGE\runtime-checkouts")
DEFAULT_MONITOR_CHECKOUT = RUNTIME_CHECKOUTS_ROOT / "site-002-monitor" / "repo"

HISTORICAL_DOC = (
    "projects/ocpilot/sites/site-002/client-ops/storage-hygiene/"
    "LEGACY-HARNESS-AUTHORITY-RECONCILIATION-2026-08-31.md"
)


def site002_tools_dir(repo_root: Path | None = None) -> Path:
    root = repo_root or CANONICAL_MONOREPO
    return root / SITE002_REL / "tools"


def site002_reports_dir(repo_root: Path | None = None) -> Path:
    root = repo_root or CANONICAL_MONOREPO
    return root / SITE002_REL / "reports"


def is_disposable_sync_path(path: Path) -> bool:
    normalized = str(path.resolve()).lower().replace("/", "\\")
    return "git-sync-" in normalized or "git-reconcile-" in normalized


def git_worktree_is_clean(repo_root: Path) -> bool:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root), "status", "--porcelain"],
            text=True,
            stderr=subprocess.STDOUT,
        )
        return out.strip() == ""
    except (subprocess.CalledProcessError, OSError):
        return False


def resolve_repo_root_for_read(
    cli_repo_root: str | None = None,
    *,
    env_var: str = "SITE002_REPO_ROOT",
) -> Path:
    """Read-only git/filesystem authority — defaults to canonical monorepo."""
    if cli_repo_root:
        root = Path(cli_repo_root).resolve()
    else:
        env = os.environ.get(env_var, "").strip()
        root = Path(env).resolve() if env else CANONICAL_MONOREPO.resolve()
    if not root.is_dir():
        raise SystemExit(f"ERROR: repo root does not exist: {root}")
    if is_disposable_sync_path(root):
        raise SystemExit(
            f"ERROR: disposable git-sync/git-reconcile path must not be used as authority: {root}\n"
            "For read-only use canonical X:\\AI MARS or pass an existing clean worktree explicitly."
        )
    return root


def resolve_clean_worktree_required(cli_repo_root: str | None = None) -> Path:
    """Git-scoped mutation preflight requires a clean checkout (not dirty MAIN)."""
    if not cli_repo_root:
        raise SystemExit(
            "ERROR: Git mutation preflight requires --repo-root pointing to a clean worktree.\n"
            "Create: X:\\AI MARS STORAGE\\git-sync-<label>\\repo from origin/mars/canonical-post-recovery"
        )
    root = Path(cli_repo_root).resolve()
    if not root.is_dir():
        raise SystemExit(f"ERROR: --repo-root does not exist: {root}")
    if is_disposable_sync_path(root) and not (root / ".git").exists():
        raise SystemExit(f"ERROR: --repo-root is not a valid git worktree: {root}")
    if root.resolve() == CANONICAL_MONOREPO.resolve():
        if not git_worktree_is_clean(root):
            raise SystemExit(
                "ERROR: canonical X:\\AI MARS has foreign WIP; Git mutation requires a clean worktree.\n"
                "Pass --repo-root to a fresh git-sync worktree."
            )
    elif not git_worktree_is_clean(root):
        raise SystemExit(f"ERROR: --repo-root worktree is not clean: {root}")
    return root


def add_repo_root_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Git/filesystem authority root (read-only default: X:\\AI MARS).",
    )


def add_historical_override_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--allow-historical-run",
        action="store_true",
        help="Acknowledge HISTORICAL/RETIRED status; requires explicit charter.",
    )


def guard_historical_harness(operation_id: str, *, allow_run: bool = False) -> None:
    if allow_run or os.environ.get("SITE002_ALLOW_HISTORICAL_HARNESS") == "1":
        return
    doc = CANONICAL_MONOREPO / HISTORICAL_DOC
    raise SystemExit(
        f"HISTORICAL HARNESS — {operation_id}\n"
        "This script is retained as evidence; it is not current operational tooling.\n"
        "Do not run without an explicit charter.\n"
        "Override: --allow-historical-run or SITE002_ALLOW_HISTORICAL_HARNESS=1\n"
        f"See: {doc}"
    )


def historical_banner(operation_id: str, classification: str = "HISTORICAL") -> str:
    return (
        f"# {classification} — {operation_id}\n"
        f"Authority: {CANONICAL_MONOREPO} (canonical); clean worktree via --repo-root for git mutation.\n"
        "Do not hardcode deleted git-sync-* contours.\n"
    )
