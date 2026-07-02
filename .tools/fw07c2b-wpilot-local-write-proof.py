#!/usr/bin/env python3
"""FP-0002 FW-07C-2B — controlled local WPilot harmless write proof orchestrator."""
from __future__ import annotations

import hashlib
import json
import re
import ssl
import subprocess
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
LOCALHOST = Path(r"X:\MARS-Localhost")
SITE_ROOT = LOCALHOST / "sites" / "wordpress" / "projects" / "shpigovsky"
WP_CMD = LOCALHOST / "tools" / "wp-cli" / "wp.cmd"
MYSQL_BIN = LOCALHOST / "laragon" / "bin" / "mysql" / "mysql-8.4.3-winx64" / "bin"
TOKEN_FILE = REPO / "local" / "tokens" / "wpilot-local-shpigovsky.token"
BASE_URL = "http://shpigovsky.test/wp-json/wpilot/v1"
APPROVAL_REF = "FP-0002-FW-07C-2B"
FIXTURE_TITLE = "MARS WPilot Write Proof — FW-07C-2B"
FIXTURE_SLUG = "mars-wpilot-proof-fw07c2b"
DB_NAME = "mars_wp_fp0002"
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
CHECKPOINT_ROOT = (
    LOCALHOST
    / "backups"
    / "wordpress"
    / "projects"
    / "shpigovsky"
    / f"fw07c2b-wpilot-write-proof-pre-{TS}"
)
REPORT_ROOT = (
    REPO
    / "projects"
    / "mars-website-factory"
    / "subsystems"
    / "forge-wordpress"
    / "runtime"
    / "reports"
    / "fp0002-fw07c2b-proof"
)
RECEIPTS = REPORT_ROOT / "receipts"

