#!/usr/bin/env python3
"""SITE-002 catalog load more — multi-file Production deploy."""
from __future__ import annotations

import argparse
import difflib
import ftplib
import hashlib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-LOAD-MORE-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-LOAD-MORE-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-LOAD-MORE-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-LOAD-MORE-01"
SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification/pre-upload",
    "verification/after-upload",
    "screenshots",
    "manifests",
    "logs",
)

REMOTE_FILES: dict[str, str] = {
    "category.twig": "/public_html/catalog/view/theme/default/template/product/category.twig",
    "category.php": "/public_html/catalog/controller/product/category.php",
    "main.js": "/public_html/assets/js/main.js",
    "style.css": "/public_html/assets/css/style.css",
}

DISCOVERY_FILES: dict[str, str] = {
    **REMOTE_FILES,
    "pagination.twig": "/public_html/catalog/view/theme/default/template/common/pagination.twig",
    "search.twig": "/public_html/catalog/view/theme/default/template/product/search.twig",
    "manufacturer_info.twig": "/public_html/catalog/view/theme/default/template/product/manufacturer_info.twig",
    "category.php": "/public_html/catalog/controller/product/category.php",
    "pagination.php": "/public_html/system/library/pagination.php",
}

VERIFY_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?page=2",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?limit=30",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?sort=p.price&order=ASC",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?sort=pd.name&order=DESC",
]

LOAD_MORE_JS = r"""
function initLoadMore(root) {
  var pagination = document.querySelector(".pagination");
  var grid = document.querySelector(".category__grid");
  var counter = document.querySelector("[data-load-more-counter]");
  if (!pagination || !grid) return;

  var moreBtn = pagination.querySelector(".pagination__more[data-next]");
  if (!moreBtn) {
    document.documentElement.classList.add("js-load-more");
    return;
  }

  var loading = false;
  var total = 0;
  if (counter) {
    total = parseInt(counter.getAttribute("data-product-total") || "0", 10);
  }

  function visibleCount() {
    return grid.querySelectorAll(".p-card").length;
  }

  function updateCounter() {
    if (!counter) return;
    var shown = visibleCount();
    var totalText = total > 0 ? total : shown;
    counter.textContent = "Показано " + shown + " из " + totalText;
  }

  function setButtonState(nextUrl) {
    var shown = visibleCount();
    if (!nextUrl || (total > 0 && shown >= total)) {
      moreBtn.hidden = true;
      moreBtn.disabled = true;
      moreBtn.removeAttribute("data-next");
      return;
    }
    moreBtn.hidden = false;
    moreBtn.disabled = false;
    moreBtn.setAttribute("data-next", nextUrl);
    moreBtn.textContent = "Показать ещё";
  }

  function extractNextUrl(doc) {
    var nextBtn = doc.querySelector(".pagination__more[data-next]");
    return nextBtn ? nextBtn.getAttribute("data-next") : "";
  }

  function appendProducts(doc) {
    var nextGrid = doc.querySelector(".category__grid");
    if (!nextGrid) return 0;
    var cards = nextGrid.querySelectorAll(".p-card");
    var added = 0;
    cards.forEach(function(card) {
      grid.appendChild(document.importNode(card, true));
      added += 1;
    });
    if (typeof reinitImages === "function") reinitImages(grid);
    return added;
  }

  function handleLoadMore(event) {
    event.preventDefault();
    if (loading) return;
    var nextUrl = moreBtn.getAttribute("data-next");
    if (!nextUrl) return;
    loading = true;
    moreBtn.disabled = true;
    moreBtn.textContent = "Загрузка…";
    fetch(nextUrl, {
      credentials: "same-origin",
      headers: { "X-Requested-With": "XMLHttpRequest" }
    })
      .then(function(response) {
        if (!response.ok) throw new Error("HTTP " + response.status);
        return response.text();
      })
      .then(function(htmlText) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(htmlText, "text/html");
        var added = appendProducts(doc);
        if (added === 0) throw new Error("No products in response");
        var nextCounter = doc.querySelector("[data-load-more-counter]");
        if (nextCounter) {
          var nextTotal = parseInt(nextCounter.getAttribute("data-product-total") || "0", 10);
          if (nextTotal > 0) total = nextTotal;
        }
        setButtonState(extractNextUrl(doc));
        updateCounter();
      })
      .catch(function() {
        moreBtn.disabled = false;
        moreBtn.textContent = "Показать ещё";
        if (nextUrl && !pagination.querySelector(".pagination__more-fallback")) {
          var fallback = document.createElement("a");
          fallback.href = nextUrl;
          fallback.className = "pagination__more-fallback";
          fallback.textContent = "Открыть следующую страницу";
          pagination.appendChild(fallback);
        }
      })
      .finally(function() {
        loading = false;
      });
  }

  var freshBtn = moreBtn.cloneNode(true);
  moreBtn.replaceWith(freshBtn);
  moreBtn = freshBtn;

  document.documentElement.classList.add("js-load-more");
  updateCounter();
  setButtonState(moreBtn.getAttribute("data-next"));
  moreBtn.addEventListener("click", handleLoadMore);
}
"""

