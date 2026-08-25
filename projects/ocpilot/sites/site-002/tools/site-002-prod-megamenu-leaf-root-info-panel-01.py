#!/usr/bin/env python3
"""SITE-002 — megamenu leaf-root info panel fallback apply.

Operation: SITE-002-PROD-MEGAMENU-LEAF-ROOT-INFO-PANEL-01
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

OPERATION_ID = "SITE-002-PROD-MEGAMENU-LEAF-ROOT-INFO-PANEL-01"
PRODUCTION_URL = "https://bzpm.ru/"
PREFIX = "oc_"
LANGUAGE_ID = 1
STORE_ID = 0
ROOT_IDS = (79, 95, 90, 186, 375, 373, 364, 381)
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
AUTHORITY_REPO = Path(r"X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo")
TOOLS = AUTHORITY_REPO / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
MIRROR_CV = TOOLS / "category_visibility.php"
MIRROR_TWIG = TOOLS / "megamenu-SITE-002-PROD-MEGAMENU-LEAF-ROOT-INFO-PANEL-01.twig"
MIRROR_CSS = TOOLS / "megamenu-leaf-info-SITE-002-PROD-MEGAMENU-LEAF-ROOT-INFO-PANEL-01.css"
REMOTE_CV = "/public_html/system/library/zpm/category_visibility.php"
REMOTE_TWIG = "/public_html/catalog/view/theme/default/template/common/megamenu.twig"
REMOTE_CSS = "/public_html/assets/css/style.css"
REMOTE_CSS_MIN = "/public_html/assets/css/style.min.css"
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"
REPORT_PATH = (
    AUTHORITY_REPO
    / "projects/ocpilot/sites/site-002/reports"
    / "SITE-002-PROD-MEGAMENU-LEAF-ROOT-INFO-PANEL-01.md"
)

STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
) / OPERATION_ID

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

CSS_MARKER = "SITE-002-PROD-MEGAMENU-LEAF-ROOT-INFO-PANEL-01"


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


def root_inventory() -> list[dict[str, Any]]:
    ids = ",".join(str(i) for i in ROOT_IDS)
    sql = f"""
SELECT c.category_id, cd.name, c.status, IFNULL(c.image,''),
       (SELECT COUNT(*) FROM {PREFIX}category ch WHERE ch.parent_id=c.category_id AND ch.status=1) AS visible_children,
       (SELECT COUNT(*) FROM {PREFIX}product_to_category ptc
          JOIN {PREFIX}product p ON p.product_id=ptc.product_id AND p.status=1
         WHERE ptc.category_id=c.category_id) AS direct_products
