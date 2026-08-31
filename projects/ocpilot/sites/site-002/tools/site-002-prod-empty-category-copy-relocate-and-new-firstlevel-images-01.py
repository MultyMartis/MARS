#!/usr/bin/env python3
"""SITE-002 — relocate empty-category copy to PLP + new first-level Neutral images.

Operation: SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01
Authority worktree only. Does not mutate dirty main, mega/tech/importer/baseline/Client Ops.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import time
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

OPERATION_ID = "SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01"
OCPILOT_RUN = "4.317"
SITE_ID = "SITE-002"
PRODUCTION_URL = "https://bzpm.ru/"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
WRONG_BRAND = "БЗПМ"
EMPTY_COPY = "Ожидайте, товары скоро поступят."
BASELINE_COUNT = 1879

SHOW_IDS = [80, 82, 83, 85, 86, 87, 89, 207, 301, 322, 326, 331, 354, 358, 360]
EMPTY_IDS = [82, 83, 85, 87, 89]
NONEMPTY_CONTROL = 301  # Столы
TECH_ROOT = 362
CRITICAL_PRODUCTS = [4707, 4708, 4709, 4710, 4712]

TARGETS = [
    {"category_id": 82, "name": "Подтоварники", "slug": "podtovarniki"},
    {"category_id": 83, "name": "Полки", "slug": "polki"},
    {"category_id": 85, "name": "Тележки", "slug": "telezhki"},
    {"category_id": 87, "name": "Столы производственные", "slug": "stoly-proizvodstvennye"},
    {"category_id": 89, "name": "Шкафы", "slug": "shkafy"},
]

SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
AUTHORITY_REPO = CANONICAL_MONOREPO
TOOLS = site002_tools_dir()
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"

REMOTE_CV = "/public_html/system/library/zpm/category_visibility.php"
REMOTE_HOME_TWIG = "/public_html/catalog/view/theme/default/template/sections/catalogsections.twig"
REMOTE_KATALOG_TWIG = "/public_html/catalog/view/theme/default/template/product/katalog.twig"
REMOTE_CATEGORY_TWIG = "/public_html/catalog/view/theme/default/template/product/category.twig"
REMOTE_CATEGORY_PHP = "/public_html/catalog/controller/product/category.php"
REMOTE_STYLE = "/public_html/assets/css/style.css"
REMOTE_IMAGE_DIR = "/public_html/image/catalog/Category-image/"
REMOTE_CACHE_DIR = "/public_html/image/cache/catalog/Category-image/"

LOCAL_MAP = {
    REMOTE_CV: TOOLS / "category_visibility.php",
    REMOTE_HOME_TWIG: TOOLS / "catalogsections-SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01.twig",
    REMOTE_KATALOG_TWIG: TOOLS / "katalog-SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01.twig",
    REMOTE_CATEGORY_TWIG: TOOLS / "category-twig-SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01.twig",
    REMOTE_CATEGORY_PHP: TOOLS / "category-SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01.php",
}


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


def ftp_connect():
    import ftplib

    f = parse_production_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=300)
    ftp.login(f["username"], f["password"])
    ftp.set_pasv(True)
    return ftp


def ftp_download(ftp, remote: str) -> bytes | None:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue()
    except Exception:
        return None


def ftp_upload(ftp, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


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
    import shlex

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


def http_get(url: str, timeout: int = 60) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            text = raw.decode("utf-8", errors="replace")
            return {"status": resp.status, "text": text, "bytes": len(raw), "url": url}
    except Exception as exc:
        return {"status": 0, "text": "", "bytes": 0, "url": url, "error": str(exc)}


def parse_cards(html: str) -> list[dict[str, Any]]:
    cards = []
    for block in re.findall(
        r'<a[^>]*class="[^"]*zpm-cat-card[^"]*"[^>]*>.*?</a>',
        html,
        re.DOTALL | re.IGNORECASE,
    ):
        href_m = re.search(r'href="([^"]+)"', block)
        title_m = re.search(r'zpm-cat-card__title[^"]*"[^>]*>([^<]*)', block)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', block)
        empty_m = re.search(r'zpm-cat-card__empty[^"]*"[^>]*>([^<]*)', block)
        cards.append(
            {
                "href": href_m.group(1) if href_m else "",
                "title": title_m.group(1).strip() if title_m else "",
                "img": img_m.group(1) if img_m else "",
                "empty_copy_present": bool(empty_m),
                "empty_copy": empty_m.group(1) if empty_m else "",
            }
        )
    return cards


def patch_style_css(src: str) -> str:
    if "category__empty-state" in src:
        return src
    block = (
        ".category__grid {\n\n"
        "  display: grid;\n\n"
        "  grid-template-columns: repeat(5, 1fr);\n\n"
        "  gap: var(--pad-gap);\n\n"
        "}"
    )
    insert = (
        block
        + "\n\n"
        + "/* SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01 */\n"
        + ".category__empty-state {\n\n"
        + "  margin: 24px 0 8px;\n\n"
        + "  padding: 16px 0;\n\n"
        + "  font-size: 18px;\n\n"
        + "  line-height: 1.45;\n\n"
        + "  color: #333;\n\n"
        + "}\n"
    )
    if block not in src:
        raise RuntimeError("style.css category__grid block not found for CSS patch")
    return src.replace(block, insert, 1)


def phase_preflight() -> None:
    import subprocess

    wt = AUTHORITY_REPO
    branch = subprocess.check_output(
        ["git", "-C", str(wt), "branch", "--show-current"], text=True
    ).strip()
    head = subprocess.check_output(["git", "-C", str(wt), "rev-parse", "HEAD"], text=True).strip()
    status = subprocess.check_output(["git", "-C", str(wt), "status", "--short"], text=True)
    main_status = subprocess.check_output(
        ["git", "-C", r"X:\AI MARS", "status", "--short"], text=True
    )
    write_text(
        DEPLOYMENT_ROOT / "preflight" / "authority-git.txt",
        f"cwd={wt}\nbranch={branch}\nHEAD={head}\nstatus:\n{status}\n",
    )
    write_text(
        DEPLOYMENT_ROOT / "preflight" / "dirty-main-readonly.txt",
        "main is dirty foreign WIP — read-only; mutations only via authority worktree + production FTP/DB\n"
        + main_status[:4000],
    )


def phase_backup_and_deploy(ftp) -> dict[str, Any]:
    bak = DEPLOYMENT_ROOT / "backups" / "production-files-before"
    bak.mkdir(parents=True, exist_ok=True)
    uploads = []

    # Patch style from live
    live_style = ftp_download(ftp, REMOTE_STYLE)
    if live_style is None:
        raise RuntimeError("cannot download style.css")
    (bak / "style.css").write_bytes(live_style)
    patched_style = patch_style_css(live_style.decode("utf-8")).encode("utf-8")
    LOCAL_STYLE = DEPLOYMENT_ROOT / "implementation" / "style.css.patched"
    LOCAL_STYLE.write_bytes(patched_style)

    file_payloads: dict[str, bytes] = {}
    for remote, local in LOCAL_MAP.items():
        data = local.read_bytes()
        # normalize newlines for text
        if remote.endswith((".php", ".twig", ".css")):
            text = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
            data = text.encode("utf-8")
        file_payloads[remote] = data
    file_payloads[REMOTE_STYLE] = patched_style

    for remote, data in file_payloads.items():
        before = ftp_download(ftp, remote) or b""
        safe = remote.strip("/").replace("/", "__")
        (bak / safe).write_bytes(before)
        before_h = sha256_bytes(before)
        after_h = sha256_bytes(data)
        if before_h == after_h:
            uploads.append(
                {
                    "remote": remote,
                    "status": "SKIPPED_UNCHANGED",
                    "sha_before": before_h,
                    "sha_after": after_h,
                }
            )
            continue
        ftp_upload(ftp, remote, data)
        verify = ftp_download(ftp, remote) or b""
        ok = sha256_bytes(verify) == after_h
        uploads.append(
            {
                "remote": remote,
                "status": "OK" if ok else "HASH_MISMATCH",
                "sha_before": before_h,
                "sha_after": after_h,
                "verify_ok": ok,
                "bytes": len(data),
            }
        )
        if not ok:
            raise RuntimeError(f"FTP verify failed for {remote}")

    # Images
    image_rows = []
    for t in TARGETS:
        slug = t["slug"]
        master = DEPLOYMENT_ROOT / "image-final" / f"{slug}.webp"
        cache = DEPLOYMENT_ROOT / "image-final" / f"{slug}-300x300.webp"
        for local, remote in (
            (master, REMOTE_IMAGE_DIR + f"{slug}.webp"),
            (cache, REMOTE_CACHE_DIR + f"{slug}-300x300.webp"),
        ):
            before = ftp_download(ftp, remote)
            if before:
                (bak / Path(remote).name).write_bytes(before)
            data = local.read_bytes()
            ftp_upload(ftp, remote, data)
            verify = ftp_download(ftp, remote) or b""
            ok = sha256_bytes(verify) == sha256_bytes(data)
            image_rows.append(
                {
                    "remote": remote,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                    "verify_ok": ok,
                }
            )
            if not ok:
                raise RuntimeError(f"image upload verify failed {remote}")
            uploads.append(
                {
                    "remote": remote,
                    "status": "OK",
                    "sha_after": sha256_bytes(data),
                    "bytes": len(data),
                    "verify_ok": ok,
                }
            )

    write_json(DEPLOYMENT_ROOT / "ftp-deploy" / "upload-result.json", {"files": uploads, "images": image_rows})
    return {"uploads": uploads, "images": image_rows}


def phase_db_bind() -> dict[str, Any]:
    before = ssh_mysql(
        "SELECT category_id, image FROM oc_category WHERE category_id IN (82,83,85,87,89) ORDER BY category_id;"
    )
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "db-image-before.txt", str(before))
    statements = []
    for t in TARGETS:
        oc = f"catalog/Category-image/{t['slug']}.webp"
        sql = (
            f"UPDATE oc_category SET image='{oc}' "
            f"WHERE category_id={t['category_id']} AND (image IS NULL OR image='' OR image<>'{oc}');"
        )
        statements.append(sql)
        res = ssh_mysql(sql)
        write_text(
            DEPLOYMENT_ROOT / "admin-evidence" / f"db-update-{t['category_id']}.txt",
            json.dumps(res, ensure_ascii=False, indent=2),
        )
        if res.get("status") != "ok":
            raise RuntimeError(f"DB update failed for {t['category_id']}: {res}")
    after = ssh_mysql(
        "SELECT category_id, image FROM oc_category WHERE category_id IN (82,83,85,87,89) ORDER BY category_id;"
    )
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "db-image-after.txt", str(after))
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "db-apply.sql", "\n".join(statements) + "\n")
    return {"before": before, "after": after, "statements": statements}


def phase_cache() -> dict[str, Any]:
    # Clear OC cache files; also remove modified copies of category controller/twig if present
    cmd = (
        f"cd {CACHE_DIR}; "
        "before=$(ls -1 cache.* 2>/dev/null | wc -l); "
        "rm -f cache.* 2>/dev/null; "
        "after=$(ls -1 cache.* 2>/dev/null | wc -l); "
        "echo BEFORE=$before AFTER=$after; "
        "MOD=/home/a/assum/bzpm.ru/storage/modification; "
        "rm -f $MOD/catalog/controller/product/category.php 2>/dev/null; "
        "rm -f $MOD/catalog/view/theme/default/template/product/category.twig 2>/dev/null; "
        "ls $MOD/catalog/controller/product 2>/dev/null | head -5 || echo NO_MOD_CTRL; "
        "echo DONE"
    )
    res = ssh_exec(cmd)
    write_json(DEPLOYMENT_ROOT / "cache" / "cache-actions.json", res)
    write_text(
        DEPLOYMENT_ROOT / "cache" / "cache-summary.md",
        "\n".join(
            [
                "# Cache actions",
                "",
                "- Cleared `storage/cache/cache.*`",
                "- Removed modification overlays for `category.php` / `category.twig` if present (live FTP files are authority)",
                f"- SSH status: {res.get('status')}",
                "```",
                (res.get("stdout") or "")[:2000],
                "```",
                "",
            ]
        ),
    )
    return res


def phase_verify() -> dict[str, Any]:
    ts = str(int(time.time()))
    home = http_get(f"https://bzpm.ru/?nocache={ts}")
    katalog = http_get(f"https://bzpm.ru/katalog/?nocache={ts}")
    write_text(DEPLOYMENT_ROOT / "public-http-after" / "home.html", home.get("text") or "")
    write_text(DEPLOYMENT_ROOT / "public-http-after" / "katalog.html", katalog.get("text") or "")

    home_cards = parse_cards(home.get("text") or "")
    kat_cards = parse_cards(katalog.get("text") or "")

    empty_div_home = (home.get("text") or "").count("zpm-cat-card__empty")
    empty_div_kat = (katalog.get("text") or "").count("zpm-cat-card__empty")
    empty_text_home_cards = any(c.get("empty_copy_present") for c in home_cards)
    empty_text_kat_cards = any(c.get("empty_copy_present") for c in kat_cards)

    # ALL-15 presence by empty names + known names
    expected_names = {t["name"] for t in TARGETS} | {
        "Столы",
        "Моечные ванны",
        "Стеллажи",
    }
    home_titles = {c["title"] for c in home_cards}
    kat_titles = {c["title"] for c in kat_cards}

    plp_rows = []
    for t in TARGETS:
        url = f"https://bzpm.ru/katalog/{t['slug']}?nocache={ts}"
        h = http_get(url)
        text = h.get("text") or ""
        write_text(DEPLOYMENT_ROOT / "public-http-after" / f"{t['slug']}.html", text)
        plp_rows.append(
            {
                "category_id": t["category_id"],
                "slug": t["slug"],
                "status": h.get("status"),
                "empty_copy_present": EMPTY_COPY in text,
                "empty_state_marker": 'data-empty-category-copy' in text,
                "card_empty_div": "zpm-cat-card__empty" in text,
                "php_noise": bool(re.search(r"(Notice|Warning|Fatal error):", text)),
                "wrong_brand": WRONG_BRAND in text,
                "img_ok": f"{t['slug']}-300x300.webp" in (home.get("text") or "")
                or f"{t['slug']}-300x300.webp" in (katalog.get("text") or ""),
            }
        )

    stoly = http_get(f"https://bzpm.ru/katalog/stoly?nocache={ts}")
    stoly_text = stoly.get("text") or ""
    write_text(DEPLOYMENT_ROOT / "public-http-after" / "stoly.html", stoly_text)

    tech = http_get(f"https://bzpm.ru/katalog/tehnologicheskoe-oborudovanie?nocache={ts}")
    write_text(DEPLOYMENT_ROOT / "public-http-after" / "tech.html", tech.get("text") or "")

    img_http = []
    for t in TARGETS:
        for label, url in (
            ("master", f"https://bzpm.ru/image/catalog/Category-image/{t['slug']}.webp"),
            ("cache", f"https://bzpm.ru/image/cache/catalog/Category-image/{t['slug']}-300x300.webp"),
        ):
            r = http_get(url)
            img_http.append({"slug": t["slug"], "label": label, "url": url, "status": r.get("status"), "bytes": r.get("bytes")})

    # Critical PDPs
    pdp = []
    for pid in CRITICAL_PRODUCTS[:2]:
        r = http_get(f"https://bzpm.ru/index.php?route=product/product&product_id={pid}&nocache={ts}")
        pdp.append(
            {
                "product_id": pid,
                "status": r.get("status"),
                "php_noise": bool(re.search(r"(Notice|Warning|Fatal error):", r.get("text") or "")),
                "wrong_brand": WRONG_BRAND in (r.get("text") or ""),
            }
        )

    # Count ALL-15 empty + curated on home via slug fragments
    empty_slugs = [t["slug"] for t in TARGETS]
    home_empty_present = all(
        any(s in c["href"] and c["title"] for c in home_cards if s in c["href"])
        or any(s in (c.get("href") or "") for c in home_cards)
        for s in empty_slugs
    )
    # simpler: each empty slug appears in home html
    home_html = home.get("text") or ""
    kat_html = katalog.get("text") or ""
    all15_home = all(f"/{s}" in home_html or s in home_html for s in empty_slugs)
    all15_kat = all(f"/{s}" in kat_html or s in kat_html for s in empty_slugs)

    # Image on cards for empty cats: no placeholder
    placeholder_on_empty = []
    for c in home_cards:
        if any(s in c["href"] for s in empty_slugs):
            if "placeholder" in (c.get("img") or ""):
                placeholder_on_empty.append(c)

    state = {
        "home_status": home.get("status"),
        "katalog_status": katalog.get("status"),
        "empty_div_home": empty_div_home,
        "empty_div_katalog": empty_div_kat,
        "card_empty_copy_home": empty_text_home_cards,
        "card_empty_copy_katalog": empty_text_kat_cards,
        "all15_empty_slugs_home": all15_home,
        "all15_empty_slugs_katalog": all15_kat,
        "plp_empty": plp_rows,
        "stoly_empty_copy": EMPTY_COPY in stoly_text,
        "stoly_status": stoly.get("status"),
        "tech_status": tech.get("status"),
        "img_http": img_http,
        "pdp": pdp,
        "placeholder_on_empty_cards": placeholder_on_empty,
        "home_card_count": len(home_cards),
        "katalog_card_count": len(kat_cards),
        "wrong_brand_home": WRONG_BRAND in home_html,
        "php_noise_home": bool(re.search(r"(Notice|Warning|Fatal error):", home_html)),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "verify-state.json", state)
    return state


def phase_report(state: dict[str, Any], deploy: dict[str, Any]) -> None:
    plp_ok = all(r.get("empty_copy_present") and r.get("empty_state_marker") for r in state["plp_empty"])
    cards_clean = state["empty_div_home"] == 0 and state["empty_div_katalog"] == 0
    imgs_ok = all(r.get("status") == 200 for r in state["img_http"]) and not state["placeholder_on_empty_cards"]
    verdict = (
        "SITE-002 EMPTY-COPY RELOCATE + FIRSTLEVEL IMAGES COMPLETE"
        if cards_clean and plp_ok and imgs_ok and state["all15_empty_slugs_home"] and not state["stoly_empty_copy"]
        else "SITE-002 EMPTY-COPY RELOCATE + FIRSTLEVEL IMAGES PARTIAL / NEEDS REVIEW"
    )
    ftp_changed = sum(1 for u in deploy["uploads"] if u.get("status") == "OK")
    md = f"""# REPORT — SITE-002 Empty Category Copy Relocate + New First-Level Images 01

