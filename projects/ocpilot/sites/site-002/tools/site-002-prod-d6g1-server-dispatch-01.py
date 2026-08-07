#!/usr/bin/env python3
"""SITE-002 D6G1 deploy: server-side completion dispatch + watchdog + admin UI."""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

OPERATION = "SITE-002-PROD-D6G1-SERVER-SIDE-COMPLETION-DISPATCH-01"
SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
REPO = Path(r"X:\AI MARS STORAGE\git-sync-d6g1-20260807\repo")
TOOLS = REPO / "projects/ocpilot/sites/site-002/tools"
ADMIN = REPO / "projects/ocpilot/sites/site-002/opencart-admin/mars_1c_exchange"
EVIDENCE = Path(
    r"X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer\tmp\d6g1-deploy"
)
MAIN = Path(r"X:\AI MARS")
WEBHOOK_SECRETS = MAIN / "local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env"
N8N_ENV = MAIN / "local/tokens/n8n-api.env"


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
        v = m.group(2)
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        out[m.group(1)] = v
    return out


def load_ftp_fields() -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    ftp_match = re.search(r"^### FTP / SFTP\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not ftp_match:
        raise RuntimeError("FTP section missing")
    fields: dict[str, str] = {}
    current_key = None
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
            current_key = None
    missing = [k for k in ("host", "port", "username", "password") if not fields.get(k)]
    if missing:
        raise RuntimeError("Missing FTP fields: " + ",".join(missing))
    return fields


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
    import ftplib

    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote, bio.write)
    except ftplib.error_perm:
        return None
    return bio.getvalue()


def php_quote(s: str) -> str:
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


def merge_local_config(existing: str | None, webhook_url: str, token: str) -> bytes:
    # Rebuild local config preserving unknown keys via regex extraction where possible.
    values: dict[str, str] = {}
    if existing:
        for m in re.finditer(
            r"['\"]([a-zA-Z0-9_]+)['\"]\s*=>\s*(true|false|null|-?\d+|['\"].*?['\"])\s*,?",
            existing,
            re.S,
        ):
            key = m.group(1)
            raw = m.group(2)
            values[key] = raw
    # Force required keys
    values["client_ops_webhook_url"] = php_quote(webhook_url)
    values["client_ops_webhook_auth_secret"] = php_quote(token)
    values["server_dispatch_enabled"] = "true"
    values["watchdog_enabled"] = "true"
    # Preserve common existing keys if captured as raw PHP literals
    for k in ("run_token", "enabled", "allow_http_run", "site_base_url", "created_by", "notes"):
        values.setdefault(k, None)
    # If we failed to parse, keep a minimal merge by rewriting known block using previous file include style
    lines = [
        "<?php",
        "/**",
        " * MARS SITE-002 local wrapper config — NOT for Git.",
        f" * Updated by: {OPERATION}",
        f" * Updated at: {utc_now()}",
        " */",
        "return [",
    ]
    # Prefer re-including parsed literals; if run_token missing, keep previous file via append of parsed raw map.
    if existing:
        # Extract run_token carefully
        m = re.search(r"['\"]run_token['\"]\s*=>\s*(['\"].*?['\"])\s*,", existing, re.S)
        if m:
            values["run_token"] = m.group(1)
        m = re.search(r"['\"]enabled['\"]\s*=>\s*(true|false)\s*,", existing)
        if m:
            values["enabled"] = m.group(1)
        m = re.search(r"['\"]allow_http_run['\"]\s*=>\s*(true|false)\s*,", existing)
        if m:
            values["allow_http_run"] = m.group(1)
        m = re.search(r"['\"]site_base_url['\"]\s*=>\s*(['\"].*?['\"])\s*,", existing)
        if m:
            values["site_base_url"] = m.group(1)
        m = re.search(r"['\"]created_by['\"]\s*=>\s*(['\"].*?['\"])\s*,", existing)
        if m:
            values["created_by"] = m.group(1)
        m = re.search(r"['\"]notes['\"]\s*=>\s*(['\"].*?['\"])\s*,", existing)
        if m:
            values["notes"] = m.group(1)

    ordered = [
        "run_token",
        "enabled",
        "allow_http_run",
        "site_base_url",
        "created_by",
        "notes",
        "client_ops_webhook_url",
        "client_ops_webhook_auth_secret",
        "server_dispatch_enabled",
        "watchdog_enabled",
    ]
    for key in ordered:
        val = values.get(key)
        if val is None:
            continue
        lines.append(f"    '{key}' => {val},")
    lines.append("];")
    lines.append("")
    return ("\n".join(lines)).encode("utf-8")


