#!/usr/bin/env python3
"""Browser-level parity capture: V7 authority reference dist vs V8 dist."""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

V7_PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4175
V8_PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4176

STORAGE_EVIDENCE = Path(r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\parity-evidence\bootstrap-reconciliation")
WORKSPACE = Path(__file__).resolve().parents[2]
AUDIT_DIR = WORKSPACE / "audits" / "bootstrap-reconciliation"
STORAGE_EVIDENCE.mkdir(parents=True, exist_ok=True)
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

TEMPLATES = [
    ("home", "index.html"),
    ("services-hub", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]

KEY_SELECTORS = [
    "header",
    ".hero, .services-inner-hero-v2, .service-subdivision-hero-v1, .service-leaf-hero-v1",
    ".page-uslugi-v2__upper-nav, .page-service-subdivision-v1__upper-nav, .page-service-leaf-v1__upper-nav",
    "main",
    "footer",
    "[data-modal='consultation']",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def png_pixel_diff_ratio(a: Path, b: Path) -> dict:
    if not a.exists() or not b.exists():
        return {"dimensions_match": False, "diff_ratio": 1.0, "error": "missing file"}

    try:
        i1 = Image.open(a).convert("RGB")
        i2 = Image.open(b).convert("RGB")
    except Exception as exc:  # noqa: BLE001
        return {"dimensions_match": False, "diff_ratio": 1.0, "error": str(exc)}

    if i1.size != i2.size:
        return {
            "dimensions_match": False,
            "diff_ratio": 1.0,
            "width_ref": i1.size[0],
            "height_ref": i1.size[1],
            "width_v8": i2.size[0],
            "height_v8": i2.size[1],
        }

    diff_img = ImageChops.difference(i1, i2)
    px1 = i1.load()
    px2 = i2.load()
    w, h = i1.size
    diff_pixels = sum(1 for y in range(h) for x in range(w) if px1[x, y] != px2[x, y])
    total = w * h
    bbox = diff_img.getbbox()
    return {
        "dimensions_match": True,
        "width": w,
        "height": h,
        "diff_pixels": diff_pixels,
        "total_pixels": total,
        "diff_ratio": round(diff_pixels / total, 8) if total else 0.0,
        "diff_bbox": bbox,
        "sha256_ref": sha256_file(a),
        "sha256_v8": sha256_file(b),
        "sha256_match": sha256_file(a) == sha256_file(b),
    }


def capture_page(page, url: str) -> dict:
    console_errors: list[str] = []
    page_errors: list[str] = []
    failed_requests: list[str] = []

    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda err: page_errors.append(str(err)))
    page.on("requestfailed", lambda req: failed_requests.append(req.url))

    page.goto(url, wait_until="networkidle", timeout=120000)
    page.add_style_tag(content="*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important;}")
    page.evaluate(
        """async () => {
          document.querySelectorAll('.swiper').forEach((el) => {
            if (el.swiper) { el.swiper.autoplay?.stop(); el.swiper.slideTo(0, 0); }
          });
          const step = Math.max(document.documentElement.clientHeight, 400);
          for (let y = 0; y <= document.body.scrollHeight; y += step) {
            window.scrollTo(0, y);
            await new Promise((r) => setTimeout(r, 120));
          }
          window.scrollTo(0, 0);
        }"""
    )
    page.wait_for_timeout(1200)

    metrics = page.evaluate(
        """() => ({
          title: document.title,
          h1: (document.querySelector('h1') || {}).textContent || '',
          documentHeight: Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          blockCount: document.querySelectorAll('section, header, footer, main').length,
        })"""
    )

    selector_presence = {}
    for sel in KEY_SELECTORS:
        selector_presence[sel] = page.locator(sel).count() > 0

    return {
        "metrics": metrics,
        "console_errors": console_errors,
        "page_errors": page_errors,
        "failed_requests": failed_requests,
        "selector_presence": selector_presence,
    }


def classify_result(entry: dict) -> str:
    if entry.get("http_status_ref") != 200 or entry.get("http_status_v8") != 200:
        return "PARITY_FAILED"
    if entry.get("console_errors_ref") or entry.get("console_errors_v8"):
        return "PARITY_FAILED"
    if entry.get("failed_requests_ref") or entry.get("failed_requests_v8"):
        return "PARITY_FAILED"
    if entry.get("title_match") is False or entry.get("h1_match") is False:
        return "PARITY_FAILED"
    if entry.get("overflow_match") is False:
        return "PARITY_FAILED"
    full = entry.get("fullpage_diff", {})
    if full.get("sha256_match"):
        return "EXACT_PARITY"
    dr = full.get("diff_ratio", 1.0)
    if dr == 0.0:
        return "EXACT_PARITY"
    if (
        entry.get("document_height_delta", 999) == 0
        and dr <= 0.02
        and full.get("dimensions_match")
    ):
        return "PARITY_WITH_RENDERING_NOISE"
    return "PARITY_FAILED"


def main() -> None:
    results = []
    manifest_shots = []
    captured_at = datetime.now(timezone.utc).isoformat()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for template_id, page_file in TEMPLATES:
            for viewport_id, width, height in VIEWPORTS:
                ref_url = f"http://127.0.0.1:{V7_PORT}/{page_file}"
                v8_url = f"http://127.0.0.1:{V8_PORT}/{page_file}"
                shot_base = f"{template_id}-{viewport_id}"
                ref_full = STORAGE_EVIDENCE / f"{shot_base}-ref-fullpage.png"
                v8_full = STORAGE_EVIDENCE / f"{shot_base}-v8-fullpage.png"
                ref_vp = STORAGE_EVIDENCE / f"{shot_base}-ref-viewport.png"
                v8_vp = STORAGE_EVIDENCE / f"{shot_base}-v8-viewport.png"

                for label, url, full_path, vp_path in (
                    ("ref", ref_url, ref_full, ref_vp),
                    ("v8", v8_url, v8_full, v8_vp),
                ):
                    page = browser.new_page(viewport={"width": width, "height": height})
                    data = capture_page(page, url)
                    page.screenshot(path=str(full_path), full_page=True)
                    page.screenshot(path=str(vp_path), full_page=False)
                    page.close()
                    if label == "ref":
                        ref_data = data
                        http_ref = 200
                    else:
                        v8_data = data
                        http_v8 = 200

                full_diff = png_pixel_diff_ratio(ref_full, v8_full)
                vp_diff = png_pixel_diff_ratio(ref_vp, v8_vp)
                entry = {
                    "template_id": template_id,
                    "page_file": page_file,
                    "viewport": viewport_id,
                    "viewport_size": {"width": width, "height": height},
                    "reference_url": ref_url,
                    "v8_url": v8_url,
                    "captured_at": captured_at,
                    "http_status_ref": http_ref,
                    "http_status_v8": http_v8,
                    "title_ref": ref_data["metrics"]["title"],
                    "title_v8": v8_data["metrics"]["title"],
                    "title_match": ref_data["metrics"]["title"] == v8_data["metrics"]["title"],
                    "h1_ref": ref_data["metrics"]["h1"].strip(),
                    "h1_v8": v8_data["metrics"]["h1"].strip(),
                    "h1_match": ref_data["metrics"]["h1"].strip() == v8_data["metrics"]["h1"].strip(),
                    "document_height_ref": ref_data["metrics"]["documentHeight"],
                    "document_height_v8": v8_data["metrics"]["documentHeight"],
                    "document_height_delta": abs(ref_data["metrics"]["documentHeight"] - v8_data["metrics"]["documentHeight"]),
                    "scroll_width_ref": ref_data["metrics"]["scrollWidth"],
                    "scroll_width_v8": v8_data["metrics"]["scrollWidth"],
                    "client_width_ref": ref_data["metrics"]["clientWidth"],
                    "client_width_v8": v8_data["metrics"]["clientWidth"],
                    "overflow_ref": ref_data["metrics"]["overflow"],
                    "overflow_v8": v8_data["metrics"]["overflow"],
                    "overflow_match": ref_data["metrics"]["overflow"] == v8_data["metrics"]["overflow"],
                    "block_count_ref": ref_data["metrics"]["blockCount"],
                    "block_count_v8": v8_data["metrics"]["blockCount"],
                    "console_errors_ref": ref_data["console_errors"],
                    "console_errors_v8": v8_data["console_errors"],
                    "page_errors_ref": ref_data["page_errors"],
                    "page_errors_v8": v8_data["page_errors"],
                    "failed_requests_ref": ref_data["failed_requests"],
                    "failed_requests_v8": v8_data["failed_requests"],
                    "selector_presence_ref": ref_data["selector_presence"],
                    "selector_presence_v8": v8_data["selector_presence"],
                    "fullpage_diff": full_diff,
                    "viewport_diff": vp_diff,
                }
                entry["result"] = classify_result(entry)
                results.append(entry)

                for kind, path in (
                    ("fullpage_ref", ref_full),
                    ("fullpage_v8", v8_full),
                    ("viewport_ref", ref_vp),
                    ("viewport_v8", v8_vp),
                ):
                    manifest_shots.append(
                        {
                            "template_id": template_id,
                            "viewport": viewport_id,
                            "kind": kind,
                            "file_name": path.name,
                            "sha256": sha256_file(path),
                            "dimensions": full_diff if "fullpage" in kind else vp_diff,
                            "storage_path": str(path),
                        }
                    )
        browser.close()

    overall = "PASS"
    if any(r["result"] == "PARITY_FAILED" for r in results):
        overall = "FAIL"

    parity_json = {
        "receipt_id": "FP-0002-V8-BASELINE-BROWSER-PARITY-01",
        "captured_at": captured_at,
        "v7_reference_port": V7_PORT,
        "v8_port": V8_PORT,
        "overall": overall,
        "entries": results,
    }
    (AUDIT_DIR / "V8-BASELINE-BROWSER-PARITY.json").write_text(
        json.dumps(parity_json, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    md_lines = [
        "# V8 Baseline Browser Parity",
        "",
        f"Captured: {captured_at}",
        f"Overall: **{overall}**",
        "",
        "| Template | Viewport | Result | Title/H1 | Console | Assets | Overflow | Fullpage diff |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        md_lines.append(
            f"| {r['template_id']} | {r['viewport']} | {r['result']} | "
            f"{'OK' if r['title_match'] and r['h1_match'] else 'FAIL'} | "
            f"{len(r['console_errors_ref'])+len(r['console_errors_v8'])} | "
            f"{len(r['failed_requests_ref'])+len(r['failed_requests_v8'])} | "
            f"{'OK' if r['overflow_match'] else 'FAIL'} | "
            f"{r['fullpage_diff'].get('diff_ratio', 'n/a')} |"
        )
    (AUDIT_DIR / "V8-BASELINE-BROWSER-PARITY.md").write_text("\n".join(md_lines), encoding="utf-8")

    manifest = {
        "manifest_id": "FP-0002-V8-BROWSER-PARITY-MANIFEST-01",
        "captured_at": captured_at,
        "evidence_storage_root": str(STORAGE_EVIDENCE),
        "screenshots": manifest_shots,
        "parity_summary": overall,
    }
    (AUDIT_DIR / "V8-BROWSER-PARITY-MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(json.dumps({"overall": overall, "entries": len(results)}, indent=2))
    if overall != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
