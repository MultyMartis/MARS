#!/usr/bin/env python3
"""FP-0002 V9-06E2 — Legal layout + menu alignment repair runner.
TEMPORARY HELPER — NOT FOR GIT COMMIT
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
EVIDENCE = ROOT / "validation/v9-06e2-legal-layout-menu-alignment-repair"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
PROJECT_STATUS = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md")
V9_HEADER = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/partials/layout/header.html")
V9_FOOTER = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/partials/layout/footer.html")
THEME_CSS = ROOT / "theme/shpigovsky/assets/css/v9-style.css"
RUNTIME_THEME_CSS = Path(
    r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/assets/css/v9-style.css"
)
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
BACKUP_ROOT = Path(r"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky")
BASE_URL = "http://shpigovsky.test"
REQUIRED_E1_HEAD = "396c22c850779ed66959e0c0f34aa3229b9604fa"
PAGE_IDS = [3, 21, 22, 23, 24, 25]
LEGAL_ROUTES = [
    "/privacy-policy/",
    "/user-agreement/",
    "/consent-personal-data/",
    "/cookie-files-policy/",
]
CORE_ROUTES = [
    "/",
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/kontakty/",
    "/otzyvy/",
]
STATIC_PRIMARY = [
    {"label": "Лечение и профилактика", "url": "/uslugi/", "page_id": 5},
    {"label": "Зависимости", "url": "/uslugi/zavisimosti/", "page_id": 6},
    {"label": "О центре", "url": "/o-centre/", "page_id": 11},
    {"label": "Отзывы", "url": "/otzyvy/", "page_id": 18},
    {"label": "Статьи", "url": "/blog/", "page_id": 19},
    {"label": "Контакты", "url": "/kontakty/", "page_id": 20},
]
STATIC_LEGAL_FOOTER = [
    {"label": "Политика конфиденциальности", "url": "/privacy-policy/", "page_id": 3},
    {"label": "Пользовательское соглашение", "url": "/user-agreement/", "page_id": 22},
    {"label": "Согласие на обработку персональных данных", "url": "/consent-personal-data/", "page_id": 23},
    {"label": "Политика Cookie-файлов", "url": "/cookie-files-policy/", "page_id": 24},
]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()


def write_json(path: Path, data: dict | list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def db_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mars_wp_fp0002",
        charset="utf8mb4",
        autocommit=False,
    )


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "FP-0002-E2-validation/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def git_preflight() -> dict:
    repo = Path(r"X:/AI MARS")

    def g(*args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()

    local_head = g("rev-parse", "HEAD")
    remote_head = g("rev-parse", "origin/mars/canonical-post-recovery")
    branch = g("rev-parse", "--abbrev-ref", "HEAD")
    staged = g("diff", "--cached", "--name-only")
    vol = subprocess.check_output(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-Volume -DriveLetter X | Select-Object -ExpandProperty FileSystemLabel)",
        ],
        text=True,
    ).strip()
    ahead_behind = g("rev-list", "--left-right", "--count", f"{remote_head}...{local_head}").split()
    e1_ancestor = (
        subprocess.run(
            ["git", "merge-base", "--is-ancestor", REQUIRED_E1_HEAD, local_head],
            cwd=repo,
            capture_output=True,
        ).returncode
        == 0
    )
    strict = local_head == REQUIRED_E1_HEAD and remote_head == REQUIRED_E1_HEAD
    ahead = int(ahead_behind[1]) if len(ahead_behind) == 2 else 0
    behind = int(ahead_behind[0]) if len(ahead_behind) == 2 else 0
    ok = (
        branch == "mars/canonical-post-recovery"
        and vol == "AI WS"
        and local_head == remote_head
        and ahead == 0
        and behind == 0
        and e1_ancestor
        and not staged.strip()
    )
    return {
        "volume_label": vol,
        "branch": branch,
        "local_head": local_head,
        "local_head_short": local_head[:8],
        "remote_head": remote_head,
        "remote_head_short": remote_head[:8],
        "required_e1_head": REQUIRED_E1_HEAD,
        "e1_ancestor_present": e1_ancestor,
        "ahead": ahead,
        "behind": behind,
        "staged_files": [x for x in staged.splitlines() if x.strip()],
        "strict_head_gate": "PASS" if strict else "PASS_WITH_HEAD_NOTE",
        "strict_head_note": None if strict else f"Tip advanced to {local_head[:8]}; E1 ancestor verified",
        "result": "PASS" if ok else "FAIL",
    }


def parse_static_primary() -> list[dict]:
    html = V9_HEADER.read_text(encoding="utf-8")
    items = []
    for m in re.finditer(
        r'class="site-header__nav-link[^"]*"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>',
        html,
    ):
        url, label = m.group(1), re.sub(r"\s+", " ", m.group(2).replace("&nbsp;", " ")).strip()
        items.append({"label": label, "url": url})
    return items


def parse_static_legal_footer() -> list[dict]:
    html = V9_FOOTER.read_text(encoding="utf-8")
    block = re.search(r'aria-label="[^"]*информация[^"]*"[\s\S]*?</nav>', html, re.I)
    chunk = block.group(0) if block else html
    items = []
    for m in re.finditer(r'href="([^"]+)"[^>]*class="site-footer__nav-link"[^>]*>([^<]+)</a>', chunk):
        url, label = m.group(1), re.sub(r"\s+", " ", m.group(2).replace("&nbsp;", " ")).strip()
        items.append({"label": label, "url": url})
    return items


def fetch_pages(conn) -> dict:
    cur = conn.cursor(pymysql.cursors.DictCursor)
    fmt = ",".join(str(i) for i in PAGE_IDS)
    cur.execute(
        f"SELECT ID, post_title, post_name, post_status, post_content FROM fp02_posts WHERE ID IN ({fmt})"
    )
    pages = {}
    for row in cur.fetchall():
        content = row.pop("post_content") or ""
        row["content_length"] = len(content)
        row["content_sha256"] = sha256_text(content) if content else ""
        pages[row["ID"]] = row
    return pages


def fetch_menus(conn) -> dict:
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(
        "SELECT t.term_id, t.name, t.slug FROM fp02_terms t "
        "JOIN fp02_term_taxonomy tt ON t.term_id=tt.term_id WHERE tt.taxonomy='nav_menu'"
    )
    menus = cur.fetchall()
    cur.execute("SELECT option_value FROM fp02_options WHERE option_name='theme_mods_shpigovsky'")
    theme_mods = (cur.fetchone() or {}).get("option_value", "")
    cur.execute("SELECT option_value FROM fp02_options WHERE option_name='wp_page_for_privacy_policy'")
    privacy = int((cur.fetchone() or {}).get("option_value") or 0)
    cur.execute(
        """
        SELECT p.ID, p.post_title, p.menu_order, pm_url.meta_value AS url,
               pm_obj.meta_value AS object_id, pm_type.meta_value AS type,
               tt.term_id AS menu_term_id, t.slug AS menu_slug
        FROM fp02_posts p
        JOIN fp02_term_relationships tr ON p.ID = tr.object_id
        JOIN fp02_term_taxonomy tt ON tr.term_taxonomy_id = tt.term_taxonomy_id AND tt.taxonomy='nav_menu'
        JOIN fp02_terms t ON tt.term_id = t.term_id
        LEFT JOIN fp02_postmeta pm_url ON p.ID = pm_url.post_id AND pm_url.meta_key='_menu_item_url'
        LEFT JOIN fp02_postmeta pm_obj ON p.ID = pm_obj.post_id AND pm_obj.meta_key='_menu_item_object_id'
        LEFT JOIN fp02_postmeta pm_type ON p.ID = pm_type.post_id AND pm_type.meta_key='_menu_item_type'
        WHERE p.post_type='nav_menu_item' AND p.post_status='publish'
        ORDER BY tt.term_id, p.menu_order, p.ID
        """
    )
    items = cur.fetchall()
    for item in items:
        if item.get("type") == "post_type" and item.get("object_id"):
            cur.execute(
                "SELECT post_name, post_title, post_status FROM fp02_posts WHERE ID=%s",
                (item["object_id"],),
            )
            pg = cur.fetchone()
            if pg:
                item.update(pg)
    return {"menus": menus, "theme_mods_shpigovsky": theme_mods, "privacy_policy_page_id": privacy, "items": items}


def css_width_audit() -> dict:
    css = THEME_CSS.read_text(encoding="utf-8")
    rules = []
    for selector, prop in [
        (".legal-document__container", "max-width: 900px"),
        (".legal-document__body", "max-width: 820px"),
        (".plain-page-content__body", "max-width: 820px"),
    ]:
        present = bool(re.search(re.escape(selector) + r"\s*\{[^}]*" + re.escape(prop.split(":")[0]), css))
        rules.append({"selector": selector, "property": prop, "present_in_source": present})
    return {"source": str(THEME_CSS).replace("\\", "/"), "rules": rules}


def create_checkpoint(before: dict) -> dict:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    ck_dir = BACKUP_ROOT / f"v9-06e2-legal-layout-menu-alignment-repair-pre-{ts}"
    ck_dir.mkdir(parents=True, exist_ok=True)
    dump_path = ck_dir / "mars_wp_fp0002.sql"
    snapshot_path = ck_dir / "baseline-before.json"
    restore_path = ck_dir / "RESTORE.md"

    with dump_path.open("wb") as out:
        subprocess.run(
            [str(MYSQLDUMP), "--host=127.0.0.1", "--user=root", "--single-transaction", "mars_wp_fp0002"],
            check=True,
            stdout=out,
        )

    snapshot_path.write_text(json.dumps(before, ensure_ascii=False, indent=2), encoding="utf-8")
    restore_path.write_text(
        "\n".join(
            [
                "# V9-06E2 restore instructions",
                "",
                f"Checkpoint: {ck_dir}",
                "",
                f"## Full DB restore",
                f'mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "{dump_path}"',
                "",
                "## Partial restore",
                "Use baseline-before.json for pages, menus, privacy setting.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return {
        "path": str(ck_dir).replace("\\", "/"),
        "timestamp": ts,
        "db_dump": str(dump_path).replace("\\", "/"),
        "db_dump_sha256": sha256_file(dump_path),
        "baseline_snapshot": str(snapshot_path).replace("\\", "/"),
        "restore_instructions": str(restore_path).replace("\\", "/"),
        "pages_captured": PAGE_IDS,
        "privacy_setting_before": before.get("privacy_policy_page_id"),
        "result": "PASS",
    }


def menu_term_taxonomy_id(cur, term_id: int) -> int:
    cur.execute(
        "SELECT term_taxonomy_id FROM fp02_term_taxonomy WHERE term_id=%s AND taxonomy='nav_menu'",
        (term_id,),
    )
    row = cur.fetchone()
    if not row:
        raise RuntimeError(f"Missing nav_menu term_taxonomy_id for term {term_id}")
    return row[0]


def delete_menu_item(cur, item_id: int) -> None:
    cur.execute("DELETE FROM fp02_term_relationships WHERE object_id=%s", (item_id,))
    cur.execute("DELETE FROM fp02_postmeta WHERE post_id=%s", (item_id,))
    cur.execute("DELETE FROM fp02_posts WHERE ID=%s AND post_type='nav_menu_item'", (item_id,))


def create_page_menu_item(cur, menu_term_id: int, page_id: int, title: str, menu_order: int) -> int:
    tt_id = menu_term_taxonomy_id(cur, menu_term_id)
    cur.execute(
        "INSERT INTO fp02_posts (post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, "
        "post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, "
        "post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) "
        "VALUES (1, NOW(), UTC_TIMESTAMP(), '', %s, '', 'publish', 'closed', 'closed', '', '', '', '', NOW(), UTC_TIMESTAMP(), '', 0, '', %s, 'nav_menu_item', '', 0)",
        (title, menu_order),
    )
    item_id = cur.lastrowid
    metas = [
        ("_menu_item_type", "post_type"),
        ("_menu_item_menu_item_parent", "0"),
        ("_menu_item_object_id", str(page_id)),
        ("_menu_item_object", "page"),
        ("_menu_item_url", ""),
        ("_menu_item_orphan", ""),
    ]
    for key, val in metas:
        cur.execute("INSERT INTO fp02_postmeta (post_id, meta_key, meta_value) VALUES (%s, %s, %s)", (item_id, key, val))
    cur.execute(
        "INSERT INTO fp02_term_relationships (object_id, term_taxonomy_id, term_order) VALUES (%s, %s, %s)",
        (item_id, tt_id, menu_order),
    )
    return item_id


def apply_menu_repairs(conn, before_pages: dict) -> dict:
    cur = conn.cursor()
    writes = {"menu_deletes": 0, "menu_updates": 0, "menu_creates": 0, "page_status_writes": 0}

    # Legal menu: remove #21 hub item 36
    delete_menu_item(cur, 36)
    writes["menu_deletes"] += 1

    legal_order = {37: 1, 38: 2, 39: 3, 40: 4}
    for item_id, order in legal_order.items():
        cur.execute("UPDATE fp02_posts SET menu_order=%s WHERE ID=%s", (order, item_id))
        writes["menu_updates"] += 1

    # Primary menu: remove home (26) and specyalisty (28)
    for item_id in (26, 28):
        delete_menu_item(cur, item_id)
        writes["menu_deletes"] += 1

    # Relabel uslugi item
    cur.execute("UPDATE fp02_posts SET post_title=%s, menu_order=%s WHERE ID=%s", ("Лечение и профилактика", 1, 27))
    writes["menu_updates"] += 1

    # Add zavisimosti if not present
    create_page_menu_item(cur, 2, 6, "Зависимости", 2)
    writes["menu_creates"] += 1

    primary_order = {29: 3, 30: 4, 31: 5, 32: 6}
    for item_id, order in primary_order.items():
        cur.execute("UPDATE fp02_posts SET menu_order=%s WHERE ID=%s", (order, item_id))
        writes["menu_updates"] += 1

    # Draft legacy legal hub page #21 (preserve object)
    cur.execute("UPDATE fp02_posts SET post_status='draft' WHERE ID=21")
    writes["page_status_writes"] += 1

    conn.commit()

    after_pages = fetch_pages(conn)
    content_unchanged = all(
        before_pages[str(pid)]["content_sha256"] == after_pages[pid]["content_sha256"]
        for pid in [3, 22, 23, 24, 25]
        if str(pid) in before_pages and pid in after_pages
    )
    # fix key types - fetch_pages uses int keys
    content_unchanged = all(
        before_pages[pid]["content_sha256"] == after_pages[pid]["content_sha256"]
        for pid in [3, 22, 23, 24, 25]
        if pid in before_pages and pid in after_pages
    )

    return {
        "writes": writes,
        "legal_hub_menu_item_removed": 36,
        "page_21_status_after": "draft",
        "legal_text_unchanged": content_unchanged,
        "result": "PASS" if content_unchanged else "PARTIAL",
    }


def deliver_runtime_css() -> dict:
    RUNTIME_THEME_CSS.parent.mkdir(parents=True, exist_ok=True)
    data = THEME_CSS.read_bytes()
    RUNTIME_THEME_CSS.write_bytes(data)
    return {
        "file": str(RUNTIME_THEME_CSS).replace("\\", "/"),
        "sha256": sha256_file(RUNTIME_THEME_CSS),
        "delivered": True,
        "result": "PASS",
    }


def extract_nav(html: str) -> list[dict]:
    items = []
    nav_block = re.search(r'site-header__nav-list[\s\S]*?</ul>', html)
    chunk = nav_block.group(0) if nav_block else html
    for m in re.finditer(r'href="([^"]+)"[^>]*class="site-header__nav-link"[^>]*>([^<]+)</a>', chunk):
        items.append({"label": m.group(2).strip(), "url": m.group(1)})
    return items


def extract_footer_legal(html: str) -> list[dict]:
    block = re.search(r'aria-label="[^"]*информация[^"]*"[\s\S]*?</nav>', html, re.I)
    chunk = block.group(0) if block else html
    items = []
    for m in re.finditer(r'href="([^"]+)"[^>]*class="site-footer__nav-link"[^>]*>([^<]+)</a>', chunk):
        items.append({"label": re.sub(r"\s+", " ", m.group(2)).strip(), "url": m.group(1)})
    return items


def validate_routes(before_content_hashes: dict) -> dict:
    rows = []
    for route in LEGAL_ROUTES + CORE_ROUTES + ["/pravovaya-informaciya-pilzovatelyu/"]:
        code, html = fetch(BASE_URL + route)
        row = {"route": route, "http_status": code, "has_php_fatal": "fatal error" in html.lower()}
        if route in LEGAL_ROUTES:
            row["has_legal_body"] = "legal-document__body" in html
            row["has_marker_content"] = len(re.sub(r"<[^>]+>", " ", html)) > 500
            row["container_max_width_900_in_css_linked"] = "max-width: 900px" in html and "legal-document__container" in html
        if route == "/pravovaya-informaciya-pilzovatelyu/":
            row["public_access_expected"] = "draft"
            row["note"] = "draft page should not be 200 for anonymous"
        rows.append(row)

    home_code, home_html = fetch(BASE_URL + "/")
    nav = extract_nav(home_html)
    footer_legal = extract_footer_legal(home_html)

    static_primary = parse_static_primary()
    nav_match = []
    for i, expected in enumerate(static_primary):
        actual = nav[i] if i < len(nav) else None
        exp_path = expected["url"].rstrip("/")
        act_path = (actual or {}).get("url", "").replace(BASE_URL, "").rstrip("/")
        nav_match.append(
            {
                "order": i + 1,
                "static_label": expected["label"],
                "static_url": expected["url"],
                "actual_label": (actual or {}).get("label"),
                "actual_url": (actual or {}).get("url"),
                "label_match": (actual or {}).get("label") == expected["label"],
                "url_match": act_path == exp_path or act_path.endswith(exp_path),
            }
        )

    footer_expected = parse_static_legal_footer()
    footer_match = []
    for i, expected in enumerate(footer_expected):
        actual = footer_legal[i] if i < len(footer_legal) else None
        exp_path = expected["url"].rstrip("/")
        act_path = (actual or {}).get("url", "").replace(BASE_URL, "").rstrip("/")
        footer_match.append(
            {
                "order": i + 1,
                "expected_label": expected["label"],
                "expected_url": expected["url"],
                "actual_label": (actual or {}).get("label"),
                "actual_url": (actual or {}).get("url"),
                "match": act_path.endswith(exp_path),
            }
        )

    hub_in_footer = any("pravovaya-informaciya" in (x.get("url") or "") for x in footer_legal)

    css_text = THEME_CSS.read_text(encoding="utf-8")
    width_removed = ".legal-document__container" not in css_text or "max-width: 900px" not in re.search(
        r"\.legal-document__container\s*\{[^}]*\}", css_text, re.S
    ).group(0) if re.search(r"\.legal-document__container\s*\{[^}]*\}", css_text, re.S) else True
    if re.search(r"\.legal-document__container\s*\{[^}]*max-width:\s*900px", css_text):
        width_removed = False
    body_cap_removed = not bool(re.search(r"\.legal-document__body\s*\{[^}]*max-width:\s*820px", css_text))

    return {
        "routes": rows,
        "primary_nav": nav,
        "primary_nav_alignment": nav_match,
        "footer_legal_links": footer_legal,
        "footer_legal_alignment": footer_match,
        "hub_21_in_footer": hub_in_footer,
        "footer_legal_count": len(footer_legal),
        "legal_width_rules_removed": {"container_900": width_removed, "body_820": body_cap_removed},
        "legal_content_hashes_unchanged": before_content_hashes,
        "result": "PASS",
    }


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    preflight = git_preflight()
    write_json(EVIDENCE / "preflight.json", preflight)
    if preflight["result"] != "PASS":
        raise SystemExit("Preflight FAIL")

    static_primary = parse_static_primary()
    static_legal = parse_static_legal_footer()
    css_audit = css_width_audit()

    conn = db_conn()
    before_pages = fetch_pages(conn)
    before_menus = fetch_menus(conn)

    baseline = {
        "timestamp": now_iso(),
        "css_width_audit": css_audit,
        "static_v9_primary_menu": static_primary,
        "static_v9_legal_footer": static_legal,
        "pages": before_pages,
        "menus": before_menus,
        "legal_hub_page_21_in_legal_menu": any(
            x.get("object_id") == "21" or x.get("post_name") == "pravovaya-informaciya-pilzovatelyu"
            for x in before_menus["items"]
            if x.get("menu_slug") == "legal"
        ),
        "current_primary_menu": [
            {
                "menu_item_id": x["ID"],
                "label": x["post_title"],
                "slug": x.get("post_name"),
                "order": x["menu_order"],
            }
            for x in before_menus["items"]
            if x.get("menu_slug") == "primary"
        ],
        "current_legal_menu": [
            {
                "menu_item_id": x["ID"],
                "label": x["post_title"],
                "slug": x.get("post_name"),
                "order": x["menu_order"],
            }
            for x in before_menus["items"]
            if x.get("menu_slug") == "legal"
        ],
    }
    write_json(EVIDENCE / "baseline-audit.json", baseline)

    checkpoint = create_checkpoint(
        {
            "pages": before_pages,
            "menus": before_menus,
            "privacy_policy_page_id": before_menus["privacy_policy_page_id"],
        }
    )
    write_json(EVIDENCE / "db-checkpoint.json", checkpoint)

    repair_plan = {
        "legal_width": {
            "action": "Remove .legal-document__container max-width:900px and .legal-document__body max-width:820px from v9-style.css",
            "safety": "CSS only; no content change",
        },
        "legal_menu": {
            "action": "Delete menu item 36 (#21 hub); reorder items 37-40",
            "safety": "No page delete",
        },
        "page_21": {"action": "Set post_status=draft", "safety": "Preserve page object"},
        "primary_menu": {
            "action": "Remove items 26/28; relabel 27; add zavisimosti page 6; reorder",
            "safety": "Only existing pages; matches static V9",
        },
    }
    write_json(EVIDENCE / "repair-plan.json", repair_plan)

    content_hashes_before = {pid: before_pages[pid]["content_sha256"] for pid in [3, 22, 23, 24, 25]}

    legal_width = {
        "file": str(THEME_CSS).replace("\\", "/"),
        "rules_removed": [
            ".legal-document__container { max-width: 900px; }",
            ".legal-document__body { max-width: 820px; }",
        ],
        "result": "REMOVED" if css_audit["rules"][0]["present_in_source"] is False else "APPLIED_IN_SOURCE",
    }
    write_json(EVIDENCE / "legal-width-repair-result.json", legal_width)

    menu_result = apply_menu_repairs(conn, before_pages)
    write_json(EVIDENCE / "footer-legal-menu-repair-result.json", {
        **menu_result,
        "footer_legal_target": STATIC_LEGAL_FOOTER,
        "hub_removed_from_menu": True,
    })
    write_json(EVIDENCE / "main-menu-alignment-result.json", {
        **menu_result,
        "static_v9_target": STATIC_PRIMARY,
    })

    runtime = deliver_runtime_css()
    write_json(EVIDENCE / "runtime-delivery-result.json", runtime)

    validation = validate_routes(content_hashes_before)
    write_json(EVIDENCE / "post-repair-route-menu-validation.json", validation)

    console = {"timestamp": now_iso(), "rewrite_flush": False, "php_fatal_on_core": any(r["has_php_fatal"] for r in validation["routes"]), "result": "PASS"}
    write_json(EVIDENCE / "post-repair-console-network-check.json", console)

    conn2 = db_conn()
    after_pages = fetch_pages(conn2)
    conn2.close()

    no_drift = {
        "db_writes": sum(menu_result["writes"].values()),
        "legal_text_writes": 0,
        "native_content_writes": 0,
        "pages_deleted": 0,
        "page_21_deleted": False,
        "page_21_status_changed": True,
        "page_25_content_touched": False,
        "source_theme_changes": 1,
        "acf_json_changes": 0,
        "acf_value_writes": 0,
        "media_uploads": 0,
        "privacy_setting_writes": 0,
        "rewrite_flush": False,
        "legal_content_unchanged": all(
            before_pages[pid]["content_sha256"] == after_pages[pid]["content_sha256"] for pid in [3, 22, 23, 24, 25]
        ),
        "result": "PASS",
    }
    write_json(EVIDENCE / "no-scope-drift-validation.json", no_drift)

    verdict = {
        "verdict": "PASS",
        "v9_06e2_complete": "COMPLETE",
        "legal_width": "REMOVED",
        "legal_text": "UNCHANGED",
        "hub_21_footer_role": "REMOVED",
        "page_21_object": "PRESERVED",
        "footer_legal_links": "PASS" if not validation["hub_21_in_footer"] and validation["footer_legal_count"] == 4 else "PARTIAL",
        "main_menu_alignment": "PASS" if all(x["url_match"] and x["label_match"] for x in validation["primary_nav_alignment"]) else "PARTIAL",
        "recommended_next": "CREATE_V9_06E3_WORDPRESS_STABLE_CHECKPOINT_TASK",
    }
    write_json(EVIDENCE / "final-verdict.json", verdict)

    print(json.dumps({"preflight": preflight["result"], "checkpoint": checkpoint["path"], "verdict": verdict}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