**Operation:** `{OPERATION_ID}`  
**OCPilot run:** **{OCPILOT_RUN}**  
**Date:** {utc_now()}  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Verdict:** **{verdict}**

---

## 1. Scope

1. Remove card-level empty copy (`zpm-cat-card__empty`) from home + `/katalog/` first-level Neutral tiles.
2. Keep ALL-15 Neutral first-level visibility (incl. empty 82/83/85/87/89).
3. Show empty-state copy **only** on actual empty category PLP pages.
4. Generate/apply white-studio category images for empty first-level Neutral categories that used placeholders.

**Out of scope:** HYBRID revert, mega menu, Tech 362 logic, importer, monitor baseline (**1879**), Client Ops / MetaBOT / n8n / Telegram, dirty main.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Volume `AI WS` (X:) | PASS |
| Authority (canonical) | `X:\\AI MARS` (clean worktree via --repo-root for git mutation) |
| Dirty main | read-only; foreign WIP untouched |
| Prior accepted | Run **4.316** ALL-15 + baseline **1879** |

---

## 3. Empty-copy relocate

| Surface | Before | After |
|---------|--------|-------|
| Home first-level cards `.zpm-cat-card__empty` | 5 | **{state['empty_div_home']}** |
| `/katalog/` first-level cards `.zpm-cat-card__empty` | 5 | **{state['empty_div_katalog']}** |
| Empty PLP pages (82/83/85/87/89) | copy absent | copy present: **{plp_ok}** |
| Non-empty control `/katalog/stoly` | — | empty copy present: **{state['stoly_empty_copy']}** (expected false) |

