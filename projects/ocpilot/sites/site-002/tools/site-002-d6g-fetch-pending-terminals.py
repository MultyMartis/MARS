#!/usr/bin/env python3
"""Fetch pending D6G dispatch-inbox entries and terminal.json from SITE-002 via FTP."""
from __future__ import annotations

import json
import re
import ftplib
from datetime import datetime, timezone
from pathlib import Path

SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
STATE = Path(r"X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer")
OUT = STATE / "import-terminals"
PENDING = OUT / "_pending"


def load_ftp() -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    # Find PRODUCTION FTP block
    m = re.search(r"### FTP / SFTP\s*([\s\S]*?)(?=^### |\Z)", text, re.M)
    if not m:
        raise RuntimeError("FTP section missing")
    fields: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fields[k.strip().lower()] = v.strip().strip("`")
    # normalize keys
    mapping = {
        "host": fields.get("host") or fields.get("ftp host") or fields.get("server"),
        "port": fields.get("port") or "21",
        "username": fields.get("username") or fields.get("user") or fields.get("login"),
        "password": fields.get("password") or fields.get("pass"),
    }
    # try labeled lines like - host: x
    for line in m.group(1).splitlines():
        lm = re.match(r"[-*]\s*(host|port|username|user|login|password|pass)\s*[:=]\s*(.+)$", line.strip(), re.I)
        if lm:
            key = lm.group(1).lower()
            val = lm.group(2).strip().strip("`")
            if key in ("host",):
                mapping["host"] = val
            elif key == "port":
                mapping["port"] = val
            elif key in ("username", "user", "login"):
                mapping["username"] = val
            elif key in ("password", "pass"):
                mapping["password"] = val
    missing = [k for k, v in mapping.items() if not v]
    if missing:
        raise RuntimeError("Missing FTP fields: " + ",".join(missing))
    return mapping


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes | None:
    import io
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote, bio.write)
    except ftplib.error_perm:
        return None
    return bio.getvalue()


def list_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, _facts in ftp.mlsd(path):
            if name not in (".", ".."):
                names.append(name)
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


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    PENDING.mkdir(parents=True, exist_ok=True)
    fields = load_ftp()
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields["port"]), timeout=120)
    ftp.login(fields["username"], fields["password"])
    # discover storage root
    pwd = ftp.pwd() or "/"
    storage = None
    for cand in (pwd.rstrip("/") + "/storage", "/storage", pwd.rstrip("/") + "/bzpm.ru/storage"):
        try:
            ftp.cwd(cand)
            storage = ftp.pwd()
            break
        except Exception:
            continue
    if not storage:
        # try login listing
        for name in list_names(ftp, pwd):
            if name.lower() == "storage":
                storage = (pwd.rstrip("/") + "/" + name)
                break
    if not storage:
        raise RuntimeError("storage root not found")

    inbox = storage.rstrip("/") + "/mars-tools/cron/dispatch-inbox"
    runs = storage.rstrip("/") + "/mars-tools/cron/runs"
    current = storage.rstrip("/") + "/mars-tools/cron/current-run.json"

    cur = ftp_download(ftp, current)
    if cur:
        (OUT / "_current").mkdir(parents=True, exist_ok=True)
        (OUT / "_current" / "run-state.json").write_bytes(cur)

    pending_files = list_names(ftp, inbox) if True else []
    fetched = []
    for name in pending_files:
        if not name.endswith(".json"):
            continue
        data = ftp_download(ftp, inbox.rstrip("/") + "/" + name)
        if not data:
            continue
        try:
            meta = json.loads(data.decode("utf-8"))
        except Exception:
            continue
        run_id = str(meta.get("run_id") or name[:-5])
        term = ftp_download(ftp, runs.rstrip("/") + "/" + run_id + "/terminal.json")
        if not term:
            continue
        dest = OUT / run_id
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "terminal.json").write_bytes(term)
        (dest / "dispatch-meta.json").write_bytes(data)
        (PENDING / f"{run_id}.runid").write_text(run_id + "\n", encoding="utf-8")
        fetched.append(run_id)
        # remove remote inbox marker after local mirror (best-effort)
        try:
            ftp.delete(inbox.rstrip("/") + "/" + name)
        except Exception:
            pass

    ftp.quit()
    summary = {
        "fetched": fetched,
        "count": len(fetched),
        "finished_at": datetime.now(timezone.utc).isoformat(),
    }
    (OUT / "_last_fetch.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
