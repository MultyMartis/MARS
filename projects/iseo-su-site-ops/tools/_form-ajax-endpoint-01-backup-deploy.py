#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-FORM-AJAX-ENDPOINT-01: backup + scoped deploy of js/common.js only."""
from __future__ import annotations

import hashlib
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SITE = "https://i-seo.su"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
REMOTE_JS = f"{DOC}/js/common.js"
LOCAL_JS = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js")
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_form-ajax-endpoint-01")
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-ajax-endpoint-01")
OUT = EVIDENCE / "_backup-deploy.json"
UA = "ISEO-SU-FORM-AJAX-ENDPOINT-01/1.0"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sftp_connect():
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"], password=secrets["ftp_or_sftp_password"]
    )
    return paramiko.SFTPClient.from_transport(transport), transport


def read_remote_bytes(sftp, path: str) -> bytes:
    with sftp.open(path, "r") as f:
        return f.read()


def write_remote_bytes(sftp, path: str, data: bytes) -> None:
    with sftp.open(path, "w") as f:
        f.write(data)


def http_get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    BAK_ROOT.mkdir(parents=True, exist_ok=True)
    stamp = utc_now().replace(":", "")
    local = LOCAL_JS.read_bytes()
    report = {
        "started_utc": utc_now(),
        "local_path": str(LOCAL_JS),
        "local_sha256": sha256_bytes(local),
        "local_len": len(local),
        "seo_handler_root_relative": b"url: '/page__FORM.php'" in local
        and b'$("#page__FORM_send_seo")' in local,
        "relative_page_form_count": local.decode("utf-8", "replace").count("url: 'page__FORM.php'"),
        "root_relative_page_form_count": local.decode("utf-8", "replace").count(
            "url: '/page__FORM.php'"
        ),
    }
    sftp, transport = sftp_connect()
    try:
        before = read_remote_bytes(sftp, REMOTE_JS)
        bak_name = f"common.js.before.{stamp}"
        bak_path = BAK_ROOT / bak_name
        bak_path.write_bytes(before)
        report["backup"] = {
            "absolute_path": str(bak_path),
            "sha256_before": sha256_bytes(before),
            "len_before": len(before),
            "timestamp_utc": utc_now(),
        }
        write_remote_bytes(sftp, REMOTE_JS, local)
        after = read_remote_bytes(sftp, REMOTE_JS)
        report["remote_after"] = {
            "sha256": sha256_bytes(after),
            "len": len(after),
            "matches_local": after == local,
        }
    finally:
        sftp.close()
        transport.close()
    live = http_get(f"{SITE}/js/common.js?v={stamp}")
    report["live_http"] = {
        "sha256": sha256_bytes(live),
        "len": len(live),
        "matches_local": live == local,
        "seo_handler_has_root_relative": b"$(\"#page__FORM_send_seo\")" in live
        and b"url: '/page__FORM.php'" in live,
    }
    report["ended_utc"] = utc_now()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["remote_after"]["matches_local"]:
        raise SystemExit("REMOTE HASH MISMATCH")


if __name__ == "__main__":
    main()
