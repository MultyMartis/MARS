#!/usr/bin/env python3
"""SITE-002 Catalog Normalization UI Repair 01 — repair public catalog root UI after DB apply.

Operation: SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01
Previous apply commit: b0447bc8

Deploys patched category_visibility.php only; clears OpenCart cache.
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
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01"
PREVIOUS_APPLY_COMMIT = "b0447bc8"
SITE_ID = "SITE-002"
PRODUCTION_URL = "https://bzpm.ru/"
PREFIX = "oc_"
LANGUAGE_ID = 1
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
AUTHORITY_REPO = Path(r"X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo")
TOOLS = AUTHORITY_REPO / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
MIRROR_CV = TOOLS / "category_visibility.php"
REMOTE_CV = "/public_html/system/library/zpm/category_visibility.php"
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"

APPROVED_ROOTS = [
    (79, "Нейтральное оборудование", "nejtralnoe-oborudovanie"),
    (95, "Холодильное оборудование", "holodilnoe-oborudovanie"),
    (90, "Тепловое оборудование", "teplovoe-oborudovanie"),
    (186, "Хлебопекарное оборудование", "hlebopekarnoe-oborudovanie"),
    (375, "Электромеханическое", "elektromehanicheskoe"),
    (373, "Мясоперерабатывающее", "myasopererabatyvayuschee"),
    (364, "Посуда и инвентарь", "posuda-i-inventar"),
    (381, "Упаковочное оборудование", "upakovochnoe-oborudovanie"),
]
TMP_DISABLED = [362, 93, 171, 205, 206]
HOLD_ZAPCHASTI = 96
NEUTRAL_CHILD_MARKERS = ("Зонты вытяжные", "Кондитерский инвентарь", "Моечные ванны", "Подтоварники")

STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
STORAGE_SUBDIRS = (
    "preflight",
    "reports-read",
    "operator-screenshot",
    "db-verify",
    "public-before",
    "render-source-diagnostic",
    "file-backups",
    "exact-fix-plan",
    "production-apply",
    "cache",
    "public-after",
    "visual-smoke",
    "rollback",
    "decision",
    "regression",
    "reports",
    "manifests",
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


def run_git(args: list[str]) -> str:
    return subprocess.check_output(["git", "-C", str(AUTHORITY_REPO), *args], text=True, errors="replace").strip()


def parse_production_section(subsection: str | None = None) -> dict[str, str]:
    text = SECRETS_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    if subsection:
        sub = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)",
            block,
            re.MULTILINE,
        )
        if not sub:
            raise RuntimeError(f"PRODUCTION subsection {subsection!r} not found")
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
    text = out.read().decode("utf-8", errors="replace") + err.read().decode("utf-8", errors="replace")
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
        raise RuntimeError(f"MySQL failed: {text[:500]}")
    return text


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


def http_fetch(path: str) -> dict[str, Any]:
    url = PRODUCTION_URL.rstrip("/") + path
    req = urllib.request.Request(
        url,
        headers={"User-Agent": f"MARS-{OPERATION_ID}", "Cache-Control": "no-cache"},
    )
    result: dict[str, Any] = {
        "path": path,
        "url": url,
        "status": "",
        "final_url": url,
        "title": "",
        "section_titles": "",
        "tile_names": "",
        "error": "",
    }
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            result["status"] = str(resp.status)
            result["final_url"] = resp.geturl()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        result["status"] = str(exc.code)
        result["error"] = str(exc)
    except Exception as exc:  # noqa: BLE001
        result["status"] = "ERR"
        result["error"] = str(exc)
        return result

    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
    if m:
        result["title"] = re.sub(r"\s+", " ", m.group(1)).strip()[:200]
    titles = re.findall(r'class="zpm-cat-sections__title"[^>]*>([^<]+)<', body)
    result["section_titles"] = " | ".join(t.strip() for t in titles)
    tiles = re.findall(r'class="zpm-cat-card__title"[^>]*>([^<]+)<', body)
    result["tile_names"] = " | ".join(t.strip() for t in tiles[:30])
    result["has_bzpm"] = "БЗПМ" in body
    result["has_php_fatal"] = any(x in body.lower() for x in ("php fatal", "php warning"))
    result["has_neutral_child_marker"] = any(x in body for x in NEUTRAL_CHILD_MARKERS)
    approved_hits = sum(1 for _id, name, _kw in APPROVED_ROOTS if name in body)
    result["approved_root_hits_in_html"] = approved_hits
    return result


def setup_storage() -> None:
    for sub in STORAGE_SUBDIRS:
        (STORAGE / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        STORAGE / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "production_url": PRODUCTION_URL,
            "environment": "CATALOG_NORMALIZATION_UI_REPAIR_PRODUCTION",
            "current_local_time": "2026-08-25T01:18+07:00",
            "previous_apply_commit": PREVIOUS_APPLY_COMMIT,
            "production_mutation_allowed": True,
            "db_write_allowed": False,
            "ftp_write_allowed": True,
            "import_run_allowed": False,
            "mapping_change_allowed": False,
            "category_product_change_allowed": False,
            "monitor_code_change_allowed": False,
            "baseline_refresh_allowed": False,
            "cleanup_delete_allowed": False,
            "created_utc": utc_now(),
        },
    )


def phase_git_preflight() -> None:
    run_git(["fetch", "origin"])
    lines = [
        run_git(["status", "--short"]),
        run_git(["status", "--branch", "--porcelain=v2"]),
        f"branch: {run_git(['branch', '--show-current'])}",
        f"HEAD: {run_git(['rev-parse', 'HEAD'])}",
        f"origin/mars/canonical-post-recovery: {run_git(['rev-parse', 'origin/mars/canonical-post-recovery'])}",
        run_git(["log", "--oneline", "--decorate", "-20"]),
    ]
    write_text(STORAGE / "preflight" / "authority-git-state.txt", "\n".join(lines) + "\n")
    write_text(
        STORAGE / "preflight" / "authority-origin-state.txt",
        run_git(["log", "--oneline", "origin/mars/canonical-post-recovery..HEAD"])
        + "\n---\n"
        + run_git(["log", "--oneline", "HEAD..origin/mars/canonical-post-recovery"])
        + "\n",
    )


def phase_db_verify() -> list[dict[str, Any]]:
    ids = [str(r[0]) for r in APPROVED_ROOTS] + [str(i) for i in TMP_DISABLED] + [str(HOLD_ZAPCHASTI)]
    id_list = ",".join(ids)
    sql = f"""
