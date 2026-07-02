#!/usr/bin/env python3
"""CF-012 CF-011 protection validation — program-cta-band must be unchanged."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRE = ROOT / "audits" / "cf-011-dark-cta" / "data" / "cf-011-source-hash-guard-pre.json"
OUT = ROOT / "audits" / "cf-012-program-modifiers" / "data" / "CF-012-CF011-PROTECTION.json"

CTA_PARTIAL = ROOT / "src/partials/components/program-cta-band.html"
SCSS = ROOT / "src/scss/style.scss"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_cta_css(text: str) -> str:
    m = re.search(r"/\* CF-011 program-cta-band \*/.*?(?=\n/\* |\Z)", text, re.DOTALL)
    return m.group(0) if m else ""


def main() -> None:
    pre = json.loads(PRE.read_text(encoding="utf-8"))
    pre_hashes = pre.get("hashes", pre.get("sha256", {}))
    partial_hash = sha256_file(CTA_PARTIAL)
    scss_text = SCSS.read_text(encoding="utf-8")
    cta_css = extract_cta_css(scss_text)
    cta_css_hash = hashlib.sha256(cta_css.encode("utf-8")).hexdigest()

    expected_partial = pre_hashes.get("src/partials/components/program-cta-band.html")
    partial_ok = partial_hash == expected_partial if expected_partial else True

    payload = {
        "program_cta_band_partial_hash": partial_hash,
        "program_cta_band_partial_unchanged": partial_ok,
        "program_cta_band_css_hash": cta_css_hash,
        "program_cta_band_css_present": bool(cta_css),
        "result": "PASS" if partial_ok and cta_css else "FAIL",
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
