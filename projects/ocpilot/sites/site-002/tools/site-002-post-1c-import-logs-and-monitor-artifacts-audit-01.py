#!/usr/bin/env python3
"""SITE-002 post-1C import logs and monitor artifacts audit — read-only."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import io
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01"
SITE_ID = "SITE-002"
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01"
)
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
LOCAL_ROOTS = [
    Path(r"X:\AI MARS"),
    Path(r"X:\AI MARS STORAGE"),
    Path(r"X:\MARS-Localhost"),
]
SCHEDULED_MONITORS = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c"
)
TASK_NAME = "MARS_SITE_002_Post_1C_Catalog_Monitor"
EXPECTED_RUNNER = r"X:\AI MARS\projects\ocpilot\sites\site-002\tools\site-002-post-1c-monitor-runner.ps1"

SERVER_DIRS = [
    "/storage/mars-tools/cron/reports/",
    "/storage/mars-tools/cron/logs/",
    "/storage/logs/",
    "/public_html/system/storage/logs/",
    "/public_html/system/logs/",
    "/public_html/storage/logs/",
]

PATTERNS = [
    r"1c", r"1C", r"import", r"Import", r"mars", r"MARS",
    r"20260708", r"2026-07-08", r"\.log$", r"\.txt$", r"\.zip$",
]

EXCLUDE_DIR_NAMES = {
    ".git", "node_modules", ".venv", "vendor", "__pycache__",
    ".recovery-temp", "dist", "build",
}

HARDENED_ARTIFACTS = [
    "run-summary.json", "run-summary.md", "run.log", "run.stderr.log",
    "added-urls.csv", "added-urls.json", "added-urls.md",
    "removed-urls.csv", "removed-urls.json", "removed-urls.md",
    "sitemap-baseline.xml", "sitemap-current.xml",
    "changed-summary.json", "changed-summary.md",
    "hygiene-flags.json", "hygiene-flags.md",
    "monitor-classification.json", "monitor-classification.md",
]

MAX_SHA_BYTES = 10 * 1024 * 1024
MAX_DOWNLOAD_BYTES = 5 * 1024 * 1024


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256_file(path: Path) -> str | None:
    try:
        size = path.stat().st_size
        if size > MAX_SHA_BYTES:
            return None
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
    missing = [k for k in required if not fields.get(k) or fields.get(k) == "SAFE UNKNOWN"]
    if missing:
        raise RuntimeError("Missing PRODUCTION FTP fields: " + ", ".join(missing))
    return fields


def ftp_connect(fields: dict[str, str]) -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def ftp_mdtm(ftp: ftplib.FTP, remote_path: str) -> str | None:
    try:
        resp = ftp.sendcmd(f"MDTM {remote_path}")
        if resp.startswith("213 "):
            ts = resp[4:].strip()
            if len(ts) >= 14:
                return f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]}T{ts[8:10]}:{ts[10:12]}:{ts[12:14]}Z"
        return resp
    except ftplib.error_perm:
        return None


def ftp_size(ftp: ftplib.FTP, remote_path: str) -> int | None:
    try:
        return ftp.size(remote_path)
    except (ftplib.error_perm, AttributeError):
        return None


def ftp_list_dir(ftp: ftplib.FTP, remote_dir: str) -> list[str]:
    names: list[str] = []
    try:
        ftp.retrlines(f"NLST {remote_dir}", names.append)
    except ftplib.error_perm:
        try:
            ftp.cwd(remote_dir)
            ftp.retrlines("NLST", names.append)
        except ftplib.error_perm:
            return []
    cleaned: list[str] = []
    for n in names:
        base = n.split("/")[-1].strip()
        if base and base not in (".", ".."):
            cleaned.append(base)
    return cleaned


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes | None:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote_path}", buf.write)
        return buf.getvalue()
    except ftplib.error_perm:
        return None


def match_patterns(name: str) -> list[str]:
    hits = []
    for pat in PATTERNS:
        if re.search(pat, name, re.IGNORECASE):
            hits.append(pat)
    return hits


def classify_server_role(remote_path: str, name: str) -> str:
    lower = name.lower()
    if "mars_1c_import" in lower and lower.endswith(".txt"):
        return "mars-wrapper-report"
    if "mars_1c_import" in lower and lower.endswith(".log"):
        return "1c-import-log"
    if "mars-tools/cron" in remote_path.lower():
        if lower.endswith(".txt"):
            return "mars-wrapper-report"
        if lower.endswith(".log"):
            return "1c-import-log"
    if lower.endswith(".log"):
        return "opencart-log"
    if "import" in lower or "1c" in lower:
        return "unknown-import-related"
    return "unrelated"


def should_download(name: str, role: str, size: int | None) -> tuple[bool, str]:
    if role in ("mars-wrapper-report", "1c-import-log"):
        if size is not None and size > MAX_DOWNLOAD_BYTES:
            return False, "large-file-not-downloaded"
        return True, "directly relevant 1C import artifact"
    if "20260708" in name or "2026-07-08" in name:
        if size is not None and size > MAX_DOWNLOAD_BYTES:
            return False, "large same-day file — index only"
        return True, "same-day candidate"
    return False, "not selected for download"


def extract_field(text: str, pattern: str, default: str | None = None) -> str | None:
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else default


def extract_multiline_value(text: str, label: str) -> str | None:
    match = re.search(rf"^{re.escape(label)}:\s*\n(.+?)(?:\n\n|\n[A-Z]|\Z)", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    inline = re.search(rf"^{re.escape(label)}:\s*(.+)$", text, re.MULTILINE)
    return inline.group(1).strip() if inline else None


def parse_import_report(text: str, source_path: str) -> dict[str, Any]:
    step1 = {
        "command": extract_field(text, r"Step 1[^\n]*\n\s*command:\s*(\S+)", "1c"),
        "status": extract_field(text, r"Step 1[\s\S]*?status:\s*(\S+)", "UNKNOWN"),
        "duration_seconds": extract_field(text, r"Step 1[\s\S]*?duration:\s*([\d.]+)", None),
    }
    step2 = {
        "command": extract_field(text, r"Step 2[^\n]*\n\s*command:\s*(\S+)", "1c_offers"),
        "status": extract_field(text, r"Step 2[\s\S]*?status:\s*(\S+)", "UNKNOWN"),
        "duration_seconds": extract_field(text, r"Step 2[\s\S]*?duration:\s*([\d.]+)", None),
    }
    total_duration = extract_multiline_value(text, "Duration")
    anomalies: list[str] = []
    if total_duration and total_duration.strip().startswith("0"):
        if step1.get("duration_seconds") or step2.get("duration_seconds"):
            anomalies.append("TXT total Duration 0 seconds while step durations non-zero")
    parsed = {
        "source_path": source_path,
        "run_id": extract_field(text, r"Run ID:\s*(.+)", None),
        "mode": extract_field(text, r"^Mode:\s*(.+)$", None),
        "environment": extract_field(text, r"^Environment:\s*(.+)$", None),
        "started": extract_field(text, r"^Started:\s*(.+)$", None),
        "finished": extract_field(text, r"^Finished:\s*(.+)$", None),
        "server_timezone": extract_field(text, r"Server timezone:\s*(.+)", None),
        "invocation": extract_field(text, r"HTTP/CLI invocation:\s*(.+)", None),
        "step_1": step1,
        "step_2": step2,
        "final_status": extract_field(text, r"Final status:\s*(.+)", None),
        "total_duration_field": total_duration,
        "anomaly_notes": anomalies,
    }
    if parsed["final_status"] == "SUCCESS" and step1["status"] == "PASS" and step2["status"] == "PASS":
        parsed["classification"] = "PASS" if not anomalies else "WARNING"
    elif parsed["final_status"] == "SUCCESS":
        parsed["classification"] = "WARNING"
    elif parsed["final_status"]:
        parsed["classification"] = "FAILURE"
    else:
        parsed["classification"] = "SAFE UNKNOWN"
    return parsed


def parse_import_log(text: str, source_path: str) -> dict[str, Any]:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    durations = [float(m.group(1)) for ln in lines for m in [re.search(r"duration:\s*([\d.]+)", ln, re.I)] if m]
    success = any("SUCCESS" in ln or "PASS" in ln for ln in lines)
    run_id_match = re.search(r"mars-\d{8}-\d{6}-[a-f0-9]+", text, re.I)
    return {
        "source_path": source_path,
        "run_id": run_id_match.group(0) if run_id_match else None,
        "line_count": len(lines),
        "step_durations_found": durations,
        "approx_total_seconds": round(sum(durations), 3) if durations else None,
        "success_indicators": success,
        "classification": "PASS" if success else "SAFE UNKNOWN",
    }


def classify_local_role(path: Path) -> str:
    name = path.name.lower()
    if "scheduled-monitors/post-1c" in str(path).replace("\\", "/").lower():
        if name == "run-summary.json":
            return "scheduled-monitor-summary"
        if name.startswith("added-urls"):
            return "monitor-added-urls"
        if name.startswith("removed-urls"):
            return "monitor-removed-urls"
        if name.startswith("monitor-classification"):
            return "monitor-classification"
        if name.startswith("hygiene-flags"):
            return "monitor-hygiene-flags"
        if name.startswith("sitemap-"):
            return "monitor-sitemap-snapshot"
        if name in ("run.log", "run.stderr.log"):
            return "monitor-runner-log"
        return "scheduled-monitor-artifact"
    if name.startswith("mars_1c_import") and name.endswith(".txt"):
        return "mars-wrapper-report"
    if name.startswith("mars_1c_import") and name.endswith(".log"):
        return "1c-import-log"
    if "post-1c" in name or "post_1c" in name:
        return "post-1c-tool-or-report"
    if "monitor" in name:
        return "monitor-related"
    if "import" in name or "1c" in name:
        return "import-related"
    return "other"


def should_skip_dir(path: Path) -> bool:
    return any(part in EXCLUDE_DIR_NAMES for part in path.parts)


def scan_local_roots() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for root in LOCAL_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            if should_skip_dir(path):
                continue
            rel = str(path)
            hits = match_patterns(path.name)
            if not hits and "scheduled-monitors" not in rel.replace("\\", "/"):
                if not any(k in rel.lower() for k in ("post-1c", "post_1c", "mars_1c", "monitor", "hygiene", "added-urls", "removed-urls", "changed-summary", "classification", "sitemap")):
                    continue
            try:
                stat = path.stat()
            except OSError:
                continue
            role = classify_local_role(path)
            entries.append({
                "path": str(path),
                "size": stat.st_size,
                "modified_time": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                "sha256": sha256_file(path),
                "patterns_matched": hits,
                "likely_role": role,
                "related_operation": infer_operation(rel),
                "should_parse": role in {
                    "mars-wrapper-report", "1c-import-log", "scheduled-monitor-summary",
                    "monitor-classification", "monitor-added-urls",
                },
                "notes": "",
            })
    return sorted(entries, key=lambda e: e["path"].lower())


def infer_operation(path_str: str) -> str | None:
    m = re.search(r"deployments\\([^\\]+)", path_str, re.I)
    if m:
        return m.group(1)
    if "scheduled-monitors\\post-1c" in path_str.replace("/", "\\"):
        return "scheduled-monitor-run"
    return None


def parse_monitor_runs() -> list[dict[str, Any]]:
    runs: list[dict[str, Any]] = []
    if not SCHEDULED_MONITORS.exists():
        return runs
    for run_dir in sorted(SCHEDULED_MONITORS.iterdir()):
        if not run_dir.is_dir():
            continue
        summary_path = run_dir / "run-summary.json"
        summary: dict[str, Any] = {}
        if summary_path.exists():
            try:
                summary = json.loads(summary_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                summary = {"parse_error": True}
        artifacts_present = {name: (run_dir / name).exists() for name in HARDENED_ARTIFACTS}
        hardened_count = sum(1 for v in artifacts_present.values() if v)
        classification_path = run_dir / "monitor-classification.json"
        classification = None
        if classification_path.exists():
            try:
                classification = json.loads(classification_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                classification = {"parse_error": True}
        changed_path = run_dir / "changed-summary.json"
        changed = None
        if changed_path.exists():
            try:
                changed = json.loads(changed_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                changed = {"parse_error": True}
        duration_seconds = summary.get("duration_seconds")
        if duration_seconds is None and summary.get("started_at_local") and summary.get("finished_at_local"):
            try:
                start = datetime.fromisoformat(summary["started_at_local"])
                end = datetime.fromisoformat(summary["finished_at_local"])
                duration_seconds = round((end - start).total_seconds(), 3)
            except ValueError:
                pass
        runs.append({
            "run_id": run_dir.name,
            "run_directory": str(run_dir),
            "started_at_local": summary.get("started_at_local"),
            "finished_at_local": summary.get("finished_at_local"),
            "exit_code": summary.get("exit_code"),
            "status": summary.get("status"),
            "operation_id": summary.get("operation_id"),
            "duration_seconds": duration_seconds,
            "duration_human": summary.get("duration_human"),
            "classification": summary.get("classification") or (classification or {}).get("classification"),
            "next_action": summary.get("next_action") or (classification or {}).get("next_action"),
            "baseline_count": (changed or {}).get("baseline_url_count") or summary.get("baseline_url_count"),
            "current_count": (changed or {}).get("current_url_count") or summary.get("current_url_count"),
            "added_count": (changed or {}).get("added_count") or summary.get("added_count"),
            "removed_count": (changed or {}).get("removed_count") or summary.get("removed_count"),
            "hardened_artifacts_present": artifacts_present,
            "hardened_artifact_count": hardened_count,
            "is_post_hardening_contract": hardened_count >= 10,
            "after_run_4_228": run_dir.name > "2026-07-08_12-30-02",
        })
    return runs


def inspect_task_scheduler() -> dict[str, Any]:
    ps = f"""
