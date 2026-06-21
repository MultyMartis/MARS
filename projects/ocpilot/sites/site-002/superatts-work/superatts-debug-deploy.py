#!/usr/bin/env python3
"""SITE-002 — inject super_atts debug marker into live producthero.twig, deploy to TEST, screenshot."""
import asyncio
import ftplib
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from html import unescape

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK = os.path.join(BASE, "superatts-work")
QA = os.path.join(BASE, "qa", "superatts-debug")
REMOTE_TWIG = "catalog/view/theme/default/template/product/producthero.twig"
CACHE_DIR = "system/storage/cache"

PDP_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)

DEBUG_MARKER = "MARS-SUPER-ATTS-DEBUG"
DEBUG_BLOCK = """          {# """ + DEBUG_MARKER + """ — temporary QA probe #}
          <pre data-debug="super-atts">SUPER_ATTS COUNT: {{ super_atts|default([])|length }}
{% for a in super_atts|default([])|slice(0, 3) %}DEBUG[{{ loop.index }}]: name={{ a.name }} | text={{ a.text }} | attribute_id={{ a.attribute_id|default('?') }}
{% else %}DEBUG: super_atts has no items
{% endfor %}</pre>
"""

LOOP_ANCHOR = "          {% if super_atts %}"


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path):
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def ftp_upload(remote_path, data):
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_cache():
    cleared = []
    errors = []
    ftp = ftp_connect()
    try:
        ftp.cwd(CACHE_DIR)
        entries = []
        ftp.retrlines("LIST", entries.append)
        for line in entries:
            parts = line.split(None, 8)
            if len(parts) < 9:
                continue
            name = parts[8]
            if name in (".", "..", "index.html"):
                continue
            if line.startswith("d"):
                continue
            try:
                ftp.delete(name)
                cleared.append(name)
            except ftplib.error_perm as e:
                errors.append(f"{name}: {e}")
    except Exception as e:
        errors.append(str(e))
    finally:
        ftp.quit()
    return cleared, errors


def inject_debug(text):
    if DEBUG_MARKER in text:
        return text, False
    if LOOP_ANCHOR not in text:
        raise RuntimeError("super_atts loop anchor not found in live producthero.twig")
    patched = text.replace(LOOP_ANCHOR, DEBUG_BLOCK + LOOP_ANCHOR, 1)
    return patched, True


def parse_debug_from_html(html):
    m = re.search(r'<pre[^>]*data-debug="super-atts"[^>]*>(.*?)</pre>', html, re.S)
    if not m:
        return None
    raw = unescape(re.sub(r"<[^>]+>", "", m.group(1)))
    raw = re.sub(r"\r\n?", "\n", raw).strip()
    lines = [ln.strip() for ln in raw.split("\n") if ln.strip()]
    count = None
    items = []
    for ln in lines:
        if ln.startswith("SUPER_ATTS COUNT:"):
            count = int(re.search(r"\d+", ln).group())
        elif ln.startswith("DEBUG["):
            items.append(ln)
        elif ln == "DEBUG: super_atts has no items":
            items.append(ln)
    return {"count": count, "lines": lines, "items": items}


def classify(count, items):
    if count == 0:
        return "a"
    dim_names = {"длина, мм", "ширина, мм", "высота, мм", "масса, кг"}
    parsed_names = []
    for it in items:
        nm = re.search(r"name=([^|]+)", it)
        if nm:
            parsed_names.append(nm.group(1).strip().lower())
    if count == 4 and parsed_names and all(n in dim_names for n in parsed_names):
        return "b"
    if count > 4:
        return "c"
    if count <= 4 and parsed_names and all(n in dim_names for n in parsed_names):
        return "b"
    return "unknown"


async def screenshot(url, out_path):
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        page = await context.new_page()
        await page.goto(url, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector(".product-hero", timeout=30000)
        await page.locator(".product-hero").screenshot(path=out_path)
        await context.close()
        await browser.close()


def main():
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(QA, exist_ok=True)

    live_raw = ftp_download(REMOTE_TWIG)
    live_text = live_raw.decode("utf-8", "replace")

    bak_path = os.path.join(WORK, "producthero.live.pre-debug.bak")
    with open(bak_path, "wb") as f:
        f.write(live_raw)

    patched_text, changed = inject_debug(live_text)
    debug_local = os.path.join(WORK, "producthero.debug.twig")
    with open(debug_local, "w", encoding="utf-8") as f:
        f.write(patched_text)

    if changed:
        ftp_upload(REMOTE_TWIG, patched_text.encode("utf-8"))

    cleared, cache_errors = clear_cache()

    html = urllib.request.urlopen(PDP_URL, timeout=60).read().decode("utf-8", "replace")
    debug_info = parse_debug_from_html(html)
    verdict = classify(debug_info["count"], debug_info["items"]) if debug_info else "unknown"

    shot_path = os.path.join(QA, "spkb-18-7-vl5-super-atts-debug.png")
    asyncio.run(screenshot(PDP_URL, shot_path))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "pdp_url": PDP_URL,
        "remote_twig": REMOTE_TWIG,
        "debug_injected": changed,
        "backup_local": bak_path,
        "debug_local": debug_local,
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "debug_on_page": debug_info,
        "verdict_code": verdict,
        "screenshot": shot_path,
        "php_error": "Fatal error" in html or "Parse error" in html,
    }
    out_path = os.path.join(WORK, "superatts-debug-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