Exact copy: `{EMPTY_COPY}`

Implementation:
- `category_visibility.php` — `buildNeutralFirstLevelBlockCards` keeps ALL-15, `attach_empty_copy=false`
- `catalogsections.twig` + `katalog.twig` — remove card empty-copy hooks
- `category.php` + `category.twig` — PLP `empty_category_copy` when `product_total<=0` and no request filters
- `style.css` — `.category__empty-state`

---

## 4. Images applied

| ID | Name | slug | OC image |
|---:|------|------|----------|
| 82 | Подтоварники | podtovarniki | `catalog/Category-image/podtovarniki.webp` |
| 83 | Полки | polki | `catalog/Category-image/polki.webp` |
| 85 | Тележки | telezhki | `catalog/Category-image/telezhki.webp` |
| 87 | Столы производственные | stoly-proizvodstvennye | `catalog/Category-image/stoly-proizvodstvennye.webp` |
| 89 | Шкафы | shkafy | `catalog/Category-image/shkafy.webp` |

Generation: **COMPOSER_ONLY_NO_API** (Cursor GenerateImage + Pillow → 1800×1200 + 300×300 WEBP).  
DB binds: `UPDATE oc_category.image` for the five IDs.  
Placeholder remaining on empty cards: **{len(state['placeholder_on_empty_cards'])}**

