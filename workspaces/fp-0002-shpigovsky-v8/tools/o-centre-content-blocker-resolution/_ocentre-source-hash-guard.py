#!/usr/bin/env python3
"""Compute FP-0002 V8 source protection hashes for O-Centre content task."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = (
    ROOT
    / "audits/o-centre-content-blocker-resolution/data/FP-0002-V8-OCENTRE-SOURCE-HASH-GUARD.json"
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    groups: dict[str, dict[str, str]] = {
        "pages": {},
        "partials": {},
        "style_scss": {},
        "main_js": {},
        "o_centre_assets": {},
        "favicon": {},
    }

    for p in sorted((ROOT / "src/pages").glob("**/*")):
        if p.is_file():
            rel = p.relative_to(ROOT).as_posix()
            groups["pages"][rel] = sha256_file(p)

    for p in sorted((ROOT / "src/partials").glob("**/*")):
        if p.is_file():
            rel = p.relative_to(ROOT).as_posix()
            groups["partials"][rel] = sha256_file(p)

    scss = ROOT / "src/scss/style.scss"
    if scss.is_file():
        groups["style_scss"]["src/scss/style.scss"] = sha256_file(scss)

    js = ROOT / "src/js/main.js"
    if js.is_file():
        groups["main_js"]["src/js/main.js"] = sha256_file(js)

    oc_dir = ROOT / "src/img/content/o-centre"
    if oc_dir.is_dir():
        for p in sorted(oc_dir.glob("**/*")):
            if p.is_file():
                rel = p.relative_to(ROOT).as_posix()
                groups["o_centre_assets"][rel] = sha256_file(p)

    fav = ROOT / "src/favicon"
    if fav.is_dir():
        for p in sorted(fav.glob("**/*")):
            if p.is_file():
                rel = p.relative_to(ROOT).as_posix()
                groups["favicon"][rel] = sha256_file(p)

    payload = {
        "workspace": str(ROOT),
        "groups": groups,
        "counts": {k: len(v) for k, v in groups.items()},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(OUT), "counts": payload["counts"]}, indent=2))


if __name__ == "__main__":
    main()
