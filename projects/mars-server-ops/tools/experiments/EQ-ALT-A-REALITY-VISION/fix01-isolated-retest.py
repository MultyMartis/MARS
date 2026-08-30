#!/usr/bin/env python3
"""FIX-01 isolated workstation Xray transport retest + :8443 regression. Secrets not printed."""
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
XRAY = Path(
    r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ingress-deployment-raw-2026-08-27\xray-win-26.7.28\xray.exe"
)
SOCKS_PORT = 18088
OUT = WAVE / "fix01-isolated-transport-retest.json"


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


def curl_via_socks(url: str, timeout: int = 25) -> str:
    try:
        return subprocess.check_output(
            [
                "curl",
                "-sS",
                "--max-time",
                str(timeout),
                "-x",
                f"socks5h://127.0.0.1:{SOCKS_PORT}",
                url,
            ],
            text=True,
            stderr=subprocess.STDOUT,
            timeout=timeout + 8,
        ).strip()
    except subprocess.CalledProcessError as e:
        msg = (e.output or str(e))[:220]
        msg = re.sub(r"[A-Za-z0-9\-_]{40,}", "[REDACTED]", msg)
        return "FAIL:" + msg
    except Exception as e:
        return "ERR:" + type(e).__name__


def main() -> int:
    sec = json.loads((WAVE / "client-secrets.local.json").read_text(encoding="utf-8"))
    result: dict = {
        "test_id": "EQ-ALT-A-FIX-01",
        "socks_port": SOCKS_PORT,
        "pub_sha12": hashlib.sha256(sec["publicKey"].encode()).hexdigest()[:12],
        "sni": sec["serverName"],
        "flow": "xtls-rprx-vision",
        "fingerprint": "chrome",
        "port": 9443,
    }

    # :8443 regression via SSH (no profile secrets)
    pw = load_pw()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(HOST, 22, username="marsops", key_filename=str(KEY), timeout=30, allow_agent=False, look_for_keys=False)
    try:
        code, out = sudo(
            c,
            "ss -lntp | grep -E ':8443|:9443' || true; "
            "echo | timeout 8 openssl s_client -connect 127.0.0.1:8443 -servername metacode-cloud.com 2>/dev/null | openssl x509 -noout -subject 2>/dev/null || true",
            pw,
        )
        listen_8443 = ":8443" in out
        listen_9443 = ":9443" in out
        subj = ""
        for line in out.splitlines():
            if "subject=" in line.lower() or line.strip().startswith("subject="):
                subj = line.strip()
        result["regression_8443"] = {
            "listening": listen_8443,
            "subject": subj[:120],
            "ok": listen_8443 and "metacode-cloud.com" in subj,
        }
        result["listener_9443"] = listen_9443
        print("8443_listening", listen_8443)
        print("9443_listening", listen_9443)
        print("8443_subject", subj[:120])
    finally:
        c.close()

    cfg = {
        "log": {"loglevel": "warning"},
        "inbounds": [
            {
                "listen": "127.0.0.1",
                "port": SOCKS_PORT,
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
    td = Path(tempfile.mkdtemp(prefix="eq-alt-a-fix01-"))
    cfg_path = td / "client.json"
    log_path = td / "xray.log"
    cfg_path.write_text(json.dumps(cfg), encoding="utf-8")
    proc = subprocess.Popen(
        [str(XRAY), "run", "-c", str(cfg_path)],
        stdout=open(log_path, "w", encoding="utf-8"),
        stderr=subprocess.STDOUT,
    )
    time.sleep(2)
    started = proc.poll() is None
    result["xray_client_started"] = started

    egress = curl_via_socks("https://api.ipify.org", timeout=30)
    https = curl_via_socks("https://www.cloudflare.com/cdn-cgi/trace", timeout=30)
    repeat = curl_via_socks("https://api.ipify.org", timeout=30)

    # sanitize log (no secrets)
    log_tail = ""
    try:
        raw_log = log_path.read_text(encoding="utf-8", errors="replace")
        raw_log = raw_log.replace(sec["publicKey"], "[PBK]").replace(sec["uuid"], "[UUID]").replace(sec["shortId"], "[SID]")
        lines = [ln for ln in raw_log.splitlines() if ln.strip()]
        log_tail = " | ".join(lines[-8:])[:600]
    except Exception:
        log_tail = ""

    proc.terminate()
    try:
        proc.wait(timeout=3)
    except Exception:
        proc.kill()

    ok = egress == HOST and started
    https_ok = "visit_scheme=https" in https
    classification = "PASS" if ok and https_ok else ("UNSTABLE" if ok or https_ok else "FAIL")

    # interpret error class without blaming network prematurely
    err_class = "none"
    low = (log_tail + " " + egress + " " + https).lower()
    if "timeout" in low or "timed out" in low:
        err_class = "timeout"
    elif "invalid" in low and "publickey" in low.replace(" ", ""):
        err_class = "invalid_publickey"
    elif "reality" in low and ("fail" in low or "reject" in low):
        err_class = "reality_protocol"
    elif egress.startswith(("FAIL", "ERR")) and not ok:
        err_class = "proxy_fetch_fail"

    result.update(
        {
            "classification": classification,
            "ok": ok,
            "egress": egress if egress == HOST else egress[:100],
            "https_ok": https_ok,
            "repeat_ok": repeat == HOST,
            "error_class": err_class,
            "xray_log_tail_sanitized": log_tail,
            "note": "[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]",
        }
    )
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "xray_log_tail_sanitized"}, indent=2))
    print("LOG_TAIL", log_tail[:300])
    return 0 if classification == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
