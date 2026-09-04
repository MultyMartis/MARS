# -*- coding: utf-8 -*-
"""WAVE 02A: backup 5 city pages, deploy source→production, live validate cross-nav."""
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

SITE = "https://i-seo.su"
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
SRC = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source")
BAK_ROOT = Path(
    r"X:\AI MARS\local\sites\iseo-su-production\_city-pages-wave-02a-cross-linking"
)
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_wave02a_deploy_validate.json")

CITY_SLUGS = [
    "prodvizhenie-v-sankt-peterburge.html",
    "prodvizhenie-v-kazani.html",
    "prodvizhenie-v-ekaterinburge.html",
    "prodvizhenie-v-novosibirske.html",
    "prodvizhenie-v-krasnoyarske.html",
]

CITY_META = {
    "prodvizhenie-v-sankt-peterburge.html": {
        "title": "SEO-продвижение сайта компании в Санкт-Петербурге | i-seo.su",
        "h1": "SEO-продвижение сайта в Санкт-Петербурге",
        "description": "Продвигаем сайты компаний Санкт-Петербурга в топ Яндекса и Google. Бесплатный аудит, прозрачные тарифы, рост позиций и трафика за 3 месяца.",
        "faq4": "Общий запрос «купить недвижимость в Санкт-Петербурге» высококонкурентный, а более узкий запрос с указанием конкретного района или типа объекта продвинуть значительно проще.",
        "current_label": "Санкт-Петербург",
    },
    "prodvizhenie-v-kazani.html": {
        "title": "SEO-продвижение сайта компании в Казани | i-seo.su",
        "h1": "SEO-продвижение сайта в Казани",
        "description": "Продвижение сайтов в Казани под ключ. Аудит, оптимизация и рост позиций в Яндексе и Google. Работаем с бизнесом Татарстана любого масштаба.",
        "faq4": "Широкий запрос «купить недвижимость в Казани» высококонкурентный, тогда как более узкий запрос с указанием района или типа объекта выводится в топ быстрее.",
        "current_label": "Казань",
    },
    "prodvizhenie-v-ekaterinburge.html": {
        "title": "SEO-продвижение сайта компании в Екатеринбурге | i-seo.su",
        "h1": "SEO-продвижение сайта в Екатеринбурге",
        "description": "Комплексное SEO-продвижение сайтов в Екатеринбурге. Выводим бизнес в топ поисковой выдачи, увеличиваем трафик и заявки с сайта.",
        "faq4": "Запрос «купить недвижимость в Екатеринбурге» занят крупными федеральными агрегаторами, а более узкий запрос с уточнением по району продвинуть проще и быстрее.",
        "current_label": "Екатеринбург",
    },
    "prodvizhenie-v-novosibirske.html": {
        "title": "SEO-продвижение сайта компании в Новосибирске | i-seo.su",
        "h1": "SEO-продвижение сайта в Новосибирске",
        "description": "Продвигаем сайты бизнеса в Новосибирске. Аудит, стратегия, рост позиций и трафика. Опыт в разных нишах, прозрачная отчетность на каждом этапе.",
        "faq4": "Запрос «купить недвижимость в Новосибирске» высококонкурентный по всему городу, а более узкий запрос с уточнением по району продвигается значительно легче.",
        "current_label": "Новосибирск",
    },
    "prodvizhenie-v-krasnoyarske.html": {
        "title": "SEO-продвижение сайта компании в Красноярске | i-seo.su",
        "h1": "SEO-продвижение сайта в Красноярске",
        "description": "SEO-продвижение сайтов в Красноярске под ключ. Бесплатный аудит, работа над позициями и трафиком, отчетность на каждом этапе сотрудничества.",
        "faq4": "Широкий запрос «купить недвижимость в Красноярске» перегружен конкурентами, а более узкий запрос с уточнением по району продвигается заметно быстрее.",
        "current_label": "Красноярск",
    },
}

ALL_CITY_URLS = [f"{SITE}/services/seo/{s}" for s in CITY_SLUGS]
HUB_URL = f"{SITE}/services/seo/b-regionakh.html"
NAV_TITLE = "Продвижение сайтов в других городах"


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


