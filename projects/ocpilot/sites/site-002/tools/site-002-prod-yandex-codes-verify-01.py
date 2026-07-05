#!/usr/bin/env python3
"""SITE-002 Yandex Metrika / Webmaster codes — read-only verification."""
from __future__ import annotations

import argparse
import ftplib
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-YANDEX-CODES-VERIFY-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-ROBOTS-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-YANDEX-CODES-VERIFY-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-YANDEX-CODES-VERIFY-01 (read-only)"

TWIG_PATHS = [
    "/public_html/catalog/view/theme/default/template/common/header.twig",
    "/public_html/catalog/view/theme/default/template/common/footer.twig",
]

THEME_SEARCH_PATHS = [
    "/public_html/catalog/view/theme/default/template/common/",
]

LIVE_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/guarantee",
]

SUBDIRS = ("source", "html", "verification", "manifests", "reports")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)


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
    host = fields["host"]
    port = int(fields.get("port") or 21)
    ftp = ftplib.FTP()
    ftp.connect(host, port, timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes:
    buf: list[bytes] = []

    def collect(data: bytes) -> None:
        buf.append(data)

    ftp.retrbinary("RETR " + remote_path, collect)
    return b"".join(buf)


def ftp_list_dir(ftp: ftplib.FTP, remote_dir: str) -> list[str]:
    try:
        return ftp.nlst(remote_dir)
    except ftplib.error_perm:
        return []


def mask_id(value: str) -> str:
    if not value:
        return "***"
    if len(value) <= 6:
        return value[:1] + "***" + value[-1:]
    return value[:3] + "***" + value[-3:]


def mask_html(text: str) -> str:
    """Sanitize HTML for repo-safe storage — mask Yandex IDs/tokens."""

    def repl_counter(m: re.Match[str]) -> str:
        return f"ym({mask_id(m.group(1))}"

    def repl_verify(m: re.Match[str]) -> str:
        return f'yandex-verification" content="{mask_id(m.group(1))}"'

    def repl_tag_js(m: re.Match[str]) -> str:
        return f"mc.yandex.ru/metrika/tag.js?id={mask_id(m.group(1))}"

    out = re.sub(r"ym\s*\(\s*(\d+)", repl_counter, text)
    out = re.sub(
        r'yandex-verification["\']?\s*content=["\']([^"\']+)["\']',
        repl_verify,
        out,
        flags=re.I,
    )
    out = re.sub(r"mc\.yandex\.ru/metrika/tag\.js\?id=(\d+)", repl_tag_js, out)
    out = re.sub(r"watch/(\d+)", lambda m: f"watch/{mask_id(m.group(1))}", out)
    return out


def infer_location(line: str, remote_path: str) -> str:
    lower = line.lower()
    fname = remote_path.rsplit("/", 1)[-1].lower()
    if "noscript" in lower:
        return "noscript"
    if fname == "header.twig":
        return "head"
    if fname == "footer.twig":
        return "footer/body-end"
    if "<head" in lower or "</head>" in lower:
        return "head"
    return "body"


def analyze_twig_line(remote_path: str, line: str, line_number: int) -> dict[str, Any] | None:
    lower = line.lower()
    code_type = None
    if any(t in lower for t in ("ym(", "yandex.metrika", "mc.yandex", "metrika", "tag.js")):
        code_type = "YANDEX_METRIKA"
    elif any(t in lower for t in ("yandex-verification", "yandex_webmaster", "webmaster")):
        code_type = "YANDEX_WEBMASTER"
    elif "яндекс" in lower and ("metrika" in lower or "метрика" in lower):
        code_type = "YANDEX_METRIKA"
    if not code_type:
        return None

    counter_match = re.search(r"ym\s*\(\s*(\d+)", line)
    if not counter_match:
        counter_match = re.search(r"tag\.js\?id=(\d+)", line)
    if not counter_match:
        counter_match = re.search(r"watch/(\d+)", line)
    verify_match = re.search(
        r'yandex-verification["\']?\s*content=["\']([^"\']+)', line, re.I
    )
    return {
        "remote_path": remote_path,
        "code_type": code_type,
        "line_number": line_number,
        "approximate_location": infer_location(line, remote_path),
        "line_summary": line.strip()[:140],
        "masked_id": mask_id(counter_match.group(1))
        if counter_match
        else (mask_id(verify_match.group(1)) if verify_match else None),
        "protection_rule": "OPERATOR WIP — DO NOT OVERWRITE",
    }


def analyze_twig_content(remote_path: str, content: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for idx, line in enumerate(content.splitlines(), start=1):
        hit = analyze_twig_line(remote_path, line, idx)
        if hit:
            findings.append(hit)
    return findings


def analyze_html_page(url: str, html_text: str, status_code: int | None) -> dict[str, Any]:
    lower = html_text.lower()
    twig_error = bool(re.search(r"(twig\s+error|syntax\s+error|fatal\s+error)", lower))

    metrika_script = bool(
        re.search(r"mc\.yandex\.ru/metrika/tag\.js", lower)
        or re.search(r"ym\s*\(\s*\d+", html_text)
    )
    metrika_noscript = bool(re.search(r"mc\.yandex\.ru/watch/\d+", lower))
    webmaster = bool(re.search(r'name=["\']yandex-verification["\']', lower))

    counter_ids = [mask_id(m.group(1)) for m in re.finditer(r"ym\s*\(\s*(\d+)", html_text)]
    if not counter_ids:
        counter_ids = [
            mask_id(m.group(1))
            for m in re.finditer(r"tag\.js\?id=(\d+)", html_text, re.I)
        ]
    verify_ids = [
        mask_id(m.group(1))
        for m in re.finditer(
            r'yandex-verification["\']?\s*content=["\']([^"\']+)', html_text, re.I
        )
    ]

    metrika_occurrences = len(re.findall(r"mc\.yandex\.ru/metrika/tag\.js", lower)) + len(
        re.findall(r"ym\s*\(\s*\d+", html_text)
    )
    webmaster_occurrences = len(
        re.findall(r'name=["\']yandex-verification["\']', lower)
    )

    return {
        "url": url,
        "status_code": status_code,
        "http_ok": status_code == 200,
        "twig_error_visible": twig_error,
        "yandex_metrika_script": metrika_script,
        "yandex_metrika_noscript": metrika_noscript,
        "yandex_webmaster_verification": webmaster,
        "masked_counter_ids": sorted(set(counter_ids)),
        "masked_verification_ids": sorted(set(verify_ids)),
        "metrika_occurrence_count": metrika_occurrences,
        "webmaster_occurrence_count": webmaster_occurrences,
        "duplicate_metrika": metrika_occurrences > 1,
        "duplicate_webmaster": webmaster_occurrences > 1,
    }


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Cache-Control": "no-cache",
            "Accept": "text/html,*/*",
        },
    )
    started = utc_now()
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "url": url,
                "checked_at": started,
                "status_code": response.status,
                "body": text,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        charset = exc.headers.get_content_charset() or "utf-8"
        text = body.decode(charset, errors="replace")
        return {
            "url": url,
            "checked_at": started,
            "status_code": exc.code,
            "body": text,
            "error": str(exc),
        }
    except Exception as exc:
        return {
            "url": url,
            "checked_at": started,
            "status_code": None,
            "body": "",
            "error": str(exc),
        }


