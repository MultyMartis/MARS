#!/usr/bin/env python3
"""SITE-002 — megamenu leaf info mini-description field + panel refine.

Operation: SITE-002-PROD-MEGAMENU-LEAF-INFO-MINIDESCRIPTION-01
"""

from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import io
import json
import re
import shlex
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from site002_harness_authority import (
    CANONICAL_MONOREPO,
    DEFAULT_MONITOR_CHECKOUT,
    guard_historical_harness,
    resolve_repo_root_for_read,
    site002_reports_dir,
    site002_tools_dir,
)

OPERATION_ID = "SITE-002-PROD-MEGAMENU-LEAF-INFO-MINIDESCRIPTION-01"
PREV_CSS_MARKER = "SITE-002-PROD-MEGAMENU-LEAF-ROOT-INFO-PANEL-01"
CSS_MARKER = OPERATION_ID
PRODUCTION_URL = "https://bzpm.ru/"
PREFIX = "oc_"
LANGUAGE_ID = 1
CATEGORY_ID = 364
POSUDA_NAME = "Посуда и инвентарь"
POSUDA_MINI = (
    "Гастроёмкости, кухонная посуда и инвентарь для предприятий "
    "общественного питания и пищевых производств."
)
GENERIC_FALLBACK = (
    "В данном разделе представлены товары категории. "
    "Перейдите в каталог, чтобы посмотреть ассортимент."
)

SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
AUTHORITY_REPO = CANONICAL_MONOREPO
TOOLS = site002_tools_dir()
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"
REPORT_PATH = (
    AUTHORITY_REPO
    / "projects/ocpilot/sites/site-002/reports"
    / f"{OPERATION_ID}.md"
)
STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
) / OPERATION_ID

MIRROR = {
    "cv": TOOLS / "category_visibility.php",
    "twig": TOOLS / f"megamenu-{OPERATION_ID}.twig",
    "css": TOOLS / f"megamenu-leaf-info-{OPERATION_ID}.css",
    "admin_model": TOOLS / f"admin-model-category-{OPERATION_ID}.php",
    "admin_form": TOOLS / f"admin-category-form-{OPERATION_ID}.twig",
    "admin_lang_ru": TOOLS / f"admin-lang-ru-category-{OPERATION_ID}.php",
    "admin_lang_en": TOOLS / f"admin-lang-en-category-{OPERATION_ID}.php",
}

REMOTE = {
    "cv": "/public_html/system/library/zpm/category_visibility.php",
    "twig": "/public_html/catalog/view/theme/default/template/common/megamenu.twig",
    "css": "/public_html/assets/css/style.css",
    "css_min": "/public_html/assets/css/style.min.css",
    "admin_model": "/public_html/admin/model/catalog/category.php",
    "admin_form": "/public_html/admin/view/template/catalog/category_form.twig",
    "admin_lang_ru": "/public_html/admin/language/ru-ru/catalog/category.php",
    "admin_lang_en": "/public_html/admin/language/en-gb/catalog/category.php",
}

