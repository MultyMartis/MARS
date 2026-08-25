#!/usr/bin/env python3
"""SITE-002 — mega menu hide disabled roots + Posuda leaf hub product PLP fallback.

Operation: SITE-002-PROD-MEGAMENU-AND-POSUDA-PLP-REPAIR-01
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

OPERATION_ID = "SITE-002-PROD-MEGAMENU-AND-POSUDA-PLP-REPAIR-01"
PRODUCTION_URL = "https://bzpm.ru/"
PREFIX = "oc_"
LANGUAGE_ID = 1
STORE_ID = 0
TARGET_IDS = (364, 381, 96)
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
AUTHORITY_REPO = Path(r"X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo")
TOOLS = AUTHORITY_REPO / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
MIRROR_CV = TOOLS / "category_visibility.php"
MIRROR_CATEGORY = TOOLS / "catalog_controller_product_category-SITE-002-PROD-CATALOG-TILE-BLOCKS-AUTOMATION-01.php"
REMOTE_CV = "/public_html/system/library/zpm/category_visibility.php"
REMOTE_CATEGORY = "/public_html/catalog/controller/product/category.php"
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"
REPORT_PATH = AUTHORITY_REPO / "projects/ocpilot/sites/site-002/reports/SITE-002-PROD-MEGAMENU-AND-POSUDA-PLP-REPAIR-01.md"

STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
STORAGE_SUBDIRS = (
    "preflight",
    "db-before",
    "public-before",
    "render-source",
    "exact-fix-plan",
    "file-backups",
    "production-apply",
    "cache",
    "public-after",
    "visual-smoke",
    "rollback",
    "regression",
    "reports",
    "logs",
)

TMP_DISABLED_MARKERS = (
    "tmp Технологическое",
    "tmp Инвентарь",
    "tmp Барное",
    "tmp Посудомоечные",
    "tmp Вентиляционное",
    "tmp-tehnologicheskoe",
    "tmp-inventar",
    "tmp-barnoe",
    "tmp-posudomoechnye",
    "tmp-ventilyacionnoe",
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


def count_product_cards(html: str) -> int:
    patterns = (
        r'class="[^"]*product-layout[^"]*"',
        r'class="[^"]*product-thumb[^"]*"',
        r'data-product-id=',
        r'product/product&product_id=',
    )
    counts = [len(re.findall(p, html, re.I)) for p in patterns]
    return max(counts) if counts else 0


def has_php_warning(html: str) -> bool:
    return bool(re.search(r"(Fatal error|Warning:|Notice:|Parse error)", html, re.I))


def megamenu_contains(html: str, needle: str) -> bool:
    # megamenu block heuristic
    m = re.search(r'class="[^"]*megamenu[^"]*"[\s\S]*?</(?:div|nav|section)>', html, re.I)
    block = m.group(0) if m else html
    return needle.lower() in block.lower()


def ensure_storage() -> None:
    for sub in STORAGE_SUBDIRS:
        (STORAGE / sub).mkdir(parents=True, exist_ok=True)


def git_preflight() -> dict[str, str]:
    def run(args: list[str]) -> str:
        return subprocess.check_output(args, cwd=AUTHORITY_REPO, text=True, stderr=subprocess.STDOUT).strip()

    return {
        "branch": run(["git", "branch", "--show-current"]),
        "head": run(["git", "rev-parse", "--short", "HEAD"]),
        "status_short": run(["git", "status", "--short"]) or "(clean except listed)",
        "origin_head": run(["git", "rev-parse", "--short", "origin/mars/canonical-post-recovery"]),
    }


def db_category_snapshot(cat_id: int) -> dict[str, Any]:
    sql = f"""
SELECT c.category_id, cd.name, c.parent_id, c.status, su.keyword,
       (SELECT COUNT(*) FROM {PREFIX}product_to_category ptc
          JOIN {PREFIX}product p ON p.product_id=ptc.product_id
         WHERE ptc.category_id=c.category_id AND p.status=1) AS direct_enabled,
       (SELECT COUNT(*) FROM {PREFIX}category ch WHERE ch.parent_id=c.category_id AND ch.status=1) AS active_children
