"""Create GROUP 2 design block crops from operator PNG authority rasters."""
from pathlib import Path
from PIL import Image

review = Path(__file__).parent
design = review / "design-rasters"
out_d = review / "design-crops" / "group-2" / "desktop"
out_m = review / "design-crops" / "group-2" / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

DESKTOP = [
    ("DESIGN-D-05-CTA-01", 2680, 2990),
    ("DESIGN-D-06-PROGRAM-HEADER", 2990, 3380),
    ("DESIGN-D-07-PROGRAM-CARDS", 3380, 4480),
    ("DESIGN-D-08-CTA-02", 4480, 4585),
]

MOBILE = [
    ("DESIGN-M-05-CTA-01", 3480, 3920),
    ("DESIGN-M-06-PROGRAM-HEADER", 3920, 4480),
    ("DESIGN-M-07-PROGRAM-CARDS", 4480, 5980),
    ("DESIGN-M-08-CTA-02", 5980, 6125),
]


def crop_list(src: Path, blocks, out_dir: Path, width: int):
    im = Image.open(src)
    h = im.size[1]
    for name, y1, y2 in blocks:
        y2 = h if y2 is None else min(y2, h)
        im.crop((0, y1, width, y2)).save(out_dir / f"{name}.png")


crop_list(
    design / "SERVICE-SUBDIVISION-DESIGN-AUTHORITY-DESKTOP.png",
    DESKTOP,
    out_d,
    1437,
)
crop_list(
    design / "SERVICE-SUBDIVISION-DESIGN-AUTHORITY-MOBILE.png",
    MOBILE,
    out_m,
    380,
)
print("group-2 design crops written", out_d, out_m)
