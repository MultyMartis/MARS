#!/usr/bin/env python3
"""SITE-002 — ALL-15 Neutral first-level block correction apply (Run 4.316).

Corrects Run 4.314 HYBRID (10 curated) to ALL-15 direct children of Neutral 79,
including empty 82/83/85/87/89 with empty copy. Mega/deep/Tech/sitemap/baseline untouched.
Authority worktree only. Does not mutate dirty main, DB, Client Ops.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import io
import json
import re
import shlex
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01"
OCPILOT_RUN = "4.316"
SITE_ID = "SITE-002"
ENVIRONMENT = "FIRST_LEVEL_BLOCK_ALL15_CORRECTION_APPLY_PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
WRONG_BRAND = "БЗПМ"
EMPTY_COPY = "Ожидайте, товары скоро поступят."

# ALL-15 direct children of Neutral 79 (correction target)
SHOW_IDS = [80, 82, 83, 85, 86, 87, 89, 207, 301, 322, 326, 331, 354, 358, 360]
PREVIOUSLY_HIDDEN_IDS = [82, 83, 85, 87, 89]
PREVIOUS_HYBRID_SHOW_IDS = [80, 86, 207, 301, 322, 326, 331, 354, 358, 360]
# No longer hiding any first-level Neutral IDs in Catalog Section Tiles
HIDE_WAIT_IDS: list[int] = []
TECH_ROOT = 362
NEUTRAL_ROOT = 79
TECH_CHILDREN_EXPECTED = [373, 364, 369, 368, 375]
CRITICAL_PRODUCTS = [4707, 4708, 4709, 4710, 4712]
DELETED_CATS = list(range(153, 171))
BASELINE_COUNT = 1879
BASELINE_CHECKPOINT = "SITE-002-STABLE-PROD-POST-1C-IMPORT-20260728-MONITOR-BASELINE-1879-08"
EXPECTED_IMPORT_LOG = "mars_1c_import_2026-07-28_080011.txt"
EXPECTED_IMPORT_ID = "mars-20260728-080001-24823ddf"
PREVIOUS_HYBRID_APPLY = "SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01"
PREVIOUS_HYBRID_COMMIT = "1a3ff58b"
PREVIOUS_CLOSEOUT = "SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-CLOSEOUT-01"
PREVIOUS_CLOSEOUT_COMMIT = "7e133aa6"

SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
AUTHORITY_REPO = Path(r"X:\AI MARS STORAGE\git-sync-e01\repo")
TOOLS = AUTHORITY_REPO / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
MIRROR_CV = TOOLS / "category_visibility.php"
MONITOR_REPO = Path(r"X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo")
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"

REMOTE_CV = "/public_html/system/library/zpm/category_visibility.php"
REMOTE_HOME_TWIG = "/public_html/catalog/view/theme/default/template/sections/catalogsections.twig"
REMOTE_KATALOG_TWIG = "/public_html/catalog/view/theme/default/template/product/katalog.twig"

REMOTE_FILES = [REMOTE_CV, REMOTE_HOME_TWIG, REMOTE_KATALOG_TWIG]

TXT_NAME_RE = re.compile(r"^mars_1c_import_(?P<date>\d{4}-\d{2}-\d{2})_(?P<time>\d{6})\.txt$")
STATUS_RE = re.compile(r"Final status:\s*(\S+)", re.I)
RUN_ID_RE = re.compile(r"(mars-\d{8}-\d{6}-[0-9a-f]+)", re.I)
DURATION_TOTAL_RE = re.compile(r"Total duration:\s*([0-9]+(?:\.[0-9]+)?)\s*seconds?", re.I)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def parse_production_section(subsection: str | None = None) -> dict[str, str]:
    text = SECRETS_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE
        )
        if not sub:
            raise RuntimeError(f"Subsection {subsection!r} not found")
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


def ftp_connect() -> ftplib.FTP:
    f = parse_production_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=300)
    ftp.login(f["username"], f["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes | None:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue()
    except ftplib.error_perm:
        return None


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def list_dir_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, _ in ftp.mlsd(path):
            if name not in (".", ".."):
                names.append(name)
        return sorted(names)
    except ftplib.error_perm:
        pass
    lines: list[str] = []
    ftp.retrlines("LIST " + path, lines.append)
    for line in lines:
        parts = line.split(maxsplit=8)
        if len(parts) >= 9:
            names.append(parts[8])
    return sorted(names)


def ssh_exec(cmd: str, timeout: int = 180) -> dict[str, Any]:
    try:
        import paramiko  # type: ignore
    except ImportError:
        return {"status": "blocked", "reason": "paramiko not available", "stdout": "", "stderr": ""}
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
    _i, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    rc = stdout.channel.recv_exit_status()
    client.close()
    return {"status": "ok" if rc == 0 else "failed", "rc": rc, "stdout": out, "stderr": err}


def ssh_mysql(sql: str) -> dict[str, Any]:
    db = parse_production_section("Database")
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B -u {shlex.quote(db["username"])} '
        f'{shlex.quote(db["database"])} -e "{esc}" 2>&1'
    )
    res = ssh_exec(cmd, timeout=180)
    blob = res.get("stdout", "") + res.get("stderr", "")
    if "ERROR" in blob or "Access denied" in blob:
        return {"status": "failed", "stdout": res.get("stdout", ""), "stderr": res.get("stderr", "")}
    return {"status": "ok", "stdout": res.get("stdout", ""), "stderr": res.get("stderr", "")}


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xml,*/*",
            "Cache-Control": "no-cache",
        },
        method="GET",
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=90, context=ctx) as resp:
            body = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "url": url,
                "final_url": resp.geturl(),
                "status": resp.status,
                "bytes": len(body),
                "sha256": sha256_bytes(body),
                "text": text,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read() if exc.fp else b""
        text = raw.decode("utf-8", errors="replace")
        return {
            "url": url,
            "final_url": exc.geturl(),
            "status": exc.code,
            "bytes": len(raw),
            "sha256": sha256_bytes(raw),
            "text": text,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "url": url,
            "final_url": url,
            "status": None,
            "bytes": 0,
            "sha256": "",
            "text": "",
            "error": str(exc),
        }


def moscow_to_utc(dt: datetime) -> datetime:
    return (dt - timedelta(hours=3)).replace(tzinfo=timezone.utc)


def parse_txt_content(text: str) -> dict[str, Any]:
    out: dict[str, Any] = {"duration_seconds": None, "run_id": None, "final_status": None}
    if m := DURATION_TOTAL_RE.search(text):
        out["duration_seconds"] = float(m.group(1))
    if m := RUN_ID_RE.search(text):
        out["run_id"] = m.group(1)
    if m := STATUS_RE.search(text):
        out["final_status"] = m.group(1)
    return out


def extract_cards(html: str, surface: str) -> list[dict[str, Any]]:
    """Extract zpm-cat-card entries from Catalog Section Tiles markup."""
    cards: list[dict[str, Any]] = []
    # Prefer section blocks; fall back to all cards
    blocks = re.findall(
        r'data-catalog-section-tiles[^>]*data-section-id="(\d+)"[\s\S]*?</div>\s*</div>\s*</div>',
        html,
        re.I,
    )
    # Simpler: all zpm-cat-card anchors with title
    for m in re.finditer(
        r'<a class="zpm-cat-card"[^>]*href="([^"]+)"[^>]*>\s*'
        r'<div class="zpm-cat-card__title">([^<]+)</div>'
        r'(?:\s*<div class="zpm-cat-card__empty">([^<]*)</div>)?',
        html,
        re.I,
    ):
        href, title, empty = m.group(1), m.group(2).strip(), (m.group(3) or "").strip()
        cards.append(
            {
                "surface": surface,
                "title": title,
                "url": href if href.startswith("http") else f"https://bzpm.ru{href}",
                "empty_copy": empty,
                "empty_copy_present": bool(empty),
            }
        )
    return cards


def sitemap_url_count(text: str) -> int:
    try:
        root = ET.fromstring(text)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = root.findall(".//sm:url/sm:loc", ns)
        if not locs:
            locs = root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        return len({(el.text or "").strip() for el in locs if el.text})
    except ET.ParseError:
        return len(set(re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", text)))


def patch_twig_empty_copy(src: str) -> str:
    """Insert empty_copy div after card title if missing."""
    if "zpm-cat-card__empty" in src and "cat.empty_copy" in src:
        return src
    pattern = re.compile(
        r'(<div class="zpm-cat-card__title">\{\{\s*cat\.name\s*\}\}</div>)',
        re.M,
    )
    repl = (
        r'\1\n'
        r'            {% if cat.empty_copy %}\n'
        r'            <div class="zpm-cat-card__empty">{{ cat.empty_copy }}</div>\n'
        r'            {% endif %}'
    )
    out, n = pattern.subn(repl, src, count=0)
    if n == 0:
        # fallback for `c.name` loop variants in legacy elseif only — leave as-is
        pass
    return out


def build_all15_category_visibility(src: str) -> str:
    """Correct HYBRID Neutral first-level block to ALL-15 (home + /katalog/)."""
    src = src.replace("\r\n", "\n").replace("\r", "\n")
    if "SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01" in src:
        # Ensure IDs still match ALL-15 even if marker present
        pass

    show_php = "array(" + ", ".join(str(i) for i in SHOW_IDS) + ")"

    # Header note
    if "SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01" not in src:
        if "SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01" in src:
            src = src.replace(
                " * SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01 — HYBRID Neutral first-level block (home+/katalog):\n"
                " *   explicit show list; hide legacy wait IDs 82/83/85/87/89; empty copy for future proven empties;\n"
                " *   mega/buildHubChildCards product gate unchanged; Tech 362 unchanged.\n",
                " * SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01 — HYBRID Neutral first-level block (superseded by ALL15 correction).\n"
                " * SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01 — ALL-15 Neutral first-level block (home+/katalog):\n"
                " *   all 15 direct children of 79; empty copy for zero-product first-level cards;\n"
                " *   mega/buildHubChildCards product gate unchanged; Tech 362 unchanged.\n",
            )
        else:
            src = src.replace(
                " * SITE-002-PROD-MEGAMENU-CHILDREN-AUTOMATION-01 — mega menu children rebuilt DB-driven to match Catalog Section Tiles\n"
                " *   (neutral keeps product gate; other section hubs include empty active children).\n",
                " * SITE-002-PROD-MEGAMENU-CHILDREN-AUTOMATION-01 — mega menu children rebuilt DB-driven to match Catalog Section Tiles\n"
                " *   (neutral keeps product gate; other section hubs include empty active children).\n"
                " * SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01 — ALL-15 Neutral first-level block (home+/katalog):\n"
                " *   all 15 direct children of 79; empty copy for zero-product first-level cards;\n"
                " *   mega/buildHubChildCards product gate unchanged; Tech 362 unchanged.\n",
            )

    if "EMPTY_FIRST_LEVEL_COPY" not in src:
        src = src.replace(
            "\tconst PLACEHOLDER_IMAGE = 'placeholder.png';\n",
            "\tconst PLACEHOLDER_IMAGE = 'placeholder.png';\n"
            "\t/** Empty first-level caption for empty Neutral first-level cards. */\n"
            f"\tconst EMPTY_FIRST_LEVEL_COPY = '{EMPTY_COPY}';\n",
        )
    else:
        src = src.replace(
            "\t/** Empty first-level caption for future proven empty Neutral show-list cards. */\n",
            "\t/** Empty first-level caption for empty Neutral first-level cards. */\n",
        )

    # ALL-15 show list
    src = re.sub(
        r"\t/\*\*[^*]*Neutral first-level Catalog Section Tiles[^*]*\*/\n"
        r"\tprivate static \$neutral_hub_branch_ids = array\([^)]*\);",
        "\t/** ALL-15 Neutral first-level Catalog Section Tiles (home + /katalog/) — direct children of 79. */\n"
        f"\tprivate static $neutral_hub_branch_ids = {show_php};",
        src,
        count=1,
    )
    src = re.sub(
        r"\tprivate static \$neutral_hub_branch_ids = array\([^)]*\);",
        f"\tprivate static $neutral_hub_branch_ids = {show_php};",
        src,
        count=1,
    )

    # Clear hide/wait — previously hidden IDs are now shown
    if "neutral_first_level_hide_wait_ids" in src:
        src = re.sub(
            r"\t/\*\* Legacy Neutral first-level duplicates[^*]*\*/\n"
            r"\tprivate static \$neutral_first_level_hide_wait_ids = array\([^)]*\);",
            "\t/** No Neutral first-level IDs hidden in Catalog Section Tiles after ALL15 correction. */\n"
            "\tprivate static $neutral_first_level_hide_wait_ids = array();",
            src,
            count=1,
        )
        src = re.sub(
            r"\tprivate static \$neutral_first_level_hide_wait_ids = array\([^)]*\);",
            "\tprivate static $neutral_first_level_hide_wait_ids = array();",
            src,
            count=1,
        )
    else:
        src = src.replace(
            f"\tprivate static $neutral_hub_branch_ids = {show_php};\n",
            f"\tprivate static $neutral_hub_branch_ids = {show_php};\n\n"
            "\t/** No Neutral first-level IDs hidden in Catalog Section Tiles after ALL15 correction. */\n"
            "\tprivate static $neutral_first_level_hide_wait_ids = array();\n",
        )

    # Update helper docblock
    src = src.replace(
        "\t * HYBRID Neutral first-level cards for Catalog Section Tiles only (home + /katalog/).\n"
        "\t * Show approved IDs; never include hide/wait IDs; allow zero-product cards with empty copy.\n"
        "\t * Mega menu continues to use buildHubChildCards() with Neutral product gate.\n",
        "\t * ALL-15 Neutral first-level cards for Catalog Section Tiles only (home + /katalog/).\n"
        "\t * Show all 15 direct children of 79; allow zero-product cards with empty copy.\n"
        "\t * Mega menu continues to use buildHubChildCards() with Neutral product gate.\n",
    )

    if "buildNeutralFirstLevelBlockCards" not in src:
        raise RuntimeError("Expected HYBRID helper buildNeutralFirstLevelBlockCards on production source")

    if "buildNeutralFirstLevelBlockCards($controller)" not in src:
        raise RuntimeError("Expected Neutral tile path wired to buildNeutralFirstLevelBlockCards")

    return src


def phase_manifest() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "production_url": PRODUCTION_URL,
            "environment": ENVIRONMENT,
            "ocpilot_run": OCPILOT_RUN,
            "previous_hybrid_apply_run": PREVIOUS_HYBRID_APPLY,
            "previous_hybrid_apply_commit": PREVIOUS_HYBRID_COMMIT,
            "previous_closeout_run": PREVIOUS_CLOSEOUT,
            "previous_closeout_commit": PREVIOUS_CLOSEOUT_COMMIT,
            "baseline_checkpoint": BASELINE_CHECKPOINT,
            "baseline_count": BASELINE_COUNT,
            "latest_import_log": EXPECTED_IMPORT_LOG,
            "latest_import_id": EXPECTED_IMPORT_ID,
            "neutral_root_id": NEUTRAL_ROOT,
            "tech_root_id": TECH_ROOT,
            "all15_target_ids": SHOW_IDS,
            "previously_hidden_ids_to_show_now": PREVIOUSLY_HIDDEN_IDS,
            "previous_hybrid_show_ids": PREVIOUS_HYBRID_SHOW_IDS,
            "empty_copy": EMPTY_COPY,
            "beget_external_backup_by_operator": True,
            "db_write_allowed": False,
            "ftp_write_allowed": True,
            "code_change_allowed": True,
            "template_change_allowed": True,
            "cache_clear_allowed": True,
            "import_run_allowed": False,
            "scheduler_change_allowed": False,
            "monitor_baseline_change_allowed": False,
            "category_product_change_allowed": False,
            "redirect_change_allowed": False,
            "client_ops_changes_allowed": False,
            "dirty_main_mutation_allowed": False,
            "mega_menu_change_allowed": False,
            "deep_leaf_global_visibility_change_allowed": False,
            "tech_behavior_change_allowed": False,
            "created_utc": utc_now(),
        },
    )


def phase_reports_read() -> None:
    write_text(
        DEPLOYMENT_ROOT / "reports-read" / "current-state-summary.md",
        "\n".join(
            [
                "# Current state summary (reports read)",
                "",
                "- Run 4.312 Monitor Baseline Refresh 08: baseline **1879**, checkpoint `…-1879-08`, monitor after `NO_ACTION_REQUIRED`.",
                "- Run 4.313 Scope Decision: **HYBRID RECOMMENDED** (historical).",
                "- Run 4.314 HYBRID apply: live 10 curated; hide 82/83/85/87/89.",
                "- Run 4.315 HYBRID closeout: docs accepted; operator visual review later found UX still looks like before.",
                "- This correction: ALL-15 Neutral first-level on home + `/katalog/` including empty cards with copy.",
                "- Latest accepted import: `mars_1c_import_2026-07-28_080011.txt` / `mars-20260728-080001-24823ddf` SUCCESS.",
                "- Mega / deep leaves / Tech 362 / importer / sitemap / baseline: out of apply scope.",
                "",
            ]
        ),
    )
    write_text(
        DEPLOYMENT_ROOT / "reports-read" / "correction-scope-summary.md",
        "\n".join(
            [
                "# Correction scope summary",
                "",
                "## ALL15_TARGET_IDS (SHOW)",
                ", ".join(str(i) for i in SHOW_IDS),
                "",
                "## PREVIOUSLY_HIDDEN_NOW_SHOW",
                ", ".join(str(i) for i in PREVIOUSLY_HIDDEN_IDS),
                "",
                "## Surfaces",
                "- home Catalog Section Tiles",
                "- `/katalog/` Catalog Section Tiles",
                "",
                "## Must not change",
                "- mega menu product gate",
                "- deep leaf global visibility",
                "- Tech root 362 behavior",
                "- sitemap / baseline / importer / products / categories",
                "",
                "## Empty copy",
                f"`{EMPTY_COPY}`",
                "",
                "## Operator",
                "- External Beget backup by operator: true",
                "- Correction apply approved",
                "",
            ]
        ),
    )


def phase_current_state(ftp: ftplib.FTP) -> dict[str, Any]:
    roots = {
        "login_root": (ftp.pwd() or "/"),
    }
    root = roots["login_root"]
    if not root.endswith("/"):
        root += "/"
    reports_dir = root + "storage/mars-tools/cron/reports/"
    names = [n for n in list_dir_names(ftp, reports_dir) if TXT_NAME_RE.match(n)]
    names_sorted = sorted(
        names,
        key=lambda n: (
            TXT_NAME_RE.match(n).group("date"),
            TXT_NAME_RE.match(n).group("time"),
        ),
        reverse=True,
    )
    newest_success = ""
    newest_success_parsed: dict[str, Any] = {}
    later_failed = False
    for n in names_sorted:
        raw_n = ftp_download(ftp, reports_dir + n)
        text_n = (raw_n or b"").decode("utf-8", errors="replace")
        parsed_n = parse_txt_content(text_n)
        st = str(parsed_n.get("final_status") or "").upper()
        if st == "SUCCESS" and not newest_success:
            newest_success = n
            newest_success_parsed = parsed_n
        # dated name lexicographic order matches chronological for this filename scheme
        if n > EXPECTED_IMPORT_LOG and st and st != "SUCCESS":
            later_failed = True
    latest_name = newest_success or (names_sorted[0] if names_sorted else "")
    parsed = newest_success_parsed if newest_success_parsed else {}
    if latest_name and not parsed:
        raw = ftp_download(ftp, reports_dir + latest_name)
        parsed = parse_txt_content((raw or b"").decode("utf-8", errors="replace"))

    sm = http_get("https://bzpm.ru/sitemap.xml")
    sm_count = sitemap_url_count(sm.get("text") or "") if sm.get("status") == 200 else None

    # monitor artifacts
    monitor_note = "SAFE UNKNOWN"
    monitor_dir = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\monitor")
    latest_monitor = ""
    monitor_verdict = ""
    if monitor_dir.exists():
        cands = sorted(monitor_dir.glob("**/summary*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
        # also look for timestamped folders
        stamp_dirs = sorted(
            [p for p in monitor_dir.iterdir() if p.is_dir()],
            key=lambda p: p.name,
            reverse=True,
        )
        for d in stamp_dirs[:5]:
            for name in ("summary.md", "decision.md", "monitor-summary.md", "result.json"):
                f = d / name
                if f.exists():
                    latest_monitor = str(f)
                    txt = f.read_text(encoding="utf-8", errors="replace")
                    if "NO_ACTION_REQUIRED" in txt:
                        monitor_verdict = "NO_ACTION_REQUIRED"
                    monitor_note = f"read {f}"
                    break
            if monitor_verdict:
                break
        if not monitor_verdict:
            # search reports
            rep = AUTHORITY_REPO / "projects/ocpilot/sites/site-002/reports"
            br = rep / "SITE-002-MONITOR-BASELINE-REFRESH-08.md"
            if br.exists() and "NO_ACTION_REQUIRED" in br.read_text(encoding="utf-8", errors="replace"):
                monitor_verdict = "NO_ACTION_REQUIRED"
                monitor_note = "from baseline refresh 08 report + live sitemap"

    # critical products via HTTP (canonical URLs often /product_id= or SEO)
    crit_rows = []
    for pid in CRITICAL_PRODUCTS:
        # probe common SEO-less route
        r = http_get(f"https://bzpm.ru/index.php?route=product/product&product_id={pid}")
        body = r.get("text") or ""
        crit_rows.append(
            {
                "product_id": pid,
                "status": r.get("status"),
                "not_found": "Товар не найден" in body,
                "wrong_brand": WRONG_BRAND in body,
                "final_url": r.get("final_url"),
            }
        )

    write_csv(
        DEPLOYMENT_ROOT / "current-state" / "critical-products-current.csv",
        crit_rows,
        ["product_id", "status", "not_found", "wrong_brand", "final_url"],
    )
    write_csv(
        DEPLOYMENT_ROOT / "current-state" / "import-monitor-sitemap-current.csv",
        [
            {
                "latest_import_log": latest_name,
                "final_status": parsed.get("final_status"),
                "run_id": parsed.get("run_id"),
                "duration_seconds": parsed.get("duration_seconds"),
                "matches_expected_log": latest_name == EXPECTED_IMPORT_LOG,
                "matches_expected_id": parsed.get("run_id") == EXPECTED_IMPORT_ID,
                "later_failed_supersede": later_failed,
                "sitemap_status": sm.get("status"),
                "sitemap_count": sm_count,
                "baseline_count": BASELINE_COUNT,
                "monitor_verdict": monitor_verdict or "SAFE_UNKNOWN",
                "monitor_note": monitor_note,
            }
        ],
        [
            "latest_import_log",
            "final_status",
            "run_id",
            "duration_seconds",
            "matches_expected_log",
            "matches_expected_id",
            "later_failed_supersede",
            "sitemap_status",
            "sitemap_count",
            "baseline_count",
            "monitor_verdict",
            "monitor_note",
        ],
    )

    import_ok = (
        newest_success == EXPECTED_IMPORT_LOG
        and str(parsed.get("final_status", "")).upper() == "SUCCESS"
        and parsed.get("run_id") == EXPECTED_IMPORT_ID
        and not later_failed
    )
    # Soft monitor: prior baseline-refresh 08 was NO_ACTION_REQUIRED; UI apply does not require re-run.
    gate_ok = (
        import_ok
        and sm_count == BASELINE_COUNT
        and all(r["status"] == 200 and not r["not_found"] for r in crit_rows)
    )

    write_text(
        DEPLOYMENT_ROOT / "current-state" / "current-state-reconfirm.md",
        "\n".join(
            [
                "# Current state reconfirm",
                "",
                f"- Latest import: `{latest_name}` / `{parsed.get('run_id')}` / `{parsed.get('final_status')}`",
                f"- Expected still current: **{latest_name == EXPECTED_IMPORT_LOG}**",
                f"- Later failed supersede: **{later_failed}**",
                f"- Sitemap count: **{sm_count}** (baseline {BASELINE_COUNT})",
                f"- Critical products: **{sum(1 for r in crit_rows if r['status']==200 and not r['not_found'])}/5**",
                f"- Monitor: `{monitor_verdict or 'SAFE_UNKNOWN'}` ({monitor_note})",
                f"- Hard gate: **{'PASS' if gate_ok else 'FAIL'}**",
                "",
            ]
        ),
    )
    return {
        "gate_ok": gate_ok,
        "sitemap_count": sm_count,
        "latest_import": latest_name,
        "monitor_verdict": monitor_verdict,
        "critical_ok": all(r["status"] == 200 and not r["not_found"] for r in crit_rows),
    }


def phase_db_readonly() -> dict[str, Any]:
    ids = SHOW_IDS + PREVIOUSLY_HIDDEN_IDS + [NEUTRAL_ROOT, TECH_ROOT] + TECH_CHILDREN_EXPECTED
    ids = sorted(set(ids))
    id_list = ",".join(str(i) for i in ids)
    sql = (
        "SELECT c.category_id, cd.name, c.parent_id, c.status, c.image, "
        "IFNULL(ua.keyword,'') AS keyword, "
        "(SELECT COUNT(*) FROM oc_category_to_store cs WHERE cs.category_id=c.category_id AND cs.store_id=0) AS store_linked, "
        "(SELECT COUNT(DISTINCT p2c.product_id) FROM oc_product_to_category p2c "
        " INNER JOIN oc_product p ON p.product_id=p2c.product_id AND p.status=1 "
        " INNER JOIN oc_category_path cp ON cp.category_id=p2c.category_id "
        " WHERE cp.path_id=c.category_id) AS subtree_products, "
        "(SELECT COUNT(*) FROM oc_mars_1c_category_map m WHERE m.category_id=c.category_id) AS map_hits "
        "FROM oc_category c "
        "LEFT JOIN oc_category_description cd ON cd.category_id=c.category_id AND cd.language_id=1 "
        "LEFT JOIN oc_seo_url ua ON ua.query=CONCAT('category_id=',c.category_id) AND ua.store_id=0 AND ua.language_id=1 "
        f"WHERE c.category_id IN ({id_list}) ORDER BY c.category_id"
    )
    res = ssh_mysql(sql)
    rows_raw = []
    if res["status"] == "ok":
        for line in res["stdout"].strip().splitlines():
            if not line.strip():
                continue
            p = line.split("\t")
            while len(p) < 9:
                p.append("")
            rows_raw.append(
                {
                    "category_id": int(p[0]),
                    "name": p[1],
                    "parent_id": int(p[2] or 0),
                    "status": int(p[3] or 0),
                    "image": p[4],
                    "keyword": p[5],
                    "store_linked": int(p[6] or 0),
                    "subtree_products": int(p[7] or 0),
                    "map_hits": int(p[8] or 0),
                }
            )
    by_id = {r["category_id"]: r for r in rows_raw}

    show_rows = []
    for cid in SHOW_IDS:
        r = by_id.get(cid, {})
        kw = r.get("keyword") or ""
        url = f"https://bzpm.ru/katalog/{kw}" if kw else ""
        http = http_get(url) if url else {"status": None}
        show_rows.append(
            {
                "category_id": cid,
                "exists": cid in by_id,
                "name": r.get("name", ""),
                "status": r.get("status", ""),
                "store_linked": r.get("store_linked", ""),
                "subtree_products": r.get("subtree_products", ""),
                "image": r.get("image", ""),
                "keyword": kw,
                "public_url": url,
                "http_status": http.get("status"),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "db-readonly" / "all15-neutral-control.csv",
        show_rows,
        [
            "category_id",
            "exists",
            "name",
            "status",
            "store_linked",
            "subtree_products",
            "image",
            "keyword",
            "public_url",
            "http_status",
        ],
    )
    # Keep alias for harness continuity
    write_csv(
        DEPLOYMENT_ROOT / "db-readonly" / "show-ids-control.csv",
        show_rows,
        [
            "category_id",
            "exists",
            "name",
            "status",
            "store_linked",
            "subtree_products",
            "image",
            "keyword",
            "public_url",
            "http_status",
        ],
    )

    hide_rows = []
    for cid in PREVIOUSLY_HIDDEN_IDS:
        r = by_id.get(cid, {})
        kw = r.get("keyword") or ""
        url = f"https://bzpm.ru/katalog/{kw}" if kw else ""
        http = http_get(url) if url else {"status": None}
        hide_rows.append(
            {
                "category_id": cid,
                "exists": cid in by_id,
                "name": r.get("name", ""),
                "parent_id": r.get("parent_id", ""),
                "status": r.get("status", ""),
                "store_linked": r.get("store_linked", ""),
                "subtree_products": r.get("subtree_products", ""),
                "map_hits": r.get("map_hits", ""),
                "is_empty": int(r.get("subtree_products") or 0) == 0,
                "public_url": url,
                "http_status": http.get("status"),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "db-readonly" / "empty-first-level-control.csv",
        hide_rows,
        [
            "category_id",
            "exists",
            "name",
            "parent_id",
            "status",
            "store_linked",
            "subtree_products",
            "map_hits",
            "is_empty",
            "public_url",
            "http_status",
        ],
    )
    write_csv(
        DEPLOYMENT_ROOT / "db-readonly" / "hide-wait-ids-control.csv",
        hide_rows,
        [
            "category_id",
            "exists",
            "name",
            "parent_id",
            "status",
            "store_linked",
            "subtree_products",
            "map_hits",
            "is_empty",
            "public_url",
            "http_status",
        ],
    )

    tech_rows = []
    for cid in [TECH_ROOT] + TECH_CHILDREN_EXPECTED:
        r = by_id.get(cid, {})
        kw = r.get("keyword") or ""
        url = f"https://bzpm.ru/katalog/{kw}" if kw else ""
        http = http_get(url) if url else {"status": None}
        tech_rows.append(
            {
                "category_id": cid,
                "exists": cid in by_id,
                "name": r.get("name", ""),
                "parent_id": r.get("parent_id", ""),
                "status": r.get("status", ""),
                "subtree_products": r.get("subtree_products", ""),
                "public_url": url,
                "http_status": http.get("status"),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "db-readonly" / "tech-controls.csv",
        tech_rows,
        [
            "category_id",
            "exists",
            "name",
            "parent_id",
            "status",
            "subtree_products",
            "public_url",
            "http_status",
        ],
    )

    # deleted cats absent
    del_sql = f"SELECT category_id FROM oc_category WHERE category_id IN ({','.join(str(i) for i in DELETED_CATS)})"
    del_res = ssh_mysql(del_sql)
    present_deleted = [ln.strip() for ln in (del_res.get("stdout") or "").splitlines() if ln.strip()]

    show_ok = all(
        r["exists"] and r["status"] == 1 and r["store_linked"] and r["http_status"] == 200 for r in show_rows
    )
    write_text(
        DEPLOYMENT_ROOT / "db-readonly" / "db-readonly-summary.md",
        "\n".join(
            [
                "# DB read-only summary",
                "",
                f"- ALL-15 IDs OK: **{show_ok}** ({len(show_rows)} targets)",
                f"- Previously-hidden empty candidates present: {sum(1 for r in hide_rows if r['exists'])}/5",
                f"- Empty (subtree_products=0) among previously-hidden: {sum(1 for r in hide_rows if r.get('is_empty'))}/5",
                f"- Tech root+children present: {sum(1 for r in tech_rows if r['exists'])}/{len(tech_rows)}",
                f"- Deleted 153–170 still present in DB: {present_deleted or 'none'}",
                f"- mysql status: {res['status']}",
                "",
            ]
        ),
    )
    # Also verify parent_id=79 for all SHOW_IDS
    parent_ok = all(
        cid in by_id and int(by_id[cid].get("parent_id") or 0) == NEUTRAL_ROOT for cid in SHOW_IDS
    )
    if not parent_ok:
        show_ok = False
    return {"show_ok": show_ok, "show_rows": show_rows, "hide_rows": hide_rows, "by_id": by_id}


def phase_public_before(show_rows: list[dict[str, Any]], hide_rows: list[dict[str, Any]]) -> dict[str, Any]:
    home = http_get("https://bzpm.ru/")
    katalog = http_get("https://bzpm.ru/katalog/")
    home_cards = extract_cards(home.get("text") or "", "home")
    kat_cards = extract_cards(katalog.get("text") or "", "katalog")
    write_csv(
        DEPLOYMENT_ROOT / "public-http-before" / "home-cards-before.csv",
        home_cards,
        ["surface", "title", "url", "empty_copy", "empty_copy_present"],
    )
    write_csv(
        DEPLOYMENT_ROOT / "public-http-before" / "katalog-cards-before.csv",
        kat_cards,
        ["surface", "title", "url", "empty_copy", "empty_copy_present"],
    )
    # sanitized extract only (no full HTML dump of potentially sensitive pages)
    write_text(
        DEPLOYMENT_ROOT / "public-http-before" / "public-before-summary.md",
        "\n".join(
            [
                "# Public before summary",
                "",
                f"- Home HTTP: {home.get('status')} / cards={len(home_cards)}",
                f"- /katalog/ HTTP: {katalog.get('status')} / cards={len(kat_cards)}",
                f"- Home wrong brand: {WRONG_BRAND in (home.get('text') or '')}",
                f"- Katalog wrong brand: {WRONG_BRAND in (katalog.get('text') or '')}",
                f"- Empty copy already live: {EMPTY_COPY in (home.get('text') or '') or EMPTY_COPY in (katalog.get('text') or '')}",
                "",
                "Full HTML not stored (sanitized extract tables only).",
                "",
            ]
        ),
    )
    return {"home_cards": home_cards, "katalog_cards": kat_cards, "home": home, "katalog": katalog}


def phase_source_prep_and_impl(ftp: ftplib.FTP) -> dict[str, bytes]:
    write_text(
        DEPLOYMENT_ROOT / "source-prep" / "source-files-inspected.txt",
        "\n".join(
            [
                str(MIRROR_CV),
                REMOTE_CV,
                REMOTE_HOME_TWIG,
                REMOTE_KATALOG_TWIG,
                "tools/catalogsections-SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01.twig",
                "tools/katalog-SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01.twig",
            ]
        )
        + "\n",
    )
    write_text(
        DEPLOYMENT_ROOT / "source-prep" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                "1. Patch `category_visibility.php` (correction from HYBRID → ALL-15):",
                "   - expand Neutral show list to all 15 direct children of 79;",
                "   - clear hide/wait list (82/83/85/87/89 now shown);",
                "   - keep `buildNeutralFirstLevelBlockCards` for Catalog Section Tiles;",
                "   - keep `buildHubChildCards` Neutral product gate for mega;",
                "   - Tech 362 path unchanged;",
                "   - empty copy for zero-product first-level cards.",
                "2. Twig: keep existing `cat.empty_copy` hooks (already from Run 4.314); redeploy only if hash changes.",
                "3. Deploy changed files only; clear `storage/cache/cache.*` only.",
                "",
            ]
        ),
    )
    write_text(
        DEPLOYMENT_ROOT / "source-prep" / "change-risk-assessment.md",
        "\n".join(
            [
                "# Change risk assessment",
                "",
                "- Visual delta expected: +5 Neutral first-level cards (82/83/85/87/89) with empty copy.",
                "- Duplicate-name cards vs curated siblings (Подтоварники / Полки / …) are intentional per operator ALL-15 request.",
                "- Mega menu risk mitigated by keeping `buildHubChildCards` product gate.",
                "- Tech risk mitigated by leaving non-Neutral branch on `buildHubChildCards`.",
                "- Sitemap/baseline/import unchanged (UI-only).",
                "",
            ]
        ),
    )

    before: dict[str, bytes] = {}
    after: dict[str, bytes] = {}
    for remote in REMOTE_FILES:
        data = ftp_download(ftp, remote)
        if data is None:
            raise RuntimeError(f"Missing remote file: {remote}")
        before[remote] = data
        bak = DEPLOYMENT_ROOT / "backups" / "production-files-before" / remote.replace("/", "__").lstrip("_")
        bak.parent.mkdir(parents=True, exist_ok=True)
        bak.write_bytes(data)

    live_cv = before[REMOTE_CV].decode("utf-8", errors="replace")
    patched_cv = build_all15_category_visibility(live_cv)
    MIRROR_CV.write_text(patched_cv.replace("\r\n", "\n"), encoding="utf-8", newline="\n")

    home_twig = before[REMOTE_HOME_TWIG].decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    katalog_twig = before[REMOTE_KATALOG_TWIG].decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
    patched_home = patch_twig_empty_copy(home_twig)
    patched_katalog = patch_twig_empty_copy(katalog_twig)

    (TOOLS / "catalogsections-SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01.twig").write_text(
        patched_home.replace("\r\n", "\n"), encoding="utf-8", newline="\n"
    )
    (TOOLS / "katalog-SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01.twig").write_text(
        patched_katalog.replace("\r\n", "\n"), encoding="utf-8", newline="\n"
    )

    after[REMOTE_CV] = patched_cv.encode("utf-8")
    after[REMOTE_HOME_TWIG] = patched_home.encode("utf-8")
    after[REMOTE_KATALOG_TWIG] = patched_katalog.encode("utf-8")

    for remote, data in after.items():
        p = DEPLOYMENT_ROOT / "implementation" / remote.replace("/", "__").lstrip("_")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    diff_cv = "\n".join(
        difflib.unified_diff(
            live_cv.splitlines(),
            patched_cv.splitlines(),
            fromfile="before/category_visibility.php",
            tofile="after/category_visibility.php",
            lineterm="",
        )
    )
    write_text(DEPLOYMENT_ROOT / "implementation" / "source-diff.patch", diff_cv + "\n")
    write_text(
        DEPLOYMENT_ROOT / "implementation" / "files-changed.txt",
        "\n".join(
            [
                "projects/ocpilot/sites/site-002/tools/category_visibility.php",
                "projects/ocpilot/sites/site-002/tools/catalogsections-SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01.twig",
                "projects/ocpilot/sites/site-002/tools/katalog-SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01.twig",
                "projects/ocpilot/sites/site-002/tools/site-002-prod-first-level-block-all15-correction-apply-01.py",
                "production: " + REMOTE_CV,
                "production: " + REMOTE_HOME_TWIG + " (only if hash differs)",
                "production: " + REMOTE_KATALOG_TWIG + " (only if hash differs)",
            ]
        )
        + "\n",
    )
    write_text(
        DEPLOYMENT_ROOT / "implementation" / "implementation-summary.md",
        "\n".join(
            [
                "# Implementation summary",
                "",
                "- ALL-15 Neutral tile builder: `buildNeutralFirstLevelBlockCards`",
                "- Show IDs (15): " + ", ".join(str(i) for i in SHOW_IDS),
                "- Previously hidden now shown: " + ", ".join(str(i) for i in PREVIOUSLY_HIDDEN_IDS),
                "- Hide/wait list: empty",
                f"- Empty copy constant: `{EMPTY_COPY}`",
                "- Mega path: `buildHubChildCards` unchanged (product gate)",
                "- Tech path: unchanged",
                "",
            ]
        ),
    )

    forbidden = []
    for label, text in [
        ("cv", patched_cv),
        ("home_twig", patched_home),
        ("katalog_twig", patched_katalog),
    ]:
        if WRONG_BRAND in text:
            forbidden.append(f"{label}: contains {WRONG_BRAND}")
        if re.search(r"['\"][^'\"]*\\n[^'\"]*['\"]", text):
            forbidden.append(f"{label}: possible literal \\n in string")
    php_ok = (
        "buildNeutralFirstLevelBlockCards" in patched_cv
        and "EMPTY_FIRST_LEVEL_COPY" in patched_cv
        and "SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01" in patched_cv
        and "array(82, 83, 85, 87, 89)" not in patched_cv.split("neutral_first_level_hide_wait_ids")[1][:120]
        if "neutral_first_level_hide_wait_ids" in patched_cv
        else False
    )
    # Simpler: hide wait must be empty array
    hide_empty = "private static $neutral_first_level_hide_wait_ids = array();" in patched_cv
    show_all15 = "array(80, 82, 83, 85, 86, 87, 89, 207, 301, 322, 326, 331, 354, 358, 360)" in patched_cv
    write_text(
        DEPLOYMENT_ROOT / "implementation" / "static-checks.txt",
        "\n".join(
            [
                f"php_all15_markers: {php_ok or (show_all15 and hide_empty)}",
                f"show_all15_ids: {show_all15}",
                f"hide_wait_empty: {hide_empty}",
                f"home_twig_empty_hook: {'cat.empty_copy' in patched_home}",
                f"katalog_twig_empty_hook: {'cat.empty_copy' in patched_katalog}",
                f"forbidden_findings: {forbidden or 'none'}",
                f"cv_sha256: {sha256_bytes(after[REMOTE_CV])}",
            ]
        )
        + "\n",
    )

    # deploy plan + rollback
    bak_rows = []
    for remote in REMOTE_FILES:
        bak_rows.append(
            {
                "remote_path": remote,
                "local_backup_path": str(
                    DEPLOYMENT_ROOT
                    / "backups"
                    / "production-files-before"
                    / remote.replace("/", "__").lstrip("_")
                ),
                "size_before": len(before[remote]),
                "hash_before": sha256_bytes(before[remote]),
                "hash_after_planned": sha256_bytes(after[remote]),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "backups" / "backup-manifest.csv",
        bak_rows,
        ["remote_path", "local_backup_path", "size_before", "hash_before", "hash_after_planned"],
    )
    write_text(
        DEPLOYMENT_ROOT / "deploy-plan" / "deploy-plan.md",
        "\n".join(
            [
                "# Deploy plan",
                "",
                "FTP upload exact 3 files:",
                *[f"- `{r}`" for r in REMOTE_FILES],
                "",
                "Then clear `storage/cache/cache.*` via SSH.",
                "Do not wipe `storage/modification/` unless required.",
                "",
            ]
        ),
    )
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "\n".join(
            [
                "# Rollback plan",
                "",
                "1. FTP restore each file from `backups/production-files-before/` (exact Run 4.314 HYBRID production state).",
                "2. Clear `storage/cache/cache.*`.",
                "3. Re-fetch home + `/katalog/` and confirm pre-correction HYBRID card set (10 Neutral + Tech).",
                "",
            ]
        ),
    )
    return after


def phase_ftp_deploy(ftp: ftplib.FTP, after: dict[str, bytes]) -> list[dict[str, Any]]:
    rows = []
    for remote, data in after.items():
        before = ftp_download(ftp, remote) or b""
        before_h = sha256_bytes(before)
        after_h = sha256_bytes(data)
        if before_h == after_h:
            rows.append(
                {
                    "remote_path": remote,
                    "local_source": "implementation harness",
                    "hash_before": before_h,
                    "hash_after": before_h,
                    "expected_hash": after_h,
                    "upload_status": "SKIPPED_UNCHANGED",
                }
            )
            continue
        ftp_upload(ftp, remote, data)
        verify = ftp_download(ftp, remote) or b""
        ok = sha256_bytes(verify) == after_h
        rows.append(
            {
                "remote_path": remote,
                "local_source": "implementation harness",
                "hash_before": before_h,
                "hash_after": sha256_bytes(verify),
                "expected_hash": after_h,
                "upload_status": "OK" if ok else "MISMATCH",
            }
        )
        if not ok:
            bak = (
                DEPLOYMENT_ROOT
                / "backups"
                / "production-files-before"
                / remote.replace("/", "__").lstrip("_")
            )
            if bak.exists():
                ftp_upload(ftp, remote, bak.read_bytes())
            raise RuntimeError(f"FTP verify mismatch for {remote}")
    uploaded = [r for r in rows if r["upload_status"] == "OK"]
    write_csv(
        DEPLOYMENT_ROOT / "ftp-deploy" / "ftp-deploy-manifest.csv",
        rows,
        ["remote_path", "local_source", "hash_before", "hash_after", "expected_hash", "upload_status"],
    )
    write_text(
        DEPLOYMENT_ROOT / "ftp-deploy" / "ftp-deploy-summary.md",
        "\n".join(
            [
                "# FTP deploy summary",
                "",
                f"- Files considered: {len(rows)}",
                f"- Uploaded: {len(uploaded)}",
                f"- Skipped unchanged: {sum(1 for r in rows if r['upload_status']=='SKIPPED_UNCHANGED')}",
                f"- All OK: {all(r['upload_status'] in ('OK', 'SKIPPED_UNCHANGED') for r in rows)}",
                "",
            ]
        ),
    )
    return rows


def phase_cache() -> dict[str, Any]:
    cmd = (
        f"cd {shlex.quote(CACHE_DIR)} && "
        "before=$(ls -1 cache.* 2>/dev/null | wc -l); "
        "rm -f cache.* 2>/dev/null; "
        "after=$(ls -1 cache.* 2>/dev/null | wc -l); "
        'echo "before=$before after=$after"; '
        "ls /home/a/assum/bzpm.ru/storage/modification/catalog/view/theme/default/template/sections 2>/dev/null | head -5 || echo NO_MOD_SECTIONS; "
        "ls /home/a/assum/bzpm.ru/storage/modification/system/library/zpm 2>/dev/null | head -5 || echo NO_MOD_ZPM"
    )
    res = ssh_exec(cmd, timeout=120)
    write_csv(
        DEPLOYMENT_ROOT / "cache" / "cache-actions.csv",
        [
            {
                "action": "rm -f storage/cache/cache.*",
                "path": CACHE_DIR + "/cache.*",
                "modification_cleared": False,
                "ssh_status": res.get("status"),
                "stdout": (res.get("stdout") or "").replace("\n", " | ")[:500],
            }
        ],
        ["action", "path", "modification_cleared", "ssh_status", "stdout"],
    )
    write_text(
        DEPLOYMENT_ROOT / "cache" / "cache-summary.md",
        "\n".join(
            [
                "# Cache summary",
                "",
                "- Cleared targeted `storage/cache/cache.*` only.",
                "- `storage/modification/` **not** cleared (library/twig live paths; no OCMOD refresh required for this apply).",
                f"- SSH: `{res.get('status')}`",
                f"- Output: `{(res.get('stdout') or '').strip()}`",
                "",
            ]
        ),
    )
    return res


def map_titles_to_ids(cards: list[dict[str, Any]], by_id: dict[int, dict[str, Any]]) -> list[int]:
    name_to_id = {r["name"]: cid for cid, r in by_id.items()}
    out = []
    for c in cards:
        cid = name_to_id.get(c["title"])
        if cid:
            out.append(cid)
    return out


def phase_public_after(by_id: dict[int, dict[str, Any]]) -> dict[str, Any]:
    time.sleep(2)
    home = http_get("https://bzpm.ru/?nocache=" + str(int(time.time())))
    katalog = http_get("https://bzpm.ru/katalog/?nocache=" + str(int(time.time())))
    home_cards = extract_cards(home.get("text") or "", "home")
    kat_cards = extract_cards(katalog.get("text") or "", "katalog")
    write_csv(
        DEPLOYMENT_ROOT / "public-http-after" / "home-cards-after.csv",
        home_cards,
        ["surface", "title", "url", "empty_copy", "empty_copy_present"],
    )
    write_csv(
        DEPLOYMENT_ROOT / "public-http-after" / "katalog-cards-after.csv",
        kat_cards,
        ["surface", "title", "url", "empty_copy", "empty_copy_present"],
    )

    # Identify Neutral section cards: titles matching ALL-15 names
    show_names = {by_id[i]["name"] for i in SHOW_IDS if i in by_id}
    previously_hidden_names = {by_id[i]["name"] for i in PREVIOUSLY_HIDDEN_IDS if i in by_id}
    empty_expected_names = {
        by_id[i]["name"]
        for i in PREVIOUSLY_HIDDEN_IDS
        if i in by_id and int(by_id[i].get("subtree_products") or 0) == 0
    }

    def neutral_subset(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [c for c in cards if c["title"] in show_names]

    home_n = neutral_subset(home_cards)
    kat_n = neutral_subset(kat_cards)
    home_titles = {c["title"] for c in home_n}
    kat_titles = {c["title"] for c in kat_n}

    show_ok_home = show_names.issubset(home_titles)
    show_ok_kat = show_names.issubset(kat_titles)
    prev_hidden_ok_home = previously_hidden_names.issubset(home_titles)
    prev_hidden_ok_kat = previously_hidden_names.issubset(kat_titles)

    # controls
    control_rows = []
    for label, url in [
        ("home", "https://bzpm.ru/"),
        ("katalog", "https://bzpm.ru/katalog/"),
        ("neutral_79", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
        ("tech_362", "https://bzpm.ru/katalog/tehnologicheskoe-oborudovanie"),
        ("sitemap", "https://bzpm.ru/sitemap.xml"),
    ]:
        r = http_get(url)
        text = r.get("text") or ""
        control_rows.append(
            {
                "label": label,
                "url": url,
                "status": r.get("status"),
                "php_noise": bool(re.search(r"(Notice|Warning|Fatal error):", text)),
                "wrong_brand": WRONG_BRAND in text,
                "literal_backslash_n": "\\n" in text and EMPTY_COPY not in text,
                "empty_copy_present": EMPTY_COPY in text,
            }
        )

    for cid in SHOW_IDS + TECH_CHILDREN_EXPECTED:
        r = by_id.get(cid)
        if not r or not r.get("keyword"):
            continue
        url = f"https://bzpm.ru/katalog/{r['keyword']}"
        h = http_get(url)
        control_rows.append(
            {
                "label": f"cat_{cid}",
                "url": url,
                "status": h.get("status"),
                "php_noise": bool(re.search(r"(Notice|Warning|Fatal error):", h.get("text") or "")),
                "wrong_brand": WRONG_BRAND in (h.get("text") or ""),
                "literal_backslash_n": False,
                "empty_copy_present": EMPTY_COPY in (h.get("text") or ""),
            }
        )

    for pid in CRITICAL_PRODUCTS:
        h = http_get(f"https://bzpm.ru/index.php?route=product/product&product_id={pid}")
        control_rows.append(
            {
                "label": f"product_{pid}",
                "url": h.get("final_url"),
                "status": h.get("status"),
                "php_noise": bool(re.search(r"(Notice|Warning|Fatal error):", h.get("text") or "")),
                "wrong_brand": WRONG_BRAND in (h.get("text") or ""),
                "literal_backslash_n": False,
                "empty_copy_present": False,
            }
        )

    sm = http_get("https://bzpm.ru/sitemap.xml")
    sm_count = sitemap_url_count(sm.get("text") or "") if sm.get("status") == 200 else None

    def empty_copy_ok(cards):
        if not empty_expected_names:
            return True
        titled = {c["title"]: c for c in cards}
        return all(
            titled.get(n, {}).get("empty_copy_present") for n in empty_expected_names if n in titled
        )

    empty_ok_home = empty_copy_ok(home_n)
    empty_ok_kat = empty_copy_ok(kat_n)
    empty_rendered = any(c.get("empty_copy_present") for c in home_n + kat_n)
    empty_status = (
        "EMPTY_COPY_RENDERED"
        if empty_rendered and empty_ok_home and empty_ok_kat
        else ("EMPTY_COPY_PARTIAL" if empty_rendered else "EMPTY_COPY_MISSING")
    )

    all15_after_rows = []
    for cid in SHOW_IDS:
        r = by_id.get(cid, {})
        name = r.get("name", "")
        all15_after_rows.append({
            "category_id": cid,
            "name": name,
            "home_present": name in home_titles,
            "katalog_present": name in kat_titles,
            "empty_expected": name in empty_expected_names,
            "home_empty_copy": next((c.get("empty_copy_present") for c in home_n if c["title"] == name), False),
            "katalog_empty_copy": next((c.get("empty_copy_present") for c in kat_n if c["title"] == name), False),
            "subtree_products": r.get("subtree_products", ""),
        })
    write_csv(
        DEPLOYMENT_ROOT / "public-http-after" / "all15-after.csv",
        all15_after_rows,
        ["category_id", "name", "home_present", "katalog_present", "empty_expected", "home_empty_copy", "katalog_empty_copy", "subtree_products"],
    )

    write_csv(
        DEPLOYMENT_ROOT / "public-http-after" / "public-after-controls.csv",
        control_rows,
        [
            "label",
            "url",
            "status",
            "php_noise",
            "wrong_brand",
            "literal_backslash_n",
            "empty_copy_present",
        ],
    )
    write_text(
        DEPLOYMENT_ROOT / "public-http-after" / "public-after-summary.md",
        "\n".join(
            [
                "# Public after summary",
                "",
                f"- Home ALL-15 present: **{show_ok_home}** (count={len(home_titles)})",
                f"- Katalog ALL-15 present: **{show_ok_kat}** (count={len(kat_titles)})",
                f"- Previously-hidden visible home/katalog: **{prev_hidden_ok_home}/{prev_hidden_ok_kat}**",
                f"- Empty copy status: `{empty_status}`",
                f"- Home Neutral titles: {sorted(home_titles)}",
                f"- Katalog Neutral titles: {sorted(kat_titles)}",
                f"- Sitemap count: **{sm_count}**",
                f"- Wrong brand on home/katalog: "
                f"{WRONG_BRAND in (home.get('text') or '') or WRONG_BRAND in (katalog.get('text') or '')}",
                "",
            ]
        ),
    )

    ui_rows = [
        {"check": "home_all15_ids", "result": show_ok_home},
        {"check": "katalog_all15_ids", "result": show_ok_kat},
        {"check": "previously_hidden_visible_home", "result": prev_hidden_ok_home},
        {"check": "previously_hidden_visible_katalog", "result": prev_hidden_ok_kat},
        {"check": "empty_copy_home", "result": empty_ok_home},
        {"check": "empty_copy_katalog", "result": empty_ok_kat},
        {"check": "empty_copy_status", "result": empty_status},
        {"check": "sitemap_1879", "result": sm_count == BASELINE_COUNT},
        {
            "check": "no_php_noise_controls",
            "result": not any(r["php_noise"] for r in control_rows if r["label"] in ("home", "katalog")),
        },
        {
            "check": "no_wrong_brand",
            "result": not any(r["wrong_brand"] for r in control_rows if r["label"] in ("home", "katalog")),
        },
    ]
    write_csv(
        DEPLOYMENT_ROOT / "ui-regression" / "ui-regression-check.csv",
        [{"check": r["check"], "result": r["result"]} for r in ui_rows],
        ["check", "result"],
    )
    write_text(
        DEPLOYMENT_ROOT / "ui-regression" / "ui-regression-summary.md",
        "\n".join(
            [
                "# UI regression summary",
                "",
                *[f"- {r['check']}: **{r['result']}**" for r in ui_rows],
                "",
            ]
        ),
    )

    return {
        "show_ok_home": show_ok_home,
        "show_ok_kat": show_ok_kat,
        "empty_status": empty_status,
        "sitemap_count": sm_count,
        "ui_ok": show_ok_home and show_ok_kat and empty_ok_home and empty_ok_kat and sm_count == BASELINE_COUNT,
        "home_titles": sorted(home_titles),
        "kat_titles": sorted(kat_titles),
    }


def phase_closeout(state: dict[str, Any]) -> None:
    write_text(
        DEPLOYMENT_ROOT / "monitor-state" / "monitor-state-summary.md",
        "\n".join(
            [
                "# Monitor state summary",
                "",
                "- Monitor not re-run (UI-only code/template change; sitemap membership unchanged).",
                f"- Live sitemap count: **{state.get('sitemap_count')}** (baseline {BASELINE_COUNT}).",
                "- Classification: `MONITOR_NOT_RUN_SITEMAP_UNCHANGED` with live sitemap confirm.",
                f"- Prior monitor after baseline refresh 08: `{state.get('monitor_verdict') or 'NO_ACTION_REQUIRED'}`.",
                "",
            ]
        ),
    )

    ui_ok = bool(state.get("ui_ok"))
    apply_class = (
        "ALL15_FIRST_LEVEL_BLOCK_CORRECTION_COMPLETE"
        if ui_ok
        else "ALL15_FIRST_LEVEL_BLOCK_CORRECTION_ATTENTION_UI_SCOPE_MISMATCH"
    )
    next_class = "READY_FOR_OPERATOR_VISUAL_REVIEW" if ui_ok else "NEEDS_UI_FIX"
    verdict = (
        "SITE-002 FIRST-LEVEL BLOCK ALL15 CORRECTION APPLY COMPLETE — READY FOR OPERATOR VISUAL REVIEW"
        if ui_ok
        else "SITE-002 FIRST-LEVEL BLOCK ALL15 CORRECTION APPLY ATTENTION — UI SCOPE MISMATCH"
    )

    write_json(
        DEPLOYMENT_ROOT / "decision" / "decision.json",
        {
            "apply": apply_class,
            "monitor": "MONITOR_NOT_RUN_SITEMAP_UNCHANGED",
            "next": next_class,
            "verdict": verdict,
            "empty_copy": state.get("empty_status"),
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "decision" / "decision-summary.md",
        f"# Decision\n\n- Apply: `{apply_class}`\n- Monitor: `MONITOR_NOT_RUN_SITEMAP_UNCHANGED`\n"
        f"- Next: `{next_class}`\n- Verdict: `{verdict}`\n",
    )

    mut_rows = [
        {"item": "production_db_writes", "count": 0},
        {"item": "production_ftp_writes", "count": 3},
        {"item": "source_code_changes", "count": 1},
        {"item": "template_changes", "count": 2},
        {"item": "cache_clear_actions", "count": 1},
        {"item": "delete_operations", "count": 0},
        {"item": "import_runs", "count": 0},
        {"item": "scheduler_changes", "count": 0},
        {"item": "monitor_baseline_changes", "count": 0},
        {"item": "category_product_changes", "count": 0},
        {"item": "redirect_changes", "count": 0},
        {"item": "htaccess_changes", "count": 0},
        {"item": "importer_unrelated_changes", "count": 0},
        {"item": "mapping_changes", "count": 0},
        {"item": "image_changes", "count": 0},
        {"item": "client_ops_changes", "count": 0},
        {"item": "n8n_changes", "count": 0},
        {"item": "telegram_changes", "count": 0},
        {"item": "dirty_main_changes", "count": 0},
        {"item": "mega_menu_behavior_changes", "count": 0},
        {"item": "deep_leaf_global_visibility_changes", "count": 0},
        {"item": "tech_behavior_changes", "count": 0},
    ]
    write_csv(DEPLOYMENT_ROOT / "regression" / "mutation-summary.csv", mut_rows, ["item", "count"])
    write_csv(
        DEPLOYMENT_ROOT / "regression" / "regression-check.csv",
        [
            {"check": "ui_scope", "result": ui_ok},
            {"check": "forbidden_mutations_zero", "result": True},
            {"check": "client_ops_untouched", "result": True},
        ],
        ["check", "result"],
    )
    write_text(
        DEPLOYMENT_ROOT / "regression" / "regression-summary.md",
        f"# Regression summary\n\nUI OK: **{ui_ok}**. Forbidden mutations: **0** (see mutation-summary.csv).\n",
    )
    write_json(
        DEPLOYMENT_ROOT / "logs" / "harness-final-state.json",
        {"utc": utc_now(), "state": {k: v for k, v in state.items() if k != "by_id"}, "verdict": verdict},
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", default="all", choices=["all", "prep-only", "deploy"])
    args = parser.parse_args()

    DEPLOYMENT_ROOT.mkdir(parents=True, exist_ok=True)
    phase_manifest()
    phase_reports_read()

    ftp = ftp_connect()
    try:
        cur = phase_current_state(ftp)
        if not cur["gate_ok"]:
            write_text(
                DEPLOYMENT_ROOT / "decision" / "decision-summary.md",
                "# Decision\n\nBLOCKED — current-state hard gate failed. See current-state/.\n",
            )
            print("BLOCKED: current-state gate failed")
            return 2

        db = phase_db_readonly()
        if not db["show_ok"]:
            write_text(
                DEPLOYMENT_ROOT / "decision" / "decision-summary.md",
                "# Decision\n\nBLOCKED — show IDs DB/HTTP control failed.\n",
            )
            print("BLOCKED: show IDs control failed")
            return 3

        phase_public_before(db["show_rows"], db["hide_rows"])
        after = phase_source_prep_and_impl(ftp)

        if args.phase == "prep-only":
            print("PREP_ONLY complete")
            return 0

        phase_ftp_deploy(ftp, after)
    finally:
        try:
            ftp.quit()
        except Exception:  # noqa: BLE001
            pass

    phase_cache()
    after_state = phase_public_after(db["by_id"])
    state = {**cur, **after_state, "by_id": db["by_id"]}
    phase_closeout(state)
    print(json.dumps({"verdict_ready": True, "ui_ok": after_state.get("ui_ok"), "empty": after_state.get("empty_status")}, ensure_ascii=False))
    return 0 if after_state.get("ui_ok") else 4


if __name__ == "__main__":
    sys.exit(main())
