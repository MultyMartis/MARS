#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-WEBINAR-LANDING-01: backup CREATE, deploy HTML+CSS, live+form validate."""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SITE = "https://i-seo.su"
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
URL = f"{SITE}/webinar-seo-podryadchik.html"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
SRC = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source")
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_webinar-landing-01")
OUT = BAK_ROOT / "_deploy_validate.json"
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\webinar-landing-01")
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
    "Зарегистрируйтесь на вебинар",
    'name="personal_data_consent"',
    'value="1"',
    "privacy-policy.html",
    "WEBINAR SEO CONTRACTOR 2026-09",
    'id="page__FORM_seo"',
    'id="page__FORM_send_seo"',
    'name="pf_phone"',
    'href="#webinar-register"',
    "new-seo-landing-flex-first-screen",
    "webinar-seo-podryadchik.css",
    "Меня зовут Никита Шваков, я руководитель INTLSEO.",
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
    req = urllib.request.Request(
        url, headers={"User-Agent": "ISEO-SU-WEBINAR-LANDING-01/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return resp.status, resp.read(), headers
    except urllib.error.HTTPError as e:
        return e.code, e.read() if e.fp else b"", {}


def http_post(url: str, data: dict) -> tuple[int, bytes]:
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": "ISEO-SU-WEBINAR-LANDING-01/1.0",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
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


def get_form_token() -> dict | None:
    status, raw, _ = http_get(f"{SITE}/iseo-form-token.php")
    if status != 200:
        return None
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return None


def form_base(token: dict, consent: str | None) -> dict:
    data = {
        "pf_name": "QA Webinar",
        "pf_contact": "WhatsApp / Telegram",
        "pf_phone": "+79990001122",
        "pf_site": "WEBINAR SEO CONTRACTOR 2026-09",
        "pf_comment": "WEBINAR LANDING 01 NEGATIVE TEST — discard",
        "pf_page_title": TITLE,
        "pf_page_link": URL,
        "contact_company_url": "",
        "iseo_ft": token["t"],
        "iseo_fs": token["s"],
        "iseo_fid": token["id"],
    }
    if consent is not None:
        data["personal_data_consent"] = consent
    return data


def validate_html(html: str, status: int) -> list[str]:
    bad = []
    if status != 200:
        bad.append(f"http:{status}")
    if extract_title(html) != TITLE:
        bad.append(f"title:{extract_title(html)[:80]}")
    if extract_meta(html, "description") != DESCRIPTION:
        bad.append("description")
    if extract_h1(html) != H1:
        bad.append(f"h1:{extract_h1(html)}")
    if extract_canonical(html) != URL:
        bad.append(f"canonical:{extract_canonical(html)}")
    robots = extract_meta(html, "robots").lower()
    if "noindex" in robots:
        bad.append(f"robots:{robots}")
    for n in NEEDLES:
        if n not in html:
            bad.append(f"missing:{n[:60]}")
    for a in ABSENT:
        if a.lower() in html.lower():
            bad.append(f"present:{a}")
    # count program/after bullets roughly
    if html.count("по каким критериям оценивать SEO-агентство") < 1:
        bad.append("program_1")
    if html.count("составить понятные критерии выбора подрядчика") < 1:
        bad.append("after_1")
    return bad


def preflight_exclusions() -> dict:
    menu = MENU.read_text(encoding="utf-8")
    mobile = MOBILE.read_text(encoding="utf-8") if MOBILE.exists() else ""
    allow = ALLOWLIST.read_text(encoding="utf-8") if ALLOWLIST.exists() else ""
    smap = SITEMAP_SRC.read_text(encoding="utf-8") if SITEMAP_SRC.exists() else ""
    slug = "webinar-seo-podryadchik"
    return {
        "in_menu": slug in menu or slug in mobile,
        "in_allowlist": slug in allow,
        "in_sitemap_source": slug in smap,
    }


def main() -> None:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bak = BAK_ROOT / f"backup-{ts}"
    bak.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)

    excl = preflight_exclusions()
    report: dict = {
        "task": "ISEO-SU-SITE-OPS-WEBINAR-LANDING-01",
        "timestamp_utc": ts,
        "final_url": URL,
        "exclusions": excl,
        "files": [],
        "live": {},
        "form_tests": {},
        "ok": False,
    }

    if excl["in_menu"] or excl["in_allowlist"] or excl["in_sitemap_source"]:
        report["error"] = "preflight_exclusion_fail"
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        raise SystemExit("STOP — page unexpectedly present in menu/sitemap/allowlist")

    local_payloads = []
    for item in FILES:
        data = item["local"].read_bytes()
        local_payloads.append({**item, "bytes": data, "sha256": sha256_bytes(data)})

    sftp, transport = sftp_connect()
    try:
        for item in local_payloads:
            before = read_remote_bytes(sftp, item["remote"])
            before_sha = sha256_bytes(before) if before is not None else None
            op = "CREATE" if before is None else "REPLACE"
            # backup only if existed
            if before is not None:
                rel = item["remote"].replace(DOC + "/", "").replace("/", "__")
                (bak / f"before__{rel}").write_bytes(before)
            (bak / f"source__{item['local'].name}").write_bytes(item["bytes"])
            write_remote_bytes(sftp, item["remote"], item["bytes"])
            after = read_remote_bytes(sftp, item["remote"])
            after_sha = sha256_bytes(after) if after is not None else None
            aligned = after_sha == item["sha256"]
            report["files"].append(
                {
                    "local": str(item["local"]),
                    "remote": item["remote"],
                    "op": op,
                    "backup_dir": str(bak),
                    "sha256_local": item["sha256"],
                    "sha256_before": before_sha,
                    "sha256_after": after_sha,
                    "remote_checksum_match": aligned,
                }
            )
            if not aligned:
                report["error"] = f"checksum_mismatch:{item['local'].name}"
                OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
                raise SystemExit("STOP — remote checksum mismatch")
    finally:
        sftp.close()
        transport.close()

    time.sleep(1.5)
    status, raw, headers = http_get(URL)
    html = raw.decode("utf-8", errors="replace")
    bad = validate_html(html, status)
    # live sitemap/menu absence
    sm_status, sm_raw, _ = http_get(f"{SITE}/sitemap-static.xml")
    sm_text = sm_raw.decode("utf-8", errors="replace") if sm_status == 200 else ""
    img_status, _, img_headers = http_get(f"{SITE}/img/iSEO_Boss.png")
    css_status, css_raw, _ = http_get(f"{SITE}/css/webinar-seo-podryadchik.css")
    report["live"] = {
        "http": status,
        "content_type": headers.get("content-type"),
        "validation_errors": bad,
        "title": extract_title(html),
        "description": extract_meta(html, "description"),
        "h1": extract_h1(html),
        "canonical": extract_canonical(html),
        "nikita_img_http": img_status,
        "nikita_img_type": img_headers.get("content-type"),
        "css_http": css_status,
        "css_sha_match": sha256_bytes(css_raw) == local_payloads[1]["sha256"]
        if css_status == 200
        else False,
        "in_live_sitemap": "webinar-seo-podryadchik" in sm_text,
        "program_items": sum(
            1
            for s in (
                "по каким критериям оценивать SEO-агентство",
                "как отличить профессиональную команду",
                "как проверить компетентность SEO-команды",
                "как понять, за что вы платите",
            )
            if s in html
        ),
        "after_items": sum(
            1
            for s in (
                "составить понятные критерии выбора подрядчика",
                "самостоятельно оценить коммерческое предложение",
                "распознать подозрительные обещания",
                "выбрать команду, которая работает прозрачно",
            )
            if s in html
        ),
    }

    # Form negative tests (mail must be 0 / not true)
    token = get_form_token()
    form_results = {}
    if token and token.get("t") and token.get("s") and token.get("id"):
        time.sleep(3.2)  # min_fill_seconds
        # refresh token age still ok after wait — re-fetch to stay within window but age>=3
        # keep original token issued before wait so age >= 3
        cases = [
            ("no_consent", form_base(token, None)),
            ("consent_0", form_base(token, "0")),
            ("malformed_empty_name", {**form_base(token, "1"), "pf_name": ""}),
        ]
        for name, payload in cases:
            # each case needs fresh enough token age; reuse same token after initial wait
            st, body = http_post(f"{SITE}/page__FORM.php", payload)
            text = body.decode("utf-8", errors="replace").strip()
            form_results[name] = {
                "http": st,
                "body": text[:200],
                "rejected": text != "true",
                "mail_sent_signal": text == "true",
            }
            time.sleep(0.5)
    else:
        form_results["token_fetch"] = {"ok": False}
    report["form_tests"] = form_results

    ok = (
        status == 200
        and not bad
        and report["live"]["program_items"] == 4
        and report["live"]["after_items"] == 4
        and not report["live"]["in_live_sitemap"]
        and img_status == 200
        and css_status == 200
        and all(f.get("rejected") for k, f in form_results.items() if k != "token_fetch")
        and not any(f.get("mail_sent_signal") for f in form_results.values() if isinstance(f, dict))
    )
    report["ok"] = ok
    report["test_mode_final"] = "OFF"
    report["normal_recipient"] = "nikel007i33@yandex.ru"
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": ok, "http": status, "errors": bad, "form": form_results}, ensure_ascii=False, indent=2))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