def phase_twig(ftp: ftplib.FTP) -> dict[str, Any]:
    all_findings: list[dict[str, Any]] = []
    downloaded: list[str] = []
    errors: list[dict[str, str]] = []

    for remote in TWIG_PATHS:
        local_name = remote.replace("/public_html/", "").replace("/", "__")
        try:
            data = ftp_download(ftp, remote)
            dest = DEPLOYMENT_ROOT / "source" / local_name
            dest.write_bytes(data)
            downloaded.append(remote)
            all_findings.extend(
                analyze_twig_content(remote, data.decode("utf-8", errors="replace"))
            )
        except ftplib.error_perm as exc:
            errors.append({"remote_path": remote, "error": str(exc)})

    extra_twig: list[str] = []
    for theme_dir in THEME_SEARCH_PATHS:
        for name in ftp_list_dir(ftp, theme_dir):
            if not name.endswith(".twig"):
                continue
            base = name.rsplit("/", 1)[-1]
            if base in ("header.twig", "footer.twig"):
                continue
            remote = theme_dir + base if theme_dir.endswith("/") else theme_dir + "/" + base
            if remote in downloaded:
                continue
            try:
                data = ftp_download(ftp, remote)
                text = data.decode("utf-8", errors="replace")
                hits = analyze_twig_content(remote, text)
                if hits:
                    local_name = remote.replace("/public_html/", "").replace("/", "__")
                    (DEPLOYMENT_ROOT / "source" / local_name).write_bytes(data)
                    downloaded.append(remote)
                    extra_twig.append(remote)
                    all_findings.extend(hits)
            except ftplib.error_perm:
                pass

    metrika = [f for f in all_findings if f["code_type"] == "YANDEX_METRIKA"]
    webmaster = [f for f in all_findings if f["code_type"] == "YANDEX_WEBMASTER"]

    payload = {
        "operation_id": OPERATION_ID,
        "checked_at": utc_now(),
        "files_downloaded": downloaded,
        "extra_theme_files_with_codes": extra_twig,
        "findings": all_findings,
        "metrika_findings_count": len(metrika),
        "webmaster_findings_count": len(webmaster),
        "download_errors": errors,
        "operator_wip_protected": bool(all_findings),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "yandex-twig-findings.json", payload)

    md = [
        "# Yandex Twig Findings",
        "",
        f"Operation: `{OPERATION_ID}`",
        f"Checked at: {payload['checked_at']}",
        "",
        "## Protection rule",
        "",
        "**OPERATOR WIP — DO NOT OVERWRITE / DO NOT REFORMAT / DO NOT REGENERATE FROM REPO**",
        "",
        "## Summary",
        "",
        f"- Files downloaded: {len(downloaded)}",
        f"- YANDEX_METRIKA findings: {len(metrika)}",
        f"- YANDEX_WEBMASTER findings: {len(webmaster)}",
        "",
        "## Findings",
        "",
    ]
    if not all_findings:
        md.append(
            "**None** — no Yandex Metrika or Webmaster verification strings detected in inspected Twig paths."
        )
    else:
        for f in all_findings:
            md.append(
                f"- `{f['remote_path']}` — **{f['code_type']}** — line {f['line_number']} — "
                f"location `{f['approximate_location']}` — masked ID `{f.get('masked_id')}`"
            )
    if errors:
        md.extend(["", "## Download errors", ""])
        for e in errors:
            md.append(f"- `{e['remote_path']}` — {e['error']}")
    write_text(DEPLOYMENT_ROOT / "verification" / "yandex-twig-findings.md", "\n".join(md))
    return payload


