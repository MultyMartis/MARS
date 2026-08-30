#!/usr/bin/env python3
"""Write local-only client profile artifacts + set flow_override. No secret prints."""
from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"

REMOTE = r'''#!/usr/bin/env python3
import sqlite3, json
conn = sqlite3.connect("/etc/x-ui/x-ui.db")
cur = conn.cursor()
rid = [i for i, p, _ in cur.execute("SELECT id, port, settings FROM inbounds") if int(p) == 9443][0]
cur.execute(
    "UPDATE client_inbounds SET flow_override=? WHERE inbound_id=?",
    ("xtls-rprx-vision", rid),
)
conn.commit()
cfg = json.load(open("/usr/local/x-ui/bin/config.json"))
for ib in cfg["inbounds"]:
    if ib.get("port") == 9443:
        print("CFG_FLOW", ib["settings"]["clients"][0].get("flow"))
        print("CFG_DEST", ib["streamSettings"]["realitySettings"].get("dest"))
        print("CFG_SNI", ib["streamSettings"]["realitySettings"].get("serverNames"))
print("FO", cur.execute("SELECT flow_override FROM client_inbounds WHERE inbound_id=?", (rid,)).fetchone())
print("OK")
'''


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def main() -> int:
    pw = load_pw()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        22,
        username="marsops",
        key_filename=str(KEY),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    try:
        sftp = c.open_sftp()
        sftp.file("/home/marsops/mars-fo.py", "w").write(REMOTE.replace("\r\n", "\n"))
        sftp.close()
        full = f"sudo -S -p '' bash -lc {json.dumps('python3 /home/marsops/mars-fo.py')}"
        stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=60)
        stdin.write(pw + "\n")
        stdin.flush()
        stdin.channel.shutdown_write()
        out = (stdout.read() + stderr.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
        print(out)
    finally:
        c.close()

    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))
    remark = sec.get("remark", "MCA-ONE-EQ-ALT-A-REALITY-VISION")
    address = sec.get("address", HOST)
    qs = urllib.parse.urlencode(
        {
            "encryption": "none",
            "flow": "xtls-rprx-vision",
            "security": "reality",
            "sni": sec["serverName"],
            "fp": "chrome",
            "pbk": sec["publicKey"],
            "sid": sec["shortId"],
            "spx": "/",
            "type": "tcp",
            "headerType": "none",
        }
    )
    uri = f"vless://{sec['uuid']}@{address}:9443?{qs}#{urllib.parse.quote(remark)}"
    (WAVE / "vless-share.uri.local").write_text(uri + "\n", encoding="utf-8")
    profile = {
        "remarks": remark,
        "address": address,
        "port": 9443,
        "id": sec["uuid"],
        "flow": "xtls-rprx-vision",
        "encryption": "none",
        "network": "tcp",
        "headerType": "none",
        "security": "reality",
        "sni": sec["serverName"],
        "fingerprint": "chrome",
        "publicKey": sec["publicKey"],
        "shortId": sec["shortId"],
        "spiderX": "/",
    }
    (WAVE / "v2rayn-profile.local.json").write_text(
        json.dumps(profile, indent=2) + "\n", encoding="utf-8"
    )
    meta = {
        "display_name": remark,
        "port": 9443,
        "sni": sec["serverName"],
        "dest": sec.get("dest"),
        "flow": "xtls-rprx-vision",
        "fingerprint": "chrome",
        "pub_sha12": hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12],
        "files": [
            str(WAVE / "client-secrets.local.json"),
            str(WAVE / "vless-share.uri.local"),
            str(WAVE / "v2rayn-profile.local.json"),
        ],
        "note": "[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]",
    }
    (WAVE / "client-profile-meta.json").write_text(
        json.dumps(meta, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
