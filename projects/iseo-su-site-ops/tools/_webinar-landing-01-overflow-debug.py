#!/usr/bin/env python3
"""Debug horizontal overflow + mobile image + $ error for webinar landing."""
from __future__ import annotations

import json
from playwright.sync_api import sync_playwright

URL = "https://i-seo.su/webinar-seo-podryadchik.html"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        stacks = []
        page.on(
            "pageerror",
            lambda e: stacks.append({"msg": str(e), "stack": getattr(e, "stack", None)}),
        )
        page.goto(URL, wait_until="networkidle", timeout=90000)
        page.wait_for_timeout(900)
        info = page.evaluate(
            """() => {
              const cw = document.documentElement.clientWidth;
              const out = [];
              document.querySelectorAll('*').forEach((el) => {
                const sw = el.scrollWidth;
                if (sw > cw + 2) {
                  const st = getComputedStyle(el);
                  out.push({
                    tag: el.tagName,
                    id: el.id || '',
                    cls: (el.className || '').toString().slice(0, 120),
                    scrollW: sw,
                    offsetW: el.offsetWidth,
                    clientW: el.clientWidth,
                    transform: st.transform,
                    overflowX: st.overflowX,
                    position: st.position,
                    left: st.left,
                    marginLeft: st.marginLeft,
                    width: st.width,
                  });
                }
              });
              out.sort((a, b) => b.scrollW - a.scrollW);
              const ps = document.querySelector('.page_scene');
              let before = null;
              let after = null;
              if (ps) {
                const b = getComputedStyle(ps, '::before');
                const a = getComputedStyle(ps, '::after');
                before = { content: b.content, w: b.width, h: b.height, transform: b.transform, pos: b.position, right: b.right, top: b.top };
                after = { content: a.content, w: a.width, h: a.height, transform: a.transform, pos: a.position };
              }
              return {
                docSW: document.documentElement.scrollWidth,
                bodySW: document.body.scrollWidth,
                cw,
                top: out.slice(0, 25),
                before,
                after,
                page_scene_overflow: ps ? getComputedStyle(ps).overflow : null,
                page_scene_position: ps ? getComputedStyle(ps).position : null,
              };
            }"""
        )
        print("DESKTOP", json.dumps({"info": info, "stacks": stacks}, ensure_ascii=False, indent=2))
        ctx.close()

        ctx3 = browser.new_context(viewport={"width": 390, "height": 844})
        page3 = ctx3.new_page()
        page3.goto(URL, wait_until="networkidle", timeout=90000)
        page3.wait_for_timeout(800)
        img = page3.evaluate(
            """() => {
              const img = document.querySelector('img[src*="iSEO_Boss"]');
              if (!img) return { missing: true };
              const r = img.getBoundingClientRect();
              const st = getComputedStyle(img);
              const p = img.parentElement;
              const pr = p ? p.getBoundingClientRect() : null;
              const info = document.querySelector('.page_scene__info');
              const ir = info ? info.getBoundingClientRect() : null;
              const ist = info ? getComputedStyle(info) : null;
              return {
                r: { t: r.top, l: r.left, b: r.bottom, ri: r.right, w: r.width, h: r.height },
                display: st.display,
                vis: st.visibility,
                opacity: st.opacity,
                maxH: st.maxHeight,
                parent: pr
                  ? { t: pr.top, l: pr.left, w: pr.width, h: pr.height, cls: p.className }
                  : null,
                infoBox: ir
                  ? {
                      t: ir.top,
                      l: ir.left,
                      w: ir.width,
                      h: ir.height,
                      order: ist.order,
                      display: ist.display,
                      overflow: ist.overflow,
                    }
                  : null,
                naturalW: img.naturalWidth,
                complete: img.complete,
                scrollW: document.documentElement.scrollWidth,
                clientW: document.documentElement.clientWidth,
              };
            }"""
        )
        print("MOBILE", json.dumps(img, ensure_ascii=False, indent=2))
        ctx3.close()
        browser.close()


if __name__ == "__main__":
    main()
