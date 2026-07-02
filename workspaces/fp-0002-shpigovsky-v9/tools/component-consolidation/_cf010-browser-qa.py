#!/usr/bin/env python3
"""FP-0002 V8 CF-010 browser baseline / parity capture."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(
    r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-010-evidence"
)
AUDIT = ROOT / "audits" / "cf-010-clinic-landscape"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4198

CONSUMERS = [
    ("home", "index.html", ".home-clinic-landscape, .clinic-landscape"),
    ("service-subdivision", "usluga-podrazdel-v1.html", ".home-clinic-landscape, .clinic-landscape"),
    ("service-leaf", "usluga-konechnaya-v1.html", ".home-clinic-landscape, .clinic-landscape"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

LANDSCAPE_JS = """(selector) => {
  const section = document.querySelector(selector);
  const img = section ? section.querySelector('img') : null;
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const cs = (el) => el ? getComputedStyle(el) : null;
  const imgCs = cs(img);
  return {
    sectionFound: !!section,
    sectionClass: section ? section.className : null,
    oldRootCount: document.querySelectorAll('.home-clinic-landscape').length,
    neutralRootCount: document.querySelectorAll('.clinic-landscape').length,
    ariaLabel: section ? section.getAttribute('aria-label') : null,
    imgSrc: img ? img.getAttribute('src') : null,
    imgAlt: img ? img.getAttribute('alt') : null,
    imgNatural: img ? { w: img.naturalWidth, h: img.naturalHeight } : null,
    imgRendered: img ? { w: Math.round(img.offsetWidth), h: Math.round(img.offsetHeight) } : null,
    objectFit: imgCs ? imgCs.objectFit : null,
    objectPosition: imgCs ? imgCs.objectPosition : null,
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    boundingBox: rect(section) ? {
      x: Math.round(rect(section).x),
      y: Math.round(rect(section).y),
      width: Math.round(rect(section).width),
      height: Math.round(rect(section).height)
    } : null,
    imgBox: rect(img) ? {
      x: Math.round(rect(img).x),
      y: Math.round(rect(img).y),
      width: Math.round(rect(img).width),
      height: Math.round(rect(img).height)
    } : null,
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
            console_errors: list[str] = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            page.on("pageerror", lambda err: console_errors.append(str(err)))
            for consumer_id, page_file, selector in CONSUMERS:
                url = f"http://127.0.0.1:{PORT}/{page_file}"
                page.goto(url, wait_until="networkidle")
                page.evaluate(
                    """(selector) => {
                      const section = document.querySelector(selector);
                      if (section) section.scrollIntoView({block: 'center'});
                    }""",
                    selector,
                )
                page.wait_for_function(
                    """(selector) => {
                      const section = document.querySelector(selector);
                      const img = section ? section.querySelector('img') : null;
                      return !!(img && img.complete && img.naturalWidth > 0);
                    }""",
                    arg=selector,
                    timeout=15000,
                )
                metrics = page.evaluate(LANDSCAPE_JS, selector)
                stem = f"{consumer_id}__{vp_name}"
                full_path = out_dir / f"{stem}__full.png"
                page.screenshot(path=str(full_path), full_page=True)
                section = page.query_selector(selector)
                if section:
                    section.screenshot(path=str(out_dir / f"{stem}__landscape-crop.png"))
                    section.evaluate(
                        """(el) => {
                          el.scrollIntoView({block: 'center'});
                          const prev = el.previousElementSibling;
                          const next = el.nextElementSibling;
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
                        "landscape_crop": str(out_dir / f"{stem}__landscape-crop.png"),
                        "context": str(out_dir / f"{stem}__context.png"),
                    }
                )
                metrics_rows.append(
                    {
                        "consumer": consumer_id,
                        "viewport": vp_name,
                        "console_errors": len(console_errors),
                        "overflow": metrics.get("overflow"),
                        "section_found": metrics.get("sectionFound"),
                        "img_loaded": bool(metrics.get("imgNatural", {}).get("w")),
                        **{k: metrics.get(k) for k in [
                            "sectionClass", "oldRootCount", "neutralRootCount",
                            "imgSrc", "imgAlt", "objectFit", "objectPosition",
                            "boundingBox", "imgBox", "imgRendered"
                        ]},
                        "result": "PASS"
                        if metrics.get("sectionFound") and not metrics.get("overflow")
                        else "FAIL",
                    }
                )
            context.close()
        browser.close()

    manifest = {
        "phase": PHASE,
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "port": PORT,
        "manual_polish_authority": "472be1abffb666a836eb83d5644e1fd3a233cc2d",
        "items": manifest_rows,
    }
    manifest_name = f"CF-010-{PHASE.upper()}-SCREENSHOT-MANIFEST.json"
    (AUDIT / manifest_name).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (AUDIT / "data" / f"CF-010-BROWSER-METRICS-{PHASE}.json").write_text(
        json.dumps({"metrics": metrics_rows}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"phase": PHASE, "shots": len(manifest_rows)}, indent=2))


if __name__ == "__main__":
    main()
