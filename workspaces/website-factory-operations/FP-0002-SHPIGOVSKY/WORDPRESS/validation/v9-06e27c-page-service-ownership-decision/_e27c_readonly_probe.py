#!/usr/bin/env python3
"""TEMPORARY E27C read-only probe — NOT FOR GIT COMMIT."""
from __future__ import annotations

import hashlib
import json
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

BASE = "http://shpigovsky.test"
PREFIX = "fp02_"
DB = "mars_wp_fp0002"
DB_USER = "mli_shpigovsky_app"
DB_PASS = "9st4UPjdkc5MXyuNKEGTQaS0V7AD1ClR"
OUT = Path(__file__).resolve().parent
MANIFEST = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/tools/v9-route-manifest.json")
TASK_ID = "V9-06E27C"
NOW = datetime.now(timezone.utc).isoformat()

ROUTES = [
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/uslugi/zavisimosti/profilakticheskiy-analiz/",
    "/uslugi/zavisimosti/specialistam/",
    "/uslugi/zavisimosti/lekarstvennaya-zavisimost/",
    "/uslugi/zavisimosti/narkoticheskaya-zavisimost/",
    "/uslugi/zavisimosti/povedencheskie-zavisimosti/",
    "/uslugi/psihicheskoe-zdorovie/",
    "/uslugi/rasstroystva-pischevogo-povedeniya/",
]

PAGE_IDS = [6, 7, 8]
SERVICE_ROOT_IDS = [73, 77, 84]


def fetch(route: str) -> tuple[int, str, str]:
    url = BASE.rstrip("/") + route
    try:
        with urllib.request.urlopen(url, timeout=25) as resp:
            return resp.status, resp.geturl(), resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return exc.code, url, body


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def h1(body: str) -> str | None:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.I | re.S)
    return strip_html(m.group(1)) if m else None


def body_class(body: str) -> str | None:
    m = re.search(r'<body[^>]*class="([^"]*)"', body, re.I)
    return m.group(1) if m else None


def detect_wp_object(body: str) -> dict:
    bc = body_class(body) or ""
    out: dict = {"body_class": bc}
    for pat, key in [
        (r"\bpage-id-(\d+)\b", "page_id"),
        (r"\bpostid-(\d+)\b", "post_id"),
        (r"\bsingle-service\b", "is_single_service"),
        (r"\bpage-template-[\w-]+\b", "page_template_class"),
        (r"\bpage-uslugi-v2\b", "has_page_uslugi_v2"),
        (r"\bservice-subdivision\b", "has_service_subdivision"),
        (r"\bservice-leaf\b", "has_service_leaf"),
        (r"\bservices-hub\b", "has_services_hub"),
    ]:
        m = re.search(pat, bc)
        if m:
            out[key] = m.group(1) if m.lastindex else True
    canon = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', body, re.I)
    if canon:
        out["canonical_url"] = canon.group(1)
    return out


def build_page_path(cur, post_name: str, parent_id: int) -> str:
    chain: list[str] = []
    parent = parent_id
    while parent:
        cur.execute(f"SELECT post_name, post_parent FROM {PREFIX}posts WHERE ID=%s", (parent,))
        row = cur.fetchone()
        if not row:
            break
        chain.insert(0, row["post_name"])
        parent = row["post_parent"]
    parts = [p for p in chain + [post_name] if p]
    return "/" + "/".join(parts) + "/" if parts else "/"


def build_service_path(cur, post_name: str, parent_id: int) -> str:
    chain: list[str] = []
    parent = parent_id
    while parent:
        cur.execute(f"SELECT post_name, post_parent FROM {PREFIX}posts WHERE ID=%s", (parent,))
        row = cur.fetchone()
        if not row:
            break
        chain.insert(0, row["post_name"])
        parent = row["post_parent"]
    parts = [p for p in chain + [post_name] if p]
    return "/uslugi/" + "/".join(parts) + "/" if parts else "/uslugi/"


