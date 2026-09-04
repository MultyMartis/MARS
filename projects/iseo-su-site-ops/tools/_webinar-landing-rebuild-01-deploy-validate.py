#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-WEBINAR-LANDING-REBUILD-01: deploy HTML+tiny CSS, live validate."""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SITE = "https://i-seo.su"
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
URL = f"{SITE}/webinar-seo-podryadchik.html"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
SRC = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source")
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_webinar-landing-rebuild-01")
OUT = BAK_ROOT / "_deploy_validate.json"
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\webinar-landing-rebuild-01")
MENU = SRC / "theme" / "iseoblog" / "template-parts" / "content-topbar.php"
MOBILE = SRC / "theme" / "iseoblog" / "template-parts" / "content-mobilemenu.php"
SITEMAP_SRC = SRC / "sitemaps" / "sitemap-static.xml"
ALLOWLIST = SRC.parent / "data" / "sitemaps" / "sitemap-static-urls-v1.txt"

FILES = [
    {
        "local": SRC / "static-html" / "webinar-seo-podryadchik.html",
        "remote": f"{DOC}/webinar-seo-podryadchik.html",
        "kind": "html",
    },
    {
        "local": SRC / "css" / "webinar-seo-podryadchik.css",
        "remote": f"{DOC}/css/webinar-seo-podryadchik.css",
        "kind": "css",
    },
]

TITLE = "Вебинар «Как выбрать подрядчика в SEO и не ошибиться?» | INTLSEO"
DESCRIPTION = (
    "Бесплатный вебинар Никиты Швакова о выборе SEO-подрядчика. "
    "3 сентября 2026 в 19:00 МСК. Разберем критерии выбора агентства, риски и реальные результаты SEO."
)
H1 = "Как выбрать подрядчика в SEO и не ошибиться?"

NEEDLES = [
    "Вебинар",
    "недобросовестный",
    "/img/iSEO_Boss.png",
    "3 сентября 2026",
    "19:00 МСК",
    "Участие бесплатное",
    "На вебинаре разберем",
    "После вебинара вы сможете",
    "Записаться на вебинар",
    'name="personal_data_consent"',
    'value="1"',
    "privacy-policy.html",
    "WEBINAR SEO CONTRACTOR 2026-09",
    'id="page__FORM_seo"',
    'id="page__FORM_send_seo"',
    'name="pf_contact"',
    'href="#webinar-register"',
    "new-seo-landing-flex-first-screen",
    "content_block__title",
    "uni_check_list",
    "free_audit",
    "webinar-seo-podryadchik.css",
    "Меня зовут Никита Шваков, я руководитель INTLSEO.",
    # Live PHP expands includes — use rendered markers (not include filenames)
    "main_navigations",
    "footer_menu",
    "footer_bottom",
]

# Rejected custom design markers that must NOT dominate
ABSENT_REJECTED = [
    "webinar-hero__",
    "webinar-section__",
    "webinar-register__grid",
    "webinar-facts__item",
]

ABSENT = ["lorem ipsum", "Lorem Ipsum", "noindex", "TODO", "FIXME"]


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


def write_remote_bytes(sftp, path: str, data: bytes) -> None:
    with sftp.open(path, "w") as f:
        f.write(data)


def http_get(url: str) -> tuple[int, bytes, dict]:
    req = urllib.request.Request(
        url, headers={"User-Agent": "ISEO-SU-WEBINAR-LANDING-REBUILD-01/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.status, resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read() if e.fp else b"", dict(e.headers or {})


def check_menu_sitemap() -> dict:
    menu_hit = False
    for p in (MENU, MOBILE):
        if p.exists() and "webinar-seo-podryadchik" in p.read_text(encoding="utf-8", errors="ignore"):
            menu_hit = True
    sm_hit = False
    if SITEMAP_SRC.exists() and "webinar-seo-podryadchik" in SITEMAP_SRC.read_text(
        encoding="utf-8", errors="ignore"
    ):
        sm_hit = True
    if ALLOWLIST.exists() and "webinar-seo-podryadchik" in ALLOWLIST.read_text(
        encoding="utf-8", errors="ignore"
    ):
        sm_hit = True
    return {"menu": menu_hit, "sitemap": sm_hit}


def main() -> int:
    BAK_ROOT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()
    report: dict = {"task": "WEBINAR-LANDING-REBUILD-01", "ts": ts, "url": URL}

    # CSS line count
    css_text = (SRC / "css" / "webinar-seo-podryadchik.css").read_text(encoding="utf-8")
    css_lines = len([ln for ln in css_text.splitlines() if ln.strip() and not ln.strip().startswith("/*") and "*/" not in ln.strip()[:3]])
    report["css_total_lines"] = len(css_text.splitlines())
    report["css_nonempty_approx"] = css_lines
    report["large_custom_css_remains"] = report["css_total_lines"] > 120

    sftp, transport = sftp_connect()
    deployed = []
    try:
        for item in FILES:
            local_bytes = item["local"].read_bytes()
            write_remote_bytes(sftp, item["remote"], local_bytes)
            deployed.append(
                {
                    "kind": item["kind"],
                    "remote": item["remote"],
                    "sha256": sha256_bytes(local_bytes),
                    "bytes": len(local_bytes),
                }
            )
            print(f"DEPLOYED {item['kind']}: {item['remote']} ({len(local_bytes)} bytes)")
    finally:
        sftp.close()
        transport.close()

    report["deployed"] = deployed
    time.sleep(2)

    status, body, headers = http_get(URL)
    text = body.decode("utf-8", errors="replace")
    report["http"] = status
    report["content_length"] = len(body)
    report["live_sha256"] = sha256_bytes(body)

    missing = [n for n in NEEDLES if n not in text]
    rejected_present = [n for n in ABSENT_REJECTED if n in text]
    bad = [n for n in ABSENT if n.lower() in text.lower()]
    report["needles_missing"] = missing
    report["rejected_markers_present"] = rejected_present
    report["absent_hits"] = bad

    title_ok = TITLE in text
    desc_ok = DESCRIPTION in text
    h1_ok = f"<h1>{H1}</h1>" in text or H1 in text
    canon_ok = 'rel="canonical" href="https://i-seo.su/webinar-seo-podryadchik.html"' in text
    report["meta"] = {
        "title": title_ok,
        "description": desc_ok,
        "h1": h1_ok,
        "canonical": canon_ok,
    }

    ms = check_menu_sitemap()
    report["menu"] = "YES" if ms["menu"] else "NO"
    report["sitemap"] = "YES" if ms["sitemap"] else "NO"

    # Asset check
    boss_status, _, _ = http_get(f"{SITE}/img/iSEO_Boss.png")
    report["nikita_asset_http"] = boss_status

    ok = (
        status == 200
        and not missing
        and not rejected_present
        and not bad
        and title_ok
        and desc_ok
        and h1_ok
        and canon_ok
        and report["menu"] == "NO"
        and report["sitemap"] == "NO"
        and not report["large_custom_css_remains"]
        and boss_status == 200
    )
    report["pass"] = ok
    report["status"] = (
        "COMPLETE — WEBINAR LANDING REBUILT ON EXISTING I-SEO SITE DESIGN / CUSTOM DESIGN REMOVED / RSYA READY"
        if ok
        else "INCOMPLETE — FIX VALIDATION GAPS"
    )

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (EVIDENCE / "deploy-validate.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