def http_get(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(
        url, headers={"User-Agent": "ISEO-SU-CITY-PAGES-WAVE-02A/1.0"}
    )
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
    return re.sub(r"<[^>]+>", "", m.group(1)).replace("\xa0", " ").strip()


def extract_nav_block(html: str) -> str | None:
    # Block is followed by the same <!-- --- --> separator used elsewhere.
    m = re.search(
        r'<div[^>]+id=["\']city-seo-cross-nav["\'][^>]*>.*?</div>\s*<!-- --- -->',
        html,
        re.I | re.S,
    )
    return m.group(0) if m else None


def sitemap_url_count(xml_bytes: bytes) -> int:
    root = ET.fromstring(xml_bytes)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = root.findall("sm:url", ns)
    if not urls:
        urls = root.findall("url")
    return len(urls)


def main() -> None:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = BAK_ROOT / f"backup-{ts}"
    bak.mkdir(parents=True, exist_ok=True)
    manifest: dict = {
        "timestamp_utc": ts,
        "backup_dir": str(bak),
        "files": [],
        "deploy": [],
        "pages": {},
        "hub": {},
        "sitemap": {},
        "smoke": {},
        "final": {},
    }

    sftp, transport = sftp_connect()
    try:
        for slug in CITY_SLUGS:
            remote = f"{DOC}/services/seo/{slug}"
            data = read_remote_bytes(sftp, remote)
            if data is None:
                raise SystemExit(f"missing remote for backup: {remote}")
            dest = bak / slug
            dest.write_bytes(data)
            entry = {
                "role": "MODIFY",
                "production": remote,
                "backup": str(dest),
                "sha256_before": sha256_bytes(data),
                "bytes": len(data),
            }
            manifest["files"].append(entry)
            print(f"BACKUP {slug} sha256={entry['sha256_before']}")

        for slug in CITY_SLUGS:
            local = SRC / f"static-html/services/seo/{slug}"
            remote = f"{DOC}/services/seo/{slug}"
            data = local.read_bytes()
            if b'id="city-seo-cross-nav"' not in data and b"id='city-seo-cross-nav'" not in data:
                raise SystemExit(f"source missing nav block: {local}")
            write_remote_bytes(sftp, remote, data)
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
            print(f"DEPLOY {slug} verify={ok} sha256={entry['sha256']}")
            if not ok:
                raise SystemExit(f"deploy verify failed: {remote}")
    finally:
        sftp.close()
        transport.close()

    time.sleep(1.5)

    pages_ok = True
    cross_targets_ok = 0
    for slug, meta in CITY_META.items():
        url = f"{SITE}/services/seo/{slug}"
        status, body = http_get(url)
        html = body.decode("utf-8", "replace")
        nav = extract_nav_block(html)
        hrefs = re.findall(r'<a\s+href=["\']([^"\']+)["\']', nav or "", re.I)
        current_spans = re.findall(
            r'aria-current=["\']page["\'][^>]*>([^<]+)</span>', nav or "", re.I
        )
        if not current_spans:
            current_spans = re.findall(
                r'class=["\'][^"\']*city-seo-cross-nav__current[^"\']*["\'][^>]*>([^<]+)</span>',
                nav or "",
                re.I,
            )
        expected_outbound = [u for u in ALL_CITY_URLS if u != url]
        outbound_ok = sorted(hrefs) == sorted(expected_outbound)
        nofollow = "nofollow" in (nav or "").lower()
        target_blank = 'target="_blank"' in (nav or "").lower() or "target='_blank'" in (
            nav or ""
        ).lower()

        # validate each outbound target HTTP 200
        target_http = {}
        for turl in expected_outbound:
            st, _ = http_get(turl)
            target_http[turl] = st
            if st == 200:
                cross_targets_ok += 1

        consent_n = html.count('name="personal_data_consent"')
        privacy_n = html.count("/privacy-policy.html")
        calc_has = 'id="callback__FORM_tariff_calc"' in html
        calc_consent_field = 'id="personal_data_consent_callback__FORM_tariff_calc"' in html

        row = {
            "url": url,
            "http": status,
            "nav_present": nav is not None,
            "nav_title_ok": NAV_TITLE in (nav or ""),
            "outbound_links": hrefs,
            "outbound_count": len(hrefs),
            "outbound_ok": outbound_ok and len(hrefs) == 4,
            "current_labels": current_spans,
            "current_ok": len(current_spans) == 1
            and current_spans[0].strip() == meta["current_label"],
            "nofollow": nofollow,
            "target_blank": target_blank,
            "target_http": target_http,
            "targets_200": all(v == 200 for v in target_http.values()),
            "title_ok": extract_title(html) == meta["title"],
            "title": extract_title(html),
            "description_ok": extract_meta(html, "description") == meta["description"],
            "h1_ok": extract_h1(html) == meta["h1"],
            "h1": extract_h1(html),
            "faq4_ok": meta["faq4"] in html,
            "canonical": extract_canonical(html),
            "canonical_ok": extract_canonical(html) == url,
            "hub_backlink": HUB_URL in html,
            "consent_count": consent_n,
            "privacy_count": privacy_n,
            "consent_ok": consent_n >= 1 and privacy_n >= 1,
            "calc_present": calc_has,
            "calc_consent_ok": (not calc_has) or calc_consent_field,
        }
        ok = (
            row["http"] == 200
            and row["nav_present"]
            and row["nav_title_ok"]
            and row["outbound_ok"]
            and row["current_ok"]
            and not row["nofollow"]
            and not row["target_blank"]
            and row["targets_200"]
            and row["title_ok"]
            and row["description_ok"]
            and row["h1_ok"]
            and row["faq4_ok"]
            and row["canonical_ok"]
            and row["hub_backlink"]
            and row["consent_ok"]
            and row["calc_consent_ok"]
        )
        row["ok"] = ok
        pages_ok = pages_ok and ok
        manifest["pages"][slug] = row
        print(
            f"PAGE {slug} http={status} nav={row['nav_present']} "
            f"out={row['outbound_count']} current={row['current_ok']} ok={ok}"
        )

    # Hub → city links
    hub_status, hub_body = http_get(HUB_URL)
    hub_html = hub_body.decode("utf-8", "replace")
    hub_city_links = sum(1 for u in ALL_CITY_URLS if u in hub_html)
    hub_has_nav = 'id="city-seo-cross-nav"' in hub_html
    manifest["hub"] = {
        "url": HUB_URL,
        "http": hub_status,
        "city_links": hub_city_links,
        "city_links_ok": hub_city_links == 5,
        "cross_nav_absent": not hub_has_nav,
    }
    print(
        f"HUB http={hub_status} city_links={hub_city_links} "
        f"cross_nav_absent={not hub_has_nav}"
    )

    # Sitemap verify only
    sm_status, sm_body = http_get(f"{SITE}/sitemap-static.xml")
    sm_count = sitemap_url_count(sm_body) if sm_status == 200 else -1
    # spot-check 5 city URLs present
    sm_text = sm_body.decode("utf-8", "replace")
    sm_cities = sum(1 for u in ALL_CITY_URLS if u in sm_text)
    manifest["sitemap"] = {
        "http": sm_status,
        "url_count": sm_count,
        "url_count_ok": sm_count == 132,
        "city_urls_present": sm_cities,
        "changed": False,
    }
    print(f"SITEMAP http={sm_status} count={sm_count} cities={sm_cities}")

    smoke_urls = [
        HUB_URL,
        *ALL_CITY_URLS,
        f"{SITE}/sitemap-static.xml",
    ]
    for u in smoke_urls:
        st, _ = http_get(u)
        manifest["smoke"][u] = st
        print(f"SMOKE {u} -> {st}")

    smoke_ok = all(v == 200 for v in manifest["smoke"].values())
    final_ok = (
        pages_ok
        and manifest["hub"]["http"] == 200
        and manifest["hub"]["city_links_ok"]
        and manifest["sitemap"]["url_count_ok"]
        and smoke_ok
        and cross_targets_ok == 20
    )
    manifest["final"] = {
        "CITY_PAGES_CHECKED": 5,
        "CITY_NAV_BLOCK_ADDED": pages_ok,
        "CITY_NAV_BLOCK_PAGES": "5/5" if pages_ok else "FAIL",
        "CURRENT_CITY_STATE": "DISTINCT / NON-LINKED",
        "CROSS_CITY_LINKS_PER_PAGE": 4,
        "CROSS_CITY_TARGETS_VALID": f"{cross_targets_ok}/20",
        "CITY_CITY_CONNECTIVITY": "PASS" if pages_ok else "FAIL",
        "CITY_HUB_BACKLINK": "5/5"
        if all(p.get("hub_backlink") for p in manifest["pages"].values())
        else "FAIL",
        "HUB_CITY_LINKS": "5/5" if manifest["hub"]["city_links_ok"] else "FAIL",
        "TITLE_CHANGED": "NO",
        "DESCRIPTION_CHANGED": "NO",
        "H1_CHANGED": "NO",
        "FAQ_CHANGED": "NO",
        "CANONICAL_CHANGED": "NO",
        "SITEMAP_CHANGED": "NO",
        "STATIC_SITEMAP_URL_COUNT": sm_count,
        "ok": final_ok,
    }
    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"WROTE {OUT}")
    print(f"FINAL_OK={final_ok}")
    if not final_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