def content_class(content: str, template: str | None) -> str:
    text = (content or "").strip()
    if len(text) < 50:
        return "skeleton_or_empty"
    if "placeholder" in text.lower() or "skeleton" in text.lower() or "demo" in text.lower():
        return "placeholder"
    return "full_or_template_managed"


def acf_fields(cur, post_id: int) -> list[dict]:
    cur.execute(
        f"""
        SELECT pm.meta_key, LEFT(pm.meta_value, 200) AS meta_value
        FROM {PREFIX}postmeta pm
        WHERE pm.post_id=%s AND pm.meta_key NOT LIKE '\\_%%' ESCAPE '\\\\'
        ORDER BY pm.meta_key
        LIMIT 50
        """,
        (post_id,),
    )
    return [{"key": r["meta_key"], "preview": r["meta_value"]} for r in cur.fetchall()]


def object_inventory(cur) -> list[dict]:
    ids = PAGE_IDS + SERVICE_ROOT_IDS
    cur.execute(
        f"""
        SELECT p.ID, p.post_title, p.post_name, p.post_status, p.post_parent,
               p.post_type, p.menu_order, p.post_modified, p.post_excerpt,
               LENGTH(p.post_content) AS content_len, p.post_content,
               pm.meta_value AS page_template
        FROM {PREFIX}posts p
        LEFT JOIN {PREFIX}postmeta pm ON p.ID=pm.post_id AND pm.meta_key='_wp_page_template'
        WHERE p.ID IN ({",".join(str(i) for i in ids)})
        """
    )
    rows = []
    for row in cur.fetchall():
        pid = row["ID"]
        if row["post_type"] == "page":
            path = build_page_path(cur, row["post_name"], row["post_parent"])
        else:
            path = build_service_path(cur, row["post_name"], row["post_parent"])
        cur.execute(f"SELECT COUNT(*) AS c FROM {PREFIX}postmeta WHERE post_id=%s", (pid,))
        meta_count = cur.fetchone()["c"]
        cur.execute(
            f"SELECT COUNT(*) AS c FROM {PREFIX}postmeta WHERE post_id=%s AND meta_key LIKE 'field_%%'",
            (pid,),
        )
        acf_ref_count = cur.fetchone()["c"]
        fields = acf_fields(cur, pid)
        cur.execute(
            f"""
            SELECT pmi.ID AS menu_item_id, t.name AS menu_name, t.slug AS menu_slug,
                   pmi.menu_order,
                   (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_object_id') AS object_id,
                   (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_object') AS object_type,
                   (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_url') AS item_url,
                   (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_menu_item_parent') AS parent_item
            FROM {PREFIX}posts pmi
            JOIN {PREFIX}postmeta mobj ON pmi.ID=mobj.post_id AND mobj.meta_key='_menu_item_object_id' AND mobj.meta_value=%s
            JOIN {PREFIX}term_relationships tr ON pmi.ID=tr.object_id
            JOIN {PREFIX}term_taxonomy tt ON tr.term_taxonomy_id=tt.term_taxonomy_id AND tt.taxonomy='nav_menu'
            JOIN {PREFIX}terms t ON tt.term_id=t.term_id
            WHERE pmi.post_type='nav_menu_item'
            """,
            (str(pid),),
        )
        menu_refs = cur.fetchall()
        children = []
        if row["post_type"] == "service":
            cur.execute(
                f"SELECT ID, post_title, post_name, post_status FROM {PREFIX}posts "
                f"WHERE post_type='service' AND post_parent=%s AND post_status='publish' ORDER BY menu_order, ID",
                (pid,),
            )
            for ch in cur.fetchall():
                children.append(
                    {
                        "id": ch["ID"],
                        "title": ch["post_title"],
                        "slug": ch["post_name"],
                        "path": build_service_path(cur, ch["post_name"], pid),
                    }
                )
        rows.append(
            {
                "id": pid,
                "type": row["post_type"],
                "title": row["post_title"],
                "slug": row["post_name"],
                "path": path,
                "status": row["post_status"],
                "parent_id": row["post_parent"],
                "menu_order": row["menu_order"],
                "modified": str(row["post_modified"]),
                "content_len": row["content_len"],
                "excerpt_len": len((row["post_excerpt"] or "").strip()),
                "page_template": row["page_template"] or "default",
                "content_class": content_class(row["post_content"], row["page_template"]),
                "meta_count": meta_count,
                "acf_field_ref_count": acf_ref_count,
                "key_acf_fields": [f["key"] for f in fields[:15]],
                "acf_field_preview": fields[:8],
                "menu_references": menu_refs,
                "service_children": children,
            }
        )
    return rows


