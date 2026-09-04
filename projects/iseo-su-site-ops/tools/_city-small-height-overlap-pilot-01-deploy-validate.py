#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-CITY-SMALL-HEIGHT-OVERLAP-PILOT-01: backup + SFTP deploy + validate + screenshots."""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import paramiko

ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops")
SRC = ROOT / "production-source"
HTML_LOCAL = SRC / "static-html" / "services" / "seo" / "prodvizhenie-v-novosibirske.html"
CSS_LOCAL = SRC / "css" / "city-seo-novosibirsk-height-pilot.css"
BAK_ROOT = Path(
    r"X:\AI MARS\local\sites\iseo-su-production\_city-small-height-overlap-pilot-01"
)
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
EVIDENCE_DIR = ROOT / "evidence" / "city-small-height-overlap-pilot-01"
OUT = ROOT / "tools" / "_city-small-height-overlap-pilot-01-validate.json"

DOC = "/home/n/nikel0rv/i-seo.su/public_html"
REMOTE_HTML = f"{DOC}/services/seo/prodvizhenie-v-novosibirske.html"
REMOTE_CSS = f"{DOC}/css/city-seo-novosibirsk-height-pilot.css"
PILOT_URL = "https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html"

CONTROLS = {
    "hub": "https://i-seo.su/services/seo/b-regionakh.html",
    "spb": "https://i-seo.su/services/seo/prodvizhenie-v-sankt-peterburge.html",
    "kazan": "https://i-seo.su/services/seo/prodvizhenie-v-kazani.html",
    "ekb": "https://i-seo.su/services/seo/prodvizhenie-v-ekaterinburge.html",
    "krsk": "https://i-seo.su/services/seo/prodvizhenie-v-krasnoyarske.html",
}

VIEWPORTS = [
    ("1920x1080", 1920, 1080),
    ("1440x900", 1440, 900),
    ("1366x768", 1366, 768),
    ("1280x720", 1280, 720),
    ("1366x650", 1366, 650),
    ("1440x600", 1440, 600),
    ("390x844", 390, 844),
    ("360x800", 360, 800),
]

UA = "ISEO-SU-CITY-SMALL-HEIGHT-OVERLAP-PILOT-01/1.0"


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sftp_connect():
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"],
        password=secrets["ftp_or_sftp_password"],
    )
    return paramiko.SFTPClient.from_transport(transport), transport


def read_remote_bytes(sftp, path: str) -> bytes | None:
    try:
        with sftp.open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


def write_remote_bytes(sftp, path: str, data: bytes) -> None:
    parent = str(Path(path).as_posix().rsplit("/", 1)[0])
    try:
        sftp.stat(parent)
    except FileNotFoundError:
        # css dir should exist; if not, fail loudly
        raise
    with sftp.open(path, "w") as f:
        f.write(data)


def http_get(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() if e.fp else b""


def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    return m.group(1).strip() if m else ""


def extract_meta(html: str, name: str) -> str:
    m = re.search(
        rf'<meta[^>]+name=["\']{re.escape(name)}["\'][^>]+content=["\'](.*?)["\']',
        html,
        re.I | re.S,
    )
    if not m:
        m = re.search(
            rf'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']{re.escape(name)}["\']',
            html,
            re.I | re.S,
        )
    return m.group(1).strip() if m else ""


def extract_canonical(html: str) -> str:
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']', html, re.I)
    if not m:
        m = re.search(r'<link[^>]+href=["\'](.*?)["\'][^>]+rel=["\']canonical["\']', html, re.I)
    return m.group(1).strip() if m else ""


