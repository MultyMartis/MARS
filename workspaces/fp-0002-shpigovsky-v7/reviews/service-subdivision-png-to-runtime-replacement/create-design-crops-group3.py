"""Create GROUP 3 design block crops from operator PNG authority rasters."""
from pathlib import Path
from PIL import Image

review = Path(__file__).parent
design = review / "design-rasters"
out_d = review / "design-crops" / "group-3" / "desktop"
out_m = review / "design-crops" / "group-3" / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

DESKTOP = [
    ("DESIGN-D-G3-01-REHABILITATION-HEADER", 4585, 4980),
    ("DESIGN-D-G3-02-REHABILITATION-STAGES", 4980, 5320),
    ("DESIGN-D-G3-03-CTA", 5320, 5560),
    ("DESIGN-D-G3-04-SUPPORT-BLOCK", 5560, 5980),
    ("DESIGN-D-G3-05-TRANSITION", 5980, 6150),
]

MOBILE = [
    ("DESIGN-M-G3-01-REHABILITATION-HEADER", 6125, 6420),
    ("DESIGN-M-G3-02-REHABILITATION-STAGES", 6420, 7180),
    ("DESIGN-M-G3-03-CTA", 7180, 7520),
    ("DESIGN-M-G3-04-SUPPORT-BLOCK", 7520, 7920),
    ("DESIGN-M-G3-05-TRANSITION", 7920, 8100),
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
print("group-3 design crops written", out_d, out_m)