def menu_audit(cur, route_owners: dict) -> list[dict]:
    cur.execute(
        f"""
        SELECT pmi.ID AS menu_item_id, t.name AS menu_name, t.slug AS menu_slug,
               pmi.menu_order, pmi.post_title AS item_label,
               (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_object_id') AS object_id,
               (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_object') AS object_type,
               (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_type') AS item_type,
               (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_url') AS item_url,
               (SELECT meta_value FROM {PREFIX}postmeta WHERE post_id=pmi.ID AND meta_key='_menu_item_menu_item_parent') AS parent_item
        FROM {PREFIX}posts pmi
        JOIN {PREFIX}term_relationships tr ON pmi.ID=tr.object_id
        JOIN {PREFIX}term_taxonomy tt ON tr.term_taxonomy_id=tt.term_taxonomy_id AND tt.taxonomy='nav_menu'
        JOIN {PREFIX}terms t ON tt.term_id=t.term_id
        WHERE pmi.post_type='nav_menu_item' AND pmi.post_status='publish'
        ORDER BY t.name, pmi.menu_order, pmi.ID
        """
    )
    items = []
    for row in cur.fetchall():
        oid = row["object_id"]
        otype = row["object_type"]
        url = row["item_url"] or ""
        if oid in ("6", "7", "8", "73", "77", "84") or "/uslugi/" in (url or ""):
            route = url.replace(BASE, "") if url.startswith("http") else url
            if not route and oid:
                if otype == "page":
                    cur.execute(f"SELECT post_name, post_parent FROM {PREFIX}posts WHERE ID=%s", (oid,))
                    pr = cur.fetchone()
                    if pr:
                        route = build_page_path(cur, pr["post_name"], pr["post_parent"])
                elif otype == "service":
                    cur.execute(f"SELECT post_name, post_parent FROM {PREFIX}posts WHERE ID=%s", (oid,))
                    pr = cur.fetchone()
                    if pr:
                        route = build_service_path(cur, pr["post_name"], pr["post_parent"])
            owner = route_owners.get(route, {})
            items.append(
                {
                    "menu_name": row["menu_name"],
                    "menu_slug": row["menu_slug"],
                    "menu_item_id": row["menu_item_id"],
                    "label": row["item_label"],
                    "linked_object_id": int(oid) if oid and oid.isdigit() else oid,
                    "linked_object_type": otype,
                    "item_type": row["item_type"],
                    "url": url or route,
                    "route_path": route,
                    "menu_order": row["menu_order"],
                    "parent_item_id": row["parent_item"],
                    "current_route_owner": owner,
                    "menu_route_mismatch": (
                        owner.get("queried_object_id") is not None
                        and oid
                        and str(owner.get("queried_object_id")) != str(oid)
                    ),
                }
            )
    return items


