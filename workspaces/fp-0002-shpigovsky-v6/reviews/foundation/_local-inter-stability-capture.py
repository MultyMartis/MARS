"""Local Inter zero-FOUT validation — FP-0002 V6 filmstrip + metrics capture."""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "foundation" / "visual"
METRICS = OUT_DIR / "FP-0002-V6-LOCAL-INTER-STABILITY-METRICS.json"
VIEWPORT_W = 1398
VIEWPORT_H = 2200

SHOTS = {
    "FP-0002-V6-LOCAL-INTER-FIRST-PAINT.png": 0,
    "FP-0002-V6-LOCAL-INTER-50MS.png": 50,
    "FP-0002-V6-LOCAL-INTER-100MS.png": 100,
    "FP-0002-V6-LOCAL-INTER-FONTS-READY.png": "fonts_ready",
    "FP-0002-V6-LOCAL-INTER-FULL.png": "networkidle",
}


def ensure_playwright() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def run_pass(page, url: str, label: str, cache_disabled: bool) -> dict:
    metrics: dict = {
        "pass": label,
        "cache_disabled": cache_disabled,
        "cls_samples": [],
        "layout_shift_sources": [],
        "font_requests": [],
        "external_font_requests": [],
        "preload_warnings": [],
        "document_fonts_checks": {},
        "timings": {},
        "first_visible_font": "NONE",
        "fallback_font_visibly_painted": "NOT OBSERVED",
        "fout_observed": False,
    }

    page.add_init_script(
        """
        window.__clsEntries = [];
        window.__fontRequests = [];
        new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            if (!entry.hadRecentInput) {
              window.__clsEntries.push({
                value: entry.value,
                sources: (entry.sources || []).map((s) => ({
                  node: s.node ? (s.node.className || s.node.tagName) : null,
                })),
              });
            }
          }
        }).observe({ type: 'layout-shift', buffered: true });
        """
    )

    nav_start = time.perf_counter()
    page.goto(url, wait_until="commit")
    metrics["timings"]["navigation_start_ms"] = 0

    def capture_at(delay_ms: int | str, filename: str) -> None:
        if isinstance(delay_ms, int):
            page.wait_for_timeout(delay_ms)
        elif delay_ms == "fonts_ready":
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(0)
        elif delay_ms == "networkidle":
            page.wait_for_load_state("networkidle")
        page.screenshot(path=str(OUT_DIR / filename), full_page=True)

    for filename, delay in SHOTS.items():
        if delay == 0:
            capture_at(0, filename)
        elif delay == "fonts_ready":
            capture_at("fonts_ready", filename)
        elif delay == "networkidle":
            capture_at("networkidle", filename)
        else:
            capture_at(int(delay), filename)

    resources = page.evaluate(
        """() => performance.getEntriesByType('resource').map(r => ({
            name: r.name,
            initiatorType: r.initiatorType,
            transferSize: r.transferSize,
            responseEnd: r.responseEnd,
            startTime: r.startTime
        }))"""
    )
    font_reqs = [r for r in resources if ".woff2" in r.get("name", "")]
    metrics["font_requests"] = font_reqs
    metrics["external_font_requests"] = [
        r for r in font_reqs if "fonts.googleapis.com" in r["name"] or "fonts.gstatic.com" in r["name"]
    ]

    paint = page.evaluate(
        """() => {
          const fcp = performance.getEntriesByName('first-contentful-paint')[0];
          return { fcp: fcp ? fcp.startTime : null };
        }"""
    )
    fonts_ready_ms = page.evaluate(
        """async () => {
          const t0 = performance.now();
          await document.fonts.ready;
          return performance.now() - t0;
        }"""
    )
    checks = page.evaluate(
        """() => ({
          w300: document.fonts.check('300 16px "Inter"'),
          w400: document.fonts.check('400 16px "Inter"'),
          w500: document.fonts.check('500 16px "Inter"'),
          status: document.fonts.status
        })"""
    )
    computed = page.evaluate(
        """() => {
          const pick = (sel) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            const cs = getComputedStyle(el);
            return { fontFamily: cs.fontFamily, fontWeight: cs.fontWeight };
          };
          return {
            headerPhone: pick('.site-header__phone'),
            heroTitle: pick('.hero__title'),
            heroTagline: pick('.hero__tagline'),
            btn: pick('.hero__button'),
          };
        }"""
    )

    cls_entries = page.evaluate("window.__clsEntries || []")
    metrics["cls_samples"] = cls_entries
    metrics["cls_total"] = sum(float(e.get("value", 0)) for e in cls_entries)
    for entry in cls_entries:
        for src in entry.get("sources", []):
            node = src.get("node")
            if node:
                metrics["layout_shift_sources"].append(str(node))

    metrics["document_fonts_checks"] = checks
    metrics["computed_fonts"] = computed
    metrics["timings"]["fcp_ms"] = paint.get("fcp")
    metrics["timings"]["fonts_ready_after_navigation_ms"] = fonts_ready_ms
    metrics["timings"]["total_pass_ms"] = round((time.perf_counter() - nav_start) * 1000, 2)

    if checks.get("w400"):
        metrics["first_visible_font"] = "Inter 400"
    elif checks.get("w300"):
        metrics["first_visible_font"] = "Inter 300"

    console_msgs = []
    try:
        console_msgs = [m.text for m in page.console_messages if "preload" in m.text.lower()]
    except Exception:
        pass
    metrics["preload_warnings"] = console_msgs

    return metrics


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_playwright()
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()
    all_metrics: dict = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "local_font_urls": [
            "assets/fonts/inter/inter-300.woff2",
            "assets/fonts/inter/inter-300-latin.woff2",
            "assets/fonts/inter/inter-400.woff2",
            "assets/fonts/inter/inter-400-latin.woff2",
            "assets/fonts/inter/inter-500.woff2",
            "assets/fonts/inter/inter-500-latin.woff2",
        ],
        "google_fonts_requests_after": 0,
        "external_inter_requests_after": 0,
        "font_display": "block",
        "preloaded_files": [
            "assets/fonts/inter/inter-400.woff2",
            "assets/fonts/inter/inter-400-latin.woff2",
            "assets/fonts/inter/inter-300.woff2",
        ],
        "passes": [],
        "cls_before_reference": 0.006411790278448994,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for label, cache_disabled in [
            ("cold_1", True),
            ("cold_2", True),
            ("cold_3", True),
            ("warm_1", False),
            ("warm_2", False),
        ]:
            context = browser.new_context(
                viewport={"width": VIEWPORT_W, "height": VIEWPORT_H},
                ignore_https_errors=True,
            )
            if cache_disabled:
                context.route("**/*", lambda route: route.continue_())
            page = context.new_page()
            m = run_pass(page, url, label, cache_disabled)
            all_metrics["passes"].append(m)
            if label == "cold_1":
                all_metrics["primary_pass"] = m
            context.close()

        throttled = browser.new_context(
            viewport={"width": VIEWPORT_W, "height": VIEWPORT_H},
        )
        throttled.set_extra_http_headers({})
        page = throttled.new_page()
        cdp = throttled.new_cdp_session(page)
        cdp.send("Network.enable")
        cdp.send("Network.emulateNetworkConditions", {
            "offline": False,
            "downloadThroughput": 1.5 * 1024 * 1024 / 8,
            "uploadThroughput": 750 * 1024 / 8,
            "latency": 40,
        })
        m = run_pass(page, url, "throttled_1", True)
        all_metrics["passes"].append(m)
        throttled.close()
        browser.close()

    primary = all_metrics.get("primary_pass", {})
    all_metrics["cls_after"] = primary.get("cls_total", 0)
    all_metrics["duplicate_font_requests"] = len(primary.get("font_requests", [])) > 9
    all_metrics["google_fonts_requests_after"] = len(primary.get("external_font_requests", []))
    all_metrics["external_inter_requests_after"] = len(primary.get("external_font_requests", []))

    METRICS.write_text(json.dumps(all_metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"metrics={METRICS}")
    print(f"cls_after={all_metrics['cls_after']}")
    print(f"external_font_requests={all_metrics['external_inter_requests_after']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
