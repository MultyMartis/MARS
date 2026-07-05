#!/usr/bin/env python3
"""SITE-002 duplicate body/preloader fix — single-file Production deploy."""
from __future__ import annotations

import argparse
import difflib
import ftplib
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-ROBOTS-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-HTML-BODY-FIX-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01"

REMOTE_HEADER = "/public_html/catalog/view/theme/default/template/common/header.twig"
REMOTE_FOOTER = "/public_html/catalog/view/theme/default/template/common/footer.twig"

LIVE_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/guarantee",
]

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification/pre-upload",
    "verification/after-upload",
    "html-before",
    "html-after",
    "screenshots",
    "manifests",
    "logs",
)

DUPLICATE_BLOCK = """

<body class="{{ bodyclass }}">

  <!-- GLOBAL PAGE PRELOADER -->
<div class="zpm-preloader" data-preloader aria-hidden="false">
  <div class="zpm-preloader__inner">
    <div class="zpm-preloader__bar">
      <span class="zpm-preloader__line" data-preloader-line></span>
    </div>

    <div class="zpm-preloader__percent" data-preloader-percent>0%</div>
  </div>
</div>

<div class="page_overlay" data-overlay aria-hidden="true"></div>
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def mask_id(value: str) -> str:
    if not value:
        return "***"
    if len(value) <= 6:
        return value[:1] + "***" + value[-1:]
    return value[:3] + "***" + value[-3:]


def mask_html(text: str) -> str:
    out = re.sub(r"ym\s*\(\s*(\d+)", lambda m: f"ym({mask_id(m.group(1))}", text)
    out = re.sub(
        r'yandex-verification["\']?\s*content=["\']([^"\']+)',
        lambda m: f'yandex-verification" content="{mask_id(m.group(1))}"',
        out,
        flags=re.I,
    )
    out = re.sub(
        r"mc\.yandex\.ru/metrika/tag\.js\?id=(\d+)",
        lambda m: f"mc.yandex.ru/metrika/tag.js?id={mask_id(m.group(1))}",
        out,
    )
    return out


def parse_production_secrets(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    ftp_match = re.search(r"^### FTP / SFTP\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not ftp_match:
        raise RuntimeError("PRODUCTION FTP / SFTP subsection not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in ftp_match.group(1).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current_key = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current_key, "")
            continue
        if current_key:
            fields[current_key] = stripped
    return fields


def ftp_connect(fields: dict[str, str]) -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes:
    chunks: list[bytes] = []
    ftp.retrbinary(f"RETR {remote_path}", chunks.append)
    return b"".join(chunks)


def ftp_upload(ftp: ftplib.FTP, remote_path: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote_path}", BytesIO(data))


def ensure_dirs() -> None:
    for name in SUBDIRS:
        (DEPLOYMENT_ROOT / name).mkdir(parents=True, exist_ok=True)


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache", "Accept": "text/html,*/*"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            return {"url": url, "status_code": response.status, "body": body.decode(charset, errors="replace"), "error": None}
    except urllib.error.HTTPError as exc:
        body = exc.read()
        charset = exc.headers.get_content_charset() or "utf-8"
        return {"url": url, "status_code": exc.code, "body": body.decode(charset, errors="replace"), "error": str(exc)}
    except Exception as exc:
        return {"url": url, "status_code": None, "body": "", "error": str(exc)}


def analyze_html_structure(url: str, html_text: str, status_code: int | None) -> dict[str, Any]:
    lower = html_text.lower()
    return {
        "url": url,
        "status_code": status_code,
        "http_ok": status_code == 200,
        "html_open": len(re.findall(r"<html\b", html_text, re.I)),
        "html_close": lower.count("</html>"),
        "head_open": len(re.findall(r"<head\b", html_text, re.I)),
        "head_close": lower.count("</head>"),
        "body_open": len(re.findall(r"<body\b", html_text, re.I)),
        "body_close": lower.count("</body>"),
        "zpm_preloader": lower.count("zpm-preloader"),
        "page_overlay": lower.count("page_overlay"),
        "yandex_metrika": bool(re.search(r"mc\.yandex|tag\.js|ym\(", html_text)),
        "yandex_webmaster": bool(re.search(r"yandex-verification", html_text, re.I)),
        "twig_error_visible": bool(re.search(r"(twig\s+error|syntax\s+error|fatal\s+error)", lower)),
        "load_more_visible": "pagination__more" in lower or "показать ещё" in lower,
    }


def analyze_twig_markers(remote_path: str, text: str) -> dict[str, Any]:
    lower = text.lower()
    body_lines = [i + 1 for i, line in enumerate(text.splitlines()) if "<body" in line.lower()]
    return {
        "remote_path": remote_path,
        "contains_body": "<body" in lower,
        "body_line_numbers": body_lines,
        "body_count": len(body_lines),
        "contains_preloader": "zpm-preloader" in lower,
        "contains_overlay": "page_overlay" in lower,
        "contains_yandex_metrika": any(t in lower for t in ("ym(", "mc.yandex", "metrika", "tag.js")),
        "contains_yandex_webmaster": "yandex-verification" in lower,
        "duplicate_block_present": len(re.findall(r"<body\b", text, re.I)) > 1,
        "classification": "CHANGE_TARGET"
        if remote_path == REMOTE_HEADER and len(re.findall(r"<body\b", text, re.I)) > 1
        else "READ_ONLY",
    }


def yandex_block_hash(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        low = line.lower()
        if any(t in low for t in ("yandex-verification", "ym(", "mc.yandex", "metrika", "tag.js", "noscript")):
            lines.append(line.strip())
    return sha256_bytes("\n".join(lines).encode("utf-8"))


def write_operation_manifest() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "baseline_after": BASELINE_AFTER,
            "change_type": "html-duplicate-body-fix",
            "remote_changes_allowed": True,
            "twig_changes_allowed": "true_targeted_only",
            "yandex_blocks_protected": True,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "meta_change_allowed": False,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "cron_change_allowed": False,
            "import_execution_allowed": False,
            "authorized_remote_files": [REMOTE_HEADER],
        },
    )


def phase_html_before() -> list[dict[str, Any]]:
    ensure_dirs()
    write_operation_manifest()
    results: list[dict[str, Any]] = []
    for url in LIVE_URLS:
        resp = http_get(url)
        slug = re.sub(r"https?://[^/]+/?", "", url).strip("/") or "home"
        slug = re.sub(r"[^\w\-]+", "_", slug)
        raw_path = DEPLOYMENT_ROOT / "html-before" / f"{slug}.html"
        raw_path.write_text(resp["body"], encoding="utf-8")
        masked_path = DEPLOYMENT_ROOT / "html-before" / f"{slug}.masked.html"
        masked_path.write_text(mask_html(resp["body"]), encoding="utf-8")
        analysis = analyze_html_structure(url, resp["body"], resp["status_code"])
        analysis["saved_raw"] = str(raw_path)
        results.append(analysis)
    write_json(DEPLOYMENT_ROOT / "verification" / "html-structure-before.json", {"timestamp": utc_now(), "pages": results})
    md = ["# HTML structure before", "", f"Timestamp: {utc_now()}", ""]
    for page in results:
        md.append(f"## {page['url']}")
        md.append(f"- HTTP: {page['status_code']}")
        md.append(f"- body_open: {page['body_open']} / body_close: {page['body_close']}")
        md.append(f"- zpm_preloader: {page['zpm_preloader']} / page_overlay: {page['page_overlay']}")
        md.append(f"- Yandex Metrika: {page['yandex_metrika']} / Webmaster: {page['yandex_webmaster']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "verification" / "html-structure-before.md", "\n".join(md))
    return results


def phase_discovery() -> dict[str, Any]:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    candidates: list[dict[str, Any]] = []
    try:
        for remote in (REMOTE_HEADER, REMOTE_FOOTER):
            data = ftp_download(ftp, remote)
            local_name = remote.rsplit("/", 1)[-1]
            dest = DEPLOYMENT_ROOT / "source" / local_name
            dest.write_bytes(data)
            text = data.decode("utf-8", errors="replace")
            entry = analyze_twig_markers(remote, text)
            entry["sha256"] = sha256_bytes(data)
            entry["size"] = len(data)
            entry["likely_source_of_duplicate"] = entry["body_count"] > 1
            candidates.append(entry)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    discovery = {
        "timestamp": utc_now(),
        "operation_id": OPERATION_ID,
        "candidates": candidates,
        "change_target": REMOTE_HEADER,
        "root_cause_summary": "Duplicate <body> + preloader + overlay block within header.twig lines 113-126",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-discovery.json", discovery)
    md = [
        "# Source discovery",
        "",
        f"Timestamp: {utc_now()}",
        "",
        "## Candidates",
        "",
    ]
    for c in candidates:
        md.extend(
            [
                f"### {c['remote_path']}",
                f"- classification: {c['classification']}",
                f"- body_count: {c['body_count']} (lines: {c['body_line_numbers']})",
                f"- duplicate_block_present: {c['duplicate_block_present']}",
                f"- Yandex Metrika: {c['contains_yandex_metrika']} / Webmaster: {c['contains_yandex_webmaster']}",
                "",
            ]
        )
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-discovery.md", "\n".join(md))
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "root-cause.md",
        "\n".join(
            [
                "# Root cause",
                "",
                "## First body/preloader",
                "- File: header.twig",
                "- Lines: 96-109 — canonical block immediately after </head>",
                "",
                "## Duplicate body/preloader",
                "- File: header.twig",
                "- Lines: 113-126 — exact duplicate within same file",
                "",
                "## Include composition",
                "- Duplicate is within the same file, not from a second include.",
                "",
                "## Yandex code location",
                "- Webmaster meta: header.twig head section (line ~21) — outside duplicate block",
                "- Metrika: footer.twig — unchanged",
                "",
                "## Minimal safe fix",
                "- Remove duplicate block lines 111-126 (blank lines + second body/preloader/overlay)",
                "- Keep first canonical body/preloader/overlay block",
            ]
        ),
    )
    return discovery


def prepare_header(source: str) -> tuple[str, dict[str, Any]]:
    checks: dict[str, Any] = {}
    body_matches = list(re.finditer(r"<body\b", source, re.I))
    checks["body_count_before"] = len(body_matches)
    if len(body_matches) != 2:
        checks["status"] = "FAIL"
        checks["error"] = f"expected exactly 2 body tags before fix, found {len(body_matches)}"
        return source, checks

    first_overlay = re.search(
        r'<div class="page_overlay" data-overlay aria-hidden="true"></div>',
        source,
    )
    if not first_overlay:
        checks["status"] = "FAIL"
        checks["error"] = "first page_overlay block not found"
        return source, checks

    second_body_start = body_matches[1].start()
    second_overlay = re.search(
        r'<div class="page_overlay" data-overlay aria-hidden="true"></div>',
        source[second_body_start:],
    )
    if not second_overlay:
        checks["status"] = "FAIL"
        checks["error"] = "second page_overlay block not found"
        return source, checks

    remove_start = first_overlay.end()
    remove_end = second_body_start + second_overlay.end()
    gap = source[remove_start:remove_end]
    if "<body" not in gap.lower() or "zpm-preloader" not in gap.lower():
        checks["status"] = "FAIL"
        checks["error"] = "removal window does not contain expected duplicate block"
        return source, checks

    prepared = source[:remove_start] + "\n\n" + source[remove_end:].lstrip("\r\n")
    checks["body_count_after"] = len(re.findall(r"<body\b", prepared, re.I))
    checks["preloader_count_before"] = source.lower().count("zpm-preloader")
    checks["preloader_count_after"] = prepared.lower().count("zpm-preloader")
    checks["overlay_count_before"] = source.lower().count("page_overlay")
    checks["overlay_count_after"] = prepared.lower().count("page_overlay")
    checks["yandex_hash_before"] = yandex_block_hash(source)
    checks["yandex_hash_after"] = yandex_block_hash(prepared)
    checks["yandex_unchanged"] = checks["yandex_hash_before"] == checks["yandex_hash_after"]
    checks["removed_chars"] = len(gap)
    checks["status"] = (
        "PASS"
        if checks["body_count_after"] == 1
        and checks["preloader_count_after"] == checks["preloader_count_before"] // 2
        and checks["overlay_count_after"] == 1
        and checks["yandex_unchanged"]
        else "FAIL"
    )
    return prepared, checks


def phase_backup_prepare() -> dict[str, Any]:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    try:
        data = ftp_download(ftp, REMOTE_HEADER)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    source_text = data.decode("utf-8", errors="replace")
    sha = sha256_bytes(data)
    for folder in ("backup", "rollback", "source"):
        (DEPLOYMENT_ROOT / folder / "header.twig").write_bytes(data)

    prepared_text, checks = prepare_header(source_text)
    if checks["status"] != "PASS":
        raise RuntimeError(f"Prepare failed: {checks}")

    prepared_bytes = prepared_text.encode("utf-8")
    (DEPLOYMENT_ROOT / "prepared" / "header.twig").write_bytes(prepared_bytes)

    diff_lines = list(
        difflib.unified_diff(
            source_text.splitlines(),
            prepared_text.splitlines(),
            fromfile="backup/header.twig",
            tofile="prepared/header.twig",
            lineterm="",
        )
    )
    write_text(DEPLOYMENT_ROOT / "manifests" / "dry-run.md", "\n".join(["# Dry-run diff", ""] + diff_lines))
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.json",
        {
            "timestamp": utc_now(),
            "files_to_upload": [REMOTE_HEADER],
            "removed_lines": sum(1 for line in diff_lines if line.startswith("-") and not line.startswith("---")),
            "added_lines": sum(1 for line in diff_lines if line.startswith("+") and not line.startswith("+++")),
            "checks": checks,
            "yandex_unchanged": checks["yandex_unchanged"],
            "rollback_file": str(DEPLOYMENT_ROOT / "rollback" / "header.twig"),
        },
    )

    yandex_md = ["# Yandex blocks before edit (masked)", ""]
    for i, line in enumerate(source_text.splitlines(), 1):
        low = line.lower()
        if any(t in low for t in ("yandex-verification", "ym(", "mc.yandex", "metrika")):
            masked = line
            masked = re.sub(r'content="([^"]+)"', lambda m: f'content="{mask_id(m.group(1))}"', masked)
            masked = re.sub(r"ym\s*\(\s*(\d+)", lambda m: f"ym({mask_id(m.group(1))}", masked)
            yandex_md.append(f"Line {i}: {masked.strip()}")
    write_text(DEPLOYMENT_ROOT / "verification" / "yandex-blocks-before.md", "\n".join(yandex_md))

    backup_record = {
        "timestamp": utc_now(),
        "remote_path": REMOTE_HEADER,
        "sha256_source": sha,
        "sha256_backup": sha256_file(DEPLOYMENT_ROOT / "backup" / "header.twig"),
        "sha256_rollback": sha256_file(DEPLOYMENT_ROOT / "rollback" / "header.twig"),
        "sha256_prepared": sha256_bytes(prepared_bytes),
        "hashes_match_source_backup_rollback": sha
        == sha256_file(DEPLOYMENT_ROOT / "backup" / "header.twig")
        == sha256_file(DEPLOYMENT_ROOT / "rollback" / "header.twig"),
        "prepare_checks": checks,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "backup-record.json", backup_record)
    return backup_record


def phase_deploy() -> dict[str, Any]:
    backup_sha = sha256_file(DEPLOYMENT_ROOT / "backup" / "header.twig")
    prepared_bytes = (DEPLOYMENT_ROOT / "prepared" / "header.twig").read_bytes()
    prepared_sha = sha256_bytes(prepared_bytes)

    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    try:
        pre_upload = ftp_download(ftp, REMOTE_HEADER)
        pre_sha = sha256_bytes(pre_upload)
        (DEPLOYMENT_ROOT / "verification" / "pre-upload" / "header.twig").write_bytes(pre_upload)
        if pre_sha != backup_sha:
            raise RuntimeError(f"STOP — LIVE FILE CHANGED SINCE BACKUP: backup={backup_sha} live={pre_sha}")

        ftp_upload(ftp, REMOTE_HEADER, prepared_bytes)
        after_upload = ftp_download(ftp, REMOTE_HEADER)
        after_sha = sha256_bytes(after_upload)
        (DEPLOYMENT_ROOT / "verification" / "after-upload" / "header.twig").write_bytes(after_upload)
        if after_sha != prepared_sha:
            raise RuntimeError(f"Upload hash mismatch: prepared={prepared_sha} remote={after_sha}")
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    result = {
        "timestamp": utc_now(),
        "remote_uploads": 1,
        "remote_path": REMOTE_HEADER,
        "pre_upload_sha256": pre_sha,
        "prepared_sha256": prepared_sha,
        "after_upload_sha256": after_sha,
        "upload_verified": after_sha == prepared_sha,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-result.json", result)
    return result


def phase_html_after() -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for url in LIVE_URLS:
        resp = http_get(url)
        slug = re.sub(r"https?://[^/]+/?", "", url).strip("/") or "home"
        slug = re.sub(r"[^\w\-]+", "_", slug)
        raw_path = DEPLOYMENT_ROOT / "html-after" / f"{slug}.html"
        raw_path.write_text(resp["body"], encoding="utf-8")
        masked_path = DEPLOYMENT_ROOT / "html-after" / f"{slug}.masked.html"
        masked_path.write_text(mask_html(resp["body"]), encoding="utf-8")
        analysis = analyze_html_structure(url, resp["body"], resp["status_code"])
        results.append(analysis)

    all_pass = all(
        p["http_ok"] and p["body_open"] == 1 and p["body_close"] == 1 and p["yandex_metrika"] and p["yandex_webmaster"]
        for p in results
    )
    payload = {"timestamp": utc_now(), "pages": results, "all_pass": all_pass}
    write_json(DEPLOYMENT_ROOT / "verification" / "html-structure-after.json", payload)
    md = ["# HTML structure after", "", f"Timestamp: {utc_now()}", f"All pass: {all_pass}", ""]
    for page in results:
        md.append(f"## {page['url']}")
        md.append(f"- HTTP: {page['status_code']}")
        md.append(f"- body_open: {page['body_open']} / body_close: {page['body_close']}")
        md.append(f"- zpm_preloader: {page['zpm_preloader']} / page_overlay: {page['page_overlay']}")
        md.append(f"- Yandex Metrika: {page['yandex_metrika']} / Webmaster: {page['yandex_webmaster']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "verification" / "html-structure-after.md", "\n".join(md))
    return results


def phase_rollback() -> dict[str, Any]:
    rollback_bytes = (DEPLOYMENT_ROOT / "rollback" / "header.twig").read_bytes()
    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    try:
        ftp_upload(ftp, REMOTE_HEADER, rollback_bytes)
        restored = ftp_download(ftp, REMOTE_HEADER)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass
    result = {
        "timestamp": utc_now(),
        "restored_sha256": sha256_bytes(restored),
        "rollback_sha256": sha256_bytes(rollback_bytes),
        "verified": sha256_bytes(restored) == sha256_bytes(rollback_bytes),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "rollback-result.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument(
        "phase",
        choices=["html-before", "discovery", "prepare", "deploy", "html-after", "rollback", "run-all"],
    )
    args = parser.parse_args()

    if args.phase == "html-before":
        phase_html_before()
    elif args.phase == "discovery":
        phase_discovery()
    elif args.phase == "prepare":
        phase_backup_prepare()
    elif args.phase == "deploy":
        phase_deploy()
    elif args.phase == "html-after":
        phase_html_after()
    elif args.phase == "rollback":
        phase_rollback()
    elif args.phase == "run-all":
        before = phase_html_before()
        if not all(p["body_open"] == 2 for p in before):
            print("WARNING: duplicate body not confirmed on all pages before fix", file=sys.stderr)
        phase_discovery()
        phase_backup_prepare()
        phase_deploy()
        after = phase_html_after()
        if not all(p["body_open"] == 1 and p["body_close"] == 1 for p in after):
            print("POST-DEPLOY FAIL — rolling back", file=sys.stderr)
            phase_rollback()
            return 1
        print("SITE-002 HTML BODY DUPLICATE FIX COMPLETE — LIVE HTML VALIDATED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
