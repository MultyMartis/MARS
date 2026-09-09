#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Backup and apply proven pf_contact→hidden + pf_phone patch to live authorities only."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
WALK = Path(
    r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-contract-regression-01\live-authority-walk.json"
)
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_form-contract-regression-01")
EVIDENCE = Path(
    r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-contract-regression-01"
)
SRC_ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source")
OLD_CORE = (
    '<input type="tel" id="pf_contact" name="pf_contact" placeholder="WhatsApp / Telegram" required>'
)
OLD_CORE_B = OLD_CORE.encode("ascii")
TEL_BAD = re.compile(rb'<input\s+type="tel"[^>]*name="pf_contact"', re.I)

REMOTE_TO_LOCAL = {
    f"{DOC}/wp-content/themes/iseoblog/template-parts/content-form-seo.php": SRC_ROOT
    / "theme"
    / "iseoblog"
    / "template-parts"
    / "content-form-seo.php",
    f"{DOC}/blog.html": SRC_ROOT / "static-html" / "blog.html",
    f"{DOC}/blog-article.html": SRC_ROOT / "static-html" / "blog-article.html",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def apply_core_patch_bytes(raw: bytes) -> tuple[bytes, str, int]:
    already = b'name="pf_phone"' in raw and b'value="WhatsApp"' in raw
    if OLD_CORE_B not in raw:
        if already and TEL_BAD.search(raw) is None:
            return raw, "already_patched", 0
        raise SystemExit("OLD_CORE tel/name=pf_contact not found; refuse rewrite")
    nl = b"\r\n" if b"\r\n" in raw else b"\n"
    remaining = raw
    result = bytearray()
    n = 0
    while True:
        idx = remaining.find(OLD_CORE_B)
        if idx < 0:
            result.extend(remaining)
            break
        line_start = remaining.rfind(b"\n", 0, idx)
        indent = remaining[line_start + 1 : idx] if line_start >= 0 else remaining[:idx]
        indent = indent.replace(b"\r", b"")
        replacement = (
            b'<input type="hidden" name="pf_contact" value="WhatsApp">'
            + nl
            + indent
            + b'<input type="tel" id="pf_contact" name="pf_phone" placeholder="WhatsApp / Telegram" required>'
        )
        result.extend(remaining[:idx])
        result.extend(replacement)
        remaining = remaining[idx + len(OLD_CORE_B) :]
        n += 1
    after = bytes(result)
    if TEL_BAD.search(after):
        raise SystemExit("tel still named pf_contact after patch")
    if b'name="pf_phone"' not in after:
        raise SystemExit("patch did not introduce pf_phone")
    if b'cf_agree21' in raw and b'cf_agree21' not in after:
        raise SystemExit("cf_agree21 lost")
    if b"personal_data_consent" in raw and b"personal_data_consent" not in after:
        raise SystemExit("consent lost")
    return after, "patched", n


def main() -> int:
    walk = json.loads(WALK.read_text(encoding="utf-8"))
    remotes = [f["remote"] for f in walk["proven_authorities"] if f.get("kind") == "file"]
    if not remotes:
        raise SystemExit("no proven authorities")
    BAK_ROOT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"],
        password=secrets["ftp_or_sftp_password"],
    )
    sftp = paramiko.SFTPClient.from_transport(transport)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = {
        "task": "ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01",
        "started": utc_now(),
        "backup_root": str(BAK_ROOT),
        "files": [],
        "local_source_patched": [],
    }
    try:
        for remote in remotes:
            with sftp.open(remote, "r") as f:
                before = f.read()
            rel = remote.replace(DOC + "/", "").replace("/", "__")
            bak_path = BAK_ROOT / f"{rel}.before.{ts}"
            bak_path.write_bytes(before)
            patched, mode, n = apply_core_patch_bytes(before)
            entry = {
                "remote": remote,
                "backup": str(bak_path),
                "sha256_before": sha256_bytes(before),
                "bytes_before": len(before),
                "mode": mode,
                "replacements": n,
            }
            if mode == "patched":
                with sftp.open(remote, "w") as f:
                    f.write(patched)
                with sftp.open(remote, "r") as f:
                    verify = f.read()
                if sha256_bytes(verify) != sha256_bytes(patched):
                    raise SystemExit(f"checksum mismatch after write: {remote}")
                entry["sha256_after"] = sha256_bytes(verify)
                entry["bytes_after"] = len(verify)
            else:
                entry["sha256_after"] = sha256_bytes(before)
                entry["bytes_after"] = len(before)
            local = REMOTE_TO_LOCAL.get(remote)
            if local and local.exists():
                local_raw = local.read_bytes()
                local_patched, local_mode, local_n = apply_core_patch_bytes(local_raw)
                if local_mode == "patched":
                    local.write_bytes(local_patched)
                report["local_source_patched"].append(
                    {
                        "path": str(local),
                        "mode": local_mode,
                        "replacements": local_n,
                        "sha256_after": sha256_bytes(local.read_bytes()),
                    }
                )
            report["files"].append(entry)
    finally:
        sftp.close()
        transport.close()
    report["ended"] = utc_now()
    report["patched_count"] = sum(1 for f in report["files"] if f["mode"] == "patched")
    report["already_patched_count"] = sum(
        1 for f in report["files"] if f["mode"] == "already_patched"
    )
    out = EVIDENCE / "_backup-patch.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "out": str(out),
                "patched_count": report["patched_count"],
                "already_patched_count": report["already_patched_count"],
                "file_count": len(report["files"]),
                "local_source_patched": report["local_source_patched"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