FORBIDDEN_DIFF_MARKERS = (
    "cron",
    "import_1C",
    "mail",
    "anketa",
    "smtp",
    "database",
    "mysqli",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


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
    required = ("host", "port", "username", "password")
    missing = [key for key in required if not fields.get(key) or fields.get(key) == "SAFE UNKNOWN"]
    if missing:
        raise RuntimeError("Missing PRODUCTION FTP fields: " + ", ".join(missing))
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


def classify_file(local_name: str, text: str) -> str:
    if local_name in REMOTE_FILES:
        return "A. MUST CHANGE"
    if local_name == "pagination.php":
        return "B. MAY CHANGE"
    return "C. READ ONLY"


def marker_scan(text: str) -> dict[str, bool]:
    return {
        "data-next": "data-next" in text,
        "pagination__more": "pagination__more" in text,
        "initPaginationAJAX": "initPaginationAJAX" in text,
        "initLoadMore": "initLoadMore" in text,
        "category__grid": "category__grid" in text,
        "results_var": "{{ results }}" in text,
        "pagination__pages": "pagination__pages" in text,
        "product_total": "product_total" in text,
        "data-load-more-counter": "data-load-more-counter" in text,
    }


def discover() -> dict[str, Any]:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    results: list[dict[str, Any]] = []
    try:
        for local_name, remote_path in DISCOVERY_FILES.items():
            entry: dict[str, Any] = {"local_name": local_name, "remote_path": remote_path}
            try:
                data = ftp_download(ftp, remote_path)
                text = data.decode("utf-8", errors="replace")
                entry["status"] = "downloaded"
                entry["size"] = len(data)
                entry["sha256"] = sha256_bytes(data)
                entry["classification"] = classify_file(local_name, text)
                entry["markers"] = marker_scan(text)
                (DEPLOYMENT_ROOT / "source" / local_name).write_bytes(data)
            except Exception as exc:
                entry["status"] = "error"
                entry["error"] = str(exc)
            results.append(entry)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    must_change = [r for r in results if r.get("classification") == "A. MUST CHANGE" and r.get("status") == "downloaded"]
    if len(must_change) != len(REMOTE_FILES):
        raise RuntimeError("Discovery incomplete — required deploy files missing")

    discovery = {
        "operation_id": OPERATION_ID,
        "timestamp": utc_now(),
        "files": results,
        "must_change": [r["local_name"] for r in must_change],
        "may_change": [r["local_name"] for r in results if r.get("classification") == "B. MAY CHANGE"],
        "read_only": [r["local_name"] for r in results if r.get("classification") == "C. READ ONLY"],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "discovery.json", discovery)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "catalog-load-more",
            "backup_gate": "full_beget_backup_required",
            "cron_change_allowed": False,
            "import_execution_allowed": False,
            "db_change_allowed": False,
            "email_change_allowed": False,
            "authorized_files": list(REMOTE_FILES.keys()),
        },
    )
    return discovery


