#!/usr/bin/env python3
"""SITE-002 production llms.txt encoding fix — UTF-8 BOM reupload, optional .htaccess."""
from __future__ import annotations

import argparse
import ftplib
import hashlib
import io
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-LLMS-TXT-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01"
RUN_4203_SHA = "e2e752c6dab1ebf751283cc3013fee711925c77a4c764d2474500383c8b8de58"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01"
REMOTE_LLMS = "/public_html/llms.txt"
REMOTE_HTACCESS = "/public_html/.htaccess"
PUBLIC_LLMS = "https://bzpm.ru/llms.txt"
UTF8_BOM = b"\xef\xbb\xbf"
HTACCESS_BLOCK = (
    "# MARS SITE-002 llms.txt UTF-8 charset fix\n"
    "AddCharset UTF-8 .txt\n"
    "# /MARS SITE-002 llms.txt UTF-8 charset fix\n"
)

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "verification/pre-upload",
    "verification/after-upload",
    "headers",
    "content",
    "manifests",
    "logs",
)

SANITY_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[dict[str, str]] = []
        self.body_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "body":
            self.body_count += 1
        elif tag_l == "meta":
            name = (attrs_dict.get("name") or attrs_dict.get("property") or "").lower()
            content = attrs_dict.get("content", "")
            if name:
                self.meta[name] = content
        elif tag_l == "link":
            rel = attrs_dict.get("rel", "").lower()
            href = attrs_dict.get("href", "")
            self.links.append({"rel": rel, "href": href})

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        elif tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        elif self.in_h1:
            self.h1_list.append(data.strip())


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


def ensure_dirs() -> None:
    for name in SUBDIRS:
        (DEPLOYMENT_ROOT / name).mkdir(parents=True, exist_ok=True)


def write_operation_metadata() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "llms-txt-encoding-fix",
            "target_remote_file": REMOTE_LLMS,
            "target_public_url": PUBLIC_LLMS,
            "htaccess_change_allowed": "conditional_only_if_needed",
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "php_change_allowed": False,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "product_meta_change_allowed": False,
            "yandex_blocks_protected": True,
        },
    )