def route_audit(cur) -> list[dict]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    static_by_route = {r["route"]: r for r in manifest.get("routes", [])}
    rows = []
    for route in ROUTES:
        status, final_url, body = fetch(route)
        markers = detect_wp_object(body)
        page_id = markers.get("page_id")
        post_id = markers.get("post_id")
        queried_id = post_id or page_id
        queried_type = "service" if markers.get("is_single_service") or (post_id and not page_id) else (
            "page" if page_id else None
        )
        if queried_id:
            cur.execute(
                f"SELECT post_type, post_title, post_name FROM {PREFIX}posts WHERE ID=%s",
                (queried_id,),
            )
            db_row = cur.fetchone()
            if db_row:
                queried_type = db_row["post_type"]
        static = static_by_route.get(route, {})
        conflict_ids = []
        if route == "/uslugi/zavisimosti/":
            conflict_ids = [{"type": "page", "id": 6}, {"type": "service", "id": 73}]
        elif route == "/uslugi/psihicheskoe-zdorovie/":
            conflict_ids = [{"type": "page", "id": 7}, {"type": "service", "id": 77}]
        elif route == "/uslugi/rasstroystva-pischevogo-povedeniya/":
            conflict_ids = [{"type": "page", "id": 8}, {"type": "service", "id": 84}]
        winner = {"type": queried_type, "id": int(queried_id) if queried_id else None}
        severity = "none"
        if conflict_ids and winner["id"]:
            losers = [c for c in conflict_ids if not (c["type"] == winner["type"] and c["id"] == winner["id"])]
            if losers:
                severity = "high" if route in (
                    "/uslugi/zavisimosti/",
                    "/uslugi/psihicheskoe-zdorovie/",
                    "/uslugi/rasstroystva-pischevogo-povedeniya/",
                ) else "medium"
        rows.append(
            {
                "route": route,
                "http_status": status,
                "final_url": final_url,
                "queried_object_type": queried_type,
                "queried_object_id": int(queried_id) if queried_id else None,
                "primary_h1": h1(body),
                "title_tag": strip_html(re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S).group(1))
                if re.search(r"<title", body, re.I)
                else None,
                "body_markers": markers,
                "template_hint": (
                    "services-hub.php"
                    if markers.get("has_services_hub") or markers.get("has_page_uslugi_v2")
                    else "single-service.php (subdivision)"
                    if markers.get("has_service_subdivision")
                    else "single-service.php (leaf)"
                    if markers.get("has_service_leaf") or markers.get("is_single_service")
                    else "page template"
                    if page_id
                    else "unknown"
                ),
                "static_v9_role": static.get("page_type"),
                "static_v9_status": static.get("status"),
                "conflict_objects": conflict_ids,
                "current_owner": winner,
                "conflict_severity": severity,
                "canonical_expectation": static.get("wordpress_family"),
            }
        )
    return rows


def snapshot_protected(cur) -> dict:
    snap = {"pages": {}, "services": {}, "options": {}, "menu_checksum": None}
    for pid in [6, 7, 8]:
        cur.execute(
            f"SELECT ID, post_status, post_modified FROM {PREFIX}posts WHERE ID=%s",
            (pid,),
        )
        snap["pages"][str(pid)] = {k: str(v) if v is not None else None for k, v in cur.fetchone().items()}
    for sid in [73]:
        cur.execute(
            f"SELECT ID, post_status, post_modified FROM {PREFIX}posts WHERE ID=%s",
            (sid,),
        )
        snap["services"][str(sid)] = {k: str(v) if v is not None else None for k, v in cur.fetchone().items()}
    for key in [
        "page_on_front",
        "page_for_posts",
        "permalink_structure",
        "blog_public",
        "wp_page_for_privacy_policy",
    ]:
        cur.execute(f"SELECT option_value FROM {PREFIX}options WHERE option_name=%s", (key,))
        row = cur.fetchone()
        snap["options"][key] = row["option_value"] if row else None
    cur.execute(
        f"""
        SELECT pmi.ID, GROUP_CONCAT(pm.meta_key, '=', pm.meta_value ORDER BY pm.meta_key SEPARATOR '|') AS meta_blob
        FROM {PREFIX}posts pmi
        JOIN {PREFIX}postmeta pm ON pmi.ID=pm.post_id
        WHERE pmi.post_type='nav_menu_item'
        GROUP BY pmi.ID ORDER BY pmi.ID
        """
    )
    blob = "".join(f"{r['ID']}:{r['meta_blob']};" for r in cur.fetchall())
    snap["menu_checksum"] = hashlib.sha256(blob.encode()).hexdigest()
    return snap


