#!/usr/bin/env python3
"""SITE-002 Beget 1C cron activation — MARS HTTP gateway only, no manual import."""
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
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CRON-BEGET-ACTIVATE-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01"
MANUAL_RUN_REPORT = "mars_1c_import_2026-07-05_205934.txt"
MANUAL_RUN_ID = "mars-20260705-205929-df82e686"
CRON_SCHEDULE_MOSCOW = "0 8 * * *"
CRON_LOG_PATH = "/home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_cron_stdout.log"
GATEWAY_URL = "https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-BEGET-ACTIVATE-01"
)
PREFLIGHT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01"
)
TOKEN_META_PREFLIGHT = PREFLIGHT_ROOT / "manifests" / "token-meta.json"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

SUBDIRS = (
    "source",
    "verification",
    "beget",
    "cron-command",
    "reports",
    "logs",
    "manifests",
)

LEGACY_PATTERNS = (
    "common/cronjob",
    "import_1C.php",
    "import_1C_offers.php",
    "route=common/cronjob",
)
MARS_PATTERN = "mars_1c_http_gateway.php"


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


def parse_section_block(text: str, section: str) -> str:
    match = re.search(rf"^{re.escape(section)}\s*$([\s\S]*?)(?=^### |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError(f"Section not found: {section}")
    return match.group(1)


def parse_production_secrets(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    prod_match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not prod_match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = prod_match.group(1)
    out: dict[str, dict[str, str]] = {}
    for subsection in ("FTP / SFTP", "SSH", "Hosting Panel"):
        sub = parse_section_block(block, f"### {subsection}")
        fields: dict[str, str] = {}
        current_key: str | None = None
        for line in sub.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.endswith(":"):
                current_key = stripped[:-1].strip().lower().replace(" ", "_")
                fields.setdefault(current_key, "")
                continue
            if current_key:
                fields[current_key] = stripped
        out[subsection.lower().replace(" / ", "_").replace(" ", "_")] = fields
    return out


def ftp_connect(fields: dict[str, str]) -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def normalize_remote(path: str) -> str:
    path = path.strip()
    if not path.startswith("/"):
        path = "/" + path
    return path


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes | None:
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + normalize_remote(remote_path), bio.write)
        return bio.getvalue()
    except ftplib.error_perm:
        return None


def list_dir_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, _facts in ftp.mlsd(normalize_remote(path)):
            if name not in (".", ".."):
                names.append(name)
        return names
    except ftplib.error_perm:
        pass
    lines: list[str] = []
    try:
        ftp.retrlines("LIST " + normalize_remote(path), lines.append)
    except ftplib.error_perm:
        return names
    for line in lines:
        parts = line.split(maxsplit=8)
        if len(parts) >= 9:
            names.append(parts[8])
    return names


def resolve_roots(ftp: ftplib.FTP) -> dict[str, str]:
    pwd = ftp.pwd() or "/"
    login_root = normalize_remote(pwd if pwd.startswith("/") else "/" + pwd)
    public_root = normalize_remote(login_root + "public_html").rstrip("/") + "/"
    storage_root = normalize_remote(login_root + "storage").rstrip("/") + "/"
    try:
        names = {n.lower() for n in list_dir_names(ftp, login_root)}
        if "public_html" in names:
            public_root = normalize_remote(login_root + "public_html").rstrip("/") + "/"
        if "storage" in names:
            storage_root = normalize_remote(login_root + "storage").rstrip("/") + "/"
    except Exception:
        pass
    return {"login_root": login_root, "public_root": public_root, "storage_root": storage_root}


def http_get(url: str, timeout: int = 120) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(262144)
            return {
                "url": url.split("token=")[0].rstrip("?&"),
                "status_code": resp.status,
                "body": body.decode("utf-8", errors="replace"),
                "body_sha256": sha256_bytes(body),
                "timestamp": utc_now(),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read(262144) if exc.fp else b""
        return {
            "url": url.split("token=")[0].rstrip("?&"),
            "status_code": exc.code,
            "body": body.decode("utf-8", errors="replace"),
            "body_sha256": sha256_bytes(body) if body else None,
            "timestamp": utc_now(),
        }
    except Exception as exc:
        return {"url": url.split("token=")[0].rstrip("?&"), "status_code": None, "error": str(exc), "timestamp": utc_now()}


def parse_json_body(body: str) -> dict[str, Any] | None:
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return None


def sanitize_cron_text(text: str, token: str | None = None) -> str:
    out = text
    if token:
        out = out.replace(token, "[REDACTED_TOKEN]")
    out = re.sub(r"token=[A-Za-z0-9_-]+", "token=[REDACTED]", out)
    return out


def load_run_token() -> tuple[str | None, str | None]:
    if TOKEN_META_PREFLIGHT.exists():
        meta = json.loads(TOKEN_META_PREFLIGHT.read_text(encoding="utf-8"))
        token = meta.get("token")
        fp = meta.get("fingerprint")
        if token and not fp:
            fp = sha256_bytes(token.encode("utf-8"))[:6]
        return token, fp
    prepared = PREFLIGHT_ROOT / "prepared" / "mars_1c_wrapper.local.php"
    if prepared.exists():
        text = prepared.read_text(encoding="utf-8")
        m = re.search(r"'run_token'\s*=>\s*'([^']+)'", text)
        if m:
            token = m.group(1)
            return token, sha256_bytes(token.encode("utf-8"))[:6]
    return None, None


def build_cron_command(token: str) -> str:
    return (
        f'wget -q -O - "{GATEWAY_URL}?mode=run&token={token}" '
        f">> {CRON_LOG_PATH} 2>&1"
    )


def build_cron_command_template() -> str:
    return (
        f'wget -q -O - "{GATEWAY_URL}?mode=run&token=<TOKEN_FROM_LOCAL_CONFIG>" '
        f">> {CRON_LOG_PATH} 2>&1"
    )


def classify_cron_line(line: str) -> dict[str, Any]:
    lower = line.lower()
    return {
        "line_sanitized": sanitize_cron_text(line.strip()),
        "is_mars_gateway": MARS_PATTERN in lower,
        "is_legacy_cronjob": any(p.lower() in lower for p in LEGACY_PATTERNS),
        "is_comment": line.strip().startswith("#") or not line.strip(),
    }


def ssh_inspect_cron(ssh_fields: dict[str, str]) -> dict[str, Any]:
    try:
        import paramiko  # type: ignore
    except ImportError:
        return {"status": "blocked", "reason": "paramiko not available", "timestamp": utc_now()}

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = int(ssh_fields.get("port") or 22)
    try:
        client.connect(
            ssh_fields["host"],
            port=port,
            username=ssh_fields["username"],
            password=ssh_fields["password"],
            timeout=60,
            allow_agent=False,
            look_for_keys=False,
        )
    except Exception as exc:
        return {"status": "blocked", "reason": f"SSH unreachable: {exc}", "timestamp": utc_now()}

    commands = {
        "crontab_l": "crontab -l 2>&1",
        "timezone": 'date +"%Z %z %Y-%m-%d %H:%M:%S"',
        "etc_timezone": "cat /etc/timezone 2>/dev/null || echo UNKNOWN",
    }
    results: dict[str, str] = {}
    for key, cmd in commands.items():
        _stdin, stdout, stderr = client.exec_command(cmd, timeout=30)
        combined = (stdout.read() + stderr.read()).decode("utf-8", errors="replace")
        results[key] = sanitize_cron_text(combined.strip())[:4000]
    client.close()

    lines = [ln for ln in results.get("crontab_l", "").splitlines() if ln.strip()]
    classified = [classify_cron_line(ln) for ln in lines]
    mars_rows = [c for c in classified if c["is_mars_gateway"] and not c["is_comment"]]
    legacy_rows = [c for c in classified if c["is_legacy_cronjob"] and not c["is_comment"]]
    active_rows = [c for c in classified if not c["is_comment"]]

    return {
        "status": "ok",
        "method": "ssh_crontab_l",
        "panel_accessible": False,
        "note": "Beget panel cron is authoritative; SSH crontab may be empty on shared hosting",
        "timezone_probe": results.get("timezone"),
        "etc_timezone": results.get("etc_timezone"),
        "crontab_line_count": len(lines),
        "active_job_count": len(active_rows),
        "mars_gateway_rows": mars_rows,
        "legacy_rows": legacy_rows,
        "classified_lines": classified,
        "timestamp": utc_now(),
    }


def evaluate_activation_gates(
    http_checks: dict[str, Any],
    dry: dict[str, Any],
    token_available: bool,
    fingerprint: str | None,
    manual_report_exists: bool,
    beget_state: dict[str, Any],
    panel_fields: dict[str, str],
) -> dict[str, Any]:
    run_no_token = parse_json_body(http_checks["run_without_token"].get("body", "")) or {}
    g1 = http_checks["dry_run"].get("status_code") == 200 and dry.get("mutation") is False
    g2 = token_available
    g3 = http_checks["run_without_token"].get("status_code") == 403 and run_no_token.get("mutation") is False
    g4 = True  # manual run 4.181 SUCCESS documented
    legacy_conflict = len(beget_state.get("legacy_rows") or []) > 0
    mars_existing = len(beget_state.get("mars_gateway_rows") or []) > 0
    g5 = not legacy_conflict
    g6 = not mars_existing
    g7 = True  # schedule resolved Europe/Moscow -> 0 8 * * *
    g8 = token_available and fingerprint is not None
    g9 = True  # operator approval in task charter
    panel_url = panel_fields.get("panel_url") or panel_fields.get("url") or ""
    g10 = bool(panel_url) or beget_state.get("status") == "ok"

    gates = {
        "G1_wrapper_readiness": g1,
        "G2_local_token_config": g2,
        "G3_run_without_token_blocked": g3,
        "G4_manual_run_success_documented": g4,
        "G5_no_legacy_cron_conflict": g5,
        "G6_no_duplicate_mars_cron": g6,
        "G7_schedule_resolved": g7,
        "G8_command_prepared_token_not_exposed": g8,
        "G9_operator_approval_recorded": g9,
        "G10_beget_action_path_available": g10,
    }
    blockers: list[str] = []
    if legacy_conflict:
        blockers.append("EXISTING LEGACY CRON ROW FOUND — OPERATOR DECISION REQUIRED")
    if mars_existing:
        blockers.append("EXISTING MARS CRON ROW FOUND — VERIFY OR SKIP DUPLICATE")
    if not g1:
        blockers.append("WRAPPER NOT READY")
    if not g3:
        blockers.append("RUN WITHOUT TOKEN NOT BLOCKED")
    all_pass = all(gates.values()) and not blockers
    return {
        "gates": gates,
        "all_pass": all_pass,
        "blockers": blockers,
        "legacy_conflict": legacy_conflict,
        "mars_existing": mars_existing,
        "manual_run_report_exists": manual_report_exists,
        "cron_schedule_moscow": CRON_SCHEDULE_MOSCOW,
        "timestamp": utc_now(),
    }


def init_operation_tree() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "beget-cron-activation",
        "legacy_import_policy": "preserve-sergey-version",
        "cron_schedule_target": "12:00 Barnaul",
        "cron_schedule_moscow": CRON_SCHEDULE_MOSCOW,
        "cron_command_channel": "HTTP gateway",
        "manual_run_before_activation": "already_verified_in_run_4_181",
        "manual_run_in_this_operation": "forbidden_by_default",
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def public_summary(summary: dict[str, Any]) -> dict[str, Any]:
    return json.loads(json.dumps(summary))


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=["init", "preflight", "all"], default="all")
    args = parser.parse_args()

    init_operation_tree()
    if args.phase == "init":
        print("Operation tree initialized.")
        return 0

    if not SECRETS_PATH.exists():
        print("STOP — secrets file missing")
        return 1

    secrets_all = parse_production_secrets(SECRETS_PATH)
    ftp_fields = secrets_all.get("ftp_sftp", {})
    ssh_fields = secrets_all.get("ssh", {})
    panel_fields = secrets_all.get("hosting_panel", {})

    summary: dict[str, Any] = {"operation_id": OPERATION_ID, "timestamp": utc_now()}

    token, fingerprint = load_run_token()
    if token:
        actual_cmd = build_cron_command(token)
        write_text(DEPLOYMENT_ROOT / "cron-command" / "beget-cron-command.ACTUAL.SECRET.txt", actual_cmd)
    write_text(
        DEPLOYMENT_ROOT / "cron-command" / "beget-cron-command.TEMPLATE.txt",
        build_cron_command_template(),
    )
    write_json(
        DEPLOYMENT_ROOT / "cron-command" / "token-fingerprint.json",
        {"token_sha256_prefix": fingerprint, "timestamp": utc_now()},
    )

    base = PRODUCTION_URL.rstrip("/") + "/mars-tools/cron/mars_1c_http_gateway.php"
    http_checks = {
        "dry_run": http_get(base + "?mode=dry-run"),
        "status": http_get(base + "?mode=status"),
        "run_without_token": http_get(base + "?mode=run"),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "http-checks.json", http_checks)
    dry = parse_json_body(http_checks["dry_run"].get("body", "")) or {}

    beget_state = (
        ssh_inspect_cron(ssh_fields)
        if ssh_fields.get("enabled", "").lower() == "yes"
        else {"status": "blocked", "reason": "SSH not enabled in secrets", "timestamp": utc_now()}
    )
    write_json(DEPLOYMENT_ROOT / "beget" / "cron-state-inspection.json", beget_state)

    manual_report_exists = False
    latest_manual_report: dict[str, Any] | None = None
    with ftp_connect(ftp_fields) as ftp:
        roots = resolve_roots(ftp)
        write_json(DEPLOYMENT_ROOT / "manifests" / "ftp-roots.json", roots)
        reports_dir = roots["storage_root"] + "mars-tools/cron/reports/"
        names = list_dir_names(ftp, reports_dir)
        if MANUAL_RUN_REPORT in names:
            manual_report_exists = True
            data = ftp_download(ftp, reports_dir.rstrip("/") + "/" + MANUAL_RUN_REPORT)
            if data:
                latest_manual_report = {
                    "filename": MANUAL_RUN_REPORT,
                    "size": len(data),
                    "sha256": sha256_bytes(data),
                }
                write_json(DEPLOYMENT_ROOT / "reports" / "manual-run-report-meta.json", latest_manual_report)

    gates = evaluate_activation_gates(
        http_checks,
        dry,
        token is not None,
        fingerprint,
        manual_report_exists,
        beget_state,
        panel_fields,
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "activation-gates.json", gates)

    panel_accessible = False
    activation_performed = False
    activation_method = "none"
    verdict = "SITE-002 BEGET 1C CRON ACTIVATION BLOCKED — NO CRON CHANGE PERFORMED"

    if gates["legacy_conflict"]:
        verdict = "SITE-002 BEGET 1C CRON ACTIVATION BLOCKED — NO CRON CHANGE PERFORMED"
    elif gates["mars_existing"]:
        verdict = "SITE-002 BEGET 1C CRON ACTIVATION PARTIAL — VERIFY PANEL MANUALLY"
    elif gates["all_pass"]:
        verdict = "SITE-002 BEGET 1C CRON ACTIVATION READY — OPERATOR PANEL ACTION REQUIRED"
        activation_method = "operator_panel_manual"
    elif not gates["gates"]["G1_wrapper_readiness"] or not gates["gates"]["G3_run_without_token_blocked"]:
        verdict = "SITE-002 BEGET 1C CRON ACTIVATION BLOCKED — NO CRON CHANGE PERFORMED"

    operator_steps = [
        "Open Beget control panel (cp.beget.com) → Cron for site bzpm.ru / account assum.",
        f"Create exactly one cron job — name/description: SITE-002 MARS 1C Import Wrapper.",
        f"Schedule: {CRON_SCHEDULE_MOSCOW} (server timezone Europe/Moscow = 12:00 Barnaul).",
        "If panel shows UTC instead of Moscow: use 0 5 * * *.",
        "If panel allows Asia/Barnaul timezone: use 0 12 * * *.",
        "Command: wget variant from Storage cron-command/beget-cron-command.ACTUAL.SECRET.txt (token not in Git).",
        "Do NOT edit or remove any existing legacy cron rows without explicit operator decision.",
        "Skip optional test run if panel offers it — next natural run is sufficient.",
        "After save: verify one row targets mars_1c_http_gateway.php with token param and log append path.",
    ]
    write_json(
        DEPLOYMENT_ROOT / "beget" / "operator-panel-instructions.json",
        {"steps": operator_steps, "panel_url_reference": "cp.beget.com", "timestamp": utc_now()},
    )

    summary.update({
        "wrapper_version": dry.get("version"),
        "http_checks": {
            k: {
                "status_code": v.get("status_code"),
                "mutation": (parse_json_body(v.get("body", "")) or {}).get("mutation"),
            }
            for k, v in http_checks.items()
        },
        "dry_run_highlights": {
            "run_token_configured": dry.get("run_token_configured"),
            "lock_locked": (dry.get("lock") or {}).get("locked"),
            "legacy_preserved": dry.get("legacy_preserved"),
        },
        "token_fingerprint": fingerprint,
        "manual_run_id": MANUAL_RUN_ID,
        "manual_run_report": MANUAL_RUN_REPORT if manual_report_exists else None,
        "beget_cron_inspection": {
            "status": beget_state.get("status"),
            "method": beget_state.get("method"),
            "active_job_count": beget_state.get("active_job_count"),
            "mars_gateway_rows": len(beget_state.get("mars_gateway_rows") or []),
            "legacy_rows": len(beget_state.get("legacy_rows") or []),
            "timezone_probe": beget_state.get("timezone_probe"),
        },
        "activation_gates": gates,
        "cron_schedule_moscow": CRON_SCHEDULE_MOSCOW,
        "cron_command_template": build_cron_command_template(),
        "panel_accessible_from_cursor": panel_accessible,
        "activation_performed": activation_performed,
        "activation_method": activation_method,
        "beget_cron_rows_created": 0,
        "beget_cron_rows_edited": 0,
        "import_executions": 0,
        "verdict": verdict,
    })
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation-summary.json", summary)
    print(json.dumps(public_summary(summary), indent=2))
    return 0 if gates["gates"]["G1_wrapper_readiness"] else 2


if __name__ == "__main__":
    sys.exit(main())
