#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Narrow live SFTP walk for exact OLD_CORE form-contract defect. No full public_html recurse."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
OUT = Path(
    r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-contract-regression-01\live-authority-walk.json"
)
OLD_CORE = (
    '<input type="tel" id="pf_contact" name="pf_contact" placeholder="WhatsApp / Telegram" required>'
)
TEL_BAD = re.compile(r'<input\s+type="tel"[^>]*name="pf_contact"', re.I)

DIRS = [
    DOC,
    f"{DOC}/services",
    f"{DOC}/services/seo",
    f"{DOC}/services/adv",
    f"{DOC}/services/audit",
    f"{DOC}/services/development",
    f"{DOC}/services/serm",
    f"{DOC}/services/ai-optimization",
    f"{DOC}/wp-content/themes/iseoblog/template-parts",
]

EXTS = (".html", ".htm", ".php")


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def classify(text: str) -> dict:
    tel_bad = TEL_BAD.search(text) is not None
    pf_phone = 'name="pf_phone"' in text
    includes = re.findall(r"content-form[\w.-]+\.php", text)
    return {
        "tel_named_pf_contact": tel_bad,
        "pf_phone_present": pf_phone,
        "old_core_exact": OLD_CORE in text,
        "old_core_count": text.count(OLD_CORE),
        "consent_checkbox": 'name="personal_data_consent"' in text,
        "includes": includes,
        "proven_defect": tel_bad and (not pf_phone),
    }


def main() -> int:
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"],
        password=secrets["ftp_or_sftp_password"],
    )
    sftp = paramiko.SFTPClient.from_transport(transport)
    files = []
    try:
        for d in DIRS:
            try:
                names = sftp.listdir(d)
            except OSError as exc:
                files.append({"kind": "listdir_error", "remote": d, "error": str(exc)})
                continue
            for name in sorted(names):
                if not name.lower().endswith(EXTS):
                    continue
                remote = f"{d}/{name}"
                try:
                    with sftp.open(remote, "r") as f:
                        raw = f.read()
                except OSError as exc:
                    files.append({"kind": "read_error", "remote": remote, "error": str(exc)})
                    continue
                text = raw.decode("utf-8", "replace")
                info = classify(text)
                if (
                    info["old_core_exact"]
                    or info["proven_defect"]
                    or info["tel_named_pf_contact"]
                    or any("content-form" in x for x in info["includes"])
                ):
                    files.append({"kind": "file", "remote": remote, **info})
    finally:
        sftp.close()
        transport.close()

    proven = [f for f in files if f.get("old_core_exact") or f.get("proven_defect")]
    includes_only = [
        f
        for f in files
        if f.get("includes") and not f.get("old_core_exact") and not f.get("proven_defect")
    ]
    payload = {
        "task": "ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01",
        "scanned_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dirs": DIRS,
        "hit_count": len(files),
        "proven_authority_count": len(proven),
        "proven_authorities": proven,
        "include_only_pages": includes_only,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "out": str(OUT),
                "hit_count": len(files),
                "proven_authority_count": len(proven),
                "proven_remotes": [f["remote"] for f in proven],
                "include_only_count": len(includes_only),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