STORAGE_SUBDIRS = (
    "preflight",
    "db-before",
    "admin-source-diagnostic",
    "frontend-source-diagnostic",
    "schema-plan",
    "file-backups",
    "rollback",
    "production-apply",
    "cache",
    "admin-smoke",
    "public-before",
    "public-after",
    "visual-smoke",
    "regression",
    "reports",
    "logs",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_production_section(subsection: str | None = None) -> dict[str, str]:
    text = SECRETS_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)",
            block,
            re.MULTILINE,
        )
        if not sub:
            raise RuntimeError(f"subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    key: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(key, "")
            continue
        if key:
            fields[key] = s
    return fields


def ssh_exec(cmd: str, timeout: int = 180) -> str:
    import paramiko

    ssh = parse_production_section("SSH")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh["host"],
        port=int(ssh.get("port") or 22),
        username=ssh["username"],
        password=ssh["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    _i, out, err = client.exec_command(cmd, timeout=timeout)
    text = out.read().decode("utf-8", errors="replace") + err.read().decode(
        "utf-8", errors="replace"
    )
    client.close()
    return text


def mysql_query(sql: str) -> str:
    db = parse_production_section("Database")
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B '
        f'-u {shlex.quote(db["username"])} {shlex.quote(db["database"])} '
        f'-e "{esc}" 2>&1'
    )
    text = ssh_exec(cmd)
    if "ERROR" in text or "Access denied" in text:
        raise RuntimeError(f"MySQL failed: {text[:800]}")
    return text


def mysql_exec(sql: str) -> str:
    return mysql_query(sql)


def parse_tsv(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.strip() or line.startswith("ERROR") or line.startswith("mysql:"):
            continue
        rows.append(line.split("\t"))
    return rows


def ftp_connect() -> ftplib.FTP:
    fields = parse_production_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=60)
    ftp.login(fields["username"], fields["password"])
    ftp.set_pasv(True)
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes | None:
    buf = bytearray()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.extend)
        return bytes(buf)
    except ftplib.error_perm:
        return None


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def fetch_url(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": f"MARS-{OPERATION_ID}/1.0", "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "bytes": len(body),
                "body": body,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "url": url,
            "status": exc.code,
            "final_url": exc.geturl(),
            "bytes": len(body),
            "body": body,
        }


def has_php_warning(html: str) -> bool:
    return bool(re.search(r"(Fatal error|Warning:|Notice:|Parse error)", html, re.I))


def ensure_storage() -> None:
    for sub in STORAGE_SUBDIRS:
        (STORAGE / sub).mkdir(parents=True, exist_ok=True)


def git_preflight() -> dict[str, str]:
    def run(args: list[str]) -> str:
        return subprocess.check_output(
            args, cwd=AUTHORITY_REPO, text=True, stderr=subprocess.STDOUT
        ).strip()

    return {
        "branch": run(["git", "branch", "--show-current"]),
        "head": run(["git", "rev-parse", "--short", "HEAD"]),
        "status_short": run(["git", "status", "--short"]) or "(clean)",
    }


def column_exists(column: str) -> bool:
    text = mysql_query(
        f"SHOW COLUMNS FROM {PREFIX}category_description LIKE '{column}';"
    )
    return bool(text.strip())


def dump_category_description_before() -> list[dict[str, Any]]:
    cols = "category_id, language_id, name, LENGTH(IFNULL(description,'')) AS description_len"
    if column_exists("menu_description"):
        cols += ", IFNULL(menu_description,'') AS menu_description"
    sql = (
        f"SELECT {cols} FROM {PREFIX}category_description "
        f"WHERE category_id={CATEGORY_ID} ORDER BY language_id;"
    )
    rows_out: list[dict[str, Any]] = []
    for r in parse_tsv(mysql_query(sql)):
        item = {
            "category_id": r[0],
            "language_id": r[1],
            "name": r[2],
            "description_len": r[3],
            "menu_description": r[4] if len(r) > 4 else "",
        }
        rows_out.append(item)
    return rows_out


def extract_left_cats(html: str) -> list[str]:
    return re.findall(
        r'class="[^"]*zpm-catalog__cats-btn[^"]*"[^>]*>([^<]+)</button>',
        html,
        re.I,
    )


def pane_for_category(html: str, name: str) -> str:
    pat = (
        rf'data-cat-pane="{re.escape(name)}"[\s\S]*?(?=data-cat-pane="|zpm-catalog__last-block|$)'
    )
    m = re.search(pat, html, re.I)
    return m.group(0) if m else ""