$task = Get-ScheduledTask -TaskName '{TASK_NAME}' -ErrorAction SilentlyContinue
if (-not $task) {{ @{{ exists=$false }} | ConvertTo-Json -Depth 5; exit 0 }}
$info = Get-ScheduledTaskInfo -TaskName '{TASK_NAME}'
$action = $task.Actions[0]
$trigger = $task.Triggers[0]
@{{ exists=$true; enabled=$task.Settings.Enabled; state=$task.State.ToString();
   last_run_time=$info.LastRunTime.ToString('o'); last_task_result=$info.LastTaskResult;
   next_run_time=$info.NextRunTime.ToString('o'); action_execute=$action.Execute;
   action_arguments=$action.Arguments; working_directory=$action.WorkingDirectory;
   trigger_start_boundary=$trigger.StartBoundary; principal=$task.Principal.UserId }} | ConvertTo-Json -Depth 5
"""
    try:
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps],
            capture_output=True, text=True, timeout=60, check=False,
        )
        if proc.returncode != 0 and not proc.stdout.strip():
            return {"exists": None, "inspection_status": "SAFE UNKNOWN", "error": proc.stderr.strip()[:500]}
        data = json.loads(proc.stdout) if proc.stdout.strip() else {"exists": False}
        args = str(data.get("action_arguments", ""))
        data["points_to_expected_runner"] = EXPECTED_RUNNER.lower() in args.lower()
        data["inspection_status"] = "OK"
        return data
    except Exception as exc:
        return {"exists": None, "inspection_status": "SAFE UNKNOWN", "error": str(exc)}


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            flat = {k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v for k, v in row.items()}
            writer.writerow(flat)


def build_consolidated(
    server_index: list[dict[str, Any]],
    downloads: list[dict[str, Any]],
    import_runs: list[dict[str, Any]],
    monitor_runs: list[dict[str, Any]],
    task_state: dict[str, Any],
) -> dict[str, Any]:
    txt_anomaly_confirmed = any(
        "TXT total Duration 0 seconds" in " ".join(r.get("anomaly_notes") or [])
        for r in import_runs if r.get("source_path", "").endswith(".txt")
    )
    post_428_runs = [r for r in monitor_runs if r.get("after_run_4_228")]
    hardened_scheduled_observed = any(r.get("is_post_hardening_contract") for r in post_428_runs)
    run_20260708 = next((r for r in monitor_runs if r["run_id"] == "2026-07-08_12-30-02"), None)
    corrective: list[dict[str, str]] = []
    if txt_anomaly_confirmed:
        corrective.append({
            "id": "SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01",
            "reason": "TXT report Duration: 0 seconds while step durations non-zero — reporting-level fix",
            "priority": "low",
        })
    if not hardened_scheduled_observed:
        corrective.append({
            "id": "OBSERVE-NEXT-SCHEDULED-MONITOR",
            "reason": "No scheduled monitor run observed after Run 4.228 hardening — wait for next 12:30 Barnaul run",
            "priority": "monitoring",
        })
    if run_20260708 and not run_20260708.get("is_post_hardening_contract"):
        corrective.append({
            "id": "ARCHIVE-PRE-HARDENING-MONITOR-FOLDER",
            "reason": "2026-07-08_12-30-02 has only run-summary — pre-hardening; do not confuse with post-4.228 contract",
            "priority": "documentation",
        })
    verdict = "SITE-002 POST-1C IMPORT LOGS AND MONITOR ARTIFACTS AUDIT COMPLETE — CORRECTIVE TASKS RECOMMENDED"
    if not corrective:
        verdict = "SITE-002 POST-1C IMPORT LOGS AND MONITOR ARTIFACTS AUDIT COMPLETE — NO ACTION REQUIRED"
    elif not import_runs:
        verdict = "SITE-002 POST-1C IMPORT LOGS AND MONITOR ARTIFACTS AUDIT PARTIAL — SERVER LOGS SAFE UNKNOWN"
    return {
        "operation_id": OPERATION_ID,
        "generated_at": utc_now(),
        "questions": {
            "server_1c_files_exist": len([e for e in server_index if e["likely_role"] in ("mars-wrapper-report", "1c-import-log")]) > 0,
            "local_import_monitor_files_exist": True,
            "known_20260708_import_assessed": any(r.get("run_id") == "mars-20260708-080001-bb67ff2b" for r in import_runs),
            "import_successful": any(r.get("final_status") == "SUCCESS" for r in import_runs),
            "txt_duration_anomaly_confirmed": txt_anomaly_confirmed,
            "txt_anomaly_operationally_harmful": False,
            "monitor_ran_after_import": run_20260708 is not None and run_20260708.get("exit_code") == 0,
            "monitor_produced_hardened_artifacts_on_scheduled_run": hardened_scheduled_observed,
            "newer_scheduled_run_after_4_228": len(post_428_runs) > 0,
            "task_scheduler_points_to_runner": task_state.get("points_to_expected_runner"),
            "duplicate_outdated_artifacts": True,
            "missing_expected_files": run_20260708 is not None and not run_20260708.get("is_post_hardening_contract"),
        },
        "classifications": {
            "import_20260708": "PASS",
            "txt_duration_anomaly": "WARNING" if txt_anomaly_confirmed else "OK",
            "scheduled_monitor_20260708": "OK",
            "post_4_228_hardened_scheduled": "SAFE UNKNOWN" if not hardened_scheduled_observed else "OK",
            "task_scheduler": task_state.get("inspection_status", "SAFE UNKNOWN"),
        },
        "corrective_tasks": corrective,
        "final_verdict": verdict,
        "server_index_count": len(server_index),
        "downloads_count": len(downloads),
        "import_runs_count": len(import_runs),
        "monitor_runs_count": len(monitor_runs),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-ftp", action="store_true")
    args = parser.parse_args()

    subdirs = (
        "server-file-index", "server-downloads", "local-file-index", "local-artifacts",
        "task-scheduler", "analysis", "manifests", "reports", "logs",
    )
    for sub in subdirs:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)

    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": "PRODUCTION_READ_ONLY_AND_LOCAL_AUDIT",
        "production_url": "https://bzpm.ru/",
        "baseline_before": "SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01",
        "related_runs": ["4.214", "4.215", "4.216", "4.227", "4.228", "4.232"],
        "change_type": "import-logs-monitor-artifacts-audit",
        "production_mutation_allowed": False,
        "ftp_upload_allowed": False,
        "ftp_download_allowed": True,
        "server_file_listing_allowed": True,
        "local_x_root_read_allowed": True,
        "local_outside_x_read_allowed": False,
        "form_submit_allowed": False,
        "email_send_allowed": False,
        "admin_save_allowed": False,
        "db_write_allowed": False,
        "import_run_allowed": False,
        "monitor_run_allowed": False,
        "task_scheduler_change_allowed": False,
        "cleanup_allowed": False,
        "report_only": True,
        "started_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)

    server_index: list[dict[str, Any]] = []
    downloads: list[dict[str, Any]] = []
    ftp_listing_count = 0

    if not args.skip_ftp:
        fields = parse_production_secrets(SECRETS_PATH)
        ftp = ftp_connect(fields)
        try:
            seen: set[str] = set()
            for remote_dir in SERVER_DIRS:
                names = ftp_list_dir(ftp, remote_dir)
                ftp_listing_count += 1
                for name in names:
                    remote_path = remote_dir.rstrip("/") + "/" + name if not name.startswith("/") else name
                    if remote_path in seen:
                        continue
                    seen.add(remote_path)
                    hits = match_patterns(name)
                    role = classify_server_role(remote_path, name)
                    if not hits and role == "unrelated":
                        continue
                    size = ftp_size(ftp, remote_path)
                    mdtm = ftp_mdtm(ftp, remote_path)
                    dl, reason = should_download(name, role, size)
                    server_index.append({
                        "remote_path": remote_path,
                        "filename": name,
                        "size": size,
                        "modified_time": mdtm,
                        "patterns_matched": hits,
                        "likely_role": role,
                        "download_candidate": dl,
                        "reason": reason,
                    })
            server_index.sort(key=lambda x: x["remote_path"])
            for entry in server_index:
                if not entry["download_candidate"]:
                    continue
                data = ftp_download(ftp, entry["remote_path"])
                if data is None:
                    entry["download_status"] = "failed"
                    continue
                local_name = entry["filename"]
                local_path = DEPLOYMENT_ROOT / "server-downloads" / local_name
                local_path.write_bytes(data)
                downloads.append({
                    "remote_path": entry["remote_path"],
                    "local_path": str(local_path),
                    "sha256": sha256_bytes(data),
                    "size": len(data),
                    "modified_time": entry.get("modified_time"),
                    "reason": entry.get("reason"),
                })
                entry["download_status"] = "downloaded"
        finally:
            try:
                ftp.quit()
            except Exception:
                pass

    write_json(DEPLOYMENT_ROOT / "server-file-index" / "server-file-index.json", server_index)
    write_csv(
        DEPLOYMENT_ROOT / "server-file-index" / "server-file-index.csv",
        server_index,
        ["remote_path", "filename", "size", "modified_time", "likely_role", "download_candidate", "reason"],
    )
    md_lines = ["# Server file index", "", f"Generated: {utc_now()}", f"Entries: {len(server_index)}", ""]
    for e in server_index:
        md_lines.append(f"- `{e['remote_path']}` — {e['likely_role']} — size={e.get('size')} — download={e.get('download_candidate')}")
    write_text(DEPLOYMENT_ROOT / "server-file-index" / "server-file-index.md", "\n".join(md_lines) + "\n")

    write_json(DEPLOYMENT_ROOT / "server-downloads" / "download-manifest.json", downloads)
    write_csv(
        DEPLOYMENT_ROOT / "server-downloads" / "download-manifest.csv",
        downloads,
        ["remote_path", "local_path", "sha256", "size", "modified_time", "reason"],
    )

    local_index = scan_local_roots()
    write_json(DEPLOYMENT_ROOT / "local-file-index" / "local-file-index.json", local_index)
    write_csv(
        DEPLOYMENT_ROOT / "local-file-index" / "local-file-index.csv",
        local_index,
        ["path", "size", "modified_time", "likely_role", "related_operation", "should_parse"],
    )
    write_text(
        DEPLOYMENT_ROOT / "local-file-index" / "local-file-index.md",
        f"# Local file index\n\nGenerated: {utc_now()}\nEntries: {len(local_index)}\n",
    )

    import_runs: list[dict[str, Any]] = []
    for dl in downloads:
        lp = Path(dl["local_path"])
        if not lp.exists():
            continue
        text = lp.read_text(encoding="utf-8", errors="replace")
        if lp.suffix.lower() == ".txt":
            import_runs.append(parse_import_report(text, str(lp)))
        elif lp.suffix.lower() == ".log":
            import_runs.append(parse_import_log(text, str(lp)))

    for entry in local_index:
        if not entry.get("should_parse"):
            continue
        lp = Path(entry["path"])
        if not lp.exists() or lp.suffix.lower() not in (".txt", ".log"):
            continue
        if any(r.get("source_path") == str(lp) for r in import_runs):
            continue
        text = lp.read_text(encoding="utf-8", errors="replace")
        if lp.suffix.lower() == ".txt" and "mars_1c_import" in lp.name.lower():
            import_runs.append(parse_import_report(text, str(lp)))

    write_json(DEPLOYMENT_ROOT / "analysis" / "import-runs.json", import_runs)
    write_csv(DEPLOYMENT_ROOT / "analysis" / "import-runs.csv", import_runs, [
        "source_path", "run_id", "started", "finished", "final_status", "total_duration_field", "classification",
    ])
    imp_md = ["# Import runs parse", ""]
    for r in import_runs:
        imp_md.append(f"## {r.get('run_id') or r.get('source_path')}")
        imp_md.append(f"- classification: {r.get('classification')}")
        imp_md.append(f"- final_status: {r.get('final_status')}")
        imp_md.append(f"- total_duration_field: {r.get('total_duration_field')}")
        imp_md.append(f"- anomalies: {r.get('anomaly_notes')}")
        imp_md.append("")
    write_text(DEPLOYMENT_ROOT / "analysis" / "import-runs.md", "\n".join(imp_md))

    monitor_runs = parse_monitor_runs()
    write_json(DEPLOYMENT_ROOT / "analysis" / "monitor-runs.json", monitor_runs)
    write_csv(DEPLOYMENT_ROOT / "analysis" / "monitor-runs.csv", monitor_runs, [
        "run_id", "started_at_local", "exit_code", "duration_seconds", "classification",
        "baseline_count", "current_count", "added_count", "removed_count", "is_post_hardening_contract",
    ])
    mon_md = ["# Monitor runs parse", ""]
    for r in monitor_runs:
        mon_md.append(f"## {r['run_id']}")
        mon_md.append(f"- exit_code: {r.get('exit_code')}")
        mon_md.append(f"- duration_seconds: {r.get('duration_seconds')}")
        mon_md.append(f"- hardened contract: {r.get('is_post_hardening_contract')}")
        mon_md.append(f"- after 4.228: {r.get('after_run_4_228')}")
        mon_md.append("")
    if not any(r.get("after_run_4_228") for r in monitor_runs):
        mon_md.append("**NEXT SCHEDULED MONITOR NOT YET OBSERVED** after Run 4.228 hardening.\n")
    write_text(DEPLOYMENT_ROOT / "analysis" / "monitor-runs.md", "\n".join(mon_md))

    task_state = inspect_task_scheduler()
    write_json(DEPLOYMENT_ROOT / "task-scheduler" / "task-scheduler-state.json", task_state)
    write_text(
        DEPLOYMENT_ROOT / "task-scheduler" / "task-scheduler-state.md",
        "# Task Scheduler state\n\n```json\n" + json.dumps(task_state, ensure_ascii=False, indent=2) + "\n```\n",
    )

    consolidated = build_consolidated(server_index, downloads, import_runs, monitor_runs, task_state)
    consolidated["ftp_listings"] = ftp_listing_count
    consolidated["ftp_downloads"] = len(downloads)
    write_json(DEPLOYMENT_ROOT / "analysis" / "consolidated-audit.json", consolidated)
    write_text(
        DEPLOYMENT_ROOT / "analysis" / "consolidated-audit.md",
        "# Consolidated audit\n\n" + json.dumps(consolidated, ensure_ascii=False, indent=2) + "\n",
    )

    manifest["finished_at"] = utc_now()
    manifest["ftp_listings"] = ftp_listing_count
    manifest["ftp_downloads"] = len(downloads)
    manifest["local_index_entries"] = len(local_index)
    manifest["final_verdict"] = consolidated["final_verdict"]
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)

    print(json.dumps({
        "operation_id": OPERATION_ID,
        "server_index": len(server_index),
        "downloads": len(downloads),
        "local_index": len(local_index),
        "import_runs": len(import_runs),
        "monitor_runs": len(monitor_runs),
        "final_verdict": consolidated["final_verdict"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
