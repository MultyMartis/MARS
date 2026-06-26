"""Create design block crops from operator PNG authority rasters."""
from pathlib import Path
from PIL import Image

review = Path(__file__).parent
design = review / "design-rasters"
out_d = review / "design-crops" / "desktop"
out_m = review / "design-crops" / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

DESKTOP = [
    ("DESIGN-D-01-HEADER-HERO", 0, 900),
    ("DESIGN-D-02-UPPER-CONTENT", 820, 1200),
    ("DESIGN-D-03-DEPENDENCIES", 900, 2100),
    ("DESIGN-D-04-NATURE", 2100, 3200),
    ("DESIGN-D-05-CTA-01", 3200, 3500),
    ("DESIGN-D-06-PROGRAM", 3500, 5200),
    ("DESIGN-D-07-REHABILITATION-STAGES", 5200, 6800),
    ("DESIGN-D-08-CTA-02", 6800, 7200),
    ("DESIGN-D-09-APPROACH-INTERIOR", 7200, 9000),
    ("DESIGN-D-10-TEAM-CENTER", 9000, 10200),
    ("DESIGN-D-11-SPECIALISTS", 10200, 11200),
    ("DESIGN-D-12-FOUNDER", 11200, 12000),
    ("DESIGN-D-13-COMFORT", 12000, 13200),
    ("DESIGN-D-14-REVIEWS", 12800, 13150),
    ("DESIGN-D-15-FAQ", 13150, 13450),
    ("DESIGN-D-16-FINAL-FORM-FOOTER", 13450, None),
]

MOBILE = [
    ("DESIGN-M-01-HEADER-HERO", 0, 700),
    ("DESIGN-M-02-UPPER-CONTENT", 700, 1200),
    ("DESIGN-M-03-DEPENDENCIES", 1200, 2200),
    ("DESIGN-M-04-NATURE", 2200, 3400),
    ("DESIGN-M-05-CTA-01", 3400, 3800),
    ("DESIGN-M-06-PROGRAM", 3800, 5600),
    ("DESIGN-M-07-REHABILITATION-STAGES", 5600, 7200),
    ("DESIGN-M-08-CTA-02", 7200, 7600),
    ("DESIGN-M-09-APPROACH-INTERIOR", 7600, 9400),
    ("DESIGN-M-10-TEAM-CENTER", 9400, 10800),
    ("DESIGN-M-11-SPECIALISTS", 10800, 12000),
    ("DESIGN-M-12-FOUNDER", 12000, 12800),
    ("DESIGN-M-13-COMFORT", 12800, 14500),
    ("DESIGN-M-14-REVIEWS", 16800, 17200),
    ("DESIGN-M-15-FAQ", 17200, 17650),
    ("DESIGN-M-16-FINAL-FORM-FOOTER", 17650, None),
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
print("design crops written", out_d, out_m)
