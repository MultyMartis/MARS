#!/usr/bin/env python3
"""SITE-002 Beget 1C cron active confirmation — documentation only, no import."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01"
MANUAL_RUN_REPORT = "mars_1c_import_2026-07-05_205934.txt"
MANUAL_RUN_ID = "mars-20260705-205929-df82e686"
CRON_SCHEDULE = "0 8 * * *"
GATEWAY_BASE = "https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php"
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01"
)
STORAGE_BASELINE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

SUBDIRS = ("verification", "beget", "reports", "manifests")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def http_get(url: str, timeout: int = 120) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(262144)
            return {
                "url": re.sub(r"token=[^&]+", "token=<TOKEN_PRESENT>", url.split("?")[0] + "?" + url.split("?", 1)[-1] if "?" in url else url),
                "status_code": resp.status,
                "body": body.decode("utf-8", errors="replace"),
                "body_sha256": sha256_bytes(body),
                "timestamp": utc_now(),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read(262144) if exc.fp else b""
        safe_url = url.split("token=")[0].rstrip("?&")
        return {
            "url": safe_url,
            "status_code": exc.code,
            "body": body.decode("utf-8", errors="replace"),
            "body_sha256": sha256_bytes(body) if body else None,
            "timestamp": utc_now(),
        }
    except Exception as exc:
        return {"url": GATEWAY_BASE, "status_code": None, "error": str(exc), "timestamp": utc_now()}


def parse_json_body(body: str) -> dict[str, Any] | None:
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return None


def evaluate_wrapper_checks(checks: dict[str, dict[str, Any]]) -> dict[str, Any]:
    dry = parse_json_body(checks["dry-run"]["body"]) or {}
    status = parse_json_body(checks["status"]["body"]) or {}
    run_no = parse_json_body(checks["run-no-token"]["body"]) or {}

    results = {
        "dry_run_http": checks["dry-run"]["status_code"],
        "dry_run_mutation": dry.get("mutation"),
        "dry_run_pass": checks["dry-run"]["status_code"] == 200 and dry.get("mutation") is False,
        "status_http": checks["status"]["status_code"],
        "status_mutation": status.get("mutation"),
        "status_pass": checks["status"]["status_code"] == 200 and status.get("mutation") is False,
        "run_no_token_http": checks["run-no-token"]["status_code"],
        "run_no_token_mutation": run_no.get("mutation"),
        "run_no_token_pass": checks["run-no-token"]["status_code"] == 403 and run_no.get("mutation") is False,
        "wrapper_version": dry.get("version"),
        "run_token_configured": dry.get("run_token_configured"),
        "lock_held": (dry.get("lock") or {}).get("locked"),
        "reports_dir": (dry.get("paths") or {}).get("reports_dir"),
        "log_dir": (dry.get("paths") or {}).get("log_dir"),
        "manual_run_report_in_logs": MANUAL_RUN_REPORT in (status.get("last_log_lines") or []),
    }
    results["overall_pass"] = all(
        (
            results["dry_run_pass"],
            results["status_pass"],
            results["run_no_token_pass"],
            results["wrapper_version"] is not None,
            results["run_token_configured"] is True,
            results["lock_held"] is False,
        )
    )
    return results


def operator_cron_evidence() -> dict[str, Any]:
    return {
        "source": "operator_screenshot_and_charter",
        "name": "SITE-002 MARS 1C Import Wrapper",
        "schedule_cron": CRON_SCHEDULE,
        "schedule_fields": {
            "minutes": "0",
            "hours": "8",
            "days": "*",
            "months": "*",
            "weekdays": "*",
        },
        "server_timezone": "Europe/Moscow",
        "business_time": "12:00 Barnaul",
        "command_target": "https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php",
        "query_mode": "run",
        "query_token": "<TOKEN_PRESENT>",
        "log_append": ">> /home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_cron_stdout.log 2>&1",
        "active_toggle": "enabled",
        "created_by": "operator_manual_panel",
        "token_rotation": "not_performed_by_operator_decision",
        "screenshot_token_visible": True,
        "screenshot_stored_in_repo": False,
    }


def external_cron_rows() -> list[dict[str, str]]:
    return [
        {"classification": "EXTERNAL / EXISTING HOSTING CRON ROWS — NOT TOUCHED", "target": "https://assum.ru/data/parse_yml.php"},
        {"classification": "EXTERNAL / EXISTING HOSTING CRON ROWS — NOT TOUCHED", "target": "https://assum.ru/data/parse_techno.php"},
        {"classification": "EXTERNAL / EXISTING HOSTING CRON ROWS — NOT TOUCHED", "target": "rm -f *php*"},
        {"classification": "EXTERNAL / EXISTING HOSTING CRON ROWS — NOT TOUCHED", "target": "https://assum.ru/data/parse.php"},
    ]


def build_operation_manifest(wrapper_eval: dict[str, Any]) -> dict[str, Any]:
    return {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "checkpoint_after": CHECKPOINT_AFTER,
        "change_type": "beget-cron-active-confirmation",
        "operator_created_cron_row": True,
        "token_rotation": "not_performed_by_operator_decision",
        "import_execution_allowed": False,
        "import_executed_in_operation": False,
        "beget_panel_change_by_cursor": False,
        "cron_schedule": CRON_SCHEDULE,
        "cron_business_time": "12:00 Barnaul",
        "cron_server_time": "08:00 Europe/Moscow",
        "cron_command_sanitized": "mars_1c_http_gateway.php?mode=run&token=<TOKEN_PRESENT>",
        "wrapper_readiness_pass": wrapper_eval["overall_pass"],
        "manual_run_reference": {
            "run_id": MANUAL_RUN_ID,
            "report_file": MANUAL_RUN_REPORT,
        },
        "timestamp_utc": utc_now(),
    }


def run_verification() -> int:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    STORAGE_BASELINE.mkdir(parents=True, exist_ok=True)

    checks = {
        "dry-run": http_get(f"{GATEWAY_BASE}?mode=dry-run"),
        "status": http_get(f"{GATEWAY_BASE}?mode=status"),
        "run-no-token": http_get(f"{GATEWAY_BASE}?mode=run"),
    }
    for name, payload in checks.items():
        sanitized = dict(payload)
        sanitized["body"] = re.sub(r"token=[A-Za-z0-9_-]+", "token=<TOKEN_PRESENT>", sanitized.get("body", ""))
        write_json(DEPLOYMENT_ROOT / "verification" / f"http-{name.replace('-', '_')}.json", sanitized)

    wrapper_eval = evaluate_wrapper_checks(checks)
    write_json(DEPLOYMENT_ROOT / "verification" / "wrapper-readiness.json", wrapper_eval)

    cron_evidence = operator_cron_evidence()
    write_json(DEPLOYMENT_ROOT / "beget" / "operator-cron-row-evidence.json", cron_evidence)
    write_json(DEPLOYMENT_ROOT / "beget" / "external-cron-rows-observed.json", external_cron_rows())

    manifest = build_operation_manifest(wrapper_eval)
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)
    write_json(STORAGE_BASELINE / "checkpoint-meta.json", manifest)

    write_json(
        DEPLOYMENT_ROOT / "reports" / "operation-summary.json",
        {
            "operation_id": OPERATION_ID,
            "wrapper_pass": wrapper_eval["overall_pass"],
            "verdict": (
                "SITE-002 BEGET 1C CRON ACTIVE — DAILY IMPORT SCHEDULED"
                if wrapper_eval["overall_pass"]
                else "SITE-002 BEGET 1C CRON ACTIVE CONFIRMATION BLOCKED — WRAPPER NOT READY"
            ),
            "next_monitoring": "after 08:00 Europe/Moscow / 12:00 Barnaul scheduled run",
        },
    )

    print(json.dumps({"wrapper_eval": wrapper_eval, "manifest_written": str(DEPLOYMENT_ROOT)}, indent=2))
    return 0 if wrapper_eval["overall_pass"] else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--verify", action="store_true", help="Run HTTP checks and write Storage artefacts")
    args = parser.parse_args()
    if args.verify:
        return run_verification()
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
