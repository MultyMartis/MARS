#!/usr/bin/env python3
"""EQ-ALT-A server loopback REALITY probe via sudo/root. LOCAL ONLY."""
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
PORT = 9443
XRAY = "/usr/local/x-ui/bin/xray-linux-amd64"


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


def main() -> int:
    pw = load_pw()
    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))

    def cfg(addr: str) -> dict:
        return {
            "log": {"loglevel": "warning"},
            "inbounds": [
                {
                    "tag": "socks-in",
                    "port": 18095,
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
                                "address": addr,
                                "port": PORT,
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
                            "show": False,
                            "fingerprint": "chrome",
                            "serverName": sec["serverName"],
                            "publicKey": sec["publicKey"],
                            "shortId": sec["shortId"],
                            "spiderX": "/",
                        },
                        "tcpSettings": {"header": {"type": "none"}},
                    },
                },
                {"tag": "direct", "protocol": "freedom"},
            ],
        }

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
        results = {}
        for name, addr in (("loopback", "127.0.0.1"), ("hairpin", HOST)):
            remote_cfg = f"/tmp/mars-alt-a-{name}.json"
            remote_log = f"/tmp/mars-alt-a-{name}.log"
            sftp = c.open_sftp()
            with sftp.file(f"/home/marsops/mars-alt-a-{name}.json", "w") as rf:
                rf.write(json.dumps(cfg(addr)))
            sftp.close()
            cmd = f"""
set -e
cp /home/marsops/mars-alt-a-{name}.json {remote_cfg}
chmod 600 {remote_cfg}
pkill -f '{remote_cfg}' >/dev/null 2>&1 || true
ss -lntp | grep ':9443' || true
{XRAY} run -c {remote_cfg} >{remote_log} 2>&1 &
XPID=$!
sleep 3
if ! kill -0 $XPID 2>/dev/null; then
  echo XRAY_DIED
  cat {remote_log} | tail -40
  exit 0
fi
echo XRAY_PID=$XPID
IP=$(curl -sS --max-time 15 -x socks5h://127.0.0.1:18095 https://api.ipify.org || echo CURL_FAIL)
echo EGRESS=$IP
TRACE=$(curl -sS --max-time 15 -x socks5h://127.0.0.1:18095 https://www.cloudflare.com/cdn-cgi/trace | head -8 || true)
echo "TRACE_BEGIN"
echo "$TRACE"
echo "TRACE_END"
kill $XPID >/dev/null 2>&1 || true
wait $XPID 2>/dev/null || true
rm -f {remote_cfg} /home/marsops/mars-alt-a-{name}.json
echo DONE_{name.upper()}
"""
            code, out = sudo(c, cmd, pw, timeout=90)
            print("====", name, "code", code)
            print(out[-2000:])
            (WAVE / f"server-{name}-probe.txt").write_text(out, encoding="utf-8")
            results[name] = {
                "ok": f"EGRESS={HOST}" in out and f"DONE_{name.upper()}" in out,
                "egress_host_match": f"EGRESS={HOST}" in out,
                "xray_died": "XRAY_DIED" in out,
            }
        (WAVE / "transport-probe-summary.json").write_text(
            json.dumps(
                {
                    "server_loopback": results.get("loopback"),
                    "server_hairpin": results.get("hairpin"),
                    "workstation": {
                        "ok": False,
                        "error": "SSL handshake timeout to EQVPS:9443 REALITY",
                    },
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps(results, indent=2))
        return 0 if results.get("loopback", {}).get("ok") else 2
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
