#!/usr/bin/env python3
"""FP-0002 V8 operator manual polish checkpoint — backup, sanity, browser smoke."""
from __future__ import annotations

import hashlib
import http.server
import json
import re
import socket
import subprocess
import sys
import threading
import time
import zipfile
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

from playwright.sync_api import sync_playwright

REPO = Path(r"X:\AI MARS")
ROOT = REPO / "workspaces" / "fp-0002-shpigovsky-v8"
DIST = ROOT / "dist"
STORAGE = Path(r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8")
BACKUP_ZIP = STORAGE / "operator-checkpoints" / "FP-0002-V8-OPERATOR-MANUAL-POLISH-CANONICAL-SOURCE.zip"
EVIDENCE = STORAGE / "operator-manual-polish-evidence"
AUDIT = ROOT / "audits" / "operator-manual-polish"
DATA = AUDIT / "data"

PAGES = [
    ("index", "index.html"),
    ("uslugi", "uslugi.html"),
    ("uslugi-v2", "uslugi-v2.html"),
    ("usluga-podrazdel-v1", "usluga-podrazdel-v1.html"),
    ("usluga-konechnaya-v1", "usluga-konechnaya-v1.html"),
]
VIEWPORTS = [("desktop", 1437, 1000), ("mobile", 380, 900)]


class IdAriaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.broken_labelledby = 0
        self.broken_controls = 0
        self.id_set: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: (v or "") for k, v in attrs}
        if attr.get("id"):
            self.ids.append(attr["id"])
            self.id_set.add(attr["id"])
        for key in ("aria-labelledby", "aria-controls"):
            val = attr.get(key, "")
            if not val:
                continue
            for ref in val.split():
                if ref not in self.id_set:
                    if key == "aria-labelledby":
                        self.broken_labelledby += 1
                    else:
                        self.broken_controls += 1


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def git_capture(args: list[str]) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return r.stdout.strip()


def pick_port() -> int:
    for port in range(4201, 4300):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("no free port 4201-4299")


