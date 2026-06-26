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

# GROUP 2: after CTA-01 (Y~1820) through before approach heading (Y~2493 desktop)
DESKTOP = [
    ("SERVICE-LEAF-D-G2-01-BOUNDARY-START", 1780, 1920),
    ("SERVICE-LEAF-D-G2-02-SIGNS-HEADING-INTRO", 1820, 1980),
    ("SERVICE-LEAF-D-G2-03-EDITORIAL-UPPER", 1980, 2140),
    ("SERVICE-LEAF-D-G2-04-EDITORIAL-MIDDLE", 2140, 2280),
    ("SERVICE-LEAF-D-G2-05-EDITORIAL-LOWER", 2280, 2420),
    ("SERVICE-LEAF-D-G2-06-LINKS-ACCENTS", 2320, 2480),
    ("SERVICE-LEAF-D-G2-07-BOUNDARY-END", 2460, 2580),
    ("SERVICE-LEAF-D-G2-FULL", 1820, 2493),
]

MOBILE = [
    ("SERVICE-LEAF-M-G2-01-BOUNDARY-START", 2340, 2520),
    ("SERVICE-LEAF-M-G2-02-SIGNS-HEADING-INTRO", 2394, 2620),
    ("SERVICE-LEAF-M-G2-03-EDITORIAL-UPPER", 2620, 2900),
    ("SERVICE-LEAF-M-G2-04-EDITORIAL-MIDDLE", 2900, 3180),
    ("SERVICE-LEAF-M-G2-05-EDITORIAL-LOWER", 3180, 3460),
    ("SERVICE-LEAF-M-G2-06-LINKS-ACCENTS", 3400, 3580),
    ("SERVICE-LEAF-M-G2-07-BOUNDARY-END", 3580, 3720),
    ("SERVICE-LEAF-M-G2-FULL", 2394, 3655),
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
