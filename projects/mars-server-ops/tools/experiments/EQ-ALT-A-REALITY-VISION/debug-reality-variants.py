#!/usr/bin/env python3
"""Debug Reality handshake: openssl view + client debug log. Secrets not printed."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
import time
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
PORT = 9443
XRAY = Path(r"C:\Program Files\v2rayN\bin\xray\xray.exe")


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
        # What does :9443 present as TLS?
        code, out = sudo(
            c,
            "timeout 8 openssl s_client -connect 127.0.0.1:9443 -servername www.microsoft.com </dev/null 2>&1 | sed -n '1,40p'",
            pw,
        )
        print("==== OPENSSL_LOOPBACK code", code)
        # redact cert blobs partially
        safe = re.sub(r"-----BEGIN[^-]+-----.*?-----END[^-]+-----", "[CERT]", out, flags=re.S)
        print(safe[-3500:])
        (WAVE / "openssl-9443.txt").write_text(safe, encoding="utf-8")

        # Temporarily raise xray log? skip — use client debug instead
    finally:
        c.close()

    variants = [
        ("vision_short", "xtls-rprx-vision", sec["shortId"]),
        ("vision_empty_short", "xtls-rprx-vision", ""),
        ("noflow_short", "", sec["shortId"]),
    ]
    results = []
    for name, flow, short_id in variants:
        cfg = {
            "log": {"loglevel": "debug"},
            "inbounds": [
                {
                    "tag": "socks-in",
                    "port": 18096,
                    "listen": "127.0.0.1",
                    "protocol": "socks",
                    "settings": {"udp": False},
                }
            ],
            "outbounds": [
                {
                    "tag": "proxy",
                    "protocol": "vless",
                    "settings": {
                        "vnext": [
                            {
                                "address": "127.0.0.1" if False else HOST,
                                # For local workstation we can't loopback to server; use HOST
                                "port": PORT,
                                "users": [
                                    {
                                        "id": sec["uuid"],
                                        "encryption": "none",
                                        **({"flow": flow} if flow else {}),
                                    }
                                ],
                            }
                        ]
                    },
                    "streamSettings": {
                        "network": "tcp",
                        "security": "reality",
                        "realitySettings": {
                            "show": False,
                            "fingerprint": "chrome",
                            "serverName": sec["serverName"],
                            "publicKey": sec["publicKey"],
                            "shortId": short_id,
                            "spiderX": "/",
                        },
                    },
                },
                {"protocol": "freedom", "tag": "direct"},
            ],
        }
        # Actually for debug we want server-side loopback. Upload and run on server.
        results.append({"name": name, "note": "queued for remote"})
        print("VARIANT", name, "flow=", flow or "(empty)", "short_len=", len(short_id))

    # Remote multi-variant probe
    remote = {
        "sec": {
            "uuid": sec["uuid"],
            "publicKey": sec["publicKey"],
            "shortId": sec["shortId"],
            "serverName": sec["serverName"],
        },
        "variants": [
            {"name": "vision_short", "flow": "xtls-rprx-vision", "shortId": sec["shortId"]},
            {"name": "vision_empty", "flow": "xtls-rprx-vision", "shortId": ""},
            {"name": "noflow_short", "flow": "", "shortId": sec["shortId"]},
            {"name": "noflow_empty", "flow": "", "shortId": ""},
        ],
    }
    REMOTE_PY = "/home/marsops/mars-alt-a-variant-probe.py"
    remote_py = r'''#!/usr/bin/env python3
import json, subprocess, os, time, signal
meta = json.load(open("/home/marsops/mars-alt-a-variants.json"))
sec = meta["sec"]
xray = "/usr/local/x-ui/bin/xray-linux-amd64"
results = []
for v in meta["variants"]:
    user = {"id": sec["uuid"], "encryption": "none"}
    if v["flow"]:
        user["flow"] = v["flow"]
    cfg = {
      "log": {"loglevel": "warning"},
      "inbounds": [{"tag":"socks-in","port":18097,"listen":"127.0.0.1","protocol":"socks","settings":{"udp":False}}],
      "outbounds": [{
        "tag":"proxy","protocol":"vless",
        "settings":{"vnext":[{"address":"127.0.0.1","port":9443,"users":[user]}]},
        "streamSettings":{
          "network":"tcp","security":"reality",
          "realitySettings":{
            "show":False,"fingerprint":"chrome","serverName":sec["serverName"],
            "publicKey":sec["publicKey"],"shortId":v["shortId"],"spiderX":"/"
          }
        }
      },{"protocol":"freedom","tag":"direct"}]
    }
    path = f"/tmp/mars-var-{v['name']}.json"
    log = f"/tmp/mars-var-{v['name']}.log"
    open(path,"w").write(json.dumps(cfg))
    os.chmod(path, 0o600)
    subprocess.call(["pkill","-f",path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    p = subprocess.Popen([xray,"run","-c",path], stdout=open(log,"w"), stderr=subprocess.STDOUT)
    time.sleep(2)
    died = p.poll() is not None
    eg = "DIED" if died else ""
    if not died:
        try:
            eg = subprocess.check_output(
                ["curl","-sS","--max-time","12","-x","socks5h://127.0.0.1:18097","https://api.ipify.org"],
                stderr=subprocess.STDOUT, text=True, timeout=20
            ).strip()
        except subprocess.CalledProcessError as e:
            eg = "CURL_FAIL:" + (e.output or "")[:120].replace("\n"," ")
        except Exception as e:
            eg = "ERR:" + type(e).__name__
        p.send_signal(signal.SIGTERM)
        try:
            p.wait(timeout=3)
        except Exception:
            p.kill()
    # redact secrets from log tail
    try:
        tail = open(log).read()[-800:]
        for s in (sec["uuid"], sec["publicKey"], sec["shortId"]):
            if s:
                tail = tail.replace(s, "[REDACTED]")
    except Exception:
        tail = ""
    print(f"RESULT name={v['name']} egress={eg}")
    print(f"LOGTAIL_BEGIN {v['name']}")
    print(tail)
    print(f"LOGTAIL_END {v['name']}")
    results.append({"name": v["name"], "egress": eg})
print("JSON", json.dumps(results))
'''
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
        with sftp.file("/home/marsops/mars-alt-a-variants.json", "w") as rf:
            rf.write(json.dumps(remote))
        with sftp.file(REMOTE_PY, "w") as rf:
            rf.write(remote_py)
        sftp.close()
        code, out = sudo(c, f"python3 {REMOTE_PY}", pw, timeout=120)
        safe = out
        for secret in (sec["uuid"], sec["publicKey"], sec["shortId"]):
            if secret:
                safe = safe.replace(secret, "[REDACTED]")
        print("==== VARIANT PROBE code", code)
        print(safe[-6000:])
        (WAVE / "variant-probe.txt").write_text(safe, encoding="utf-8")
    finally:
        c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
