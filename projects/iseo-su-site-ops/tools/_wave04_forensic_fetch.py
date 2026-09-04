#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 04: fetch automotive source + seo hub + verify Maltipoo case."""
from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
SRC_DIR = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\static-html")
FORENSIC = Path(r"X:\AI MARS\local\sites\iseo-su-production\_niche-pages-wave-04\_forensic")
REPORT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_wave04_forensic_report.json")
SITE = "https://i-seo.su"

REMOTE_FILES = {
    "source": ("services/seo/prodvizhenie-avtomobilnogo-sajta.html", SRC_DIR / "services" / "seo" / "prodvizhenie-avtomobilnogo-sajta.html"),
    "hub": ("services/seo.html", SRC_DIR / "services" / "seo.html"),
}


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def http_get(url: str, timeout: int = 45) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-ISEO-WAVE04/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() if e.fp else b""


def sftp_connect():
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"], password=secrets["ftp_or_sftp_password"]
    )
    return paramiko.SFTPClient.from_transport(transport), transport


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main() -> None:
    FORENSIC.mkdir(parents=True, exist_ok=True)
    sftp, transport = sftp_connect()
    fetched = {}
    for key, (rel, out_path) in REMOTE_FILES.items():
        remote = f"{DOC}/{rel}"
        with sftp.open(remote, "r") as f:
            raw = f.read()
        if not isinstance(raw, (bytes, bytearray)):
            raw = bytes(raw)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(raw)
        (FORENSIC / Path(rel).name).write_bytes(raw)
        fetched[key] = {
            "remote": remote,
            "local": str(out_path),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
        }
    sftp.close()
    transport.close()

    source = (SRC_DIR / "services" / "seo" / "prodvizhenie-avtomobilnogo-sajta.html").read_text(
        encoding="utf-8", errors="replace"
    )
    hub = (SRC_DIR / "services" / "seo.html").read_text(encoding="utf-8", errors="replace")

    title = re.search(r"<title>(.*?)</title>", source, re.I | re.S)
    desc = re.search(r'name=["\']description["\']\s+content=["\'](.*?)["\']', source, re.I | re.S)
    if not desc:
        desc = re.search(r'content=["\'](.*?)["\']\s+name=["\']description["\']', source, re.I | re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", source, re.I | re.S)
    robots = re.search(r'name=["\']robots["\']\s+content=["\'](.*?)["\']', source, re.I)
    canon = re.search(r'rel=["\']canonical["\']\s+href=["\'](.*?)["\']', source, re.I)
    if not canon:
        canon = re.search(r'href=["\'](.*?)["\']\s+rel=["\']canonical["\']', source, re.I)

    # intro: first span after h1 (city/niche pattern)
    intro_m = re.search(r"</h1>\s*(<span>.*?</span>)", source, re.I | re.S)
    # breadcrumbs last li / last crumb text
    crumbs = re.findall(r'class=["\'][^"\']*breadcrumb[^"\']*["\'][^>]*>.*?</(?:nav|ol|ul|div)>', source, re.I | re.S)
    crumb_items = re.findall(
        r'<li[^>]*>\s*(?:<a[^>]*>)?(.*?)(?:</a>)?\s*</li>',
        source,
        re.I | re.S,
    )
    # also schema breadcrumb
    crumb_schema = re.findall(r'"name"\s*:\s*"([^"]+)"', source)

    drive = "Drive" in source or "drive-avenue" in source.lower() or "Drive Avenue" in source
    consent = "personal_data_consent" in source
    privacy = "privacy-policy.html" in source
    calc = "tarif-calc" in source.lower() or "tariff" in source.lower()

    # hub niche links under services/seo/
    niche_hrefs = re.findall(
        r'href=["\'](?:https://i-seo\.su)?(/services/seo/[^"\']+\.html)["\']',
        hub,
        re.I,
    )
    niche_unique = sorted(set(niche_hrefs))
    # tab items pattern - look for list of niche promo links
    niche_labels = re.findall(
        r'href=["\'](?:https://i-seo\.su)?/services/seo/([^"\']+\.html)["\'][^>]*>(.*?)</a>',
        hub,
        re.I | re.S,
    )

    # case live
    case_url = f"{SITE}/cases/maltipoo-honey-club.html"
    st, body = http_get(case_url)
    case_html = body.decode("utf-8", errors="replace")
    case_title = re.search(r"<title>(.*?)</title>", case_html, re.I | re.S)
    case_ok = st == 200 and ("maltipoo" in case_html.lower() or "Maltipoo" in case_html)

    # extract case block snippet from source for later replacement reference
    cases_block = None
    m = re.search(r'<div class="our_cases">.*?</div>\s*</div>\s*</div>', source, re.I | re.S)
    if m:
        cases_block = m.group(0)[:2500]

    report = {
        "fetched": fetched,
        "source": {
            "title": title.group(1).strip() if title else None,
            "description": desc.group(1).strip() if desc else None,
            "h1_raw": h1.group(1).strip() if h1 else None,
            "h1_text": strip_tags(h1.group(1)) if h1 else None,
            "intro_raw": intro_m.group(1) if intro_m else None,
            "intro_text": strip_tags(intro_m.group(1)) if intro_m else None,
            "robots": robots.group(1) if robots else None,
            "canonical": canon.group(1) if canon else None,
            "consent": consent,
            "privacy": privacy,
            "calc_markers": calc,
            "drive_avenue_present": drive,
            "crumb_li_count": len(crumb_items),
            "crumb_last_raw": crumb_items[-1] if crumb_items else None,
            "crumb_last_text": strip_tags(crumb_items[-1]) if crumb_items else None,
            "crumb_schema_names_tail": crumb_schema[-5:] if crumb_schema else [],
            "cases_block_preview": cases_block,
        },
        "hub": {
            "niche_href_total_matches": len(niche_hrefs),
            "niche_href_unique": len(niche_unique),
            "niche_unique_sample": niche_unique[:15],
            "niche_label_pairs": [
                {"href": h, "label": strip_tags(lab)} for h, lab in niche_labels[:40]
            ],
            "niche_label_count": len(niche_labels),
        },
        "pitomnik_case": {
            "url": case_url,
            "http": st,
            "title": case_title.group(1).strip() if case_title else None,
            "valid": case_ok,
        },
        "stop": not case_ok,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": not report["stop"], "report": str(REPORT), "case_valid": case_ok, "hub_niche_unique": len(niche_unique)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