FROM {PREFIX}category c
JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID}
WHERE c.category_id IN ({ids})
ORDER BY c.category_id;
"""
    rows = []
    for r in parse_tsv(mysql_query(sql)):
        item = {
            "category_id": int(r[0]),
            "name": r[1],
            "status": int(r[2]),
            "image": r[3],
            "visible_children": int(r[4]),
            "direct_products": int(r[5]),
        }
        item["leaf_info_candidate"] = (
            item["status"] == 1
            and item["visible_children"] == 0
            and item["direct_products"] > 0
        )
        rows.append(item)
    return rows


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
    posuda_pane = pane_for_category(html, "Посуда и инвентарь")
    neutral_pane = pane_for_category(html, "Нейтральное оборудование")
    return {
        "left_categories": left,
        "has_posuda_left": any("Посуда" in x for x in left),
        "has_upak_left": any("Упаковочн" in x for x in left),
        "posuda_has_leaf_info": 'data-leaf-info="1"' in posuda_pane
        or "zpm-catalog__leaf-info" in posuda_pane,
        "posuda_has_tiles": "zpm-catalog__tile" in posuda_pane,
        "posuda_pane_emptyish": (
            "zpm-catalog__tile" not in posuda_pane
            and "zpm-catalog__leaf-info" not in posuda_pane
            and posuda_pane != ""
        ),
        "neutral_has_tiles": "zpm-catalog__tile" in neutral_pane,
        "php_warning": has_php_warning(html),
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


def append_css_block(existing: bytes, block: str) -> bytes:
    text = existing.decode("utf-8", errors="replace")
    if CSS_MARKER in text:
        # replace previous block if re-applied
        text = re.sub(
            rf"/\* {re.escape(CSS_MARKER)}[\s\S]*?(?=\Z|/\* SITE-002)",
            "",
            text,
            count=1,
        ).rstrip() + "\n\n"
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


def write_report(payload: dict[str, Any]) -> None:
    inv = payload["inventory"]
    candidates = [r for r in inv if r["leaf_info_candidate"]]
    before = payload["before_home_menu"]
    after = payload["after_home_menu"]
    lines = [
        f"# REPORT — {OPERATION_ID}",
        "",
        f"- Generated: {utc_now()}",
        f"- Authority worktree: `{AUTHORITY_REPO}`",
        f"- Branch: `{payload['preflight']['branch']}` @ `{payload['preflight']['head']}`",
        f"- Storage: `{STORAGE}`",
        "",
        "## Verdict",
        "",
        f"**{payload['verdict']}**",
        "",
        "## Objective",
        "",
        "For mega-menu root categories that are visible (`status=1`), have no visible child tiles,",
        "but do have products — render a compact right-pane info panel (title / image / text / CTA)",
        "instead of an empty white panel. Preserve normal child-grid megamenu and status=0 hiding.",
        "",
        "## Leaf-root inventory (approved public roots)",
        "",
        "| ID | Name | status | visible children | direct products | leaf-info candidate |",
        "|----|------|--------|------------------|-----------------|---------------------|",
    ]
    for r in inv:
        lines.append(
            f"| {r['category_id']} | {r['name']} | {r['status']} | {r['visible_children']} | "
            f"{r['direct_products']} | {'YES' if r['leaf_info_candidate'] else 'no'} |"
        )
    lines += [
        "",
        f"Current leaf-info candidates: **{', '.join(str(c['category_id']) + ' ' + c['name'] for c in candidates) or '(none)'}**",
        "",
        "## Changed production files",
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
        "## Cache actions",
        "",
        "- Cleared OpenCart storage template/twig cache files under `storage/cache`.",
        "",
        "```",
        payload["cache_clear_tail"],
        "```",
        "",
        "## Before / after (home megamenu)",
        "",
        "| Check | Before | After |",
        "|-------|--------|-------|",
        f"| Posuda in left column | {before.get('has_posuda_left')} | {after.get('has_posuda_left')} |",
        f"| Upakovochnoe in left column | {before.get('has_upak_left')} | {after.get('has_upak_left')} |",
        f"| Posuda empty pane | {before.get('posuda_pane_emptyish')} | {after.get('posuda_pane_emptyish')} |",
        f"| Posuda leaf info panel | {before.get('posuda_has_leaf_info')} | {after.get('posuda_has_leaf_info')} |",
        f"| Neutral still has tiles | {before.get('neutral_has_tiles')} | {after.get('neutral_has_tiles')} |",
        f"| PHP warnings | {before.get('php_warning')} | {after.get('php_warning')} |",
        "",
        "## Regression summary",
        "",
        "- Categories with visible children keep tile-grid megamenu (Neutral checked).",
        "- Hidden root `[381] Упаковочное оборудование` (`status=0`) stays out of left column.",
        "- Posuda PLP leaf-hub product rendering path untouched in this wave (no `category.php` change).",
        "- No DB / import / URL / redirect / category structure mutations.",
        "",
        "## HTTP smoke",
        "",
    ]
    for row in payload["smoke_after"]:
        lines.append(
            f"- `{row['key']}` → HTTP {row['status']} ({row['bytes']} bytes); php_warning={row['php_warning']}"
        )
    lines += [
        "",
        "## Rollback",
        "",
        "Restore byte backups from `file-backups/` via FTP to the three remote paths, then clear twig cache.",
        "",
        "## Git note",
        "",
        "Canonical `X:\\AI MARS` remains dirty (foreign WIP). Docs/tools live in authority Storage worktree;",
        "no commit/push performed by this apply wave.",
        "",
    ]
    write_text(REPORT_PATH, "\n".join(lines) + "\n")
    write_text(STORAGE / "reports" / REPORT_PATH.name, "\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    ensure_storage()

    preflight = git_preflight()
    write_json(STORAGE / "preflight" / "git.json", preflight)
    write_text(STORAGE / "preflight" / "worktree.txt", preflight["status_short"] + "\n")

    inventory = root_inventory()
    write_csv(
        STORAGE / "db-before" / "root-leaf-inventory.csv",
        inventory,
        [
            "category_id",
            "name",
            "status",
            "image",
            "visible_children",
            "direct_products",
            "leaf_info_candidate",
        ],
    )
    write_json(STORAGE / "db-before" / "root-leaf-inventory.json", inventory)

    write_text(
        STORAGE / "exact-fix-plan" / "plan.md",
        "\n".join(
            [
                f"# Exact fix plan — {OPERATION_ID}",
                "",
                "1. `category_visibility.php` — after empty children, attach `leaf_info` when products exist.",
                "2. `megamenu.twig` — render compact info panel when `has_leaf_info`.",
                "3. Append scoped CSS to `assets/css/style.css` (+ `style.min.css`).",
                "4. Clear twig/template cache only.",
                "5. Verify home + /katalog/ Posuda pane populated; Neutral tiles intact; 381 still hidden.",
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
        print("DRY-RUN complete. Re-run with --apply to deploy.")
        print("Candidates:", [c for c in inventory if c["leaf_info_candidate"]])
        print("Before Posuda empty:", before_home.get("posuda_pane_emptyish"))
        return

    for required in (MIRROR_CV, MIRROR_TWIG, MIRROR_CSS):
        if not required.is_file():
            raise FileNotFoundError(required)

    ftp = ftp_connect()
    backups: dict[str, bytes] = {}
    changed: list[dict[str, Any]] = []

    try:
        for remote, local_name in (
            (REMOTE_CV, "category_visibility.php"),
            (REMOTE_TWIG, "megamenu.twig"),
            (REMOTE_CSS, "style.css"),
            (REMOTE_CSS_MIN, "style.min.css"),
        ):
            data = ftp_download(ftp, remote)
            if data is None:
                raise RuntimeError(f"Missing remote file: {remote}")
            backups[remote] = data
            (STORAGE / "file-backups" / local_name).write_bytes(data)
            write_text(
                STORAGE / "file-backups" / f"{local_name}.sha256",
                sha256_bytes(data) + "\n",
            )

        cv_bytes = MIRROR_CV.read_bytes()
        twig_bytes = MIRROR_TWIG.read_bytes()
        css_block = MIRROR_CSS.read_text(encoding="utf-8")

        style_css = append_css_block(backups[REMOTE_CSS], css_block)
        style_min = append_css_block(backups[REMOTE_CSS_MIN], css_block)

        uploads = [
            (REMOTE_CV, cv_bytes, "replace"),
            (REMOTE_TWIG, twig_bytes, "replace"),
            (REMOTE_CSS, style_css, "append-css"),
            (REMOTE_CSS_MIN, style_min, "append-css"),
        ]
        for remote, data, action in uploads:
            ftp_upload(ftp, remote, data)
            changed.append(
                {
                    "remote": remote,
                    "action": action,
                    "sha256_after": sha256_bytes(data),
                    "bytes": len(data),
                }
            )
            # verify round-trip
            verify = ftp_download(ftp, remote)
            if verify != data:
                raise RuntimeError(f"FTP verify mismatch for {remote}")
    finally:
        ftp.quit()

    write_csv(
        STORAGE / "production-apply" / "changed-files.csv",
        changed,
        ["remote", "action", "sha256_after", "bytes"],
    )
    write_json(STORAGE / "production-apply" / "changed-files.json", changed)
    write_json(
        STORAGE / "rollback" / "instructions.json",
        {
            "restore_from": str(STORAGE / "file-backups"),
            "remotes": list(backups.keys()),
            "then": "clear storage/cache twig templates",
        },
    )

    cache_out = clear_twig_cache()
    write_text(STORAGE / "cache" / "clear-output.txt", cache_out)
    cache_tail = "\n".join(cache_out.strip().splitlines()[-8:])

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

    ok = (
        after_home.get("has_posuda_left") is True
        and after_home.get("has_upak_left") is False
        and after_home.get("posuda_has_leaf_info") is True
        and after_home.get("posuda_pane_emptyish") is False
        and after_home.get("neutral_has_tiles") is True
        and after_home.get("php_warning") is False
        and after_katalog.get("posuda_has_leaf_info") is True
        and after_katalog.get("has_upak_left") is False
    )
    verdict = (
        "SITE-002 MEGAMENU LEAF-ROOT INFO PANEL COMPLETE — POSUDA RIGHT PANE POPULATED"
        if ok
        else "SITE-002 MEGAMENU LEAF-ROOT INFO PANEL APPLY NEEDS ATTENTION — VERIFY FAILURES"
    )
    write_json(
        STORAGE / "regression" / "checks.json",
        {
            "ok": ok,
            "home": after_home,
            "katalog": after_katalog,
            "verdict": verdict,
        },
    )

    write_report(
        {
            "preflight": preflight,
            "inventory": inventory,
            "changed_files": changed,
            "cache_clear_tail": cache_tail,
            "before_home_menu": before_home,
            "after_home_menu": after_home,
            "smoke_after": smoke_after,
            "verdict": verdict,
        }
    )
    print(verdict)
    print("Report:", REPORT_PATH)


if __name__ == "__main__":
    main()