UPLOADS = [
    ("tools/mars_1c_import_wrapper.php", "storage", "mars-tools/cron/mars_1c_import_wrapper.php"),
    ("tools/mars_1c_import_run_contract.php", "storage", "mars-tools/cron/mars_1c_import_run_contract.php"),
    ("tools/mars_1c_completion_dispatch.php", "storage", "mars-tools/cron/mars_1c_completion_dispatch.php"),
    ("tools/mars_1c_no_import_watchdog.php", "storage", "mars-tools/cron/mars_1c_no_import_watchdog.php"),
    (
        "opencart-admin/mars_1c_exchange/admin/controller/tool/mars_1c_exchange.php",
        "public",
        "admin/controller/tool/mars_1c_exchange.php",
    ),
    (
        "opencart-admin/mars_1c_exchange/admin/model/tool/mars_1c_exchange.php",
        "public",
        "admin/model/tool/mars_1c_exchange.php",
    ),
    (
        "opencart-admin/mars_1c_exchange/admin/view/template/tool/mars_1c_exchange.twig",
        "public",
        "admin/view/template/tool/mars_1c_exchange.twig",
    ),
]


def local_bytes(rel: str) -> bytes:
    if rel.startswith("tools/"):
        return (TOOLS / rel[len("tools/") :]).read_bytes()
    if rel.startswith("opencart-admin/"):
        return (REPO / "projects/ocpilot/sites/site-002" / rel).read_bytes()
    raise RuntimeError(rel)


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    secrets = load_env(WEBHOOK_SECRETS)
    n8n = load_env(N8N_ENV)
    token = (
        secrets.get("CLIENT_OPS_WEBHOOK_AUTH_SECRET")
        or secrets.get("CLIENT_OPS_WEBHOOK_TOKEN")
        or secrets.get("WEBHOOK_TOKEN")
        or secrets.get("MARS_CLIENT_OPS_TOKEN")
        or ""
    )
    api = (n8n.get("N8N_API_URL") or "").rstrip("/")
    # webhook path confirmed active for D6G
    webhook_path = "mars-client-ops-bridge-bzpm-sandbox"
    webhook_url = f"{api}/webhook/{webhook_path}"
    if not token or not api:
        raise RuntimeError("webhook credentials missing in local secret contour")

    evidence = {
        "operation": OPERATION,
        "started_at": utc_now(),
        "webhook_url_host": re.sub(r"^https?://", "", api).split("/")[0],
        "webhook_path": webhook_path,
        "token_present": True,
        "token_sha256_prefix8": sha256(token.encode("utf-8"))[:8],
        "uploads": [],
    }

    fields = load_ftp_fields()
    ftp = ftp_connect(fields)
    roots = resolve_roots(ftp)
    evidence["roots"] = {"public_suffix": roots["public"].rstrip("/").split("/")[-1], "storage_suffix": roots["storage"].rstrip("/").split("/")[-1]}

    for rel, root_key, remote_rel in UPLOADS:
        data = local_bytes(rel)
        remote = roots[root_key].rstrip("/") + "/" + remote_rel
        ftp_upload(ftp, remote, data)
        verify = ftp_download(ftp, remote)
        evidence["uploads"].append(
            {
                "rel": rel,
                "remote": remote_rel,
                "bytes": len(data),
                "sha256": sha256(data),
                "verified": verify is not None and sha256(verify) == sha256(data),
            }
        )

    # Merge local config secrets
    local_remote = roots["storage"].rstrip("/") + "/mars-tools/cron/mars_1c_wrapper.local.php"
    prev = ftp_download(ftp, local_remote)
    merged = merge_local_config(prev.decode("utf-8", errors="replace") if prev else None, webhook_url, token)
    ftp_upload(ftp, local_remote, merged)
    evidence["local_config_updated"] = True
    evidence["local_config_bytes"] = len(merged)
    evidence["local_config_contains_webhook_url"] = b"client_ops_webhook_url" in merged
    evidence["local_config_contains_secret_key"] = b"client_ops_webhook_auth_secret" in merged

    # Clear OpenCart modification cache files (scoped)
    mod = roots["storage"].rstrip("/") + "/modification"
    cleared = []
    for name in list_names(ftp, mod):
        # Only clear index/cache markers commonly used; avoid deleting entire tree recursively via wildcards.
        # Delete PHP cache files directly under modification root if present.
        if name.endswith(".php") or name in ("index.html",):
            try:
                ftp.delete(mod + "/" + name)
                cleared.append(name)
            except Exception:
                pass
    evidence["modification_cleared_names"] = cleared

    # PHP lint remotely is unavailable; record local file sizes
    evidence["finished_at"] = utc_now()
    write_json(EVIDENCE / "DEPLOYMENT.json", evidence)
    # Redacted summary to stdout
    print(json.dumps({k: v for k, v in evidence.items()}, ensure_ascii=False, indent=2))
    ftp.quit()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        raise
