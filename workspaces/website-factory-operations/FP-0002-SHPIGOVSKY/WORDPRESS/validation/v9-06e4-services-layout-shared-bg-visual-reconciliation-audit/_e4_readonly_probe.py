#!/usr/bin/env python3
"""TEMPORARY E4 read-only probe — NOT FOR GIT."""
import hashlib
import json
import os
import re
import urllib.error
import urllib.request

import pymysql

BASE = "http://shpigovsky.test"
ROUTES = ["/uslugi/", "/uslugi/zavisimosti/"]
THEME_RUNTIME = r"X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky"
THEME_GIT = r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\theme\shpigovsky"
STATIC_V9_SRC = r"X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\src"
STATIC_V9_DIST = r"X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\dist"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "E4-audit-probe"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except Exception as exc:
        return 0, str(exc)


def head(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "E4-audit-probe"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:
        return 0


def sha256_file(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def first_match(pattern, html):
    match = re.search(pattern, html, re.I | re.S)
    return match.group(1) if match else None


conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="mars_wp_fp0002",
    charset="utf8mb4",
)
cur = conn.cursor(pymysql.cursors.DictCursor)

out = {"routes": {}, "assets": {}, "css_url_checks": {}}

for route in ROUTES:
    status, payload = fetch(BASE + route)
    html = payload if isinstance(payload, str) and payload.startswith("<") else ""
    error = None if html else payload

    post_id = None
    post_type = None
    template = None
    hero_meta = []
    hero_media = None

    if route == "/uslugi/":
        cur.execute(
            "SELECT ID, post_title, post_name, post_status, post_type "
            "FROM fp02_posts WHERE post_name='uslugi' AND post_type='page' LIMIT 1"
        )
        row = cur.fetchone()
        if row:
            post_id = row["ID"]
            post_type = row["post_type"]
            cur.execute(
                "SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key='_wp_page_template'",
                (post_id,),
            )
            t = cur.fetchone()
            template = t["meta_value"] if t else None
    else:
        cur.execute(
            "SELECT p.ID, p.post_title, p.post_name, p.post_status, p.post_type, pm.meta_value AS template "
            "FROM fp02_posts p "
            "LEFT JOIN fp02_postmeta pm ON p.ID=pm.post_id AND pm.meta_key='_wp_page_template' "
            "WHERE p.post_name='zavisimosti' AND p.post_type IN ('page','service') "
            "ORDER BY FIELD(p.post_type,'service','page')"
        )
        rows = cur.fetchall()
        for row in rows:
            if row["post_type"] == "service":
                post_id = row["ID"]
                post_type = row["post_type"]
                template = row["template"]
                break
        if not post_id and rows:
            post_id = rows[0]["ID"]
            post_type = rows[0]["post_type"]
            template = rows[0]["template"]
        if post_id:
            cur.execute(
                "SELECT meta_key, meta_value FROM fp02_postmeta "
                "WHERE post_id=%s AND meta_key LIKE %s",
                (post_id, "%hero%"),
            )
            hero_meta = cur.fetchall()
            if function_exists := True:
                cur.execute(
                    "SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key='hero_media'",
                    (post_id,),
                )
                hero_media_row = cur.fetchone()
                hero_media = hero_media_row["meta_value"] if hero_media_row else None

    section_classes = re.findall(r"<section[^>]*class=\"([^\"]+)\"", html)
    out["routes"][route] = {
        "http_status": status,
        "error": error,
        "post_id": post_id,
        "post_type": post_type,
        "template": template,
        "body_class": first_match(r"<body[^>]*class=\"([^\"]*)\"", html),
        "main_class": first_match(r"<main[^>]*class=\"([^\"]*)\"", html),
        "hero_section_classes": [c for c in section_classes if "hero" in c.lower()][:5],
        "services_inner_hero_present": "services-inner-hero-v2" in html,
        "hero_inner_present": "hero hero--inner" in html or "hero--inner" in html,
        "hero_image_url": first_match(r'class="services-inner-hero-v2__image"[^>]*src="([^"]+)"', html),
        "has_final_form_band": "final-form__band" in html,
        "has_program_cta_band": "program-cta-band" in html,
        "has_service_subdivision_start": "service-subdivision-start" in html,
        "has_home_rehab_cta_band": "home-rehabilitation-requirements__cta-band" in html,
        "hero_meta": hero_meta,
        "hero_media_meta": hero_media,
        "section_order_sample": section_classes[:12],
    }

asset_paths = [
    "assets/img/content/home-final-form/home-final-form-background.webp",
    "assets/img/content/services/services-hero.webp",
    "assets/img/content/services/service-subdivision-hero.webp",
]

for rel in asset_paths:
    runtime = os.path.join(THEME_RUNTIME, rel.replace("/", os.sep))
    git = os.path.join(THEME_GIT, rel.replace("/", os.sep))
    static_src = os.path.join(STATIC_V9_SRC, rel.replace("/", os.sep))
    static_dist = os.path.join(STATIC_V9_DIST, rel.replace("/", os.sep))
    entry = {
        "static_src_path": static_src,
        "static_dist_path": static_dist,
        "wp_git_theme_path": git,
        "runtime_theme_path": runtime,
        "exists_static_src": os.path.isfile(static_src),
        "exists_static_dist": os.path.isfile(static_dist),
        "exists_git_theme": os.path.isfile(git),
        "exists_runtime_theme": os.path.isfile(runtime),
        "url_root": BASE + "/" + rel,
        "url_root_status": head(BASE + "/" + rel),
        "url_theme": BASE + "/wp-content/themes/shpigovsky/" + rel,
        "url_theme_status": head(BASE + "/wp-content/themes/shpigovsky/" + rel),
    }
    for key, path in [
        ("static_src_sha256", static_src),
        ("static_dist_sha256", static_dist),
        ("git_theme_sha256", git),
        ("runtime_theme_sha256", runtime),
    ]:
        if os.path.isfile(path):
            entry[key] = sha256_file(path)
    out["assets"][rel] = entry

css_bg = "/assets/img/content/home-final-form/home-final-form-background.webp"
out["css_url_checks"][BASE + css_bg] = head(BASE + css_bg)

conn.close()
print(json.dumps(out, ensure_ascii=False, indent=2))