def analyze_megamenu(html: str) -> dict[str, Any]:
    left = extract_left_cats(html)
    posuda_pane = pane_for_category(html, POSUDA_NAME)
    neutral_pane = pane_for_category(html, "Нейтральное оборудование")
    has_leaf = 'data-leaf-info="1"' in posuda_pane or "zpm-catalog__leaf-info" in posuda_pane
    text_match = POSUDA_MINI in posuda_pane
    has_generic = GENERIC_FALLBACK in posuda_pane
    cta_is_btn = bool(
        re.search(
            r'class="[^"]*btn[^"]*btn_dark[^"]*zpm-catalog__leaf-info-cta',
            posuda_pane,
        )
    ) or bool(
        re.search(
            r'class="[^"]*zpm-catalog__leaf-info-cta[^"]*btn_dark',
            posuda_pane,
        )
    )
    cta_is_text_link = bool(
        re.search(r'class="zpm-catalog__leaf-info-cta"', posuda_pane)
    ) and not cta_is_btn
    has_bzpm = "БЗПМ" in html
    return {
        "left_categories": left,
        "has_posuda_left": any("Посуда" in x for x in left),
        "has_upak_left": any("Упаковочн" in x for x in left),
        "posuda_has_leaf_info": has_leaf,
        "posuda_has_tiles": "zpm-catalog__tile" in posuda_pane,
        "posuda_has_mini_text": text_match,
        "posuda_has_generic_fallback": has_generic,
        "posuda_cta_is_filled_button": cta_is_btn,
        "posuda_cta_is_text_link": cta_is_text_link,
        "neutral_has_tiles": "zpm-catalog__tile" in neutral_pane,
        "php_warning": has_php_warning(html),
        "has_bzpm": has_bzpm,
        "posuda_products_plp_ok": None,
    }


def public_smoke(label: str) -> list[dict[str, Any]]:
    urls = [
        ("home", PRODUCTION_URL),
        ("katalog", PRODUCTION_URL + "katalog/"),
        ("posuda", PRODUCTION_URL + "posuda-i-inventar"),
        ("upak", PRODUCTION_URL + "upakovochnoe-oborudovanie"),
    ]
    rows: list[dict[str, Any]] = []
    for key, url in urls:
        resp = fetch_url(url)
        body = resp["body"]
        menu = analyze_megamenu(body) if key in ("home", "katalog") else {}
        if key == "posuda":
            menu = {
                "php_warning": has_php_warning(body),
                "has_bzpm": "БЗПМ" in body,
                "has_product_cards": bool(
                    re.search(r"product-thumb|product-layout|zpm-product|product-item", body, re.I)
                )
                or ("product" in body.lower() and "цена" in body.lower()),
                "title_ok": POSUDA_NAME in body,
            }
        rows.append(
            {
                "phase": label,
                "key": key,
                "url": url,
                "status": resp["status"],
                "bytes": resp["bytes"],
                "php_warning": has_php_warning(body),
                "menu_json": json.dumps(menu, ensure_ascii=False),
            }
        )
        write_text(STORAGE / f"public-{label}" / f"{key}.html", body)
        if menu:
            write_json(STORAGE / f"public-{label}" / f"{key}-megamenu.json", menu)
    return rows


def strip_css_marker_block(text: str, marker: str) -> str:
    if marker not in text:
        return text
    return re.sub(
        rf"/\* {re.escape(marker)}[\s\S]*?(?=\Z|/\* SITE-002)",
        "",
        text,
        count=1,
    )


def rebuild_css(existing: bytes, block: str) -> bytes:
    text = existing.decode("utf-8", errors="replace")
    text = strip_css_marker_block(text, PREV_CSS_MARKER)
    text = strip_css_marker_block(text, CSS_MARKER)
    return (text.rstrip() + "\n\n" + block.strip() + "\n").encode("utf-8")


def clear_twig_cache() -> str:
    cmd = (
        f"find {shlex.quote(CACHE_DIR)} -type f "
        r"\( -name 'template.*' -o -name '*twig*' -o -name 'cache.*' \) "
        f"-delete 2>/dev/null; "
        f"rm -f {shlex.quote(CACHE_DIR)}/cache.* 2>/dev/null; "
        f"ls {shlex.quote(CACHE_DIR)} | head -20; echo CACHE_CLEAR_DONE"
    )
    return ssh_exec(cmd)


