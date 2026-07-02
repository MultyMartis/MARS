#!/usr/bin/env python3
"""Build OLD CF-011 program state in isolated temp, capture hub/leaf crops, restore."""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
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
BACKUP = ROOT / "audits" / "cf-012-program-modifiers" / "data" / "_old-state-snapshot"
OUT = Path(
    r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-012-evidence\old-ref"
)


def git_show(path: str) -> str:
    rel = f"workspaces/fp-0002-shpigovsky-v8/{path}"
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{COMMIT}:{rel}"],
        text=True,
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    BACKUP.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    saved: dict[Path, str] = {}
    for rel in FILES:
        p = ROOT / rel
        saved[p] = p.read_text(encoding="utf-8")
        (BACKUP / Path(rel).name).write_text(saved[p], encoding="utf-8")

    try:
        for rel in FILES:
            p = ROOT / rel
            p.write_text(git_show(rel), encoding="utf-8")

        subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)

        import time
        from playwright.sync_api import sync_playwright

        server = subprocess.Popen(
            [sys.executable, "-m", "http.server", "4200"],
            cwd=ROOT / "dist",
        )
        time.sleep(1)

        shots = [
            ("hub-desktop", "uslugi-v2.html", "#services-program", 1437, 1000),
            ("leaf-mobile", "usluga-konechnaya-v1.html", "#service-leaf-program", 380, 900),
        ]
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for stem, page_file, sel, w, h in shots:
                ctx = browser.new_context(viewport={"width": w, "height": h})
                page = ctx.new_page()
                page.goto(f"http://127.0.0.1:4200/{page_file}", wait_until="networkidle")
                el = page.query_selector(sel)
                if el:
                    el.screenshot(path=str(OUT / f"{stem}__program-crop.png"))
                ctx.close()
            browser.close()

        report = {}
        before_dir = Path(
            r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-012-evidence\before"
        )
        after_dir = Path(
            r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-012-evidence\after"
        )
        for stem, before_name, after_name in [
            ("hub-desktop", "hub-services-program__desktop__program-crop.png", "hub-services-program__desktop__program-crop.png"),
            ("leaf-mobile", "leaf-program__mobile__program-crop.png", "leaf-program__mobile__program-crop.png"),
        ]:
            old_ref = OUT / f"{stem}__program-crop.png"
            before = before_dir / before_name
            after = after_dir / after_name
            report[stem] = {
                "old_ref_sha": sha256(old_ref) if old_ref.exists() else None,
                "before_sha": sha256(before) if before.exists() else None,
                "after_sha": sha256(after) if after.exists() else None,
                "before_matches_old_ref": sha256(old_ref) == sha256(before) if old_ref.exists() and before.exists() else None,
                "after_matches_old_ref": sha256(old_ref) == sha256(after) if old_ref.exists() and after.exists() else None,
            }
        (BACKUP / "compare-report.json").write_text(
            __import__("json").dumps(report, indent=2) + "\n", encoding="utf-8"
        )
        print(__import__("json").dumps(report, indent=2))
    finally:
        if "server" in locals():
            server.terminate()
            server.wait(timeout=5)
        for p, content in saved.items():
            p.write_text(content, encoding="utf-8")
        subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)


if __name__ == "__main__":
    main()
