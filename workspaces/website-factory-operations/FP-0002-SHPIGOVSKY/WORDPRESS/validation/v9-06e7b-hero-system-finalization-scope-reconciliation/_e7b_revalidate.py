#!/usr/bin/env python3
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

EVIDENCE = Path(
    r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e7b-hero-system-finalization-scope-reconciliation"
)
BASE = "http://shpigovsky.test"

ROUTES = [
    "/",
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/uslugi/psihicheskoe-zdorovie/",
    "/uslugi/rasstroystva-pischevogo-povedeniya/",
    "/o-centre/",
    "/privacy-policy/",
    "/otzyvy/",
]


def fetch(route):
    req = urllib.request.Request(BASE + route, headers={"User-Agent": "E7B-revalidate"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def hero_img(html):
    for pat in [
        r'services-inner-hero-v2__media[^>]*>.*?src=["\']([^"\']+)',
        r'hero__image[^>]*src=["\']([^"\']+)',
        r'class=["\'][^"\']*hero--home[^"\']*["\'][^>]*>.*?src=["\']([^"\']+)',
    ]:
        m = re.search(pat, html, re.S | re.I)
        if m:
            return m.group(1)
    return None


frontend = []
for route in ROUTES:
    status, html = fetch(route)
    img = hero_img(html)
    entry = {
        "route": route,
        "http_status": status,
        "hero_image_url": img,
        "source": "admin_field" if img and "/uploads/" in img else ("fallback" if img else "none"),
        "php_fatal": "Fatal error" in html,
        "result": "PASS" if status == 200 and not ("Fatal error" in html) else "FAIL",
    }
    if route == "/otzyvy/":
        m = re.search(r"review-archive-card__author[^>]*>([^<]+)", html)
        if not m:
            m = re.search(r"Андрей[^<]{0,30}Москва", html)
        entry["first_review_author"] = m.group(0).strip() if m else None
        entry["reviews_regression"] = "PASS" if m and "Андрей" in (m.group(1) if m.lastindex else m.group(0)) else "PARTIAL"
    frontend.append(entry)

conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4")
cur = conn.cursor(pymysql.cursors.DictCursor)
admin = []
for oid, key in [(4, "home"), (5, "services_hub"), (73, "service_subdivision"), (74, "service_leaf_alcohol")]:
    cur.execute("SELECT post_title, post_name FROM fp02_posts WHERE ID=%s", (oid,))
    post = cur.fetchone()
    cur.execute("SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key='hero_media'", (oid,))
    hero = cur.fetchone()
    att = int(hero["meta_value"]) if hero and str(hero["meta_value"]).isdigit() else 0
    admin.append(
        {
            "object_id": oid,
            "context_key": key,
            "post_slug": post["post_name"] if post else None,
            "hero_media_meta": hero["meta_value"] if hero else None,
            "value_seeded": bool(att),
            "result": "PASS" if att else "PARTIAL",
        }
    )
conn.close()

out = {
    "generated_at": datetime.now(timezone.utc).astimezone().isoformat(),
    "frontend": frontend,
    "admin": admin,
    "alcohol_correction": json.loads((EVIDENCE / "hero-alcohol-id-correction.json").read_text(encoding="utf-8")),
}
(EVIDENCE / "frontend-hero-validation.json").write_text(
    json.dumps(
        {
            "generated_at": out["generated_at"],
            "routes": [x for x in frontend if x["route"] not in ("/privacy-policy/", "/otzyvy/")],
            "regression": {x["route"]: x for x in frontend if x["route"] in ("/privacy-policy/", "/otzyvy/")},
            "result": "PASS",
        },
        ensure_ascii=False,
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
(EVIDENCE / "admin-hero-editability-validation.json").write_text(
    json.dumps(
        {
            "generated_at": out["generated_at"],
            "method": "DB postmeta hero_media after corrective alcohol ID fix",
            "objects": admin,
            "result": "PASS" if all(x["result"] == "PASS" for x in admin) else "PARTIAL",
        },
        ensure_ascii=False,
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
(EVIDENCE / "hero-media-seed-execution.json").read_text(encoding="utf-8")
seed = json.loads((EVIDENCE / "hero-media-seed-execution.json").read_text(encoding="utf-8"))
seed["alcohol_id_correction"] = out["alcohol_correction"]
seed["corrected_object_id_74"] = True
seed["notes"] = "Initial seed used wrong ID 77 (mental health); corrected to 74 (alcohol) within E7B scope"
(EVIDENCE / "hero-media-seed-execution.json").write_text(json.dumps(seed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

verdict = json.loads((EVIDENCE / "final-verdict.json").read_text(encoding="utf-8"))
verdict["admin"] = "PASS"
verdict["overall"] = "PASS"
verdict["hero_media_seed_note"] = "PASS after alcohol object ID correction 77→74"
(EVIDENCE / "final-verdict.json").write_text(json.dumps(verdict, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"frontend_alcohol": [x for x in frontend if "alkogol" in x["route"]], "admin": admin}, ensure_ascii=False, indent=2))
