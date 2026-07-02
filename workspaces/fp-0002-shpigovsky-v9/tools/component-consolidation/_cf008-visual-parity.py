#!/usr/bin/env python3
"""FP-0002 V8 CF-008 before/after visual parity comparison."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageChops

STORAGE = Path(r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-008-evidence")
AUDIT = Path(__file__).resolve().parents[2] / "audits" / "cf-008-faq"

PAGES = ["home", "services", "services-v2", "service-subdivision", "service-leaf"]
VIEWPORTS = ["desktop", "mobile"]
STATES = ["initial", "open-first"]
KINDS = ["faq_crop", "faq_context"]


def diff_pixels(a: Path, b: Path) -> dict:
    if not a.exists() or not b.exists():
        return {"exists": False, "different_pixels": None, "total_pixels": None, "ratio": None}
    img_a = Image.open(a).convert("RGB")
    img_b = Image.open(b).convert("RGB")
    if img_a.size != img_b.size:
        img_b = img_b.resize(img_a.size, Image.Resampling.LANCZOS)
    diff = ImageChops.difference(img_a, img_b)
    bbox = diff.getbbox()
    different = 0 if bbox is None else (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
    total = img_a.size[0] * img_a.size[1]
    return {
        "exists": True,
        "size": img_a.size,
        "different_pixels": different,
        "total_pixels": total,
        "ratio": 0 if total == 0 else different / total,
        "bbox": bbox,
        "exact_match": bbox is None,
    }


def main() -> None:
    matrix: list[dict] = []
    for page in PAGES:
        for viewport in VIEWPORTS:
            for state in STATES:
                for kind in KINDS:
                    base = f"{page}-{viewport}-{state}"
                    suffix = "-faq-crop.png" if kind == "faq_crop" else "-faq-context.png"
                    before = STORAGE / "before" / f"{base}{suffix}"
                    after = STORAGE / "after" / f"{base}{suffix}"
                    d = diff_pixels(before, after)
                    row = {
                        "page": page,
                        "viewport": viewport,
                        "state": state,
                        "kind": kind,
                        "before": str(before),
                        "after": str(after),
                        **d,
                        "result": "PASS" if d.get("exact_match") else "FAIL",
                    }
                    matrix.append(row)

    overall = "PASS" if all(r["result"] == "PASS" for r in matrix if r.get("exists")) else "FAIL"
    payload = {
        "manifest_id": "CF-008-VISUAL-PARITY-MATRIX",
        "overall": overall,
        "matrix": matrix,
    }
    (AUDIT / "CF-008-VISUAL-PARITY-MATRIX.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": overall, "rows": len(matrix)}, indent=2))
    if overall != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
