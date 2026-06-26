import hashlib
import shutil
from pathlib import Path

design_dir = Path(
    r"C:\MARS Phenix\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\26.06.2026"
)
out_dir = Path(__file__).parent / "design-rasters"
out_dir.mkdir(parents=True, exist_ok=True)

desktop_src = next(
    p
    for p in design_dir.iterdir()
    if p.suffix.lower() == ".png"
    and "десктоп" in p.name
    and p.name.startswith("Услуга")
    and "подраздел" not in p.name
)
mobile_src = next(
    p
    for p in design_dir.iterdir()
    if p.suffix.lower() == ".png"
    and "мобильная" in p.name
    and p.name.startswith("Услуга")
    and "подраздел" not in p.name
)

pairs = [
    (desktop_src, out_dir / "SERVICE-LEAF-DESIGN-AUTHORITY-DESKTOP.png"),
    (mobile_src, out_dir / "SERVICE-LEAF-DESIGN-AUTHORITY-MOBILE.png"),
]

from PIL import Image

for src, dst in pairs:
    shutil.copy2(src, dst)
    data = dst.read_bytes()
    h = hashlib.sha256(data).hexdigest().upper()
    with Image.open(dst) as im:
        print(dst.name, f"{im.width}x{im.height}", h, "source", src.name)