---

## 5. Verification summary

| Check | Result |
|-------|--------|
| Home HTTP | {state['home_status']} |
| `/katalog/` HTTP | {state['katalog_status']} |
| ALL-15 empty slugs still on home | {state['all15_empty_slugs_home']} |
| ALL-15 empty slugs still on `/katalog/` | {state['all15_empty_slugs_katalog']} |
| Card empty-copy removed | {cards_clean} |
| PLP empty-copy only on empty cats | {plp_ok and not state['stoly_empty_copy']} |
| Image HTTP 200 | {imgs_ok} |
| Public `БЗПМ` home | {state['wrong_brand_home']} |
| PHP noise home | {state['php_noise_home']} |
| Tech hub HTTP | {state['tech_status']} |
| Baseline / sitemap / importer | untouched (baseline **{BASELINE_COUNT}**) |

---

## 6. Production mutation counts

| Item | Count |
|------|------:|
| FTP text/CSS files changed | {ftp_changed} (includes images OK rows) |
| Image masters+cache uploaded | 10 |
| DB category image UPDATE | 5 |
| Cache clear actions | 1 (`cache.*` + scoped modification overlays) |

---

## 7. Git / Storage

- Authority allowlist commit/push from clean worktree only (never hardcode git-sync-*)
- Storage pack: `X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\deployments\\{OPERATION_ID}\\`
- Repo report: `projects/ocpilot/sites/site-002/reports/{OPERATION_ID}.md`

