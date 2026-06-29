#!/usr/bin/env python3
"""FP-0002 V8 CF-008 browser baseline / parity capture (before or after)."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-008-evidence")
AUDIT = ROOT / "audits" / "cf-008-faq"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4198

PAGES = [
    ("home", "index.html"),
    ("services", "uslugi.html"),
    ("services-v2", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

FAQ_JS = """() => {
  const section = document.querySelector('.home-faq, .faq');
  const list = section ? section.querySelector('[data-accordion]') : null;
  const items = list ? list.querySelectorAll('[data-accordion-item]') : [];
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const sectionRect = rect(section);
  const heading = section ? section.querySelector('.home-faq__heading, .faq__heading') : null;
  const triggers = section ? section.querySelectorAll('[data-accordion-button]') : [];
  const openCount = Array.from(triggers).filter(b => b.getAttribute('aria-expanded') === 'true').length;
  const ariaMap = Array.from(triggers).map((b, i) => ({
    id: b.id,
    ariaExpanded: b.getAttribute('aria-expanded'),
    ariaControls: b.getAttribute('aria-controls'),
    panelHidden: (() => {
      const p = document.getElementById(b.getAttribute('aria-controls'));
      return p ? p.hidden : null;
    })()
  }));
  return {
    neutralRootCount: document.querySelectorAll('.faq').length,
    oldRootCount: document.querySelectorAll('.home-faq').length,
    faqCount: document.querySelectorAll('.home-faq, .faq').length,
    sectionClass: section ? section.className : null,
    sectionId: section ? section.id || null : null,
    itemCount: items.length,
    openItemCount: openCount,
    headingText: heading ? heading.textContent.trim() : null,
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    boundingBox: sectionRect ? {
      x: Math.round(sectionRect.x),
      y: Math.round(sectionRect.y),
      width: Math.round(sectionRect.width),
      height: Math.round(sectionRect.height)
    } : null,
    ariaMap,
    computed: {
      headingFontSize: heading ? getComputedStyle(heading).fontSize : null,
      itemBorder: items[0] ? getComputedStyle(items[0]).borderWidth : null,
    }
  };
}"""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def capture_page(page, url: str, open_first: bool) -> dict:
    console_errors: list[str] = []
    page_errors: list[str] = []
    failed_requests: list[str] = []

    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda err: page_errors.append(str(err)))
    page.on("requestfailed", lambda req: failed_requests.append(req.url))

    response = page.goto(url, wait_until="networkidle", timeout=120000)
    page.add_style_tag(
        content="*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important;}"
    )
    page.wait_for_timeout(800)
    section = page.locator(".home-faq, .faq").first
    section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    if open_first:
        page.evaluate(
            """() => {
              const section = document.querySelector('.home-faq, .faq');
              const btn = section ? section.querySelector('[data-accordion-button]') : null;
              if (btn && btn.getAttribute('aria-expanded') !== 'true') btn.click();
            }"""
        )
        page.wait_for_timeout(400)
    else:
        page.evaluate(
            """() => {
              const section = document.querySelector('.home-faq, .faq');
              const triggers = section ? section.querySelectorAll('[data-accordion-button]') : [];
              triggers.forEach((btn, idx) => {
                const panel = document.getElementById(btn.getAttribute('aria-controls'));
                const open = idx === 0;
                btn.setAttribute('aria-expanded', open ? 'true' : 'false');
                if (panel) panel.hidden = !open;
              });
            }"""
        )
        page.wait_for_timeout(300)

    metrics = page.evaluate(FAQ_JS)
    return {
        "http_status": response.status if response else None,
        "state": "open-first" if open_first else "initial",
        "faq": metrics,
        "console_errors": console_errors,
        "page_errors": page_errors,
        "failed_requests": failed_requests,
    }


def main() -> None:
    out_dir = STORAGE_ROOT / PHASE
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_rows: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_id, page_file in PAGES:
            for viewport_id, width, height in VIEWPORTS:
                for state_id, open_first in [("initial", False), ("open-first", True)]:
                    page = browser.new_page(viewport={"width": width, "height": height})
                    url = f"http://127.0.0.1:{PORT}/{page_file}"
                    entry = capture_page(page, url, open_first)
                    section = page.locator(".home-faq, .faq").first

                    base = f"{page_id}-{viewport_id}-{state_id}"
                    full_path = out_dir / f"{base}-full.png"
                    crop_path = out_dir / f"{base}-faq-crop.png"
                    context_path = out_dir / f"{base}-faq-context.png"

                    page.screenshot(path=str(full_path), full_page=True)
                    box = section.bounding_box()
                    if box:
                        page.screenshot(
                            path=str(crop_path),
                            clip={
                                "x": max(0, box["x"]),
                                "y": max(0, box["y"]),
                                "width": box["width"],
                                "height": box["height"],
                            },
                        )
                        page.screenshot(
                            path=str(context_path),
                            clip={
                                "x": 0,
                                "y": max(0, box["y"] - 80),
                                "width": width,
                                "height": min(height, box["height"] + 160),
                            },
                        )

                    row = {
                        "page": page_id,
                        "page_file": page_file,
                        "viewport": viewport_id,
                        "phase": PHASE,
                        "state": state_id,
                        "screenshots": {
                            "full": str(full_path),
                            "faq_crop": str(crop_path),
                            "faq_context": str(context_path),
                        },
                        "sha256": {
                            "full": sha256_file(full_path) if full_path.exists() else None,
                            "faq_crop": sha256_file(crop_path) if crop_path.exists() else None,
                        },
                        **entry,
                    }
                    manifest_rows.append(row)
                    page.close()
        browser.close()

    manifest = {
        "manifest_id": "CF-008-BEFORE-SCREENSHOT-MANIFEST" if PHASE == "before" else "CF-008-AFTER-SCREENSHOT-MANIFEST",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "phase": PHASE,
        "port": PORT,
        "rows": manifest_rows,
    }
    manifest_name = (
        "CF-008-BEFORE-SCREENSHOT-MANIFEST.json"
        if PHASE == "before"
        else "CF-008-AFTER-SCREENSHOT-MANIFEST.json"
    )
    (AUDIT / manifest_name).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"phase": PHASE, "rows": len(manifest_rows), "manifest": str(AUDIT / manifest_name)}, indent=2))


if __name__ == "__main__":
    main()
