from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent / "design-rasters"
crops_dir = Path(__file__).parent / "crops"
crops_dir.mkdir(exist_ok=True)

DESKTOP_CROPS = [
    ("GROUP1-HEADER-HERO-NAV", 0, 980),
    ("GROUP1-UPPER-CONTENT-CTA", 980, 2520),
    ("GROUP2-SIGNS-EDITORIAL", 2520, 4200),
    ("GROUP3-APPROACH-LANDSCAPE", 4200, 6500),
    ("GROUP4-PROGRAM", 6500, 8300),
    ("GROUP5-STAGES-CTA-SUPPORT", 8300, 10100),
    ("GROUP6A-CORRIDOR-SPECIALISTS-FOUNDER", 10100, 11250),
    ("GROUP6B-COMFORT-REVIEWS-FAQ-FORM-FOOTER", 11250, 13313),
]

MOBILE_CROPS = [
    ("GROUP1-HEADER-HERO-NAV", 0, 720),
    ("GROUP1-UPPER-CONTENT-CTA", 720, 2400),
    ("GROUP2-SIGNS-EDITORIAL", 2400, 4800),
    ("GROUP3-APPROACH-LANDSCAPE", 4800, 7200),
    ("GROUP4-PROGRAM", 7200, 9400),
    ("GROUP5-STAGES-CTA-SUPPORT", 9400, 12000),
    ("GROUP6A-CORRIDOR-SPECIALISTS-FOUNDER", 12000, 14500),
    ("GROUP6B-COMFORT-REVIEWS-FAQ-FORM-FOOTER", 14500, 18136),
]

for variant, crops in [("DESKTOP", DESKTOP_CROPS), ("MOBILE", MOBILE_CROPS)]:
    src = ROOT / f"SERVICE-LEAF-DESIGN-AUTHORITY-{variant}.png"
    im = Image.open(src)
    for name, y0, y1 in crops:
        y1 = min(y1, im.height)
        crop = im.crop((0, y0, im.width, y1))
        out = crops_dir / f"SERVICE-LEAF-{variant}-{name}.png"
        crop.save(out)
        print("wrote", out.name, f"{crop.width}x{crop.height}")
