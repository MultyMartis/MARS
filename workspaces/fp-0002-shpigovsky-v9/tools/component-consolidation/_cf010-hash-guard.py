#!/usr/bin/env python3
"""FP-0002 V8 CF-010 scoped hash guard (pre/post)."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-010-clinic-landscape" / "data"

CF010_SELECTOR_PATTERNS = [
    r"home-clinic-landscape",
    r"clinic-landscape",
    r"10h\. Home clinic landscape",
    r"10h\. Clinic landscape",
]

PROTECTED_FILES = {
    "src/favicon/favicon.svg",
    "src/partials/sections/home-gallery.html",
    "src/partials/components/program-cta-band.html",
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_cf010_scss_ranges(text: str) -> list[dict]:
    lines = text.splitlines(keepends=True)
    ranges: list[dict] = []
    in_block = False
    start = 0
    for i, line in enumerate(lines):
        if "home-clinic-landscape" in line or "clinic-landscape" in line or (
            "10h" in line and "clinic landscape" in line.lower()
        ):
            if not in_block:
                start = i
                in_block = True
        elif in_block and line.strip() == "" and i + 1 < len(lines):
            next_line = lines[i + 1]
            if not any(p in next_line for p in ["home-clinic-landscape", "clinic-landscape"]):
                ranges.append({"start_line": start + 1, "end_line": i + 1, "text": "".join(lines[start : i + 1])})
                in_block = False
    if in_block:
        ranges.append({"start_line": start + 1, "end_line": len(lines), "text": "".join(lines[start:])})
    return ranges


def cf010_scss_declarations(text: str) -> str:
    """Extract declaration blocks ignoring selector names."""
    decls = []
    for block in re.findall(r"\{([^}]+)\}", text):
        if "home-clinic-landscape" in block or "clinic-landscape" in block:
            continue
        cleaned = re.sub(r"//[^\n]*", "", block)
        decls.append(cleaned.strip())
    return "\n".join(sorted(decls))


def main() -> None:
    phase = sys.argv[1] if len(sys.argv) > 1 else "pre"
    scss = (ROOT / "src/scss/style.scss").read_text(encoding="utf-8")
    partial = ROOT / "src/partials/sections/home-clinic-landscape.html"
    if not partial.exists():
        partial = ROOT / "src/partials/sections/clinic-landscape.html"
    payload = {
        "phase": phase,
        "partial": {
            "path": str(partial.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256_file(partial) if partial.exists() else None,
        },
        "consumers": {
            p.name: sha256_file(p)
            for p in [
                ROOT / "src/pages/index.html",
                ROOT / "src/pages/usluga-podrazdel-v1.html",
                ROOT / "src/pages/usluga-konechnaya-v1.html",
            ]
        },
        "scss_cf010_ranges": extract_cf010_scss_ranges(scss),
        "scss_cf010_declarations_normalized": cf010_scss_declarations(
            "".join(r["text"] for r in extract_cf010_scss_ranges(scss))
        ),
        "protected": {p: sha256_file(ROOT / p) for p in PROTECTED_FILES if (ROOT / p).exists()},
        "main_js_sha256": sha256_file(ROOT / "src/js/main.js"),
        "asset_sha256": sha256_file(
            ROOT / "src/img/content/pre-reviews/shpigovsky-clinic-landscape.webp"
        ),
    }
    out = AUDIT / f"cf-010-source-hash-guard-{phase}.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"phase": phase, "out": str(out)}, indent=2))


if __name__ == "__main__":
    main()
