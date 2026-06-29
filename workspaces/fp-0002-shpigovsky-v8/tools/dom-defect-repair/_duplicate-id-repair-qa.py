#!/usr/bin/env python3
"""FP-0002 V8 duplicate-ID repair validation and evidence capture."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
AUDIT = ROOT / "audits" / "dom-defect-repair" / "data"
STORAGE = Path(
    r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\duplicate-id-repair-evidence"
)
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4197
PHASE = sys.argv[2] if len(sys.argv) > 2 else "after"
TARGET_ID = "home-treatment-prevention-panel-1"


def duplicate_id_report(html: str) -> dict:
    ids = re.findall(r'\bid="([^"]+)"', html)
    counts = Counter(ids)
    dups = {k: v for k, v in counts.items() if v > 1}
    return {
        "total_ids": len(ids),
        "unique_ids": len(counts),
        "duplicate_id_count": sum(v - 1 for v in dups.values()),
        "duplicate_ids": dups,
        f"{TARGET_ID}_count": counts.get(TARGET_ID, 0),
    }


def broken_aria_report(html: str) -> dict:
    broken_controls = []
    broken_labelledby = []
    for m in re.finditer(
        r'<([a-zA-Z0-9-]+)[^>]*\bid="([^"]+)"[^>]*aria-controls="([^"]+)"',
        html,
    ):
        if f'id="{m.group(3)}"' not in html:
            broken_controls.append(m.group(3))
    for m in re.finditer(
        r'<([a-zA-Z0-9-]+)[^>]*\bid="([^"]+)"[^>]*aria-labelledby="([^"]+)"',
        html,
    ):
        if f'id="{m.group(3)}"' not in html:
            broken_labelledby.append(m.group(3))
    return {
        "broken_aria_controls": len(broken_controls),
        "broken_aria_labelledby": len(broken_labelledby),
        "broken_controls_ids": broken_controls,
        "broken_labelledby_ids": broken_labelledby,
    }


def capture_evidence(page, out_dir: Path, label: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle", timeout=120000)
    section = page.locator(".home-treatment-prevention").first
    section.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    box = section.bounding_box()
    if box:
        page.screenshot(path=str(out_dir / f"{label}-treatment-prevention-initial.png"), clip=box)
    btn1 = page.locator("#home-treatment-prevention-trigger-1")
    btn1.click()
    page.wait_for_timeout(300)
    box = section.bounding_box()
    if box:
        page.screenshot(path=str(out_dir / f"{label}-treatment-prevention-open.png"), clip=box)


def accordion_functional(page) -> dict:
    page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle", timeout=120000)
    btn1 = page.locator("#home-treatment-prevention-trigger-1")
    panel1 = page.locator("#home-treatment-prevention-panel-1").first
    default_expanded = btn1.get_attribute("aria-expanded") == "true"
    default_hidden = panel1.evaluate("el => el.hidden")
    btn1.click()
    page.wait_for_timeout(200)
    click_toggles = btn1.get_attribute("aria-expanded") == "false"
    btn1.focus()
    page.keyboard.press("Enter")
    page.wait_for_timeout(200)
    enter_works = btn1.get_attribute("aria-expanded") == "true"
    page.keyboard.press(" ")
    page.wait_for_timeout(200)
    space_works = btn1.get_attribute("aria-expanded") == "false"
    return {
        "trigger_exists": btn1.count() == 1,
        "panel_exists": page.locator(f"#{TARGET_ID}").count() == 1,
        "default_expanded": default_expanded,
        "default_hidden": default_hidden,
        "click_works": click_toggles,
        "enter_works": enter_works,
        "space_works": space_works,
    }


def main() -> None:
    html = (DIST / "index.html").read_text(encoding="utf-8")
    dom = duplicate_id_report(html)
    aria = broken_aria_report(html)

    evidence_dir = STORAGE / PHASE
    functional: dict = {}
    console_errors: list[str] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for vp_id, w, h in [("desktop", 1437, 1000), ("mobile", 380, 900)]:
            page = browser.new_page(viewport={"width": w, "height": h})
            page.on(
                "console",
                lambda msg: console_errors.append(msg.text) if msg.type == "error" else None,
            )
            capture_evidence(page, evidence_dir / vp_id, vp_id)
            if vp_id == "desktop":
                functional = accordion_functional(page)
            page.close()
        browser.close()

    payload = {
        "validation_id": "FP-0002-V8-DUPLICATE-ID-REPAIR-VALIDATION",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "phase": PHASE,
        "port": PORT,
        "target_duplicate_id": TARGET_ID,
        "dom": dom,
        "aria": aria,
        "functional": functional,
        "console_errors": console_errors,
    }
    if PHASE == "after":
        payload["result"] = (
            "PASS"
            if dom[f"{TARGET_ID}_count"] == 1
            and dom["duplicate_id_count"] == 0
            and aria["broken_aria_controls"] == 0
            and aria["broken_aria_labelledby"] == 0
            and functional.get("panel_exists")
            and functional.get("click_works")
            else "FAIL"
        )
    else:
        payload["result"] = "BASELINE"
    AUDIT.mkdir(parents=True, exist_ok=True)
    (AUDIT / "FP-0002-V8-DUPLICATE-ID-REPAIR-VALIDATION.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"result": payload["result"], "dom": dom, "functional": functional}, indent=2))
    if PHASE == "after" and payload["result"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