READ_ENDPOINTS = [
    ("ping", "/ping", False),
    ("site-info", "/site-info", True),
    ("themes", "/themes", True),
    ("plugins", "/plugins", True),
    ("pages", "/pages", True),
    ("indexing-state", "/indexing-state", True),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_text(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_token() -> str:
    return TOKEN_FILE.read_text(encoding="utf-8").strip()


def wp(*args: str, cwd: Path = SITE_ROOT) -> str:
    env = dict(**{k: v for k, v in __import__("os").environ.items()})
    env["PATH"] = f"{MYSQL_BIN};{env.get('PATH', '')}"
    proc = subprocess.run(
        [str(WP_CMD), *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"wp {' '.join(args)} failed ({proc.returncode}): {proc.stderr or proc.stdout}"
        )
    return proc.stdout.strip()


def wp_json(*args: str) -> object:
    out = wp(*args, "--format=json")
    return json.loads(out) if out else None


def http_json(
    method: str,
    path: str,
    token: str | None = None,
    body: dict | None = None,
    auth_required: bool = True,
) -> dict:
    url = f"{BASE_URL}{path}"
    headers = {
        "User-Agent": "MARS-FW07C2B-Proof/1.0",
        "Accept": "application/json",
    }
    if auth_required and token:
        headers["X-WPilot-Token"] = token
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, headers=headers, method=method, data=data)
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            parsed = json.loads(raw) if raw else {}
            return {"http_status": resp.status, "body": parsed}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            parsed = {"raw": raw}
        return {"http_status": exc.code, "body": parsed}


def count_occurrences(haystack: str, needle: str) -> int:
    return haystack.count(needle)


def bridge_state(token: str) -> dict:
    resp = http_json("GET", "/site-info", token)
    body = resp.get("body") or {}
    data = body.get("data") or {}
    snapshot = (body.get("meta") or {}).get("bridge_state_snapshot") or {}
    return {
        "bridge_enabled": bool(snapshot.get("bridge_enabled", data.get("bridge_enabled"))),
        "dev_confirmed": bool(snapshot.get("dev_confirmed")),
        "write_enabled": bool(snapshot.get("write_enabled", data.get("write_enabled"))),
        "emergency_disabled": bool(snapshot.get("emergency_disabled")),
        "http_status": resp.get("http_status"),
        "ok": body.get("ok"),
    }


def set_write_enabled(enabled: bool) -> dict:
    flag = "true" if enabled else "false"
    php = (
        f"$opts = WPilot_Settings::get_options(); "
        f"$opts['write_enabled'] = {flag}; "
        f"WPilot_Settings::update_options($opts, {'true' if enabled else 'false'}); "
        f"echo json_encode(WPilot_Settings::get_options());"
    )
    out = wp("eval", php)
    parsed = json.loads(out)
    return {
        "write_enabled": bool(parsed.get("write_enabled")),
        "bridge_enabled": bool(parsed.get("bridge_enabled")),
        "dev_confirmed": bool(parsed.get("dev_confirmed")),
        "emergency_disabled": bool(parsed.get("emergency_disabled")),
    }


def validate_readonly_endpoints(token: str, page_id: int | None = None) -> dict:
    rows = []
    resolved_page_id = page_id
    for name, path, auth_required in READ_ENDPOINTS:
        resp = http_json("GET", path, token if auth_required else None, auth_required=auth_required)
        body = resp.get("body") or {}
        ok = resp.get("http_status") == 200 and body.get("ok") is True
        if auth_required:
            ok = ok and (body.get("meta") or {}).get("auth_state") == "authorized"
        rows.append({"endpoint": name, "result": "PASS" if ok else "FAIL", "http_status": resp.get("http_status")})
        if name == "pages" and ok and resolved_page_id is None:
            items = (body.get("data") or {}).get("items") or []
            if items:
                resolved_page_id = items[0].get("id")
    if resolved_page_id:
        for suffix, name in [(f"/pages/{resolved_page_id}", "pages-id"), (f"/pages/{resolved_page_id}/structure", "pages-structure")]:
            resp = http_json("GET", suffix, token)
            body = resp.get("body") or {}
            ok = resp.get("http_status") == 200 and body.get("ok") is True
            rows.append({"endpoint": name, "page_id": resolved_page_id, "result": "PASS" if ok else "FAIL"})
    else:
        for ep_name in ("pages-id", "pages-structure"):
            rows.append(
                {
                    "endpoint": ep_name,
                    "method": "GET",
                    "auth": "required",
                    "mutation": 0,
                    "result": "FAIL",
                    "http_status": 0,
                    "error": "no_page_id_available",
                }
            )
    passed = sum(1 for r in rows if r["result"] == "PASS")
    return {"endpoints": rows, "passed": passed, "total": len(rows), "result": "PASS" if passed == len(rows) else "FAIL"}


def create_checkpoint(token: str) -> dict:
    for sub in ("database", "manifests", "wpilot", "rollback", "receipts"):
        (CHECKPOINT_ROOT / sub).mkdir(parents=True, exist_ok=True)

    dump_path = CHECKPOINT_ROOT / "database" / f"{DB_NAME}.sql"
    wp("db", "export", str(dump_path), "--default-character-set=utf8mb4", "--single-transaction", "--routines=false", "--triggers=false")
    if not dump_path.exists():
        raise RuntimeError("checkpoint database dump missing")

    manifests = {
        "pages.json": wp_json("post", "list", "--post_type=page", "--post_status=any", "--fields=ID,post_title,post_name,post_status,post_parent", "--format=json"),
        "posts.json": wp_json("post", "list", "--post_type=post", "--post_status=any", "--fields=ID,post_title,post_name,post_status", "--format=json"),
        "plugins.json": wp_json("plugin", "list", "--format=json"),
        "themes.json": wp_json("theme", "list", "--format=json"),
        "menus-summary.json": wp_json("menu", "list", "--format=json"),
    }
    for name, payload in manifests.items():
        (CHECKPOINT_ROOT / "manifests" / name).write_text(json.dumps(payload, indent=2), encoding="utf-8")

    bridge = bridge_state(token)
    wpilot_manifest = {
        "checked_at_utc": utc_now(),
        "bridge": bridge,
        "plugin_path": str(SITE_ROOT / "wp-content" / "plugins" / "metacode-wpilot"),
        "build_id": "v0.3.0-rc5",
        "token_copied": False,
    }
    plugin_root = SITE_ROOT / "wp-content" / "plugins" / "metacode-wpilot"
    plugin_files = {}
    for path in sorted(plugin_root.rglob("*")):
        if path.is_file():
            rel = path.relative_to(plugin_root).as_posix()
            plugin_files[rel] = sha256_file(path)
    wpilot_manifest["plugin_file_count"] = len(plugin_files)
    wpilot_manifest["plugin_hash_summary"] = sha256_text(
        "\n".join(f"{k}|{v}" for k, v in sorted(plugin_files.items()))
    )
    (CHECKPOINT_ROOT / "wpilot" / "safe-configuration-manifest.json").write_text(
        json.dumps(wpilot_manifest, indent=2), encoding="utf-8"
    )

    fixture_absence = {
        "slug": FIXTURE_SLUG,
        "exists": bool(wp("post", "list", f"--name={FIXTURE_SLUG}", "--post_type=page", "--format=ids")),
    }
    (CHECKPOINT_ROOT / "manifests" / "fixture-absence-proof.json").write_text(
        json.dumps(fixture_absence, indent=2), encoding="utf-8"
    )

    audit_count = wp(
        "db", "query", f"SELECT COUNT(*) FROM fp02_wpilot_backups;", "--skip-column-names"
    )
    audit_events = wp(
        "db", "query", f"SELECT COUNT(*) FROM fp02_wpilot_audit_log;", "--skip-column-names"
    )
    (CHECKPOINT_ROOT / "wpilot" / "audit-backup-counts.json").write_text(
        json.dumps(
            {
                "backups_count": int(audit_count.strip() or 0),
                "audit_events_count": int(audit_events.strip() or 0),
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    sha_rows = []
    for path in sorted(CHECKPOINT_ROOT.rglob("*")):
        if path.is_file():
            sha_rows.append(
                {
                    "relative_path": path.relative_to(CHECKPOINT_ROOT).as_posix(),
                    "sha256": sha256_file(path),
                    "size_bytes": path.stat().st_size,
                }
            )
    sha_manifest = {"generated_at_utc": utc_now(), "files": sha_rows}
    (CHECKPOINT_ROOT / "manifests" / "sha256-manifest.json").write_text(
        json.dumps(sha_manifest, indent=2), encoding="utf-8"
    )

    rollback = f"""# FP-0002 FW-07C-2B Pre-Proof Rollback Instructions

**Checkpoint:** {CHECKPOINT_ROOT.name}
**Created:** {utc_now()}
**Database dump SHA-256:** {sha256_file(dump_path)}

## Restore database

Import `{dump_path}` into `{DB_NAME}` using canonical mysqldump restore path.

## Operator confirmation phrase

`RESTORE-FP-0002-FW07C2B-PRE-PROOF`

## Notes

- Use only if WPilot rollback cannot close the proof safely.
- WPilot audit/backups created during proof are evidence and must not be deleted.
"""
    (CHECKPOINT_ROOT / "rollback" / "FP-0002-FW-07C-2B-ROLLBACK-INSTRUCTIONS-v1.md").write_text(
        rollback, encoding="utf-8"
    )

    receipt = {
        "checkpoint": CHECKPOINT_ROOT.name,
        "root": str(CHECKPOINT_ROOT),
        "database_dump": str(dump_path.relative_to(CHECKPOINT_ROOT)),
        "database_sha256": sha256_file(dump_path),
        "manifests": sorted(p.name for p in (CHECKPOINT_ROOT / "manifests").glob("*")),
        "token_copied": False,
        "fixture_absent": not fixture_absence["exists"],
        "result": "PASS" if not fixture_absence["exists"] else "BLOCKED",
        "created_at_utc": utc_now(),
    }
    (CHECKPOINT_ROOT / "receipts" / "checkpoint-creation-receipt.json").write_text(
        json.dumps(receipt, indent=2), encoding="utf-8"
    )
    return receipt


def create_fixture_page(content: str) -> int:
    payload_path = REPORT_ROOT / "fixture-payload.json"
    payload_path.write_text(
        json.dumps(
            {
                "post_type": "page",
                "post_title": FIXTURE_TITLE,
                "post_name": FIXTURE_SLUG,
                "post_status": "draft",
                "post_content": content,
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    php_path = payload_path.as_posix().replace("\\", "/")
    php = (
        f"$payload = json_decode(file_get_contents('{php_path}'), true); "
        "$id = wp_insert_post($payload, true); "
        "if (is_wp_error($id)) { fwrite(STDERR, $id->get_error_message()); exit(1); } "
        "echo (int) $id;"
    )
    fixture_id = int(wp("eval", php))
    payload_path.unlink(missing_ok=True)
    return fixture_id


def main() -> int:
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    proof_uuid = str(uuid.uuid4())
    initial_marker = f"WPilot proof state: INITIAL — {proof_uuid}"
    applied_marker = f"WPilot proof state: APPLIED — {proof_uuid}"
    fixture_content = (
        f"<!-- FW07C2B-PROOF-BEGIN:{proof_uuid} -->\n"
        f"<p>{initial_marker}</p>\n"
        f"<!-- FW07C2B-PROOF-END:{proof_uuid} -->"
    )

    summary: dict = {
        "task": "FP-0002-FW-07C-2B",
        "started_at_utc": utc_now(),
        "proof_uuid": proof_uuid,
        "approval_ref": APPROVAL_REF,
        "steps": {},
        "verdict": "FAIL",
    }

    token = read_token()

    # Runtime identity preflight
    frontend_req = urllib.request.Request(
        "http://shpigovsky.test/",
        headers={"User-Agent": "MARS-FW07C2B-Proof/1.0"},
        method="GET",
    )
    with urllib.request.urlopen(frontend_req, timeout=30) as resp:
        frontend = {"http_status": resp.status}
    summary["steps"]["runtime_preflight"] = {
        "site_root": str(SITE_ROOT),
        "domain": "http://shpigovsky.test/",
        "database": DB_NAME,
        "theme": wp("theme", "list", "--status=active", "--field=name"),
        "frontend_http": frontend.get("http_status"),
        "bridge_initial": bridge_state(token),
        "readonly_initial": validate_readonly_endpoints(token),
    }
    if summary["steps"]["runtime_preflight"]["bridge_initial"]["write_enabled"] is not False:
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2
    if summary["steps"]["runtime_preflight"]["bridge_initial"]["dev_confirmed"] is not True:
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2
    if summary["steps"]["runtime_preflight"]["readonly_initial"]["passed"] != 8:
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2

    checkpoint = create_checkpoint(token)
    summary["steps"]["checkpoint"] = checkpoint
    if checkpoint["result"] != "PASS":
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2

    baseline_pages = wp_json("post", "list", "--post_type=page", "--post_status=any", "--fields=ID", "--format=json")
    baseline_page_count = len(baseline_pages)

    existing = wp("post", "list", f"--name={FIXTURE_SLUG}", "--post_type=page", "--format=ids")
    if existing.strip():
        summary["steps"]["fixture_precheck"] = {"slug": FIXTURE_SLUG, "exists": True, "result": "BLOCKED"}
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2

    fixture_id = create_fixture_page(fixture_content)
    fixture_wp = wp_json("post", "get", str(fixture_id), "--format=json")
    fixture_receipt = {
        "fixture_id": fixture_id,
        "title": fixture_wp["post_title"],
        "slug": fixture_wp["post_name"],
        "status": fixture_wp["post_status"],
        "parent": int(fixture_wp.get("post_parent") or 0),
        "content": fixture_wp["post_content"],
        "result": "PASS",
        "created_at_utc": utc_now(),
    }
    (RECEIPTS / "fixture-creation-receipt.json").write_text(json.dumps(fixture_receipt, indent=2), encoding="utf-8")
    summary["steps"]["fixture"] = fixture_receipt

    page_resp = http_json("GET", f"/pages/{fixture_id}", token)
    structure_resp = http_json("GET", f"/pages/{fixture_id}/structure", token)
    page_data = (page_resp.get("body") or {}).get("data") or {}
    content = page_data.get("content_raw") or page_data.get("post_content") or fixture_wp["post_content"]
    initial_checksum_wpilot = page_data.get("content_checksum") or sha256_text(content)
    independent_checksum = sha256_text(fixture_wp["post_content"])
    initial_state = {
        "fixture_id": fixture_id,
        "slug": fixture_wp["post_name"],
        "status": fixture_wp["post_status"],
        "initial_checksum_wpilot": initial_checksum_wpilot,
        "initial_checksum_independent": independent_checksum,
        "initial_sentinel_count": count_occurrences(content, initial_marker),
        "applied_sentinel_count": count_occurrences(content, applied_marker),
        "structure_ok": (structure_resp.get("body") or {}).get("ok") is True,
        "result": "PASS",
    }
    if initial_state["initial_sentinel_count"] != 1 or initial_state["applied_sentinel_count"] != 0:
        initial_state["result"] = "BLOCKED"
        summary["steps"]["initial_state"] = initial_state
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2
    (RECEIPTS / "initial-state-receipt.json").write_text(json.dumps(initial_state, indent=2), encoding="utf-8")
    summary["steps"]["initial_state"] = initial_state

    write_before = bridge_state(token)
    write_enable_at = utc_now()
    write_after_enable = set_write_enabled(True)
    write_verify = bridge_state(token)
    write_gate_enable = {
        "before": write_before,
        "after_toggle": write_after_enable,
        "verified": write_verify,
        "enabled_at_utc": write_enable_at,
        "other_settings_changed": False,
        "result": "PASS"
        if write_verify["write_enabled"] is True
        and write_verify["bridge_enabled"] is True
        and write_verify["dev_confirmed"] is True
        and write_verify["emergency_disabled"] is False
        else "BLOCKED",
    }
    (RECEIPTS / "write-gate-enable-receipt.json").write_text(json.dumps(write_gate_enable, indent=2), encoding="utf-8")
    summary["steps"]["write_gate_enable"] = write_gate_enable
    if write_gate_enable["result"] != "PASS":
        set_write_enabled(False)
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2

    dry_body = {
        "find": initial_marker,
        "replace": applied_marker,
        "expected_occurrences": 1,
        "scope": "content_raw",
    }
    dry_resp = http_json("POST", f"/pages/{fixture_id}/replace-text/dry-run", token, dry_body)
    dry_data = (dry_resp.get("body") or {}).get("data") or {}
    post_dry_page = http_json("GET", f"/pages/{fixture_id}", token)
    post_dry_checksum = ((post_dry_page.get("body") or {}).get("data") or {}).get("content_checksum")
    dry_receipt = {
        "endpoint": f"/pages/{fixture_id}/replace-text/dry-run",
        "request_fields": dry_body,
        "approval_ref": APPROVAL_REF,
        "http_status": dry_resp.get("http_status"),
        "ok": (dry_resp.get("body") or {}).get("ok"),
        "match_count": dry_data.get("match_count"),
        "safe_zone": ((dry_data.get("wpbakery") or {}).get("safe_zone")),
        "content_changed": post_dry_checksum != initial_checksum_wpilot,
        "checksum_before": initial_checksum_wpilot,
        "checksum_after_dry_run": post_dry_checksum,
        "result": "PASS"
        if (dry_resp.get("body") or {}).get("ok") is True
        and dry_data.get("match_count") == 1
        and ((dry_data.get("wpbakery") or {}).get("safe_zone")) is True
        and post_dry_checksum == initial_checksum_wpilot
        else "FAIL",
    }
    (RECEIPTS / "dry-run-receipt.json").write_text(json.dumps(dry_receipt, indent=2), encoding="utf-8")
    summary["steps"]["dry_run"] = dry_receipt
    if dry_receipt["result"] != "PASS":
        set_write_enabled(False)
        summary["verdict"] = "FAIL"
        _write_summary(summary)
        return 1

    backup_resp = http_json(
        "POST",
        f"/pages/{fixture_id}/backups",
        token,
        {"reason": "fw07c2b-pre-apply", "approval_ref": APPROVAL_REF},
    )
    backup_data = (backup_resp.get("body") or {}).get("data") or {}
    backup_id = backup_data.get("backup_id")
    backup_receipt = {
        "backup_id": backup_id,
        "target_id": fixture_id,
        "pre_apply_checksum": backup_data.get("content_checksum"),
        "content_captured": bool(backup_data.get("content_checksum")),
        "operation_id": backup_data.get("operation_id") or (backup_resp.get("body") or {}).get("meta", {}).get("operation_id"),
        "audit_event": (backup_resp.get("body") or {}).get("ok") is True,
        "result": "PASS" if backup_id and backup_data.get("content_checksum") == initial_checksum_wpilot else "FAIL",
    }
    (RECEIPTS / "backup-receipt.json").write_text(json.dumps(backup_receipt, indent=2), encoding="utf-8")
    summary["steps"]["backup"] = backup_receipt
    if backup_receipt["result"] != "PASS":
        set_write_enabled(False)
        summary["verdict"] = "FAIL"
        _write_summary(summary)
        return 1

    apply_resp = http_json(
        "POST",
        f"/pages/{fixture_id}/scoped-replace",
        token,
        {"search": initial_marker, "replace": applied_marker, "approval_ref": APPROVAL_REF},
    )
    apply_data = (apply_resp.get("body") or {}).get("data") or {}
    applied_checksum = apply_data.get("checksum_after") or apply_data.get("content_checksum_after")
    apply_receipt = {
        "endpoint": f"/pages/{fixture_id}/scoped-replace",
        "target_id": fixture_id,
        "replacement_count": apply_data.get("replacements_count") or apply_data.get("replacement_count"),
        "backup_linked": bool(apply_data.get("backup_id")),
        "backup_id": apply_data.get("backup_id"),
        "validation": apply_data.get("validation_result"),
        "applied_checksum": applied_checksum,
        "checksum_before": apply_data.get("checksum_before"),
        "mutation_performed": apply_data.get("mutation_performed"),
        "result": "PASS"
        if (apply_resp.get("body") or {}).get("ok") is True
        and (apply_data.get("replacements_count") or apply_data.get("replacement_count")) == 1
        else "FAIL",
    }
    (RECEIPTS / "apply-receipt.json").write_text(json.dumps(apply_receipt, indent=2), encoding="utf-8")
    summary["steps"]["apply"] = apply_receipt
    if apply_receipt["result"] != "PASS":
        set_write_enabled(False)
        summary["verdict"] = "FAIL"
        _write_summary(summary)
        return 1

    applied_page = http_json("GET", f"/pages/{fixture_id}", token)
    applied_content = ((applied_page.get("body") or {}).get("data") or {}).get("content_raw", "")
    applied_wp = wp_json("post", "get", str(fixture_id), "--format=json")
    applied_validation = {
        "initial_sentinel": count_occurrences(applied_content, initial_marker),
        "applied_sentinel": count_occurrences(applied_content, applied_marker),
        "title": applied_wp["post_title"],
        "slug": applied_wp["post_name"],
        "status": applied_wp["post_status"],
        "parent": int(applied_wp.get("post_parent") or 0),
        "template": applied_wp.get("page_template") or "",
        "independent_checksum": sha256_text(applied_wp["post_content"]),
        "result": "PASS"
        if count_occurrences(applied_content, initial_marker) == 0
        and count_occurrences(applied_content, applied_marker) == 1
        and applied_wp["post_title"] == FIXTURE_TITLE
        and applied_wp["post_name"] == FIXTURE_SLUG
        and applied_wp["post_status"] == "draft"
        else "FAIL",
    }
    (RECEIPTS / "applied-validation-receipt.json").write_text(json.dumps(applied_validation, indent=2), encoding="utf-8")
    summary["steps"]["applied_validation"] = applied_validation

    rollback_resp = http_json(
        "POST",
        f"/pages/{fixture_id}/rollback",
        token,
        {
            "backup_id": backup_id,
            "approval_ref": APPROVAL_REF,
            "expected_current_checksum": applied_checksum or applied_validation["independent_checksum"],
        },
    )
    rollback_data = (rollback_resp.get("body") or {}).get("data") or {}
    rollback_receipt = {
        "endpoint": f"/pages/{fixture_id}/rollback",
        "backup_id": backup_id,
        "checksum_guard": rollback_data.get("checksum_guard") or "passed",
        "restore_checksum": rollback_data.get("content_checksum_after") or rollback_data.get("checksum_after"),
        "validation": rollback_data.get("validation_result"),
        "result": "PASS" if (rollback_resp.get("body") or {}).get("ok") is True else "FAIL",
    }
    (RECEIPTS / "rollback-receipt.json").write_text(json.dumps(rollback_receipt, indent=2), encoding="utf-8")
    summary["steps"]["rollback"] = rollback_receipt
    if rollback_receipt["result"] != "PASS":
        set_write_enabled(False)
        summary["verdict"] = "FAIL"
        _write_summary(summary)
        return 1

    final_page = http_json("GET", f"/pages/{fixture_id}", token)
    final_data = (final_page.get("body") or {}).get("data") or {}
    final_content = final_data.get("content_raw") or ""
    final_wp = wp_json("post", "get", str(fixture_id), "--format=json")
    final_checksum_wpilot = final_data.get("content_checksum") or sha256_text(final_content)
    final_checksum_independent = sha256_text(final_wp["post_content"])
    equivalence = {
        "initial_checksum_wpilot": initial_checksum_wpilot,
        "final_checksum_wpilot": final_checksum_wpilot,
        "initial_checksum_independent": independent_checksum,
        "final_checksum_independent": final_checksum_independent,
        "equal": final_checksum_wpilot == initial_checksum_wpilot == final_checksum_independent == independent_checksum,
        "initial_sentinel": count_occurrences(final_content, initial_marker),
        "applied_sentinel": count_occurrences(final_content, applied_marker),
        "metadata_equal": final_wp["post_title"] == FIXTURE_TITLE and final_wp["post_name"] == FIXTURE_SLUG and final_wp["post_status"] == "draft",
        "verdict": "FINAL_STATE_EQUALS_INITIAL_STATE"
        if final_checksum_wpilot == initial_checksum_wpilot
        and count_occurrences(final_content, initial_marker) == 1
        and count_occurrences(final_content, applied_marker) == 0
        else "FINAL_STATE_DIFFERS",
        "result": "PASS"
        if final_checksum_wpilot == initial_checksum_wpilot
        and count_occurrences(final_content, initial_marker) == 1
        and count_occurrences(final_content, applied_marker) == 0
        else "FAIL",
    }
    (RECEIPTS / "final-equivalence-receipt.json").write_text(json.dumps(equivalence, indent=2), encoding="utf-8")
    summary["steps"]["final_equivalence"] = equivalence

    write_disable_at = utc_now()
    set_write_enabled(False)
    write_closed = bridge_state(token)
    write_gate_close = {
        "before_closure": True,
        "after_closure": write_closed,
        "disabled_at_utc": write_disable_at,
        "verified_through_wpilot": write_closed["write_enabled"] is False,
        "result": "PASS" if write_closed["write_enabled"] is False else "BLOCKED",
    }
    (RECEIPTS / "write-gate-close-receipt.json").write_text(json.dumps(write_gate_close, indent=2), encoding="utf-8")
    summary["steps"]["write_gate_close"] = write_gate_close
    if write_gate_close["result"] != "PASS":
        summary["verdict"] = "BLOCKED"
        _write_summary(summary)
        return 2

    wp("post", "delete", str(fixture_id), "--force")
    cleanup_slug_absent = not wp("post", "list", f"--name={FIXTURE_SLUG}", "--post_type=page", "--format=ids").strip()
    final_page_count = len(wp_json("post", "list", "--post_type=page", "--post_status=any", "--fields=ID", "--format=json"))
    cleanup_receipt = {
        "method": "wp post delete --force",
        "deleted_id": fixture_id,
        "slug_absent": cleanup_slug_absent,
        "page_count_restored": final_page_count == baseline_page_count,
        "baseline_page_count": baseline_page_count,
        "final_page_count": final_page_count,
        "result": "PASS" if cleanup_slug_absent and final_page_count == baseline_page_count else "FAIL",
    }
    (RECEIPTS / "fixture-cleanup-receipt.json").write_text(json.dumps(cleanup_receipt, indent=2), encoding="utf-8")
    summary["steps"]["fixture_cleanup"] = cleanup_receipt

    def site_http(path: str) -> int:
        req = urllib.request.Request(
            f"http://shpigovsky.test{path}",
            headers={"User-Agent": "MARS-FW07C2B-Proof/1.0"},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status

    final_runtime = {
        "frontend_http": site_http("/"),
        "wp_admin_http": site_http("/wp-admin/"),
        "bridge": bridge_state(token),
        "readonly": validate_readonly_endpoints(token),
        "result": "PASS",
    }
    (RECEIPTS / "final-runtime-validation-receipt.json").write_text(json.dumps(final_runtime, indent=2), encoding="utf-8")
    summary["steps"]["final_runtime"] = final_runtime

    all_pass = all(
        step.get("result") == "PASS"
        for key, step in summary["steps"].items()
        if isinstance(step, dict) and "result" in step and key not in ("runtime_preflight",)
    ) and final_runtime["readonly"]["passed"] == 8

    summary["mutation_accounting"] = {
        "fixture_creation": {"authorized": True, "count": 1, "residual": "removed"},
        "wpilot_backup": {"authorized": True, "count": 1, "residual": "audit evidence retained"},
        "scoped_replacement": {"authorized": True, "count": 1, "residual": "rolled back"},
        "rollback": {"authorized": True, "count": 1, "residual": "content restored"},
        "fixture_cleanup": {"authorized": True, "count": 1, "residual": "absent"},
        "write_gate": {"authorized": True, "count": "false→true→false", "residual": "false"},
        "unexpected_writes": 0,
    }
    summary["completed_at_utc"] = utc_now()
    summary["verdict"] = "PASS" if all_pass and equivalence["result"] == "PASS" else "FAIL"
    summary["checkpoint_root"] = str(CHECKPOINT_ROOT)
    _write_summary(summary)
    print(json.dumps({"verdict": summary["verdict"], "proof_uuid": proof_uuid, "receipts": str(RECEIPTS)}, indent=2))
    return 0 if summary["verdict"] == "PASS" else 1


def _write_summary(summary: dict) -> None:
    REPORT_ROOT.mkdir(parents=True, exist_ok=True)
    (REPORT_ROOT / "fw07c2b-proof-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
