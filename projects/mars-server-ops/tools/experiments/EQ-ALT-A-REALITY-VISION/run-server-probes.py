#!/usr/bin/env python3
"""Upload configs + remote-server-probe.sh; run loopback/hairpin. LOCAL ONLY."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
TOOLS = Path(r"X:\AI MARS\projects\mars-server-ops\tools\experiments\EQ-ALT-A-REALITY-VISION")
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
PORT = 9443


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


def cfg(addr: str, sec: dict) -> dict:
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
        sftp.put(str(TOOLS / "remote-server-probe.sh"), "/home/marsops/remote-server-probe.sh")
        for name, addr in (("loopback", "127.0.0.1"), ("hairpin", HOST)):
            with sftp.file(f"/home/marsops/mars-alt-a-{name}.json", "w") as rf:
                rf.write(json.dumps(cfg(addr, sec)))
        sftp.close()
        results = {}
        for name, addr in (("loopback", "127.0.0.1"), ("hairpin", HOST)):
            code, out = sudo(
                c,
                f"bash /home/marsops/remote-server-probe.sh {name} {addr}",
                pw,
                timeout=90,
            )
            print("====", name, "code", code)
            # redact uuid-like
            safe = re.sub(
                r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
                "[UUID]",
                out,
                flags=re.I,
            )
            print(safe[-2500:])
            (WAVE / f"server-{name}-probe.txt").write_text(safe, encoding="utf-8")
            results[name] = {
                "ok": f"EGRESS={HOST}" in out and f"DONE_{name.upper()}" in out,
                "egress_host_match": f"EGRESS={HOST}" in out,
                "xray_died": "XRAY_DIED" in out,
                "curl_fail": "CURL_FAIL" in out or "Failed to connect" in out,
            }
        summary = {
            "server_loopback": results["loopback"],
            "server_hairpin": results["hairpin"],
            "workstation": {
                "ok": False,
                "error": "SSL handshake timeout to EQVPS:9443 REALITY",
            },
        }
        (WAVE / "transport-probe-summary.json").write_text(
            json.dumps(summary, indent=2), encoding="utf-8"
        )
        print(json.dumps(summary, indent=2))
        return 0 if results["loopback"]["ok"] else 2
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
