# -*- coding: utf-8 -*-
"""Redeploy ConsultationHandler after comment tweak + live specialist new-site check."""
from __future__ import annotations

import hashlib
import io
import json
import re
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
SRC = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\plugins\shpigovsky-core\src\Forms\ConsultationHandler.php")
REMOTE = "/home/s/shpigovsky/shpigovsky.ru/public_html/wp-content/plugins/shpigovsky-core/src/Forms/ConsultationHandler.php"
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p17-fu02-final-tail")
BASE = "http://shpigovsky.beget.tech"


def parse_secrets(text: str) -> dict:
    pairs = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs, *keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None


def main() -> int:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    local = SRC.read_bytes()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host"),
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username"),
        password=getf(pairs, "ssh_password_or_key_reference"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()
    with sftp.file(REMOTE, "wb") as fh:
        fh.write(local)
    bio = io.BytesIO()
    sftp.getfo(REMOTE, bio)
    after = bio.getvalue()
    sftp.close()
    client.close()
    match = after == local
    print("MATCH" if match else "FAIL", hashlib.sha256(local).hexdigest())
    sess = requests.Session()
    rows = []
    for path in [
        "/specyalisty/",
        "/blog/nazvanie-stati/",
        "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
        "/wp-content/uploads/2026/07/sergey-shpigovsky-interview.mp4",
    ]:
        r = sess.get(BASE + path, timeout=30)
        rows.append({"path": path, "status": r.status_code, "new_site": "new-site.space" in (r.text or "")})
        print(path, r.status_code, "newsite" if rows[-1]["new_site"] else "ok")
    (EV / "APPLY-REDEPLOY-HANDLER.json").write_text(
        json.dumps({"match": match, "sha": hashlib.sha256(local).hexdigest(), "http": rows}, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0 if match else 2


if __name__ == "__main__":
    raise SystemExit(main())