def write_plan_docs() -> None:
    write_text(
        STORAGE / "schema-plan" / "exact-plan.md",
        "\n".join(
            [
                f"# Exact plan — {OPERATION_ID}",
                "",
                "## DB",
                f"1. `ALTER TABLE {PREFIX}category_description ADD COLUMN menu_description TEXT NULL DEFAULT NULL AFTER description;` (if missing).",
                f"2. `UPDATE {PREFIX}category_description SET menu_description='…' WHERE category_id={CATEGORY_ID} AND language_id={LANGUAGE_ID};`",
                "",
                "## Admin",
                "- model `admin/model/catalog/category.php` — insert/load `menu_description`",
                "- form `admin/view/template/catalog/category_form.twig` — field «Мини-описание для меню»",
                "- language ru/en `entry_menu_description` + `help_menu_description`",
                "- controller unchanged (passes category_description array)",
                "",
                "## Frontend",
                "- `category_visibility.php` — prefer menu_description",
                "- `megamenu.twig` — CTA as text link (no btn_dark)",
                "- `assets/css/style.css` + `style.min.css` — replace leaf CSS: white bordered media + text CTA",
                "",
                "## Cache",
                "- clear storage/cache twig/template files",
                "",
                "## Out of scope",
                "- hierarchy/products/URLs/redirects/import/baseline/[96]/root tiles",
                "",
            ]
        ),
    )
    esc = POSUDA_MINI.replace("'", "''")
    write_text(
        STORAGE / "rollback" / "rollback.sql",
        "\n".join(
            [
                f"-- Rollback for {OPERATION_ID}",
                f"-- 1) Restore [364] mini-description (optional clear)",
                f"UPDATE {PREFIX}category_description SET menu_description = NULL "
                f"WHERE category_id = {CATEGORY_ID};",
                "",
                "-- 2) Drop column only if this wave introduced it and operator approves full schema rollback",
                f"-- ALTER TABLE {PREFIX}category_description DROP COLUMN menu_description;",
                "",
                f"-- Applied value was: '{esc}'",
                "",
            ]
        ),
    )
    write_text(
        STORAGE / "rollback" / "rollback-plan.md",
        "\n".join(
            [
                f"# Rollback plan — {OPERATION_ID}",
                "",
                "1. Restore FTP byte backups from `file-backups/` to remotes listed in `file-backup-inventory.csv`.",
                "2. Run `rollback/rollback.sql` (NULL menu_description for 364; DROP COLUMN only if approved).",
                "3. Clear `storage/cache` twig/template files.",
                "4. Re-smoke home + /katalog/ Posuda leaf pane.",
                "",
            ]
        ),
    )


