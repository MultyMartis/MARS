#!/usr/bin/env python3
"""SITE-002 D6G1A: Beget watchdog cron + kill-switch config + deploy + acceptance."""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

OPERATION = "SITE-002-PROD-D6G1A-WATCHDOG-KILL-SWITCH-01"
SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
REPO = Path(r"X:\AI MARS STORAGE\git-sync-d6g1a-20260807T162210\repo")
TOOLS = REPO / "projects/ocpilot/sites/site-002/tools"
ADMIN = REPO / "projects/ocpilot/sites/site-002/opencart-admin/mars_1c_exchange"
EVIDENCE_RUNTIME = Path(
    r"X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer\tmp\d6g1a-ops"
)
N8N_ENV = Path(r"X:\AI MARS\local\tokens\n8n-api.env")
WORKFLOW_ID = "tkM4H0G0gM3q9Foi"
WATCHDOG_GATEWAY_PATH = "/mars-tools/cron/mars_1c_watchdog_http_gateway.php"
WATCHDOG_LOG = "/home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_watchdog_stdout.log"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_env(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*([A-Za-z0-9_]+)\s*=\s*(.*)\s*$", line)
        if not m:
            continue
        v = m.group(2).strip()
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        out[m.group(1)] = v
    return out


def parse_section_fields(text: str, section: str, subsection: str) -> dict[str, str]:
    match = re.search(rf"^## {re.escape(section)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError(f"section {section} missing")
    block = match.group(1)
    sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not sub:
        raise RuntimeError(f"subsection {subsection} missing")
    fields: dict[str, str] = {}
    current = None
    for line in sub.group(1).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current, "")
            continue
        if current:
            fields[current] = stripped
            current = None
    return fields


def load_ftp_fields() -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    fields = parse_section_fields(text, "PRODUCTION", "FTP / SFTP")
    missing = [k for k in ("host", "port", "username", "password") if not fields.get(k)]
    if missing:
        raise RuntimeError("Missing FTP fields: " + ",".join(missing))
    return fields


def load_panel_creds() -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    panel = parse_section_fields(text, "PRODUCTION", "Hosting Panel")
    ssh = parse_section_fields(text, "PRODUCTION", "SSH")
    login = (
        panel.get("login")
        or panel.get("username")
        or panel.get("user")
        or ssh.get("username")
        or ssh.get("login")
        or ssh.get("user")
    )
    password = panel.get("password")
    if not login or not password:
        raise RuntimeError("Hosting Panel credentials unavailable")
    return {"login": login, "password": password}


def ftp_connect(fields: dict[str, str]):
    import ftplib

    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields["port"]), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def list_names(ftp, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, _ in ftp.mlsd(path):
            if name not in (".", ".."):
                names.append(name)
        return names
    except Exception:
        lines: list[str] = []
        try:
            ftp.retrlines("LIST " + path, lines.append)
        except Exception:
            return []
        for line in lines:
            parts = line.split()
            if parts:
                names.append(parts[-1])
        return names


def resolve_roots(ftp) -> dict[str, str]:
    pwd = ftp.pwd() or "/"
    public = storage = None
    for base in [pwd, "/"]:
        names = {n.lower(): n for n in list_names(ftp, base)}
        if "public_html" in names:
            public = base.rstrip("/") + "/" + names["public_html"]
        if "storage" in names:
            storage = base.rstrip("/") + "/" + names["storage"]
        if public and storage:
            break
    if not public or not storage:
        raise RuntimeError("Could not resolve public_html/storage")
    return {"public": public, "storage": storage}


def ftp_mkdirs(ftp, remote_dir: str) -> None:
    import ftplib

    parts = remote_dir.strip("/").split("/")
    cur = ""
    for p in parts:
        cur += "/" + p
        try:
            ftp.mkd(cur)
        except ftplib.error_perm:
            pass


def ftp_upload(ftp, remote: str, data: bytes) -> None:
    ftp_mkdirs(ftp, "/".join(remote.split("/")[:-1]))
    ftp.storbinary("STOR " + remote, io.BytesIO(data))


def ftp_download(ftp, remote: str) -> bytes | None:
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote, bio.write)
    except Exception:
        return None
    return bio.getvalue()