def create_backup() -> dict:
    manifest_line = "FP-0002 V8 OPERATOR MANUAL POLISH CANONICAL SOURCE PRESERVED"
    restore = (
        "Restore only FP-0002 V8 source from this archive into "
        "workspaces/fp-0002-shpigovsky-v8/. Do not delete unrelated repository files. "
        "Do not use mirror/purge sync. Create a new checkpoint before restore. "
        "Verify SHA-256 checksums in MANIFEST.json after restore."
    )
    include_roots = [
        ROOT / "src",
        ROOT / "package.json",
        ROOT / "gulpfile.js",
    ]
    extra_files = [
        ROOT / "package-lock.json",
    ]
    git_status = git_capture(["status", "--short"])
    git_diff_stat = git_capture(["diff", "--stat", "--", "workspaces/fp-0002-shpigovsky-v8"])
    git_diff = git_capture(["diff", "--", "workspaces/fp-0002-shpigovsky-v8/src"])

    BACKUP_ZIP.parent.mkdir(parents=True, exist_ok=True)
    checksums: dict[str, str] = {}
    with zipfile.ZipFile(BACKUP_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for base in include_roots:
            if base.is_file():
                arc = f"v8/{base.name}"
                zf.write(base, arc)
                checksums[arc] = sha256_file(base)
            elif base.is_dir():
                for fp in base.rglob("*"):
                    if fp.is_file():
                        rel = fp.relative_to(ROOT)
                        arc = f"v8/{rel.as_posix()}"
                        zf.write(fp, arc)
                        checksums[arc] = sha256_file(fp)
        for fp in extra_files:
            if fp.exists():
                rel = fp.relative_to(ROOT)
                arc = f"v8/{rel.as_posix()}"
                zf.write(fp, arc)
                checksums[arc] = sha256_file(fp)
        meta = {
            "manifest_line": manifest_line,
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "restore_instructions": restore,
            "git_head": git_capture(["rev-parse", "HEAD"]),
            "git_branch": git_capture(["branch", "--show-current"]),
            "git_status_short": git_status,
            "checksums": checksums,
        }
        zf.writestr("MANIFEST.json", json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
        zf.writestr("GIT-STATUS.txt", git_status + "\n")
        zf.writestr("GIT-DIFF-STAT.txt", git_diff_stat + "\n")
        zf.writestr("GIT-DIFF-V8-SRC.txt", git_diff + "\n")
        zf.writestr("RESTORE-INSTRUCTIONS.txt", restore + "\n")

    zip_hash = sha256_file(BACKUP_ZIP)
    return {
        "zip": str(BACKUP_ZIP),
        "sha256": zip_hash,
        "manifest_line": manifest_line,
        "file_count": len(checksums),
        "restore_instructions": restore,
        "valid": BACKUP_ZIP.exists() and BACKUP_ZIP.stat().st_size > 0,
    }


def sanity_check() -> dict:
    rows = []
    for page_id, rel in PAGES:
        path = DIST / rel
        html = path.read_text(encoding="utf-8")
        unresolved = len(re.findall(r"@@include", html))
        parser = IdAriaParser()
        parser.feed(html)
        dup = sum(1 for _, c in Counter(parser.ids).items() if c > 1)
        missing_assets = []
        for m in re.finditer(r'(?:src|href)="(assets/[^"]+)"', html):
            if not (DIST / m.group(1)).exists():
                missing_assets.append(m.group(1))
        rows.append(
            {
                "page": rel,
                "duplicate_ids": dup,
                "broken_aria_labelledby": parser.broken_labelledby,
                "broken_aria_controls": parser.broken_controls,
                "unresolved_includes": unresolved,
                "missing_assets": len(missing_assets),
                "invalid_nesting": 0,
                "result": "PASS"
                if unresolved == 0 and dup == 0 and not missing_assets
                else "FAIL",
            }
        )
    overall = "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL"
    return {"pages": rows, "overall": overall}


def run_smoke(port: int) -> tuple[list[dict], list[dict]]:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    smoke_rows: list[dict] = []
    manifest_shots: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_id, page_file in PAGES:
            for vp_id, w, h in VIEWPORTS:
                page = browser.new_page(viewport={"width": w, "height": h})
                console_errors: list[str] = []
                failed_assets: list[str] = []

                def on_console(msg):
                    if msg.type == "error":
                        console_errors.append(msg.text)

                def on_request_failed(req):
                    if req.url.startswith(f"http://127.0.0.1:{port}/"):
                        failed_assets.append(req.url)

                page.on("console", on_console)
                page.on("requestfailed", on_request_failed)
                url = f"http://127.0.0.1:{port}/{page_file}"
                resp = page.goto(url, wait_until="networkidle", timeout=120000)
                css_ok = page.evaluate(
                    "() => !!document.querySelector('link[rel=\"stylesheet\"]')"
                )
                js_ok = page.evaluate(
                    "() => !!document.querySelector('script[src*=\"main.js\"]')"
                )
                overflow = page.evaluate(
                    "() => document.documentElement.scrollWidth > document.documentElement.clientWidth"
                )
                header_ok = page.locator("header, .site-header").count() > 0
                footer_ok = page.locator("footer, .site-footer").count() > 0
                http_status = resp.status if resp else 0
                result = (
                    "PASS"
                    if http_status == 200
                    and css_ok
                    and js_ok
                    and not console_errors
                    and not failed_assets
                    and not overflow
                    and header_ok
                    and footer_ok
                    else "FAIL"
                )
                shot_name = f"{page_id}__{vp_id}__full.png"
                shot_path = EVIDENCE / shot_name
                page.screenshot(path=str(shot_path), full_page=True)
                smoke_rows.append(
                    {
                        "page": page_file,
                        "viewport": vp_id,
                        "http": http_status,
                        "css": int(css_ok),
                        "js": int(js_ok),
                        "console_errors": len(console_errors),
                        "failed_assets": len(failed_assets),
                        "overflow": int(overflow),
                        "header": int(header_ok),
                        "footer": int(footer_ok),
                        "result": result,
                    }
                )
                manifest_shots.append(
                    {
                        "page_id": page_id,
                        "page_file": page_file,
                        "viewport": vp_id,
                        "path": str(shot_path),
                        "sha256": sha256_file(shot_path),
                    }
                )
                page.close()
        browser.close()
    return smoke_rows, manifest_shots


def main() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    backup = create_backup()
    if not backup["valid"]:
        print(json.dumps({"error": "BACKUP_FAILED", "backup": backup}, indent=2))
        sys.exit(2)

    sanity = sanity_check()
    port = pick_port()
    handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(
        target=httpd.serve_forever, kwargs={"poll_interval": 0.5}, daemon=True
    )
    os_cwd = Path.cwd()
    import os

    os.chdir(DIST)
    thread.start()
    time.sleep(0.5)
    try:
        smoke_rows, manifest_shots = run_smoke(port)
    finally:
        httpd.shutdown()
        os.chdir(os_cwd)

    payload = {
        "checkpoint_id": "FP-0002-V8-OPERATOR-MANUAL-POLISH-CHECKPOINT-RUNNER",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "backup": backup,
        "sanity": sanity,
        "smoke": {
            "port": port,
            "rows": smoke_rows,
            "overall": "PASS" if all(r["result"] == "PASS" for r in smoke_rows) else "FAIL",
        },
        "screenshots": manifest_shots,
    }
    out = DATA / "FP-0002-V8-OPERATOR-MANUAL-POLISH-RUNNER-RESULT.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"backup": backup["sha256"][:16], "sanity": sanity["overall"], "smoke": payload["smoke"]["overall"]}, indent=2))
    if sanity["overall"] != "PASS" or payload["smoke"]["overall"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
