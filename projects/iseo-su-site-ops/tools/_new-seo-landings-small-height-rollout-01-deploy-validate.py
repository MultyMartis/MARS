#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-NEW-SEO-LANDINGS-SMALL-HEIGHT-OVERLAP-ROLLOUT-01: backup + SFTP deploy + validate."""
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
HTML_DIR = SRC / "static-html" / "services" / "seo"
CSS_LOCAL = SRC / "css" / "new-seo-landing-flex-first-screen.css"
PILOT_CSS_NAME = "city-seo-novosibirsk-height-pilot.css"
BAK_ROOT = Path(
    r"X:\AI MARS\local\sites\iseo-su-production\_new-seo-landings-small-height-rollout-01"
)
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
EVIDENCE_DIR = ROOT / "evidence" / "new-seo-landings-small-height-rollout-01"
OUT = ROOT / "tools" / "_new-seo-landings-small-height-rollout-01-validate.json"

DOC = "/home/n/nikel0rv/i-seo.su/public_html"
REMOTE_CSS = f"{DOC}/css/new-seo-landing-flex-first-screen.css"
REMOTE_PILOT_CSS = f"{DOC}/css/{PILOT_CSS_NAME}"

PAGES = [
    ("city", "prodvizhenie-v-sankt-peterburge.html"),
    ("city", "prodvizhenie-v-kazani.html"),
    ("city", "prodvizhenie-v-ekaterinburge.html"),
    ("city", "prodvizhenie-v-novosibirske.html"),
    ("city", "prodvizhenie-v-krasnoyarske.html"),
    ("niche", "prodvizhenie-sajta-pitomnika.html"),
    ("niche", "prodvizhenie-sajta-smi.html"),
    ("niche", "prodvizhenie-sajta-restorana.html"),
    ("niche", "prodvizhenie-internet-magazina-zapchastej.html"),
    ("niche", "prodvizhenie-sajta-internet-provajdera.html"),
    ("niche", "prodvizhenie-internet-magazina-kosmetiki.html"),
    ("niche", "prodvizhenie-internet-magazina-czvetov.html"),
    ("intl", "prodvizhenie-v-ssha.html"),
    ("intl", "prodvizhenie-v-oae.html"),
]

