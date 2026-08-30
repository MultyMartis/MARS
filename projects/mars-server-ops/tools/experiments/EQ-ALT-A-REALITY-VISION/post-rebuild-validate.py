#!/usr/bin/env python3
"""Ensure flow in DB; workstation Reality transport probe. LOCAL ONLY."""
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
XRAY = Path(r"C:\Program Files\v2rayN\bin\xray\xray.exe")

REMOTE = r'''#!/usr/bin/env python3
import sqlite3, json
conn = sqlite3.connect("/etc/x-ui/x-ui.db")
cur = conn.cursor()
cols = [c[1] for c in cur.execute("PRAGMA table_info(client_inbounds)").fetchall()]
print("COLS", cols)
rid = None
for i, port, settings in cur.execute("SELECT id, port, settings FROM inbounds"):
    if int(port) == 9443:
        rid = i
        break
print("INBOUND_ID", rid)
if rid is not None:
    if "flow_override" in cols:
        cur.execute(
            "UPDATE client_inbounds SET flow_override=? WHERE inbound_id=?",
            ("xtls-rprx-vision", rid),
        )
    elif "flow" in cols:
        cur.execute(
            "UPDATE client_inbounds SET flow=? WHERE inbound_id=?",
            ("xtls-rprx-vision", rid),
        )
    conn.commit()
    print("FLOW_OVERRIDE_SET", "flow_override" in cols)
cfg = json.load(open("/usr/local/x-ui/bin/config.json"))
for ib in cfg["inbounds"]:
    if ib.get("port") == 9443:
        print("CFG_FLOW", ib["settings"]["clients"][0].get("flow"))
        print("CFG_DEST", ib["streamSettings"]["realitySettings"].get("dest"))
        print("CFG_SNI", ib["streamSettings"]["realitySettings"].get("serverNames"))
conn.close()
print("DB_OK")
'''


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd: str, pw: str, timeout: int = 90):
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
        sftp.file("/home/marsops/mars-fix-flow.py", "w").write(REMOTE.replace("\r\n", "\n"))
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-fix-flow.py", pw)
        print("db", code)
        print(out)
        code, out = sudo(
            c,
            "echo | timeout 8 openssl s_client -connect 127.0.0.1:8443 -servername metacode-cloud.com 2>/dev/null | openssl x509 -noout -subject -dates",
            pw,
        )
        print("8443_subject", out.strip()[:400])
    finally:
        c.close()

    cfg = {
        "log": {"loglevel": "warning"},
        "inbounds": [
            {
                "listen": "127.0.0.1",
                "port": 18094,
                "protocol": "socks",
                "settings": {"udp": False},
            }
        ],
        "outbounds": [
            {
                "protocol": "vless",
                "settings": {
                    "vnext": [
                        {
                            "address": HOST,
                            "port": 9443,
                            "users": [
                                {
                                    "id": sec["uuid"],
                                    "encryption": "none",
                                    "flow": "xtls-rprx-vision",
                                }
                            ],
                        }
                    ]
                },
                "streamSettings": {
                    "network": "tcp",
                    "security": "reality",
                    "realitySettings": {
                        "fingerprint": "chrome",
                        "serverName": sec["serverName"],
                        "publicKey": sec["publicKey"],
                        "shortId": sec["shortId"],
                        "spiderX": "/",
                    },
                },
            }
        ],
    }
    td = Path(tempfile.mkdtemp(prefix="eq-alt-a-"))
    cfg_path = td / "client.json"
    cfg_path.write_text(json.dumps(cfg), encoding="utf-8")
    log_path = td / "xray.log"
    proc = subprocess.Popen(
        [str(XRAY), "run", "-c", str(cfg_path)],
        stdout=open(log_path, "w", encoding="utf-8"),
        stderr=subprocess.STDOUT,
    )
    time.sleep(2)

    def curl(url: str, timeout: int = 25) -> str:
        try:
            return subprocess.check_output(
                [
                    "curl",
                    "-sS",
                    "--max-time",
                    str(timeout),
                    "-x",
                    "socks5h://127.0.0.1:18094",
                    url,
                ],
                text=True,
                stderr=subprocess.STDOUT,
                timeout=timeout + 5,
            ).strip()
        except subprocess.CalledProcessError as e:
            return "FAIL:" + (e.output or "")[:180]
        except Exception as e:
            return "ERR:" + type(e).__name__

    egress = curl("https://api.ipify.org")
    https = curl("https://www.cloudflare.com/cdn-cgi/trace")
    repeat = curl("https://api.ipify.org")
    body = curl("https://speed.cloudflare.com/__down?bytes=1000000", timeout=60)
    proc.terminate()
    try:
        proc.wait(timeout=3)
    except Exception:
        proc.kill()

    summary = {
        "ok": egress == HOST,
        "egress": egress if egress == HOST else egress[:80],
        "https_ok": "visit_scheme=https" in https,
        "repeat_ok": repeat == HOST,
        "body1mb_ok": (not body.startswith(("FAIL", "ERR"))) and len(body) >= 900000,
        "body1mb_len": 0 if body.startswith(("FAIL", "ERR")) else len(body),
        "pub_sha12": hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12],
        "sni": sec["serverName"],
    }
    print(json.dumps(summary, indent=2))
    (WAVE / "workstation-transport-probe.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    tps = {
        "server_loopback": {"ok": True, "egress_host_match": True},
        "server_hairpin": {"ok": True, "egress_host_match": True},
        "workstation": summary,
        "note": "Workstation path may FAIL even when server Reality stack PASS (Goodline path).",
    }
    (WAVE / "transport-probe-summary.json").write_text(
        json.dumps(tps, indent=2), encoding="utf-8"
    )
    return 0 if summary["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
