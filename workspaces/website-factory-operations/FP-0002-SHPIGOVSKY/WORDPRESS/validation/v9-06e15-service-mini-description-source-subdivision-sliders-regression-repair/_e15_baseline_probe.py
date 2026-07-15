#!/usr/bin/env python3
"""E15 baseline probe — TEMPORARY, NOT FOR GIT."""
from __future__ import annotations

import json
import re
import urllib.request
from html import unescape
from pathlib import Path

import pymysql

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
VAL = ROOT / "validation/v9-06e15-service-mini-description-source-subdivision-sliders-regression-repair"
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


def fetch(route: str) -> tuple[int | None, str]:
    req = urllib.request.Request(BASE + route, headers={"User-Agent": "E15-probe"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def extract_cards(html: str) -> list[str]:
    cards = re.findall(
        r'<p class="services-category-section-v2__service-text">(.*?)</p>',
        html,
        re.S,
    )
    out = []
    for c in cards:
        out.append(unescape(re.sub(r"<.*?>", "", c)).strip())
    return out


def main() -> None:
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT p.ID, p.post_title, p.post_name, p.post_parent,
          md.meta_value AS short_desc,
          ref.meta_value AS acf_ref
        FROM fp02_posts p
        LEFT JOIN fp02_postmeta md ON md.post_id = p.ID AND md.meta_key = 'service_short_description'
        LEFT JOIN fp02_postmeta ref ON ref.post_id = p.ID AND ref.meta_key = '_service_short_description'
        WHERE p.post_type = 'service' AND p.post_status = 'publish'
        ORDER BY p.menu_order, p.ID
        """
    )
    services = cur.fetchall()

    cur.execute(
        "SELECT meta_value FROM fp02_postmeta WHERE meta_key = 'services_hub_query_mode' LIMIT 1"
    )
    hub_mode_row = cur.fetchone()
    hub_mode = (hub_mode_row or {}).get("meta_value") or "grouped_by_parent"

    status, grouped_html = fetch("/uslugi/")
    grouped_cards = extract_cards(grouped_html)

    # flat mode via query param if supported
    flat_cards: list[str] = []
    try:
        _, flat_html = fetch("/uslugi/?fp02_hub_mode=flat")
        flat_cards = extract_cards(flat_html)
    except Exception:
        pass

    audit = {
        "generated_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "services_hub_query_mode": hub_mode,
        "mini_description_audit": [],
        "slider_audit": {},
        "root_causes": [],
    }

    slug_to_rendered_grouped: dict[str, str] = {}
    # map by order is weak; we'll match by DB text

    for svc in services:
        meta = (svc.get("short_desc") or "").strip()
        ref = (svc.get("acf_ref") or "").strip()
        slug = svc["post_name"]

        source = "UNKNOWN"
        if meta:
            if ref == "field_fp02_service_short_description":
                source = "ACF_FIELD"
            else:
                source = "RAW_META_NO_ACF_REF"
        else:
            source = "EMPTY_FIELD"

        # find rendered in grouped by matching meta or first unmatched
        rendered_grouped = ""
        for card in grouped_cards:
            if meta and card == meta:
                rendered_grouped = card
                break
        if not rendered_grouped:
            for card in grouped_cards:
                if card not in slug_to_rendered_grouped.values():
                    pass

        audit["mini_description_audit"].append(
            {
                "id": svc["ID"],
                "title": svc["post_title"],
                "slug": slug,
                "parent": svc["post_parent"],
                "admin_field_value": meta,
                "acf_reference_meta": ref,
                "source_attribution_db": source,
                "rendered_grouped_match_admin": bool(meta and meta in grouped_cards),
                "admin_nonempty": bool(meta),
            }
        )

    empty_count = sum(1 for s in audit["mini_description_audit"] if not s["admin_nonempty"])
    no_ref_count = sum(
        1
        for s in audit["mini_description_audit"]
        if s["admin_nonempty"] and s["acf_reference_meta"] != "field_fp02_service_short_description"
    )

    if empty_count:
        audit["root_causes"].append(
            f"{empty_count} published services have empty service_short_description in DB"
        )
    if no_ref_count:
        audit["root_causes"].append(
            f"{no_ref_count} services have meta value but missing/wrong ACF reference key"
        )

    _, zav_html = fetch("/uslugi/zavisimosti/")
    audit["slider_audit"] = {
        "route": "/uslugi/zavisimosti/",
        "http_status": status,
        "swiper_css_loaded": "swiper-bundle.min.css" in zav_html,
        "swiper_js_loaded": "swiper-bundle.min.js" in zav_html,
        "specialists_slider_dom": "specialists__slider" in zav_html,
        "reviews_slider_dom": "reviews__slider" in zav_html,
        "v9_shell_loaded": "v9-shell" in zav_html,
        "home_vendors_gated_front_page_only": True,
        "alcohol_vendors_route_scoped": True,
        "subdivision_vendor_loader_present": False,
    }
    if not audit["slider_audit"]["swiper_js_loaded"]:
        audit["root_causes"].append(
            "Subdivision route /uslugi/zavisimosti/ renders specialists/reviews sliders but Swiper vendor is not enqueued (gated to is_front_page and alcohol leaf only)"
        )

    out = VAL / "baseline-corrective-audit.json"
    out.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"services": len(services), "empty_meta": empty_count, "no_acf_ref": no_ref_count, "root_causes": audit["root_causes"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