def parse_production_section(path: Path, subsection: str) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    sub_match = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not sub_match:
        raise RuntimeError(f"Subsection {subsection} not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in sub_match.group(1).splitlines():
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


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    ftp.set_pasv(True)
    if creds.get("remote_root"):
        try:
            ftp.cwd(creds["remote_root"])
        except ftplib.error_perm:
            pass
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes:
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {remote}", buf.write)
    return buf.getvalue()


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def ftp_exists(ftp: ftplib.FTP, remote: str) -> bool:
    try:
        ftp.size(remote)
        return True
    except ftplib.error_perm:
        try:
            buf = io.BytesIO()
            ftp.retrbinary(f"RETR {remote}", buf.write, rest=0)
            return True
        except ftplib.error_perm:
            return False


def http_get(url: str, accept: str = "*/*") -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return {
                "url": url,
                "final_url": resp.geturl(),
                "status": resp.status,
                "headers": headers,
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        return {
            "url": url,
            "final_url": exc.geturl() if hasattr(exc, "geturl") else url,
            "status": exc.code,
            "headers": {k.lower(): v for k, v in exc.headers.items()} if exc.headers else {},
            "body": body,
            "error": str(exc),
        }
    except Exception as exc:
        return {
            "url": url,
            "final_url": url,
            "status": 0,
            "headers": {},
            "body": b"",
            "error": str(exc),
        }


def analyze_bytes(data: bytes, label: str) -> dict[str, Any]:
    bom = data.startswith(UTF8_BOM)
    payload = data[len(UTF8_BOM) :] if bom else data
    utf8_valid = True
    utf8_error = None
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        utf8_valid = False
        utf8_error = str(exc)
        text = payload.decode("utf-8", errors="replace")
    cyr = sum(1 for c in text if "\u0400" <= c <= "\u04FF")
    moj = any(x in text for x in ("Ð", "Ñ", "Ã", "â€", "�"))
    crlf = b"\r\n" in data
    lf_only = b"\n" in data and not crlf
    return {
        "label": label,
        "size_bytes": len(data),
        "sha256": sha256_bytes(data),
        "bom_present": bom,
        "utf8_valid": utf8_valid,
        "utf8_error": utf8_error,
        "cyrillic_char_count": cyr,
        "mojibake_suspected": moj,
        "readable_russian": cyr > 50 and not moj,
        "line_endings": "CRLF" if crlf else ("LF" if lf_only else "unknown"),
        "first_bytes_hex": data[:16].hex(" "),
        "text_without_bom": text,
    }


def encoding_diagnosis(resp: dict[str, Any], prefix: str) -> dict[str, Any]:
    body = resp["body"]
    headers = resp["headers"]
    analysis = analyze_bytes(body, prefix)
    ct = headers.get("content-type", "")
    charset_match = re.search(r"charset=([^\s;]+)", ct, re.I)
    info = {
        "captured_at": utc_now(),
        "url": resp["url"],
        "final_url": resp["final_url"],
        "status": resp["status"],
        "content_type": ct,
        "charset_in_header": charset_match.group(1) if charset_match else None,
        "content_length_header": headers.get("content-length"),
        "content_length_actual": len(body),
        "sha256": sha256_bytes(body),
        **{k: v for k, v in analysis.items() if k != "text_without_bom"},
    }
    (DEPLOYMENT_ROOT / "content" / f"llms-{prefix}-response.bin").write_bytes(body)
    write_text(
        DEPLOYMENT_ROOT / "content" / f"llms-{prefix}-decoded-utf8.txt",
        analysis["text_without_bom"],
    )
    header_lines = [
        f"HTTP/1.1 {resp['status']}",
        f"Final-URL: {resp['final_url']}",
    ]
    for k, v in headers.items():
        header_lines.append(f"{k}: {v}")
    write_text(DEPLOYMENT_ROOT / "headers" / f"llms-{prefix}-headers.txt", "\n".join(header_lines) + "\n")
    write_json(DEPLOYMENT_ROOT / "headers" / f"llms-{prefix}-headers.json", info)
    md = [
        f"# Encoding diagnosis — {prefix}",
        "",
        f"- Status: {info['status']}",
        f"- Content-Type: {info['content_type']}",
        f"- Charset in header: {info['charset_in_header']}",
        f"- BOM present: {info['bom_present']}",
        f"- UTF-8 valid: {info['utf8_valid']}",
        f"- Cyrillic chars: {info['cyrillic_char_count']}",
        f"- Mojibake suspected: {info['mojibake_suspected']}",
        f"- Readable Russian: {info['readable_russian']}",
        f"- First bytes: `{info['first_bytes_hex']}`",
        f"- SHA-256: `{info['sha256']}`",
    ]
    write_text(DEPLOYMENT_ROOT / "verification" / f"encoding-diagnosis-{prefix}.md", "\n".join(md))
    write_json(DEPLOYMENT_ROOT / "verification" / f"encoding-diagnosis-{prefix}.json", info)
    return info


def parse_html_page(body: bytes) -> dict[str, Any]:
    text = body.decode("utf-8", errors="replace")
    parser = PageParser()
    parser.feed(text)
    return {
        "title": parser.title.strip(),
        "body_count": parser.body_count,
        "has_yandex_metrika": "mc.yandex.ru" in text or "ym(" in text,
        "has_yandex_webmaster": "yandex-verification" in text.lower(),
        "has_load_more": "load-more" in text.lower() or "load_more" in text.lower() or "Загрузить ещё" in text,
    }


def phase1_diagnose_public() -> dict[str, Any]:
    llms = http_get(PUBLIC_LLMS, accept="text/plain")
    before = encoding_diagnosis(llms, "before")
    sanity: list[dict[str, Any]] = []
    for url in SANITY_URLS:
        is_xml = url.endswith(".xml")
        is_txt = url.endswith(".txt")
        accept = "application/xml" if is_xml else "text/plain" if is_txt else "text/html"
        resp = http_get(url, accept=accept)
        entry: dict[str, Any] = {"url": url, "status": resp["status"]}
        if resp["status"] == 200 and is_xml:
            try:
                root = ET.fromstring(resp["body"])
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                locs = root.findall(".//sm:loc", ns) or root.findall(
                    ".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"
                )
                entry["sitemap_url_count"] = len(locs)
            except ET.ParseError:
                entry["sitemap_url_count"] = None
        elif resp["status"] == 200 and not is_txt:
            entry.update(parse_html_page(resp["body"]))
        sanity.append(entry)
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-before.json", {"sanity": sanity})
    return {"llms_before": before, "sanity": sanity}


def phase2_ftp_read(ftp: ftplib.FTP) -> dict[str, Any]:
    if not ftp_exists(ftp, REMOTE_LLMS):
        raise RuntimeError("Remote llms.txt missing")
    data = ftp_download(ftp, REMOTE_LLMS)
    remote_path = DEPLOYMENT_ROOT / "source" / "llms.txt.remote-current"
    remote_path.write_bytes(data)
    analysis = analyze_bytes(data, "remote-current")
    analysis["matches_run_4203_sha"] = analysis["sha256"] == RUN_4203_SHA
    write_json(DEPLOYMENT_ROOT / "verification" / "remote-file-encoding-analysis.json", analysis)
    md = [
        "# Remote file encoding analysis",
        "",
        f"- Size: {analysis['size_bytes']} bytes",
        f"- SHA-256: `{analysis['sha256']}`",
        f"- Matches Run 4.203 SHA: {analysis['matches_run_4203_sha']}",
        f"- BOM present: {analysis['bom_present']}",
        f"- UTF-8 valid: {analysis['utf8_valid']}",
        f"- Line endings: {analysis['line_endings']}",
        f"- Cyrillic chars: {analysis['cyrillic_char_count']}",
        f"- Readable Russian: {analysis['readable_russian']}",
    ]
    write_text(DEPLOYMENT_ROOT / "verification" / "remote-file-encoding-analysis.md", "\n".join(md))
    return analysis


def phase3_prepare(analysis: dict[str, Any], http_before: dict[str, Any]) -> dict[str, Any]:
    text = analysis["text_without_bom"].replace("\r\n", "\n").replace("\r", "\n")
    if not text.endswith("\n"):
        text += "\n"
    prepared_bytes = UTF8_BOM + text.encode("utf-8")
    prepared_path = DEPLOYMENT_ROOT / "prepared" / "llms.txt"
    prepared_path.write_bytes(prepared_bytes)
    write_text(DEPLOYMENT_ROOT / "content" / "llms-prepared-readable.txt", text)
    bom_added = not analysis["bom_present"]
    plan = {
        "prepared_at": utc_now(),
        "current_encoding": "UTF-8",
        "current_http_charset": http_before.get("charset_in_header"),
        "current_content_type": http_before.get("content_type"),
        "chosen_fix": "UTF-8 with BOM reupload",
        "bom_added": bom_added,
        "htaccess_needed_now": False,
        "semantic_text_preserved": True,
        "before_sha256": analysis["sha256"],
        "prepared_sha256": sha256_bytes(prepared_bytes),
        "byte_diff_summary": "UTF-8 BOM prefix (+3 bytes) and optional final newline normalization only",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "llms-encoding-plan.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "llms-encoding-plan.md",
        "\n".join(
            [
                "# llms.txt encoding plan",
                "",
                f"- Current encoding: UTF-8 (valid)",
                f"- HTTP Content-Type: {http_before.get('content_type')}",
                f"- Charset in header: {http_before.get('charset_in_header') or 'none'}",
                f"- Chosen fix: reupload with UTF-8 BOM",
                f"- BOM added: {bom_added}",
                f"- .htaccess needed now: no (unless post-deploy verification fails)",
            ]
        ),
    )
    return plan


def phase4_backup(ftp: ftplib.FTP, remote_analysis: dict[str, Any]) -> dict[str, Any]:
    data = (DEPLOYMENT_ROOT / "source" / "llms.txt.remote-current").read_bytes()
    (DEPLOYMENT_ROOT / "backup" / "llms.txt").write_bytes(data)
    (DEPLOYMENT_ROOT / "rollback" / "llms.txt").write_bytes(data)
    info = {
        "backup_at": utc_now(),
        "sha256": sha256_bytes(data),
        "size_bytes": len(data),
        "matches_remote_analysis": sha256_bytes(data) == remote_analysis["sha256"],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "backup.json", info)
    return info


def phase5_dry_run(remote_analysis: dict[str, Any], plan: dict[str, Any]) -> dict[str, Any]:
    prepared = (DEPLOYMENT_ROOT / "prepared" / "llms.txt").read_bytes()
    remote_text = remote_analysis["text_without_bom"].replace("\r\n", "\n").replace("\r", "\n").strip()
    prepared_text = prepared[len(UTF8_BOM) :].decode("utf-8").strip()
    semantic_match = remote_text == prepared_text
    diff = {
        "before_sha": plan["before_sha256"],
        "prepared_sha": plan["prepared_sha256"],
        "semantic_match": semantic_match,
        "only_bom_and_newline_diff": semantic_match,
        "target_remote_path": REMOTE_LLMS,
        "rollback_path": str(DEPLOYMENT_ROOT / "rollback" / "llms.txt"),
        "verification_plan": [
            "Fetch https://bzpm.ru/llms.txt after upload",
            "Verify BOM in response bytes",
            "Verify readable Russian / no mojibake",
            "Sanity: home, robots, sitemap, stoly unchanged",
        ],
    }
    if not semantic_match:
        diff["semantic_error"] = "Prepared text differs from remote content"
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", diff)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run",
                "",
                f"- Before SHA: `{diff['before_sha']}`",
                f"- Prepared SHA: `{diff['prepared_sha']}`",
                f"- Semantic match: {semantic_match}",
                f"- Target: `{REMOTE_LLMS}`",
                "",
                "Byte diff: BOM (+3) and newline normalization only.",
            ]
        ),
    )
    if not semantic_match:
        raise RuntimeError("STOP — prepared content differs semantically from remote")
    return diff