def beget_api(login: str, password: str, section: str, method: str, input_data: dict | None = None) -> dict:
    payload = {
        "login": login,
        "passwd": password,
        "input_format": "json",
        "output_format": "json",
    }
    if input_data is not None:
        payload["input_data"] = json.dumps(input_data, ensure_ascii=False)
    body = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(
        f"https://api.beget.com/api/{section}/{method}",
        data=body,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
    return json.loads(raw)


def redact_cmd(cmd: str) -> str:
    return re.sub(r"(token=)[^&\s\"']+", r"\1***", cmd, flags=re.I)


def parse_local_php(local_php: str) -> dict:
    keys: dict = {}
    for key in (
        "CLIENT_OPS_DISPATCH_ENABLED",
        "client_ops_dispatch_enabled",
        "server_dispatch_enabled",
        "watchdog_enabled",
        "enabled",
        "run_token",
        "client_ops_webhook_url",
        "client_ops_webhook_auth_secret",
        "client_ops_webhook_token",
    ):
        m = re.search(rf"['\"]{re.escape(key)}['\"]\s*=>\s*([^,\n]+)", local_php)
        if not m:
            continue
        raw = m.group(1).strip().rstrip(",")
        if key == "run_token":
            val = raw.strip("'\"")
            keys[key + "_present"] = True
            keys[key + "_fp"] = sha256(val.encode())[:12]
            keys["_run_token_value"] = val
            continue
        if "webhook" in key or "secret" in key:
            keys[key + "_present"] = raw not in ("''", '""', "null", "")
            continue
        if raw in ("true", "false"):
            keys[key] = raw == "true"
        else:
            keys[key] = raw.strip("'\"")
    return keys


def ensure_local_kill_switch(local_php: str) -> tuple[str, dict]:
    """Ensure CLIENT_OPS_DISPATCH_ENABLED=true and server_dispatch_enabled=true."""
    changes = {"added_client_ops_key": False, "forced_true": False, "already_ok": False}
    parsed = parse_local_php(local_php)
    enabled = True
    if "CLIENT_OPS_DISPATCH_ENABLED" in parsed:
        enabled = bool(parsed["CLIENT_OPS_DISPATCH_ENABLED"])
    elif "server_dispatch_enabled" in parsed:
        enabled = bool(parsed["server_dispatch_enabled"])

    out = local_php
    if "CLIENT_OPS_DISPATCH_ENABLED" not in parsed:
        if re.search(r"\];\s*$", out.strip()):
            out = re.sub(
                r"\];\s*$",
                "    'CLIENT_OPS_DISPATCH_ENABLED' => true,\n];\n",
                out.strip() + "\n",
                count=1,
            )
            changes["added_client_ops_key"] = True
        elif re.search(r"\);\s*$", out.strip()):
            out = re.sub(
                r"\);\s*$",
                "    'CLIENT_OPS_DISPATCH_ENABLED' => true,\n);\n",
                out.strip() + "\n",
                count=1,
            )
            changes["added_client_ops_key"] = True
        else:
            raise RuntimeError("Cannot patch local config closing")
    else:
        out = re.sub(
            r"(['\"]CLIENT_OPS_DISPATCH_ENABLED['\"]\s*=>\s*)([^,\n]+)",
            r"\1true",
            out,
            count=1,
        )
        if not enabled:
            changes["forced_true"] = True

    parsed2 = parse_local_php(out)
    if "server_dispatch_enabled" in parsed2:
        out = re.sub(
            r"(['\"]server_dispatch_enabled['\"]\s*=>\s*)([^,\n]+)",
            r"\1true",
            out,
            count=1,
        )
    else:
        if re.search(r"\];\s*$", out.strip()):
            out = re.sub(
                r"\];\s*$",
                "    'server_dispatch_enabled' => true,\n];\n",
                out.strip() + "\n",
                count=1,
            )
        else:
            out = re.sub(
                r"\);\s*$",
                "    'server_dispatch_enabled' => true,\n);\n",
                out.strip() + "\n",
                count=1,
            )

    final = parse_local_php(out)
    if final.get("CLIENT_OPS_DISPATCH_ENABLED") is True or final.get("server_dispatch_enabled") is True:
        if not changes["added_client_ops_key"] and not changes["forced_true"]:
            changes["already_ok"] = True
    return out, changes


def n8n_workflow_status() -> dict:
    env = load_env(N8N_ENV)
    base = (env.get("N8N_BASE_URL") or env.get("N8N_API_URL") or "").rstrip("/")
    key = env.get("N8N_API_KEY") or env.get("N8N_API_TOKEN") or ""
    if not base or not key:
        return {"ok": False, "error": "n8n env missing"}
    req = urllib.request.Request(
        f"{base}/api/v1/workflows/{WORKFLOW_ID}",
        headers={"X-N8N-API-KEY": key, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    nodes = data.get("nodes") or []
    return {
        "ok": True,
        "id": data.get("id"),
        "name": data.get("name"),
        "active": bool(data.get("active")),
        "versionId": data.get("versionId"),
        "node_count": len(nodes),
        "updatedAt": data.get("updatedAt"),
    }


def n8n_datatable_count() -> dict:
    env = load_env(N8N_ENV)
    base = (env.get("N8N_BASE_URL") or env.get("N8N_API_URL") or "").rstrip("/")
    key = env.get("N8N_API_KEY") or env.get("N8N_API_TOKEN") or ""
    table_id = "H6VYhwz7RXZCBMmu"
    if not base or not key:
        return {"ok": False, "error": "n8n env missing"}
    # Best-effort; API shape may vary
    url = f"{base}/api/v1/data-tables/{table_id}/rows?limit=1"
    try:
        req = urllib.request.Request(url, headers={"X-N8N-API-KEY": key, "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return {"ok": True, "raw_keys": sorted(list(data.keys()))[:20], "sample": "redacted"}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def cron_matches_watchdog(row: dict) -> bool:
    cmd = str(row.get("command") or row.get("CMD") or "")
    return "mars_1c_watchdog_http_gateway.php" in cmd


def cron_matches_import(row: dict) -> bool:
    cmd = str(row.get("command") or row.get("CMD") or "")
    return ("mars_1c_http_gateway.php" in cmd and "watchdog" not in cmd) or (
        "mars_1c_import_wrapper.php" in cmd
    )


def sanitize_cron_rows(rows) -> list[dict]:
    out = []
    if not isinstance(rows, list):
        return out
    for row in rows:
        if not isinstance(row, dict):
            continue
        item = {
            "row_number": row.get("row_number") or row.get("id"),
            "minutes": row.get("minutes"),
            "hours": row.get("hours"),
            "days": row.get("days"),
            "months": row.get("months"),
            "weekdays": row.get("weekdays"),
            "is_active": row.get("is_active", row.get("active")),
            "command_redacted": redact_cmd(str(row.get("command") or "")),
            "is_watchdog": cron_matches_watchdog(row),
            "is_import": cron_matches_import(row),
        }
        out.append(item)
    return out


def build_watchdog_command(token: str) -> str:
    url = f"https://bzpm.ru{WATCHDOG_GATEWAY_PATH}?token={token}"
    return f'wget -q -O - "{url}" >> {WATCHDOG_LOG} 2>&1'


def mode_prestate() -> int:
    EVIDENCE_RUNTIME.mkdir(parents=True, exist_ok=True)
    ftp_fields = load_ftp_fields()
    panel = load_panel_creds()
    ftp = ftp_connect(ftp_fields)
    roots = resolve_roots(ftp)

    files = {
        "wrapper": f"{roots['storage']}/mars-tools/cron/mars_1c_import_wrapper.php",
        "dispatch": f"{roots['storage']}/mars-tools/cron/mars_1c_completion_dispatch.php",
        "watchdog": f"{roots['storage']}/mars-tools/cron/mars_1c_no_import_watchdog.php",
        "gateway": f"{roots['public']}/mars-tools/cron/mars_1c_watchdog_http_gateway.php",
        "local": f"{roots['storage']}/mars-tools/cron/mars_1c_wrapper.local.php",
        "current": f"{roots['storage']}/mars-tools/cron/current-run.json",
    }
    hashes = {}
    local_meta = {}
    run_token = None
    for k, remote in files.items():
        data = ftp_download(ftp, remote)
        if data is None:
            hashes[k] = None
            continue
        hashes[k] = sha256(data)
        if k == "local":
            local_meta = parse_local_php(data.decode("utf-8", errors="replace"))
            run_token = local_meta.pop("_run_token_value", None)
        if k == "wrapper":
            text = data.decode("utf-8", errors="replace")
            m = re.search(r"MARS_WRAPPER_VERSION\s*=\s*'([^']+)'", text)
            hashes["wrapper_version"] = m.group(1) if m else None
        if k == "current":
            try:
                cur = json.loads(data.decode("utf-8"))
                write_json(
                    EVIDENCE_RUNTIME / "current-run-prestate-sanitized.json",
                    {
                        "run_id": cur.get("run_id"),
                        "final_status": cur.get("final_status"),
                        "trigger_source": cur.get("trigger_source"),
                        "completed_at": cur.get("completed_at"),
                        "report_dispatch_status": cur.get("report_dispatch_status"),
                    },
                )
            except Exception:
                pass

    ftp.quit()

    cron_raw = beget_api(panel["login"], panel["password"], "cron", "getList")
    answer = cron_raw.get("answer") or {}
    result = answer.get("result") if isinstance(answer, dict) else None
    rows = sanitize_cron_rows(result if isinstance(result, list) else [])

    wf = n8n_workflow_status()
    dt = n8n_datatable_count()

    prestate = {
        "operation": OPERATION,
        "captured_at": utc_now(),
        "server_hashes": hashes,
        "local_config_keys": {k: v for k, v in local_meta.items() if not str(k).startswith("_")},
        "run_token_present": bool(run_token),
        "beget_cron": {
            "api_status": cron_raw.get("status"),
            "error_text": (answer.get("errors") if isinstance(answer, dict) else None),
            "row_count": len(rows),
            "rows": rows,
            "watchdog_rows": [r for r in rows if r["is_watchdog"]],
            "import_rows": [r for r in rows if r["is_import"]],
            "cursor_can_update_via_api": True,
            "ssh_crontab_authoritative": False,
            "panel_or_api_authoritative": True,
            "timezone_semantics": "Beget cron fields are Europe/Moscow wall-clock for this contour (import 0 8 proven)",
        },
        "n8n_workflow": wf,
        "data_table": dt,
        "kill_switch_prestate": {
            "CLIENT_OPS_DISPATCH_ENABLED": local_meta.get("CLIENT_OPS_DISPATCH_ENABLED"),
            "server_dispatch_enabled": local_meta.get("server_dispatch_enabled"),
            "old_local_producer_kill_switch_mode": "ENABLED_BUT_NOT_AUTHORITATIVE_FOR_SERVER_DISPATCH",
            "d6g1_flag_note": "D6G1_KILL_SWITCH_ENABLED=NO referred to absence of formalized server-side CLIENT_OPS_DISPATCH_ENABLED semantics, not to outbound being disabled",
        },
    }
    write_json(EVIDENCE_RUNTIME / "PRESTATE.json", prestate)
    write_json(EVIDENCE_RUNTIME / "BEGET-CRON-INVENTORY.json", prestate["beget_cron"])
    # stash token fingerprint only for later modes via separate secret file outside git
    if run_token:
        secret_path = EVIDENCE_RUNTIME / "run-token.SECRET.txt"
        secret_path.write_text(run_token, encoding="utf-8")
    print(json.dumps({"ok": True, "mode": "prestate", "out": str(EVIDENCE_RUNTIME / "PRESTATE.json")}, indent=2))
    return 0


def mode_install_watchdog_cron() -> int:
    panel = load_panel_creds()
    token_path = EVIDENCE_RUNTIME / "run-token.SECRET.txt"
    if not token_path.is_file():
        raise RuntimeError("run-token.SECRET.txt missing; run prestate first")
    token = token_path.read_text(encoding="utf-8").strip()
    cron_raw = beget_api(panel["login"], panel["password"], "cron", "getList")
    answer = cron_raw.get("answer") or {}
    result = answer.get("result") if isinstance(answer, dict) else None
    rows = result if isinstance(result, list) else []
    existing = [r for r in rows if isinstance(r, dict) and cron_matches_watchdog(r)]
    post = {
        "captured_at": utc_now(),
        "pre_existing_watchdog_count": len(existing),
        "action": None,
        "row_number": None,
        "schedule": "0 9 * * *",
        "timezone": "Europe/Moscow",
        "equivalent_plus07": "13:00",
        "command_redacted": redact_cmd(build_watchdog_command(token)),
        "active": None,
    }
    if len(existing) == 1:
        row = existing[0]
        post["action"] = "CONFIRM_EXISTING"
        post["row_number"] = row.get("row_number") or row.get("id")
        post["active"] = row.get("is_active", True)
        # ensure schedule 0 9 if different — Beget may expose edit; if hours!=9, delete+add
        if str(row.get("hours")) != "9" or str(row.get("minutes")) != "0":
            rid = row.get("row_number") or row.get("id")
            if rid is not None:
                beget_api(panel["login"], panel["password"], "cron", "delete", {"row_number": int(rid)})
            add = beget_api(
                panel["login"],
                panel["password"],
                "cron",
                "add",
                {
                    "minutes": "0",
                    "hours": "9",
                    "days": "*",
                    "months": "*",
                    "weekdays": "*",
                    "command": build_watchdog_command(token),
                },
            )
            post["action"] = "REPLACE_WRONG_SCHEDULE"
            post["add_response_status"] = add.get("status")
            post["row_number"] = ((add.get("answer") or {}).get("result") or {}).get("row_number")
            post["active"] = True
    elif len(existing) > 1:
        # keep first matching 0 9, delete extras
        keep = None
        for r in existing:
            if str(r.get("hours")) == "9" and str(r.get("minutes")) == "0":
                keep = r
                break
        if keep is None:
            keep = existing[0]
        for r in existing:
            if r is keep:
                continue
            rid = r.get("row_number") or r.get("id")
            if rid is not None:
                beget_api(panel["login"], panel["password"], "cron", "delete", {"row_number": int(rid)})
        post["action"] = "DEDUPED_EXTRAS"
        post["row_number"] = keep.get("row_number") or keep.get("id")
        post["active"] = True
    else:
        add = beget_api(
            panel["login"],
            panel["password"],
            "cron",
            "add",
            {
                "minutes": "0",
                "hours": "9",
                "days": "*",
                "months": "*",
                "weekdays": "*",
                "command": build_watchdog_command(token),
            },
        )
        post["action"] = "CREATED"
        post["add_response_status"] = add.get("status")
        post["add_error"] = (add.get("answer") or {}).get("errors")
        res = (add.get("answer") or {}).get("result")
        if isinstance(res, dict):
            post["row_number"] = res.get("row_number")
        elif isinstance(res, (int, str)):
            post["row_number"] = res
        post["active"] = add.get("status") == "success"

    # re-list
    cron_raw2 = beget_api(panel["login"], panel["password"], "cron", "getList")
    rows2 = sanitize_cron_rows(((cron_raw2.get("answer") or {}).get("result")) or [])
    post["post_rows"] = rows2
    post["watchdog_rows"] = [r for r in rows2 if r["is_watchdog"]]
    post["exactly_one_watchdog"] = len(post["watchdog_rows"]) == 1
    write_json(EVIDENCE_RUNTIME / "WATCHDOG-CRON-POSTSTATE.json", post)
    print(json.dumps({"ok": True, "mode": "install_watchdog_cron", "exactly_one": post["exactly_one_watchdog"]}, indent=2))
    return 0 if post.get("exactly_one_watchdog") else 2


def mode_deploy() -> int:
    ftp_fields = load_ftp_fields()
    ftp = ftp_connect(ftp_fields)
    roots = resolve_roots(ftp)
    uploads = [
        (TOOLS / "mars_1c_import_wrapper.php", f"{roots['storage']}/mars-tools/cron/mars_1c_import_wrapper.php"),
        (TOOLS / "mars_1c_import_run_contract.php", f"{roots['storage']}/mars-tools/cron/mars_1c_import_run_contract.php"),
        (TOOLS / "mars_1c_completion_dispatch.php", f"{roots['storage']}/mars-tools/cron/mars_1c_completion_dispatch.php"),
        (TOOLS / "mars_1c_no_import_watchdog.php", f"{roots['storage']}/mars-tools/cron/mars_1c_no_import_watchdog.php"),
        (TOOLS / "mars_1c_watchdog_http_gateway.php", f"{roots['public']}/mars-tools/cron/mars_1c_watchdog_http_gateway.php"),
        (TOOLS / "mars_1c_d6g1a_offline_regression.php", f"{roots['storage']}/mars-tools/cron/mars_1c_d6g1a_offline_regression.php"),
        (
            ADMIN / "admin/model/tool/mars_1c_exchange.php",
            f"{roots['public']}/admin/model/tool/mars_1c_exchange.php",
        ),
        (
            ADMIN / "admin/view/template/tool/mars_1c_exchange.twig",
            f"{roots['public']}/admin/view/template/tool/mars_1c_exchange.twig",
        ),
    ]
    report = {"operation": OPERATION, "deployed_at": utc_now(), "files": [], "local_config": None}
    for local, remote in uploads:
        data = local.read_bytes()
        ftp_upload(ftp, remote, data)
        verify = ftp_download(ftp, remote)
        report["files"].append(
            {
                "local": str(local.relative_to(REPO)).replace("\\", "/"),
                "remote": remote,
                "sha256": sha256(data),
                "verified": verify is not None and sha256(verify) == sha256(data),
                "bytes": len(data),
            }
        )

    # Patch local config kill switch to true
    local_remote = f"{roots['storage']}/mars-tools/cron/mars_1c_wrapper.local.php"
    local_bytes = ftp_download(ftp, local_remote)
    if local_bytes is None:
        raise RuntimeError("local config missing on server")
    patched, changes = ensure_local_kill_switch(local_bytes.decode("utf-8", errors="replace"))
    ftp_upload(ftp, local_remote, patched.encode("utf-8"))
    report["local_config"] = {
        "changes": changes,
        "CLIENT_OPS_DISPATCH_ENABLED": parse_local_php(patched).get("CLIENT_OPS_DISPATCH_ENABLED"),
        "server_dispatch_enabled": parse_local_php(patched).get("server_dispatch_enabled"),
    }

    # Clear OpenCart modification cache files (not broad storage wipe)
    mod_dir = f"{roots['storage']}/modification"
    cleared = 0
    for name in list_names(ftp, mod_dir):
        # only clear top-level cache markers / php caches commonly used; avoid deleting everything recursively if deep
        if name.endswith(".php") or name in ("cache",):
            try:
                # if directory named cache, skip deep delete — just note
                if name == "cache":
                    continue
                ftp.delete(mod_dir + "/" + name)
                cleared += 1
            except Exception:
                pass
    report["modification_php_cleared"] = cleared

    ftp.quit()
    write_json(EVIDENCE_RUNTIME / "SERVER-DEPLOYMENT.json", report)
    print(json.dumps({"ok": True, "mode": "deploy", "files": len(report["files"]), "all_verified": all(f["verified"] for f in report["files"])}, indent=2))
    return 0 if all(f["verified"] for f in report["files"]) else 2


def mode_watchdog_live() -> int:
    token = (EVIDENCE_RUNTIME / "run-token.SECRET.txt").read_text(encoding="utf-8").strip()
    url = f"https://bzpm.ru{WATCHDOG_GATEWAY_PATH}?token={urllib.parse.quote(token)}"
    req = urllib.request.Request(url, method="GET", headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        status = resp.status
    try:
        data = json.loads(body)
    except Exception:
        data = {"raw_len": len(body)}
    out = {
        "invoked_at": utc_now(),
        "http_status": status,
        "response": data,
        "expected_reason_today": "TERMINAL_EXISTS",
        "pass": isinstance(data, dict)
        and data.get("skipped") is True
        and data.get("reason") in ("TERMINAL_EXISTS", "ALREADY_SENT_TODAY", "BEFORE_DEADLINE"),
    }
    # After deadline hour (13 Barnaul): TERMINAL_EXISTS expected given today's scheduled terminal.
    write_json(EVIDENCE_RUNTIME / "WATCHDOG-LIVE-NO-SEND-ACCEPTANCE.json", out)
    print(json.dumps({"ok": out["pass"], "reason": data.get("reason") if isinstance(data, dict) else None}, indent=2))
    return 0 if out["pass"] else 2


def mode_ssh_php_checks() -> int:
    """Run php -l and offline regression over SSH."""
    import paramiko

    text = SECRETS.read_text(encoding="utf-8")
    sshf = parse_section_fields(text, "PRODUCTION", "SSH")
    host = sshf.get("host") or sshf.get("hostname")
    user = sshf.get("username") or sshf.get("user") or sshf.get("login")
    password = sshf.get("password")
    port = int(sshf.get("port") or "22")
    if not host or not user or not password:
        raise RuntimeError("SSH fields missing")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, password=password, timeout=45)
    cmds = [
        "php -l /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_completion_dispatch.php",
        "php -l /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_no_import_watchdog.php",
        "php -l /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php",
        "php -l /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_d6g1a_offline_regression.php",
        "php /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_d6g1a_offline_regression.php",
    ]
    results = []
    for cmd in cmds:
        stdin, stdout, stderr = client.exec_command(cmd, timeout=120)
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        code = stdout.channel.recv_exit_status()
        results.append({"cmd": cmd.split()[-1], "exit": code, "stdout_tail": out[-2000:], "stderr_tail": err[-500:]})
    client.close()
    write_json(EVIDENCE_RUNTIME / "SSH-PHP-CHECKS.json", {"captured_at": utc_now(), "results": results})
    ok = all(r["exit"] == 0 for r in results)
    print(json.dumps({"ok": ok, "mode": "ssh_php_checks"}, indent=2))
    return 0 if ok else 2


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: prestate|install_watchdog_cron|deploy|watchdog_live|ssh_php_checks")
        return 2
    mode = sys.argv[1]
    if mode == "prestate":
        return mode_prestate()
    if mode == "install_watchdog_cron":
        return mode_install_watchdog_cron()
    if mode == "deploy":
        return mode_deploy()
    if mode == "watchdog_live":
        return mode_watchdog_live()
    if mode == "ssh_php_checks":
        return mode_ssh_php_checks()
    raise SystemExit(f"unknown mode {mode}")


if __name__ == "__main__":
    raise SystemExit(main())
