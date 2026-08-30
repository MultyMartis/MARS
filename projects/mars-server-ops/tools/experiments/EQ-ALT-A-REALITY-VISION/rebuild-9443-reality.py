#!/usr/bin/env python3
"""Rebuild EQ-ALT-A :9443 Reality settings to match proven standalone shape. LOCAL ONLY."""
from __future__ import annotations

import hashlib
import json
import re
import uuid
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
REMOTE = "/home/marsops/mars-rebuild-9443.py"

BODY = r'''#!/usr/bin/env python3
import json, sqlite3, subprocess, os, time, hashlib, secrets, uuid

XRAY="/usr/local/x-ui/bin/xray-linux-amd64"
DB="/etc/x-ui/x-ui.db"
CFG="/usr/local/x-ui/bin/config.json"
DEST="www.cloudflare.com:443"
SNI="www.cloudflare.com"

out=subprocess.check_output([XRAY,"x25519"], text=True)
priv=pub=None
for line in out.splitlines():
    low=line.lower()
    if "private" in low and "public" not in low:
        priv=line.split(":",1)[-1].strip()
    if "public" in low:
        pub=line.split(":",1)[-1].strip()
if not priv or not pub:
    raise SystemExit("keygen failed")
sid=secrets.token_bytes(8).hex()

# keep existing client uuid/email/flow if present
cfg=json.load(open(CFG))
ib=None
for x in cfg.get("inbounds",[]):
    if x.get("port")==9443:
        ib=x; break
if not ib:
    raise SystemExit("9443 missing")
clients=ib.get("settings",{}).get("clients") or []
if not clients:
    raise SystemExit("no clients")
cl=clients[0]
uid=cl.get("id")
email=cl.get("email") or "MCA-ONE-EQ-ALT-A-REALITY-VISION"
cl["flow"]="xtls-rprx-vision"

rs=ib.setdefault("streamSettings",{})
rs["network"]="tcp"
rs["security"]="reality"
# drop tcpSettings to match standalone
rs.pop("tcpSettings", None)
rs["realitySettings"]={
  "show": False,
  "dest": DEST,
  "xver": 0,
  "serverNames": [SNI],
  "privateKey": priv,
  "shortIds": ["", sid],
}
ib["settings"]["decryption"]="none"
ib["sniffing"]={"enabled": False, "destOverride": ["http","tls"], "metadataOnly": False, "routeOnly": False}

# write config
open(CFG,"w").write(json.dumps(cfg, indent=2))
os.chmod(CFG, 0o644)

# update sqlite inbounds.settings JSON for port 9443
conn=sqlite3.connect(DB)
cur=conn.cursor()
rows=cur.execute("SELECT id, port, settings, stream_settings, sniffing FROM inbounds").fetchall()
target=None
for rid, port, settings, stream_settings, sniffing in rows:
    if int(port)==9443:
        target=rid
        st=json.loads(settings or "{}")
        if "clients" in st and st["clients"]:
            st["clients"][0]["flow"]="xtls-rprx-vision"
            st["clients"][0]["id"]=uid
            st["clients"][0]["email"]=email
        st["decryption"]="none"
        ss=json.loads(stream_settings or "{}")
        ss["network"]="tcp"
        ss["security"]="reality"
        ss.pop("tcpSettings", None)
        ss["realitySettings"]={
          "show": False,
          "dest": DEST,
          "xver": 0,
          "serverNames": [SNI],
          "privateKey": priv,
          "shortIds": ["", sid],
        }
        sn={"enabled": False, "destOverride": ["http","tls"], "metadataOnly": False, "routeOnly": False}
        cur.execute(
          "UPDATE inbounds SET settings=?, stream_settings=?, sniffing=? WHERE id=?",
          (json.dumps(st), json.dumps(ss), json.dumps(sn), rid),
        )
        # flow_override
        try:
            cur.execute(
              "UPDATE client_inbounds SET flow=?, flow_override=? WHERE inbound_id=?",
              ("xtls-rprx-vision","xtls-rprx-vision", rid),
            )
        except Exception as e:
            print("client_inbounds_update_warn", type(e).__name__)
        break
conn.commit(); conn.close()
if target is None:
    raise SystemExit("db inbound not found")

# restart x-ui
subprocess.check_call(["systemctl","restart","x-ui"])
time.sleep(4)
# validate
subprocess.check_call([XRAY,"run","-test","-c",CFG])
# listeners
ss=subprocess.check_output("ss -lntp | grep -E ':8443|:9443|:443 ' || true", shell=True, text=True)
print("LISTENERS")
print(ss)
# emit local secret payload to stdout for capture by parent (will be redacted in reports)
print("SECRET_JSON="+json.dumps({
  "uuid": uid,
  "publicKey": pub,
  "shortId": sid,
  "serverName": SNI,
  "dest": DEST,
  "port": 9443,
  "flow": "xtls-rprx-vision",
  "address": "95.216.126.173",
  "fingerprint": "chrome",
  "spiderX": "/",
  "remark": "MCA-ONE-EQ-ALT-A-REALITY-VISION",
}))
print("PUB_SHA12="+hashlib.sha256(pub.encode()).hexdigest()[:12])
print("REBUILD_OK")
'''


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd, pw, timeout=120):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    i, o, e = c.exec_command(full, get_pty=True, timeout=timeout)
    i.write(pw + "\n")
    i.flush()
    i.channel.shutdown_write()
    out = (o.read() + e.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return o.channel.recv_exit_status(), out


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
        sftp.file(REMOTE, "w").write(BODY.replace("\r\n", "\n"))
        sftp.close()
        code, out = sudo(c, f"python3 {REMOTE}", pw, timeout=120)
        m = re.search(r"SECRET_JSON=(\{.*\})", out)
        if not m:
            safe = re.sub(r"SECRET_JSON=\{.*\}", "SECRET_JSON=[REDACTED]", out)
            print("code", code)
            print(safe)
            return 2
        sec = json.loads(m.group(1))
        path = WAVE / "client-secrets.local.json"
        path.write_text(json.dumps(sec, indent=2) + "\n", encoding="utf-8")
        print("code", code)
        print(re.sub(r"SECRET_JSON=\{.*\}", "SECRET_JSON=[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]", out))
        print("PUB_SHA12", hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12])
        print("SNI", sec["serverName"])
        print("[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]")
        return 0 if "REBUILD_OK" in out and ":8443" in out and ":9443" in out else 2
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
