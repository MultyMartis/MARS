"""FP-0002 PASS 2.1 horizontal overflow diagnostic matrix."""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"

WIDTHS = [320, 380, 390, 430, 660, 768, 1024, 1025, 1280, 1437]

PAGES = [
    ("home", "index.html", "HOME_PAGE_TEMPLATE", False),
    ("services-hub-canonical", "uslugi-v2.html", "SERVICES_HUB_INTERNAL_PAGE", True),
    ("subdivision-canonical", "usluga-podrazdel-v1.html", "SERVICE_SUBDIVISION_INTERNAL_PAGE", True),
    ("leaf-canonical", "usluga-konechnaya-v1.html", "SERVICE_LEAF_INTERNAL_PAGE", True),
    ("services-hub-generated", "uslugi/index.html", "SERVICES_HUB_INTERNAL_PAGE", False),
    ("subdivision-genotipirovanie", "uslugi/genotipirovanie/index.html", "SERVICE_SUBDIVISION_INTERNAL_PAGE", False),
    ("subdivision-zavisimosti", "uslugi/zavisimosti/index.html", "SERVICE_SUBDIVISION_INTERNAL_PAGE", False),
    ("leaf-alkogol", "uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html", "SERVICE_LEAF_INTERNAL_PAGE", False),
    ("leaf-depressiya", "uslugi/psihicheskoe-zdorovie/depressiya/index.html", "SERVICE_LEAF_INTERNAL_PAGE", False),
    ("leaf-ptsr", "uslugi/psihicheskoe-zdorovie/ptsr/index.html", "SERVICE_LEAF_INTERNAL_PAGE", False),
    ("placeholder-reserved", "uslugi/psihicheskoe-zdorovie/nazvanie-slot-01/index.html", "PLACEHOLDER_PAGE", False),
]

MEASURE_JS = """
() => {
  const doc = document.documentElement;
  const body = document.body;
  const viewport = window.innerWidth;
  const canScrollX = doc.scrollWidth > doc.clientWidth && (
    window.scrollX > 0 ||
    (() => {
    const before = window.scrollX;
    window.scrollBy(1, 0);
    const moved = window.scrollX !== before;
    window.scrollTo(before, window.scrollY);
    return moved;
  })()
  );
  return {
    docScrollWidth: doc.scrollWidth,
    docClientWidth: doc.clientWidth,
    bodyScrollWidth: body ? body.scrollWidth : null,
    innerWidth: viewport,
    delta: doc.scrollWidth - doc.clientWidth,
    overflow: doc.scrollWidth > doc.clientWidth,
    canScrollX,
  };
}
"""

OFFENDER_JS = """
() => {
  const viewport = window.innerWidth;
  const offenders = [];
  const all = document.querySelectorAll('body *');
  for (const el of all) {
    const style = window.getComputedStyle(el);
    if (style.display === 'none' || style.visibility === 'hidden') continue;
    const rect = el.getBoundingClientRect();
    if (!rect.width && !rect.height) continue;
    const right = rect.right;
    const left = rect.left;
    const width = rect.width;
    const overRight = right > viewport + 1;
    const overLeft = left < -1;
    const overWidth = width > viewport + 1;
    if (!overRight && !overLeft && !overWidth) continue;

    let selector = el.tagName.toLowerCase();
    if (el.id) selector += '#' + el.id;
    else if (el.className && typeof el.className === 'string') {
      const cls = el.className.trim().split(/\\s+/).slice(0, 3).join('.');
      if (cls) selector += '.' + cls;
    }

    const ariaHidden = el.getAttribute('aria-hidden');
    const hiddenAttr = el.hasAttribute('hidden');
    const parent = el.parentElement;
    let parentOverflow = parent ? window.getComputedStyle(parent).overflowX : null;

    offenders.push({
      selector,
      left: Math.round(left * 100) / 100,
      right: Math.round(right * 100) / 100,
      width: Math.round(width * 100) / 100,
      position: style.position,
      overflowX: style.overflowX,
      transform: style.transform !== 'none' ? style.transform : null,
      visibility: style.visibility,
      display: style.display,
      ariaHidden,
      hidden: hiddenAttr,
      parentOverflow,
      tag: el.tagName.toLowerCase(),
      className: typeof el.className === 'string' ? el.className : '',
    });
  }
  offenders.sort((a, b) => (b.right - b.left) - (a.right - a.left));
  return offenders.slice(0, 40);
}
"""

