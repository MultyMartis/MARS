#!/usr/bin/env python3
"""E15 detailed render vs admin probe — TEMPORARY, NOT FOR GIT."""
from __future__ import annotations

import json
import re
import urllib.request
from html import unescape
from pathlib import Path

import pymysql

BASE = "http://shpigovsky.test"


def db_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mars_wp_fp0002",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def fetch(route: str) -> str:
    req = urllib.request.Request(BASE + route, headers={"User-Agent": "E15-detail"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def extract_service_blocks(html: str) -> list[dict]:
    blocks = []
    pattern = re.compile(
        r'<article class="services-category-section-v2__service[^"]*">.*?'
        r'<h3 class="services-category-section-v2__service-name">(.*?)</h3>.*?'
        r'<p class="services-category-section-v2__service-text">(.*?)</p>',
        re.S,
    )
    for m in pattern.finditer(html):
        title = unescape(re.sub(r"<.*?>", "", m.group(1))).strip()
        text = unescape(re.sub(r"<.*?>", "", m.group(2))).strip()
        blocks.append({"title": title, "text": text})
    return blocks


def main() -> None:
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT p.ID, p.post_title, p.post_name,
          md.meta_value AS short_desc,
          ref.meta_value AS acf_ref
        FROM fp02_posts p
        LEFT JOIN fp02_postmeta md ON md.post_id = p.ID AND md.meta_key = 'service_short_description'
        LEFT JOIN fp02_postmeta ref ON ref.post_id = p.ID AND ref.meta_key = '_service_short_description'
        WHERE p.post_type = 'service' AND p.post_status = 'publish'
        ORDER BY p.menu_order, p.ID
        """
    )
    services = {r["post_title"]: r for r in cur.fetchall()}
    # also by V9 title aliases
    title_map = {}
    for r in cur.fetchall():
        title_map[r["post_title"]] = r

    html = fetch("/uslugi/")
    blocks = extract_service_blocks(html)
    rows = []
    for b in blocks:
        svc = services.get(b["title"])
        if not svc:
            # try partial match
            for t, s in services.items():
                if b["title"] in t or t in b["title"]:
                    svc = s
                    break
        admin = (svc or {}).get("short_desc", "").strip() if svc else ""
        rendered = b["text"]
        if admin and rendered == admin:
            src = "ACF_FIELD"
            ok = True
        elif admin and rendered != admin:
            src = "MISMATCH_ADMIN_VS_RENDERED"
            ok = False
        elif not admin:
            src = "NO_ADMIN_VALUE"
            ok = False
        else:
            src = "UNKNOWN"
            ok = False
        rows.append(
            {
                "rendered_title": b["title"],
                "service_id": (svc or {}).get("ID"),
                "service_slug": (svc or {}).get("post_name"),
                "admin_value": admin[:120] + ("..." if len(admin) > 120 else ""),
                "rendered_text": rendered[:120] + ("..." if len(rendered) > 120 else ""),
                "source": src,
                "result": "PASS" if ok else "FAIL",
            }
        )
    print(json.dumps(rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
