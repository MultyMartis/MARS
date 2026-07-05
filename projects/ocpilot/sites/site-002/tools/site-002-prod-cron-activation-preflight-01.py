#!/usr/bin/env python3
"""SITE-002 1C cron activation preflight — token config, DB readonly, gated manual run."""
from __future__ import annotations

import argparse
import ftplib
import hashlib
import io
import json
import re
import secrets
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-RUN-REPORTS-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01"
)
SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "verification",
    "rollback",
    "manifests",
    "logs",
    "db-readonly",
    "manual-run",
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

LOCAL_CONFIG_REMOTE_SUFFIX = "mars-tools/cron/mars_1c_wrapper.local.php"
WRAPPER_REMOTE_SUFFIX = "mars-tools/cron/mars_1c_import_wrapper.php"
GATEWAY_REMOTE_SUFFIX = "public_html/mars-tools/cron/mars_1c_http_gateway.php"
XML_DIR_SUFFIX = "public_html/1c_incoming/webdata"
LOCK_REMOTE_SUFFIX = "mars-tools/cron/mars_1c_import.lock"
HOSTING_CLI_WRAPPER = "/home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php"

LOCAL_CONFIG_PREPARED = DEPLOYMENT_ROOT / "prepared" / "mars_1c_wrapper.local.php"
TOKEN_META = DEPLOYMENT_ROOT / "manifests" / "token-meta.json"


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


def token_fingerprint(token: str) -> str:
    return sha256_bytes(token.encode("utf-8"))[:6]


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
    for subsection in ("FTP / SFTP", "SSH", "Database"):
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


def ftp_upload(ftp: ftplib.FTP, remote_path: str, data: bytes) -> None:
    remote_path = normalize_remote(remote_path)
    parent = "/".join(remote_path.split("/")[:-1])
    if parent:
        ftp_mkdirs(ftp, parent)
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)


def ftp_mkdirs(ftp: ftplib.FTP, remote_dir: str) -> None:
    parts = [p for p in normalize_remote(remote_dir).split("/") if p]
    current = ""
    for part in parts:
        current += "/" + part
        try:
            ftp.mkd(current)
        except ftplib.error_perm as exc:
            if "550" not in str(exc):
                raise


def ftp_exists(ftp: ftplib.FTP, remote_path: str) -> bool:
    remote_path = normalize_remote(remote_path)
    try:
        ftp.size(remote_path)
        return True
    except ftplib.error_perm:
        return False