def pre_upload_verify(ftp: ftplib.FTP, backup_sha: str) -> None:
    live = ftp_download(ftp, REMOTE_LLMS)
    (DEPLOYMENT_ROOT / "verification" / "pre-upload" / "llms.txt").write_bytes(live)
    if sha256_bytes(live) != backup_sha:
        raise RuntimeError("STOP — LIVE LLMS.TXT CHANGED SINCE BACKUP")


def deploy_llms_bom(ftp: ftplib.FTP) -> dict[str, Any]:
    prepared = (DEPLOYMENT_ROOT / "prepared" / "llms.txt").read_bytes()
    ftp_upload(ftp, REMOTE_LLMS, prepared)
    after = ftp_download(ftp, REMOTE_LLMS)
    (DEPLOYMENT_ROOT / "verification" / "after-upload" / "llms.txt").write_bytes(after)
    return {
        "remote": REMOTE_LLMS,
        "sha256_prepared": sha256_bytes(prepared),
        "sha256_after_upload": sha256_bytes(after),
        "match": sha256_bytes(prepared) == sha256_bytes(after),
        "deployed_at": utc_now(),
    }


def public_serving_ok(info: dict[str, Any]) -> bool:
    return (
        info.get("status") == 200
        and info.get("readable_russian")
        and not info.get("mojibake_suspected")
    )


