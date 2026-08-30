#!/usr/bin/env python3
"""Safe Reality inbound diag — no secret values printed."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
REMOTE_PY = "/home/marsops/mars-alt-a-diag.py"

REMOTE_SCRIPT = r'''#!/usr/bin/env python3
import json, subprocess, hashlib
cfg = json.load(open("/usr/local/x-ui/bin/config.json"))
found = False
for ib in cfg.get("inbounds", []):
    if ib.get("port") != 9443:
        continue
    found = True
    ss = ib.get("streamSettings", {})
    rs = ss.get("realitySettings", {})
    clients = ib.get("settings", {}).get("clients", [])
    pk = rs.get("privateKey") or ""
    pub = rs.get("publicKey") or ""
    sids = rs.get("shortIds") or []
    print("FOUND_9443=1")
    print("protocol", ib.get("protocol"))
    print("network", ss.get("network"))
    print("security", ss.get("security"))
    print("dest", rs.get("dest") or rs.get("target"))
    print("serverNames", rs.get("serverNames"))
    print("shortIds_count", len(sids))
    print("shortIds_lens", [len(x) for x in sids])
    print("shortIds_empty_present", "" in sids)
    print("fingerprint", rs.get("fingerprint"))
    print("show", rs.get("show"))
    print("privateKey_len", len(pk))
    print("publicKey_len", len(pub))
    print("publicKey_sha12", hashlib.sha256(pub.encode()).hexdigest()[:12] if pub else "NONE")
    print("privateKey_sha12", hashlib.sha256(pk.encode()).hexdigest()[:12] if pk else "NONE")
    for cl in clients:
        print("client_id_prefix", str(cl.get("id", ""))[:8])
        print("client_flow", repr(cl.get("flow")))
        print("client_email", cl.get("email"))
    print("sniffing", ib.get("sniffing"))
if not found:
    print("FOUND_9443=0")
# dest reachability
import socket
for host, port in [("www.microsoft.com", 443), ("www.cloudflare.com", 443), ("dl.google.com", 443)]:
    try:
        s = socket.create_connection((host, port), 8)
        s.close()
        print(f"DEST_OK {host}:{port}")
    except Exception as e:
        print(f"DEST_FAIL {host}:{port} {type(e).__name__}")
# xray x25519 if available
xray = "/usr/local/x-ui/bin/xray-linux-amd64"
try:
    out = subprocess.check_output([xray, "x25519"], text=True, timeout=10)
    print("X25519_TOOL_OK lines", len(out.splitlines()))
except Exception as e:
    print("X25519_TOOL", type(e).__name__)
'''


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd: str, pw: str, timeout: int = 60):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=timeout)
    stdin.write(pw + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return stdout.channel.recv_exit_status(), out


def main() -> int:
    pw = load_pw()
    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))
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
        with sftp.file(REMOTE_PY, "w") as rf:
            rf.write(REMOTE_SCRIPT)
        sftp.close()
        code, out = sudo(c, f"python3 {REMOTE_PY}", pw)
        print("code", code)
        print(out)
        import hashlib

        print(
            "LOCAL_pub_sha12",
            hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12],
        )
        print("LOCAL_shortId_len", len(sec["shortId"]))
        print("LOCAL_uuid_prefix", sec["uuid"][:8])
        print("LOCAL_sni", sec["serverName"])
        (WAVE / "diag-reality-safe.txt").write_text(out, encoding="utf-8")
        return 0
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
