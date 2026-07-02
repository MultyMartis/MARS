#!/usr/bin/env python3
"""FP-0002 V8 CF-003 post-implementation source hash guard."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-003-upper-navigation" / "data"

TARGET = [
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/partials/components/breadcrumbs.html",
    "src/partials/components/services-page-subnav.html",
    "src/partials/components/internal-page-nav.html",
    "src/scss/style.scss",
]

PROTECTED = [
    "src/pages/index.html",
    "src/partials/layout/header.html",
    "src/partials/layout/footer.html",
    "src/partials/components/modal-consultation.html",
    "src/js/main.js",
    "src/partials/sections/services-inner-hero-v2.html",
    "src/partials/components/services-program-cta-band-v2.html",
    "src/partials/sections/services-program-v2.html",
    "src/partials/sections/home-specialists.html",
    "src/partials/sections/home-reviews.html",
    "src/partials/sections/home-final-form.html",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    pre = json.loads((AUDIT / "cf-003-source-hash-guard-pre.json").read_text(encoding="utf-8"))
    post = {
        "phase": "post-implementation",
        "target": {rel: sha256_file(ROOT / rel) for rel in TARGET},
        "protected": {rel: sha256_file(ROOT / rel) for rel in PROTECTED if (ROOT / rel).is_file()},
    }
    protected_unchanged = {
        rel: pre["protected"][rel] == post["protected"][rel]
        for rel in pre["protected"]
        if rel in post["protected"]
    }
    report = {
        "post": post,
        "protected_unchanged": protected_unchanged,
        "protected_changes": [k for k, v in protected_unchanged.items() if not v],
        "pre_target": pre["target"],
        "target_changed": {
            rel: pre["target"].get(rel) != post["target"].get(rel)
            for rel in set(pre["target"]) | set(post["target"])
        },
    }
    (AUDIT / "cf-003-source-hash-guard-post.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if report["protected_changes"]:
        raise SystemExit(f"Protected file drift: {report['protected_changes']}")


if __name__ == "__main__":
    main()