CONTROLS = {
    "hub_regions": "https://i-seo.su/services/seo/b-regionakh.html",
    "auto_niche_source": "https://i-seo.su/services/seo/prodvizhenie-avtomobilnogo-sajta.html",
    "zarubezhnye": "https://i-seo.su/services/seo/zarubezhnye.html",
    "seo_hub": "https://i-seo.su/services/seo.html",
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

# Full matrix on all 14 is expensive; required set + family representatives get all viewports.
FULL_MATRIX_PAGES = {
    "prodvizhenie-v-novosibirske.html",
    "prodvizhenie-v-sankt-peterburge.html",
    "prodvizhenie-sajta-pitomnika.html",
    "prodvizhenie-v-ssha.html",
}
REQUIRED_VIEWPORTS = [
    ("1440x900", 1440, 900),
    ("1366x768", 1366, 768),
    ("1280x720", 1280, 720),
    ("1366x650", 1366, 650),
    ("1440x600", 1440, 600),
    ("390x844", 390, 844),
    ("360x800", 360, 800),
]

UA = "ISEO-SU-NEW-SEO-LANDINGS-SMALL-HEIGHT-ROLLOUT-01/1.0"
SHARED_CLASS = "new-seo-landing-flex-first-screen"


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
    with sftp.open(path, "w") as f:
        f.write(data)


def remove_remote(sftp, path: str) -> bool:
    try:
        sftp.remove(path)
        return True
    except FileNotFoundError:
        return False


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


def page_url(name: str) -> str:
    return f"https://i-seo.su/services/seo/{name}"


def remote_html_path(name: str) -> str:
    return f"{DOC}/services/seo/{name}"


def measure_layout(page) -> dict:
    return page.evaluate(
        f"""() => {{
          const inner = document.querySelector('.page_scene_inner');
          const second = document.querySelector('main#SecondScreen');
          const desc = document.querySelector('.page_scene__description');
          const intro = desc ? desc.querySelector('span') : null;
          const btn = document.querySelector('.page_scene__btn_order');
          if (!inner || !second) {{
            return {{ ok: false, error: 'missing nodes' }};
          }}
          const ir = inner.getBoundingClientRect();
          const sr = second.getBoundingClientRect();
          const introBottom = intro
            ? (intro.getBoundingClientRect().bottom + window.scrollY)
            : null;
          const descBottom = desc
            ? (desc.getBoundingClientRect().bottom + window.scrollY)
            : null;
          const contentBottom = Math.max(introBottom || 0, descBottom || 0);
          const secondTop = sr.top + window.scrollY;
          const cs = getComputedStyle(inner);
          const overlap = secondTop < (contentBottom - 1);
          const clipped =
            intro &&
            (intro.getBoundingClientRect().bottom > ir.bottom + 1);
          const heightPx = parseFloat(cs.height) || ir.height;
          const vh = window.innerHeight;
          const excessive_blank =
            heightPx > (contentBottom - (ir.top + window.scrollY) + 180) &&
            heightPx > vh + 120;
          return {{
            ok: true,
            viewport: {{ w: window.innerWidth, h: window.innerHeight }},
            inner: {{
              height_css: cs.height,
              minHeight_css: cs.minHeight,
              height_px: ir.height,
              bottom_doc: ir.bottom + window.scrollY,
            }},
            content_bottom_doc: contentBottom,
            second_top_doc: secondTop,
            gap_px: secondTop - contentBottom,
            overlap: overlap,
            clipped_by_inner_box: !!clipped,
            excessive_blank: !!excessive_blank,
            intro_visible: !!(intro && intro.getBoundingClientRect().height > 0),
            cta_visible: !!(btn && btn.getBoundingClientRect().height > 0),
            shared_body: document.body.classList.contains('{SHARED_CLASS}'),
            pilot_body: document.body.classList.contains('city-seo-novosibirsk-height-pilot'),
          }};
        }}"""
    )


def run_viewport_matrix(url: str, out_dir: Path, viewports: list[tuple]) -> list[dict]:
    from playwright.sync_api import sync_playwright

    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, w, h in viewports:
            context = browser.new_context(
                viewport={"width": w, "height": h},
                device_scale_factor=1,
                user_agent=UA,
            )
            page = context.new_page()
            page.goto(url, wait_until="networkidle", timeout=90000)
            page.wait_for_timeout(700)
            metrics = measure_layout(page)
            shot = out_dir / f"{name}.png"
            page.screenshot(path=str(shot), full_page=False)
            if h <= 720:
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
                boundary = out_dir / f"{name}-boundary.png"
                page.screenshot(path=str(boundary), full_page=False)
                metrics["boundary_shot"] = str(boundary)
            metrics["viewport_name"] = name
            metrics["screenshot"] = str(shot)
            metrics["pass"] = (
                metrics.get("ok")
                and not metrics.get("overlap")
                and not metrics.get("clipped_by_inner_box")
                and metrics.get("intro_visible")
                and metrics.get("cta_visible")
                and metrics.get("gap_px", -999) >= -1
                and metrics.get("shared_body") is True
                and metrics.get("pilot_body") is False
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
    shots_root = EVIDENCE_DIR / "screenshots" / ts
    shots_root.mkdir(parents=True, exist_ok=True)

    css_bytes = CSS_LOCAL.read_bytes()
    assert b"height: auto" in css_bytes
    assert b"min-height: 100vh" in css_bytes
    assert SHARED_CLASS.encode() in css_bytes

    page_locals: dict[str, dict] = {}
    for family, name in PAGES:
        path = HTML_DIR / name
        data = path.read_bytes()
        text = data.decode("utf-8")
        assert SHARED_CLASS in text, name
        assert f"{SHARED_CLASS}.css" in text, name
        assert "city-seo-novosibirsk-height-pilot" not in text, name
        page_locals[name] = {
            "family": family,
            "path": str(path),
            "bytes": data,
            "title": extract_title(text),
            "h1": extract_h1(text),
            "description": extract_meta(text, "description"),
            "canonical": extract_canonical(text),
            "sha256": sha256_bytes(data),
        }

    report: dict = {
        "task": "ISEO-SU-SITE-OPS-NEW-SEO-LANDINGS-SMALL-HEIGHT-OVERLAP-ROLLOUT-01",
        "timestamp_utc": ts,
        "rollout_model": "MODEL_A_ALL_14_SHARED_CLASS",
        "shared_class": SHARED_CLASS,
        "shared_css": str(CSS_LOCAL),
        "backup_dir": str(bak_dir),
        "screenshots_dir": str(shots_root),
        "pages_local": {
            n: {k: v for k, v in d.items() if k != "bytes"} for n, d in page_locals.items()
        },
    }

    sftp, transport = sftp_connect()
    try:
        backup_meta = []
        # Backup all 14 HTML + shared CSS + pilot CSS if present
        for family, name in PAGES:
            remote = remote_html_path(name)
            before = read_remote_bytes(sftp, remote)
            if before is None:
                raise SystemExit(f"REMOTE HTML missing: {remote}")
            bak_path = bak_dir / f"{name}.before"
            bak_path.write_bytes(before)
            backup_meta.append(
                {
                    "production_absolute_path": remote,
                    "backup_absolute_path": str(bak_path),
                    "sha256_before": sha256_bytes(before),
                    "timestamp_utc": ts,
                    "family": family,
                }
            )

        before_css = read_remote_bytes(sftp, REMOTE_CSS)
        css_bak = bak_dir / "new-seo-landing-flex-first-screen.css.before"
        if before_css is not None:
            css_bak.write_bytes(before_css)
        else:
            (bak_dir / "new-seo-landing-flex-first-screen.css.before.MISSING").write_text(
                "file did not exist on remote before deploy\n", encoding="utf-8"
            )
        backup_meta.append(
            {
                "production_absolute_path": REMOTE_CSS,
                "backup_absolute_path": str(css_bak)
                if before_css
                else str(bak_dir / "new-seo-landing-flex-first-screen.css.before.MISSING"),
                "sha256_before": sha256_bytes(before_css) if before_css else None,
                "timestamp_utc": ts,
            }
        )

        before_pilot = read_remote_bytes(sftp, REMOTE_PILOT_CSS)
        if before_pilot is not None:
            pilot_bak = bak_dir / f"{PILOT_CSS_NAME}.before"
            pilot_bak.write_bytes(before_pilot)
            backup_meta.append(
                {
                    "production_absolute_path": REMOTE_PILOT_CSS,
                    "backup_absolute_path": str(pilot_bak),
                    "sha256_before": sha256_bytes(before_pilot),
                    "timestamp_utc": ts,
                    "note": "pilot css removed after deploy",
                }
            )
        report["backup"] = backup_meta

        control_before = {}
        for key, url in CONTROLS.items():
            remote_path = url.replace("https://i-seo.su", DOC)
            data = read_remote_bytes(sftp, remote_path)
            control_before[key] = {
                "remote": remote_path,
                "sha256": sha256_bytes(data) if data else None,
            }
        report["controls_before"] = control_before

        # Deploy HTML + shared CSS; remove pilot CSS
        for name, meta in page_locals.items():
            write_remote_bytes(sftp, remote_html_path(name), meta["bytes"])
        write_remote_bytes(sftp, REMOTE_CSS, css_bytes)
        pilot_removed = remove_remote(sftp, REMOTE_PILOT_CSS)

        deploy_check = {}
        for name, meta in page_locals.items():
            after = read_remote_bytes(sftp, remote_html_path(name))
            deploy_check[name] = {
                "matches_local": after == meta["bytes"],
                "sha256_after": sha256_bytes(after or b""),
            }
        after_css = read_remote_bytes(sftp, REMOTE_CSS)
        after_pilot = read_remote_bytes(sftp, REMOTE_PILOT_CSS)
        report["deploy"] = {
            "pages": deploy_check,
            "css_matches_local": after_css == css_bytes,
            "css_sha256_after": sha256_bytes(after_css or b""),
            "pilot_css_removed": pilot_removed,
            "pilot_css_absent_after": after_pilot is None,
            "all_html_aligned": all(v["matches_local"] for v in deploy_check.values()),
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

    # Live SEO / class checks
    live_pages = {}
    for family, name in PAGES:
        url = page_url(name)
        status, body = http_get(url)
        text = body.decode("utf-8", errors="replace")
        base = page_locals[name]
        live_pages[name] = {
            "family": family,
            "url": url,
            "status": status,
            "title": extract_title(text),
            "h1": extract_h1(text),
            "description": extract_meta(text, "description"),
            "canonical": extract_canonical(text),
            "has_shared_class": SHARED_CLASS in text,
            "has_shared_css_link": f"{SHARED_CLASS}.css" in text,
            "has_pilot_class": "city-seo-novosibirsk-height-pilot" in text,
            "has_pilot_css_link": PILOT_CSS_NAME in text,
            "title_unchanged": extract_title(text) == base["title"],
            "h1_unchanged": extract_h1(text) == base["h1"],
            "desc_unchanged": extract_meta(text, "description") == base["description"],
            "canonical_unchanged": extract_canonical(text) == base["canonical"],
            "personal_data_consent": "personal_data_consent" in text,
            "sha256": sha256_bytes(body),
        }
    report["live_pages"] = live_pages

    css_status, css_body = http_get(
        f"https://i-seo.su/css/{SHARED_CLASS}.css"
    )
    pilot_css_status, _ = http_get(f"https://i-seo.su/css/{PILOT_CSS_NAME}")
    report["live_css"] = {
        "shared_status": css_status,
        "shared_sha256": sha256_bytes(css_body),
        "shared_matches_local": css_body == css_bytes,
        "pilot_css_http_status": pilot_css_status,
        "pilot_css_gone": pilot_css_status == 404,
    }

    sm_status, sm_body = http_get("https://i-seo.su/sitemap-static.xml")
    report["sitemap"] = {
        "status": sm_status,
        "url_count": sitemap_count(sm_body) if sm_status == 200 else None,
        "expected": 139,
    }

    # Form / calculator smoke
    smoke = {}
    for label, url in [
        ("home", "https://i-seo.su/"),
        ("tariff_calc", "https://i-seo.su/tariff-calc"),
        ("city_nsk", page_url("prodvizhenie-v-novosibirske.html")),
        ("niche_pitomnik", page_url("prodvizhenie-sajta-pitomnika.html")),
        ("intl_usa", page_url("prodvizhenie-v-ssha.html")),
        ("hub", CONTROLS["seo_hub"]),
    ]:
        st, body = http_get(url)
        text = body.decode("utf-8", errors="replace")
        smoke[label] = {
            "status": st,
            "has_personal_data_consent": "personal_data_consent" in text,
            "has_privacy": "privacy-policy.html" in text,
        }
    report["form_smoke"] = smoke

    # Viewport matrices
    viewport_results = {}
    total_overlaps = 0
    for family, name in PAGES:
        url = page_url(name)
        vps = VIEWPORTS if name in FULL_MATRIX_PAGES else REQUIRED_VIEWPORTS
        if name in FULL_MATRIX_PAGES and ("1920x1080", 1920, 1080) not in vps:
            pass
        rows = run_viewport_matrix(url, shots_root / name.replace(".html", ""), vps)
        overlaps = sum(1 for r in rows if r.get("overlap"))
        total_overlaps += overlaps
        viewport_results[name] = {
            "family": family,
            "url": url,
            "viewports": rows,
            "all_pass": all(r.get("pass") for r in rows),
            "overlap_count": overlaps,
        }
    report["viewport_matrix"] = viewport_results
    report["total_post_rollout_overlaps"] = total_overlaps

    # Aggregate required viewport flags across all pages
    required_flags = {}
    for vp_name, _, _ in REQUIRED_VIEWPORTS:
        statuses = []
        for name, block in viewport_results.items():
            row = next(
                (r for r in block["viewports"] if r.get("viewport_name") == vp_name),
                None,
            )
            statuses.append(bool(row and row.get("pass")))
        required_flags[vp_name] = all(statuses)

    seo_ok = all(
        p["title_unchanged"]
        and p["h1_unchanged"]
        and p["desc_unchanged"]
        and p["canonical_unchanged"]
        and p["status"] == 200
        and p["has_shared_class"]
        and not p["has_pilot_class"]
        and not p["has_pilot_css_link"]
        for p in live_pages.values()
    )
    controls_ok = all(v.get("unchanged") for v in report["controls_after"].values())
    all_vp_ok = all(v["all_pass"] for v in viewport_results.values())

    report["summary"] = {
        "new_seo_landings_audited": 14,
        "city_audited": 5,
        "niche_audited": 7,
        "intl_audited": 2,
        "rollout_model": "MODEL_A",
        "pilot_body_class_removed": all(not p["has_pilot_class"] for p in live_pages.values()),
        "pilot_css_removed": report["live_css"]["pilot_css_gone"]
        or report["deploy"]["pilot_css_absent_after"],
        "required_viewport_flags": required_flags,
        "total_post_rollout_overlaps": total_overlaps,
        "seo_ok": seo_ok,
        "sitemap_ok": report["sitemap"]["url_count"] == 139,
        "controls_ok": controls_ok,
        "all_viewports_pass": all_vp_ok,
        "deploy_aligned": report["deploy"]["all_html_aligned"]
        and report["deploy"]["css_matches_local"],
        "novosibirsk_pass": viewport_results["prodvizhenie-v-novosibirske.html"]["all_pass"],
        "final_status": (
            "COMPLETE — NEW SEO LANDINGS LOW-HEIGHT OVERLAP ROLLOUT / 14 PAGES SAFE / PILOT GENERALIZED"
            if all_vp_ok and seo_ok and controls_ok and total_overlaps == 0
            else "ROLLOUT VALIDATION FAILED — INSPECT MATRIX"
        ),
    }

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    print(f"FULL_REPORT={OUT}")
    return 0 if report["summary"]["final_status"].startswith("COMPLETE") else 2


if __name__ == "__main__":
    raise SystemExit(main())
