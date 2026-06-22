"""Capture font-stability screenshots — FP-0002 V6 operator-canonical load pass."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "foundation" / "visual"
OUT_COLD = OUT_DIR / "FP-0002-V6-FIRST-PAINT-COLD.png"
OUT_FONTS = OUT_DIR / "FP-0002-V6-FONTS-LOADED.png"
OUT_FULL = OUT_DIR / "FP-0002-V6-FONT-STABILITY-FULL.png"
METRICS = OUT_DIR / "FP-0002-V6-FONT-STABILITY-METRICS.json"
VIEWPORT_W = 1398
VIEWPORT_H = 2200


def ensure_playwright() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_playwright()
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()
    metrics: dict = {"cls_samples": [], "layout_shift_sources": []}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page = context.new_page()

        page.add_init_script(
            """
            window.__clsEntries = [];
            new PerformanceObserver((list) => {
              for (const entry of list.getEntries()) {
                if (!entry.hadRecentInput) {
                  window.__clsEntries.push({
                    value: entry.value,
                    sources: (entry.sources || []).map((s) => ({
                      node: s.node ? (s.node.className || s.node.tagName) : null,
                      previousRect: s.previousRect,
                      currentRect: s.currentRect,
                    })),
                  });
                }
              }
            }).observe({ type: 'layout-shift', buffered: true });
            """
        )

        page.goto(url, wait_until="commit")
        page.screenshot(path=str(OUT_COLD), full_page=True)
        page.wait_for_timeout(150)
        page.wait_for_load_state("networkidle")
        page.screenshot(path=str(OUT_FONTS), full_page=True)
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT_FULL), full_page=True)

        cls_entries = page.evaluate("window.__clsEntries || []")
        metrics["cls_samples"] = cls_entries
        metrics["cls_total"] = sum(float(e.get("value", 0)) for e in cls_entries)
        for entry in cls_entries:
            for src in entry.get("sources", []):
                node = src.get("node")
                if node:
                    metrics["layout_shift_sources"].append(str(node))

        browser.close()

    METRICS.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"viewport={VIEWPORT_W}x{VIEWPORT_H}")
    print(f"cold={OUT_COLD}")
    print(f"fonts={OUT_FONTS}")
    print(f"full={OUT_FULL}")
    print(f"metrics={METRICS}")
    print(f"cls_total={metrics['cls_total']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