CLASSIFY_JS = """
(offenders, overflow, canScrollX) => {
  const classifyOne = (o) => {
    const cls = (o.className || '').toLowerCase();
    const sel = (o.selector || '').toLowerCase();
    if (cls.includes('swiper') || cls.includes('slick') || sel.includes('swiper')) {
      return 'EXPECTED_SLIDER_TRACK';
    }
    if (cls.includes('fancybox') || sel.includes('fancybox')) {
      return 'EXPECTED_FANCYBOX_LAYER';
    }
    if (cls.includes('modal') || cls.includes('off-canvas') || cls.includes('mobile-menu') || cls.includes('site-nav')) {
      return 'EXPECTED_MODAL_LAYER';
    }
    if (o.position === 'fixed' && (o.left < -1 || o.right > window.innerWidth + 1)) {
      return 'EXPECTED_OFFCANVAS';
    }
    if (o.ariaHidden === 'true' || o.hidden) {
      return 'EXPECTED_MODAL_LAYER';
    }
    return 'REAL_LAYOUT_OVERFLOW';
  };
  return {
    overflow,
    canScrollX,
    top: offenders.slice(0, 8).map(o => ({...o, classification: classifyOne(o)})),
  };
}
"""


def page_url(rel: str) -> str:
    if rel == "index.html":
        return "http://127.0.0.1:4176/"
    if rel.endswith("index.html"):
        return f"http://127.0.0.1:4176/{rel.replace('index.html', '')}"
    return f"http://127.0.0.1:4176/{rel}"


