#!/usr/bin/env python3
"""Capture browser evidence for CF-011 baseline (before) or current tree."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = Path(
    subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"], text=True, encoding="utf-8"
    ).strip()
)
COMMIT = "4d98d6fbc273bd1bd4cf4555d973f2b978bef0fa"
FILES = [
    "src/scss/style.scss",
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
]
PHASE = sys.argv[1]
PORT = int(sys.argv[2])


def git_show(rel: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{COMMIT}:workspaces/fp-0002-shpigovsky-v8/{rel}"],
        text=True,
        encoding="utf-8",
    )


def main() -> None:
    saved = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in FILES}
    server = None
    try:
        if PHASE == "before":
            for rel in FILES:
                (ROOT / rel).write_text(git_show(rel), encoding="utf-8")
            subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)
        server = subprocess.Popen(
            [sys.executable, "-m", "http.server", str(PORT)],
            cwd=ROOT / "dist",
        )
        time.sleep(1)
        subprocess.check_call(
            [
                sys.executable,
                str(ROOT / "tools/component-consolidation/_cf012-browser-qa.py"),
                PHASE,
                str(PORT),
            ],
            cwd=ROOT,
        )
    finally:
        if server:
            server.terminate()
            server.wait(timeout=5)
        if PHASE == "before":
            for rel in FILES:
                (ROOT / rel).write_text(saved[rel], encoding="utf-8")
            subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)


if __name__ == "__main__":
    main()
