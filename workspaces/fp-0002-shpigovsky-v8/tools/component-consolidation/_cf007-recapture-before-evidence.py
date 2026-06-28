#!/usr/bin/env python3
"""Rebuild pre-CF-007 source from backup and recapture before evidence with stabilized harness."""
from __future__ import annotations

import shutil
import subprocess
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BACKUP = Path(
    r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints\FP-0002-V8-BEFORE-CF-007-REVIEWS-UNIVERSALIZATION.zip"
)
STAGING = ROOT / ".cf007-recapture-staging"
FILES = [
    "src/partials/sections/home-reviews.html",
    "src/pages/index.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/scss/style.scss",
    "src/js/main.js",
]


def main() -> None:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    post = STAGING / "post"
    post.mkdir(parents=True)

    for rel in FILES:
        src = ROOT / rel
        if src.is_file():
            dest = post / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
    reviews = ROOT / "src/partials/sections/reviews.html"
    if reviews.is_file():
        dest = post / "src/partials/sections/reviews.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(reviews, dest)

    with zipfile.ZipFile(BACKUP, "r") as zf:
        for rel in FILES:
            zf.extract(rel, STAGING / "pre")
            shutil.copy2(STAGING / "pre" / rel, ROOT / rel)
    reviews.unlink(missing_ok=True)

    subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)
    server = subprocess.Popen(
        ["python", "-m", "http.server", "4197"],
        cwd=ROOT / "dist",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.5)
    try:
        subprocess.check_call(
            [
                "python",
                str(ROOT / "tools/component-consolidation/_cf007-browser-qa.py"),
                "before",
                "4197",
            ]
        )
    finally:
        server.terminate()
        server.wait(timeout=10)

    for rel in FILES:
        shutil.copy2(post / rel, ROOT / rel)
    post_reviews = post / "src/partials/sections/reviews.html"
    if post_reviews.is_file():
        shutil.copy2(post_reviews, ROOT / "src/partials/sections/reviews.html")
    (ROOT / "src/partials/sections/home-reviews.html").unlink(missing_ok=True)

    subprocess.check_call(["npm", "run", "build"], cwd=ROOT, shell=True)
    shutil.rmtree(STAGING)
    print("before evidence recaptured")


if __name__ == "__main__":
    main()
