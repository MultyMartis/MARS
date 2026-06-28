#!/usr/bin/env python3
"""FP-0002 V8 CF-007 browser baseline / parity capture (before or after)."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-007-evidence")
AUDIT = ROOT / "audits" / "cf-007-reviews"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4197

PAGES = [
    ("home", "index.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

REVIEWS_JS = """() => {
  const section = document.querySelector('.home-reviews, .reviews');
  const slider = section ? section.querySelector('[data-reviews-slider]') : null;
  const pagination = section ? section.querySelector('[data-reviews-pagination]') : null;
  const slides = slider ? slider.querySelectorAll('.swiper-slide') : [];
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const sectionRect = rect(section);
  const heading = section ? section.querySelector('.home-reviews__title, .reviews__title') : null;
  const sw = slider && slider.swiper ? slider.swiper : null;
  return {
    neutralRootCount: document.querySelectorAll('.reviews').length,
    oldRootCount: document.querySelectorAll('.home-reviews').length,
    reviewsCount: document.querySelectorAll('.home-reviews, .reviews').length,
    sectionClass: section ? section.className : null,
    sectionId: section ? section.id || null : null,
    slideCount: slides.length,
    activeIndex: sw ? sw.activeIndex : null,
    visibleSlides: sw ? sw.params.slidesPerView : null,
    hasSwiper: !!(slider && slider.swiper),
    paginationPresent: !!pagination,
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
    computed: {
      headingFontSize: heading ? getComputedStyle(heading).fontSize : null,
      sectionOverflow: section ? getComputedStyle(section).overflow : null,
    }
  };
}"""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def capture_page(page, url: str) -> dict:
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
    section = page.locator(".home-reviews, .reviews").first
    section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.evaluate(
        """() => {
          const section = document.querySelector('.home-reviews, .reviews');
          const slider = section ? section.querySelector('[data-reviews-slider]') : null;
          if (slider && slider.swiper) {
            slider.swiper.slideTo(0, 0);
            slider.swiper.update();
          }
        }"""
    )
    page.wait_for_timeout(600)
    page.evaluate("window.scrollTo(0, 0)")
    section.scroll_into_view_if_needed()
    page.wait_for_timeout(400)

    metrics = page.evaluate(REVIEWS_JS)
    return {
        "http_status": response.status if response else None,
        "reviews": metrics,
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
                page = browser.new_page(viewport={"width": width, "height": height})
                url = f"http://127.0.0.1:{PORT}/{page_file}"
                entry = capture_page(page, url)
                section = page.locator(".home-reviews, .reviews").first

                base = f"{page_id}-{viewport_id}"
                full_path = out_dir / f"{base}-full.png"
                crop_path = out_dir / f"{base}-reviews-crop.png"
                context_path = out_dir / f"{base}-reviews-context.png"

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
                    "screenshots": {
                        "full": str(full_path),
                        "reviews_crop": str(crop_path),
                        "reviews_context": str(context_path),
                    },
                    "sha256": {
                        "full": sha256_file(full_path) if full_path.exists() else None,
                        "reviews_crop": sha256_file(crop_path) if crop_path.exists() else None,
                    },
                    **entry,
                }
                manifest_rows.append(row)
                page.close()
        browser.close()

    manifest = {
        "manifest_id": "CF-007-BEFORE-SCREENSHOT-MANIFEST" if PHASE == "before" else "CF-007-AFTER-SCREENSHOT-MANIFEST",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "phase": PHASE,
        "port": PORT,
        "rows": manifest_rows,
    }
    manifest_name = (
        "CF-007-BEFORE-SCREENSHOT-MANIFEST.json"
        if PHASE == "before"
        else "CF-007-AFTER-SCREENSHOT-MANIFEST.json"
    )
    (AUDIT / manifest_name).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"phase": PHASE, "rows": len(manifest_rows), "manifest": str(AUDIT / manifest_name)}, indent=2))


if __name__ == "__main__":
    main()
