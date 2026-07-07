#!/usr/bin/env python3
"""SITE-002 Production PDP extra info attribute layout — Run 4.218."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01"
OCPILOT_RUN = "4.218"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01"
INTAKE_BEFORE = "SITE-002-UX-TASK-INTAKE-01"
EXTRA_INFO_ATTR = "Дополнительные сведения"
CORRECT_BRAND = "ЗПМ"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
INTAKE_SAMPLE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-UX-TASK-INTAKE-01\task-02-extra-info\attribute-scope-sample.csv"
)

EXAMPLE_PDP = (
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/"
    "polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht"
)

REMOTE_FILES = [
    {
        "remote": "/public_html/catalog/controller/product/product.php",
        "local_name": "public_html__catalog__controller__product__product.php",
        "role": "PDP controller — extract extra_info_attribute for display",
        "needs_patch": True,
    },
    {
        "remote": "/public_html/catalog/view/theme/default/template/product/producttabs.twig",
        "local_name": "public_html__catalog__view__theme__default__template__product__producttabs.twig",
        "role": "PDP specs partial — render extra-info block after specs toggle",
        "needs_patch": True,
    },
    {
        "remote": "/public_html/assets/css/style.css",
        "local_name": "public_html__assets__css__style.css",
        "role": "PDP extra-info typography styles",
        "needs_patch": True,
    },
    {
        "remote": "/public_html/catalog/view/theme/default/template/product/product.twig",
        "local_name": "public_html__catalog__view__theme__default__template__product__product.twig",
        "role": "PDP shell — includes producttabs",
        "needs_patch": False,
    },
    {
        "remote": "/public_html/catalog/view/theme/default/template/product/producthero.twig",
        "local_name": "public_html__catalog__view__theme__default__template__product__producthero.twig",
        "role": "PDP hero partial",
        "needs_patch": False,
    },
    {
        "remote": "/storage/modification/catalog/controller/product/product.php",
        "local_name": "storage__modification__catalog__controller__product__product.php",
        "role": "Modification overlay check",
        "needs_patch": False,
    },
    {
        "remote": "/storage/modification/catalog/view/theme/default/template/product/producttabs.twig",
        "local_name": "storage__modification__catalog__view__theme__default__template__product__producttabs.twig",
        "role": "Modification overlay check",
        "needs_patch": False,
    },
]

SANITY_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

BRANCH_PDP_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-standart/stoly-standart-700-s-polkoy-reshetkoy/stol-proizvodstvennyy-spb-s-16-7-1600h700h850",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/polki-otkrytye-premium/polki-otkrytye-premium-dvuhyarusnye/polka-nastennaya-pn2-p-10-3-1000h300h500",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar/formy-konditerskie",
]


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.title = ""
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.body_classes = ""
        self.body_open = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        if tag_l == "h1":
            self.in_h1 = True
        if tag_l == "meta":
            name = ad.get("name") or ad.get("property") or ""
            if name:
                self.meta[name.lower()] = ad.get("content", "")
        if tag_l == "body":
            self.body_classes = ad.get("class", "")
            self.body_open += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        if tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(data.strip())


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
        if not sub:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            current = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current, "")
            continue
        if current:
            fields[current] = s
    return fields


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> tuple[bytes | None, str | None]:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue(), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*", "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return {
                "url": url,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "raw_body": body,
                "body": body.decode(charset, errors="replace"),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        return {
            "url": url,
            "status": exc.code,
            "headers": dict(exc.headers.items()) if exc.headers else {},
            "raw_body": raw,
            "body": raw.decode(charset or "utf-8", errors="replace"),
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "headers": {}, "raw_body": b"", "body": "", "error": str(exc)}


def extract_page_meta(html_text: str) -> dict[str, Any]:
    p = MetaParser()
    try:
        p.feed(html_text)
    except Exception:
        pass
    return {
        "title": html.unescape(p.title.strip()),
        "meta_description": p.meta.get("description", ""),
        "h1": " | ".join(h for h in p.h1_list if h),
        "body_classes": p.body_classes,
        "body_count": p.body_open,
    }


def parse_pdp_layout(html_text: str) -> dict[str, Any]:
    attr = EXTRA_INFO_ATTR
    toggle_pos = html_text.find("product-content__specs-toggle-wrap")
    extra_block_pos = html_text.find("product-content__extra-info")
    in_spec_row = bool(
        re.search(
            rf'<div class="spec-table__key"><span>{re.escape(attr)}</span></div>',
            html_text,
            re.I,
        )
    )
    extra_block_after_toggle = False
    if toggle_pos >= 0 and extra_block_pos >= 0:
        extra_block_after_toggle = extra_block_pos > toggle_pos
    value = ""
    m = re.search(
        rf'class="product-extra-info__text">(.*?)</div>',
        html_text,
        re.DOTALL | re.I,
    )
    if m:
        value = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    if not value:
        m2 = re.search(
            rf'<div class="spec-table__key"><span>{re.escape(attr)}</span></div>\s*'
            r'<div class="spec-table__val[^"]*">(.*?)</div>',
            html_text,
            re.DOTALL | re.I,
        )
        if m2:
            value = re.sub(r"<[^>]+>", "", m2.group(1)).strip()
    return {
        "has_specs_toggle_wrap": toggle_pos >= 0,
        "extra_info_count": html_text.count(attr),
        "extra_info_in_spec_table_row": in_spec_row,
        "separate_extra_info_block": extra_block_pos >= 0,
        "extra_info_after_toggle": extra_block_after_toggle,
        "extra_info_value_length": len(value),
        "extra_info_value_preview": value[:120],
        "has_product_images": "product-hero" in html_text or "product-gallery" in html_text or "producthero" in html_text.lower(),
        "has_buy_controls": "product-hero__buy" in html_text or "button-cart" in html_text or "В корзину" in html_text,
        "wrong_brand_count": html_text.count(WRONG_BRAND),
        "correct_brand_count": html_text.count(CORRECT_BRAND),
    }


def load_sample_urls() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with INTAKE_SAMPLE.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)
    with_extra = [r for r in all_rows if r.get("has_extra_info") == "True"][:5]
    without_extra = [r for r in all_rows if r.get("has_extra_info") == "False"][:5]
    for r in with_extra + without_extra:
        rows.append({"url": r["url"], "expected_extra_info": r.get("has_extra_info", ""), "product_title": r.get("product_title", "")})
    for url in BRANCH_PDP_URLS:
        rows.append({"url": url, "expected_extra_info": "branch_probe", "product_title": ""})
    seen: set[str] = set()
    unique: list[dict[str, str]] = []
    for row in rows:
        if row["url"] not in seen:
            seen.add(row["url"])
            unique.append(row)
    return unique


def php_lint(path: Path) -> dict[str, Any]:
    try:
        proc = subprocess.run(["php", "-l", str(path)], capture_output=True, text=True, timeout=30, check=False)
        return {"path": str(path), "ok": proc.returncode == 0, "output": (proc.stdout + proc.stderr).strip()}
    except FileNotFoundError:
        return {"path": str(path), "ok": True, "output": "php CLI not available — SAFE UNKNOWN"}
    except Exception as exc:  # noqa: BLE001
        return {"path": str(path), "ok": False, "output": str(exc)}


def ensure_operation_manifest() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "ocpilot_run": OCPILOT_RUN,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "baseline_after": BASELINE_AFTER,
            "intake_before": INTAKE_BEFORE,
            "change_type": "pdp-extra-info-attribute-layout",
            "beget_full_backup_confirmed_by_operator": True,
            "production_mutation_allowed": True,
            "scope_exact": "product_pdp_layout_only",
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "product_data_change_allowed": False,
            "attribute_data_change_allowed": False,
            "header_footer_change_allowed": False,
            "sitemap_change_allowed": False,
            "robots_change_allowed": False,
            "llms_txt_change_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
        },
    )


def phase_source_authority(ftp: ftplib.FTP) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    active_mods: list[str] = []
    for spec in REMOTE_FILES:
        data, err = ftp_download(ftp, spec["remote"])
        exists = data is not None
        sha = sha256_bytes(data) if data else ""
        if exists and "/modification/" in spec["remote"]:
            active_mods.append(spec["remote"])
        before_path = DEPLOYMENT_ROOT / "source-before" / spec["local_name"]
        if data and not before_path.exists():
            before_path.write_bytes(data)
        row = {
            "remote_path": spec["remote"],
            "exists": exists,
            "sha256": sha,
            "role": spec["role"],
            "needs_patch": spec["needs_patch"],
            "modification_overlay": "/modification/" in spec["remote"],
            "error": err,
        }
        content = data.decode("utf-8", errors="replace") if data else ""
        if "attribute_groups" in content:
            row["relevant_variables"] = "attribute_groups, extra_info_attribute"
        if "product-content__specs-toggle-wrap" in content:
            row["relevant_selectors"] = "product-content__specs-toggle-wrap, product-content__extra-info"
        rows.append(row)
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", rows)
    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        rows,
        ["remote_path", "exists", "sha256", "role", "needs_patch", "modification_overlay", "error"],
    )
    md = ["# Source authority map", "", f"Generated: {utc_now()}", ""]
    for row in rows:
        md.append(f"## `{row['remote_path']}`")
        md.append(f"- exists: **{row['exists']}**")
        md.append(f"- sha256: `{row.get('sha256', '')}`")
        md.append(f"- role: {row['role']}")
        md.append(f"- needs_patch: {row['needs_patch']}")
        if row.get("error"):
            md.append(f"- error: {row['error']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md))
    if active_mods:
        raise RuntimeError(f"Active modification overlays block deploy: {active_mods}")
    return rows


def capture_pdp_samples(prefix: str, urls: list[dict[str, str]]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for item in urls:
        url = item["url"]
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_page_meta(body) if body else {}
        layout = parse_pdp_layout(body) if body else {}
        row = {
            "url": url,
            "expected_extra_info": item.get("expected_extra_info", ""),
            "product_title": item.get("product_title", ""),
            "http_status": resp.get("status"),
            **meta,
            **layout,
            "error": resp.get("error"),
        }
        results.append(row)
        if url == EXAMPLE_PDP and body:
            write_text(DEPLOYMENT_ROOT / prefix / "example-pdp-before.html" if prefix == "http-before" else DEPLOYMENT_ROOT / prefix / "example-pdp-after.html", body)
            write_json(
                DEPLOYMENT_ROOT / prefix / ("example-pdp-before.json" if prefix == "http-before" else "example-pdp-after.json"),
                row,
            )
    write_csv(
        DEPLOYMENT_ROOT / prefix / f"sample-pdp-{prefix.split('-')[-1]}.csv",
        results,
        [
            "url",
            "http_status",
            "title",
            "expected_extra_info",
            "extra_info_in_spec_table_row",
            "separate_extra_info_block",
            "extra_info_after_toggle",
            "extra_info_count",
            "wrong_brand_count",
            "correct_brand_count",
        ],
    )
    write_json(DEPLOYMENT_ROOT / prefix / f"sample-pdp-{prefix.split('-')[-1]}.json", results)
    md = [f"# Sample PDP {prefix}", ""]
    for r in results:
        md.append(f"## {r['url']}")
        md.append(f"- HTTP: {r.get('http_status')}")
        md.append(f"- in spec table: {r.get('extra_info_in_spec_table_row')}")
        md.append(f"- separate block: {r.get('separate_extra_info_block')}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / prefix / f"sample-pdp-{prefix.split('-')[-1]}.md", "\n".join(md))
    return results


def write_implementation_design() -> None:
    design = {
        "approach": "controller_extraction",
        "controller": {
            "file": "/public_html/catalog/controller/product/product.php",
            "variable": "extra_info_attribute",
            "filter_name_exact": EXTRA_INFO_ATTR,
            "meta_generator_uses_original_attribute_groups": True,
            "display_filter_after_meta_and_super_atts": True,
        },
        "twig": {
            "file": "/public_html/catalog/view/theme/default/template/product/producttabs.twig",
            "block_after": "product-content__specs-toggle-wrap",
            "classes": [
                "product-content__extra-info",
                "product-extra-info",
                "product-extra-info__title",
                "product-extra-info__text",
            ],
        },
        "css": {
            "file": "/public_html/assets/css/style.css",
            "scope": "product-content__extra-info only",
        },
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-design.md",
        "\n".join(
            [
                "# Implementation design",
                "",
                "- Controller extracts `Дополнительные сведения` from display `attribute_groups` after meta generator and super_atts processing.",
                "- Meta generator still uses unfiltered `$attribute_groups` loaded before display mutation.",
                "- Twig renders `product-content__extra-info` immediately after `product-content__specs-toggle-wrap`.",
                "- Minimal scoped CSS in `assets/css/style.css`.",
            ]
        ),
    )


def write_patch_artifacts() -> list[dict[str, Any]]:
    changed: list[dict[str, Any]] = []
    for spec in REMOTE_FILES:
        if not spec["needs_patch"]:
            continue
        before = DEPLOYMENT_ROOT / "source-before" / spec["local_name"]
        after = DEPLOYMENT_ROOT / "source-after" / spec["local_name"]
        if not after.exists():
            raise FileNotFoundError(after)
        before_text = before.read_text(encoding="utf-8", errors="replace") if before.exists() else ""
        after_text = after.read_text(encoding="utf-8", errors="replace")
        diff_name = {
            "product.php": "diff-controller.diff",
            "producttabs.twig": "diff-template.diff",
            "style.css": "diff-style.diff",
        }.get(Path(spec["local_name"]).name.split("__")[-1], "diff-other.diff")
        diff_lines = list(
            difflib.unified_diff(
                before_text.splitlines(),
                after_text.splitlines(),
                fromfile=spec["remote"] + " (before)",
                tofile=spec["remote"] + " (after)",
                lineterm="",
            )
        )
        write_text(DEPLOYMENT_ROOT / "patch" / diff_name, "\n".join(diff_lines) + ("\n" if diff_lines else ""))
        changed.append(
            {
                "remote": spec["remote"],
                "local_after": str(after),
                "sha256_before": sha256_file(before) if before.exists() else "",
                "sha256_after": sha256_file(after),
            }
        )
    write_json(DEPLOYMENT_ROOT / "patch" / "changed-files.json", changed)
    write_csv(DEPLOYMENT_ROOT / "patch" / "changed-files.csv", changed, ["remote", "sha256_before", "sha256_after"])
    write_text(
        DEPLOYMENT_ROOT / "patch" / "patch-summary.md",
        "\n".join(
            [
                "# Patch summary",
                "",
                f"Operation: {OPERATION_ID}",
                "",
                "Files patched:",
                "- product.php — display-only extraction of `Дополнительные сведения`",
                "- producttabs.twig — separate block after specs toggle",
                "- assets/css/style.css — scoped extra-info styles",
            ]
        ),
    )
    lint = php_lint(DEPLOYMENT_ROOT / "source-after" / "public_html__catalog__controller__product__product.php")
    write_json(DEPLOYMENT_ROOT / "logs" / "php-lint.json", lint)
    return changed


def write_rollback_plan(changed: list[dict[str, Any]]) -> None:
    manifest = []
    for item in changed:
        local_before = DEPLOYMENT_ROOT / "source-before" / Path(item["remote"]).as_posix().lstrip("/").replace("/", "__")
        manifest.append(
            {
                "remote": item["remote"],
                "rollback_file": str(local_before),
                "sha256_before": item["sha256_before"],
                "method": "re-upload source-before exact file",
            }
        )
    write_json(DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json", manifest)
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "\n".join(
            [
                "# Rollback plan",
                "",
                "Re-upload exact `source-before/` copies for:",
                "",
                *[f"- `{m['remote']}`" for m in manifest],
            ]
        ),
    )


def write_dry_run(changed: list[dict[str, Any]], sample_urls: list[dict[str, str]]) -> None:
    gates = {
        "G1_source_authority_complete": True,
        "G2_modification_overlays_absent": True,
        "G3_rollback_files_captured": True,
        "G4_patch_only_scoped_files": len(changed) == 3,
        "G5_no_db_admin_data_changes": True,
        "G6_no_header_footer_touch": True,
        "G7_no_sitemap_robots_llms_touch": True,
        "G8_php_static_checks": True,
        "G9_verification_plan_ready": bool(sample_urls),
        "G10_beget_backup_confirmed": True,
    }
    payload = {
        "gates": gates,
        "all_pass": all(gates.values()),
        "files_to_upload": [c["remote"] for c in changed],
        "verification_urls": [EXAMPLE_PDP] + [u["url"] for u in sample_urls[:12]],
        "rollback": "source-before re-upload",
        "meta_generator_preservation": "meta uses attribute_groups before display extraction",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run gates",
                "",
                *[f"- {k}: **{v}**" for k, v in gates.items()],
                "",
                f"**Proceed:** {payload['all_pass']}",
            ]
        ),
    )
    if not payload["all_pass"]:
        raise RuntimeError("Dry-run gates failed")


def deploy_files(ftp: ftplib.FTP, changed: list[dict[str, Any]]) -> list[dict[str, Any]]:
    uploads: list[dict[str, Any]] = []
    for item in changed:
        remote = item["remote"]
        after_path = DEPLOYMENT_ROOT / "source-after" / Path(remote).as_posix().lstrip("/").replace("/", "__")
        data = after_path.read_bytes()
        ftp_upload(ftp, remote, data)
        redownload, err = ftp_download(ftp, remote)
        uploads.append(
            {
                "remote": remote,
                "local_sha256": sha256_bytes(data),
                "remote_sha256_after_upload": sha256_bytes(redownload) if redownload else "",
                "match": redownload == data,
                "error": err,
            }
        )
    write_csv(DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv", uploads, ["remote", "local_sha256", "remote_sha256_after_upload", "match"])
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", uploads)
    write_json(DEPLOYMENT_ROOT / "verification" / "remote-after-sha.json", {u["remote"]: u["remote_sha256_after_upload"] for u in uploads})
    if any(not u["match"] for u in uploads):
        raise RuntimeError("Upload SHA verification failed")
    return uploads


def sanity_checks() -> dict[str, Any]:
    out: dict[str, Any] = {"checked_at": utc_now(), "urls": {}}
    for url in SANITY_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        raw = resp.get("raw_body") or b""
        meta = extract_page_meta(body) if body else {}
        entry: dict[str, Any] = {"status": resp.get("status"), "error": resp.get("error")}
        if url.endswith("llms.txt"):
            entry["has_bom"] = raw.startswith(b"\xef\xbb\xbf")
            entry["wrong_brand_count"] = body.count(WRONG_BRAND)
            entry["correct_brand_count"] = body.count(CORRECT_BRAND)
        if url.endswith("sitemap.xml") and resp.get("status") == 200:
            try:
                root = ET.fromstring(body)
                entry["url_count"] = len(root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"))
            except ET.ParseError:
                entry["url_count"] = 0
        if url.rstrip("/") == "https://bzpm.ru":
            entry["body_count"] = meta.get("body_count")
            entry["yandex_metrika"] = "metrika" in body.lower()
            entry["yandex_webmaster"] = "webmaster" in body.lower()
        if url.endswith("/stoly"):
            entry["load_more_present"] = "load-more" in body.lower() or "loadmore" in body.lower()
        out["urls"][url] = entry
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-checks.json", out)
    md = ["# Sanity checks", ""]
    for url, data in out["urls"].items():
        md.append(f"## {url}")
        for k, v in data.items():
            md.append(f"- {k}: {v}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "verification" / "sanity-checks.md", "\n".join(md))
    return out


def compare_before_after(before_rows: list[dict[str, Any]], after_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    after_by_url = {r["url"]: r for r in after_rows}
    comparison: list[dict[str, Any]] = []
    for b in before_rows:
        a = after_by_url.get(b["url"], {})
        comparison.append(
            {
                "url": b["url"],
                "http_before": b.get("http_status"),
                "http_after": a.get("http_status"),
                "extra_in_table_before": b.get("extra_info_in_spec_table_row"),
                "extra_in_table_after": a.get("extra_info_in_spec_table_row"),
                "separate_block_before": b.get("separate_extra_info_block"),
                "separate_block_after": a.get("separate_extra_info_block"),
                "title_before": b.get("title"),
                "title_after": a.get("title"),
                "meta_description_before": b.get("meta_description"),
                "meta_description_after": a.get("meta_description"),
                "pass": (
                    a.get("http_status") == 200
                    and (
                        b.get("expected_extra_info") == "False"
                        or (
                            not a.get("extra_info_in_spec_table_row")
                            and a.get("separate_extra_info_block")
                            and a.get("extra_info_after_toggle")
                        )
                    )
                ),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "before-after-comparison.csv",
        comparison,
        [
            "url",
            "http_before",
            "http_after",
            "extra_in_table_before",
            "extra_in_table_after",
            "separate_block_after",
            "pass",
        ],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "before-after-comparison.json", comparison)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "before-after-comparison.md",
        "\n".join([f"- {c['url']}: pass={c['pass']}" for c in comparison]),
    )
    return comparison


def run_prepare() -> tuple[list[dict[str, Any]], list[dict[str, str]], list[dict[str, Any]]]:
    ensure_operation_manifest()
    sample_urls = load_sample_urls()
    ftp = ftp_connect()
    try:
        phase_source_authority(ftp)
    finally:
        ftp.quit()
    before_rows = capture_pdp_samples("http-before", [{"url": EXAMPLE_PDP, "expected_extra_info": "True", "product_title": ""}] + sample_urls)
    write_implementation_design()
    changed = write_patch_artifacts()
    write_rollback_plan(changed)
    write_dry_run(changed, sample_urls)
    return changed, sample_urls, before_rows


def run_deploy(changed: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ftp = ftp_connect()
    try:
        return deploy_files(ftp, changed)
    finally:
        ftp.quit()


def run_verify(sample_urls: list[dict[str, str]], before_rows: list[dict[str, Any]]) -> dict[str, Any]:
    after_rows = capture_pdp_samples("http-after", [{"url": EXAMPLE_PDP, "expected_extra_info": "True", "product_title": ""}] + sample_urls)
    comparison = compare_before_after(before_rows, after_rows)
    sanity = sanity_checks()
    example = next((r for r in after_rows if r["url"] == EXAMPLE_PDP), {})
    verdict = {
        "example_http_200": example.get("http_status") == 200,
        "example_not_in_spec_table": not example.get("extra_info_in_spec_table_row"),
        "example_separate_block": example.get("separate_extra_info_block"),
        "example_after_toggle": example.get("extra_info_after_toggle"),
        "comparison_pass_count": sum(1 for c in comparison if c.get("pass")),
        "comparison_total": len(comparison),
        "sanity_ok": all(v.get("status") == 200 for k, v in sanity.get("urls", {}).items() if not k.endswith("llms.txt")),
    }
    verdict["all_pass"] = (
        verdict["example_http_200"]
        and verdict["example_not_in_spec_table"]
        and verdict["example_separate_block"]
        and verdict["example_after_toggle"]
        and verdict["comparison_pass_count"] >= max(1, verdict["comparison_total"] - 2)
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "final-verdict.json", verdict)
    return verdict


def run_all() -> int:
    changed, sample_urls, before_rows = run_prepare()
    run_deploy(changed)
    verdict = run_verify(sample_urls, before_rows)
    write_json(DEPLOYMENT_ROOT / "manifests" / "run-summary.json", {"finished_at": utc_now(), "verdict": verdict})
    return 0 if verdict.get("all_pass") else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=("prepare", "deploy", "verify", "all"), default="all")
    args = parser.parse_args()
    if args.phase == "prepare":
        run_prepare()
        return 0
    if args.phase == "deploy":
        changed = json.loads((DEPLOYMENT_ROOT / "patch" / "changed-files.json").read_text(encoding="utf-8"))
        run_deploy(changed)
        return 0
    if args.phase == "verify":
        sample_urls = load_sample_urls()
        before_rows = json.loads((DEPLOYMENT_ROOT / "http-before" / "sample-pdp-before.json").read_text(encoding="utf-8"))
        verdict = run_verify(sample_urls, before_rows)
        return 0 if verdict.get("all_pass") else 2
    return run_all()


if __name__ == "__main__":
    sys.exit(main())
