# -*- coding: utf-8 -*-
"""WAVE 02: backup, deploy city pages + hub + sitemap, live validation."""
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
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_city-pages-wave-02")
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_wave02_deploy_validate.json")
FORENSIC_HUB = BAK_ROOT / "_forensic" / "b-regionakh.html"

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
        "intro_needle": "Санкт-Петербург входит в число самых конкурентных регионов",
        "main_title": "SEO продвижение сайта в Санкт-Петербурге",
    },
    "prodvizhenie-v-kazani.html": {
        "title": "SEO-продвижение сайта компании в Казани | i-seo.su",
        "h1": "SEO-продвижение сайта в Казани",
        "description": "Продвижение сайтов в Казани под ключ. Аудит, оптимизация и рост позиций в Яндексе и Google. Работаем с бизнесом Татарстана любого масштаба.",
        "faq4": "Широкий запрос «купить недвижимость в Казани» высококонкурентный, тогда как более узкий запрос с указанием района или типа объекта выводится в топ быстрее.",
        "intro_needle": "Казань закрепилась как один из растущих IT-центров",
        "main_title": "SEO продвижение сайта в Казани",
    },
    "prodvizhenie-v-ekaterinburge.html": {
        "title": "SEO-продвижение сайта компании в Екатеринбурге | i-seo.su",
        "h1": "SEO-продвижение сайта в Екатеринбурге",
        "description": "Комплексное SEO-продвижение сайтов в Екатеринбурге. Выводим бизнес в топ поисковой выдачи, увеличиваем трафик и заявки с сайта.",
        "faq4": "Запрос «купить недвижимость в Екатеринбурге» занят крупными федеральными агрегаторами, а более узкий запрос с уточнением по району продвинуть проще и быстрее.",
        "intro_needle": "Екатеринбург остается крупнейшим логистическим",
        "main_title": "SEO продвижение сайта в Екатеринбурге",
    },
    "prodvizhenie-v-novosibirske.html": {
        "title": "SEO-продвижение сайта компании в Новосибирске | i-seo.su",
        "h1": "SEO-продвижение сайта в Новосибирске",
        "description": "Продвигаем сайты бизнеса в Новосибирске. Аудит, стратегия, рост позиций и трафика. Опыт в разных нишах, прозрачная отчетность на каждом этапе.",
        "faq4": "Запрос «купить недвижимость в Новосибирске» высококонкурентный по всему городу, а более узкий запрос с уточнением по району продвигается значительно легче.",
        "intro_needle": "Новосибирск остается крупным научным и IT-центром",
        "main_title": "SEO продвижение сайта в Новосибирске",
    },
    "prodvizhenie-v-krasnoyarske.html": {
        "title": "SEO-продвижение сайта компании в Красноярске | i-seo.su",
        "h1": "SEO-продвижение сайта в Красноярске",
        "description": "SEO-продвижение сайтов в Красноярске под ключ. Бесплатный аудит, работа над позициями и трафиком, отчетность на каждом этапе сотрудничества.",
        "faq4": "Широкий запрос «купить недвижимость в Красноярске» перегружен конкурентами, а более узкий запрос с уточнением по району продвигается заметно быстрее.",
        "intro_needle": "Красноярск остается промышленным центром Сибири",
        "main_title": "SEO продвижение сайта в Красноярске",
    },
}

SMOKE = [
    f"{SITE}/",
    f"{SITE}/services.html",
    f"{SITE}/services/seo.html",
    f"{SITE}/services/seo/b-regionakh.html",
    f"{SITE}/services/seo/zarubezhnye.html",
    f"{SITE}/tariff-calc",
    f"{SITE}/blog/",
    f"{SITE}/glossary/",
    f"{SITE}/sitemap.xml",
    f"{SITE}/sitemap-static.xml",
]


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
    req = urllib.request.Request(url, headers={"User-Agent": "ISEO-SU-CITY-PAGES-WAVE-02/1.0"})
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
    return re.sub(r"<[^>]+>", "", m.group(1)).replace("\xa0", " ").strip()