def phase_html() -> dict[str, Any]:
    page_results: list[dict[str, Any]] = []
    for url in LIVE_URLS:
        resp = http_get(url)
        slug = (
            url.replace("https://bzpm.ru", "")
            .strip("/")
            .replace("/", "_")
            or "home"
        )
        raw_path = DEPLOYMENT_ROOT / "html" / f"{slug}.raw.html"
        sanitized_path = DEPLOYMENT_ROOT / "html" / f"{slug}.sanitized.html"
        raw_path.write_text(resp["body"], encoding="utf-8")
        sanitized_path.write_text(mask_html(resp["body"]), encoding="utf-8")
        analysis = analyze_html_page(url, resp["body"], resp.get("status_code"))
        analysis["checked_at"] = resp["checked_at"]
        analysis["error"] = resp.get("error")
        analysis["html_artifact"] = str(sanitized_path)
        page_results.append(analysis)

    all_http_ok = all(p["http_ok"] for p in page_results)
    any_metrika = any(p["yandex_metrika_script"] for p in page_results)
    any_noscript = any(p["yandex_metrika_noscript"] for p in page_results)
    any_webmaster = any(p["yandex_webmaster_verification"] for p in page_results)
    home = page_results[0] if page_results else {}
    webmaster_on_home = home.get("yandex_webmaster_verification", False)
    duplicate_metrika = any(p["duplicate_metrika"] for p in page_results)
    duplicate_webmaster = any(p["duplicate_webmaster"] for p in page_results)
    twig_errors = any(p["twig_error_visible"] for p in page_results)

    if any_metrika and any_webmaster and all_http_ok:
        live_status = "VERIFIED"
    elif any_metrika or any_webmaster:
        live_status = "PARTIAL"
    else:
        live_status = "NOT_FOUND"

    payload = {
        "operation_id": OPERATION_ID,
        "checked_at": utc_now(),
        "pages": page_results,
        "summary": {
            "all_http_200": all_http_ok,
            "yandex_metrika_script_any_page": any_metrika,
            "yandex_metrika_noscript_any_page": any_noscript,
            "yandex_webmaster_any_page": any_webmaster,
            "yandex_webmaster_on_home": webmaster_on_home,
            "duplicate_metrika_any_page": duplicate_metrika,
            "duplicate_webmaster_any_page": duplicate_webmaster,
            "twig_error_visible_any_page": twig_errors,
            "live_status": live_status,
        },
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "yandex-live-html-verification.json", payload)

    md = [
        "# Yandex Live HTML Verification",
        "",
        f"Operation: `{OPERATION_ID}`",
        f"Checked at: {payload['checked_at']}",
        "",
        "## Summary",
        "",
        f"- Live status: **{live_status}**",
        f"- All pages HTTP 200: {all_http_ok}",
        f"- Metrika script on any page: {any_metrika}",
        f"- Metrika noscript on any page: {any_noscript}",
        f"- Webmaster verification on any page: {any_webmaster}",
        f"- Webmaster on home: {webmaster_on_home}",
        f"- Duplicate Metrika: {duplicate_metrika}",
        f"- Duplicate Webmaster: {duplicate_webmaster}",
        f"- Visible Twig errors: {twig_errors}",
        "",
        "## Per-page",
        "",
    ]
    for p in page_results:
        md.append(f"### {p['url']}")
        md.append(f"- HTTP: {p['status_code']}")
        md.append(f"- Metrika script: {p['yandex_metrika_script']}")
        md.append(f"- Metrika noscript: {p['yandex_metrika_noscript']}")
        md.append(f"- Webmaster: {p['yandex_webmaster_verification']}")
        md.append(f"- Masked counter IDs: {p['masked_counter_ids']}")
        md.append(f"- Masked verification IDs: {p['masked_verification_ids']}")
        md.append(f"- Metrika occurrences: {p['metrika_occurrence_count']}")
        md.append(f"- Webmaster occurrences: {p['webmaster_occurrence_count']}")
        md.append("")
    write_text(
        DEPLOYMENT_ROOT / "verification" / "yandex-live-html-verification.md",
        "\n".join(md),
    )
    return payload


