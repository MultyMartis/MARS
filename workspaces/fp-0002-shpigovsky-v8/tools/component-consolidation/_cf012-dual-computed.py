#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

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
OUT = ROOT / "audits" / "cf-012-program-modifiers" / "data" / "CF-012-COMPUTED-OLD-NEW-DIFF.json"

JS = """(sel) => {
  const section = document.querySelector(sel);
  const pick = (s) => {
    const el = section.querySelector(s);
    if (!el) return null;
    const cs = getComputedStyle(el);
    return {h: cs.height, p: cs.padding, g: cs.gap, fit: cs.objectFit, cols: cs.gridTemplateColumns};
  };
  return {
    mods: section.className,
    grid: pick('.services-program-v2__grid'),
    media: pick('.services-program-v2__item-media'),
    image: pick('.services-program-v2__item-image'),
    body: pick('.services-program-v2__item-body'),
    title: pick('.services-program-v2__item-title'),
    sectionH: getComputedStyle(section).height,
  };
}"""


def git_show(rel: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "show", f"{COMMIT}:workspaces/fp-0002-shpigovsky-v8/{rel}"],
        text=True,
        encoding="utf-8",
    )


def capture(label: str, use_old: bool, saved: dict[str, str]) -> dict:
    for rel in FILES:
        p = ROOT / rel
        p.write_text(git_show(rel) if use_old else saved[rel], encoding="utf-8")
    subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)
    server = subprocess.Popen([sys.executable, "-m", "http.server", "4201"], cwd=ROOT / "dist")
    time.sleep(1)
    try:
        rows = {}
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for cid, file, sel, w, h in [
                ("hub", "uslugi-v2.html", "#services-program", 1437, 1000),
                ("leaf", "usluga-konechnaya-v1.html", "#service-leaf-program", 380, 900),
            ]:
                ctx = browser.new_context(viewport={"width": w, "height": h})
                page = ctx.new_page()
                page.goto(f"http://127.0.0.1:4201/{file}", wait_until="networkidle")
                rows[cid] = page.evaluate(JS, sel)
                ctx.close()
            browser.close()
        return rows
    finally:
        server.terminate()
        server.wait(timeout=5)


def main() -> None:
    saved = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in FILES}
    try:
        old = capture("old", True, saved)
        new = capture("new", False, saved)
        OUT.write_text(json.dumps({"old": old, "new": new}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(OUT)
    finally:
        for rel in FILES:
            (ROOT / rel).write_text(saved[rel], encoding="utf-8")
        subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)


if __name__ == "__main__":
    main()
