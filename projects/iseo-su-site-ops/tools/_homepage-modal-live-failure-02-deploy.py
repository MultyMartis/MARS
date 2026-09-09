#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Backup + scoped deploy for HOMEPAGE-MODAL-LIVE-FAILURE-02."""
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
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_homepage-modal-live-failure-02")
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\homepage-modal-live-failure-02")
OUT = EVIDENCE / "_backup-deploy.json"
UA = "ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02/1.0"

FILES = [
    {
        "local": Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\forms\audit__FORM.php"),
        "remote": f"{DOC}/audit__FORM.php",
        "live_url": None,
        "name": "audit__FORM.php",
    },
    {
        "local": Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js"),
        "remote": f"{DOC}/js/common.js",
        "live_url": f"{SITE}/js/common.js",
        "name": "common.js",
    },
]


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
    report: dict = {"started_utc": utc_now(), "files": []}
    sftp, transport = sftp_connect()
    try:
        for item in FILES:
            local = item["local"].read_bytes()
            remote_before = read_remote_bytes(sftp, item["remote"])
            bak = BAK_ROOT / f"{item['name']}.remote-before.{stamp}"
            bak.write_bytes(remote_before)
            entry = {
                "name": item["name"],
                "local_path": str(item["local"]),
                "remote_path": item["remote"],
                "backup_path": str(bak),
                "local_sha256": sha256_bytes(local),
                "remote_sha256_before": sha256_bytes(remote_before),
            }
            write_remote_bytes(sftp, item["remote"], local)
            remote_after = read_remote_bytes(sftp, item["remote"])
            entry["remote_sha256_after"] = sha256_bytes(remote_after)
            entry["remote_matches_local"] = remote_after == local
            if item["live_url"]:
                live = http_get(f"{item['live_url']}?v={stamp}")
                entry["live_http_sha256"] = sha256_bytes(live)
                entry["live_matches_local"] = live == local
            report["files"].append(entry)
        report["deployed_utc"] = utc_now()
        report["markers"] = {
            "audit_site_optional": b"$site !== \"\" && !iseo_form_is_meaningful($site, 3)"
            in Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\forms\audit__FORM.php").read_bytes(),
            "audit_preventDefault": b'$("#audit__FORM_send").on("click", function(e){'
            in Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js").read_bytes(),
        }
    finally:
        sftp.close()
        transport.close()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
