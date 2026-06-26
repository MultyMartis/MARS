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

# Y boundaries from block registry + PNG walk (GROUP 1 ends before signs at ~1820)
DESKTOP = [
    ("SERVICE-LEAF-D-G1-01-HEADER-HERO", 0, 780),
    ("SERVICE-LEAF-D-G1-02-BREADCRUMBS-SUBNAV", 780, 980),
    ("SERVICE-LEAF-D-G1-03-INTRO-QUOTE", 980, 1180),
    ("SERVICE-LEAF-D-G1-04-BORDERED-INFO", 1180, 1660),
    ("SERVICE-LEAF-D-G1-05-CTA-01", 1660, 1820),
    ("SERVICE-LEAF-D-G1-06-BOUNDARY", 1810, 1880),
]

MOBILE = [
    ("SERVICE-LEAF-M-G1-01-HEADER-HERO", 0, 520),
    ("SERVICE-LEAF-M-G1-02-BREADCRUMBS-SUBNAV", 520, 720),
    ("SERVICE-LEAF-M-G1-03-INTRO-QUOTE", 720, 1100),
    ("SERVICE-LEAF-M-G1-04-BORDERED-INFO", 1100, 2100),
    ("SERVICE-LEAF-M-G1-05-CTA-01", 2100, 2380),
    ("SERVICE-LEAF-M-G1-06-BOUNDARY", 2370, 2520),
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
        print("wrote", out.name, f"{crop.width}x{crop.height}")