def main() -> None:
    conn = pymysql.connect(
        host="127.0.0.1",
        user=DB_USER,
        password=DB_PASS,
        database=DB,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    cur = conn.cursor()
    before = snapshot_protected(cur)
    inventory = object_inventory(cur)
    routes = route_audit(cur)
    route_owners = {r["route"]: r["current_owner"] for r in routes}
    route_owners_detail = {r["route"]: r for r in routes}
    menus = menu_audit(cur, route_owners_detail)
    after = snapshot_protected(cur)

    # zavisimosti children services
    cur.execute(
        f"""
        SELECT ID, post_title, post_name, post_status, post_parent, menu_order, post_modified,
               LENGTH(post_content) AS content_len
        FROM {PREFIX}posts
        WHERE post_type='service' AND post_status='publish'
          AND (ID=73 OR post_parent=73 OR post_name LIKE '%%zavisimosti%%')
        ORDER BY post_parent, menu_order, ID
        """
    )
    zav_services = []
    for row in cur.fetchall():
        zav_services.append(
            {
                "id": row["ID"],
                "title": row["post_title"],
                "slug": row["post_name"],
                "parent_id": row["post_parent"],
                "path": build_service_path(cur, row["post_name"], row["post_parent"]),
                "status": row["post_status"],
                "modified": str(row["post_modified"]),
                "content_len": row["content_len"],
            }
        )
    inventory.extend(
        [
            {
                "id": s["id"],
                "type": "service",
                "title": s["title"],
                "slug": s["slug"],
                "path": s["path"],
                "status": s["status"],
                "parent_id": s["parent_id"],
                "modified": s["modified"],
                "content_len": s["content_len"],
                "note": "zavisimosti_tree_child" if s["parent_id"] == 73 else "zavisimosti_root",
            }
            for s in zav_services
            if s["id"] not in SERVICE_ROOT_IDS
        ]
    )

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    static_rows = []
    for obj in inventory:
        path = obj.get("path", "")
        static = next((r for r in manifest["routes"] if r["route"] == path), None)
        route_row = next((r for r in routes if r["route"] == path), None)
        static_rows.append(
            {
                "route_or_path": path,
                "object_id": obj["id"],
                "object_type": obj["type"],
                "static_v9_exists": static is not None,
                "static_v9_role": static.get("page_type") if static else None,
                "static_v9_status": static.get("status") if static else None,
                "wp_page_exists": any(i["id"] == obj["id"] and i["type"] == "page" for i in inventory),
                "wp_service_exists": obj["type"] == "service",
                "current_rendered_owner": route_row["current_owner"] if route_row else None,
                "recommended_canonical_owner": (
                    {"type": "service", "id": obj["id"]}
                    if static and static.get("page_type", "").startswith("SERVICE")
                    else {"type": "page", "id": obj["id"]}
                    if static and static.get("page_type") in ("SERVICES_HUB", "INSTITUTIONAL")
                    else {"type": "service", "id": 73}
                    if path == "/uslugi/zavisimosti/"
                    else {"type": "service", "id": 77}
                    if path == "/uslugi/psihicheskoe-zdorovie/"
                    else {"type": "service", "id": 84}
                    if path == "/uslugi/rasstroystva-pischevogo-povedeniya/"
                    else None
                ),
            }
        )

    OUT.mkdir(parents=True, exist_ok=True)
    payload = {
        "task_id": TASK_ID,
        "generated_at": NOW,
        "before_snapshot": before,
        "after_snapshot": after,
        "inventory": inventory,
        "routes": routes,
        "menus": menus,
        "static_comparison": static_rows,
        "zavisimosti_service_tree": zav_services,
    }
    (OUT / "_e27c_probe_out.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"ok": True, "routes": len(routes), "inventory": len(inventory)}, indent=2))
    conn.close()


if __name__ == "__main__":
    main()
