#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Walk live public_html for exact old tel core and content-form-seo.php includes."""
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
SKIP_DIR_NAMES = {
    ".git",
    "node_modules",
    "wp-admin",
    "wp-includes",
    "wp-content/uploads",
    "wp-content/cache",
    "wp-content/upgrade",
    "cgi-bin",
    "stats",
}

INTEREST_EXT = {".html", ".htm", ".php"}


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def skip_dir(rel: str) -> bool:
    if "/wp-admin" in rel or "/wp-includes" in rel:
        return True
    if "/wp-content/uploads" in rel:
        return True
    if "/wp-content/cache" in rel:
        return True
    if "/wp-content/upgrade" in rel:
        return True
    if "/cgi-bin" in rel:
        return True
    return False


def walk(sftp, root: str):
    stack = [root]
    while stack:
        current = stack.pop()
        rel = current[len(DOC) :] if current.startswith(DOC) else current
        if skip_dir(rel.replace("\\", "/")):
            continue
        try:
            entries = sftp.listdir_attr(current)
        except OSError:
            continue
        for attr in entries:
            name = attr.filename
            path = f"{current}/{name}"
            mode = attr.st_mode
            if mode and (mode & 0o40000):
                stack.append(path)
                continue
            lower = name.lower()
            if not any(lower.endswith(ext) for ext in INTEREST_EXT):
                continue
            yield path


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
    inline_old = []
    includes_seo_form = []
    scanned = 0
    errors = []
    try:
        for path in walk(sftp, DOC):
            scanned += 1
            try:
                with sftp.open(path, "r") as f:
                    text = f.read().decode("utf-8", "replace")
            except OSError as exc:
                errors.append({"path": path, "error": str(exc)})
                continue
            if OLD_CORE in text:
                form_ids = re.findall(r'id="(page__FORM[^"]*)"', text)
                inline_old.append({"remote": path, "form_ids": form_ids})
            if "content-form-seo.php" in text:
                includes_seo_form.append(path)
    finally:
        sftp.close()
        transport.close()

    payload = {
        "task": "ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01",
        "scanned_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "files_scanned": scanned,
        "inline_old_core_count": len(inline_old),
        "inline_old_core": inline_old,
        "includes_content_form_seo_count": len(includes_seo_form),
        "includes_content_form_seo": includes_seo_form,
        "errors": errors,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "out": str(OUT),
                "files_scanned": scanned,
                "inline_old_core_count": len(inline_old),
                "inline_old_core": [x["remote"] for x in inline_old],
                "includes_content_form_seo_count": len(includes_seo_form),
                "error_count": len(errors),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
