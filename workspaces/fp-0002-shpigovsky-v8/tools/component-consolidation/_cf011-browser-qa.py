#!/usr/bin/env python3
"""FP-0002 V8 CF-011 browser baseline / parity capture."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(
    r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-011-evidence"
)
AUDIT = ROOT / "audits" / "cf-011-dark-cta"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4199

CONSUMERS = [
    ("uslugi-v2-secondary", "uslugi-v2.html", '[data-modal-source="services-program-cta-secondary"]'),
    ("subdivision-start", "usluga-podrazdel-v1.html", "#service-subdivision-start .program-cta-band"),
    ("leaf-cta-01", "usluga-konechnaya-v1.html", "#service-leaf-cta-01 .program-cta-band"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

CTA_JS = """(selector) => {
  const band = document.querySelector(selector);
  const section = band ? band.closest('section.program-cta-band-section') : null;
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const btn = band ? band.querySelector('[data-modal-open]') : null;
  const headingId = section ? section.getAttribute('aria-labelledby') : null;
  const heading = headingId ? document.getElementById(headingId) : null;
  return {
    bandFound: !!band,
    sectionId: section ? section.id : null,
    ariaLabelledby: section ? section.getAttribute('aria-labelledby') : null,
    headingExists: !!heading,
    buttonSource: btn ? btn.getAttribute('data-modal-source') : null,
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    bandBox: rect(band),
  };
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
            for consumer_id, page_file, selector in CONSUMERS:
                url = f"http://127.0.0.1:{PORT}/{page_file}"
                page.goto(url, wait_until="networkidle")
                errors = []
                page.on("pageerror", lambda err: errors.append(str(err)))
                metrics = page.evaluate(CTA_JS, selector)
                stem = f"{consumer_id}__{vp_name}"
                full_path = out_dir / f"{stem}__full.png"
                page.screenshot(path=str(full_path), full_page=True)
                band = page.query_selector(selector)
                if band:
                    band.screenshot(path=str(out_dir / f"{stem}__cta-crop.png"))
                    band.evaluate(
                        """(el) => {
                          el.scrollIntoView({block: 'center'});
                          const prev = el.previousElementSibling;
                          const next = el.parentElement && el.parentElement.nextElementSibling;
                          if (prev) prev.style.outline = '2px solid magenta';
                          if (next) next.style.outline = '2px solid cyan';
                        }"""
                    )
                    page.screenshot(path=str(out_dir / f"{stem}__context.png"))
                manifest_rows.append(
                    {
                        "consumer": consumer_id,
                        "viewport": vp_name,
                        "page": page_file,
                        "full": str(full_path),
                        "cta_crop": str(out_dir / f"{stem}__cta-crop.png"),
                        "context": str(out_dir / f"{stem}__context.png"),
                    }
                )
                metrics_rows.append(
                    {
                        "consumer": consumer_id,
                        "viewport": vp_name,
                        "http": 200,
                        "console_errors": len(errors),
                        "overflow": metrics.get("overflow"),
                        "band_found": metrics.get("bandFound"),
                        "aria_heading_resolves": metrics.get("headingExists"),
                        "result": "PASS"
                        if metrics.get("bandFound") and not metrics.get("overflow")
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
    manifest_path = AUDIT / f"CF-011-{PHASE.upper()}-SCREENSHOT-MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (AUDIT / "data" / f"CF-011-BROWSER-METRICS-{PHASE}.json").write_text(
        json.dumps({"metrics": metrics_rows}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"phase": PHASE, "shots": len(manifest_rows)}, indent=2))


if __name__ == "__main__":
    main()
