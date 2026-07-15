#!/usr/bin/env python3
"""TEMPORARY E27A read-only probe — NOT FOR GIT COMMIT."""
from __future__ import annotations

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
OUT = Path(__file__).resolve().parent
MANIFEST = Path(
    r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/tools/v9-route-manifest.json"
)


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
    match = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.I | re.S)
    return strip_html(match.group(1)) if match else None


def title_tag(body: str) -> str | None:
    match = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
    return strip_html(match.group(1)) if match else None


def build_page_path(cur, post_name: str, parent_id: int) -> str:
    chain: list[str] = []
    parent = parent_id
    while parent:
        cur.execute(
            f"SELECT post_name, post_parent FROM {PREFIX}posts WHERE ID=%s",
            (parent,),
        )
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
        cur.execute(
            f"SELECT post_name, post_parent FROM {PREFIX}posts WHERE ID=%s",
            (parent,),
        )
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
    if "placeholder" in text.lower() or "skeleton" in text.lower():
        return "placeholder"
    return "full_or_template_managed"


def main() -> None:
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database=DB,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    cur = conn.cursor()

    counts: dict[str, dict[str, int]] = {}
    for post_type in ["page", "post", "service", "nav_menu_item", "acf-field-group", "revision"]:
        cur.execute(
            f"SELECT post_status, COUNT(*) AS c FROM {PREFIX}posts "
            f"WHERE post_type=%s GROUP BY post_status",
            (post_type,),
        )
        counts[post_type] = {row["post_status"]: row["c"] for row in cur.fetchall()}

    cur.execute(f"SELECT COUNT(*) AS c FROM {PREFIX}terms")
    terms_count = cur.fetchone()["c"]

    options: dict[str, str | None] = {}
    for key in [
        "page_on_front",
        "page_for_posts",
        "show_on_front",
        "permalink_structure",
        "blog_public",
        "wp_page_for_privacy_policy",
    ]:
        cur.execute(
            f"SELECT option_value FROM {PREFIX}options WHERE option_name=%s",
            (key,),
        )
        row = cur.fetchone()
        options[key] = row["option_value"] if row else None

    cur.execute(
        f"""
        SELECT p.ID, p.post_title, p.post_name, p.post_status, p.post_parent,
               p.menu_order, p.post_modified, p.post_content,
               pm.meta_value AS page_template
        FROM {PREFIX}posts p
        LEFT JOIN {PREFIX}postmeta pm ON p.ID = pm.post_id AND pm.meta_key='_wp_page_template'
        WHERE p.post_type='page' AND p.post_status NOT IN ('auto-draft')
        ORDER BY p.ID
        """
    )
    pages = []
    for row in cur.fetchall():
        pid = row["ID"]
        path = build_page_path(cur, row["post_name"], row["post_parent"])
        cur.execute(
            f"SELECT COUNT(*) AS c FROM {PREFIX}postmeta WHERE post_id=%s",
            (pid,),
        )
        meta_count = cur.fetchone()["c"]
        cur.execute(
            f"SELECT COUNT(*) AS c FROM {PREFIX}postmeta "
            f"WHERE post_id=%s AND meta_key LIKE %s",
            (pid, "field_%"),
        )
        acf_field_refs = cur.fetchone()["c"]
        pages.append(
            {
                "ID": pid,
                "post_title": row["post_title"],
                "post_name": row["post_name"],
                "post_status": row["post_status"],
                "post_parent": row["post_parent"],
                "menu_order": row["menu_order"],
                "post_modified": str(row["post_modified"]),
                "path": path,
                "page_template": row["page_template"] or "default",
                "meta_count": meta_count,
                "has_acf_meta": meta_count > 2,
                "content_class": content_class(row["post_content"], row["page_template"]),
                "is_front_page": str(pid) == str(options.get("page_on_front")),
                "is_posts_page": str(pid) == str(options.get("page_for_posts")),
                "is_privacy_page": str(pid) == str(options.get("wp_page_for_privacy_policy")),
                "content_len": len((row["post_content"] or "").strip()),
            }
        )

    cur.execute(
        f"""
        SELECT ID, post_title, post_name, post_status, post_date, post_modified, post_content
        FROM {PREFIX}posts
        WHERE post_type='post' AND post_status NOT IN ('auto-draft')
        ORDER BY ID
        """
    )
    posts = []
    for row in cur.fetchall():
        cur.execute(
            """
            SELECT t.name, t.slug, tt.taxonomy
            FROM fp02_terms t
            JOIN fp02_term_taxonomy tt ON t.term_id = tt.term_id
            JOIN fp02_term_relationships tr ON tt.term_taxonomy_id = tr.term_taxonomy_id
            WHERE tr.object_id=%s AND tt.taxonomy IN ('category', 'post_tag')
            """,
            (row["ID"],),
        )
        terms = cur.fetchall()
        posts.append(
            {
                "ID": row["ID"],
                "post_title": row["post_title"],
                "post_name": row["post_name"],
                "post_status": row["post_status"],
                "post_date": str(row["post_date"]),
                "post_modified": str(row["post_modified"]),
                "route": f"/blog/{row['post_name']}/",
                "terms": terms,
                "content_len": len((row["post_content"] or "").strip()),
                "is_demo_fixture": row["ID"] == 750,
            }
        )

    cur.execute(
        f"""
        SELECT p.ID, p.post_title, p.post_name, p.post_status, p.post_parent, p.post_modified,
               dup.meta_value AS duplicated_from, wave.meta_value AS duplicated_wave
        FROM {PREFIX}posts p
        LEFT JOIN {PREFIX}postmeta dup ON p.ID = dup.post_id AND dup.meta_key='_fp02_duplicated_from'
        LEFT JOIN {PREFIX}postmeta wave ON p.ID = wave.post_id AND wave.meta_key='_fp02_duplicated_wave'
        WHERE p.post_type='service' AND p.post_status NOT IN ('auto-draft')
        ORDER BY p.ID
        """
    )
    services = []
    for row in cur.fetchall():
        path = build_service_path(cur, row["post_name"], row["post_parent"])
        cur.execute(
            f"SELECT COUNT(*) AS c FROM {PREFIX}postmeta WHERE post_id=%s",
            (row["ID"],),
        )
        meta_count = cur.fetchone()["c"]
        services.append(
            {
                "ID": row["ID"],
                "post_title": row["post_title"],
                "post_name": row["post_name"],
                "post_status": row["post_status"],
                "post_parent": row["post_parent"],
                "post_modified": str(row["post_modified"]),
                "path": path,
                "meta_count": meta_count,
                "is_duplicate": bool(row.get("duplicated_from")),
                "duplicated_from": row.get("duplicated_from"),
                "duplicated_wave": row.get("duplicated_wave"),
            }
        )

    cur.execute(
        f"""
        SELECT p.ID AS menu_item_id, t.term_id AS menu_id, t.name AS menu_name, t.slug AS menu_slug,
               pm_obj.meta_value AS object_id, pm_type.meta_value AS item_type,
               pm_url.meta_value AS url, p.menu_order
        FROM {PREFIX}posts p
        JOIN {PREFIX}term_relationships tr ON p.ID = tr.object_id
        JOIN {PREFIX}term_taxonomy tt ON tr.term_taxonomy_id = tt.term_taxonomy_id AND tt.taxonomy='nav_menu'
        JOIN {PREFIX}terms t ON tt.term_id = t.term_id
        LEFT JOIN {PREFIX}postmeta pm_obj ON p.ID = pm_obj.post_id AND pm_obj.meta_key='_menu_item_object_id'
        LEFT JOIN {PREFIX}postmeta pm_type ON p.ID = pm_type.post_id AND pm_type.meta_key='_menu_item_type'
        LEFT JOIN {PREFIX}postmeta pm_url ON p.ID = pm_url.post_id AND pm_url.meta_key='_menu_item_url'
        WHERE p.post_type='nav_menu_item' AND p.post_status='publish'
        ORDER BY t.term_id, p.menu_order
        """
    )
    menu_items = cur.fetchall()
    menu_object_ids = sorted(
        {int(item["object_id"]) for item in menu_items if item.get("object_id")}
    )

    cur.execute(
        f"SELECT ID, post_title, post_status FROM {PREFIX}posts "
        f"WHERE post_type='acf-field-group' ORDER BY ID"
    )
    acf_groups = cur.fetchall()

    routes: set[str] = set()
    page_by_path = {p["path"]: p for p in pages if p["post_status"] == "publish"}
    service_by_path = {s["path"]: s for s in services if s["post_status"] == "publish"}
    for page in pages:
        if page["post_status"] == "publish":
            routes.add(page["path"])
    for service in services:
        if service["post_status"] == "publish":
            routes.add(service["path"])
    for post in posts:
        if post["post_status"] == "publish":
            routes.add(post["route"])

    mandatory = [
        "/",
        "/o-centre/",
        "/blog/",
        "/blog/nazvanie-stati/",
        "/uslugi/",
        "/uslugi/zavisimosti/",
        "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
        "/kontakty/",
        "/otzyvy/",
        "/privacy-policy/",
        "/user-agreement/",
        "/consent-personal-data/",
        "/cookie-files-policy/",
    ]
    routes.update(mandatory)

    route_health = []
    for route in sorted(routes):
        code, final_url, body = fetch(route)
        owner = None
        owner_type = None
        if route in page_by_path:
            owner = page_by_path[route]
            owner_type = "page"
        elif route in service_by_path:
            owner = service_by_path[route]
            owner_type = "service"
        else:
            for post in posts:
                if post["route"] == route:
                    owner = post
                    owner_type = "post"
                    break
        route_health.append(
            {
                "route": route,
                "http_status": code,
                "final_url": final_url,
                "title": title_tag(body),
                "h1": h1(body),
                "owner_type": owner_type,
                "owner_id": owner["ID"] if owner else None,
                "owner_status": owner["post_status"] if owner else None,
                "is_404": code == 404,
                "has_skeleton_marker": "shpigovsky-skeleton" in body,
                "has_placeholder_marker": bool(
                    re.search(r"placeholder|skeleton|LOCAL_MVP", body, re.I)
                ),
                "is_demo_route": route == "/blog/nazvanie-stati/",
            }
        )

    static_manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    static_routes = [item["route"] for item in static_manifest.get("routes", [])]

    snapshot = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "task_id": "V9-06E27A",
        "counts": counts,
        "terms_count": terms_count,
        "options": options,
        "pages": pages,
        "posts": posts,
        "services": services,
        "menu_items": menu_items,
        "menu_object_ids": menu_object_ids,
        "acf_field_groups": acf_groups,
        "route_health": route_health,
        "static_routes": static_routes,
    }
    (OUT / "_probe_raw.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )
    print(
        "PROBE_OK",
        len(pages),
        "pages",
        len(posts),
        "posts",
        len(services),
        "services",
        len(route_health),
        "routes",
    )
    conn.close()


if __name__ == "__main__":
    main()
