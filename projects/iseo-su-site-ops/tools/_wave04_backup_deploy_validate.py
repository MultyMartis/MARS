#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 04: local QA + scoped backup + SFTP deploy + live validation."""
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
STATIC = SRC / "static-html"
SEO_DIR = STATIC / "services" / "seo"
HUB_LOCAL = STATIC / "services" / "seo.html"
SITEMAP_LOCAL = SRC / "sitemaps" / "sitemap-static.xml"
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_niche-pages-wave-04")
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
OUT = ROOT / "tools" / "_wave04_deploy_validate.json"
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
SITE = "https://i-seo.su"

# Import page metadata from build script
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "wave04_build", ROOT / "tools" / "_wave04_build_niche_pages.py"
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
PAGES = _mod.PAGES

HUB_LABELS = [
    "SEO продвижение сайта питомника",
    "SEO продвижение сайта СМИ",
    "SEO продвижение сайта ресторана",
    "SEO продвижение Интернет-магазина запчастей",
    "SEO продвижение сайта интернет-провайдера",
    "SEO продвижение Интернет-магазина косметики",
    "SEO продвижение Интернет-магазина цветов",
]

SMOKE = [
    f"{SITE}/",
    f"{SITE}/services/seo.html",
    f"{SITE}/services/seo/prodvizhenie-avtomobilnogo-sajta.html",
    f"{SITE}/services/seo/b-regionakh.html",
    f"{SITE}/services/seo/prodvizhenie-v-ssha.html",
    f"{SITE}/services/seo/prodvizhenie-v-oae.html",
    f"{SITE}/tariff-calc",
    f"{SITE}/sitemap.xml",
    f"{SITE}/sitemap-static.xml",
]

SOFT_HYPHEN = "\u00ad"
NBSP = "\xa0"


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
        username=secrets["ftp_or_sftp_username"], password=secrets["ftp_or_sftp_password"]
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