FROM {PREFIX}category c
JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID}
LEFT JOIN {PREFIX}seo_url su ON su.query=CONCAT('category_id=', c.category_id) AND su.store_id={STORE_ID} AND su.language_id={LANGUAGE_ID}
WHERE c.category_id={cat_id};
"""
    rows = parse_tsv(mysql_query(sql))
    if not rows:
        return {"category_id": cat_id, "missing": True}
    r = rows[0]
    keys = ["category_id", "name", "parent_id", "status", "keyword", "direct_enabled", "active_children"]
    return dict(zip(keys, r))


def public_smoke(label: str) -> list[dict[str, Any]]:
    urls = [
        ("home", PRODUCTION_URL),
        ("katalog", PRODUCTION_URL + "katalog/"),
        ("posuda", PRODUCTION_URL + "posuda-i-inventar"),
        ("upak", PRODUCTION_URL + "upakovochnoe-oborudovanie"),
        ("zapchasti", PRODUCTION_URL + "zapchasti"),
    ]
    rows: list[dict[str, Any]] = []
    for key, url in urls:
        resp = fetch_url(url)
        body = resp["body"]
        rows.append(
            {
                "phase": label,
                "key": key,
                "url": url,
                "http_status": resp["status"],
                "product_cards": count_product_cards(body),
                "megamenu_upak_visible": megamenu_contains(body, "Упаковочное оборудование"),
                "megamenu_posuda_visible": megamenu_contains(body, "Посуда и инвентарь"),
                "tmp_marker_visible": any(m.lower() in body.lower() for m in TMP_DISABLED_MARKERS),
                "php_warning": has_php_warning(body),
            }
        )
    return rows


def phase_docs() -> None:
    write_text(
        STORAGE / "render-source" / "render-source-summary.md",
        "\n".join(
            [
                "# Render source diagnostic",
                "",
                "## Mega menu",
                "- Production: `/public_html/catalog/controller/common/header.php`",
                "- Library: `/public_html/system/library/zpm/category_visibility.php`",
                "- Flow: `cat-list-header` cache → `prepareMegamenuCategories()` → `filterRootCategories()`",
                "- Root cause: `isVisibleRootCategory()` whitelisted ID 381 without DB `status` gate; stale cache could retain disabled root.",
                "",
                "## Posuda PLP",
                "- Production: `/public_html/catalog/controller/product/category.php`",
                "- `$is_hub = isSectionHubCategory(364)` suppresses product query when hub has zero child cards.",
                "- `[364]` is section hub with 0 child categories and 6 direct enabled products.",
                "",
                "## Fix targets (mirror in tools/)",
                f"- `{MIRROR_CV.name}`",
                f"- `{MIRROR_CATEGORY.name}`",
                "",
            ]
        )
        + "\n",
    )
    write_text(
        STORAGE / "exact-fix-plan" / "exact-fix-plan.md",
        "\n".join(
            [
                "# Exact fix plan",
                "",
                "## Mega menu",
                "1. `isRootCategoryEnabled()` — DB status=1 check",
                "2. `isVisibleRootCategory()` — reject when `status` field != 1",
                "3. `prepareMegamenuCategories()` — skip/unset disabled roots before child rebuild",
                "4. Clear `cache.cat-list-header` + `cache.*`",
                "",
                "## Posuda leaf hub fallback",
                "1. `shouldRenderAsSectionHub()` — hub only if child cards exist OR no direct products",
                "2. `category.php` — use `shouldRenderAsSectionHub()` instead of `isSectionHubCategory()`",
                "",
                "## Not changed",
                "- DB / products / hierarchy / import",
                "- header.twig / footer.twig",
                "- Category 381 remains status=0",
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
                f"2. FTP restore `{REMOTE_CATEGORY}` from `file-backups/category.php.before`",
                f"3. SSH: rm -f {CACHE_DIR}/cache.* cache.cat-list-header*",
                "4. Re-verify mega menu shows prior behavior and Posuda PLP empty hub",
                "",
            ]
        )
        + "\n",
    )


def phase_apply(ftp: ftplib.FTP) -> list[dict[str, Any]]:
    deploys = [
        (REMOTE_CV, MIRROR_CV, "category_visibility.php.before"),
        (REMOTE_CATEGORY, MIRROR_CATEGORY, "category.php.before"),
    ]
    if not MIRROR_CV.is_file() or not MIRROR_CATEGORY.is_file():
        raise RuntimeError("Mirror PHP files missing in tools/")
    if b"SITE-002-PROD-MEGAMENU-AND-POSUDA-PLP-REPAIR-01" not in MIRROR_CV.read_bytes():
        raise RuntimeError("category_visibility.php mirror missing repair marker")
    if b"shouldRenderAsSectionHub" not in MIRROR_CATEGORY.read_bytes():
        raise RuntimeError("category.php mirror missing shouldRenderAsSectionHub call")

    inventory: list[dict[str, Any]] = []
    changed: list[dict[str, Any]] = []

    for remote, mirror, backup_name in deploys:
        before = ftp_download(ftp, remote)
        if before is None:
            raise RuntimeError(f"Could not download {remote}")
        backup_path = STORAGE / "file-backups" / backup_name
        backup_path.write_bytes(before)
        patched = mirror.read_bytes()
        inventory.append(
            {
                "production_path": remote,
                "local_backup": str(backup_path),
                "sha256_before": sha256_bytes(before),
                "sha256_after": sha256_bytes(patched),
                "size_before": len(before),
                "size_after": len(patched),
            }
        )
        ftp_upload(ftp, remote, patched)
        remote_after = ftp_download(ftp, remote) or b""
        if sha256_bytes(remote_after) != sha256_bytes(patched):
            raise RuntimeError(f"Post-upload hash mismatch for {remote}")
        changed.append(
            {
                "remote_path": remote,
                "mirror_path": str(mirror),
                "sha256_before": sha256_bytes(before),
                "sha256_after": sha256_bytes(remote_after),
                "upload_status": "OK",
            }
        )

    write_csv(
        STORAGE / "file-backups" / "file-backup-inventory.csv",
        inventory,
        ["production_path", "local_backup", "sha256_before", "sha256_after", "size_before", "size_after"],
    )
    write_csv(
        STORAGE / "production-apply" / "changed-files.csv",
        changed,
        ["remote_path", "mirror_path", "sha256_before", "sha256_after", "upload_status"],
    )
    write_text(
        STORAGE / "production-apply" / "apply-summary.md",
        f"# Production apply\n\nUploaded 2 PHP files at {utc_now()}\n\nNo DB changes.\n",
    )
    return changed


def phase_cache_clear() -> str:
    cmd = (
        f"cd {shlex.quote(CACHE_DIR)} 2>/dev/null || exit 1; "
        "ls -1 cache.cat-list-header 2>/dev/null || true; "
        "rm -f cache.cat-list-header 2>/dev/null; "
        "find . -maxdepth 1 -type f -name 'cache.*' -delete 2>/dev/null; "
        "echo CACHE_CLEARED"
    )
    out = ssh_exec(cmd)
    write_text(STORAGE / "cache" / "cache-action-summary.md", f"# Cache action\n\n```\n{out}\n```\n")
    return out


def build_report(
    git: dict[str, str],
    db_rows: list[dict[str, Any]],
    before: list[dict[str, Any]],
    after: list[dict[str, Any]],
    applied: bool,
    verdict: str,
) -> None:
    home_b = next(r for r in before if r["key"] == "home")
    home_a = next(r for r in after if r["key"] == "home")
    pos_b = next(r for r in before if r["key"] == "posuda")
    pos_a = next(r for r in after if r["key"] == "posuda")
    upak_a = next(r for r in after if r["key"] == "upak")

    text = "\n".join(
        [
            f"# SITE-002 — {OPERATION_ID}",
            "",
            f"Generated: {utc_now()}",
            "",
            "## 1. Scope",
            "Bounded PHP repair: mega menu hides status=0 roots; Posuda leaf section-hub falls back to product PLP.",
            "",
            "## 2. Operator issue",
            "After empty-category check, `[381]` still appeared in mega menu; `[364]` PLP empty despite 6 direct products.",
            "",
            "## 3. Boundary",
            "No DB/product/hierarchy/import changes. header.twig/footer.twig not touched.",
            "",
            "## 4. DB before",
            *(f"- `[{r['category_id']}]` {r.get('name','?')} status={r.get('status')} direct_enabled={r.get('direct_enabled')} active_children={r.get('active_children')}" for r in db_rows),
            "",
            "## 5. Public before",
            f"- Home mega menu Упаковочное: {home_b['megamenu_upak_visible']}",
            f"- Posuda product_cards: {pos_b['product_cards']}",
            "",
            "## 6. Render source diagnostic",
            f"- See `{STORAGE / 'render-source' / 'render-source-summary.md'}`",
            "",
            "## 7. Exact fix plan",
            f"- See `{STORAGE / 'exact-fix-plan' / 'exact-fix-plan.md'}`",
            "",
            "## 8. Backup / rollback",
            f"- Storage backups under `{STORAGE / 'file-backups'}`",
            f"- Rollback: `{STORAGE / 'rollback' / 'rollback-plan.md'}`",
            "",
            "## 9. Production apply",
            f"- Applied: {applied}",
            "- Files: category_visibility.php, catalog/controller/product/category.php",
            "",
            "## 10. Cache action",
            f"- Cleared OpenCart cache when apply ran — see `{STORAGE / 'cache'}`",
            "",
            "## 11. Public after",
            f"- Home mega menu Упаковочное: {home_a['megamenu_upak_visible']}",
            f"- Posuda product_cards: {pos_a['product_cards']}",
            f"- Upak HTTP: {upak_a['http_status']}",
            "",
            "## 12. Mega menu verification",
            f"- Homepage: upak in menu = {home_a['megamenu_upak_visible']} (expect False)",
            f"- Katalog page: see public-after CSV",
            f"- tmp markers on home: {home_a['tmp_marker_visible']} (expect False)",
            "",
            "## 13. Posuda PLP verification",
            f"- `/posuda-i-inventar` HTTP {pos_a['http_status']}, cards={pos_a['product_cards']} (expect 6)",
            "",
            "## 14. Regression",
            "- DB writes: 0",
            "- Product writes: 0",
            "- Category structure writes: 0",
            "- Import: 0",
            "- Baseline refresh: 0",
            "",
            "## 15. Git/worktree summary",
            f"- Branch: `{git['branch']}`",
            f"- HEAD: `{git['head']}`",
            f"- Origin canonical: `{git['origin_head']}`",
            "",
            "## 16. Storage artifacts",
            f"- `{STORAGE}`",
            "",
            "## 17. SAFE UNKNOWN / blockers",
            "- None unless apply failed or post-smoke mismatch.",
            "",
            "## 18. Final verdict",
            f"**{verdict}**",
            "",
            "## 19. Next recommendation",
            "After 1C import enables `[381]`, re-verify mega menu and `/upakovochnoe-oborudovanie` without code changes if status returns to 1.",
            "",
        ]
    )
    write_text(REPORT_PATH, text)
    write_text(STORAGE / "reports" / "SITE-002-PROD-MEGAMENU-AND-POSUDA-PLP-REPAIR-01.md", text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Deploy to production")
    args = parser.parse_args()

    ensure_storage()
    git = git_preflight()
    write_json(STORAGE / "preflight" / "git-state.json", git)
    write_text(
        STORAGE / "preflight" / "preflight-summary.md",
        f"# Preflight\n\n- {utc_now()}\n- Branch: {git['branch']}\n- HEAD: {git['head']}\n",
    )

    db_rows = [db_category_snapshot(i) for i in TARGET_IDS]
    write_csv(
        STORAGE / "db-before" / "category-status.csv",
        db_rows,
        ["category_id", "name", "parent_id", "status", "keyword", "direct_enabled", "active_children"],
    )

    before = public_smoke("before")
    write_csv(
        STORAGE / "public-before" / "public-before-smoke.csv",
        before,
        list(before[0].keys()) if before else ["phase"],
    )

    phase_docs()

    applied = False
    if args.apply:
        ftp = ftp_connect()
        try:
            phase_apply(ftp)
        finally:
            ftp.quit()
        phase_cache_clear()
        applied = True

    after = public_smoke("after")
    write_csv(STORAGE / "public-after" / "public-after-smoke.csv", after, list(after[0].keys()) if after else ["phase"])
    write_text(
        STORAGE / "public-after" / "public-after-summary.md",
        f"# Public after\n\nPosuda cards: {next(r['product_cards'] for r in after if r['key']=='posuda')}\n",
    )

    home_a = next(r for r in after if r["key"] == "home")
    pos_a = next(r for r in after if r["key"] == "posuda")
    upak_a = next(r for r in after if r["key"] == "upak")

    success = (
        applied
        and not home_a["megamenu_upak_visible"]
        and int(pos_a["product_cards"]) >= 6
        and int(upak_a["http_status"]) == 404
        and not pos_a["php_warning"]
    )
    if not applied:
        verdict = "SITE-002 MEGAMENU AND POSUDA PLP REPAIR BLOCKED — NO UNSAFE MUTATION (dry-run only)"
    elif success:
        verdict = "SITE-002 MEGAMENU AND POSUDA PLP REPAIR COMPLETE — HIDDEN CATEGORY REMOVED FROM MENU AND POSUDA PRODUCTS DISPLAY"
    else:
        verdict = "SITE-002 MEGAMENU AND POSUDA PLP REPAIR PARTIAL — FOLLOW-UP REQUIRED"

    write_csv(
        STORAGE / "regression" / "mutation-summary.csv",
        [
            {"item": "db_writes", "value": "0"},
            {"item": "product_writes", "value": "0"},
            {"item": "category_structure_writes", "value": "0"},
            {"item": "import_runs", "value": "0"},
            {"item": "files_deployed", "value": "2" if applied else "0"},
        ],
        ["item", "value"],
    )
    write_text(STORAGE / "regression" / "regression-summary.md", f"# Regression\n\nVerdict: {verdict}\n")

    build_report(git, db_rows, before, after, applied, verdict)

    print(verdict)
    return 0 if success or not args.apply else 1


if __name__ == "__main__":
    sys.exit(main())
