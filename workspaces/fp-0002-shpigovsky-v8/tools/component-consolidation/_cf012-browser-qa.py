#!/usr/bin/env python3
"""FP-0002 V8 CF-012 program block browser baseline / parity capture."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(
    r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-012-evidence"
)
AUDIT = ROOT / "audits" / "cf-012-program-modifiers"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4199

CONSUMERS = [
    ("hub-services-program", "uslugi-v2.html", "#services-program"),
    ("subdivision-program", "usluga-podrazdel-v1.html", "#service-subdivision-program"),
    ("leaf-program", "usluga-konechnaya-v1.html", "#service-leaf-program"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

PROGRAM_JS = """(selector) => {
  const section = document.querySelector(selector);
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const mods = section ? section.className.split(/\\s+/).filter(c => c.startsWith('services-program-v2')) : [];
  const cta = section ? section.querySelector('.program-cta-band') : null;
  const imgs = section ? [...section.querySelectorAll('img')] : [];
  const imagesReady = imgs.length > 0 && imgs.every((img) => img.complete && img.naturalHeight > 0);
  return {
    found: !!section,
    modifiers: mods,
    childCount: section ? section.querySelectorAll('.services-program-v2__item').length : 0,
    ctaInSection: !!cta,
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    box: rect(section),
    imagesReady,
    sectionHeight: section ? getComputedStyle(section).height : null,
  };
}"""

WAIT_JS = """(selector) => {
  const section = document.querySelector(selector);
  if (!section) return false;
  section.scrollIntoView({ block: 'start' });
  const imgs = [...section.querySelectorAll('img')];
  return imgs.every((img) => img.complete);
}"""


def main() -> None:
    out_dir = STORAGE_ROOT / PHASE
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_rows: list[dict] = []
    metrics_rows: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for vp_name, width, height in VIEWPORTS:
            context = browser.new_context(viewport={"width": width, "height": height})
            page = context.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda err: errors.append(str(err)))
            for consumer_id, page_file, selector in CONSUMERS:
                url = f"http://127.0.0.1:{PORT}/{page_file}"
                page.goto(url, wait_until="networkidle")
                page.wait_for_function(WAIT_JS, arg=selector, timeout=60000)
                page.wait_for_timeout(500)
                metrics = page.evaluate(PROGRAM_JS, selector)
                stem = f"{consumer_id}__{vp_name}"
                page.screenshot(path=str(out_dir / f"{stem}__full.png"), full_page=True)
                section = page.query_selector(selector)
                if section:
                    section.screenshot(path=str(out_dir / f"{stem}__program-crop.png"))
                    section.evaluate(
                        "el => el.scrollIntoView({block: 'start'})"
                    )
                    page.screenshot(path=str(out_dir / f"{stem}__program-top.png"))
                    cta = section.query_selector(".program-cta-band")
                    if cta:
                        cta.screenshot(path=str(out_dir / f"{stem}__cta-context.png"))
                manifest_rows.append(
                    {
                        "consumer": consumer_id,
                        "viewport": vp_name,
                        "page": page_file,
                        "selector": selector,
                        "full": str(out_dir / f"{stem}__full.png"),
                        "program_crop": str(out_dir / f"{stem}__program-crop.png"),
                    }
                )
                metrics_rows.append(
                    {
                        "consumer": consumer_id,
                        "viewport": vp_name,
                        "found": metrics.get("found"),
                        "modifiers": metrics.get("modifiers"),
                        "child_count": metrics.get("childCount"),
                        "cta_in_section": metrics.get("ctaInSection"),
                        "images_ready": metrics.get("imagesReady"),
                        "section_height": metrics.get("sectionHeight"),
                        "overflow": metrics.get("overflow"),
                        "console_errors": len(errors),
                        "result": "PASS"
                        if metrics.get("found") and not metrics.get("overflow")
                        else "FAIL",
                    }
                )
            context.close()
        browser.close()

    manifest = {
        "phase": PHASE,
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "port": PORT,
        "items": manifest_rows,
    }
    (AUDIT / f"CF-012-{PHASE.upper()}-SCREENSHOT-MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (AUDIT / "data" / f"CF-012-BROWSER-METRICS-{PHASE}.json").write_text(
        json.dumps(metrics_rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"phase": PHASE, "items": len(manifest_rows)}, indent=2))


if __name__ == "__main__":
    main()
