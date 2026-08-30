#!/usr/bin/env python3
"""Standalone Reality Vision smoke on isolated port 19443. Does not touch :8443/:9443."""
from __future__ import annotations

import json
import re
import secrets
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
TEST_PORT = 19443


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd: str, pw: str, timeout: int = 120):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=timeout)
    stdin.write(pw + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return stdout.channel.recv_exit_status(), out


REMOTE = r'''#!/usr/bin/env python3
import json, subprocess, os, time, signal, uuid, re, hashlib
XRAY="/usr/local/x-ui/bin/xray-linux-amd64"
PORT=19443
# generate keys
out=subprocess.check_output([XRAY,"x25519"], text=True)
priv=pub=None
for line in out.splitlines():
    low=line.lower()
    if "private" in low:
        priv=line.split(":",1)[-1].strip()
    if "public" in low:
        pub=line.split(":",1)[-1].strip()
if not priv or not pub:
    print("KEYGEN_FAIL", out)
    raise SystemExit(2)
uid=str(uuid.uuid4())
sid=os.urandom(8).hex()
# try dest candidates
dest="www.cloudflare.com:443"
sni="www.cloudflare.com"
server={
  "log":{"loglevel":"warning"},
  "inbounds":[{
    "listen":"0.0.0.0","port":PORT,"protocol":"vless",
    "settings":{"clients":[{"id":uid,"flow":"xtls-rprx-vision"}],"decryption":"none"},
    "streamSettings":{
      "network":"tcp","security":"reality",
      "realitySettings":{
        "show":False,"dest":dest,"xver":0,
        "serverNames":[sni],
        "privateKey":priv,
        "shortIds":["",sid]
      }
    },
    "sniffing":{"enabled":False,"destOverride":["http","tls"]}
  }],
  "outbounds":[{"protocol":"freedom","tag":"direct"}]
}
client={
  "log":{"loglevel":"warning"},
  "inbounds":[{"listen":"127.0.0.1","port":18098,"protocol":"socks","settings":{"udp":False}}],
  "outbounds":[{
    "protocol":"vless",
    "settings":{"vnext":[{"address":"127.0.0.1","port":PORT,"users":[{"id":uid,"encryption":"none","flow":"xtls-rprx-vision"}]}]},
    "streamSettings":{
      "network":"tcp","security":"reality",
      "realitySettings":{
        "fingerprint":"chrome","serverName":sni,"publicKey":pub,"shortId":sid,"spiderX":"/"
      }
    }
  }]
}
spath="/tmp/mars-standalone-server.json"
cpath="/tmp/mars-standalone-client.json"
open(spath,"w").write(json.dumps(server)); os.chmod(spath,0o600)
open(cpath,"w").write(json.dumps(client)); os.chmod(cpath,0o600)
subprocess.call(["pkill","-f","mars-standalone-"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
sp=subprocess.Popen([XRAY,"run","-c",spath], stdout=open("/tmp/mars-standalone-server.log","w"), stderr=subprocess.STDOUT)
time.sleep(2)
if sp.poll() is not None:
    print("SERVER_DIED")
    print(open("/tmp/mars-standalone-server.log").read()[-1500:])
    raise SystemExit(3)
print("SERVER_UP")
cp=subprocess.Popen([XRAY,"run","-c",cpath], stdout=open("/tmp/mars-standalone-client.log","w"), stderr=subprocess.STDOUT)
time.sleep(2)
if cp.poll() is not None:
    print("CLIENT_DIED")
    print(open("/tmp/mars-standalone-client.log").read()[-1500:])
    sp.send_signal(signal.SIGTERM)
    raise SystemExit(4)
try:
    eg=subprocess.check_output(["curl","-sS","--max-time","15","-x","socks5h://127.0.0.1:18098","https://api.ipify.org"], text=True, stderr=subprocess.STDOUT, timeout=25).strip()
    print("EGRESS="+eg)
except subprocess.CalledProcessError as e:
    print("CURL_FAIL", (e.output or "")[:200])
    print("CLIENT_LOG", open("/tmp/mars-standalone-client.log").read()[-800:])
    print("SERVER_LOG", open("/tmp/mars-standalone-server.log").read()[-800:])
except Exception as e:
    print("ERR", type(e).__name__, e)
finally:
    for p in (cp, sp):
        try:
            p.send_signal(signal.SIGTERM); p.wait(timeout=3)
        except Exception:
            try: p.kill()
            except Exception: pass
    for f in (spath,cpath):
        try: os.remove(f)
        except Exception: pass
print("PUB_SHA12="+hashlib.sha256(pub.encode()).hexdigest()[:12])
print("DONE")
'''


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
        with sftp.file("/home/marsops/mars-standalone-reality.py", "w") as rf:
            rf.write(REMOTE)
        sftp.close()
        # open UFW for test port briefly
        sudo(c, f"ufw allow {TEST_PORT}/tcp comment 'EQ-ALT-A standalone smoke' || true", pw)
        code, out = sudo(c, "python3 /home/marsops/mars-standalone-reality.py", pw, timeout=90)
        safe = re.sub(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
            "[UUID]",
            out,
            flags=re.I,
        )
        print("code", code)
        print(safe)
        (WAVE / "standalone-reality-smoke.txt").write_text(safe, encoding="utf-8")
        # close UFW rule for smoke port (keep 9443)
        sudo(
            c,
            f"ufw status numbered | grep -F '{TEST_PORT}/tcp' | head -5; "
            f"ufw --force delete allow {TEST_PORT}/tcp || true; "
            f"ufw status | grep -E '{TEST_PORT}|9443|8443' || true",
            pw,
        )
        return 0 if "EGRESS=" + HOST in out or f"EGRESS={HOST}" in out else 2
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
