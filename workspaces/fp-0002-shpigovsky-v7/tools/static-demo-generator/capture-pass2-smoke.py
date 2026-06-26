"""FP-0002 PASS 2 representative visual smoke screenshots."""
from pathlib import Path
import json
import subprocess
import sys
import time

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
OUT = ROOT / "plans/static-client-demo/evidence/screenshots/pass-2-smoke"
OUT.mkdir(parents=True, exist_ok=True)

PAGES = [
    ("home", "index.html", "HOME_PAGE_TEMPLATE"),
    ("services-hub", "uslugi/index.html", "SERVICES_HUB_INTERNAL_PAGE"),
    ("subdivision-genotipirovanie", "uslugi/genotipirovanie/index.html", "SERVICE_SUBDIVISION_INTERNAL_PAGE"),
    ("subdivision-zavisimosti", "uslugi/zavisimosti/index.html", "SERVICE_SUBDIVISION_INTERNAL_PAGE"),
    ("leaf-alkogol", "uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html", "SERVICE_LEAF_INTERNAL_PAGE"),
    ("leaf-depressiya", "uslugi/psihicheskoe-zdorovie/depressiya/index.html", "SERVICE_LEAF_INTERNAL_PAGE"),
    ("leaf-ptsr", "uslugi/psihicheskoe-zdorovie/ptsr/index.html", "SERVICE_LEAF_INTERNAL_PAGE"),
    ("placeholder-specialisty", "specialisty/index.html", "PLACEHOLDER_PAGE"),
    ("placeholder-privacy", "privacy-policy/index.html", "PLACEHOLDER_PAGE"),
    ("placeholder-reserved", "uslugi/psihicheskoe-zdorovie/nazvanie-slot-01/index.html", "PLACEHOLDER_PAGE"),
]

server = subprocess.Popen(
    [sys.executable, "-m", "http.server", "4175", "--directory", str(DIST)],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
time.sleep(1.5)

meta = {"pages": [], "output_dir": str(OUT)}

try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for slug, rel, template in PAGES:
            url = f"http://127.0.0.1:4175/{rel.replace('index.html', '')}"
            for label, width in [("desktop", 1437), ("mobile", 380)]:
                page = browser.new_page(viewport={"width": width, "height": 2000})
                page.goto(url, wait_until="networkidle")
                page.wait_for_timeout(400)
                file_name = f"{slug}-{label}-{width}.png"
                shot = OUT / file_name
                page.screenshot(path=str(shot), full_page=True)
                overflow = page.evaluate(
                    "() => document.documentElement.scrollWidth > document.documentElement.clientWidth"
                )
                meta["pages"].append(
                    {
                        "slug": slug,
                        "template": template,
                        "viewport": label,
                        "file": file_name,
                        "overflow": overflow,
                        "url": url,
                    }
                )
                page.close()
        browser.close()
finally:
    server.terminate()

(OUT / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("screenshots", len(meta["pages"]))