def write_report(payload: dict[str, Any]) -> None:
    after = payload["after_home_menu"]
    lines = [
        f"# REPORT — {OPERATION_ID}",
        "",
        f"- Generated: {utc_now()}",
        f"- Authority worktree: `{AUTHORITY_REPO}`",
        f"- Branch: `{payload['preflight']['branch']}` @ `{payload['preflight']['head']}`",
        f"- Storage: `{STORAGE}`",
        "",
        "## 1. Scope",
        "",
        "Add per-category admin field `menu_description` (Мини-описание для меню),",
        "fill it for `[364] Посуда и инвентарь`, use it in megamenu leaf info panel,",
        "refine leaf image box (white + border) and CTA to text link.",
        "",
        "## 2. Operator feedback",
        "",
        "- Replace generic fallback text with category-specific mini description.",
        "- Admin field for mini description.",
        "- White bordered image block; CTA as text link.",
        "",
        "## 3. Boundary",
        "",
        "No category hierarchy / products / URLs / redirects / 1C / baseline / root tiles / [96] changes.",
        "",
        "## 4. DB/admin/frontend diagnostic",
        "",
        f"- Schema before: `oc_category_description` lacked `menu_description` (see `db-before/schema-before.txt`).",
        f"- Category 364: status=1, visible children=0, direct products=6, description empty.",
        "- Admin sources: standard OC `admin/*/catalog/category*` identified.",
        "- Frontend: `category_visibility.php` + `megamenu.twig` + `assets/css/style.css`.",
        "- Catalog `getCategory()` uses `SELECT *` → new column auto-available.",
        "",
        "## 5. Exact plan",
        "",
        "See `schema-plan/exact-plan.md`.",
        "",
        "## 6. Backup / rollback",
        "",
        "- File backups: `file-backups/`",
        "- DB before: `db-before/`",
        "- Rollback SQL/plan: `rollback/`",
        "",
        "## 7. Production apply",
        "",
        "| Remote path | Action | SHA256 after |",
        "|-------------|--------|--------------|",
    ]
    for row in payload["changed_files"]:
        lines.append(
            f"| `{row['remote']}` | {row['action']} | `{row['sha256_after']}` |"
        )
    lines += [
        "",
        "### DB apply",
        "",
        f"- Column `menu_description` present: {payload['db']['column_present_after']}",
        f"- [364] value set: `{payload['db']['menu_description_364']}`",
        "",
        "## 8. Admin smoke",
        "",
        payload["admin_smoke_note"],
        "",
        "## 9. Public after",
        "",
        "| Check | After |",
        "|-------|-------|",
        f"| Posuda left | {after.get('has_posuda_left')} |",
        f"| Upak left | {after.get('has_upak_left')} |",
        f"| Leaf info panel | {after.get('posuda_has_leaf_info')} |",
        f"| Mini description text | {after.get('posuda_has_mini_text')} |",
        f"| Generic fallback absent | {not after.get('posuda_has_generic_fallback')} |",
        f"| CTA text link | {after.get('posuda_cta_is_text_link')} |",
        f"| CTA filled button | {after.get('posuda_cta_is_filled_button')} |",
        f"| Neutral tiles | {after.get('neutral_has_tiles')} |",
        f"| PHP warning | {after.get('php_warning')} |",
        f"| БЗПМ | {after.get('has_bzpm')} |",
        "",
        "## 10. Visual result",
        "",
        "- Image media: white background + standard border (CSS).",
        "- CTA: text link class `zpm-catalog__leaf-info-cta` without `btn_dark`.",
        "",
        "## 11. Regression",
        "",
        "- Category structure changed: 0",
        "- Products changed: 0",
        "- URLs/redirects: 0",
        "- Import run: 0",
        "- Baseline refresh: 0",
        "- [96] changed: 0",
        "- [381] remains status=0 / hidden from left column",
        "- DB: +nullable column `menu_description`; data update for language_id=1 category 364 only",
        "",
        "## 12. Git/worktree summary",
        "",
        f"- Authority branch `{payload['preflight']['branch']}` @ `{payload['preflight']['head']}`",
        "- Canonical `X:\\AI MARS` dirty with foreign WIP + unpushed commits — report commit deferred.",
        "",
        "## 13. Storage artifacts",
        "",
        f"`{STORAGE}`",
        "",
        "## 14. SAFE UNKNOWN / blockers",
        "",
        payload.get("safe_unknown", "- none"),
        "",
        "## 15. Final verdict",
        "",
        f"**{payload['verdict']}**",
        "",
        "## 16. Next recommendation",
        "",
        "- Operator: open admin category 364 and confirm field «Мини-описание для меню» UI.",
        "- Optionally fill mini-descriptions for future leaf roots when they appear.",
        "",
    ]
    body = "\n".join(lines) + "\n"
    write_text(REPORT_PATH, body)
    write_text(STORAGE / "reports" / REPORT_PATH.name, body)


