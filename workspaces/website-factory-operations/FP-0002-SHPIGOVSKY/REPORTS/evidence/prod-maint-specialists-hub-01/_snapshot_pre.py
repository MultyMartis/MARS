# -*- coding: utf-8 -*-
"""Download production FieldGroups + core header for bounded patch base."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
WT_PLUGIN = Path(
    r"X:\AI MARS\worktrees\fp0002-specialists-hub-01\workspaces\website-factory-operations"
    r"\FP-0002-SHPIGOVSKY\WORDPRESS\plugins\shpigovsky-core"
)


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if match:
            pairs[match.group(1)] = match.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def main() -> None:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username", "sftp_user"),
        password=getf(pairs, "ssh_password_or_key_reference", "sftp_password", "ftp_or_sftp_password"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()
    files = {
        "FieldGroups.php": f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php",
        "shpigovsky-core.php": f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php",
        "generic.php": f"{DOCROOT}/wp-content/themes/shpigovsky/page-templates/generic.php",
        "content-page.php": f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/generic/content-page.php",
        "reusable-blocks-helpers.php": f"{DOCROOT}/wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php",
        "home-specialists.php": f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/home/specialists.php",
        "services-hub.php": f"{DOCROOT}/wp-content/themes/shpigovsky/page-templates/services-hub.php",
        "robots.txt": f"{DOCROOT}/robots.txt",
    }
    pre = OUT / "layer-b-pre"
    pre.mkdir(parents=True, exist_ok=True)
    for name, remote in files.items():
        local = pre / name
        sftp.get(remote, str(local))
        data = local.read_bytes()
        print(f"{name} bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}")

    # Compare FieldGroups to worktree source (LF normalize)
    src = (WT_PLUGIN / "src/Fields/FieldGroups.php").read_bytes().replace(b"\r\n", b"\n")
    prod = (pre / "FieldGroups.php").read_bytes().replace(b"\r\n", b"\n")
    print("FieldGroups semantic equal?", src == prod)
    print("src sha", hashlib.sha256(src).hexdigest())
    print("prod sha", hashlib.sha256(prod).hexdigest())
    src_core = (WT_PLUGIN / "shpigovsky-core.php").read_text(encoding="utf-8", errors="replace")
    prod_core = (pre / "shpigovsky-core.php").read_text(encoding="utf-8", errors="replace")
    for label, text in (("src", src_core), ("prod", prod_core)):
        m = re.search(r"Version:\s*(\S+)", text)
        print(label, "Version", m.group(1) if m else "?")

    sftp.close()
    client.close()


if __name__ == "__main__":
    main()
