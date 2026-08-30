#!/usr/bin/env python3
"""EQ-ALT-A server-side loopback REALITY transport probe. LOCAL ONLY."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
PORT = 9443


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd: str, pw: str, timeout: int = 180):
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
    client_cfg = {
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
                            "address": "127.0.0.1",
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
    # Also public-IP hairpin variant later
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
        with sftp.file("/home/marsops/mars-alt-a-loopback-client.json", "w") as rf:
            rf.write(json.dumps(client_cfg))
        sftp.close()
        # run xray in background as marsops (config has secrets - cleanup later)
        run_cmd = (
            "pkill -f 'xray-linux-amd64 run -c /home/marsops/mars-alt-a-loopback-client.json' || true; "
            "nohup /usr/local/x-ui/bin/xray-linux-amd64 run -c /home/marsops/mars-alt-a-loopback-client.json "
            ">/tmp/mars-alt-a-loopback.log 2>&1 & echo $!; sleep 2; "
            "curl -sS --max-time 20 -x socks5h://127.0.0.1:18095 https://api.ipify.org; echo; "
            "curl -sS --max-time 20 -x socks5h://127.0.0.1:18095 https://www.cloudflare.com/cdn-cgi/trace | head -5; "
            "pkill -f 'xray-linux-amd64 run -c /home/marsops/mars-alt-a-loopback-client.json' || true; "
            "rm -f /home/marsops/mars-alt-a-loopback-client.json; "
            "echo LOOPBACK_DONE"
        )
        # xray binary may need to be readable by marsops - usually is
        _stdin, stdout, stderr = c.exec_command(run_cmd, timeout=90)
        out = (stdout.read() + stderr.read()).decode("utf-8", "replace")
        print(out)
        (WAVE / "server-loopback-probe.txt").write_text(out, encoding="utf-8")
        ok = HOST in out and "ip=" in out and "LOOPBACK_DONE" in out
        # hairpin to public IP
        client_cfg["outbounds"][0]["settings"]["vnext"][0]["address"] = HOST
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-alt-a-hairpin-client.json", "w") as rf:
            rf.write(json.dumps(client_cfg))
        sftp.close()
        run_cmd2 = (
            "pkill -f 'mars-alt-a-hairpin-client.json' || true; "
            "nohup /usr/local/x-ui/bin/xray-linux-amd64 run -c /home/marsops/mars-alt-a-hairpin-client.json "
            ">/tmp/mars-alt-a-hairpin.log 2>&1 & sleep 2; "
            "curl -sS --max-time 20 -x socks5h://127.0.0.1:18095 https://api.ipify.org; echo; "
            "pkill -f 'mars-alt-a-hairpin-client.json' || true; "
            "rm -f /home/marsops/mars-alt-a-hairpin-client.json; "
            "echo HAIRPIN_DONE"
        )
        _stdin, stdout, stderr = c.exec_command(run_cmd2, timeout=90)
        out2 = (stdout.read() + stderr.read()).decode("utf-8", "replace")
        print(out2)
        (WAVE / "server-hairpin-probe.txt").write_text(out2, encoding="utf-8")
        hairpin_ok = HOST in out2 and "HAIRPIN_DONE" in out2
        summary = {
            "loopback_ok": ok,
            "hairpin_ok": hairpin_ok,
            "workstation_probe_ok": False,
            "workstation_probe_note": "SSL handshake timeout via isolated local xray HTTP :18094 → EQVPS:9443 REALITY",
        }
        (WAVE / "transport-probe-summary.json").write_text(
            json.dumps(summary, indent=2), encoding="utf-8"
        )
        print(json.dumps(summary, indent=2))
        return 0 if ok else 2
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