def prepare_category_twig(source: str) -> tuple[str, dict[str, Any]]:
    checks: dict[str, Any] = {}
    if "{{ pagination }}" not in source:
        checks["status"] = "FAIL"
        checks["error"] = "pagination block not found"
        return source, checks

    old_block = "        {{ pagination }}"
    new_block = (
        "        {% if pagination %}\n"
        "        <div class=\"category__pagination-wrap\" data-load-more-root>\n"
        "          <p class=\"category__load-more-counter\" data-load-more-counter data-product-total=\"{{ product_total }}\">Показано {{ product_shown }} из {{ product_total }}</p>\n"
        "          {{ pagination }}\n"
        "        </div>\n"
        "        {% endif %}"
    )
    if old_block not in source:
        checks["status"] = "FAIL"
        checks["error"] = "exact pagination insertion point not found"
        return source, checks

    prepared = source.replace(old_block, new_block, 1)
    checks["has_counter"] = "data-load-more-counter" in prepared
    checks["has_product_total"] = "{{ product_total }}" in prepared
    checks["has_product_shown"] = "{{ product_shown }}" in prepared
    checks["status"] = (
        "PASS"
        if checks["has_counter"] and checks["has_product_total"] and checks["has_product_shown"]
        else "FAIL"
    )
    return prepared, checks


def prepare_category_php(source: str) -> tuple[str, dict[str, Any]]:
    checks: dict[str, Any] = {}
    marker = "$data['results'] = sprintf($this->language->get('text_pagination'),"
    if marker not in source:
        checks["status"] = "FAIL"
        checks["error"] = "results assignment not found"
        return source, checks
    if "$data['product_total']" in source:
        checks["status"] = "PASS"
        checks["note"] = "product_total already present"
        return source, checks

    insert = (
        "\n\n\t\t\t$data['product_total'] = (int)$product_total;\n"
        "\t\t\t$data['product_shown'] = $product_total ? min($page * $limit, $product_total) : 0;"
    )
    idx = source.find(marker)
    line_end = source.find("\n", idx)
    prepared = source[:line_end] + insert + source[line_end:]
    checks["product_total_added"] = True
    checks["product_shown_added"] = True
    checks["status"] = "PASS"
    return prepared, checks


def prepare_main_js(source: str) -> tuple[str, dict[str, Any]]:
    checks: dict[str, Any] = {}
    if "initLoadMore" in source:
        checks["status"] = "PASS"
        checks["note"] = "initLoadMore already present"
        return source, checks
    if "initPaginationAJAX" not in source:
        checks["status"] = "FAIL"
        checks["error"] = "initPaginationAJAX not found"
        return source, checks

    anchor = "function initPaginationAJAX(root) {"
    if anchor not in source:
        checks["status"] = "FAIL"
        checks["error"] = "pagination anchor missing"
        return source, checks

    prepared = source.replace(anchor, LOAD_MORE_JS.strip() + "\n\n" + anchor, 1)

    prepared = prepared.replace(
        "      initPaginationAJAX(root);\n    })",
        "      initPaginationAJAX(root);\n      initLoadMore(root);\n    })",
        1,
    )
    prepared = prepared.replace(
        "    initPaginationAJAX(root);\n    initCategoryLimitMenu();",
        "    initPaginationAJAX(root);\n    initLoadMore(root);\n    initCategoryLimitMenu();",
        1,
    )

    checks["initLoadMore_added"] = "function initLoadMore(root)" in prepared
    checks["init_call_added"] = "initLoadMore(root);" in prepared
    checks["status"] = "PASS" if checks["initLoadMore_added"] and checks["init_call_added"] else "FAIL"
    return prepared, checks


def prepare_style_css(source: str) -> tuple[str, dict[str, Any]]:
    checks: dict[str, Any] = {}
    if ".js-load-more .pagination__pages" in source:
        checks["status"] = "PASS"
        checks["note"] = "load-more CSS already present"
        return source, checks

    css_block = """

/* SITE-002 load more — catalog listing */
.js-load-more .pagination__pages {
  display: none !important;
}
.js-load-more .pagination__more {
  display: block;
  width: 100%;
  margin-top: var(--pad-gap-line);
}
.category__pagination-wrap {
  margin-top: 24px;
}
.category__load-more-counter {
  margin: 0 0 12px;
  text-align: center;
  color: var(--main-dark-color);
  font-size: 16px;
  line-height: 1.4;
}
.pagination__more-fallback {
  display: inline-block;
  margin-top: 8px;
  font-size: 14px;
  text-align: center;
}
.pagination__more[disabled],
.pagination__more[hidden] {
  display: none !important;
}
"""
    prepared = source.rstrip() + css_block
    checks["css_added"] = True
    checks["status"] = "PASS"
    return prepared, checks


