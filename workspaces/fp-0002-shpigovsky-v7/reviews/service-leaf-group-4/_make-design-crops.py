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
    ("SERVICE-LEAF-D-G4-01-BOUNDARY-START", 4480, 4680),
    ("SERVICE-LEAF-D-G4-02-PROGRAM-HEADING-INTRO", 4560, 4920),
    ("SERVICE-LEAF-D-G4-03-PROGRAM-CARDS-UPPER", 4920, 5420),
    ("SERVICE-LEAF-D-G4-04-PROGRAM-CARDS-LOWER", 5420, 6020),
    ("SERVICE-LEAF-D-G4-05-PROGRAM-TRANSITION", 6020, 6250),
    ("SERVICE-LEAF-D-G4-FULL", 4560, 6180),
]

MOBILE = [
    ("SERVICE-LEAF-M-G4-01-BOUNDARY-START", 5420, 5580),
    ("SERVICE-LEAF-M-G4-02-PROGRAM-HEADING-INTRO", 5503, 5850),
    ("SERVICE-LEAF-M-G4-03-PROGRAM-CARD-01", 5850, 6300),
    ("SERVICE-LEAF-M-G4-04-PROGRAM-CARD-02", 6300, 6750),
    ("SERVICE-LEAF-M-G4-05-PROGRAM-CARD-03", 6750, 7200),
    ("SERVICE-LEAF-M-G4-06-PROGRAM-CARD-04", 7200, 7650),
    ("SERVICE-LEAF-M-G4-07-PROGRAM-TRANSITION", 7580, 7780),
    ("SERVICE-LEAF-M-G4-FULL", 5503, 7687),
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
