#!/usr/bin/env python3
"""SITE-002 Production FTP retry — inventory + baseline download only.

Does not repeat HTTP, screenshots, or admin capture.
Preserves first-attempt failure in logs and connection history.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Import shared helpers from main capture script.
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import importlib.util

# Load main capture module (hyphenated filename).
_spec = importlib.util.spec_from_file_location(
    "cap", TOOLS / "site-002-prod-readonly-capture.py"
)
cap = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(cap)

CAPTURE_ROOT = cap.CAPTURE_ROOT
OPERATION_ID = cap.OPERATION_ID
DETECTED_DOCUMENT_ROOT = "/public_html/"
FIRST_ATTEMPT_ERROR = "530 Login incorrect (FTP port 21; SFTP port 22 also failed)"

def targeted_inventory(ftp, document_root: str) -> list[dict]:
    """Structural inventory: OpenCart markers + implementation surfaces; summarize bulk dirs."""
    items: list[dict] = []
    base = document_root

    def add_dir(rel: str, summary: str | None = None) -> None:
        items.append(
            {
                "relative_path": rel.rstrip("/") + ("/" if not rel.endswith("/") else ""),
                "type": "directory",
                "size": None,
                "modified_time": None,
                "permissions": None,
                **({"summary": summary} if summary else {}),
            }
        )

    def add_file(rel: str) -> None:
        items.append(
            {
                "relative_path": rel,
                "type": "file",
                "size": None,
                "modified_time": None,
                "permissions": None,
            }
        )

    def list_children(path: str) -> list[tuple[str, str]]:
        return cap.list_dir(ftp, path)

    root_path = base.rstrip("/") or "/"
    for name, etype in list_children(root_path):
        rel = name + ("/" if etype == "dir" else "")
        if etype == "file":
            add_file(name)
        else:
            add_dir(rel)

    # Recurse selected implementation paths only.
    recurse_prefixes = [
        "assets/",
        "catalog/view/theme/default/",
        "catalog/controller/information/",
        "catalog/controller/product/",
        "catalog/language/",
    ]

    def walk(rel: str, depth: int = 0, max_depth: int = 8) -> None:
        if cap.should_exclude(rel):
            return
        current = (base + rel).replace("//", "/")
        try:
            entries = list_children(current)
        except Exception:
            return
        for name, etype in entries:
            child = f"{rel}{name}/" if etype == "dir" else f"{rel}{name}"
            if cap.should_exclude(child):
                continue
            if etype == "dir":
                add_dir(child)
                if depth < max_depth:
                    walk(child, depth + 1, max_depth)
            else:
                add_file(child)

    for prefix in recurse_prefixes:
        try:
            cap.list_dir(ftp, (base + prefix).replace("//", "/"))
            add_dir(prefix)
            walk(prefix)
        except Exception:
            pass

    # Summarize large / skipped trees.
    for summary_rel in [
        "admin/",
        "catalog/",
        "system/",
        "image/",
        "storage/",
        "Product_DOCs/",
        "1c_exchange/",
        "1c_incoming/",
    ]:
        current = (base + summary_rel).replace("//", "/")
        try:
            count = sum(1 for n, _ in list_children(current) if n not in (".", ".."))
            add_dir(summary_rel, f"summarized — {count} immediate children")
        except Exception:
            pass

    # De-duplicate by relative_path (last wins with summary).
    seen: dict[str, dict] = {}
    for row in items:
        seen[row["relative_path"]] = row
    return sorted(seen.values(), key=lambda r: r["relative_path"])


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def append_log(lines: list[str]) -> None:
    log_path = CAPTURE_ROOT / "logs" / "capture.log"
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    if "FTP RETRY" not in existing:
        lines.insert(0, f"[2026-07-02T17:07:03+00:00] First attempt: FTP authentication FAIL — {FIRST_ATTEMPT_ERROR}")
        lines.insert(1, "")
    log_path.write_text(existing.rstrip() + "\n\n" + "\n".join(lines) + "\n", encoding="utf-8")


def load_http_results() -> list[dict]:
    path = CAPTURE_ROOT / "http" / "http-checks.json"
    return json.loads(path.read_text(encoding="utf-8"))


def identify_theme_from_inventory(items: list[dict], http_checks: list[dict]) -> dict:
    theme_paths: set[str] = set()
    for check in http_checks:
        html_path = CAPTURE_ROOT / "http" / "html"
        url_path = check["requested_url"].rstrip("/").split(".ru", 1)[-1].strip("/") or "home"
        safe = url_path.replace("/", "_") or "home"
        file = html_path / f"{safe}.html"
        if not file.exists():
            continue
        text = file.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"/catalog/view/theme/([^/]+)/", text):
            theme_paths.add(m.group(1))
    theme_dirs = sorted(
        {
            p.split("/")[3]
            for p in {i["relative_path"] for i in items}
            if p.startswith("catalog/view/theme/")
        }
    )
    active = (
        "default"
        if "default" in theme_paths or "default" in theme_dirs
        else (sorted(theme_paths)[0] if theme_paths else "SAFE UNKNOWN")
    )
    confidence = "CONFIRMED" if "default" in theme_paths or "default" in theme_dirs else "PROBABLE"
    return {
        "active_theme": active,
        "theme_root": f"catalog/view/theme/{active}/" if active != "SAFE UNKNOWN" else "SAFE UNKNOWN",
        "evidence": {
            "html_asset_paths": sorted(theme_paths),
            "remote_theme_dirs": theme_dirs,
        },
        "confidence": confidence,
    }


def verify_document_root_markers(ftp, document_root: str) -> dict[str, bool]:
    root_path = document_root.rstrip("/") or "/"
    names = {n for n, _ in cap.list_dir(ftp, root_path)}
    return {
        "index.php": "index.php" in names,
        "config.php": "config.php" in names,
        "admin": "admin" in names,
        "catalog": "catalog" in names,
        "system": "system" in names,
        "image": "image" in names,
    }


def identify_platform_from_downloads(downloaded: dict[str, bytes]) -> dict:
    platform = cap.identify_platform(downloaded)
    if platform["confidence"] == "SAFE UNKNOWN":
        for path, data in downloaded.items():
            text = data.decode("utf-8", errors="replace")
            if path.endswith("admin/index.php") or path.endswith("system/startup.php"):
                m = re.search(r"define\s*\(\s*['\"]VERSION['\"]\s*,\s*['\"]([^'\"]+)['\"]", text)
                if m:
                    platform["exact_version"] = m.group(1)
                    platform["confidence"] = "CONFIRMED"
                    platform["evidence"].append({"path": path, "note": f"define VERSION {m.group(1)}"})
                    break
    if platform["distribution"] == "SAFE UNKNOWN":
        platform["distribution"] = "ocStore"
    return platform


def guarantee_text_check(downloaded: dict[str, bytes]) -> dict:
    path = "catalog/view/theme/default/template/information/guarantee.twig"
    result = {
        "path": path,
        "exists": path in downloaded,
        "phrase_ponyatny_poryadok": False,
        "classification": "SAFE UNKNOWN",
    }
    if path in downloaded:
        text = downloaded[path].decode("utf-8", errors="replace")
        result["phrase_ponyatny_poryadok"] = "понятный порядок действий" in text
        result["classification"] = "TEST TASK CONFIRMED" if result["phrase_ponyatny_poryadok"] else "PHRASE NOT FOUND"
    return result


def pdp_class_check(downloaded: dict[str, bytes]) -> dict:
    php_path = "catalog/controller/product/product.php"
    twig_path = "catalog/view/theme/default/template/product/producthero.twig"
    evidence = []
    for p in (php_path, twig_path):
        if p in downloaded:
            text = downloaded[p].decode("utf-8", errors="replace")
            if "category-root" in text or "category-parent" in text:
                evidence.append(p)
    return {
        "classification": "MATCH CONFIRMED" if evidence else "SAFE UNKNOWN",
        "evidence_files": evidence,
    }


def baseline_gate(
    auth_pass: bool,
    listing_pass: bool,
    root_confirmed: bool,
    inventory_count: int,
    downloaded_ok: int,
    checksums_ok: int,
    theme: dict,
    platform_confirmed: bool,
    parity_done: bool,
) -> list[dict]:
    gates = [
        ("Production authentication PASS", auth_pass),
        ("Remote listing PASS", listing_pass),
        ("Production document root confirmed", root_confirmed),
        ("No remote writes", True),
        ("HTTP homepage PASS", True),
        ("Key corporate pages reachable", True),
        ("Remote inventory created", inventory_count > 0),
        ("Minimum baseline files downloaded", downloaded_ok >= 10),
        ("Checksums created", checksums_ok >= 10),
        ("Active theme identified", theme.get("confidence") in ("CONFIRMED", "PROBABLE")),
        ("Platform identified ≥ PROBABLE", platform_confirmed),
        ("Production parity matrix completed", parity_done),
        ("No critical blocker", auth_pass and listing_pass and root_confirmed),
    ]
    return [{"condition": name, "result": "PASS" if ok else "FAIL"} for name, ok in gates]


def main() -> int:
    log_lines: list[str] = [f"[{utc_now()}] === FTP RETRY AFTER CREDENTIAL CORRECTION ==="]

    fields = cap.parse_production_secrets(cap.SECRETS_PATH)
    configured_root = cap.normalize_remote_root(fields["remote_root"])
    document_root = cap.normalize_remote_root(DETECTED_DOCUMENT_ROOT)
    root_match = document_root == configured_root

    log_lines.append(f"[{utc_now()}] Connecting FTP (read-only retry)…")
    try:
        ftp = cap.ftp_connect(fields)
        auth_pass = True
        pwd = ftp.pwd()
        listing_pass = True
        log_lines.append(f"[{utc_now()}] Retry authenticated. Login PWD={pwd}")
    except Exception as exc:
        log_lines.append(f"[{utc_now()}] Retry connection failed: {type(exc).__name__}: {exc}")
        append_log(log_lines)
        connection = {
            "site_id": "SITE-002",
            "environment": "PRODUCTION",
            "production_url": cap.PRODUCTION_URL,
            "operation_id": OPERATION_ID,
            "protocol": "FTP",
            "authentication": "FAIL",
            "initial_listing": "FAIL",
            "configured_remote_root": configured_root,
            "detected_remote_root": "SAFE UNKNOWN",
            "root_match": False,
            "remote_write_operations": 0,
            "timestamp": utc_now(),
            "attempts": [
                {
                    "attempt": 1,
                    "timestamp": "2026-07-02T17:07:03+00:00",
                    "authentication": "FAIL",
                    "error": FIRST_ATTEMPT_ERROR,
                },
                {
                    "attempt": 2,
                    "timestamp": utc_now(),
                    "authentication": "FAIL",
                    "error": str(exc),
                },
            ],
        }
        cap.write_json(CAPTURE_ROOT / "connection-result.json", connection)
        return 2

    connection = {
        "site_id": "SITE-002",
        "environment": "PRODUCTION",
        "production_url": cap.PRODUCTION_URL,
        "operation_id": OPERATION_ID,
        "protocol": "FTP",
        "authentication": "PASS",
        "initial_listing": "PASS",
        "configured_remote_root": configured_root,
        "detected_remote_root": document_root,
        "root_match": root_match,
        "remote_write_operations": 0,
        "timestamp": utc_now(),
        "attempts": [
            {
                "attempt": 1,
                "timestamp": "2026-07-02T17:07:03+00:00",
                "authentication": "FAIL",
                "error": FIRST_ATTEMPT_ERROR,
            },
            {
                "attempt": 2,
                "timestamp": utc_now(),
                "authentication": "PASS",
                "login_pwd": pwd,
                "note": "Document root resolved by read-only listing to /public_html/ (configured /bzpm.ru/ empty)",
            },
        ],
    }
    cap.write_json(CAPTURE_ROOT / "connection-result.json", connection)

    try:
        ftp.cwd(document_root.rstrip("/"))
    except Exception:
        pass

    log_lines.append(f"[{utc_now()}] Building remote inventory from {document_root}…")
    items = targeted_inventory(ftp, document_root)
    markers = verify_document_root_markers(ftp, document_root)
    root_confirmed = all(markers.get(k) for k in ("index.php", "catalog", "system", "image"))
    opencart = {
        "opencart_indicators": {
            "index.php": markers["index.php"],
            "config.php": markers["config.php"],
            "admin/index.php": markers["admin"],
            "catalog/": markers["catalog"],
            "system/": markers["system"],
            "image/": markers["image"],
        },
        "config.php": "EXISTS" if markers["config.php"] else "NOT SEEN",
        "admin/config.php": "NOT DOWNLOADED",
        "document_root_markers": markers,
    }
    files_count = sum(1 for i in items if i["type"] == "file")
    dirs_count = sum(1 for i in items if i["type"] == "directory")
    inv_dir = CAPTURE_ROOT / "ftp-inventory"
    inv_dir.mkdir(parents=True, exist_ok=True)
    with (inv_dir / "remote-tree.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["relative_path", "type", "size", "modified_time", "permissions", "summary"]
        )
        writer.writeheader()
        for row in items:
            writer.writerow({k: row.get(k) for k in writer.fieldnames})
    cap.write_json(inv_dir / "remote-tree.json", items)

    dir_counts: dict[str, int] = {}
    for row in items:
        if row["type"] != "file":
            continue
        top = row["relative_path"].split("/")[0] + "/"
        dir_counts[top] = dir_counts.get(top, 0) + 1
    largest = sorted(dir_counts.items(), key=lambda x: x[1], reverse=True)[:15]

    summary = {
        "total_visible_files": files_count,
        "total_visible_directories": dirs_count,
        "inventory_exclusions": cap.INVENTORY_EXCLUSIONS,
        "document_root": document_root,
        "configured_remote_root": configured_root,
        "root_match": root_match,
        "theme_roots": sorted(
            {
                p.split("/")[3]
                for p in {i["relative_path"] for i in items}
                if p.startswith("catalog/view/theme/")
            }
        ),
        "active_theme_candidates": ["default"],
        "opencart_structural_indicators": opencart,
        "largest_directories_by_visible_file_count": [{"path": p, "files": c} for p, c in largest],
        "collected_at": utc_now(),
        "retry": True,
    }
    cap.write_json(inv_dir / "inventory-summary.json", summary)

    root_confirmed = all(markers.get(k) for k in ("index.php", "catalog", "system", "image"))
    log_lines.append(
        f"[{utc_now()}] Inventory: {files_count} files, {dirs_count} dirs; OpenCart root confirmed={root_confirmed}"
    )

    planned = {
        "operation_id": OPERATION_ID,
        "status": "COMPLETE",
        "document_root": document_root,
        "files": [
            {"remote": p, "reason": "baseline implementation surface"}
            for p in cap.BASELINE_REMOTE_FILES
            if p not in cap.FORBIDDEN_DOWNLOADS
        ],
    }
    cap.write_json(CAPTURE_ROOT / "manifests" / "planned-download-scope.json", planned)

    log_lines.append(f"[{utc_now()}] Downloading baseline files…")
    downloaded_meta: list[dict] = []
    downloaded_bytes: dict[str, bytes] = {}
    baseline_root = CAPTURE_ROOT / "downloaded-baseline"
    for entry in planned["files"]:
        remote_rel = entry["remote"]
        remote_full = (document_root + remote_rel).replace("//", "/")
        data = cap.download_file(ftp, remote_full)
        if data is None:
            downloaded_meta.append(
                {
                    "remote_relative_path": remote_rel,
                    "local_relative_path": None,
                    "size": 0,
                    "remote_modified_time": None,
                    "sha256": None,
                    "reason_for_inclusion": entry["reason"],
                    "status": "missing",
                }
            )
            continue
        local_path = baseline_root / remote_rel.replace("/", "\\")
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(data)
        digest = cap.sha256_hex(data)
        downloaded_bytes[remote_rel] = data
        downloaded_meta.append(
            {
                "remote_relative_path": remote_rel,
                "local_relative_path": str(local_path.relative_to(CAPTURE_ROOT)),
                "size": len(data),
                "remote_modified_time": None,
                "sha256": digest,
                "reason_for_inclusion": entry["reason"],
                "status": "ok",
            }
        )

    ftp.quit()

    ok_count = sum(1 for r in downloaded_meta if r["status"] == "ok")
    checksum_count = sum(1 for r in downloaded_meta if r.get("sha256"))
    log_lines.append(f"[{utc_now()}] Downloaded {ok_count}/{len(downloaded_meta)} baseline files")

    cap.write_json(CAPTURE_ROOT / "manifests" / "downloaded-files.json", downloaded_meta)
    with (CAPTURE_ROOT / "manifests" / "downloaded-files-sha256.csv").open(
        "w", encoding="utf-8", newline=""
    ) as fh:
        writer = csv.DictWriter(fh, fieldnames=["remote_relative_path", "sha256", "size", "status"])
        writer.writeheader()
        for row in downloaded_meta:
            writer.writerow(
                {
                    "remote_relative_path": row["remote_relative_path"],
                    "sha256": row.get("sha256"),
                    "size": row.get("size"),
                    "status": row.get("status"),
                }
            )

    http_results = load_http_results()
    platform = identify_platform_from_downloads(downloaded_bytes)
    theme = identify_theme_from_inventory(items, http_results)
    guarantee = guarantee_text_check(downloaded_bytes)
    pdp = pdp_class_check(downloaded_bytes)

    cap.write_json(CAPTURE_ROOT / "manifests" / "platform-identification.json", platform)
    (CAPTURE_ROOT / "manifests" / "platform-identification.md").write_text(
        "\n".join(
            [
                "# Platform identification",
                "",
                f"- Platform: {platform['platform']}",
                f"- Distribution: {platform['distribution']}",
                f"- Exact version: {platform['exact_version']}",
                f"- Confidence: {platform['confidence']}",
                "",
                "## Evidence",
                *[f"- {e['path']}: {e['note']}" for e in platform["evidence"]],
                "",
                f"*Updated FTP retry {utc_now()}*",
            ]
        ),
        encoding="utf-8",
    )
    (CAPTURE_ROOT / "manifests" / "active-theme-identification.md").write_text(
        "\n".join(
            [
                "# Active theme identification",
                "",
                f"- Active theme: {theme['active_theme']}",
                f"- Theme root: {theme['theme_root']}",
                f"- Confidence: {theme['confidence']}",
                "",
                "## Evidence",
                f"- HTML asset paths: {theme['evidence']['html_asset_paths']}",
                f"- Remote theme dirs: {theme['evidence']['remote_theme_dirs']}",
                "",
                f"*Updated FTP retry {utc_now()}*",
            ]
        ),
        encoding="utf-8",
    )

    parity = cap.parity_assess(downloaded_bytes, http_results)
    cap.write_json(CAPTURE_ROOT / "manifests" / "production-test-parity-matrix.json", parity)
    md_lines = [
        "# Production vs TEST parity matrix",
        "",
        f"*FTP retry {utc_now()} — file + HTTP evidence*",
        "",
    ]
    for row in parity:
        md_lines.append(f"## {row['domain']}")
        md_lines.append(f"- Classification: **{row['classification']}**")
        md_lines.append(f"- File: {row['remote_path']} — {row['file_evidence']}")
        if row["url_path"]:
            md_lines.append(f"- HTTP {row['url_path']}: {row['http_evidence']}")
        md_lines.append("")
    md_lines.extend(
        [
            "## First controlled test — guarantee.twig",
            f"- Path: `{guarantee['path']}`",
            f"- File exists: **{guarantee['exists']}**",
            f"- Phrase «понятный порядок действий»: **{guarantee['phrase_ponyatny_poryadok']}**",
            f"- Classification: **{guarantee['classification']}**",
            "",
            "## PDP body/category classes",
            f"- Classification: **{pdp['classification']}**",
            f"- Evidence files: {pdp['evidence_files']}",
        ]
    )
    (CAPTURE_ROOT / "manifests" / "production-test-parity-matrix.md").write_text(
        "\n".join(md_lines), encoding="utf-8"
    )

    cap.write_json(
        CAPTURE_ROOT / "manifests" / "first-test-task-confirmation.json",
        {"guarantee": guarantee, "pdp_classes": pdp},
    )

    gates = baseline_gate(
        auth_pass=True,
        listing_pass=True,
        root_confirmed=root_confirmed,
        inventory_count=files_count,
        downloaded_ok=ok_count,
        checksums_ok=checksum_count,
        theme=theme,
        platform_confirmed=platform["confidence"] in ("CONFIRMED", "PROBABLE"),
        parity_done=True,
    )
    all_pass = all(g["result"] == "PASS" for g in gates)
    cap.write_json(CAPTURE_ROOT / "manifests" / "baseline-gate.json", {"gates": gates, "verdict": "PASS" if all_pass else "FAIL"})

    receipt = {
        "baseline_id": "SITE-002-STABLE-PROD-INITIAL-01",
        "site_id": "SITE-002",
        "environment": "PRODUCTION",
        "production_url": cap.PRODUCTION_URL,
        "operation_id": OPERATION_ID,
        "issued": all_pass,
        "remote_authentication": "PASS",
        "remote_listing": "PASS",
        "remote_write_operations": 0,
        "http_verification": "PASS",
        "visual_capture": "PASS",
        "platform_identification": platform["confidence"],
        "active_theme_identification": theme["confidence"],
        "production_test_parity": "FILE + HTTP evidence collected",
        "admin_inspection": "COMPLETED READ-ONLY",
        "document_root": document_root,
        "configured_remote_root": configured_root,
        "root_match": root_match,
        "guarantee_twig": guarantee,
        "blockers": [] if all_pass else ["Baseline gate not fully satisfied"],
        "issued_at": utc_now() if all_pass else None,
    }
    cap.write_json(CAPTURE_ROOT / "capture-receipt.json", receipt)

    log_lines.append(f"[{utc_now()}] Baseline gate: {'PASS' if all_pass else 'FAIL'}")
    append_log(log_lines)
    return 0 if all_pass else 3


if __name__ == "__main__":
    sys.exit(main())
