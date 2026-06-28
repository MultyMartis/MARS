#!/usr/bin/env python3
"""Re-capture CF-010 before evidence from git HEAD (pre-CF-010 source)."""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
PREFIX = "workspaces/fp-0002-shpigovsky-v8/"
HEAD_FILES = [
    "src/partials/sections/home-clinic-landscape.html",
    "src/pages/index.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/scss/style.scss",
]

saved: dict[str, bytes | None] = {}
for rel in list(HEAD_FILES) + ["src/partials/sections/clinic-landscape.html"]:
    p = ROOT / rel
    saved[rel] = p.read_bytes() if p.exists() else None


def restore() -> None:
    clinic = ROOT / "src/partials/sections/clinic-landscape.html"
    old = ROOT / "src/partials/sections/home-clinic-landscape.html"
    if saved.get("src/partials/sections/clinic-landscape.html"):
        clinic.write_bytes(saved["src/partials/sections/clinic-landscape.html"])  # type: ignore[index]
    elif clinic.exists():
        clinic.unlink()
    if saved.get("src/partials/sections/home-clinic-landscape.html") is None and old.exists():
        old.unlink()
    elif saved.get("src/partials/sections/home-clinic-landscape.html"):
        old.write_bytes(saved["src/partials/sections/home-clinic-landscape.html"])  # type: ignore[index]
    for rel in HEAD_FILES:
        data = saved.get(rel)
        dest = ROOT / rel
        if data is not None:
            dest.write_bytes(data)
    subprocess.run("npm run build", cwd=str(ROOT), check=True, shell=True)


try:
    for rel in HEAD_FILES:
        data = subprocess.check_output(
            ["git", "-C", str(REPO), "show", f"HEAD:{PREFIX}{rel}"]
        )
        dest = ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    clinic = ROOT / "src/partials/sections/clinic-landscape.html"
    if clinic.exists():
        clinic.unlink()

    subprocess.run("npm run build", cwd=str(ROOT), check=True, shell=True)
    subprocess.run(
        [
            "python",
            str(ROOT / "tools/component-consolidation/_cf010-browser-qa.py"),
            "before",
            "4198",
        ],
        check=True,
    )
finally:
    restore()

print("before re-capture complete")