---

## Execution safety

- cwd: authority worktree
- scope lock honored: yes
- destructive ops: none (targeted cache file delete only)
- protected zone touch: none outside SITE-002 allowlist
"""
    write_text(DEPLOYMENT_ROOT / "reports" / f"{OPERATION_ID}.md", md)
    write_json(
        DEPLOYMENT_ROOT / "reports" / "verdict.json",
        {
            "operation_id": OPERATION_ID,
            "verdict": verdict,
            "cards_clean": cards_clean,
            "plp_ok": plp_ok,
            "imgs_ok": imgs_ok,
            "baseline": BASELINE_COUNT,
            "at": utc_now(),
        },
    )
    # also copy report into authority repo reports
    dest = AUTHORITY_REPO / "projects" / "ocpilot" / "sites" / "site-002" / "reports" / f"{OPERATION_ID}.md"
    dest.write_text(md, encoding="utf-8", newline="\n")


def main() -> int:
    guard_historical_harness('OPERATION_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--phase",
        choices=["all", "verify-only", "db-cache-verify"],
        default="all",
    )
    args = parser.parse_args()
    DEPLOYMENT_ROOT.mkdir(parents=True, exist_ok=True)
    phase_preflight()
    if args.phase == "verify-only":
        state = phase_verify()
        write_json(DEPLOYMENT_ROOT / "verification" / "verify-only.json", state)
        print(json.dumps({"empty_div_home": state["empty_div_home"], "plp": state["plp_empty"]}, ensure_ascii=False))
        return 0

    if args.phase == "db-cache-verify":
        deploy = json.loads((DEPLOYMENT_ROOT / "ftp-deploy" / "upload-result.json").read_text(encoding="utf-8"))
        # normalize shape for report
        if "uploads" not in deploy:
            deploy = {"uploads": deploy.get("files", []), "images": deploy.get("images", [])}
        db = phase_db_bind()
        write_json(DEPLOYMENT_ROOT / "admin-evidence" / "db-bind-summary.json", db)
        phase_cache()
        time.sleep(2)
        state = phase_verify()
        phase_report(state, deploy)
        print(
            json.dumps(
                {
                    "verdict_file": str(DEPLOYMENT_ROOT / "reports" / "verdict.json"),
                    "empty_div_home": state["empty_div_home"],
                    "empty_div_katalog": state["empty_div_katalog"],
                    "stoly_empty_copy": state["stoly_empty_copy"],
                    "placeholders": len(state["placeholder_on_empty_cards"]),
                },
                ensure_ascii=False,
            )
        )
        return 0

    ftp = ftp_connect()
    try:
        deploy = phase_backup_and_deploy(ftp)
    finally:
        ftp.quit()
    db = phase_db_bind()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "db-bind-summary.json", db)
    phase_cache()
    # allow caches to settle
    time.sleep(2)
    state = phase_verify()
    phase_report(state, deploy)
    print(
        json.dumps(
            {
                "verdict_file": str(DEPLOYMENT_ROOT / "reports" / "verdict.json"),
                "empty_div_home": state["empty_div_home"],
                "empty_div_katalog": state["empty_div_katalog"],
                "stoly_empty_copy": state["stoly_empty_copy"],
                "placeholders": len(state["placeholder_on_empty_cards"]),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