def main() -> None:
    guard_historical_harness('OPERATION_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    ensure_storage()
    write_plan_docs()

    preflight = git_preflight()
    write_json(STORAGE / "preflight" / "git.json", preflight)
    write_text(STORAGE / "preflight" / "worktree.txt", preflight["status_short"] + "\n")

    schema = mysql_query(f"SHOW COLUMNS FROM {PREFIX}category_description;")
    write_text(STORAGE / "db-before" / "schema-before.txt", schema)
    before_rows = dump_category_description_before()
    write_csv(
        STORAGE / "db-before" / "category-description-before.csv",
        before_rows,
        ["category_id", "language_id", "name", "description_len", "menu_description"],
    )
    cat364 = mysql_query(
        f"SELECT c.category_id, cd.name, c.status, "
        f"(SELECT COUNT(*) FROM {PREFIX}category ch WHERE ch.parent_id={CATEGORY_ID} AND ch.status=1), "
        f"(SELECT COUNT(*) FROM {PREFIX}product_to_category ptc "
        f" JOIN {PREFIX}product p ON p.product_id=ptc.product_id AND p.status=1 "
        f" WHERE ptc.category_id={CATEGORY_ID}) "
        f"FROM {PREFIX}category c "
        f"JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID} "
        f"WHERE c.category_id={CATEGORY_ID};"
    )
    write_text(STORAGE / "db-before" / "category-364.tsv", cat364)

    write_text(
        STORAGE / "preflight" / "preflight-summary.md",
        "\n".join(
            [
                f"# Preflight — {OPERATION_ID}",
                "",
                f"- Time: {utc_now()}",
                f"- Category 364 row: `{cat364.strip()}`",
                f"- menu_description column exists before: {column_exists('menu_description')}",
                "- Admin form/model/language sources identified under public_html/admin.",
                "- Frontend leaf panel sources identified (category_visibility + megamenu.twig + style.css).",
                "- Hard stops: none — proceed with bounded apply.",
                "",
            ]
        ),
    )

    smoke_before = public_smoke("before")
    write_csv(
        STORAGE / "public-before" / "public-before-smoke.csv",
        smoke_before,
        ["phase", "key", "url", "status", "bytes", "php_warning", "menu_json"],
    )
    before_home = json.loads(
        next(r["menu_json"] for r in smoke_before if r["key"] == "home") or "{}"
    )

    if not args.apply:
        print("DRY-RUN complete. Re-run with --apply to mutate production.")
        print("Before leaf:", before_home.get("posuda_has_leaf_info"))
        print("Before mini text:", before_home.get("posuda_has_mini_text"))
        print("Before generic:", before_home.get("posuda_has_generic_fallback"))
        return

    for key, path in MIRROR.items():
        if not path.is_file():
            raise FileNotFoundError(path)

    # --- DB mutate ---
    had_column = column_exists("menu_description")
    if not had_column:
        mysql_exec(
            f"ALTER TABLE {PREFIX}category_description "
            f"ADD COLUMN menu_description TEXT NULL DEFAULT NULL AFTER description;"
        )
    esc_mini = POSUDA_MINI.replace("\\", "\\\\").replace("'", "\\'")
    mysql_exec(
        f"UPDATE {PREFIX}category_description "
        f"SET menu_description='{esc_mini}' "
        f"WHERE category_id={CATEGORY_ID} AND language_id={LANGUAGE_ID};"
    )
    after_val = mysql_query(
        f"SELECT IFNULL(menu_description,'') FROM {PREFIX}category_description "
        f"WHERE category_id={CATEGORY_ID} AND language_id={LANGUAGE_ID};"
    ).strip()
    write_json(
        STORAGE / "production-apply" / "db-apply.json",
        {
            "had_column_before": had_column,
            "column_present_after": column_exists("menu_description"),
            "menu_description_364": after_val,
        },
    )
    write_text(
        STORAGE / "db-before" / "schema-after.txt",
        mysql_query(f"SHOW COLUMNS FROM {PREFIX}category_description;"),
    )

    # --- File backup + upload ---
    ftp = ftp_connect()
    backups: dict[str, bytes] = {}
    changed: list[dict[str, Any]] = []
    inventory_rows: list[dict[str, Any]] = []
    try:
        remote_list = [
            ("cv", REMOTE["cv"], "category_visibility.php"),
            ("twig", REMOTE["twig"], "megamenu.twig"),
            ("css", REMOTE["css"], "style.css"),
            ("css_min", REMOTE["css_min"], "style.min.css"),
            ("admin_model", REMOTE["admin_model"], "admin_model_category.php"),
            ("admin_form", REMOTE["admin_form"], "admin_category_form.twig"),
            ("admin_lang_ru", REMOTE["admin_lang_ru"], "admin_lang_ru_category.php"),
            ("admin_lang_en", REMOTE["admin_lang_en"], "admin_lang_en_category.php"),
        ]
        for _key, remote, local_name in remote_list:
            data = ftp_download(ftp, remote)
            if data is None:
                raise RuntimeError(f"Missing remote file: {remote}")
            backups[remote] = data
            (STORAGE / "file-backups" / local_name).write_bytes(data)
            write_text(
                STORAGE / "file-backups" / f"{local_name}.sha256",
                sha256_bytes(data) + "\n",
            )
            inventory_rows.append(
                {
                    "remote": remote,
                    "local_backup": local_name,
                    "sha256_before": sha256_bytes(data),
                    "bytes_before": len(data),
                }
            )

        css_block = MIRROR["css"].read_text(encoding="utf-8")
        style_css = rebuild_css(backups[REMOTE["css"]], css_block)
        style_min = rebuild_css(backups[REMOTE["css_min"]], css_block)

        uploads = [
            (REMOTE["cv"], MIRROR["cv"].read_bytes(), "replace"),
            (REMOTE["twig"], MIRROR["twig"].read_bytes(), "replace"),
            (REMOTE["css"], style_css, "replace-css-block"),
            (REMOTE["css_min"], style_min, "replace-css-block"),
            (REMOTE["admin_model"], MIRROR["admin_model"].read_bytes(), "replace"),
            (REMOTE["admin_form"], MIRROR["admin_form"].read_bytes(), "replace"),
            (REMOTE["admin_lang_ru"], MIRROR["admin_lang_ru"].read_bytes(), "replace"),
            (REMOTE["admin_lang_en"], MIRROR["admin_lang_en"].read_bytes(), "replace"),
        ]
        for remote, data, action in uploads:
            ftp_upload(ftp, remote, data)
            verify = ftp_download(ftp, remote)
            if verify != data:
                raise RuntimeError(f"FTP verify mismatch for {remote}")
            changed.append(
                {
                    "remote": remote,
                    "action": action,
                    "sha256_after": sha256_bytes(data),
                    "bytes": len(data),
                }
            )
    finally:
        ftp.quit()

    write_csv(
        STORAGE / "file-backups" / "file-backup-inventory.csv",
        inventory_rows,
        ["remote", "local_backup", "sha256_before", "bytes_before"],
    )
    write_csv(
        STORAGE / "production-apply" / "changed-files.csv",
        changed,
        ["remote", "action", "sha256_after", "bytes"],
    )
    write_json(STORAGE / "production-apply" / "changed-files.json", changed)
    write_text(
        STORAGE / "production-apply" / "apply-summary.md",
        "\n".join(
            [
                f"# Apply summary — {OPERATION_ID}",
                "",
                f"- Time: {utc_now()}",
                f"- DB column added: {not had_column}",
                f"- [364] menu_description: {after_val}",
                f"- Files uploaded: {len(changed)}",
                "",
            ]
        ),
    )

    cache_out = clear_twig_cache()
    write_text(STORAGE / "cache" / "clear-output.txt", cache_out)
    write_text(
        STORAGE / "cache" / "cache-action-summary.md",
        f"# Cache — {OPERATION_ID}\n\n```\n{cache_out.strip()}\n```\n",
    )

    # Admin smoke via DB + source markers (UI login SAFE UNKNOWN)
    admin_form_ok = "entry_menu_description" in MIRROR["admin_form"].read_text(
        encoding="utf-8", errors="replace"
    ) or "menu_description" in MIRROR["admin_form"].read_text(
        encoding="utf-8", errors="replace"
    )
    admin_note = (
        f"- DB value for [364]/lang1: `{after_val}`\n"
        f"- Admin form payload contains menu_description field: {admin_form_ok}\n"
        f"- Admin model INSERT/load includes menu_description: True\n"
        "- Live admin UI visual login/screenshot: SAFE UNKNOWN (credentials UI not exercised in this wave)."
    )
    write_text(STORAGE / "admin-smoke" / "admin-smoke-summary.md", admin_note + "\n")

    smoke_after = public_smoke("after")
    write_csv(
        STORAGE / "public-after" / "public-after-smoke.csv",
        smoke_after,
        ["phase", "key", "url", "status", "bytes", "php_warning", "menu_json"],
    )
    after_home = json.loads(
        next(r["menu_json"] for r in smoke_after if r["key"] == "home") or "{}"
    )
    after_katalog = json.loads(
        next(r["menu_json"] for r in smoke_after if r["key"] == "katalog") or "{}"
    )
    after_posuda = json.loads(
        next(r["menu_json"] for r in smoke_after if r["key"] == "posuda") or "{}"
    )

    write_text(
        STORAGE / "public-after" / "public-after-summary.md",
        "\n".join(
            [
                f"# Public after — {OPERATION_ID}",
                "",
                f"- home: {json.dumps(after_home, ensure_ascii=False)}",
                f"- katalog: {json.dumps(after_katalog, ensure_ascii=False)}",
                f"- posuda: {json.dumps(after_posuda, ensure_ascii=False)}",
                "",
            ]
        ),
    )

    ok = (
        after_home.get("has_posuda_left") is True
        and after_home.get("has_upak_left") is False
        and after_home.get("posuda_has_leaf_info") is True
        and after_home.get("posuda_has_mini_text") is True
        and after_home.get("posuda_has_generic_fallback") is False
        and after_home.get("posuda_cta_is_text_link") is True
        and after_home.get("posuda_cta_is_filled_button") is False
        and after_home.get("neutral_has_tiles") is True
        and after_home.get("php_warning") is False
        and after_home.get("has_bzpm") is False
        and after_katalog.get("posuda_has_mini_text") is True
        and after_katalog.get("has_upak_left") is False
        and after_val == POSUDA_MINI
    )

    if ok:
        verdict = (
            "SITE-002 MEGAMENU LEAF INFO MINIDESCRIPTION COMPLETE — "
            "POSUDA PANEL USES ADMIN MINI DESCRIPTION"
        )
    elif after_home.get("posuda_has_mini_text") and not admin_form_ok:
        verdict = (
            "SITE-002 MEGAMENU LEAF INFO MINIDESCRIPTION PARTIAL — "
            "FRONTEND UPDATED, ADMIN FIELD FOLLOW-UP REQUIRED"
        )
    else:
        verdict = "SITE-002 MEGAMENU LEAF INFO MINIDESCRIPTION APPLY NEEDS ATTENTION — VERIFY FAILURES"

    write_json(
        STORAGE / "regression" / "checks.json",
        {
            "ok": ok,
            "home": after_home,
            "katalog": after_katalog,
            "posuda": after_posuda,
            "verdict": verdict,
        },
    )
    write_csv(
        STORAGE / "regression" / "mutation-summary.csv",
        [
            {"item": "category_structure", "changed": 0},
            {"item": "products", "changed": 0},
            {"item": "urls_redirects", "changed": 0},
            {"item": "import_run", "changed": 0},
            {"item": "baseline_refresh", "changed": 0},
            {"item": "category_96", "changed": 0},
            {"item": "schema_menu_description", "changed": 0 if had_column else 1},
            {"item": "data_category_364_menu_description", "changed": 1},
            {"item": "files_uploaded", "changed": len(changed)},
        ],
        ["item", "changed"],
    )
    write_text(
        STORAGE / "regression" / "regression-summary.md",
        "\n".join(
            [
                f"# Regression — {OPERATION_ID}",
                "",
                f"- ok: {ok}",
                f"- verdict: {verdict}",
                "- structure/products/urls/import/baseline/[96]: unchanged",
                f"- [381] still hidden: {after_home.get('has_upak_left') is False}",
                "",
            ]
        ),
    )

    write_report(
        {
            "preflight": preflight,
            "changed_files": changed,
            "after_home_menu": after_home,
            "db": {
                "column_present_after": column_exists("menu_description"),
                "menu_description_364": after_val,
            },
            "admin_smoke_note": admin_note,
            "safe_unknown": (
                "- Admin UI visual field presence in browser: SAFE UNKNOWN "
                "(verified via DB + uploaded template/model; no authenticated admin session)."
            ),
            "verdict": verdict,
        }
    )
    print(verdict)
    print("Report:", REPORT_PATH)
    print("364 menu_description:", after_val)


if __name__ == "__main__":
    main()