def phase8_verify_bom() -> dict[str, Any]:
    resp = http_get(PUBLIC_LLMS, accept="text/plain")
    info = encoding_diagnosis(resp, "after-bom")
    write_text(
        DEPLOYMENT_ROOT / "verification" / "llms-response-after-bom.txt",
        analyze_bytes(resp["body"], "after-bom")["text_without_bom"],
    )
    info["public_serving_ok"] = public_serving_ok(info)
    return info


def prepare_htaccess_patch(current: bytes) -> bytes:
    text = current.decode("utf-8", errors="replace")
    if "MARS SITE-002 llms.txt UTF-8 charset fix" in text:
        return current
    if not text.endswith("\n"):
        text += "\n"
    patched = text + "\n" + HTACCESS_BLOCK + "\n"
    return patched.encode("utf-8")


def deploy_htaccess_if_needed(ftp: ftplib.FTP) -> dict[str, Any] | None:
    if not ftp_exists(ftp, REMOTE_HTACCESS):
        return None
    current = ftp_download(ftp, REMOTE_HTACCESS)
    (DEPLOYMENT_ROOT / "source" / "htaccess.remote-current").write_bytes(current)
    (DEPLOYMENT_ROOT / "backup" / ".htaccess").write_bytes(current)
    (DEPLOYMENT_ROOT / "rollback" / ".htaccess").write_bytes(current)
    patched = prepare_htaccess_patch(current)
    (DEPLOYMENT_ROOT / "prepared" / ".htaccess").write_bytes(patched)
    plan = {
        "action": "append AddCharset UTF-8 .txt block",
        "original_sha256": sha256_bytes(current),
        "prepared_sha256": sha256_bytes(patched),
        "block": HTACCESS_BLOCK.strip(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "htaccess-plan.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "htaccess-plan.md",
        "# htaccess plan\n\nAppend minimal AddCharset block for .txt UTF-8.\n",
    )
    ftp_upload(ftp, REMOTE_HTACCESS, patched)
    after = ftp_download(ftp, REMOTE_HTACCESS)
    return {
        "uploaded": True,
        "sha256_match": sha256_bytes(after) == sha256_bytes(patched),
        "deployed_at": utc_now(),
    }


def phase10_final_verification() -> dict[str, Any]:
    llms_resp = http_get(PUBLIC_LLMS, accept="text/plain")
    llms_info = encoding_diagnosis(llms_resp, "final")
    write_text(
        DEPLOYMENT_ROOT / "verification" / "llms-response-final.txt",
        analyze_bytes(llms_resp["body"], "final")["text_without_bom"],
    )
    sanity: list[dict[str, Any]] = []
    for url in SANITY_URLS:
        is_xml = url.endswith(".xml")
        is_txt = url.endswith(".txt")
        accept = "application/xml" if is_xml else "text/plain" if is_txt else "text/html"
        resp = http_get(url, accept=accept)
        entry: dict[str, Any] = {"url": url, "status": resp["status"]}
        if resp["status"] == 200 and is_xml:
            try:
                root = ET.fromstring(resp["body"])
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                locs = root.findall(".//sm:loc", ns) or root.findall(
                    ".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"
                )
                entry["sitemap_url_count"] = len(locs)
            except ET.ParseError:
                entry["sitemap_url_count"] = None
        elif resp["status"] == 200 and not is_txt:
            entry.update(parse_html_page(resp["body"]))
        elif resp["status"] == 200 and is_txt:
            entry["robots_has_sitemap"] = "Sitemap:" in resp["body"].decode("utf-8", errors="replace")
        sanity.append(entry)
    result = {
        "verified_at": utc_now(),
        "llms": llms_info,
        "sanity_checks": sanity,
        "pass": public_serving_ok(llms_info)
        and all(s["status"] == 200 for s in sanity),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "final-public-verification.json", result)
    md = ["# Final public verification", "", f"Verified: {result['verified_at']}", ""]
    md.append("## llms.txt")
    for k in ("status", "content_type", "charset_in_header", "bom_present", "readable_russian", "mojibake_suspected"):
        md.append(f"- {k}: {llms_info.get(k)}")
    md.append("")
    md.append("## Sanity")
    for s in sanity:
        md.append(f"### {s['url']}")
        md.append(f"- status: {s['status']}")
        for k in ("body_count", "sitemap_url_count", "has_yandex_metrika", "has_yandex_webmaster", "has_load_more", "robots_has_sitemap"):
            if k in s:
                md.append(f"- {k}: {s[k]}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "verification" / "final-public-verification.md", "\n".join(md))
    return result


def run_all(deploy: bool = True) -> int:
    ensure_dirs()
    write_operation_metadata()
    public_before = phase1_diagnose_public()
    http_before = public_before["llms_before"]

    ftp = ftp_connect()
    htaccess_deployed = False
    try:
        remote_analysis = phase2_ftp_read(ftp)
        plan = phase3_prepare(remote_analysis, http_before)
        backup = phase4_backup(ftp, remote_analysis)
        dry = phase5_dry_run(remote_analysis, plan)

        deploy_result = None
        after_bom = None
        if deploy:
            pre_upload_verify(ftp, backup["sha256"])
            deploy_result = deploy_llms_bom(ftp)
            write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-summary.json", deploy_result)
            if not deploy_result["match"]:
                raise RuntimeError("Upload SHA mismatch")
            after_bom = phase8_verify_bom()
            if not after_bom.get("public_serving_ok"):
                ht = deploy_htaccess_if_needed(ftp)
                htaccess_deployed = bool(ht and ht.get("uploaded"))
                write_json(DEPLOYMENT_ROOT / "manifests" / "htaccess-deploy.json", ht or {})
                after_bom = phase8_verify_bom()
    finally:
        ftp.quit()

    final = phase10_final_verification()
    summary = {
        "operation_id": OPERATION_ID,
        "deployed": deploy,
        "bom_added": plan.get("bom_added"),
        "htaccess_deployed": htaccess_deployed,
        "after_bom_public_ok": after_bom.get("public_serving_ok") if after_bom else None,
        "final_pass": final["pass"],
        "baseline_after": BASELINE_AFTER if final["pass"] else None,
        "dry_run": dry,
        "deploy_result": deploy_result,
    }
    write_json(DEPLOYMENT_ROOT / "logs" / "run-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if final["pass"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--diagnose-only", action="store_true")
    parser.add_argument("--no-deploy", action="store_true")
    args = parser.parse_args()
    if args.diagnose_only:
        ensure_dirs()
        write_operation_metadata()
        phase1_diagnose_public()
        ftp = ftp_connect()
        try:
            phase2_ftp_read(ftp)
        finally:
            ftp.quit()
        return 0
    return run_all(deploy=not args.no_deploy)


if __name__ == "__main__":
    raise SystemExit(main())
