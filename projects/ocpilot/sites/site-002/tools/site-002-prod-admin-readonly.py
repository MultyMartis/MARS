#!/usr/bin/env python3
"""SITE-002 Production admin read-only inspection."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
OUT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01\admin-readonly\admin-observations.md"
)


def parse_admin():
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    am = re.search(r"^### OpenCart Admin\s*$([\s\S]*?)(?=^### |\Z)", m.group(1), re.M)
    fields = {}
    ck = None
    for line in am.group(1).splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            ck = s[:-1].strip().lower()
            fields.setdefault(ck, "")
            continue
        if ck:
            fields[ck] = s
    return fields


def main() -> int:
    admin = parse_admin()
    url = admin.get("url", "https://bzpm.ru/admin/")
    lines = [
        "# Admin read-only observations",
        "",
        f"Captured: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
        f"Admin URL: {url}",
        "",
    ]
    status = "FAILED"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.fill('input[name="username"]', admin["login"])
            page.fill('input[name="password"]', admin["password"])
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle", timeout=30000)
            if "common/login" in page.url or "route=common/login" in page.url:
                lines.append("## Result")
                lines.append("- Status: **FAILED** — login rejected or still on login page")
                lines.append(f"- Final URL: {page.url}")
            else:
                status = "COMPLETED READ-ONLY"
                body = page.content()
                version = None
                for pat in [r"Version\s*([\d.]+)", r"ocStore\s*([\d.]+)"]:
                    m = re.search(pat, body, re.I)
                    if m:
                        version = m.group(1)
                        break
                theme = None
                m = re.search(r"theme[^<]{0,40}default", body, re.I)
                if m:
                    theme = "default (inferred from dashboard HTML)"
                lines.extend(
                    [
                        "## Result",
                        "- Status: **COMPLETED READ-ONLY**",
                        f"- Dashboard URL: {page.url}",
                        f"- Version label: {version or 'SAFE UNKNOWN'}",
                        f"- Theme hint: {theme or 'SAFE UNKNOWN'}",
                        "",
                        "## Sanitized notes",
                        "- No settings saved",
                        "- No cache cleared",
                        "- No exports performed",
                    ]
                )
                page.goto(url + "index.php?route=common/logout", timeout=15000)
        except Exception as exc:
            lines.append(f"## Result\n- Status: **FAILED**\n- Error: {type(exc).__name__}")
        browser.close()

    lines.insert(3, f"Inspection status: **{status}**")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("admin:", status)
    return 0 if status == "COMPLETED READ-ONLY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
