"""Crop runtime full-page PNG to micro-pass region."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("PIL/Pillow required for crop step")

CROP = {"x": 0, "y": 4300, "width": 1437, "height": 4500}


def main() -> None:
    full_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    img = Image.open(full_path)
    x, y, w, h = CROP["x"], CROP["y"], CROP["width"], CROP["height"]
    h = min(h, img.height - y)
    cropped = img.crop((x, y, x + w, y + h))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(out_path)
    print(json.dumps({"full": str(full_path), "crop": str(out_path), "size": cropped.size}, ensure_ascii=False))


if __name__ == "__main__":
    main()