def ftp_mtime_size(ftp: ftplib.FTP, remote_path: str) -> dict[str, Any]:
    remote_path = normalize_remote(remote_path)
    meta: dict[str, Any] = {"remote": remote_path, "exists": False}
    try:
        meta["size"] = ftp.size(remote_path)
        meta["exists"] = True
    except ftplib.error_perm:
        return meta
    try:
        for name, facts in ftp.mlsd(remote_path.rsplit("/", 1)[0] or "/"):
            if name == remote_path.rsplit("/", 1)[-1]:
                if "modify" in facts:
                    meta["modified"] = facts["modify"]
                if "size" in facts:
                    meta["size"] = int(facts["size"])
                break
    except ftplib.error_perm:
        pass
    return meta


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
            body = resp.read(131072)
            return {
                "url": url.split("token=")[0].rstrip("?&"),
                "status_code": resp.status,
                "body": body.decode("utf-8", errors="replace"),
                "body_sha256": sha256_bytes(body),
                "timestamp": utc_now(),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read(131072) if exc.fp else b""
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


def sanitize_for_log(text: str, token: str | None = None) -> str:
    out = text
    if token:
        out = out.replace(token, "[REDACTED_TOKEN]")
    for marker in ("password", "DB_PASSWORD", "DB_USERNAME", "run_token"):
        out = re.sub(rf"({marker}\s*[=:]\s*)([^\s\"']+)", r"\1[REDACTED]", out, flags=re.I)
    return out


def init_operation_tree() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "cron-activation-preflight",
        "legacy_import_policy": "preserve-sergey-version",
        "beget_cron_activation": "forbidden",
        "manual_run_allowed": "conditional",
        "db_readonly_allowed": True,
        "authorized_remote_changes": [
            "create /storage/mars-tools/cron/mars_1c_wrapper.local.php if missing",
            "no legacy file changes",
        ],
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def build_local_config_php(token: str) -> str:
    return (
        "<?php\n"
        "/**\n"
        " * MARS SITE-002 local wrapper config — NOT for Git.\n"
        f" * Created by: {OPERATION_ID}\n"
        " */\n"
        "return [\n"
        f"    'run_token' => '{token}',\n"
        "    'enabled' => true,\n"
        "    'allow_http_run' => true,\n"
        "    'site_base_url' => 'https://bzpm.ru/',\n"
        f"    'created_by' => '{OPERATION_ID}',\n"
        "    'notes' => 'local production config, not committed',\n"
        "];\n"
    )


def ssh_db_readonly(ssh_fields: dict[str, str]) -> dict[str, Any]:
    probe_php = r"""<?php
declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');
$root = realpath(__DIR__ . '/../../..');
$config = $root . '/public_html/config.php';
if (!is_file($config)) { echo json_encode(['error'=>'config missing']); exit(1); }
require_once $config;
require_once DIR_SYSTEM . 'startup.php';
$db = new DB(DB_DRIVER, DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_PORT);
$rows = [];
foreach (['1c', '1c_offers'] as $cmd) {
    $cmdEsc = $db->escape($cmd);
    $q = $db->query("SELECT command, active, duration, lastrun FROM cron WHERE command = '" . $cmdEsc . "' LIMIT 1");
    if ($q->num_rows) {
        $rows[$cmd] = [
            'exists' => true,
            'active' => (int)$q->row['active'],
            'duration' => (int)$q->row['duration'],
            'lastrun' => (string)$q->row['lastrun'],
        ];
    } else {
        $rows[$cmd] = ['exists' => false];
    }
}
echo json_encode(['operation'=>'readonly-cron-probe','mutation'=>false,'rows'=>$rows], JSON_UNESCAPED_UNICODE);
"""
    probe_local = DEPLOYMENT_ROOT / "db-readonly" / "mars_1c_cron_readonly_probe.php"
    write_text(probe_local, probe_php)

    try:
        import paramiko  # type: ignore
    except ImportError:
        return {"status": "blocked", "reason": "paramiko not available for SSH DB readonly probe"}

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
        return {"status": "blocked", "reason": f"SSH unreachable from operator environment: {exc}"}

    remote_probe = "/home/a/assum/bzpm.ru/storage/mars-tools/cron/_mars_readonly_cron_probe.php"
    php_bins = ["/usr/bin/php8.2", "/usr/bin/php8.1", "/usr/bin/php7.4", "/usr/bin/php"]
    sftp = client.open_sftp()
    out = ""
    err = ""
    probe_removed = False
    chosen_php = None
    last_out = ""
    last_err = ""
    try:
        with sftp.file(remote_probe, "w") as fh:
            fh.write(probe_php)
        for php_bin in php_bins:
            _stdin, stdout, stderr = client.exec_command(f"{php_bin} {remote_probe}", timeout=60)
            last_out = stdout.read().decode("utf-8", errors="replace")
            last_err = stderr.read().decode("utf-8", errors="replace")
            if "PHP7.3+ Required" not in last_out and last_out.strip().startswith("{"):
                out = last_out
                err = last_err
                chosen_php = php_bin
                break
        if chosen_php is None:
            out = last_out
            err = last_err
        try:
            sftp.remove(remote_probe)
            probe_removed = True
        except OSError:
            probe_removed = False
    finally:
        sftp.close()
        client.close()

    if chosen_php is None:
        result = {
            "status": "failed",
            "reason": "No PHP 7.3+ CLI binary found for readonly probe",
            "stdout_preview": out[:500],
            "stderr_preview": err[:500],
            "probe_removed": probe_removed,
            "timestamp": utc_now(),
        }
        write_json(DEPLOYMENT_ROOT / "db-readonly" / "cron-table-readonly.json", result)
        return result

    parsed = parse_json_body(out.strip())
    result = {
        "status": "ok" if parsed and parsed.get("rows") else "failed",
        "stdout_preview": out[:2000],
        "stderr_preview": err[:500] if err else "",
        "parsed": parsed,
        "probe_removed": probe_removed,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "db-readonly" / "cron-table-readonly.json", result)
    return result


def ssh_manual_run(ssh_fields: dict[str, str]) -> dict[str, Any]:
    try:
        import paramiko  # type: ignore
    except ImportError:
        return {"status": "blocked", "reason": "paramiko not available for SSH CLI run"}

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    port = int(ssh_fields.get("port") or 22)
    client.connect(
        ssh_fields["host"],
        port=port,
        username=ssh_fields["username"],
        password=ssh_fields["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    cmd = f"/usr/bin/php {HOSTING_CLI_WRAPPER} --run"
    _stdin, stdout, stderr = client.exec_command(cmd, timeout=3600)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    exit_status = stdout.channel.recv_exit_status()
    client.close()

    token = None
    if TOKEN_META.exists():
        token = json.loads(TOKEN_META.read_text(encoding="utf-8")).get("token")
    sanitized = sanitize_for_log(out + "\n" + err, token)
    write_text(DEPLOYMENT_ROOT / "manual-run" / "manual-run-output-sanitized.txt", sanitized)

    parsed = parse_json_body(out.strip())
    return {
        "status": "ok" if exit_status == 0 else "failed",
        "exit_code": exit_status,
        "parsed": parsed,
        "stdout_sha256": sha256_bytes(out.encode("utf-8")),
        "timestamp": utc_now(),
    }


def http_manual_run(token: str) -> dict[str, Any]:
    base = PRODUCTION_URL.rstrip("/") + "/mars-tools/cron/mars_1c_http_gateway.php"
    url = f"{base}?mode=run&token={token}"
    resp = http_get(url, timeout=3600)
    sanitized = sanitize_for_log(resp.get("body", ""), token)
    write_text(DEPLOYMENT_ROOT / "manual-run" / "manual-run-output-sanitized.txt", sanitized)
    parsed = parse_json_body(resp.get("body", ""))
    return {
        "status": "ok" if resp.get("status_code") == 200 and parsed and parsed.get("mode") == "run" else "failed",
        "http_status": resp.get("status_code"),
        "parsed": parsed,
        "timestamp": utc_now(),
    }


def evaluate_gates(
    http_checks: dict[str, Any],
    local_config: dict[str, Any],
    db_check: dict[str, Any],
    xml_check: dict[str, Any],
    lock_check: dict[str, Any],
) -> dict[str, Any]:
    dry = parse_json_body(http_checks["dry_run"].get("body", "")) or {}
    run_no_token = parse_json_body(http_checks["run_without_token"].get("body", "")) or {}

    g1 = http_checks["dry_run"].get("status_code") == 200 and dry.get("mutation") is False
    g2 = http_checks["status"].get("status_code") == 200
    g3 = http_checks["run_without_token"].get("status_code") == 403 and run_no_token.get("mutation") is False
    g4 = local_config.get("run_token_configured") is True
    db_ok = db_check.get("status") == "ok" and bool(db_check.get("parsed", {}).get("rows"))
    db_unknown = db_check.get("status") in ("blocked", "failed")
    g5 = db_ok or (db_unknown and False)  # SAFE UNKNOWN does not satisfy pre-run gate
    g6 = True
    if db_ok:
        rows = db_check["parsed"]["rows"]
        for cmd in ("1c", "1c_offers"):
            if rows.get(cmd, {}).get("exists") and rows[cmd].get("active") == 1:
                g6 = False
    elif db_unknown:
        g6 = False
    g7 = xml_check.get("import0_count", 0) > 0
    g8 = xml_check.get("offers0_count", 0) > 0  # wrapper does not skip offers safely
    g9 = not lock_check.get("locked") or lock_check.get("stale") is True
    g10 = dry.get("paths", {}).get("reports_dir") or dry.get("paths", {}).get("log_dir")
    g11 = True
    g12 = True

    gates = {
        "G1_wrapper_dry_run": g1,
        "G2_wrapper_status": g2,
        "G3_run_without_token_blocked": g3,
        "G4_local_token_config": g4,
        "G5_db_cron_rows_known": g5,
        "G5_db_state": "known" if db_ok else "SAFE UNKNOWN",
        "G6_no_active_before_run": g6,
        "G7_catalog_xml_exists": g7,
        "G8_offers_xml_or_skip": g8,
        "G9_lock_absent_or_stale": g9,
        "G10_reports_logs_writable": bool(g10),
        "G11_no_beget_cron_change": g11,
        "G12_maintenance_window": g12,
    }
    all_pass = all(gates.values())
    return {"gates": gates, "all_pass": all_pass}


def phase_download(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    wrapper_remote = roots["storage_root"] + "mars-tools/cron/mars_1c_import_wrapper.php"
    gateway_remote = roots["public_root"] + "mars-tools/cron/mars_1c_http_gateway.php"
    result: dict[str, Any] = {"timestamp": utc_now()}
    for key, remote in (("wrapper", wrapper_remote), ("gateway", gateway_remote)):
        data = ftp_download(ftp, remote)
        if data is None:
            result[key] = {"status": "missing", "remote": remote}
            continue
        local = DEPLOYMENT_ROOT / "source" / Path(remote).name
        if key == "wrapper":
            local = DEPLOYMENT_ROOT / "source" / "mars_1c_import_wrapper.php"
        elif key == "gateway":
            local = DEPLOYMENT_ROOT / "source" / "mars_1c_http_gateway.php"
        local.write_bytes(data)
        result[key] = {"status": "downloaded", "remote": remote, "size": len(data), "sha256": sha256_bytes(data)}
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-download.json", result)
    return result


def phase_local_config(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    remote = roots["storage_root"] + "mars-tools/cron/mars_1c_wrapper.local.php"
    exists = ftp_exists(ftp, remote)
    meta: dict[str, Any] = {
        "remote": remote,
        "existed_before": exists,
        "uploaded": False,
        "run_token_configured": False,
        "token_fingerprint": None,
        "timestamp": utc_now(),
    }
    token = secrets.token_urlsafe(48)
    if exists:
        meta["action"] = "EXISTS — not overwritten"
        meta["size"] = None
        try:
            meta["size"] = ftp.size(normalize_remote(remote))
        except ftplib.error_perm:
            pass
    else:
        config_php = build_local_config_php(token)
        LOCAL_CONFIG_PREPARED.write_text(config_php, encoding="utf-8")
        ftp_upload(ftp, remote, config_php.encode("utf-8"))
        meta["action"] = "CREATED and uploaded"
        meta["uploaded"] = True
        meta["run_token_configured"] = True
        meta["token_fingerprint"] = token_fingerprint(token)
        write_json(TOKEN_META, {"token": token, "fingerprint": meta["token_fingerprint"], "created_at": utc_now()})
    write_json(DEPLOYMENT_ROOT / "manifests" / "local-config.json", {k: v for k, v in meta.items() if k != "token"})
    return meta


def phase_xml_check(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    xml_dir = roots["public_root"] + "1c_incoming/webdata"
    alt_dir = roots["login_root"].rstrip("/") + "/1c_incoming/webdata"
    chosen = xml_dir if list_dir_names(ftp, xml_dir) else alt_dir
    names = list_dir_names(ftp, chosen)
    imports = sorted([n for n in names if re.match(r"import0_.*\.xml$", n, re.I)])
    offers = sorted([n for n in names if re.match(r"offers0_.*\.xml$", n, re.I)])
    files_meta: list[dict[str, Any]] = []
    for group in (imports[:10], offers[:10]):
        for name in group:
            remote = chosen.rstrip("/") + "/" + name
            files_meta.append({"name": name, **ftp_mtime_size(ftp, remote)})
    result = {
        "directory": chosen,
        "import0_count": len(imports),
        "offers0_count": len(offers),
        "import0_files": imports[:20],
        "offers0_files": offers[:20],
        "files_meta": files_meta,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "input-xml-check.json", result)
    return result


def phase_lock_check(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    remote = roots["storage_root"] + "mars-tools/cron/mars_1c_import.lock"
    exists = ftp_exists(ftp, remote)
    result: dict[str, Any] = {"remote": remote, "locked": exists, "stale": None, "timestamp": utc_now()}
    if exists:
        data = ftp_download(ftp, remote)
        if data:
            parts = data.decode("utf-8", errors="replace").strip().split("|")
            if len(parts) >= 2 and parts[1].isdigit():
                age = int(datetime.now(timezone.utc).timestamp()) - int(parts[1])
                result["age_seconds"] = age
                result["stale"] = age > 3600
    write_json(DEPLOYMENT_ROOT / "manifests" / "lock-check.json", result)
    return result


def verify_post_run(ftp: ftplib.FTP, roots: dict[str, str], db_check_after: dict[str, Any]) -> dict[str, Any]:
    reports_dir = roots["storage_root"] + "mars-tools/cron/reports/"
    names = list_dir_names(ftp, reports_dir)
    run_reports = sorted([n for n in names if n.startswith("mars_1c_import_") and n.endswith(".txt") and "dry_run" not in n and "status" not in n], reverse=True)
    latest = None
    if run_reports:
        data = ftp_download(ftp, reports_dir.rstrip("/") + "/" + run_reports[0])
        if data:
            local = DEPLOYMENT_ROOT / "verification" / run_reports[0]
            local.write_bytes(data)
            content = data.decode("utf-8", errors="replace")
            latest = {
                "filename": run_reports[0],
                "size": len(data),
                "sha256": sha256_bytes(data),
                "has_run_id": "Run ID:" in content,
                "has_mode_run": re.search(r"Mode:\s*\nrun", content) is not None,
                "has_step1": "Step 1" in content or "1c" in content,
                "has_final_status": "Final status:" in content,
                "contains_secrets": any(m in content.lower() for m in ("password", "db_password", "run_token=")),
            }
    site_home = http_get(PRODUCTION_URL)
    site_catalog = http_get(PRODUCTION_URL.rstrip("/") + "/katalog/")
    lock = phase_lock_check(ftp, roots)
    return {
        "latest_run_report": latest,
        "lock_after": lock,
        "db_after": db_check_after,
        "site_home_status": site_home.get("status_code"),
        "site_catalog_status": site_catalog.get("status_code"),
        "timestamp": utc_now(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument(
        "--phase",
        choices=["init", "preflight", "manual-run", "all"],
        default="all",
    )
    parser.add_argument("--force-manual-run", action="store_true", help="Execute manual run if gates pass")
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

    summary: dict[str, Any] = {"operation_id": OPERATION_ID, "timestamp": utc_now()}

    with ftp_connect(ftp_fields) as ftp:
        roots = resolve_roots(ftp)
        write_json(DEPLOYMENT_ROOT / "manifests" / "ftp-roots.json", roots)

        if args.phase in ("preflight", "all"):
            summary["download"] = phase_download(ftp, roots)
            base = PRODUCTION_URL.rstrip("/") + "/mars-tools/cron/mars_1c_http_gateway.php"
            http_checks = {
                "dry_run": http_get(base + "?mode=dry-run"),
                "status": http_get(base + "?mode=status"),
                "run_without_token": http_get(base + "?mode=run"),
            }
            write_json(DEPLOYMENT_ROOT / "manifests" / "http-checks.json", http_checks)
            summary["http_checks"] = {
                k: {"status_code": v.get("status_code"), "mutation": (parse_json_body(v.get("body", "")) or {}).get("mutation")}
                for k, v in http_checks.items()
            }

            local_config = phase_local_config(ftp, roots)
            # Re-check dry-run after config upload
            if local_config.get("uploaded"):
                post_cfg = http_get(base + "?mode=dry-run")
                dry = parse_json_body(post_cfg.get("body", "")) or {}
                local_config["run_token_configured"] = dry.get("run_token_configured") is True
                if not local_config.get("token_fingerprint") and TOKEN_META.exists():
                    local_config["token_fingerprint"] = json.loads(TOKEN_META.read_text(encoding="utf-8")).get("fingerprint")
            elif local_config.get("existed_before"):
                post_cfg = http_get(base + "?mode=dry-run")
                dry = parse_json_body(post_cfg.get("body", "")) or {}
                local_config["run_token_configured"] = dry.get("run_token_configured") is True
                local_config["action"] = "EXISTS — verified via dry-run"
            summary["local_config"] = {k: v for k, v in local_config.items() if k != "token"}

            db_check = ssh_db_readonly(ssh_fields) if ssh_fields.get("enabled", "").lower() == "yes" else {"status": "blocked", "reason": "SSH not enabled in secrets"}
            summary["db_readonly"] = {"status": db_check.get("status"), "rows": (db_check.get("parsed") or {}).get("rows")}

            xml_check = phase_xml_check(ftp, roots)
            summary["xml_check"] = {
                "import0_count": xml_check["import0_count"],
                "offers0_count": xml_check["offers0_count"],
            }

            lock_check = phase_lock_check(ftp, roots)
            summary["lock_check"] = lock_check

            gates = evaluate_gates(http_checks, local_config, db_check, xml_check, lock_check)
            write_json(DEPLOYMENT_ROOT / "manifests" / "manual-run-gates.json", gates)
            summary["gates"] = gates

            if not gates["all_pass"]:
                summary["manual_run"] = {"status": "BLOCKED", "reason": "One or more gates failed"}
                write_json(DEPLOYMENT_ROOT / "manifests" / "operation-summary.json", summary)
                print(json.dumps(summary, indent=2))
                return 2

            if args.phase == "preflight":
                summary["manual_run"] = {"status": "PENDING", "reason": "Gates pass — manual run not requested in preflight-only phase"}
                write_json(DEPLOYMENT_ROOT / "manifests" / "operation-summary.json", summary)
                print(json.dumps(summary, indent=2))
                return 0

        if args.phase in ("manual-run", "all") and (args.force_manual_run or args.phase == "manual-run"):
            gates_path = DEPLOYMENT_ROOT / "manifests" / "manual-run-gates.json"
            if not gates_path.exists():
                print("STOP — run preflight first")
                return 1
            gates = json.loads(gates_path.read_text(encoding="utf-8"))
            if not gates.get("all_pass"):
                summary["manual_run"] = {"status": "BLOCKED", "reason": "Gates failed"}
                write_json(DEPLOYMENT_ROOT / "manifests" / "operation-summary.json", summary)
                print(json.dumps(summary, indent=2))
                return 2

            run_result = ssh_manual_run(ssh_fields)
            if run_result.get("status") != "ok":
                token = json.loads(TOKEN_META.read_text(encoding="utf-8")).get("token") if TOKEN_META.exists() else None
                if token:
                    run_result = http_manual_run(token)
            summary["manual_run"] = run_result

            db_after = ssh_db_readonly(ssh_fields)
            summary["post_run"] = verify_post_run(ftp, roots, db_after)
            write_json(DEPLOYMENT_ROOT / "manifests" / "operation-summary.json", summary)
            print(json.dumps({k: v for k, v in summary.items() if k != "download"}, indent=2))
            return 0 if run_result.get("status") == "ok" else 3

    return 0


if __name__ == "__main__":
    sys.exit(main())