def phase_status_update(twig_payload: dict[str, Any], html_payload: dict[str, Any]) -> dict[str, Any]:
    twig_found = bool(twig_payload.get("findings"))
    live = html_payload["summary"]
    any_live = live["yandex_metrika_script_any_page"] or live["yandex_webmaster_any_page"]

    if any_live and twig_found:
        seo_status = "VERIFIED"
        verdict_hint = "SITE-002 YANDEX CODES VERIFIED — OPERATOR TWIG WIP PROTECTED"
    elif twig_found and not any_live:
        seo_status = "PARTIAL"
        verdict_hint = "SITE-002 YANDEX CODES PARTIAL — TWIG FOUND / LIVE HTML NOT CONFIRMED"
    elif any_live and not twig_found:
        seo_status = "VERIFIED"
        verdict_hint = "SITE-002 YANDEX CODES VERIFIED — OPERATOR TWIG WIP PROTECTED"
    else:
        seo_status = "SAFE UNKNOWN"
        verdict_hint = "SITE-002 YANDEX CODES NOT FOUND — OPERATOR REVIEW REQUIRED"

    update = {
        "operation_id": OPERATION_ID,
        "checked_at": utc_now(),
        "baseline_before": BASELINE_BEFORE,
        "previous_run": "4.188 — SITE-002 SEO Readiness and Robots",
        "previous_status": "Yandex Metrika/Webmaster — SAFE UNKNOWN / not found on live",
        "new_status": {
            "yandex_metrika": "VERIFIED"
            if live["yandex_metrika_script_any_page"]
            else ("PARTIAL (Twig only)" if twig_payload.get("metrika_findings_count") else "NOT FOUND"),
            "yandex_webmaster": "VERIFIED"
            if live["yandex_webmaster_any_page"]
            else ("PARTIAL (Twig only)" if twig_payload.get("webmaster_findings_count") else "NOT FOUND"),
            "combined_seo_status": seo_status,
        },
        "protected_twig_paths": sorted(
            {f["remote_path"] for f in twig_payload.get("findings", [])}
        ),
        "verdict_hint": verdict_hint,
        "operator_wip_protected": True,
        "remote_mutations": 0,
    }
    write_json(
        DEPLOYMENT_ROOT / "reports" / "yandex-codes-status-update.json", update
    )
    md = [
        "# Yandex Codes Status Update",
        "",
        f"Operation: `{OPERATION_ID}`",
        "",
        "## Previous (Run 4.188)",
        "",
        "Yandex Metrika / Webmaster on live — **SAFE UNKNOWN / not found**.",
        "",
        "## New status",
        "",
        f"- Yandex.Metrika: **{update['new_status']['yandex_metrika']}**",
        f"- Yandex.Webmaster: **{update['new_status']['yandex_webmaster']}**",
        f"- Combined: **{seo_status}**",
        "",
        "## Protected Twig paths",
        "",
    ]
    if update["protected_twig_paths"]:
        for p in update["protected_twig_paths"]:
            md.append(f"- `{p}`")
    else:
        md.append("- *(none detected in inspected Twig)*")
    md.extend(
        [
            "",
            "## Verdict hint",
            "",
            verdict_hint,
            "",
            "No production mutation performed in this operation.",
        ]
    )
    write_text(DEPLOYMENT_ROOT / "reports" / "yandex-codes-status-update.md", "\n".join(md))
    return update


