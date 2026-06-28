#!/usr/bin/env python3
"""FP-0002 V8 CF-004 browser baseline / parity capture (before or after)."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE_ROOT = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-004-evidence")
AUDIT = ROOT / "audits" / "cf-004-founder-quote"

PHASE = sys.argv[1] if len(sys.argv) > 1 else "before"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4194

PAGES = [
    ("home", "index.html"),
    ("services-hub", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
    ("services-legacy", "uslugi.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

QUOTE_JS = """() => {
  const section = document.querySelector('.home-founder-quote, .founder-quote');
  const labelId = section ? section.getAttribute('aria-labelledby') : null;
  const label = labelId ? document.getElementById(labelId) : null;
  const cta = section ? section.querySelector('.home-founder-quote__cta, .founder-quote__cta') : null;
  const photo = section ? section.querySelector('.home-founder-quote__photo, .founder-quote__photo') : null;
  const quote = section ? section.querySelector('.home-founder-quote__quote, .founder-quote__quote') : null;
  const rect = (el) => el ? el.getBoundingClientRect() : null;
  const sectionRect = rect(section);
  const ctaRect = rect(cta);
  const style = (el) => el ? getComputedStyle(el) : null;
  const sectionStyle = style(section);
  const layout = section ? section.querySelector('.home-founder-quote__layout, .founder-quote__layout') : null;
  const layoutStyle = style(layout);
  return {
    neutralRootCount: document.querySelectorAll('.founder-quote').length,
    oldRootCount: document.querySelectorAll('.home-founder-quote').length,
    quoteCount: document.querySelectorAll('.home-founder-quote, .founder-quote').length,
    sectionClass: section ? section.className : null,
    labelId,
    labelText: label ? label.textContent.trim() : null,
    labelResolves: !!(labelId && label),
    ctaText: cta ? cta.textContent.replace(/\\s+/g, ' ').trim() : null,
    ctaModalOpen: cta ? cta.getAttribute('data-modal-open') : null,
    ctaModalSource: cta ? cta.getAttribute('data-modal-source') : null,
    photoSrc: photo ? photo.getAttribute('src') : null,
    photoAlt: photo ? photo.getAttribute('alt') : null,
    quoteTag: quote ? quote.tagName : null,
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    boundingBox: sectionRect ? {
      x: Math.round(sectionRect.x),
      y: Math.round(sectionRect.y),
      width: Math.round(sectionRect.width),
      height: Math.round(sectionRect.height)
    } : null,
    ctaBox: ctaRect ? {
      x: Math.round(ctaRect.x),
      y: Math.round(ctaRect.y),
      width: Math.round(ctaRect.width),
      height: Math.round(ctaRect.height)
    } : null,
    computed: {
      sectionDisplay: sectionStyle ? sectionStyle.display : null,
      layoutGridTemplateColumns: layoutStyle ? layoutStyle.gridTemplateColumns : null,
      layoutGap: layoutStyle ? layoutStyle.gap : null,
    }
  };
}"""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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

    quote = page.evaluate(QUOTE_JS)
    return {
        "http_status": response.status if response else None,
        "quote": quote,
        "console_errors": console_errors,
        "page_errors": page_errors,
        "failed_requests": failed_requests,
    }


def classify(entry: dict, phase: str) -> str:
    if entry.get("http_status") != 200:
        return "FAIL"
    if entry.get("console_errors") or entry.get("page_errors") or entry.get("failed_requests"):
        return "FAIL"
    q = entry["quote"]
    if q["quoteCount"] != 1:
        return "FAIL"
    if not q["labelResolves"]:
        return "FAIL"
    if q["overflow"]:
        return "FAIL"
    if phase == "before" and q["oldRootCount"] != 1:
        return "FAIL"
    if phase == "after" and (q["neutralRootCount"] != 1 or q["oldRootCount"] != 0):
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
                quote_path = storage / f"{base}-quote-crop.png"
                context_path = storage / f"{base}-quote-context.png"

                page = browser.new_page(viewport={"width": width, "height": height})
                data = capture_page(page, url)
                page.screenshot(path=str(full_path), full_page=True)

                section = page.locator(".home-founder-quote, .founder-quote").first
                if section.count():
                    section.scroll_into_view_if_needed()
                    page.wait_for_timeout(200)
                    box = section.bounding_box()
                    if box and box["height"] > 0:
                        clip_h = min(box["height"] + 8, max(900 - max(0, box["y"] - 4), 200))
                        page.screenshot(
                            path=str(quote_path),
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
                    "viewport_size": {"width": width, "height": height},
                    "url": url,
                    "captured_at": captured_at,
                    **data,
                }
                entry["result"] = classify(entry, PHASE)
                results.append(entry)

                q = entry["quote"]
                matrix.append(
                    {
                        "page": page_id,
                        "viewport": viewport_id,
                        "structure": q["sectionClass"],
                        "bounding_box": q["boundingBox"],
                        "computed": q["computed"],
                        "overflow": q["overflow"],
                        "result": entry["result"],
                    }
                )

                for kind, path in (
                    ("fullpage", full_path),
                    ("quote_crop", quote_path),
                    ("quote_context", context_path),
                ):
                    if path.exists():
                        screenshots.append(
                            {
                                "page_id": page_id,
                                "viewport": viewport_id,
                                "kind": kind,
                                "storage_path": str(path),
                                "sha256": sha256_file(path),
                            }
                        )
                page.close()
        browser.close()

    overall = "PASS" if all(r["result"] == "PASS" for r in results) else "FAIL"
    manifest_name = "CF-004-BEFORE-SCREENSHOT-MANIFEST.json" if PHASE == "before" else "CF-004-AFTER-SCREENSHOT-MANIFEST.json"
    manifest = {
        "manifest_id": f"FP-0002-V8-CF-004-{PHASE.upper()}-BROWSER-QA",
        "manifest_line": f"CF-004 {PHASE} browser QA evidence (screenshots external to Git)",
        "phase": PHASE,
        "captured_at": captured_at,
        "port": PORT,
        "overall": overall,
        "screenshots_storage": str(storage),
        "screenshots": screenshots,
        "matrix": matrix,
        "entries": results,
    }
    (AUDIT / manifest_name).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"phase": PHASE, "overall": overall, "entries": len(results)}, indent=2))
    if overall != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
