"""Create GROUP 4 design block crops from operator PNG authority rasters."""
from pathlib import Path
from PIL import Image

review = Path(__file__).parent
design = review / "design-rasters"
out_d = review / "design-crops" / "group-4" / "desktop"
out_m = review / "design-crops" / "group-4" / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

DESKTOP = [
    ("DESIGN-D-G4-01-TRANSITION-AFTER-SUPPORT", 5960, 6150),
    ("DESIGN-D-G4-02-CORRIDOR-INTERIOR", 5980, 6430),
    ("DESIGN-D-G4-03-APPROACH-HEADING-AND-LEAD", 6430, 6730),
    ("DESIGN-D-G4-04-TEAM-PHOTO-AND-INTRO", 6730, 7240),
    ("DESIGN-D-G4-05-APPROACH-SERVICE-CARDS", 7240, 7720),
    ("DESIGN-D-G4-06-GROUP-END-TRANSITION", 7720, 7920),
]

MOBILE = [
    ("DESIGN-M-G4-01-TRANSITION-AFTER-SUPPORT", 8080, 8280),
    ("DESIGN-M-G4-02-CORRIDOR-INTERIOR", 8100, 8580),
    ("DESIGN-M-G4-03-APPROACH-HEADING-AND-LEAD", 8580, 9100),
    ("DESIGN-M-G4-04-TEAM-PHOTO-AND-INTRO", 9100, 9680),
    ("DESIGN-M-G4-05-APPROACH-SERVICE-CARDS", 9680, 10280),
    ("DESIGN-M-G4-06-GROUP-END-TRANSITION", 10280, 10480),
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
print("group-4 design crops written", out_d, out_m)
