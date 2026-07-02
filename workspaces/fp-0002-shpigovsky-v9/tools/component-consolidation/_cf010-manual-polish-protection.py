#!/usr/bin/env python3
"""FP-0002 V8 CF-010 manual polish protection validation."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRE = ROOT / "audits" / "cf-010-clinic-landscape" / "data" / "cf-010-source-hash-guard-pre.json"
OUT = ROOT / "audits" / "cf-010-clinic-landscape" / "data" / "CF-010-MANUAL-POLISH-PROTECTION.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    pre = json.loads(PRE.read_text(encoding="utf-8"))
    protected_pre = pre.get("protected", {})
    current = {p: sha256_file(ROOT / p) for p in protected_pre}
    unchanged = {p: current[p] == protected_pre[p] for p in protected_pre}
    main_js_ok = sha256_file(ROOT / "src/js/main.js") == pre.get("main_js_sha256")
    asset_ok = (
        sha256_file(ROOT / "src/img/content/pre-reviews/shpigovsky-clinic-landscape.webp")
        == pre.get("asset_sha256")
    )
    decl_pre = pre.get("scss_cf010_declarations_normalized", "")
    post_path = ROOT / "audits" / "cf-010-clinic-landscape" / "data" / "cf-010-source-hash-guard-post.json"
    decl_ok = True
    if post_path.exists():
        post = json.loads(post_path.read_text(encoding="utf-8"))
        decl_ok = post.get("scss_cf010_declarations_normalized") == decl_pre

    payload = {
        "favicon_unchanged": unchanged.get("src/favicon/favicon.svg", False),
        "gallery_unchanged": unchanged.get("src/partials/sections/home-gallery.html", False),
        "program_cta_band_unchanged": unchanged.get(
            "src/partials/components/program-cta-band.html", False
        ),
        "main_js_unchanged": main_js_ok,
        "asset_unchanged": asset_ok,
        "cf010_declaration_values_unchanged": decl_ok,
        "protected_file_checks": unchanged,
        "result": "PASS"
        if all(unchanged.values()) and main_js_ok and asset_ok and decl_ok
        else "FAIL",
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"result": payload["result"]}, indent=2))


if __name__ == "__main__":
    main()