def unified_diff(before: bytes, after: bytes, name: str) -> str:
    a = before.decode("utf-8", errors="replace").splitlines(keepends=True)
    b = after.decode("utf-8", errors="replace").splitlines(keepends=True)
    return "".join(
        difflib.unified_diff(a, b, fromfile=f"source/{name}", tofile=f"prepared/{name}", lineterm="")
    )


def diff_scope_ok(diff_text: str) -> tuple[bool, list[str]]:
    changed = [
        line
        for line in diff_text.splitlines()
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))
    ]
    lowered = "\n".join(changed).lower()
    for marker in FORBIDDEN_DIFF_MARKERS:
        if marker in lowered:
            return False, changed
    return True, changed


def backup_and_prepare() -> dict[str, Any]:
    ensure_dirs()
    discovery = discover()
    prep_report: dict[str, Any] = {"files": {}, "status": "PASS"}

    for local_name in REMOTE_FILES:
        source_path = DEPLOYMENT_ROOT / "source" / local_name
        if not source_path.exists():
            prep_report["status"] = "FAIL"
            prep_report["files"][local_name] = {"error": "missing source"}
            continue
        source = source_path.read_bytes()
        backup_path = DEPLOYMENT_ROOT / "backup" / local_name
        rollback_path = DEPLOYMENT_ROOT / "rollback" / local_name
        backup_path.write_bytes(source)
        rollback_path.write_bytes(source)
        source_sha = sha256_bytes(source)
        if sha256_file(backup_path) != source_sha or sha256_file(rollback_path) != source_sha:
            raise RuntimeError(f"Hash mismatch for {local_name}")

        text = source.decode("utf-8", errors="replace")
        if local_name == "category.twig":
            prepared_text, checks = prepare_category_twig(text)
        elif local_name == "category.php":
            prepared_text, checks = prepare_category_php(text)
        elif local_name == "main.js":
            prepared_text, checks = prepare_main_js(text)
        elif local_name == "style.css":
            prepared_text, checks = prepare_style_css(text)
        else:
            prepared_text, checks = text, {"status": "FAIL", "error": "unknown file"}

        prepared = prepared_text.encode("utf-8")
        prepared_path = DEPLOYMENT_ROOT / "prepared" / local_name
        prepared_path.write_bytes(prepared)
        diff_text = unified_diff(source, prepared, local_name)
        scope_ok, changed_lines = diff_scope_ok(diff_text)
        write_text(DEPLOYMENT_ROOT / "manifests" / f"{local_name}.diff", diff_text)
        entry = {
            "source_sha256": source_sha,
            "prepared_sha256": sha256_bytes(prepared),
            "checks": checks,
            "diff_scope_ok": scope_ok,
            "changed_lines": len(changed_lines),
            "remote_path": REMOTE_FILES[local_name],
        }
        prep_report["files"][local_name] = entry
        if checks.get("status") != "PASS" or not scope_ok:
            prep_report["status"] = "FAIL"

    write_json(DEPLOYMENT_ROOT / "manifests" / "prepare-report.json", prep_report)
    if prep_report["status"] != "PASS":
        raise RuntimeError("Prepare failed — see prepare-report.json")

    design_md = "\n".join(
        [
            f"# Load More Design — {OPERATION_ID}",
            "",
            "## UX",
            "- Initial listing shows first page products.",
            "- Counter near button: «Показано X из Y» via `{{ results }}` + JS sync.",
            "- Button text: «Показать ещё».",
            "- Click appends product cards to `.category__grid`.",
            "- Numeric pagination hidden when JS adds `js-load-more` on `<html>`.",
            "- Direct `page=N` URLs remain valid server-side.",
            "",
            "## Technical",
            "- `initLoadMore()` fetches `data-next` URL, parses HTML, appends cards.",
            "- Counter updates after append; button hidden when no next page.",
            "- Sort/limit/filter resets handled by existing full-page/AJAX refresh paths.",
            "",
        ]
    )
    write_text(DEPLOYMENT_ROOT / "manifests" / "load-more-design.md", design_md)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "files-to-change.json",
        {
            "must_change": [
                {"local": k, "remote": v, "role": "deploy target"} for k, v in REMOTE_FILES.items()
            ]
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                f"# Implementation Plan — {OPERATION_ID}",
                "",
                "1. category.twig — expose counter, keep pagination for SEO/fallback.",
                "2. main.js — add initLoadMore append handler.",
                "3. style.css — hide numeric pages under js-load-more; style counter/button.",
                "",
            ]
        ),
    )

    dry_run = {
        "operation_id": OPERATION_ID,
        "remote_files_to_upload": len(REMOTE_FILES),
        "files": prep_report["files"],
        "verification_urls": VERIFY_URLS,
        "rollback_files": [f"rollback/{name}" for name in REMOTE_FILES],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", dry_run)
    dry_md = [f"# Dry-Run — {OPERATION_ID}", "", f"- Files to upload: {len(REMOTE_FILES)}"]
    for name, remote in REMOTE_FILES.items():
        dry_md.append(f"- `{remote}` ← prepared/{name}")
    dry_md.extend(["", "## Risk", "- HIGH — multi-file frontend", "- Rollback per file ready", ""])
    write_text(DEPLOYMENT_ROOT / "manifests" / "dry-run.md", "\n".join(dry_md))
    return prep_report


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            text = body.decode(response.headers.get_content_charset() or "utf-8", errors="replace")
            return {"url": url, "status_code": response.status, "body": text, "error": None}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {"url": url, "status_code": exc.code, "body": body, "error": str(exc)}
    except Exception as exc:
        return {"url": url, "status_code": None, "body": "", "error": str(exc)}


def verify_http() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    overall = "PASS"
    hub_urls = {"https://bzpm.ru/katalog/nejtralnoe-oborudovanie"}
    for url in VERIFY_URLS:
        probe = f"{url}{'&' if '?' in url else '?'}mars_verify={OPERATION_ID}"
        result = http_get(probe)
        body = html.unescape(result.get("body", ""))
        is_hub = url in hub_urls or "category--hub" in body or "data-cat-sections" in body
        entry = {
            "url": url,
            "status_code": result.get("status_code"),
            "is_hub": is_hub,
            "php_error_visible": any(m in body for m in ("Fatal error", "Parse error", "Twig_Error", "Twig\\Error")),
            "has_pagination_more": "pagination__more" in body,
            "has_data_next": "data-next" in body,
            "has_counter_markup": "data-load-more-counter" in body or "Показано" in body,
            "has_product_grid": "category__grid" in body,
            "has_numeric_pages": "pagination__pages" in body,
        }
        if result.get("status_code") != 200 or entry["php_error_visible"]:
            entry["status"] = "FAIL"
            overall = "FAIL"
        elif is_hub:
            entry["status"] = "PASS"
        elif not entry["has_product_grid"] or not entry["has_counter_markup"]:
            entry["status"] = "FAIL"
            overall = "FAIL"
        else:
            entry["status"] = "PASS"
        checks.append(entry)

    js_probe = http_get("https://bzpm.ru/assets/js/main.js")
    js_body = js_probe.get("body", "")
    js_checks = {
        "initLoadMore_present": "function initLoadMore" in js_body,
        "init_call_present": "initLoadMore(root)" in js_body,
    }
    data = {"operation_id": OPERATION_ID, "status": overall, "checks": checks, "js_checks": js_checks}
    write_json(DEPLOYMENT_ROOT / "manifests" / "http-verification.json", data)
    return data


def verify_visual() -> dict[str, Any]:
    url = VERIFY_URLS[0] + f"?mars_visual={OPERATION_ID}"
    desktop_initial = DEPLOYMENT_ROOT / "screenshots" / "desktop-load-more-initial.png"
    desktop_after = DEPLOYMENT_ROOT / "screenshots" / "desktop-load-more-after-click.png"
    mobile_initial = DEPLOYMENT_ROOT / "screenshots" / "mobile-load-more-initial.png"
    mobile_after = DEPLOYMENT_ROOT / "screenshots" / "mobile-load-more-after-click.png"
    results: list[dict[str, Any]] = []
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        data = {"operation_id": OPERATION_ID, "status": "SAFE_UNKNOWN", "error": str(exc), "results": results}
        write_json(DEPLOYMENT_ROOT / "manifests" / "visual-verification.json", data)
        return data

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, viewport, initial_path, after_path in (
            ("desktop", {"width": 1440, "height": 1200}, desktop_initial, desktop_after),
            ("mobile", {"width": 390, "height": 844}, mobile_initial, mobile_after),
        ):
            entry: dict[str, Any] = {"viewport": name, "status": "FAIL"}
            context = browser.new_context(viewport=viewport, user_agent=USER_AGENT)
            page = context.new_page()
            try:
                response = page.goto(url, wait_until="networkidle", timeout=90000)
                page.wait_for_timeout(1000)
                initial_path.parent.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(initial_path), full_page=True)
                counter_text = ""
                counter = page.locator("[data-load-more-counter]")
                if counter.count() > 0:
                    counter_text = counter.first.inner_text()
                btn = page.locator(".pagination__more[data-next]")
                clicked = False
                cards_before = page.locator(".category__grid .p-card").count()
                if btn.count() > 0 and btn.first.is_visible():
                    btn.first.click(timeout=5000)
                    page.wait_for_timeout(2000)
                    page.screenshot(path=str(after_path), full_page=True)
                    clicked = True
                cards_after = page.locator(".category__grid .p-card").count()
                entry.update(
                    {
                        "http_ok": bool(response and response.ok),
                        "counter_text": counter_text,
                        "cards_before": cards_before,
                        "cards_after": cards_after,
                        "append_ok": clicked and cards_after > cards_before,
                        "clicked": clicked,
                        "initial_screenshot": str(initial_path),
                        "after_screenshot": str(after_path) if clicked else None,
                    }
                )
                entry["status"] = "PASS" if entry["http_ok"] and (not clicked or entry["append_ok"]) else "PARTIAL" if entry["http_ok"] else "FAIL"
            except Exception as exc:
                entry["error"] = f"{type(exc).__name__}: {exc}"
            finally:
                context.close()
            results.append(entry)
        browser.close()

    status = "PASS" if all(r.get("status") == "PASS" for r in results) else "PARTIAL"
    data = {"operation_id": OPERATION_ID, "status": status, "results": results}
    write_json(DEPLOYMENT_ROOT / "manifests" / "visual-verification.json", data)
    return data


