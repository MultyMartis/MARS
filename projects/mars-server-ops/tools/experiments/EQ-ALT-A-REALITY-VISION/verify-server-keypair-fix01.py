#!/usr/bin/env python3
"""Verify EQ-ALT-A server REALITY keypair vs local client pbk. Secrets not printed."""
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
REMOTE_PY = "/home/marsops/mars-alt-a-verify-keypair-fix01.py"

REMOTE_SCRIPT = r'''#!/usr/bin/env python3
import json, subprocess, hashlib, re
cfg = json.load(open("/usr/local/x-ui/bin/config.json"))
found = None
for ib in cfg.get("inbounds", []):
    if ib.get("port") != 9443:
        continue
    found = ib
    break
if not found:
    print("INBOUND_9443=MISSING")
    raise SystemExit(2)
ss = found.get("streamSettings", {})
rs = ss.get("realitySettings", {}) or {}
pk = rs.get("privateKey")
sids = rs.get("shortIds") or []
sid = next((x for x in sids if x), "")
clients = (found.get("settings") or {}).get("clients") or []
uuid = clients[0].get("id") if clients else ""
flow = clients[0].get("flow") if clients else ""
print("PORT", found.get("port"))
print("PROTOCOL", found.get("protocol"))
print("NETWORK", ss.get("network"))
print("SECURITY", ss.get("security"))
print("DEST", rs.get("dest") or rs.get("target"))
print("SERVER_NAMES", json.dumps(rs.get("serverNames")))
print("PRIVATE_KEY_PRESENT", bool(pk))
print("PRIVATE_KEY_LEN", len(pk) if isinstance(pk, str) else None)
print("SHORT_IDS_COUNT", len(sids))
print("SHORT_ID_NONEMPTY_LEN", len(sid) if isinstance(sid, str) else None)
print("SHORT_ID_HEX", bool(re.fullmatch(r"[0-9a-fA-F]*", sid or "")))
print("CLIENT_UUID_PRESENT", bool(uuid))
print("CLIENT_FLOW", flow)
print("TCP_SETTINGS_PRESENT", "tcpSettings" in ss)
if not pk:
    print("NO_PRIVATE_KEY")
    raise SystemExit(3)
xray = "/usr/local/x-ui/bin/xray-linux-amd64"
# Prefer derive from private key; fall back to parse styles across versions
out = subprocess.check_output([xray, "x25519", "-i", pk], text=True, timeout=15)
pub = None
for line in out.splitlines():
    if re.search(r"(?i)public", line):
        pub = line.split(":", 1)[-1].strip()
        break
if not pub:
    print("PARSE_FAIL")
    print("X25519_LINE_COUNT", len(out.splitlines()))
    raise SystemExit(4)
print("DERIVED_PUB_SHA12", hashlib.sha256(pub.encode()).hexdigest()[:12])
print("DERIVED_PUB_LEN", len(pub))
print("DERIVED_PUB_CHARSET_OK", bool(re.fullmatch(r"[A-Za-z0-9\-_+=]+", pub)))
# also emit derived pub for local compare only (parent will redact)
print("DERIVED_PUBLIC_KEY=" + pub)
print("SERVER_SHORT_ID=" + sid)
ver = subprocess.check_output([xray, "version"], text=True, timeout=10)
print("XRAY_VERSION_LINE", ver.splitlines()[0] if ver.strip() else "")
# :8443 still listening regression
import subprocess as sp
ssout = sp.check_output("ss -lntp | grep -E ':8443|:9443' || true", shell=True, text=True)
print("LISTEN_SNIPPET_LINES", len([l for l in ssout.splitlines() if l.strip()]))
for l in ssout.splitlines():
    if ":8443" in l:
        print("LISTENING_8443", True)
    if ":9443" in l:
        print("LISTENING_9443", True)
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
    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))
    local_sha = hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12]
    print("LOCAL_PUB_SHA12", local_sha)
    print("LOCAL_PBK_LEN", len(sec["publicKey"]))
    print("LOCAL_SID_LEN", len(sec.get("shortId", "")))
    print("LOCAL_SNI", sec.get("serverName"))

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
        with sftp.file(REMOTE_PY, "w") as rf:
            rf.write(REMOTE_SCRIPT.replace("\r\n", "\n"))
        sftp.close()
        code, out = sudo(c, f"python3 {REMOTE_PY}; rm -f {REMOTE_PY}", pw)
        # redact secret-bearing lines for console
        safe_lines = []
        derived = None
        server_sid = None
        for line in out.splitlines():
            if line.startswith("DERIVED_PUBLIC_KEY="):
                derived = line.split("=", 1)[1].strip()
                safe_lines.append(f"DERIVED_PUBLIC_KEY=[REDACTED_len={len(derived)}]")
            elif line.startswith("SERVER_SHORT_ID="):
                server_sid = line.split("=", 1)[1].strip()
                safe_lines.append(f"SERVER_SHORT_ID=[REDACTED_len={len(server_sid)}]")
            else:
                # scrub accidental private key echoes
                if "private" in line.lower() and "present" not in line.lower() and "len" not in line.lower():
                    safe_lines.append("[REDACTED_PRIVATE_CONTEXT]")
                else:
                    safe_lines.append(line)
        print("REMOTE_EXIT", code)
        print("\n".join(safe_lines))
        if not derived:
            print("CLASSIFICATION", "UNKNOWN")
            return 2
        derived_sha = hashlib.sha256(derived.encode()).hexdigest()[:12]
        print("DERIVED_PUB_SHA12_LOCALCALC", derived_sha)
        if derived == sec["publicKey"]:
            print("KEYPAIR_CLASS", "MATCH")
        else:
            # check if local accidentally holds private-looking material swapped
            print("KEYPAIR_CLASS", "MISMATCH")
        if server_sid is not None:
            print("SHORTID_MATCH", server_sid == sec.get("shortId"))
        # write derived pubkey to a temp local compare artifact (operator-local only) without printing
        compare = {
            "local_pub_sha12": local_sha,
            "derived_pub_sha12": derived_sha,
            "match": derived == sec["publicKey"],
            "shortid_match": (server_sid == sec.get("shortId")) if server_sid is not None else None,
            "note": "[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]",
        }
        (WAVE / "keypair-verify-safe.json").write_text(json.dumps(compare, indent=2) + "\n", encoding="utf-8")
        if derived != sec["publicKey"]:
            # store corrected expected public key into a staging secrets file (not overwriting original yet)
            fixed = dict(sec)
            fixed["publicKey"] = derived
            if server_sid:
                fixed["shortId"] = server_sid
            (WAVE / "client-secrets-fixed.local.json").write_text(
                json.dumps(fixed, indent=2) + "\n", encoding="utf-8"
            )
            print("FIXED_SECRETS_STAGED", True)
        else:
            print("FIXED_SECRETS_STAGED", False)
        return 0
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
