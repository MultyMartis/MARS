#!/usr/bin/env python3
"""FP-0002 V8 CF-008 post-implementation hash guard."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-008-faq" / "data"

TARGET_FILES = [
    "src/partials/sections/faq.html",
    "src/pages/index.html",
    "src/pages/uslugi.html",
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/scss/style.scss",
    "src/js/main.js",
]

PROTECTED_FILES = [
    "src/partials/components/internal-page-nav.html",
    "src/partials/sections/founder-quote.html",
    "src/partials/sections/specialists.html",
    "src/partials/sections/comfort.html",
    "src/partials/sections/reviews.html",
    "src/partials/layout/header.html",
    "src/partials/layout/footer.html",
    "src/partials/components/modal-consultation.html",
    "src/partials/sections/hero.html",
    "src/partials/sections/home-final-form.html",
    "src/partials/sections/home-clinic-landscape.html",
    "src/partials/sections/home-gallery.html",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    pre = json.loads((AUDIT / "cf-008-source-hash-guard-pre.json").read_text(encoding="utf-8"))
    post = {
        "phase": "post-implementation",
        "target": {rel: sha256_file(ROOT / rel) for rel in TARGET_FILES if (ROOT / rel).is_file()},
        "protected": {
            rel: sha256_file(ROOT / rel) for rel in PROTECTED_FILES if (ROOT / rel).is_file()
        },
    }
    protected_changes = [
        rel for rel, h in post["protected"].items() if pre["protected"].get(rel) != h
    ]
    post["protected_changes"] = protected_changes
    post["protected_changes_count"] = len(protected_changes)
    (AUDIT / "cf-008-source-hash-guard-post.json").write_text(
        json.dumps(post, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"protected_changes": protected_changes, "count": len(protected_changes)}, indent=2))
    if protected_changes:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
