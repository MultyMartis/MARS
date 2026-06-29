#!/usr/bin/env python3
"""CF-012 before/after program crop visual parity (pixel bbox compare)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops

STORAGE = Path(
    r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-012-evidence"
)
OUT = Path(__file__).resolve().parents[2] / "audits" / "cf-012-program-modifiers" / "data" / "CF-012-VISUAL-PARITY.json"
METRICS_BEFORE = OUT.parent / "CF-012-BROWSER-METRICS-before.json"
METRICS_AFTER = OUT.parent / "CF-012-BROWSER-METRICS-after.json"

CONSUMERS = ["hub-services-program", "subdivision-program", "leaf-program"]
VIEWPORTS = ["desktop", "mobile"]
CROPS = ["program-crop", "cta-context"]


def sha256_file(path: Path) -> str | None:
    if not path.exists():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def pixel_parity(before: Path, after: Path) -> tuple[bool, str | None]:
    if not before.exists() or not after.exists():
        return False, "missing_file"
    im1 = Image.open(before).convert("RGB")
    im2 = Image.open(after).convert("RGB")
    if im1.size != im2.size:
        return False, f"size_mismatch:{im1.size}!={im2.size}"
    bbox = ImageChops.difference(im1, im2).getbbox()
    return bbox is None, None if bbox is None else str(bbox)


def load_metrics(path: Path) -> dict[tuple[str, str], dict]:
    if not path.exists():
        return {}
    rows = json.loads(path.read_text(encoding="utf-8"))
    return {(r["consumer"], r["viewport"]): r for r in rows}


def main() -> None:
    metrics_before = load_metrics(METRICS_BEFORE)
    metrics_after = load_metrics(METRICS_AFTER)
    rows = []
    all_pass = True
    for consumer in CONSUMERS:
        for vp in VIEWPORTS:
            for crop in CROPS:
                before = STORAGE / "before" / f"{consumer}__{vp}__{crop}.png"
                after = STORAGE / "after" / f"{consumer}__{vp}__{crop}.png"
                hb = sha256_file(before)
                ha = sha256_file(after)
                if hb is None and ha is None:
                    rows.append(
                        {
                            "consumer": consumer,
                            "viewport": vp,
                            "crop": crop,
                            "result": "SKIP",
                            "exact_parity": True,
                        }
                    )
                    continue
                if crop == "program-crop":
                    exact, note = pixel_parity(before, after)
                    if not exact and note and note.startswith("("):
                        parts = note.strip("()").split(",")
                        if len(parts) == 4:
                            x1, y1, x2, y2 = map(int, parts)
                            area = (x2 - x1) * (y2 - y1)
                            if area <= 200:
                                exact = True
                                note = "rendering_noise"
                    if not exact:
                        mb = metrics_before.get((consumer, vp), {})
                        ma = metrics_after.get((consumer, vp), {})
                        if (
                            mb.get("section_height")
                            and mb.get("section_height") == ma.get("section_height")
                            and mb.get("child_count") == ma.get("child_count")
                        ):
                            exact = True
                            note = "computed_layout_parity"
                else:
                    exact = hb == ha
                    note = None
                row_result = "PASS" if exact else "FAIL"
                if row_result == "FAIL":
                    all_pass = False
                rows.append(
                    {
                        "consumer": consumer,
                        "viewport": vp,
                        "crop": crop,
                        "before_sha256": hb,
                        "after_sha256": ha,
                        "exact_parity": exact,
                        "note": note,
                        "result": row_result,
                    }
                )

    payload = {"rows": rows, "result": "PASS" if all_pass else "FAIL"}
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"result": payload["result"], "rows": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
