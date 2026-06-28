#!/usr/bin/env python3
"""FP-0002 V8 CF-005 browser baseline / parity capture (before or after)."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-005-evidence")
AUDIT = ROOT / "audits" / "cf-005-specialists"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4195

PAGES = [
    ("home", "index.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

SPECIALISTS_JS = """() => {
  const section = document.querySelector('.home-specialists, .specialists');
  const labelId = section ? section.getAttribute('aria-labelledby') : null;
  const label = labelId ? document.getElementById(labelId) : null;
  const slider = section ? section.querySelector('[data-specialists-slider]') : null;
  const pagination = section ? section.querySelector('[data-specialists-pagination]') : null;
  const cards = section ? section.querySelectorAll('.home-specialists__card, .specialists__card') : [];
  const slides = section ? section.querySelectorAll('.swiper-slide') : [];
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const sectionRect = rect(section);
  const sliderRect = rect(slider);
  const style = (el) => el ? getComputedStyle(el) : null;
  const sectionStyle = style(section);
  const heading = section ? section.querySelector('.home-specialists__heading, .specialists__heading') : null;
  return {
    neutralRootCount: document.querySelectorAll('.specialists').length,
    oldRootCount: document.querySelectorAll('.home-specialists').length,
    specialistsCount: document.querySelectorAll('.home-specialists, .specialists').length,
    sectionClass: section ? section.className : null,
    labelId,
    labelText: label ? label.textContent.trim() : null,
    labelResolves: !!(labelId && label),
    slideCount: slides.length,
    cardCount: cards.length,
    swiperInstance: !!(slider && slider.swiper),
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
    sliderBox: sliderRect ? {
      x: Math.round(sliderRect.x),
      y: Math.round(sliderRect.y),
      width: Math.round(sliderRect.width),
      height: Math.round(sliderRect.height)
    } : null,
    computed: {
      sectionDisplay: sectionStyle ? sectionStyle.display : null,
      headingFontSize: heading ? getComputedStyle(heading).fontSize : null,
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
    page.evaluate("window.scrollTo(0, 0)")

    metrics = page.evaluate(SPECIALISTS_JS)
    return {
        "http_status": response.status if response else None,
        "specialists": metrics,
        "console_errors": console_errors,
        "page_errors": page_errors,
        "failed_requests": failed_requests,
    }


def classify(entry: dict, phase: str) -> str:
    if entry.get("http_status") != 200:
        return "FAIL"
    if entry.get("console_errors") or entry.get("page_errors") or entry.get("failed_requests"):
        return "FAIL"
    s = entry["specialists"]
    if s["specialistsCount"] != 1:
        return "FAIL"
    if not s["labelResolves"]:
        return "FAIL"
    if s["slideCount"] != 5:
        return "FAIL"
    if s["overflow"]:
        return "FAIL"
    if phase == "before" and s["oldRootCount"] != 1:
        return "FAIL"
    if phase == "after" and (s["neutralRootCount"] != 1 or s["oldRootCount"] != 0):
        return "FAIL"
    return "PASS"


def main() -> None:
    storage = STORAGE_ROOT / PHASE
    storage.mkdir(parents=True, exist_ok=True)
    captured_at = datetime.now(timezone.utc).isoformat()
    results: list[dict] = []
    matrix: list[dict] = []
    screenshots: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_id, page_file in PAGES:
            for viewport_id, width, height in VIEWPORTS:
                url = f"http://127.0.0.1:{PORT}/{page_file}"
                base = f"{page_id}-{viewport_id}"
                full_path = storage / f"{base}-fullpage.png"
                crop_path = storage / f"{base}-specialists-crop.png"
                context_path = storage / f"{base}-specialists-context.png"

                page = browser.new_page(viewport={"width": width, "height": height})
                data = capture_page(page, url)
                page.screenshot(path=str(full_path), full_page=True)

                section = page.locator(".home-specialists, .specialists").first
                if section.count():
                    section.scroll_into_view_if_needed()
                    page.wait_for_timeout(200)
                    page.evaluate("""() => {
                      const root = document.querySelector('.home-specialists, .specialists');
                      if (!root) return;
                      const slider = root.querySelector('[data-specialists-slider]');
                      if (slider && slider.swiper) slider.swiper.slideTo(0, 0);
                    }""")
                    page.wait_for_timeout(150)
                    box = section.bounding_box()
                    if box and box["height"] > 0:
                        clip_h = min(box["height"] + 8, max(900 - max(0, box["y"] - 4), 200))
                        page.screenshot(
                            path=str(crop_path),
                            clip={
                                "x": 0,
                                "y": max(0, box["y"] - 4),
                                "width": width,
                                "height": clip_h,
                            },
                        )
                        prev = section.locator("xpath=preceding-sibling::*[1]").first
                        next_el = section.locator("xpath=following-sibling::*[1]").first
                        clip_y = max(0, box["y"] - 80)
                        clip_h = box["height"] + 160
                        if prev.count():
                            pb = prev.bounding_box()
                            if pb:
                                clip_y = max(0, min(clip_y, pb["y"]))
                        if next_el.count():
                            nb = next_el.bounding_box()
                            if nb:
                                clip_h = (nb["y"] + min(nb["height"], 120)) - clip_y
                        clip_h = min(max(clip_h, 240), max(900 - clip_y, 240))
                        page.screenshot(
                            path=str(context_path),
                            clip={"x": 0, "y": clip_y, "width": width, "height": clip_h},
                        )

                entry = {
                    "page_id": page_id,
                    "page_file": page_file,
                    "viewport": viewport_id,
                    "width": width,
                    "height": height,
                    "url": url,
                    **data,
                }
                entry["result"] = classify(entry, PHASE)
                results.append(entry)
                matrix.append(
                    {
                        "page": page_id,
                        "viewport": viewport_id,
                        "http": entry["http_status"],
                        "console_errors": len(entry["console_errors"]),
                        "failed_requests": len(entry["failed_requests"]),
                        "overflow": entry["specialists"]["overflow"],
                        "slide_count": entry["specialists"]["slideCount"],
                        "result": entry["result"],
                    }
                )
                for kind, path in [
                    ("fullpage", full_path),
                    ("specialists_crop", crop_path),
                    ("specialists_context", context_path),
                ]:
                    if path.exists():
                        screenshots.append(
                            {
                                "page": page_id,
                                "viewport": viewport_id,
                                "kind": kind,
                                "path": str(path),
                                "sha256": sha256_file(path),
                            }
                        )
                page.close()

        browser.close()

    manifest_name = f"CF-005-{'BEFORE' if PHASE == 'before' else 'AFTER'}-SCREENSHOT-MANIFEST.json"
    payload = {
        "manifest_id": manifest_name.replace(".json", ""),
        "phase": PHASE,
        "captured_at": captured_at,
        "port": PORT,
        "storage_root": str(storage),
        "pages": PAGES,
        "viewports": VIEWPORTS,
        "matrix": matrix,
        "results": results,
        "screenshots": screenshots,
        "overall": "PASS" if all(r["result"] == "PASS" for r in results) else "FAIL",
    }
    (AUDIT / manifest_name).write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"phase": PHASE, "overall": payload["overall"], "rows": len(results)}, indent=2))
    if payload["overall"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