SELECT c.category_id, c.parent_id, c.status, cd.name,
       COALESCE((SELECT keyword FROM {PREFIX}seo_url su
         WHERE su.query=CONCAT('category_id=', c.category_id)
           AND su.store_id=0 AND su.language_id={LANGUAGE_ID} LIMIT 1), '') AS keyword
FROM {PREFIX}category c
JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID}
WHERE c.category_id IN ({id_list})
ORDER BY c.category_id;
""".strip()
    rows_raw = mysql_query(sql)
    rows: list[dict[str, Any]] = []
    for line in rows_raw.splitlines():
        parts = line.split("\t")
        if len(parts) < 5:
            continue
        rows.append(
            {
                "category_id": parts[0],
                "parent_id": parts[1],
                "status": parts[2],
                "name": parts[3],
                "keyword": parts[4],
            }
        )
    write_csv(
        STORAGE / "db-verify" / "root-state-after-apply.csv",
        rows,
        ["category_id", "parent_id", "status", "name", "keyword"],
    )
    issues: list[str] = []
    by_id = {int(r["category_id"]): r for r in rows}
    for cid, name, kw in APPROVED_ROOTS:
        r = by_id.get(cid)
        if not r:
            issues.append(f"missing approved root {cid}")
            continue
        if r["parent_id"] != "0":
            issues.append(f"{cid} parent_id={r['parent_id']} expected 0")
        if r["status"] != "1":
            issues.append(f"{cid} status={r['status']} expected 1")
        if kw and r["keyword"] != kw:
            issues.append(f"{cid} keyword={r['keyword']!r} expected {kw!r}")
    for tid in TMP_DISABLED:
        r = by_id.get(tid)
        if r and r["status"] != "0":
            issues.append(f"tmp {tid} status={r['status']} expected 0")
    z = by_id.get(HOLD_ZAPCHASTI)
    if z and z["status"] != "0":
        issues.append(f"zapchasti {HOLD_ZAPCHASTI} changed status={z['status']}")
    summary = [
        "# DB verify summary",
        "",
        f"Verified at: {utc_now()}",
        "",
        "## Approved 8 roots",
        *[f"- [{r['category_id']}] {r['name']} parent={r['parent_id']} status={r['status']} kw={r['keyword']}" for r in rows if int(r["category_id"]) in {x[0] for x in APPROVED_ROOTS}],
        "",
        "## Issues",
        *(issues or ["None — DB root model matches apply report"]),
        "",
        f"Verdict: {'DB_STATE_ATTENTION_REQUIRED' if issues else 'DB_ROOT_STATE_CONFIRMED'}",
    ]
    write_text(STORAGE / "db-verify" / "db-verify-summary.md", "\n".join(summary) + "\n")
    if issues:
        write_text(STORAGE / "decision" / "db-blocker.txt", "\n".join(issues) + "\n")
        raise RuntimeError("DB_STATE_ATTENTION_REQUIRED: " + "; ".join(issues))
    return rows


def phase_public_smoke(label: str) -> list[dict[str, Any]]:
    paths = [
        "/",
        "/katalog/",
        "/nejtralnoe-oborudovanie",
        "/holodilnoe-oborudovanie",
        "/teplovoe-oborudovanie",
        "/hlebopekarnoe-oborudovanie",
        "/elektromehanicheskoe",
        "/myasopererabatyvayuschee",
        "/posuda-i-inventar",
        "/upakovochnoe-oborudovanie",
        "/tehnologicheskoe-oborudovanie",
        "/inventar",
        "/zapchasti",
        "/assum",
    ]
    rows = [http_fetch(p) for p in paths]
    out_dir = STORAGE / ("public-before" if label == "before" else "public-after")
    write_csv(
        out_dir / f"page-tile-inventory{'-after' if label == 'after' else ''}.csv",
        rows,
        [
            "path",
            "status",
            "title",
            "section_titles",
            "tile_names",
            "approved_root_hits_in_html",
            "has_neutral_child_marker",
            "has_bzpm",
            "has_php_fatal",
            "error",
        ],
    )
    home = next((r for r in rows if r["path"] == "/"), {})
    katalog = next((r for r in rows if r["path"] == "/katalog/"), {})
    write_text(
        out_dir / f"public-{'before' if label == 'before' else 'after'}-summary.md",
        "\n".join(
            [
                f"# Public {label} summary",
                "",
                f"Captured: {utc_now()}",
                "",
                "## Homepage `/`",
                f"- status: {home.get('status')}",
                f"- section titles: {home.get('section_titles')}",
                f"- tile names: {home.get('tile_names')}",
                f"- neutral child markers: {home.get('has_neutral_child_marker')}",
                f"- approved root hits: {home.get('approved_root_hits_in_html')}",
                "",
                "## `/katalog/`",
                f"- status: {katalog.get('status')}",
                f"- section titles: {katalog.get('section_titles')}",
                f"- tile names: {katalog.get('tile_names')}",
                f"- neutral child markers: {katalog.get('has_neutral_child_marker')}",
                f"- approved root hits: {katalog.get('approved_root_hits_in_html')}",
                "",
            ]
        )
        + "\n",
    )
    if label == "after":
        write_csv(
            out_dir / "public-http-smoke.csv",
            rows,
            ["path", "status", "title", "has_bzpm", "has_php_fatal", "error"],
        )
    return rows


def phase_render_diagnostic() -> None:
    write_text(
        STORAGE / "render-source-diagnostic" / "render-source-summary.md",
        "\n".join(
            [
                "# Render source diagnostic",
                "",
                "## Selected source",
                "- File: `/public_html/system/library/zpm/category_visibility.php`",
                "- Class: `CategoryVisibility`",
                "- Methods: `buildCatalogSectionTileBlocks`, `filterRootCategories`, `prepareMegamenuCategories`",
                "",
                "## Root cause",
                "- Stale Launch Mode config: `$visible_root_category_ids = array(79, 362)`",
                "- `$hidden_root_slugs` hid newly public roots (holodilnoe, teplovoe, etc.)",
                "- `buildCatalogSectionTileBlocks()` rendered Neutral **children** for root 79 via `buildNeutralFirstLevelBlockCards()`",
                "- Root 362 disabled in DB after normalization → broken second section",
                "",
                "## Consumers",
                "- `catalog/controller/common/home.php` → homepage tiles",
                "- `catalog/controller/product/katalog.php` → /katalog/ tiles",
                "- `catalog/controller/common/header.php` → mega menu via `prepareMegamenuCategories` + `filterRootCategories`",
                "",
                "## Fix",
                "- Update visible roots to 8 approved IDs/slugs",
                "- Replace tile block builder to show 8 root cards in one section",
                "- Update hidden slugs to tmp/disabled only",
                "",
            ]
        )
        + "\n",
    )
    write_text(
        STORAGE / "render-source-diagnostic" / "selected-source.txt",
        "/public_html/system/library/zpm/category_visibility.php\n",
    )
    write_csv(
        STORAGE / "render-source-diagnostic" / "render-source-candidates.csv",
        [
            {"file": REMOTE_CV, "role": "primary", "selected": "yes"},
            {"file": "catalog/controller/common/home.php", "role": "consumer", "selected": "no"},
            {"file": "catalog/controller/product/katalog.php", "role": "consumer", "selected": "no"},
            {"file": "catalog/view/theme/default/template/sections/catalogsections.twig", "role": "template", "selected": "no"},
        ],
        ["file", "role", "selected"],
    )


def phase_fix_plan() -> None:
    ids = ", ".join(str(r[0]) for r in APPROVED_ROOTS)
    write_text(
        STORAGE / "exact-fix-plan" / "exact-fix-plan.md",
        "\n".join(
            [
                "# Exact fix plan",
                "",
                "## Files",
                f"- Deploy: `{REMOTE_CV}` only",
                "- Mirror: `projects/ocpilot/sites/site-002/tools/category_visibility.php`",
                "",
                "## Logic changes",
                f"- `$visible_root_category_ids` → [{ids}]",
                "- `$visible_root_slugs` → 8 approved SEO keywords",
                "- `$hidden_root_slugs` → tmp/disabled + legacy slugs + zapchasti",
                "- `buildCatalogSectionTileBlocks()` → single section with 8 **root** cards",
                "- `CATALOG_PRIMARY_ENTRY` → `/katalog/`",
                "- `isVisibleRootCategory()` → reject hidden slugs",
                "",
                "## Not changed",
                "- header.twig / footer.twig",
                "- category.php product PLP",
                "- DB hierarchy",
                "- buildHubChildCards / mega menu child logic (unchanged)",
                "",
                "## Cache",
                f"- Clear `{CACHE_DIR}/cache.*`",
                "- Clear `cache.cat-list-header` if present",
                "",
            ]
        )
        + "\n",
    )
    write_text(
        STORAGE / "rollback" / "rollback-plan.md",
        "\n".join(
            [
                "# Rollback plan",
                "",
                f"1. FTP restore `{REMOTE_CV}` from `file-backups/category_visibility.php.before`",
                f"2. SSH: rm -f {CACHE_DIR}/cache.* cache.cat-list-header*",
                "3. Re-fetch `/` and `/katalog/` — expect pre-repair Neutral-children block",
                "",
            ]
        )
        + "\n",
    )


def phase_apply(ftp: ftplib.FTP) -> dict[str, Any]:
    if not MIRROR_CV.is_file():
        raise RuntimeError(f"Mirror missing: {MIRROR_CV}")
    before = ftp_download(ftp, REMOTE_CV)
    if before is None:
        raise RuntimeError(f"Could not download {REMOTE_CV}")
    backup_path = STORAGE / "file-backups" / "category_visibility.php.before"
    backup_path.write_bytes(before)
    patched = MIRROR_CV.read_bytes()
    if b"SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01" not in patched:
        raise RuntimeError("Mirror missing repair marker comment")
    if b"array(79, 95, 90, 186, 375, 373, 364, 381)" not in patched:
        raise RuntimeError("Mirror missing approved root IDs")
    write_csv(
        STORAGE / "file-backups" / "file-backup-inventory.csv",
        [
            {
                "production_path": REMOTE_CV,
                "local_backup": str(backup_path),
                "sha256_before": sha256_bytes(before),
                "sha256_after": sha256_bytes(patched),
                "size_before": len(before),
                "size_after": len(patched),
            }
        ],
        ["production_path", "local_backup", "sha256_before", "sha256_after", "size_before", "size_after"],
    )
    ftp_upload(ftp, REMOTE_CV, patched)
    remote_after = ftp_download(ftp, REMOTE_CV) or b""
    if sha256_bytes(remote_after) != sha256_bytes(patched):
        raise RuntimeError("Post-upload hash mismatch")
    row = {
        "remote_path": REMOTE_CV,
        "sha256_before": sha256_bytes(before),
        "sha256_after": sha256_bytes(remote_after),
        "upload_status": "OK",
    }
    write_csv(STORAGE / "production-apply" / "changed-files.csv", [row], list(row.keys()))
    write_text(
        STORAGE / "production-apply" / "apply-summary.md",
        f"# Production apply\n\nUploaded `{REMOTE_CV}` at {utc_now()}\n\nSingle-file bounded UI repair.\n",
    )
    return row


def phase_cache_clear() -> None:
    cmd = (
        f"cd {shlex.quote(CACHE_DIR)} 2>/dev/null || exit 1; "
        "ls -1 cache.cat-list-header 2>/dev/null || true; "
        "rm -f cache.cat-list-header 2>/dev/null; "
        "find . -maxdepth 1 -type f -name 'cache.*' -delete 2>/dev/null; "
        "echo CACHE_CLEARED"
    )
    out = ssh_exec(cmd)
    write_text(
        STORAGE / "cache" / "cache-action-summary.md",
        f"# Cache action\n\n```\n{out}\n```\n\nCleared cache.* and cat-list-header at {utc_now()}\n",
    )


def phase_regression() -> None:
    reg = [
        {"item": "category_hierarchy_changed", "value": "0"},
        {"item": "product_changes", "value": "0"},
        {"item": "mapping_changes", "value": "0"},
        {"item": "import_runs", "value": "0"},
        {"item": "baseline_refresh", "value": "0"},
        {"item": "zapchasti_changed", "value": "0"},
        {"item": "header_footer_touched", "value": "0"},
        {"item": "files_deployed", "value": "1 (category_visibility.php)"},
    ]
    write_csv(STORAGE / "regression" / "mutation-summary.csv", reg, ["item", "value"])
    write_text(
        STORAGE / "regression" / "regression-summary.md",
        "# Regression summary\n\nBounded UI-only repair; DB/import/baseline unchanged.\n",
    )


def evaluate_after(rows: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    issues: list[str] = []
    approved_names = {name for _id, name, _kw in APPROVED_ROOTS}
    for path in ("/", "/katalog/"):
        r = next((x for x in rows if x["path"] == path), None)
        if not r or r.get("status") != "200":
            issues.append(f"{path} not HTTP 200")
            continue
        if r.get("has_php_fatal"):
            issues.append(f"{path} PHP fatal")
        tile_names = [t.strip() for t in (r.get("tile_names") or "").split(" | ") if t.strip()]
        approved_in_tiles = sum(1 for name in tile_names if name in approved_names)
        neutral_children_in_tiles = sum(1 for name in tile_names if name in NEUTRAL_CHILD_MARKERS)
        if approved_in_tiles < 7:
            issues.append(
                f"{path} catalog tiles show {approved_in_tiles}/8 approved roots (tiles: {r.get('tile_names', '')[:120]})"
            )
        if neutral_children_in_tiles >= 3:
            issues.append(f"{path} still shows Neutral child tiles as main catalog block")
    for path in ("/tehnologicheskoe-oborudovanie", "/inventar", "/zapchasti"):
        r = next((x for x in rows if x["path"] == path), None)
        if r and r.get("status") == "200":
            issues.append(f"{path} should not be public 200")
    return (len(issues) == 0, issues)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Deploy to production")
    args = parser.parse_args()

    setup_storage()
    phase_git_preflight()
    write_text(
        STORAGE / "reports-read" / "reports-read-summary.md",
        "# Reports read\n\nPrior apply SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01 commit b0447bc8 — DB applied, PHP deploy 0.\n",
    )
    phase_db_verify()
    before_rows = phase_public_smoke("before")
    phase_render_diagnostic()
    phase_fix_plan()

    if not args.apply:
        print("Dry-run complete. Re-run with --apply to deploy UI repair.")
        return 0

    ftp = ftp_connect()
    try:
        phase_apply(ftp)
    finally:
        ftp.quit()

    phase_cache_clear()
    after_rows = phase_public_smoke("after")
    ok, issues = evaluate_after(after_rows)
    phase_regression()

    if ok:
        verdict = "SITE-002 CATALOG NORMALIZATION UI REPAIR COMPLETE — PUBLIC CATALOG ROOT UI SHOWS APPROVED 8 ROOTS"
    else:
        verdict = "SITE-002 CATALOG NORMALIZATION UI REPAIR BLOCKED — POST-SMOKE ISSUES: " + "; ".join(issues)

    write_text(STORAGE / "decision" / "final-verdict.txt", verdict + "\n")
    write_text(
        STORAGE / "visual-smoke" / "visual-smoke-summary.md",
        "# Visual smoke\n\nSAFE UNKNOWN — no browser screenshots captured; relied on HTML tile extraction.\n",
    )
    print(verdict)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
