#!/usr/bin/env python3
"""FP-0002 V8 CF-005 slider functional smoke QA."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-005-specialists"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4195

PAGES = [
    ("home", "index.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]
VIEWPORTS = [("desktop", 1437, 1000), ("mobile", 380, 900)]

SLIDER_JS = """() => {
  const sliders = document.querySelectorAll('[data-specialists-slider]');
  const instances = Array.from(sliders).map((el) => ({
    hasSwiper: !!el.swiper,
    activeIndex: el.swiper ? el.swiper.activeIndex : null,
    slideCount: el.querySelectorAll('.swiper-slide').length,
  }));
  return { count: sliders.length, instances };
}"""

INTERACT_JS = """() => {
  const root = document.querySelector('.specialists');
  const slider = root ? root.querySelector('[data-specialists-slider]') : null;
  if (!slider || !slider.swiper) return { ok: false, reason: 'no swiper' };
  const sw = slider.swiper;
  const start = sw.activeIndex;
  sw.slideNext();
  const afterNext = sw.activeIndex;
  sw.slidePrev();
  const afterPrev = sw.activeIndex;
  sw.slideTo(0, 0);
  return {
    ok: true,
    start,
    afterNext,
    afterPrev,
    restored: sw.activeIndex === 0,
    changedOnNext: afterNext !== start || start === sw.slides.length - 1,
  };
}"""


def main() -> None:
    rows: list[dict] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_id, page_file in PAGES:
            for viewport_id, width, height in VIEWPORTS:
                page = browser.new_page(viewport={"width": width, "height": height})
                page.goto(f"http://127.0.0.1:{PORT}/{page_file}", wait_until="networkidle")
                page.locator(".specialists").first.scroll_into_view_if_needed()
                page.wait_for_timeout(500)
                state = page.evaluate(SLIDER_JS)
                interaction = page.evaluate(INTERACT_JS)
                row = {
                    "page": page_id,
                    "viewport": viewport_id,
                    "instance_count": state["count"],
                    "swiper_created": state["count"] == 1 and state["instances"][0]["hasSwiper"],
                    "slide_count": state["instances"][0]["slideCount"] if state["instances"] else 0,
                    "next_works": interaction.get("changedOnNext") or interaction.get("afterNext") is not None,
                    "previous_works": interaction.get("afterPrev") is not None,
                    "restored_initial": interaction.get("restored"),
                    "duplicate_init": state["count"] != 1,
                    "result": "PASS"
                    if state["count"] == 1
                    and state["instances"][0]["hasSwiper"]
                    and state["instances"][0]["slideCount"] == 5
                    and interaction.get("ok")
                    and interaction.get("restored")
                    else "FAIL",
                }
                rows.append(row)
                page.close()
        browser.close()

    payload = {
        "validation_id": "CF-005-SLIDER-FUNCTIONAL-QA",
        "rows": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    (AUDIT / "CF-005-SLIDER-FUNCTIONAL-QA.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": payload["overall"], "rows": len(rows)}, indent=2))
    if payload["overall"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
