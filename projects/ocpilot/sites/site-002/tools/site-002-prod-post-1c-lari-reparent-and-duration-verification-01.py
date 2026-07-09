#!/usr/bin/env python3
"""SITE-002 Post-1C Lari reparent and duration verification — read-only (Run 4.240)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import io
import json
import re
import shlex
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-01"
OCPILOT_RUN = "4.240"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_READ_ONLY_VERIFICATION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01"
RELATED_LARI_RUN = "SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01"
RELATED_LARI_OCPILOT = "4.235"
RELATED_DURATION_RUN = "SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01"
RELATED_DURATION_OCPILOT = "4.239"
DEPLOY_4239_ISO = "2026-07-09T17:07:52+00:00"
DEPLOY_4239 = datetime.fromisoformat(DEPLOY_4239_ISO)
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REPO_TOOLS = Path(r"X:\AI MARS\projects\ocpilot\sites\site-002\tools")
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

SUBDIRS = (
    "cron-reports",
    "cron-logs",
    "db-readonly",
    "http-snapshots",
    "sitemap",
    "routing",
    "parent-tiles",
    "verification",
    "manifests",
    "reports",
    "logs",
)

TXT_NAME_RE = re.compile(
    r"^mars_1c_import_(?P<date>20\d{2}-\d{2}-\d{2})_(?P<time>\d{6})\.txt$"
)
DURATION_RE = re.compile(r"Duration:\s*([0-9]+(?:\.[0-9]+)?)\s*seconds?", re.I)
DURATION_TOTAL_RE = re.compile(
    r"Finished:\s*\n?\s*.+?\n\s*Duration:\s*\n?\s*([0-9]+(?:\.[0-9]+)?)\s*seconds?",
    re.I | re.S,
)
RUN_ID_RE = re.compile(r"Run ID:\s*\n?\s*(\S+)", re.I)
STATUS_RE = re.compile(r"Final status:\s*\n?\s*(\S+)", re.I)
STARTED_RE = re.compile(r"Started:\s*\n?\s*(.+)", re.I)
FINISHED_RE = re.compile(r"Finished:\s*\n?\s*(.+)", re.I)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub_match = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE
        )
        if not sub_match:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub_match.group(1)
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
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
    fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def list_dir_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    norm = path if path.startswith("/") else "/" + path
    try:
        for name, _facts in ftp.mlsd(norm):
            if name not in (".", ".."):
                names.append(name)
        return names
    except ftplib.error_perm:
        pass
    lines: list[str] = []
    ftp.retrlines("LIST " + norm, lines.append)
    for line in lines:
        parts = line.split(maxsplit=8)
        if len(parts) >= 9:
            names.append(parts[8])
    return names


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes | None:
    bio = io.BytesIO()
    norm = remote_path if remote_path.startswith("/") else "/" + remote_path
    try:
        ftp.retrbinary("RETR " + norm, bio.write)
        return bio.getvalue()
    except ftplib.error_perm:
        return None


def resolve_cron_roots(ftp: ftplib.FTP) -> dict[str, str]:
    pwd = ftp.pwd() or "/"
    login_root = pwd if pwd.startswith("/") else "/" + pwd
    if not login_root.endswith("/"):
        login_root += "/"
    storage_root = login_root + "storage/mars-tools/cron/"
    return {
        "login_root": login_root,
        "cron_root": storage_root,
        "reports_dir": storage_root + "reports/",
        "logs_dir": storage_root + "logs/",
    }


def moscow_to_utc(dt_moscow_naive: datetime) -> datetime:
    from datetime import timedelta

    # Report filenames use Europe/Moscow wall time (UTC+3).
    return (dt_moscow_naive - timedelta(hours=3)).replace(tzinfo=timezone.utc)


def parse_report_filename_utc(name: str) -> datetime | None:
    m = TXT_NAME_RE.match(name)
    if not m:
        return None
    dt = datetime.strptime(m.group("date") + m.group("time"), "%Y-%m-%d%H%M%S")
    return moscow_to_utc(dt)


def parse_txt_content(text: str) -> dict[str, Any]:
    out: dict[str, Any] = {"duration_line": None, "duration_seconds": None, "run_id": None, "final_status": None}
    if m := DURATION_TOTAL_RE.search(text):
        out["duration_line"] = "Duration: " + m.group(1) + " seconds"
        out["duration_seconds"] = float(m.group(1))
    else:
        for line in text.splitlines():
            if m := DURATION_RE.search(line):
                out["duration_line"] = line.strip()
                out["duration_seconds"] = float(m.group(1))
    if m := RUN_ID_RE.search(text):
        out["run_id"] = m.group(1)
    if m := STATUS_RE.search(text):
        out["final_status"] = m.group(1)
    if m := STARTED_RE.search(text):
        out["started"] = m.group(1).strip()
    if m := FINISHED_RE.search(text):
        out["finished"] = m.group(1).strip()
    steps = []
    for block in re.split(r"(?=Step \d+)", text):
        sm = re.search(
            r"Step\s+(\d+)[^\n]*\n.*?status:\s*\n?\s*(\S+).*?duration:\s*\n?\s*([0-9]+(?:\.[0-9]+)?)\s*seconds?",
            block,
            re.I | re.S,
        )
        if sm:
            steps.append({"step": int(sm.group(1)), "status": sm.group(2), "duration_seconds": float(sm.group(3))})
    out["steps"] = steps
    return out


def init_storage() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "related_lari_run": RELATED_LARI_RUN,
        "related_lari_ocpilot_run": RELATED_LARI_OCPILOT,
        "related_duration_run": RELATED_DURATION_RUN,
        "related_duration_ocpilot_run": RELATED_DURATION_OCPILOT,
        "change_type": "post-1c-verification",
        "production_mutation_allowed": False,
        "ftp_upload_allowed": False,
        "db_write_allowed": False,
        "admin_save_allowed": False,
        "import_run_allowed": False,
        "monitor_run_allowed": False,
        "task_scheduler_change_allowed": False,
        "report_only": True,
        "deploy_4239_timestamp": DEPLOY_4239_ISO,
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase1_import_gate(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    report_names = sorted(
        n for n in list_dir_names(ftp, roots["reports_dir"])
        if TXT_NAME_RE.match(n)
    )
    log_names = sorted(n for n in list_dir_names(ftp, roots["logs_dir"]) if n.endswith(".log"))
    rows: list[dict[str, Any]] = []
    for name in report_names:
        ts_utc = parse_report_filename_utc(name)
        rows.append(
            {
                "file_name": name,
                "report_timestamp_utc": ts_utc.isoformat() if ts_utc else "",
                "after_deploy_4239": bool(ts_utc and ts_utc > DEPLOY_4239),
                "remote_path": roots["reports_dir"] + name,
            }
        )
    latest_name = report_names[-1] if report_names else ""
    latest_ts = parse_report_filename_utc(latest_name) if latest_name else None
    latest_after_deploy = bool(latest_ts and latest_ts > DEPLOY_4239)

    latest_txt_path = ""
    latest_parsed: dict[str, Any] = {}
    if latest_name:
        raw = ftp_download(ftp, roots["reports_dir"] + latest_name)
        if raw:
            text = raw.decode("utf-8", errors="replace")
            (DEPLOYMENT_ROOT / "cron-reports" / latest_name).write_bytes(raw)
            latest_parsed = parse_txt_content(text)
            latest_txt_path = roots["reports_dir"] + latest_name

    # download matching log if present
    latest_log_name = log_names[-1] if log_names else ""
    log_info: dict[str, Any] = {"file_name": latest_log_name}
    if latest_log_name:
        raw_log = ftp_download(ftp, roots["logs_dir"] + latest_log_name)
        if raw_log:
            (DEPLOYMENT_ROOT / "cron-logs" / latest_log_name).write_bytes(raw_log)
            log_info["remote_path"] = roots["logs_dir"] + latest_log_name
            log_info["size_bytes"] = len(raw_log)

    index = {
        "observed_at": utc_now(),
        "deploy_4239_timestamp": DEPLOY_4239_ISO,
        "reports_dir": roots["reports_dir"],
        "logs_dir": roots["logs_dir"],
        "report_count": len(report_names),
        "log_count": len(log_names),
        "latest_report_file": latest_name,
        "latest_report_timestamp_utc": latest_ts.isoformat() if latest_ts else None,
        "latest_report_after_deploy_4239": latest_after_deploy,
        "latest_report_remote_path": latest_txt_path,
        "latest_report_parsed": latest_parsed,
        "latest_log": log_info,
        "all_reports": rows,
    }

    write_json(DEPLOYMENT_ROOT / "cron-reports" / "latest-import-report-index.json", index)
    write_csv(
        DEPLOYMENT_ROOT / "cron-reports" / "latest-import-report-index.csv",
        rows,
        ["file_name", "report_timestamp_utc", "after_deploy_4239", "remote_path"],
    )
    md = [
        "# Latest import report index",
        "",
        f"- Observed: {index['observed_at']}",
        f"- Run 4.239 deploy (UTC): `{DEPLOY_4239_ISO}`",
        f"- Latest TXT: `{latest_name}`",
        f"- Latest report UTC: `{latest_ts.isoformat() if latest_ts else 'n/a'}`",
        f"- After deploy 4.239: **{latest_after_deploy}**",
        "",
        "## Reports",
        "",
    ]
    for row in rows:
        md.append(
            f"- `{row['file_name']}` — after deploy: {row['after_deploy_4239']}"
        )
    write_text(DEPLOYMENT_ROOT / "cron-reports" / "latest-import-report-index.md", "\n".join(md) + "\n")
    return index


def blocked_consolidated(index: dict[str, Any]) -> dict[str, Any]:
    parsed = index.get("latest_report_parsed", {})
    return {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "observed_at": utc_now(),
        "latest_import_observed": False,
        "latest_import_run_id": parsed.get("run_id"),
        "latest_import_timestamp": index.get("latest_report_timestamp_utc"),
        "import_final_status": parsed.get("final_status"),
        "gate_reason": "No TXT report timestamp after Run 4.239 deployment",
        "duration_fix_pass": None,
        "txt_duration_seconds": parsed.get("duration_seconds"),
        "log_wall_time_seconds": None,
        "lari_db_pass": None,
        "lari_http_pass": None,
        "lari_sitemap_pass": None,
        "parent_tiles_pass": None,
        "public_brand_pass": None,
        "production_mutation_performed": False,
        "final_recommendation": "Re-run after next scheduled 1C import (~08:00 Europe/Moscow)",
        "final_verdict": "SITE-002 POST-1C LARI REPARENT AND DURATION VERIFICATION BLOCKED — NEXT IMPORT NOT OBSERVED",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", default="gate", choices=("gate", "full"))
    args = parser.parse_args()

    init_storage()
    ftp = ftp_connect()
    try:
        roots = resolve_cron_roots(ftp)
        index = phase1_import_gate(ftp, roots)
    finally:
        ftp.quit()

    latest_after = index["latest_report_after_deploy_4239"]
    if not latest_after:
        result = blocked_consolidated(index)
        write_json(DEPLOYMENT_ROOT / "verification" / "consolidated-result.json", result)
        write_text(
            DEPLOYMENT_ROOT / "verification" / "consolidated-result.md",
            "\n".join(
                [
                    "# Consolidated result — BLOCKED",
                    "",
                    f"**Verdict:** {result['final_verdict']}",
                    "",
                    f"- Latest report: `{index['latest_report_file']}`",
                    f"- Deploy 4.239: `{DEPLOY_4239_ISO}`",
                    "- Phases 2–6 skipped per timing gate.",
                ]
            )
            + "\n",
        )
        summary = {
            "operation_id": OPERATION_ID,
            "ocpilot_run": OCPILOT_RUN,
            "completed_at": utc_now(),
            "blocked": True,
            "verdict": result["final_verdict"],
            "latest_report": index["latest_report_file"],
            "ftp_reads": index["report_count"] + index["log_count"] + 2,
            "ftp_downloads": 1 + (1 if index.get("latest_log", {}).get("size_bytes") else 0),
        }
        write_json(DEPLOYMENT_ROOT / "reports" / "operation-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 2

    print("Post-deploy import observed — full verification not implemented in gate-only run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