def run_diagnostic(phase: str) -> dict:
    out_dir = ROOT / "plans/static-client-demo/evidence/pass-2-1-overflow"
    out_dir.mkdir(parents=True, exist_ok=True)

    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", "4176", "--directory", str(DIST)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.5)

    matrix = []
    offenders_all = []

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for slug, rel, template, is_canonical in PAGES:
                url = page_url(rel)
                for width in WIDTHS:
                    page = browser.new_page(viewport={"width": width, "height": 2000})
                    page.goto(url, wait_until="networkidle")
                    page.wait_for_timeout(600)
                    # wait fonts
                    page.evaluate("document.fonts.ready")
                    page.wait_for_timeout(200)

                    measure = page.evaluate(MEASURE_JS)
                    offenders = page.evaluate(OFFENDER_JS)
                    classified = page.evaluate(
                        """([offenders, overflow, canScrollX]) => {
                          const classifyOne = (o) => {
                            const cls = (o.className || '').toLowerCase();
                            const sel = (o.selector || '').toLowerCase();
                            if (cls.includes('swiper') || cls.includes('slick') || sel.includes('swiper')) return 'EXPECTED_SLIDER_TRACK';
                            if (cls.includes('fancybox') || sel.includes('fancybox')) return 'EXPECTED_FANCYBOX_LAYER';
                            if (cls.includes('modal') || cls.includes('off-canvas') || cls.includes('mobile-menu')) return 'EXPECTED_MODAL_LAYER';
                            if (o.position === 'fixed' && (o.left < -1 || o.right > window.innerWidth + 1)) return 'EXPECTED_OFFCANVAS';
                            if (o.ariaHidden === 'true' || o.hidden) return 'EXPECTED_MODAL_LAYER';
                            return 'REAL_LAYOUT_OVERFLOW';
                          };
                          const real = offenders.filter(o => classifyOne(o) === 'REAL_LAYOUT_OVERFLOW');
                          let classification = 'OK';
                          if (overflow) {
                            if (real.length) classification = 'REAL_LAYOUT_OVERFLOW';
                            else if (offenders.some(o => classifyOne(o) === 'EXPECTED_SLIDER_TRACK')) classification = 'EXPECTED_SLIDER_TRACK';
                            else if (offenders.some(o => classifyOne(o) === 'EXPECTED_OFFCANVAS')) classification = 'EXPECTED_OFFCANVAS';
                            else if (offenders.some(o => classifyOne(o) === 'EXPECTED_MODAL_LAYER')) classification = 'EXPECTED_MODAL_LAYER';
                            else if (!canScrollX) classification = 'VALIDATOR_FALSE_POSITIVE';
                            else classification = 'UNKNOWN';
                          }
                          return { classification, realCount: real.length, topReal: real.slice(0, 5) };
                        }""",
                        [offenders, measure["overflow"], measure["canScrollX"]],
                    )

                    row = {
                        "page": slug,
                        "template": template,
                        "canonical_source": is_canonical,
                        "url": url,
                        "width": width,
                        **measure,
                        "classification": classified["classification"],
                        "top_offenders": classified["topReal"] or offenders[:3],
                    }
                    matrix.append(row)

                    if measure["overflow"] and classified["classification"] in (
                        "REAL_LAYOUT_OVERFLOW",
                        "UNKNOWN",
                    ):
                        offenders_all.append(
                            {
                                "page": slug,
                                "width": width,
                                "classification": classified["classification"],
                                "offenders": offenders[:15],
                            }
                        )
                        # screenshot for reproducible real overflow
                        shot_dir = out_dir / "screenshots" / phase / slug
                        shot_dir.mkdir(parents=True, exist_ok=True)
                        page.screenshot(path=str(shot_dir / f"{width}-full.png"), full_page=False)
                        page.evaluate(
                            """(offenders) => {
                              document.querySelectorAll('[data-overflow-highlight]').forEach(n => {
                                n.style.outline = '';
                                n.removeAttribute('data-overflow-highlight');
                              });
                              const top = offenders[0];
                              if (!top) return;
                              const nodes = document.querySelectorAll('*');
                              for (const el of nodes) {
                                const r = el.getBoundingClientRect();
                                if (Math.abs(r.right - top.right) < 2 && Math.abs(r.width - top.width) < 2) {
                                  el.style.outline = '3px solid red';
                                  el.setAttribute('data-overflow-highlight', '1');
                                  break;
                                }
                              }
                            }""",
                            offenders[:1],
                        )
                        page.screenshot(path=str(shot_dir / f"{width}-highlight.png"), full_page=False)

                    page.close()
            browser.close()
    finally:
        server.terminate()

    matrix_path = out_dir / f"PASS-2-1-OVERFLOW-MATRIX-{phase.upper()}.json"
    offenders_path = out_dir / f"PASS-2-1-OVERFLOW-OFFENDERS-{phase.upper()}.json"
    matrix_path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
    offenders_path.write_text(json.dumps(offenders_all, ensure_ascii=False, indent=2), encoding="utf-8")

    real_cases = [r for r in matrix if r["overflow"] and r["classification"] == "REAL_LAYOUT_OVERFLOW"]
    false_pos = [r for r in matrix if r["overflow"] and r["classification"] == "VALIDATOR_FALSE_POSITIVE"]
    expected = [r for r in matrix if r["overflow"] and r["classification"].startswith("EXPECTED_")]

    md = f"""# PASS 2.1 Overflow Diagnostic — {phase.upper()}

## Summary
- Total probes: {len(matrix)}
- Overflow detected: {sum(1 for r in matrix if r['overflow'])}
- REAL_LAYOUT_OVERFLOW: {len(real_cases)}
- VALIDATOR_FALSE_POSITIVE: {len(false_pos)}
- EXPECTED (slider/offcanvas/modal): {len(expected)}

## Reproducible real overflow pages/widths
"""
    for r in real_cases[:30]:
        md += f"- {r['page']} @ {r['width']}: delta={r['delta']}, canScrollX={r['canScrollX']}\n"

    (out_dir / f"PASS-2-1-OVERFLOW-DIAGNOSTIC-{phase.upper()}.md").write_text(md, encoding="utf-8")

    return {
        "matrix_path": str(matrix_path),
        "offenders_path": str(offenders_path),
        "real_count": len(real_cases),
        "false_positive_count": len(false_pos),
        "overflow_count": sum(1 for r in matrix if r["overflow"]),
    }


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "before"
    result = run_diagnostic(phase)
    print(json.dumps(result, indent=2))