def http_get(url: str) -> tuple[int, bytes, dict]:
    req = urllib.request.Request(url, headers={"User-Agent": "ISEO-SU-NICHE-PAGES-WAVE-04/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return resp.status, resp.read(), headers
    except urllib.error.HTTPError as e:
        return e.code, e.read() if e.fp else b"", {}


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
    return re.sub(r"<[^>]+>", "", m.group(1)).replace(NBSP, " ").replace("&nbsp;", " ").strip()


def breadcrumb_last(html: str) -> str:
    m = re.search(
        r'<ul class="breadcrumbs">.*?<li><a href="/services/seo\.html">SEO-Продвижение</a></li>\s*<li>(.*?)</li>',
        html,
        re.I | re.S,
    )
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def intro_ok(html: str, intro: str) -> bool:
    # intro is first paragraph after h1 in page body
    return intro[:80] in html and intro[-60:] in html


def niche_nav_links(html: str) -> list[tuple[str, str]]:
    m = re.search(
        r'class="more_landing_pages__navigations"[^>]*>(.*?)</(?:div|ul|nav)>',
        html,
        re.I | re.S,
    )
    if not m:
        # fallback: count all niche hrefs under more_landing_pages
        m = re.search(r"more_landing_pages__navigations(.*?)more_landing_pages__", html, re.S)
    block = m.group(1) if m else ""
    out = []
    for href, label in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.S):
        text = re.sub(r"<[^>]+>", "", label).replace(NBSP, " ").strip()
        out.append((href, text))
    return out


def sitemap_locs(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [el.text.strip() for el in root.findall(".//sm:loc", ns) if el.text]


def local_qa() -> dict:
    bad: list[str] = []
    pages = []
    for page in PAGES:
        path = SEO_DIR / page["file"]
        html = path.read_text(encoding="utf-8")
        row = {
            "file": page["file"],
            "title_ok": extract_title(html) == page["title"],
            "desc_ok": extract_meta(html, "description") == page["description"],
            "h1_ok": extract_h1(html) == page["h1"],
            "intro_ok": intro_ok(html, page["intro"]),
            "bc_ok": breadcrumb_last(html) == page["breadcrumb_last"],
            "canonical_ok": extract_canonical(html) == page["url"],
            "no_auto_bc": "автомобильного сайта</li>" not in html,
            "soft_hyphen": SOFT_HYPHEN in page["file"] or SOFT_HYPHEN in html[:500],
            "pitomnik_maltipoo": ("maltipoo-honey-club" in html) if page["replace_case"] else True,
            "pitomnik_no_drive": (
                ("driveavenue" not in html.lower() and "Drive Avenue" not in html and "Drive&nbsp;Avenue" not in html)
                if page["replace_case"]
                else True
            ),
            "other_keeps_drive": (
                True
                if page["replace_case"]
                else ("driveavenue" in html.lower() or "Drive" in html)
            ),
            "other_no_maltipoo": (
                True if page["replace_case"] else ("maltipoo" not in html.lower())
            ),
        }
        ok = all(
            [
                row["title_ok"],
                row["desc_ok"],
                row["h1_ok"],
                row["intro_ok"],
                row["bc_ok"],
                row["canonical_ok"],
                row["no_auto_bc"],
                not row["soft_hyphen"],
                row["pitomnik_maltipoo"],
                row["pitomnik_no_drive"],
                row["other_keeps_drive"],
                row["other_no_maltipoo"],
            ]
        )
        row["PASS"] = ok
        if not ok:
            bad.append(page["file"])
        pages.append(row)

    hub = HUB_LOCAL.read_text(encoding="utf-8")
    hub_norm = hub.replace("&nbsp;", " ").replace(NBSP, " ")
    links = niche_nav_links(hub)
    m_nav = re.search(r"more_landing_pages__navigations([\s\S]{0,30000}?)</div>", hub, re.I)
    niche_count = len(re.findall(r"<a\s", m_nav.group(1), re.I)) if m_nav else len(links)
    # if regex failed empty, count hrefs to new files
    new_hrefs = [p["file"] for p in PAGES]
    found = {f: (f"/services/seo/{f}" in hub or f"/{f}" in hub) for f in new_hrefs}
    label_ok = {lab: lab in hub_norm for lab in HUB_LABELS}
    hub_row = {
        "niche_link_count": niche_count,
        "new_targets_present": found,
        "new_targets_ok": all(found.values()),
        "labels_ok": all(label_ok.values()),
        "labels": label_ok,
        "expected_count": 38,
        "count_ok": niche_count == 38,
    }
    if not hub_row["new_targets_ok"] or not hub_row["labels_ok"] or not hub_row["count_ok"]:
        bad.append("hub")

    sm_locs = sitemap_locs(SITEMAP_LOCAL.read_bytes())
    new_urls = [p["url"] for p in PAGES]
    sm_row = {
        "count": len(sm_locs),
        "new_present": {u: sm_locs.count(u) for u in new_urls},
        "new_ok": all(sm_locs.count(u) == 1 for u in new_urls),
        "dupes": len(sm_locs) - len(set(sm_locs)),
    }
    if not sm_row["new_ok"] or sm_row["count"] != 139 or sm_row["dupes"]:
        bad.append("sitemap_local")

    return {"pages": pages, "hub": hub_row, "sitemap": sm_row, "bad": bad, "PASS": not bad}


def validate_live_page(page: dict, html: str, status: int) -> dict:
    robots = extract_meta(html, "robots").lower()
    consent_n = html.count('name="personal_data_consent"')
    privacy_n = html.count("privacy-policy.html")
    calc_consent = 'id="personal_data_consent_calculator__FORM"' in html or (
        'id="personal_data_consent_callback__FORM_tariff_calc"' in html
    )
    tariff_consent = "personal_data_consent_callback__FORM_tariff_calc" in html
    row = {
        "url": page["url"],
        "http": status,
        "title_ok": extract_title(html) == page["title"],
        "title": extract_title(html),
        "description_ok": extract_meta(html, "description") == page["description"],
        "h1_ok": extract_h1(html) == page["h1"],
        "h1": extract_h1(html),
        "intro_ok": intro_ok(html, page["intro"]),
        "bc_ok": breadcrumb_last(html) == page["breadcrumb_last"],
        "bc": breadcrumb_last(html),
        "canonical_ok": extract_canonical(html) == page["url"],
        "canonical": extract_canonical(html),
        "indexable": status == 200 and "noindex" not in robots,
        "robots": robots,
        "consent_count": consent_n,
        "privacy_count": privacy_n,
        "consent_ok": consent_n >= 1 and privacy_n >= 1,
        "calc_consent_ok": calc_consent or tariff_consent,
        "css_ok": "css/main.css" in html,
        "js_ok": "common.js" in html,
        "case_ok": (
            ("maltipoo-honey-club" in html and "driveavenue" not in html.lower())
            if page["replace_case"]
            else ("driveavenue" in html.lower() and "maltipoo" not in html.lower())
        ),
        "auto_leak_title": "автомобильного" in extract_title(html).lower(),
        "auto_leak_h1": "автомобильного" in extract_h1(html).lower(),
        "auto_leak_bc": "автомобильного" in breadcrumb_last(html).lower(),
    }
    row["PASS"] = all(
        [
            row["http"] == 200,
            row["title_ok"],
            row["description_ok"],
            row["h1_ok"],
            row["intro_ok"],
            row["bc_ok"],
            row["canonical_ok"],
            row["indexable"],
            row["consent_ok"],
            row["calc_consent_ok"],
            row["css_ok"],
            row["js_ok"],
            row["case_ok"],
            not row["auto_leak_title"],
            not row["auto_leak_h1"],
            not row["auto_leak_bc"],
        ]
    )
    return row


def main() -> None:
    qa = local_qa()
    if not qa["PASS"]:
        OUT.write_text(json.dumps({"local_qa": qa, "final": "FAIL_LOCAL_QA"}, ensure_ascii=False, indent=2), encoding="utf-8")
        raise SystemExit(f"LOCAL QA FAIL: {qa['bad']}")

    # live hub count BEFORE deploy
    st0, hub_before_body, _ = http_get(f"{SITE}/services/seo.html")
    hub_before_html = hub_before_body.decode("utf-8", "replace")
    links_before = niche_nav_links(hub_before_html)
    # fallback count: count <a inside navigations via simpler pattern
    before_count = len(links_before)
    if before_count == 0:
        before_count = len(
            re.findall(
                r'more_landing_pages__navigations[\s\S]*?<a\s',
                hub_before_html,
                re.I,
            )
        )
        # better: count anchors between navigations open and next section
        m = re.search(
            r"more_landing_pages__navigations([\s\S]{0,20000}?)</div>",
            hub_before_html,
            re.I,
        )
        if m:
            before_count = len(re.findall(r"<a\s", m.group(1), re.I))

    st_sm0, sm0, _ = http_get(f"{SITE}/sitemap-static.xml")
    locs0 = sitemap_locs(sm0) if st_sm0 == 200 else []

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = BAK_ROOT / f"backup-{ts}"
    bak.mkdir(parents=True, exist_ok=True)
    manifest: dict = {
        "timestamp_utc": ts,
        "backup_dir": str(bak),
        "hub_links_before_live": before_count,
        "sitemap_count_before_live": len(locs0),
        "files": [],
        "creates": [],
        "deploy": [],
    }

    sftp, transport = sftp_connect()
    try:
        # backup modify targets
        for remote, label in [
            (f"{DOC}/services/seo.html", "seo.html"),
            (f"{DOC}/sitemap-static.xml", "sitemap-static.xml"),
        ]:
            data = read_remote_bytes(sftp, remote)
            if data is None:
                raise SystemExit(f"missing remote for backup: {remote}")
            dest = bak / label
            dest.write_bytes(data)
            manifest["files"].append(
                {
                    "role": "MODIFY",
                    "production": remote,
                    "backup": str(dest),
                    "sha256_before": sha256_bytes(data),
                    "bytes": len(data),
                }
            )

        for page in PAGES:
            remote = f"{DOC}/services/seo/{page['file']}"
            existing = read_remote_bytes(sftp, remote)
            if existing is not None:
                (bak / f"EXISTING-{page['file']}").write_bytes(existing)
                manifest["creates"].append(
                    {
                        "role": "UNEXPECTED_EXISTING",
                        "production": remote,
                        "sha256": sha256_bytes(existing),
                    }
                )
            else:
                manifest["creates"].append(
                    {
                        "role": "CREATE",
                        "production": remote,
                        "rollback": "DELETE exact path only",
                        "file": page["file"],
                    }
                )

        uploads = [
            (HUB_LOCAL, f"{DOC}/services/seo.html"),
            (SITEMAP_LOCAL, f"{DOC}/sitemap-static.xml"),
        ]
        for page in PAGES:
            uploads.append((SEO_DIR / page["file"], f"{DOC}/services/seo/{page['file']}"))

        for local, remote in uploads:
            data = local.read_bytes()
            # also store deployed copy in backup folder
            (bak / f"DEPLOYED-{local.name}").write_bytes(data)
            write_remote_bytes(sftp, remote, data)
            time.sleep(0.25)
            verify = read_remote_bytes(sftp, remote)
            ok = verify == data
            entry = {
                "local": str(local),
                "remote": remote,
                "sha256": sha256_bytes(data),
                "bytes": len(data),
                "verify_match": ok,
            }
            manifest["deploy"].append(entry)
            print(f"DEPLOY {local.name} verify={ok}")
            if not ok:
                raise SystemExit(f"deploy verify failed: {remote}")
    finally:
        sftp.close()
        transport.close()

    time.sleep(1.5)

    live_pages = []
    for page in PAGES:
        st, body, _ = http_get(page["url"])
        html = body.decode("utf-8", "replace")
        row = validate_live_page(page, html, st)
        live_pages.append(row)
        print(page["file"], st, "PASS" if row["PASS"] else row)

    st_h, hub_body, _ = http_get(f"{SITE}/services/seo.html")
    hub_html = hub_body.decode("utf-8", "replace")
    m = re.search(r"more_landing_pages__navigations([\s\S]{0,25000}?)</div>", hub_html, re.I)
    after_count = len(re.findall(r"<a\s", m.group(1), re.I)) if m else 0
    hub_norm_live = hub_html.replace("&nbsp;", " ").replace(NBSP, " ")
    new_ok = {
        p["file"]: (
            f"/services/seo/{p['file']}" in hub_html and p["hub_label"] in hub_norm_live
        )
        for p in PAGES
    }
    hub_live = {
        "http": st_h,
        "links_before": before_count,
        "links_after": after_count,
        "new_7": new_ok,
        "new_ok": all(new_ok.values()),
        "consent_ok": hub_html.count('name="personal_data_consent"') >= 1,
    }

    st_sm, sm_body, _ = http_get(f"{SITE}/sitemap-static.xml")
    locs = sitemap_locs(sm_body) if st_sm == 200 else []
    new_urls = [p["url"] for p in PAGES]
    sitemap_live = {
        "http": st_sm,
        "count_before": len(locs0),
        "count_after": len(locs),
        "new_present": {u: locs.count(u) for u in new_urls},
        "new_ok": all(locs.count(u) == 1 for u in new_urls),
        "duplicates": len(locs) - len(set(locs)),
    }
    st_root, root_body, _ = http_get(f"{SITE}/sitemap.xml")
    root_txt = root_body.decode("utf-8", "replace")
    sitemap_live["root_http"] = st_root
    sitemap_live["root_static"] = "sitemap-static.xml" in root_txt
    sitemap_live["root_wp"] = "wp-sitemap.xml" in root_txt

    smoke = {}
    for url in SMOKE:
        st, _, _ = http_get(url)
        smoke[url] = st
        print("SMOKE", st, url)

    pages_pass = all(r["PASS"] for r in live_pages)
    final = {
        "NICHE_PAGES_CREATED": 7,
        "NICHE_PAGE_HTTP_200": f"{sum(1 for r in live_pages if r['http']==200)}/7",
        "CONTENT_MAPPING_EXACT": "YES" if pages_pass else "NO",
        "BREADCRUMB_MAPPING_EXACT": f"{sum(1 for r in live_pages if r['bc_ok'])}/7",
        "PITOMNIK_CASE_URL": "https://i-seo.su/cases/maltipoo-honey-club.html",
        "PITOMNIK_CASE_REPLACED": next(r["case_ok"] for r in live_pages if "pitomnika" in r["url"]),
        "OTHER_6_CASE_OK": all(r["case_ok"] for r in live_pages if "pitomnika" not in r["url"]),
        "SELF_CANONICAL": f"{sum(1 for r in live_pages if r['canonical_ok'])}/7",
        "INDEXABLE": f"{sum(1 for r in live_pages if r['indexable'])}/7",
        "SERVICES_SEO_HUB_LINKS_BEFORE": before_count,
        "SERVICES_SEO_HUB_LINKS_AFTER": after_count,
        "NEW_NICHE_HUB_LINKS": f"{sum(1 for v in new_ok.values() if v)}/7",
        "FORM_CONSENT": f"{sum(1 for r in live_pages if r['consent_ok'])}/7",
        "CALC_CONSENT": f"{sum(1 for r in live_pages if r['calc_consent_ok'])}/7",
        "STATIC_SITEMAP_BEFORE": len(locs0),
        "STATIC_SITEMAP_AFTER": len(locs),
        "NEW_IN_SITEMAP": f"{sum(1 for u in new_urls if locs.count(u)==1)}/7",
        "SITEMAP_DUPES": sitemap_live["duplicates"],
        "ROOT_SITEMAP_HEALTH": st_root == 200
        and sitemap_live["root_static"]
        and sitemap_live["root_wp"],
        "SMOKE_ALL_200": all(v == 200 for v in smoke.values()),
        "pages_pass": pages_pass,
        "hub_pass": hub_live["http"] == 200 and hub_live["new_ok"] and after_count == before_count + 7,
        "sitemap_pass": (
            sitemap_live["http"] == 200
            and sitemap_live["new_ok"]
            and sitemap_live["duplicates"] == 0
            and sitemap_live["count_after"] == 139
        ),
    }
    final["PASS"] = (
        final["pages_pass"]
        and final["hub_pass"]
        and final["sitemap_pass"]
        and final["SMOKE_ALL_200"]
        and final["ROOT_SITEMAP_HEALTH"]
    )

    report = {
        "local_qa": qa,
        "manifest": manifest,
        "live_pages": live_pages,
        "hub_live": hub_live,
        "sitemap_live": sitemap_live,
        "smoke": smoke,
        "final": final,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bak / "manifest.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("FINAL", json.dumps(final, ensure_ascii=False, indent=2))
    if not final["PASS"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
