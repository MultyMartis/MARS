#!/usr/bin/env python3
"""FP-0002 V8 CF-003 completion browser QA (three service templates)."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
STORAGE = Path(r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\cf-003-evidence\completion")
AUDIT = ROOT / "audits" / "cf-003-upper-navigation" / "data"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4188

PAGES = [
    ("services-hub", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]


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

    cf003 = page.evaluate(
        """() => {
          const nav = document.querySelector('.internal-page-nav');
          const hero = document.querySelector('.services-inner-hero-v2, .service-subdivision-hero-v1, .service-leaf-hero-v1');
          const next = nav ? nav.nextElementSibling : null;
          const container = nav ? nav.querySelector('.container') : null;
          const breadcrumbs = nav ? nav.querySelector('.breadcrumbs') : null;
          const subnav = nav ? nav.querySelector('.services-page-subnav') : null;
          const bcList = breadcrumbs ? breadcrumbs.querySelector('.breadcrumbs__list') : null;
          const snList = subnav ? subnav.querySelector('.services-page-subnav__list') : null;

          const rect = (el) => el ? el.getBoundingClientRect() : null;
          const navRect = rect(nav);
          const heroRect = rect(hero);
          const nextRect = rect(next);
          const containerRect = rect(container);
          const bcRect = rect(breadcrumbs);
          const snRect = rect(subnav);

          const gapHeroNav = (navRect && heroRect) ? Math.round(navRect.top - heroRect.bottom) : null;
          const gapBcSn = (bcRect && snRect) ? Math.round(snRect.top - bcRect.bottom) : null;
          const gapNavNext = (navRect && nextRect) ? Math.round(nextRect.top - navRect.bottom) : null;
          const containerGap = container ? getComputedStyle(container).gap : null;

          const bcLink = breadcrumbs ? breadcrumbs.querySelector('.breadcrumbs__link') : null;
          const snLink = subnav ? subnav.querySelector('.services-page-subnav__link') : null;
          const bcStyle = bcLink ? getComputedStyle(bcLink) : null;
          const snStyle = snLink ? getComputedStyle(snLink) : null;

          return {
            internalPageNavCount: document.querySelectorAll('.internal-page-nav').length,
            breadcrumbsCount: document.querySelectorAll('.internal-page-nav .breadcrumbs').length,
            subnavCount: document.querySelectorAll('.internal-page-nav .services-page-subnav').length,
            breadcrumbsAria: breadcrumbs ? breadcrumbs.getAttribute('aria-label') : null,
            subnavAria: subnav ? subnav.getAttribute('aria-label') : null,
            currentCrumb: breadcrumbs ? !!breadcrumbs.querySelector('[aria-current="page"]') : false,
            subnavLinkCount: subnav ? subnav.querySelectorAll('.services-page-subnav__link').length : 0,
            scrollWidth: document.documentElement.scrollWidth,
            clientWidth: document.documentElement.clientWidth,
            overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
            gapHeroNav,
            gapBcSn,
            gapNavNext,
            containerGap,
            containerPaddingTop: container ? getComputedStyle(container).paddingTop : null,
            containerPaddingBottom: container ? getComputedStyle(container).paddingBottom : null,
            breadcrumbFontSize: bcStyle ? bcStyle.fontSize : null,
            breadcrumbLineHeight: bcStyle ? bcStyle.lineHeight : null,
            subnavLinkMinHeight: snStyle ? snStyle.minHeight : null,
            subnavLinkFontSize: snStyle ? snStyle.fontSize : null,
            subnavOverflowX: subnav ? getComputedStyle(subnav).overflowX : null,
            heroClass: hero ? hero.className : null,
            nextClass: next ? next.className : null,
          };
        }"""
    )

    metrics = page.evaluate(
        """() => ({
          title: document.title,
          h1: (document.querySelector('h1') || {}).textContent || '',
          documentHeight: Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
        })"""
    )

    return {
        "http_status": response.status if response else None,
        "metrics": metrics,
        "cf003": cf003,
        "console_errors": console_errors,
        "page_errors": page_errors,
        "failed_requests": failed_requests,
    }


def classify(entry: dict) -> str:
    if entry.get("http_status") != 200:
        return "FAIL"
    if entry.get("console_errors") or entry.get("page_errors") or entry.get("failed_requests"):
        return "FAIL"
    c = entry["cf003"]
    if c["internalPageNavCount"] != 1 or c["breadcrumbsCount"] != 1 or c["subnavCount"] != 1:
        return "FAIL"
    if not c["currentCrumb"] or c["subnavLinkCount"] < 1:
        return "FAIL"
    if c["overflow"]:
        return "FAIL"
    return "PASS"


def main() -> None:
    STORAGE.mkdir(parents=True, exist_ok=True)
    AUDIT.mkdir(parents=True, exist_ok=True)
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
                full_path = STORAGE / f"{base}-fullpage.png"
                hero_path = STORAGE / f"{base}-hero-cf003-next.png"
                crop_path = STORAGE / f"{base}-cf003-crop.png"
                metrics_path = AUDIT / f"cf-003-browser-metrics-{base}.json"

                page = browser.new_page(viewport={"width": width, "height": height})
                data = capture_page(page, url)

                page.screenshot(path=str(full_path), full_page=True)

                hero_sel = ".services-inner-hero-v2, .service-subdivision-hero-v1, .service-leaf-hero-v1"
                hero = page.locator(hero_sel).first
                cf003 = page.locator(".internal-page-nav").first
                next_block = page.locator(".internal-page-nav + *").first
                if hero.count() and cf003.count() and next_block.count():
                    hb = hero.bounding_box()
                    cb = cf003.bounding_box()
                    nb = next_block.bounding_box()
                    if hb and cb and nb:
                        clip_y = max(0, hb["y"] - 8)
                        clip_h = (nb["y"] + min(nb["height"], 120)) - clip_y
                        page.screenshot(
                            path=str(hero_path),
                            clip={
                                "x": 0,
                                "y": clip_y,
                                "width": width,
                                "height": max(clip_h, 200),
                            },
                        )

                if cf003.count():
                    box = cf003.bounding_box()
                    if box:
                        page.screenshot(
                            path=str(crop_path),
                            clip={
                                "x": 0,
                                "y": max(0, box["y"] - 4),
                                "width": width,
                                "height": min(box["height"] + 8, 220),
                            },
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
                entry["result"] = classify(entry)
                results.append(entry)

                c = entry["cf003"]
                matrix.append(
                    {
                        "page": page_id,
                        "viewport": viewport_id,
                        "wrapper": c["internalPageNavCount"],
                        "gap": c["containerGap"],
                        "padding": f"{c['containerPaddingTop']}/{c['containerPaddingBottom']}",
                        "breadcrumbs": f"{c['breadcrumbFontSize']}/{c['breadcrumbLineHeight']}",
                        "subnav": f"{c['subnavLinkMinHeight']}/{c['subnavLinkFontSize']}",
                        "overflow": c["overflow"],
                        "result": entry["result"],
                    }
                )

                metrics_payload = {
                    "page_id": page_id,
                    "viewport": viewport_id,
                    "captured_at": captured_at,
                    "result": entry["result"],
                    "cf003": c,
                    "console_errors": entry["console_errors"],
                    "failed_requests": entry["failed_requests"],
                }
                metrics_path.write_text(
                    json.dumps(metrics_payload, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )

                for kind, path in (
                    ("fullpage", full_path),
                    ("hero_cf003_next", hero_path),
                    ("cf003_crop", crop_path),
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
    manifest = {
        "manifest_id": "FP-0002-V8-CF-003-COMPLETION-BROWSER-QA",
        "manifest_line": "CF-003 completion browser QA evidence (screenshots external to Git)",
        "captured_at": captured_at,
        "port": PORT,
        "overall": overall,
        "screenshots_storage": str(STORAGE),
        "metrics_in_repo": [str(AUDIT / f"cf-003-browser-metrics-{p}-{v}.json") for p, _ in PAGES for v, _, _ in VIEWPORTS],
        "screenshots": screenshots,
        "matrix": matrix,
        "entries": results,
    }
    (AUDIT / "CF-003-COMPLETION-BROWSER-QA.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        "# CF-003 Completion Browser QA",
        "",
        f"Captured: {captured_at}",
        f"Overall: **{overall}**",
        "",
        "| Page | Viewport | HTTP | Console | Assets | Overflow | Geometry | Result |",
        "|---|---:|---:|---:|---:|---|---|---|",
    ]
    for r in results:
        c = r["cf003"]
        md.append(
            f"| {r['page_id']} | {r['viewport']} | {r['http_status']} | "
            f"{len(r['console_errors'])} | {len(r['failed_requests'])} | "
            f"{'yes' if c['overflow'] else 'no'} | "
            f"gap hero/nav {c['gapHeroNav']} / bc-sn {c['gapBcSn']} / nav-next {c['gapNavNext']} | {r['result']} |"
        )
    (ROOT / "audits" / "cf-003-upper-navigation" / "CF-003-COMPLETION-BROWSER-QA.md").write_text(
        "\n".join(md) + "\n", encoding="utf-8"
    )

    print(json.dumps({"overall": overall, "entries": len(results), "matrix": matrix}, indent=2))
    if overall != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
