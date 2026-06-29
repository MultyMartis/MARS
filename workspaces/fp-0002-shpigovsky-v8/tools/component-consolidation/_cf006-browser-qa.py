#!/usr/bin/env python3
"""FP-0002 V8 CF-006 browser baseline / parity capture (before or after)."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-006-evidence")
AUDIT = ROOT / "audits" / "cf-006-comfort"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4196

PAGES = [
    ("home", "index.html"),
    ("uslugi", "uslugi.html"),
    ("uslugi-v2", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

COMFORT_JS = """() => {
  const section = document.querySelector('.home-comfort, .comfort');
  const labelId = section ? section.getAttribute('aria-labelledby') : null;
  const label = labelId ? document.getElementById(labelId) : null;
  const gallery = section ? section.querySelector('.home-comfort__gallery, .comfort__gallery') : null;
  const items = gallery ? gallery.querySelectorAll('.home-comfort__gallery-item, .comfort__gallery-item') : [];
  const links = gallery ? gallery.querySelectorAll('[data-fancybox]') : [];
  const group = links.length ? links[0].getAttribute('data-fancybox') : null;
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const sectionRect = rect(section);
  const galleryRect = rect(gallery);
  const heading = section ? section.querySelector('.home-comfort__heading, .comfort__heading') : null;
  return {
    neutralRootCount: document.querySelectorAll('.comfort').length,
    oldRootCount: document.querySelectorAll('.home-comfort').length,
    comfortCount: document.querySelectorAll('.home-comfort, .comfort').length,
    sectionClass: section ? section.className : null,
    labelId,
    labelText: label ? label.textContent.trim() : null,
    labelResolves: !!(labelId && label),
    itemCount: items.length,
    linkCount: links.length,
    galleryGroup: group,
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
    galleryBox: galleryRect ? {
      x: Math.round(galleryRect.x),
      y: Math.round(galleryRect.y),
      width: Math.round(galleryRect.width),
      height: Math.round(galleryRect.height)
    } : null,
    computed: {
      galleryDisplay: gallery ? getComputedStyle(gallery).display : null,
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

    metrics = page.evaluate(COMFORT_JS)
    return {
        "http_status": response.status if response else None,
        "comfort": metrics,
        "console_errors": console_errors,
        "page_errors": page_errors,
        "failed_requests": failed_requests,
    }


def classify(entry: dict, phase: str) -> str:
    if entry.get("http_status") != 200:
        return "FAIL"
    if entry.get("console_errors") or entry.get("page_errors") or entry.get("failed_requests"):
        return "FAIL"
    c = entry["comfort"]
    if c["comfortCount"] != 1:
        return "FAIL"
    if not c["labelResolves"]:
        return "FAIL"
    if c["itemCount"] != 7:
        return "FAIL"
    if c["linkCount"] != 6:
        return "FAIL"
    if c["overflow"]:
        return "FAIL"
    if phase == "before" and c["oldRootCount"] != 1:
        return "FAIL"
    if phase == "after" and (c["neutralRootCount"] != 1 or c["oldRootCount"] != 0):
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
                crop_path = storage / f"{base}-comfort-crop.png"
                context_path = storage / f"{base}-comfort-context.png"

                page = browser.new_page(viewport={"width": width, "height": height})
                data = capture_page(page, url)
                page.screenshot(path=str(full_path), full_page=True)

                section = page.locator(".home-comfort, .comfort").first
                if section.count():
                    section.scroll_into_view_if_needed()
                    page.wait_for_timeout(200)
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
                        "overflow": entry["comfort"]["overflow"],
                        "item_count": entry["comfort"]["itemCount"],
                        "gallery_group": entry["comfort"]["galleryGroup"],
                        "result": entry["result"],
                    }
                )
                for kind, path in [
                    ("fullpage", full_path),
                    ("comfort_crop", crop_path),
                    ("comfort_context", context_path),
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

    manifest_name = f"CF-006-{'BEFORE' if PHASE == 'before' else 'AFTER'}-SCREENSHOT-MANIFEST.json"
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