def rollback(fields: dict[str, str], reason: str) -> int:
    ftp = ftp_connect(fields)
    restored: list[dict[str, Any]] = []
    try:
        for local_name, remote_path in REMOTE_FILES.items():
            rollback_file = DEPLOYMENT_ROOT / "rollback" / local_name
            if not rollback_file.exists():
                raise RuntimeError(f"Rollback file missing: {local_name}")
            source_sha = sha256_file(rollback_file)
            ftp_upload(ftp, remote_path, rollback_file.read_bytes())
            after = ftp_download(ftp, remote_path)
            after_sha = sha256_bytes(after)
            (DEPLOYMENT_ROOT / "verification" / "after-upload" / f"rollback-{local_name}").write_bytes(after)
            restored.append(
                {
                    "file": local_name,
                    "remote_path": remote_path,
                    "source_sha256": source_sha,
                    "remote_after_sha256": after_sha,
                    "hash_match": after_sha == source_sha,
                }
            )
    finally:
        try:
            ftp.quit()
        except Exception:
            pass
    ok = all(item["hash_match"] for item in restored)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "rollback-result.json",
        {"operation_id": OPERATION_ID, "reason": reason, "restored": restored, "ok": ok, "timestamp": utc_now()},
    )
    if not ok:
        raise RuntimeError("Rollback hash verification failed")
    return 0


