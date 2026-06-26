from pathlib import Path
from PIL import Image

desktop_src = Path(
    r"C:\MARS Phenix\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\26.06.2026\Услуга - десктоп.png"
)
mobile_src = Path(
    r"C:\MARS Phenix\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\26.06.2026\Услуга - мобильная.png"
)
out_desktop = Path(__file__).parent / "design-crops" / "desktop"
out_mobile = Path(__file__).parent / "design-crops" / "mobile"
out_desktop.mkdir(parents=True, exist_ok=True)
out_mobile.mkdir(parents=True, exist_ok=True)

DESKTOP = [
    ("SERVICE-LEAF-D-G3-01-BOUNDARY-START", 2460, 2620),
    ("SERVICE-LEAF-D-G3-02-APPROACH-HEADING-INTRO", 2580, 2860),
    ("SERVICE-LEAF-D-G3-03-TEAM-PHOTO", 2860, 3300),
    ("SERVICE-LEAF-D-G3-04-APPROACH-CARDS", 3300, 4000),
    ("SERVICE-LEAF-D-G3-05-CLINIC-LANDSCAPE", 4000, 4560),
    ("SERVICE-LEAF-D-G3-06-BOUNDARY-END", 4480, 4680),
    ("SERVICE-LEAF-D-G3-FULL", 2493, 4560),
]

MOBILE = [
    ("SERVICE-LEAF-M-G3-01-BOUNDARY-START", 3580, 3720),
    ("SERVICE-LEAF-M-G3-02-APPROACH-HEADING-INTRO", 3655, 3950),
    ("SERVICE-LEAF-M-G3-03-TEAM-PHOTO", 3950, 4350),
    ("SERVICE-LEAF-M-G3-04-APPROACH-CARDS", 4350, 5050),
    ("SERVICE-LEAF-M-G3-05-CLINIC-LANDSCAPE", 5050, 5480),
    ("SERVICE-LEAF-M-G3-06-BOUNDARY-END", 5420, 5580),
    ("SERVICE-LEAF-M-G3-FULL", 3655, 5503),
]

for src, crops, out_dir in [
    (desktop_src, DESKTOP, out_desktop),
    (mobile_src, MOBILE, out_mobile),
]:
    im = Image.open(src)
    for name, y0, y1 in crops:
        y1 = min(y1, im.height)
        crop = im.crop((0, y0, im.width, y1))
        out = out_dir / f"{name}.png"
        crop.save(out)
        print("wrote", out.name, f"{crop.width}x{crop.height}", f"Y{y0}-{y1}")
