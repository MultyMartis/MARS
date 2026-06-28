#!/usr/bin/env python3
"""Compare computed program styles for CF-012 consumers."""
from __future__ import annotations

import json
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "audits" / "cf-012-program-modifiers" / "data" / "CF-012-COMPUTED-STYLES.json"

PAGES = [
    ("hub", "uslugi-v2.html", "#services-program"),
    ("subdivision", "usluga-podrazdel-v1.html", "#service-subdivision-program"),
    ("leaf", "usluga-konechnaya-v1.html", "#service-leaf-program"),
]

JS = """(args) => {
  const { selector, width } = args;
  const section = document.querySelector(selector);
  if (!section) return { error: 'missing' };
  const pick = (sel) => {
    const el = section.querySelector(sel);
    if (!el) return null;
    const cs = getComputedStyle(el);
    return {
      display: cs.display,
      padding: cs.padding,
      margin: cs.margin,
      gap: cs.gap,
      height: cs.height,
      objectFit: cs.objectFit,
      gridTemplateColumns: cs.gridTemplateColumns,
      borderRadius: cs.borderRadius,
    };
  };
  return {
    modifiers: section.className,
    media: pick('.services-program-v2__item-media'),
    image: pick('.services-program-v2__item-image'),
    title: pick('.services-program-v2__item-title'),
    body: pick('.services-program-v2__item-body'),
    grid: pick('.services-program-v2__grid'),
    intro2: pick('.services-program-v2__intro--continued'),
  };
}"""


def main() -> None:
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for vp, w, h in [("desktop", 1437, 1000), ("mobile", 380, 900)]:
            ctx = browser.new_context(viewport={"width": w, "height": h})
            page = ctx.new_page()
            for cid, file, sel in PAGES:
                page.goto(f"http://127.0.0.1:4199/{file}", wait_until="networkidle")
                data = page.evaluate(JS, {"selector": sel, "width": w})
                rows.append({"consumer": cid, "viewport": vp, **data})
            ctx.close()
        browser.close()
    OUT.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