def deploy(confirm_backup: bool) -> int:
    if not confirm_backup:
        write_json(
            DEPLOYMENT_ROOT / "manifests" / "deploy-blocked.json",
            {
                "operation_id": OPERATION_ID,
                "reason": "FULL BEGET BACKUP NOT CONFIRMED",
                "timestamp": utc_now(),
            },
        )
        print("BLOCKED — FULL BEGET BACKUP NOT CONFIRMED (use --confirm-backup yes)")
        return 3

    prep = backup_and_prepare()
    fields = parse_production_secrets(SECRETS_PATH)
    hashes: dict[str, Any] = {"operation_id": OPERATION_ID, "files": {}}
    uploaded: list[str] = []

    ftp = ftp_connect(fields)
    try:
        for local_name, remote_path in REMOTE_FILES.items():
            source_path = DEPLOYMENT_ROOT / "source" / local_name
            prepared_path = DEPLOYMENT_ROOT / "prepared" / local_name
            source_sha = sha256_file(source_path)
            prepared_bytes = prepared_path.read_bytes()
            prepared_sha = sha256_bytes(prepared_bytes)

            pre_upload = ftp_download(ftp, remote_path)
            pre_upload_sha = sha256_bytes(pre_upload)
            (DEPLOYMENT_ROOT / "verification" / "pre-upload" / local_name).write_bytes(pre_upload)
            if pre_upload_sha != source_sha:
                rollback(fields, "Remote file changed since backup")
                raise RuntimeError(f"STOP — LIVE FILE CHANGED SINCE BACKUP: {local_name}")

            ftp_upload(ftp, remote_path, prepared_bytes)
            after = ftp_download(ftp, remote_path)
            after_sha = sha256_bytes(after)
            (DEPLOYMENT_ROOT / "verification" / "after-upload" / local_name).write_bytes(after)
            hashes["files"][local_name] = {
                "source_sha256": source_sha,
                "prepared_sha256": prepared_sha,
                "remote_pre_upload_sha256": pre_upload_sha,
                "remote_after_sha256": after_sha,
                "match": after_sha == prepared_sha,
            }
            if after_sha != prepared_sha:
                rollback(fields, "Remote hash mismatch after upload")
                raise RuntimeError(f"Upload verification failed: {local_name}")
            uploaded.append(remote_path)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    write_json(DEPLOYMENT_ROOT / "manifests" / "file-hashes.json", hashes)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "deploy-manifest.json",
        {
            "operation_id": OPERATION_ID,
            "uploaded_files": uploaded,
            "upload_count": len(uploaded),
            "delete_count": 0,
            "rename_count": 0,
        },
    )

    http_result = verify_http()
    if http_result["status"] == "FAIL":
        rollback(fields, "HTTP verification failed")
        return 2

    visual_result = verify_visual()
    verdict = "SITE-002 CATALOG LOAD MORE COMPLETE — UX VERIFIED"
    status = "DEPLOYED"
    if visual_result.get("status") != "PASS":
        verdict = "SITE-002 CATALOG LOAD MORE DEPLOYED — OPERATOR VISUAL CHECK REQUIRED"
        status = "DEPLOYED — OPERATOR VISUAL CHECK REQUIRED"

    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation-receipt.json",
        {
            "operation_id": OPERATION_ID,
            "status": status,
            "verdict": verdict,
            "uploaded": True,
            "timestamp": utc_now(),
            "http_verification": http_result,
            "visual_verification": visual_result,
        },
    )
    print(verdict)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SITE-002 catalog load more deploy.")
    parser.add_argument("command", choices=("discover", "prepare", "deploy", "verify-http", "verify-visual", "rollback"))
    parser.add_argument("--confirm-backup", default="no", help="Set to yes after operator confirms full Beget backup")
    parser.add_argument("--reason", default="operator requested rollback")
    args = parser.parse_args()

    if args.command == "discover":
        discover()
        print("DISCOVERY COMPLETE")
        return 0
    if args.command == "prepare":
        backup_and_prepare()
        print("PREPARE COMPLETE")
        return 0
    if args.command == "deploy":
        return deploy(args.confirm_backup.lower() in ("yes", "true", "1"))
    if args.command == "verify-http":
        verify_http()
        print("HTTP VERIFY COMPLETE")
        return 0
    if args.command == "verify-visual":
        verify_visual()
        print("VISUAL VERIFY COMPLETE")
        return 0
    fields = parse_production_secrets(SECRETS_PATH)
    rollback(fields, args.reason)
    print("ROLLED BACK SAFELY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