def main() -> None:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = BAK_ROOT / f"backup-{ts}"
    bak.mkdir(parents=True, exist_ok=True)
    manifest = {
        "timestamp_utc": ts,
        "backup_dir": str(bak),
        "files": [],
        "creates": [],
        "deploy": [],
        "pages": {},
        "hub": {},
        "sitemap": {},
        "smoke": {},
        "consent": {},
        "final": {},
    }

    sftp, transport = sftp_connect()
    try:
        # --- BACKUP ---
        hub_remote = f"{DOC}/services/seo/b-regionakh.html"
        sm_remote = f"{DOC}/sitemap-static.xml"
        for remote, label in [(hub_remote, "b-regionakh.html"), (sm_remote, "sitemap-static.xml")]:
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
                    "sha256": sha256_bytes(data),
                    "bytes": len(data),
                }
            )
            print(f"BACKUP {label} sha256={sha256_bytes(data)}")

        # also keep forensic original hub if present
        if FORENSIC_HUB.exists():
            manifest["forensic_hub_sha256"] = sha256_bytes(FORENSIC_HUB.read_bytes())

        for slug in CITY_SLUGS:
            remote = f"{DOC}/services/seo/{slug}"
            existing = read_remote_bytes(sftp, remote)
            if existing is not None:
                dest = bak / f"EXISTING-{slug}"
                dest.write_bytes(existing)
                manifest["files"].append(
                    {
                        "role": "UNEXPECTED_EXISTING",
                        "production": remote,
                        "backup": str(dest),
                        "sha256": sha256_bytes(existing),
                        "bytes": len(existing),
                    }
                )
                print(f"WARN existing remote {slug}")
            else:
                manifest["creates"].append(
                    {
                        "role": "CREATE",
                        "production": remote,
                        "rollback": "DELETE exact path only",
                        "slug": slug,
                    }
                )
                print(f"CREATE planned {slug}")

        # --- DEPLOY ---
        uploads = [
            (SRC / "static-html/services/seo/b-regionakh.html", hub_remote),
            (SRC / "sitemaps/sitemap-static.xml", sm_remote),
        ]
        for slug in CITY_SLUGS:
            uploads.append((SRC / f"static-html/services/seo/{slug}", f"{DOC}/services/seo/{slug}"))

        for local, remote in uploads:
            data = local.read_bytes()
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
            print(f"DEPLOY {local.name} verify={ok} sha256={sha256_bytes(data)}")
            if not ok:
                raise SystemExit(f"deploy verify failed: {remote}")
    finally:
        sftp.close()
        transport.close()

    time.sleep(1.5)

    # --- LIVE PAGE VALIDATION ---
    hub_back = "https://i-seo.su/services/seo/b-regionakh.html"
    pages_ok = True
    for slug, meta in CITY_META.items():
        url = f"{SITE}/services/seo/{slug}"
        status, body, _ = http_get(url)
        html = body.decode("utf-8", "replace")
        robots = extract_meta(html, "robots").lower()
        canon = extract_canonical(html)
        title = extract_title(html)
        desc = extract_meta(html, "description")
        h1 = extract_h1(html)
        consent_n = html.count('name="personal_data_consent"')
        privacy_n = html.count("/privacy-policy.html")
        calc_has = 'id="callback__FORM_tariff_calc"' in html
        calc_consent_field = 'id="personal_data_consent_callback__FORM_tariff_calc"' in html
        row = {
            "url": url,
            "http": status,
            "title_ok": title == meta["title"],
            "title": title,
            "description_ok": desc == meta["description"],
            "h1_ok": h1 == meta["h1"],
            "h1": h1,
            "intro_ok": meta["intro_needle"] in html,
            "main_title_ok": meta["main_title"] in html,
            "faq4_ok": meta["faq4"] in html,
            "canonical": canon,
            "canonical_ok": canon == url,
            "indexable": status == 200
            and "noindex" not in robots
            and ("index" in robots or robots == ""),
            "robots": robots,
            "hub_backlink": hub_back in html,
            "consent_count": consent_n,
            "privacy_count": privacy_n,
            "consent_ok": consent_n >= 1 and privacy_n >= 1,
            "calc_present": calc_has,
            "calc_consent_ok": (not calc_has) or calc_consent_field,
        }
        ok = (
            row["http"] == 200
            and row["title_ok"]
            and row["description_ok"]
            and row["h1_ok"]
            and row["intro_ok"]
            and row["main_title_ok"]
            and row["faq4_ok"]
            and row["canonical_ok"]
            and row["indexable"]
            and row["hub_backlink"]
            and row["consent_ok"]
            and row["calc_consent_ok"]
        )
        row["PASS"] = ok
        pages_ok = pages_ok and ok
        manifest["pages"][slug] = row
        print(
            f"PAGE {slug} http={status} pass={ok} consent={consent_n} canon={canon == url}"
        )

    # --- HUB ---
    st, body, _ = http_get(f"{SITE}/services/seo/b-regionakh.html")
    hub_html = body.decode("utf-8", "replace")
    hub_links = {slug: f"{SITE}/services/seo/{slug}" in hub_html for slug in CITY_SLUGS}
    hub_block = "Выберите ваш город" in hub_html and 'id="city-seo-pages"' in hub_html
    hub_consent = hub_html.count('name="personal_data_consent"')
    manifest["hub"] = {
        "http": st,
        "city_block": hub_block,
        "links": hub_links,
        "links_ok": all(hub_links.values()),
        "consent_count": hub_consent,
        "consent_ok": hub_consent >= 1,
    }
    print(
        f"HUB http={st} block={hub_block} links={sum(hub_links.values())}/5 consent={hub_consent}"
    )

    # --- SITEMAP ---
    st, body, _ = http_get(f"{SITE}/sitemap-static.xml")
    xml_text = body.decode("utf-8", "replace")
    locs = []
    try:
        root = ET.fromstring(body)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [el.text.strip() for el in root.findall("sm:url/sm:loc", ns) if el.text]
        xml_ok = True
    except ET.ParseError as e:
        xml_ok = False
        manifest["sitemap"]["parse_error"] = str(e)
    city_urls = [f"{SITE}/services/seo/{s}" for s in CITY_SLUGS]
    city_in = {u: locs.count(u) for u in city_urls}
    dupes = len(locs) - len(set(locs))
    manifest["sitemap"] = {
        "http": st,
        "xml_valid": xml_ok,
        "url_count": len(locs),
        "city_in_sitemap": city_in,
        "city_present_5": all(city_in[u] == 1 for u in city_urls),
        "duplicates": dupes,
    }
    # root sitemap
    st2, body2, _ = http_get(f"{SITE}/sitemap.xml")
    root_txt = body2.decode("utf-8", "replace")
    manifest["sitemap"]["root_http"] = st2
    manifest["sitemap"]["root_points_static"] = "sitemap-static.xml" in root_txt
    manifest["sitemap"]["root_points_wp"] = "wp-sitemap.xml" in root_txt
    # robots
    st3, body3, _ = http_get(f"{SITE}/robots.txt")
    robots_txt = body3.decode("utf-8", "replace")
    manifest["sitemap"]["robots_http"] = st3
    manifest["sitemap"]["robots_sitemap"] = "Sitemap:" in robots_txt and "sitemap.xml" in robots_txt
    print(
        f"SITEMAP http={st} count={len(locs)} cities={sum(1 for v in city_in.values() if v==1)}/5 dupes={dupes}"
    )

    # --- SMOKE ---
    for url in SMOKE:
        st, _, _ = http_get(url)
        manifest["smoke"][url] = st
        print(f"SMOKE {st} {url}")

    # consent summary
    consent_pages = sum(1 for r in manifest["pages"].values() if r.get("consent_ok"))
    manifest["consent"] = {
        "city_pages_covered": f"{consent_pages}/5",
        "hub_consent_ok": manifest["hub"].get("consent_ok"),
        "calc_consent_covered": all(r.get("calc_consent_ok") for r in manifest["pages"].values()),
    }

    manifest["final"] = {
        "CITY_PAGES_CREATED": 5,
        "pages_pass": pages_ok,
        "hub_pass": manifest["hub"]["http"] == 200
        and manifest["hub"]["city_block"]
        and manifest["hub"]["links_ok"],
        "sitemap_pass": manifest["sitemap"]["http"] == 200
        and manifest["sitemap"]["xml_valid"]
        and manifest["sitemap"]["city_present_5"]
        and manifest["sitemap"]["duplicates"] == 0,
        "STATIC_SITEMAP_URL_COUNT_AFTER": manifest["sitemap"]["url_count"],
    }

    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (bak / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("WROTE", OUT)
    print("FINAL", json.dumps(manifest["final"], ensure_ascii=False))


if __name__ == "__main__":
    main()
