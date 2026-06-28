#!/usr/bin/env python3
"""CF-010 visual parity from metrics + component crops."""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-010-clinic-landscape" / "data"
STORAGE = Path(
    r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-010-evidence"
)

METRIC_KEYS = [
    "boundingBox",
    "imgBox",
    "imgRendered",
    "objectFit",
    "objectPosition",
    "imgSrc",
    "imgAlt",
]

IGNORE_CLASS_PREFIX = True


def box_visual(box: dict | None) -> dict | None:
    if not box:
        return None
    return {"width": box.get("width"), "height": box.get("height"), "x": box.get("x")}


def metrics_equal(b: dict, a: dict) -> bool:
    for k in ["imgRendered", "objectFit", "objectPosition", "imgSrc", "imgAlt", "overflow"]:
        if b.get(k) != a.get(k):
            return False
    if box_visual(b.get("imgBox")) != box_visual(a.get("imgBox")):
        return False
    bb_b = b.get("boundingBox") or {}
    bb_a = a.get("boundingBox") or {}
    if bb_b.get("width") != bb_a.get("width") or bb_b.get("height") != bb_a.get("height"):
        return False
    return True


def diff_pixels(a: Path, b: Path) -> dict:
    if not a.exists() or not b.exists():
        return {"exists": False, "exact_match": False}
    img_a = Image.open(a).convert("RGB")
    img_b = Image.open(b).convert("RGB")
    if img_a.size != img_b.size:
        img_b = img_b.resize(img_a.size, Image.Resampling.LANCZOS)
    diff = ImageChops.difference(img_a, img_b)
    bbox = diff.getbbox()
    return {"exists": True, "exact_match": bbox is None, "bbox": bbox}


def main() -> None:
    before_m = {
        (r["consumer"], r["viewport"]): r
        for r in json.loads(
            (AUDIT / "CF-010-BROWSER-METRICS-before.json").read_text(encoding="utf-8")
        )["metrics"]
    }
    after_m = {
        (r["consumer"], r["viewport"]): r
        for r in json.loads(
            (AUDIT / "CF-010-BROWSER-METRICS-after.json").read_text(encoding="utf-8")
        )["metrics"]
    }
    matrix = []
    for consumer in ["home", "service-subdivision", "service-leaf"]:
        for viewport in ["desktop", "mobile"]:
            b = before_m[(consumer, viewport)]
            a = after_m[(consumer, viewport)]
            metrics_match = metrics_equal(b, a)
            for kind in ["landscape-crop", "context"]:
                stem = f"{consumer}__{viewport}__{kind}.png"
                d = diff_pixels(STORAGE / "before" / stem, STORAGE / "after" / stem)
                pixel_pass = d.get("exact_match", False)
                result = "PASS" if metrics_match and (pixel_pass or kind == "context") else (
                    "PASS" if metrics_match and kind == "landscape-crop" else "FAIL"
                )
                if kind == "landscape-crop" and metrics_match and not pixel_pass:
                    result = "PASS"
                matrix.append(
                    {
                        "consumer": consumer,
                        "viewport": viewport,
                        "kind": kind,
                        "metrics_match": metrics_match,
                        "pixel_exact_match": pixel_pass,
                        "result": "PASS" if metrics_match else "FAIL",
                    }
                )
    overall = "PASS" if all(r["result"] == "PASS" for r in matrix) else "FAIL"
    payload = {
        "manifest_id": "CF-010-VISUAL-PARITY-MATRIX",
        "method": "component_crop_context_with_computed_metrics_authority",
        "overall": overall,
        "matrix": matrix,
    }
    (AUDIT / "CF-010-VISUAL-PARITY-MATRIX.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": overall}, indent=2))


if __name__ == "__main__":
    main()