def write_manifest() -> None:
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "yandex-codes-verification",
        "remote_changes_allowed": False,
        "twig_changes_allowed": False,
        "cache_clear_allowed": False,
        "operator_wip_protected": True,
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-ftp", action="store_true", help="HTTP-only fallback")
    args = parser.parse_args()

    ensure_dirs()
    write_manifest()

    twig_payload: dict[str, Any] = {
        "findings": [],
        "metrika_findings_count": 0,
        "webmaster_findings_count": 0,
    }
    if not args.skip_ftp:
        if not SECRETS_PATH.is_file():
            print(f"ERROR: secrets missing: {SECRETS_PATH}", file=sys.stderr)
            return 2
        fields = parse_production_secrets(SECRETS_PATH)
        ftp = ftp_connect(fields)
        try:
            twig_payload = phase_twig(ftp)
        finally:
            try:
                ftp.quit()
            except Exception:
                pass

    html_payload = phase_html()
    status_update = phase_status_update(twig_payload, html_payload)

    summary = {
        "operation_id": OPERATION_ID,
        "twig_findings": twig_payload.get("metrika_findings_count", 0)
        + twig_payload.get("webmaster_findings_count", 0),
        "live_status": html_payload["summary"]["live_status"],
        "verdict_hint": status_update["verdict_hint"],
        "deployment_root": str(DEPLOYMENT_ROOT),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "run-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
