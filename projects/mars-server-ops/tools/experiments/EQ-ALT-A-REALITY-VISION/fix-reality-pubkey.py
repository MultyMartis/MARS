#!/usr/bin/env python3
"""Derive REALITY publicKey from server privateKey; sync local client secrets if mismatched. LOCAL ONLY."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
REMOTE_PY = "/home/marsops/mars-alt-a-fix-pubkey.py"

REMOTE_SCRIPT = r'''#!/usr/bin/env python3
import json, subprocess, hashlib, re
cfg = json.load(open("/usr/local/x-ui/bin/config.json"))
pk = None
sid = None
uuid = None
for ib in cfg.get("inbounds", []):
    if ib.get("port") != 9443:
        continue
    rs = ib.get("streamSettings", {}).get("realitySettings", {})
    pk = rs.get("privateKey")
    sids = rs.get("shortIds") or []
    sid = next((x for x in sids if x), "")
    for cl in ib.get("settings", {}).get("clients", []):
        uuid = cl.get("id")
        break
if not pk:
    print("NO_PRIVATE_KEY")
    raise SystemExit(2)
xray = "/usr/local/x-ui/bin/xray-linux-amd64"
out = subprocess.check_output([xray, "x25519", "-i", pk], text=True, timeout=10)
# Expected lines like Password: ... / PublicKey: ...
pub = None
for line in out.splitlines():
    if re.search(r"(?i)public", line):
        pub = line.split(":", 1)[-1].strip()
        break
if not pub:
    # some builds print PrivateKey / PublicKey labels differently
    for line in out.splitlines():
        parts = line.strip().split()
        if len(parts) >= 2 and "public" in parts[0].lower():
            pub = parts[-1]
            break
if not pub:
    print("PARSE_FAIL")
    print("LINES", len(out.splitlines()))
    raise SystemExit(3)
print("PUBLIC_KEY=" + pub)
print("SHORT_ID=" + (sid or ""))
print("UUID=" + (uuid or ""))
print("PUB_SHA12=" + hashlib.sha256(pub.encode()).hexdigest()[:12])
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
    path = WAVE / "client-secrets.local.json"
    sec = json.loads(path.read_text(encoding="utf-8"))
    old_sha = hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12]
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
        # redacted echo
        safe = out
        for line in out.splitlines():
            if line.startswith("PUBLIC_KEY=") or line.startswith("UUID=") or line.startswith("SHORT_ID="):
                k, _, v = line.partition("=")
                safe = safe.replace(line, f"{k}=[REDACTED_len={len(v)}]")
        print(safe)
        m = re.search(r"^PUBLIC_KEY=(.+)$", out, re.M)
        if not m:
            return 2
        pub = m.group(1).strip()
        new_sha = hashlib.sha256(pub.encode()).hexdigest()[:12]
        print("OLD_PUB_SHA12", old_sha)
        print("NEW_PUB_SHA12", new_sha)
        print("MATCH", old_sha == new_sha)
        if old_sha != new_sha:
            sec["publicKey"] = pub
            # also sync shortId/uuid if returned
            m2 = re.search(r"^SHORT_ID=(.+)$", out, re.M)
            m3 = re.search(r"^UUID=(.+)$", out, re.M)
            if m2 and m2.group(1).strip():
                sec["shortId"] = m2.group(1).strip()
            if m3 and m3.group(1).strip():
                sec["uuid"] = m3.group(1).strip()
            path.write_text(json.dumps(sec, indent=2) + "\n", encoding="utf-8")
            print("UPDATED_LOCAL_SECRETS=1")
            print("[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]")
        else:
            print("UPDATED_LOCAL_SECRETS=0")
        return 0
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
