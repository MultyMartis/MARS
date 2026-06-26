"""FP-0002 URGENT v2 focused browser smoke."""
from __future__ import annotations

import json
import subprocess
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
EVIDENCE = ROOT / "plans/static-client-demo/evidence/urgent-v2"
PORT = 4190

CHECKS = [
    {"name": "home", "path": "/", "desktop": True, "mobile": True},
    {"name": "zavisimosti", "path": "/zavisimosti/", "desktop": True, "mobile": True},
    {"name": "depressiya", "path": "/uslugi/psihicheskoe-zdorovie/depressiya/", "desktop": True, "mobile": False},
    {"name": "kompulsivnoe", "path": "/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/", "desktop": False, "mobile": False},
    {"name": "profilakticheskiy", "path": "/zavisimosti/genotipirovanie/profilakticheskiy-analiz/", "desktop": True, "mobile": True},
    {"name": "task002-nark", "path": "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/", "desktop": True, "mobile": False},
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    server = subprocess.Popen(
        ["python", "-m", "http.server", str(PORT)],
        cwd=str(DIST),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(2)
    base = f"http://127.0.0.1:{PORT}"
    results = []

    legacy_html = urllib.request.urlopen(base + "/genotipirovanie/", timeout=10).read().decode("utf-8", "ignore")
    results.append(
        {
            "page": "legacy-alias",
            "viewport": "http",
            "legacy_ok": "/zavisimosti/" in legacy_html and "noindex" in legacy_html,
            "result": "PASS" if "/zavisimosti/" in legacy_html and "noindex" in legacy_html else "FAIL",
        }
    )

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            for viewport_name, size in [("desktop", (1437, 1000)), ("mobile", (380, 900))]:
                context = browser.new_context(viewport={"width": size[0], "height": size[1]})
                page = context.new_page()
                console_errors: list[str] = []

                def on_console(msg):
                    if msg.type == "error":
                        console_errors.append(msg.text)

                page.on("console", on_console)

                for check in CHECKS:
                    if not check.get(viewport_name):
                        continue
                    url = base + check["path"]
                    page.goto(url, wait_until="domcontentloaded", timeout=30000)
                    overflow = page.evaluate(
                        "() => document.documentElement.scrollWidth > window.innerWidth + 1"
                    )
                    failed_requests = []
                    results.append(
                        {
                            "page": check["name"],
                            "viewport": viewport_name,
                            "url": check["path"],
                            "http_ok": page.url.startswith(base),
                            "overflow": bool(overflow),
                            "console_errors": list(console_errors),
                            "result": "PASS" if not overflow and not console_errors else "FAIL",
                        }
                    )
                    console_errors.clear()

                if viewport_name == "desktop":
                    page.goto(base + "/", wait_until="domcontentloaded")
                    page.click("#home-treatment-prevention-trigger-2")
                    links = page.locator("#home-treatment-prevention-panel-2 a.home-treatment-prevention__service-item")
                    results.append(
                        {
                            "page": "home-mental-health-links",
                            "viewport": viewport_name,
                            "link_count": links.count(),
                            "result": "PASS" if links.count() == 6 else "FAIL",
                        }
                    )

                context.close()
            browser.close()
    finally:
        server.terminate()
        server.wait(timeout=5)

    receipt = {
        "timestamp": utc_now(),
        "pass": "URGENT-V2-BROWSER-SMOKE",
        "checks": results,
        "result": "PASS" if all(r.get("result") == "PASS" for r in results) else "FAIL",
    }
    out = EVIDENCE / "URGENT-V2-BROWSER-SMOKE.json"
    out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": receipt["result"], "checks": len(results)}, ensure_ascii=False))
    return 0 if receipt["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