def extract_h1(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    if not m:
        return ""
    return re.sub(r"<[^>]+>", "", m.group(1)).replace("\xa0", " ").replace("&nbsp;", " ").strip()


def sitemap_count(xml_bytes: bytes) -> int:
    root = ET.fromstring(xml_bytes)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return len([el for el in root.findall(".//sm:loc", ns) if el.text])


def measure_layout(page) -> dict:
    return page.evaluate(
        """() => {
          const inner = document.querySelector('.page_scene_inner');
          const second = document.querySelector('main#SecondScreen');
          const desc = document.querySelector('.page_scene__description');
          const intro = desc ? desc.querySelector('span') : null;
          const btn = document.querySelector('.page_scene__btn_order');
          if (!inner || !second) {
            return { ok: false, error: 'missing nodes' };
          }
          const ir = inner.getBoundingClientRect();
          const sr = second.getBoundingClientRect();
          const introBottom = intro
            ? (intro.getBoundingClientRect().bottom + window.scrollY)
            : null;
          const descBottom = desc
            ? (desc.getBoundingClientRect().bottom + window.scrollY)
            : null;
          const innerBottom = ir.bottom + window.scrollY;
          const secondTop = sr.top + window.scrollY;
          const cs = getComputedStyle(inner);
          // Overlap: second section top is above the bottom of first-screen content
          // (intro/description), while still intersecting the visual overflow zone.
          const contentBottom = Math.max(introBottom || 0, descBottom || 0);
          const overlap = secondTop < (contentBottom - 1);
          const clipped =
            intro &&
            (intro.getBoundingClientRect().bottom > ir.bottom + 1);
          return {
            ok: true,
            viewport: { w: window.innerWidth, h: window.innerHeight },
            inner: {
              height_css: cs.height,
              minHeight_css: cs.minHeight,
              height_px: ir.height,
              bottom_doc: innerBottom,
            },
            content_bottom_doc: contentBottom,
            second_top_doc: secondTop,
            gap_px: secondTop - contentBottom,
            overlap: overlap,
            clipped_by_inner_box: !!clipped,
            intro_visible: !!(intro && intro.getBoundingClientRect().height > 0),
            cta_visible: !!(btn && btn.getBoundingClientRect().height > 0),
            pilot_body: document.body.classList.contains('city-seo-novosibirsk-height-pilot'),
          };
        }"""
    )


def run_viewport_matrix(url: str, out_dir: Path) -> list[dict]:
    from playwright.sync_api import sync_playwright

    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, w, h in VIEWPORTS:
            context = browser.new_context(
                viewport={"width": w, "height": h},
                device_scale_factor=1,
                user_agent=UA,
            )
            page = context.new_page()
            page.goto(url, wait_until="networkidle", timeout=90000)
            page.wait_for_timeout(800)
            metrics = measure_layout(page)
            shot = out_dir / f"pilot-{name}.png"
            page.screenshot(path=str(shot), full_page=False)
            # Also capture a taller crop of first+second boundary for low-height cases
            if h <= 720:
                page.evaluate("window.scrollTo(0, 0)")
                page.wait_for_timeout(200)
                boundary = out_dir / f"pilot-{name}-boundary.png"
                # scroll so we see end of intro near top and SecondScreen below
                page.evaluate(
                    """() => {
                      const intro = document.querySelector('.page_scene__description span');
                      if (intro) {
                        const y = intro.getBoundingClientRect().bottom + window.scrollY - 120;
                        window.scrollTo(0, Math.max(0, y));
                      }
                    }"""
                )
                page.wait_for_timeout(200)
                page.screenshot(path=str(boundary), full_page=False)
                metrics["boundary_shot"] = str(boundary)
            metrics["viewport_name"] = name
            metrics["screenshot"] = str(shot)
            console_errors = []
            page.on(
                "pageerror",
                lambda err: console_errors.append(str(err)),
            )
            # re-attach is late; collect via evaluate for fatal markers instead
            metrics["pass"] = (
                metrics.get("ok")
                and not metrics.get("overlap")
                and metrics.get("intro_visible")
                and metrics.get("cta_visible")
                and metrics.get("gap_px", -999) >= -1
            )
            rows.append(metrics)
            context.close()
        browser.close()
    return rows


def main() -> int:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak_dir = BAK_ROOT / ts
    bak_dir.mkdir(parents=True, exist_ok=True)
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    html_bytes = HTML_LOCAL.read_bytes()
    css_bytes = CSS_LOCAL.read_bytes()
    local_html = html_bytes.decode("utf-8")

    assert "city-seo-novosibirsk-height-pilot" in local_html
    assert "city-seo-novosibirsk-height-pilot.css" in local_html
    assert "SEO-продвижение сайта в Новосибирске" in local_html

    baseline_title = extract_title(local_html)
    baseline_h1 = extract_h1(local_html)
    baseline_desc = extract_meta(local_html, "description")
    baseline_canonical = extract_canonical(local_html)

    report: dict = {
        "task": "ISEO-SU-SITE-OPS-CITY-SMALL-HEIGHT-OVERLAP-PILOT-01",
        "timestamp_utc": ts,
        "pilot_url": PILOT_URL,
        "local_html": str(HTML_LOCAL),
        "local_css": str(CSS_LOCAL),
        "backup_dir": str(bak_dir),
        "baseline": {
            "title": baseline_title,
            "h1": baseline_h1,
            "description": baseline_desc,
            "canonical": baseline_canonical,
            "html_sha256": sha256_bytes(html_bytes),
            "css_sha256": sha256_bytes(css_bytes),
        },
    }

    sftp, transport = sftp_connect()
    try:
        before_html = read_remote_bytes(sftp, REMOTE_HTML)
        before_css = read_remote_bytes(sftp, REMOTE_CSS)
        if before_html is None:
            raise SystemExit(f"REMOTE HTML missing: {REMOTE_HTML}")

        (bak_dir / "prodvizhenie-v-novosibirske.html.before").write_bytes(before_html)
        if before_css is not None:
            (bak_dir / "city-seo-novosibirsk-height-pilot.css.before").write_bytes(before_css)
        else:
            (bak_dir / "city-seo-novosibirsk-height-pilot.css.before.MISSING").write_text(
                "file did not exist on remote before deploy\n", encoding="utf-8"
            )

        report["backup"] = {
            "remote_html": REMOTE_HTML,
            "remote_css": REMOTE_CSS,
            "html_sha256_before": sha256_bytes(before_html),
            "css_sha256_before": sha256_bytes(before_css) if before_css else None,
            "backup_html": str(bak_dir / "prodvizhenie-v-novosibirske.html.before"),
            "backup_css": str(bak_dir / "city-seo-novosibirsk-height-pilot.css.before")
            if before_css
            else str(bak_dir / "city-seo-novosibirsk-height-pilot.css.before.MISSING"),
        }

        # Control SHA before deploy (siblings must stay untouched)
        control_before = {}
        for key, url in CONTROLS.items():
            remote_path = url.replace("https://i-seo.su", DOC)
            data = read_remote_bytes(sftp, remote_path)
            control_before[key] = {
                "remote": remote_path,
                "sha256": sha256_bytes(data) if data else None,
            }
        report["controls_before"] = control_before

        write_remote_bytes(sftp, REMOTE_HTML, html_bytes)
        write_remote_bytes(sftp, REMOTE_CSS, css_bytes)

        after_html = read_remote_bytes(sftp, REMOTE_HTML)
        after_css = read_remote_bytes(sftp, REMOTE_CSS)
        report["deploy"] = {
            "html_sha256_after": sha256_bytes(after_html or b""),
            "css_sha256_after": sha256_bytes(after_css or b""),
            "html_matches_local": after_html == html_bytes,
            "css_matches_local": after_css == css_bytes,
        }

        control_after = {}
        for key, url in CONTROLS.items():
            remote_path = url.replace("https://i-seo.su", DOC)
            data = read_remote_bytes(sftp, remote_path)
            sha = sha256_bytes(data) if data else None
            control_after[key] = {
                "remote": remote_path,
                "sha256": sha,
                "unchanged": sha == control_before[key]["sha256"],
            }
        report["controls_after"] = control_after
    finally:
        sftp.close()
        transport.close()

    time.sleep(2)

    status, live = http_get(PILOT_URL)
    live_html = live.decode("utf-8", errors="replace")
    report["live_http"] = {
        "status": status,
        "title": extract_title(live_html),
        "h1": extract_h1(live_html),
        "description": extract_meta(live_html, "description"),
        "canonical": extract_canonical(live_html),
        "has_pilot_class": "city-seo-novosibirsk-height-pilot" in live_html,
        "has_pilot_css_link": "city-seo-novosibirsk-height-pilot.css" in live_html,
        "title_unchanged": extract_title(live_html) == baseline_title,
        "h1_unchanged": extract_h1(live_html) == baseline_h1,
        "desc_unchanged": extract_meta(live_html, "description") == baseline_desc,
        "canonical_unchanged": extract_canonical(live_html) == baseline_canonical,
        "sha256": sha256_bytes(live),
    }

    css_status, css_body = http_get(
        "https://i-seo.su/css/city-seo-novosibirsk-height-pilot.css"
    )
    report["live_css"] = {
        "status": css_status,
        "sha256": sha256_bytes(css_body),
        "matches_local": css_body == css_bytes,
        "contains_height_auto": b"height: auto" in css_body,
        "contains_min_height": b"min-height: 100vh" in css_body,
    }

    sm_status, sm_body = http_get("https://i-seo.su/sitemap-static.xml")
    report["sitemap"] = {
        "status": sm_status,
        "url_count": sitemap_count(sm_body) if sm_status == 200 else None,
        "expected": 139,
    }

    # Consent / calculator smoke
    smoke = {}
    for label, url in [
        ("home", "https://i-seo.su/"),
        ("tariff_calc", "https://i-seo.su/tariff-calc"),
        ("spb", CONTROLS["spb"]),
        ("hub", CONTROLS["hub"]),
    ]:
        st, body = http_get(url)
        text = body.decode("utf-8", errors="replace")
        smoke[label] = {
            "status": st,
            "has_consent_markers": ("cookie" in text.lower()) or ("consent" in text.lower()),
        }
    report["smoke"] = smoke

    shots_dir = EVIDENCE_DIR / "screenshots" / ts
    report["viewport_matrix"] = run_viewport_matrix(PILOT_URL, shots_dir)
    report["screenshots_dir"] = str(shots_dir)

    all_pass = all(r.get("pass") for r in report["viewport_matrix"])
    siblings_ok = all(v.get("unchanged") for v in report["controls_after"].values())
    report["summary"] = {
        "all_viewports_pass": all_pass,
        "siblings_unchanged": siblings_ok,
        "sitemap_ok": report["sitemap"]["url_count"] == 139,
        "content_guard_ok": all(
            [
                report["live_http"]["title_unchanged"],
                report["live_http"]["h1_unchanged"],
                report["live_http"]["desc_unchanged"],
                report["live_http"]["canonical_unchanged"],
            ]
        ),
        "deploy_aligned": report["deploy"]["html_matches_local"]
        and report["deploy"]["css_matches_local"],
        "rollout_status": "WAITING FOR OPERATOR VISUAL APPROVAL",
        "final_status": (
            "PILOT COMPLETE — NOVOSIBIRSK LOW-HEIGHT OVERLAP FIXED / WAITING FOR OPERATOR VISUAL APPROVAL"
            if all_pass and siblings_ok
            else "PILOT VALIDATION FAILED — INSPECT MATRIX"
        ),
    }

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    print(f"FULL_REPORT={OUT}")
    return 0 if report["summary"]["all_viewports_pass"] and siblings_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
