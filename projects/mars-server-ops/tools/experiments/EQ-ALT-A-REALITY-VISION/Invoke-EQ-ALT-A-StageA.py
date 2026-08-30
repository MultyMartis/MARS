#!/usr/bin/env python3
# EQ-ALT-A Stage A orchestrator v2 — LOCAL ONLY (secrets never printed).
# Test ID: EQ-ALT-A-REALITY-VISION
# Does NOT mutate :8443 / VEESP / SSH hardening.
# Uses uploaded remote scripts so sudo -S never shares stdin with heredocs.

from __future__ import annotations

import hashlib
import json
import os
import re
import secrets
import socket
import ssl
import subprocess
import sys
import time
import uuid
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
TOOLS = Path(r"X:\AI MARS\projects\mars-server-ops\tools\experiments\EQ-ALT-A-REALITY-VISION")
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
EVIDENCE_ROOT = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01"
)
HOST = "95.216.126.173"
USER = "marsops"
XRAY_BIN = "/usr/local/x-ui/bin/xray-linux-amd64"

PORT = 9443
INBOUND_REMARK = "EQVPS-ALT-A-REALITY-VISION"
INBOUND_TAG = "inbound-vless-9443-reality-vision"
CLIENT_EMAIL = "MCA-ONE-EQ-ALT-A-REALITY-VISION"
CLIENT_SUBID = "mcaoneeqaltarealityvision"
PROFILE_DISPLAY = "MCA-ONE-EQ-ALT-A-REALITY-VISION"

DEST_CANDIDATES = [
    "www.microsoft.com:443",
    "www.cloudflare.com:443",
    "dl.google.com:443",
    "www.samsung.com:443",
    "gateway.icloud.com:443",
]

WAVE.mkdir(parents=True, exist_ok=True)
EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)


def log(msg: str) -> None:
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}"
    print(line)
    with (WAVE / "stage-a-orchestrator.log").open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def redact(s: str) -> str:
    s = re.sub(r"vless://\S+", "vless://[REDACTED]", s)
    s = re.sub(r"(?i)(private[_\s]?key\s*[:=]\s*)\S+", r"\1[REDACTED]", s)
    return s


def load_sudo_password() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(
        r"## marsops sudo password[^\n]*\n+\s*```\s*\n([^`]+?)\n```", text, re.I
    )
    if m:
        return m.group(1).strip()
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    if m:
        return m.group(1).strip().strip("`")
    raise RuntimeError("Could not parse marsops sudo password from secrets.local.md")


def connect() -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=22,
        username=USER,
        key_filename=str(KEY),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    return c


def run_user(c: paramiko.SSHClient, cmd: str, timeout: int = 120) -> tuple[int, str]:
    _stdin, stdout, stderr = c.exec_command(cmd, timeout=timeout)
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace")
    return stdout.channel.recv_exit_status(), out


def run_sudo(c: paramiko.SSHClient, cmd: str, pw: str, timeout: int = 300) -> tuple[int, str]:
    """sudo -S with password-only stdin. Never embed heredocs in cmd."""
    # Quote via JSON so bash -lc gets a single safe string.
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=timeout)
    stdin.write(pw + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace")
    out = out.replace(pw, "<REDACTED>")
    return stdout.channel.recv_exit_status(), out


def upload(c: paramiko.SSHClient, local: Path, remote: str) -> None:
    sftp = c.open_sftp()
    sftp.put(str(local), remote)
    sftp.close()


def probe_tls_dest(hostport: str) -> dict:
    host, port_s = hostport.split(":")
    info = {
        "dest": hostport,
        "ok": False,
        "error": None,
        "tls_version": None,
        "subject": None,
    }
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, int(port_s)), timeout=12) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                info["tls_version"] = ssock.version()
                cert = ssock.getpeercert()
                cn = None
                for tup in cert.get("subject", ()):
                    for k, v in tup:
                        if k == "commonName":
                            cn = v
                info["subject"] = cn
                info["ok"] = True
    except Exception as e:
        info["error"] = str(e)
    return info


def choose_dest() -> tuple[str, str]:
    results = []
    for d in DEST_CANDIDATES:
        r = probe_tls_dest(d)
        results.append(r)
        log(f"DEST_PROBE {json.dumps(r)}")
    (WAVE / "reality-dest-probes.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )
    for r in results:
        if r["ok"] and r.get("tls_version") in ("TLSv1.3", "TLSv1.2"):
            sni = r["dest"].split(":")[0]
            return r["dest"], sni
    raise RuntimeError("No suitable REALITY dest found")


def ensure_local_scripts() -> None:
    # Prefer programme tools copies; sync into wave dir.
    for name in ("remote-baseline.sh", "remote-backup.sh", "remote-mutate-runner.py"):
        src_tools = TOOLS / name
        src_wave = WAVE / name
        if src_tools.exists():
            src_wave.write_bytes(src_tools.read_bytes())
        elif not src_wave.exists():
            raise FileNotFoundError(f"Missing script {name}")


def main() -> int:
    action = sys.argv[1] if len(sys.argv) > 1 else "all"
    pw = load_sudo_password()
    log(f"ACTION={action} HOST={HOST} PORT={PORT} REMARK={INBOUND_REMARK} v2")

    if action in ("dest_probe", "all"):
        dest, sni = choose_dest()
        (WAVE / "chosen-reality-dest.json").write_text(
            json.dumps(
                {"dest": dest, "serverName": sni, "fingerprint": "chrome"}, indent=2
            ),
            encoding="utf-8",
        )
        log(f"CHOSEN_DEST={dest} SNI={sni}")
        if action == "dest_probe":
            return 0
    else:
        chosen = json.loads((WAVE / "chosen-reality-dest.json").read_text(encoding="utf-8"))
        dest, sni = chosen["dest"], chosen["serverName"]

    ensure_local_scripts()
    c = connect()
    try:
        if action in ("baseline", "all"):
            upload(c, WAVE / "remote-baseline.sh", "/home/marsops/remote-baseline.sh")
            code, out = run_sudo(c, "bash /home/marsops/remote-baseline.sh", pw)
            (WAVE / "baseline-full.txt").write_text(redact(out), encoding="utf-8")
            log(f"BASELINE_DONE code={code}")
            if code != 0:
                raise RuntimeError("baseline failed:\n" + out[-800:])
            if ":8443" not in out:
                raise RuntimeError(":8443 missing in baseline")
            if ":443" not in out:
                raise RuntimeError(":443 missing unexpectedly")
            if f":{PORT}" in out and "LISTEN" in out:
                # ss may list only if listening; if free, awk won't show 9443
                pass
            if "NGINX=absent" not in out and "NGINX=present" not in out:
                log("WARN nginx marker missing")
            if action == "baseline":
                return 0

        if action in ("backup", "all"):
            upload(c, WAVE / "remote-backup.sh", "/home/marsops/remote-backup.sh")
            code, out = run_sudo(c, "bash /home/marsops/remote-backup.sh", pw, timeout=300)
            (WAVE / "backup-remote.txt").write_text(redact(out), encoding="utf-8")
            log("BACKUP_REMOTE_DONE")
            m = re.search(r"BACKUP_TGZ=(\S+)", out)
            n = re.search(r"BACKUP_NAME=(\S+)", out)
            h = re.search(r"([a-f0-9]{64})\s+\S+\.tgz", out)
            if not (m and n and h and code == 0):
                raise RuntimeError("backup markers missing:\n" + out[-800:])
            remote_tgz, backup_name, remote_sha = m.group(1), n.group(1), h.group(1)
            run_sudo(
                c,
                f"cp {remote_tgz} /tmp/{backup_name}.tgz && chmod 644 /tmp/{backup_name}.tgz",
                pw,
            )
            local_tgz = WAVE / "backups" / f"{backup_name}.tgz"
            local_tgz.parent.mkdir(parents=True, exist_ok=True)
            sftp = c.open_sftp()
            sftp.get(f"/tmp/{backup_name}.tgz", str(local_tgz))
            sftp.close()
            run_sudo(c, f"rm -f /tmp/{backup_name}.tgz", pw)
            local_sha = hashlib.sha256(local_tgz.read_bytes()).hexdigest()
            meta = {
                "backup_name": backup_name,
                "remote_tgz": remote_tgz,
                "local_tgz": str(local_tgz),
                "sha256_remote": remote_sha,
                "sha256_local": local_sha,
                "match": remote_sha.lower() == local_sha.lower(),
                "classification": (
                    "BACKUP + RESTORE STRATEGY CONFIRMED"
                    if remote_sha.lower() == local_sha.lower()
                    else "BACKUP HASH MISMATCH"
                ),
                "rollback_summary": [
                    "1. Disable/remove inbound EQVPS-ALT-A-REALITY-VISION (port 9443) and client MCA-ONE-EQ-ALT-A-REALITY-VISION only.",
                    "2. Remove UFW allow 9443/tcp comment 'EQ-ALT-A REALITY VISION'.",
                    "3. If DB drift: stop x-ui; restore /etc/x-ui from backup etc-x-ui; restore config.json; start x-ui.",
                    "4. Verify listeners 22/443/8443/20901/2096; confirm 9443 absent; confirm :8443 RAW/TLS unchanged.",
                ],
            }
            (WAVE / "backup-meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
            (BASE / "backups" / f"{backup_name}.tgz").write_bytes(local_tgz.read_bytes())
            log(
                json.dumps(
                    {
                        k: meta[k]
                        for k in (
                            "backup_name",
                            "sha256_local",
                            "match",
                            "classification",
                            "local_tgz",
                        )
                    }
                )
            )
            if not meta["match"]:
                raise RuntimeError("backup hash mismatch")
            if action == "backup":
                return 0

        if action in ("mutate", "all"):
            code, out = run_user(c, f"ss -lntp | grep -E ':{PORT}\\b' || true")
            if f":{PORT}" in out:
                raise RuntimeError(f"port {PORT} already listening:\n{out}")

            code, out = run_sudo(c, f"{XRAY_BIN} x25519", pw)
            priv = pub = None
            for line in out.splitlines():
                low = line.lower()
                if "private" in low and (":" in line or "=" in line):
                    priv = line.split(":", 1)[-1].strip().split("=", 1)[-1].strip()
                if "public" in low and (":" in line or "=" in line):
                    pub = line.split(":", 1)[-1].strip().split("=", 1)[-1].strip()
            if not priv or not pub:
                raise RuntimeError("x25519 parse failed:\n" + redact(out))

            short_id = secrets.token_hex(8)
            client_uuid = str(uuid.uuid4())
            payload = {
                "port": PORT,
                "remark": INBOUND_REMARK,
                "tag": INBOUND_TAG,
                "client_email": CLIENT_EMAIL,
                "client_subid": CLIENT_SUBID,
                "uuid": client_uuid,
                "flow": "xtls-rprx-vision",
                "dest": dest,
                "serverNames": [sni],
                "privateKey": priv,
                "publicKey": pub,
                "shortIds": [short_id, ""],
                "fingerprint": "chrome",
                "spiderX": "/",
            }
            local_secret = {
                "test_id": "EQ-ALT-A-REALITY-VISION",
                "profile_display_name": PROFILE_DISPLAY,
                "address": HOST,
                "port": PORT,
                "protocol": "vless",
                "security": "reality",
                "network": "tcp",
                "flow": "xtls-rprx-vision",
                "fingerprint": "chrome",
                "dest": dest,
                "serverNames": [sni],
                "serverName": sni,
                "uuid": client_uuid,
                "publicKey": pub,
                "shortId": short_id,
                "privateKey_value": priv,
                "note": "REALITY SNI/serverName is dest hostname, not metacode-cloud.com",
            }
            sec_path = WAVE / "client-secrets.local.json"
            sec_path.write_text(json.dumps(local_secret, indent=2), encoding="utf-8")
            try:
                os.chmod(sec_path, 0o600)
            except Exception:
                pass

            sftp = c.open_sftp()
            with sftp.file("/home/marsops/mars-alt-a-reality-payload.json", "w") as rf:
                rf.write(json.dumps(payload))
            sftp.close()
            upload(
                c,
                WAVE / "remote-mutate-runner.py",
                "/home/marsops/mars-alt-a-reality-runner.py",
            )
            code, out = run_sudo(
                c, "python3 /home/marsops/mars-alt-a-reality-runner.py", pw
            )
            (WAVE / "mutate-result.txt").write_text(redact(out), encoding="utf-8")
            log("MUTATE " + ("OK" if "MUTATION_OK" in out else "FAIL"))
            if "MUTATION_OK" not in out:
                raise RuntimeError("mutation failed:\n" + redact(out)[-800:])

            code, out = run_sudo(
                c,
                f"ufw status | grep -E '{PORT}/tcp' || ufw allow {PORT}/tcp comment 'EQ-ALT-A REALITY VISION'",
                pw,
            )
            log("UFW " + redact(out).strip()[:300])
            code, out = run_sudo(
                c, "systemctl restart x-ui && sleep 5 && systemctl is-active x-ui", pw
            )
            log("RESTART " + out.strip())
            if "active" not in out:
                raise RuntimeError("x-ui not active after restart")
            run_sudo(
                c,
                "rm -f /home/marsops/mars-alt-a-reality-payload.json /home/marsops/mars-alt-a-reality-runner.py",
                pw,
            )
            if action == "mutate":
                return 0

        if action in ("validate", "all"):
            code, out = run_user(
                c,
                "ss -lntp | awk 'NR==1 || /:22|:443|:8443|:24443|:9443|:20901|:2096/'",
            )
            (WAVE / "post-ss.txt").write_text(out, encoding="utf-8")
            log("POST_SS\n" + out)
            if f":{PORT}" not in out or ":8443" not in out:
                raise RuntimeError("listener check failed")

            # Write tiny remote inspect script to avoid sudo+heredoc issues
            inspect = (
                "import json\n"
                "cfg=json.load(open('/usr/local/x-ui/bin/config.json'))\n"
                "for ib in cfg.get('inbounds',[]):\n"
                " p=ib.get('port')\n"
                " if p in (443,8443,24443,9443):\n"
                "  ss=ib.get('streamSettings') or {}\n"
                "  clients=(ib.get('settings') or {}).get('clients') or []\n"
                "  flows=[c.get('flow') for c in clients]\n"
                "  print('runtime',p,ib.get('protocol'),ss.get('network'),ss.get('security'),'flows',flows)\n"
                "  if ss.get('security')=='reality':\n"
                "   rs=ss.get('realitySettings') or {}\n"
                "   print(' reality_dest', rs.get('dest'), 'serverNames', rs.get('serverNames'), 'shortIds_count', len(rs.get('shortIds') or []))\n"
            )
            sftp = c.open_sftp()
            with sftp.file("/home/marsops/mars-alt-a-inspect.py", "w") as rf:
                rf.write(inspect)
            sftp.close()
            code, out = run_sudo(c, "python3 /home/marsops/mars-alt-a-inspect.py", pw)
            (WAVE / "post-runtime.txt").write_text(redact(out), encoding="utf-8")
            log("POST_RUNTIME\n" + redact(out))
            lines8443 = [ln for ln in out.splitlines() if "runtime 8443" in ln]
            if not lines8443 or "tcp" not in lines8443[0] or "tls" not in lines8443[0]:
                raise RuntimeError(":8443 regression")
            lines9443 = [ln for ln in out.splitlines() if f"runtime {PORT}" in ln]
            if (
                not lines9443
                or "reality" not in lines9443[0]
                or "xtls-rprx-vision" not in lines9443[0]
            ):
                raise RuntimeError("9443 reality/vision missing in runtime")

            code, out = run_sudo(
                c, f"{XRAY_BIN} run -test -c /usr/local/x-ui/bin/config.json", pw
            )
            (WAVE / "xray-config-test.txt").write_text(redact(out), encoding="utf-8")
            log(f"XRAY_TEST code={code}")
            ok_msg = "ok" in out.lower() or "Configuration" in out
            if code != 0 and not ok_msg:
                raise RuntimeError("xray config test failed:\n" + redact(out)[-500:])

            code, out = run_user(
                c,
                "echo | openssl s_client -connect 127.0.0.1:8443 -servername metacode-cloud.com -alpn http/1.1 2>/dev/null | grep -E 'Verify return code|subject=' || true",
            )
            (WAVE / "post-8443-tls.txt").write_text(out, encoding="utf-8")
            run_sudo(c, "rm -f /home/marsops/mars-alt-a-inspect.py", pw)
            log("SERVER_VALIDATE_PASS")
            if action == "validate":
                return 0

        if action in ("probe_client", "all"):
            sec = json.loads(
                (WAVE / "client-secrets.local.json").read_text(encoding="utf-8")
            )
            probe_port = 18094
            client_cfg = {
                "log": {"loglevel": "warning"},
                "inbounds": [
                    {
                        "tag": "http-in",
                        "port": probe_port,
                        "listen": "127.0.0.1",
                        "protocol": "http",
                        "settings": {"allowTransparent": False},
                    }
                ],
                "outbounds": [
                    {
                        "tag": "proxy",
                        "protocol": "vless",
                        "settings": {
                            "vnext": [
                                {
                                    "address": HOST,
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
            cfg_path = WAVE / "probe-client-config.local.json"
            cfg_path.write_text(json.dumps(client_cfg, indent=2), encoding="utf-8")
            xray = Path(r"C:\Program Files\v2rayN\bin\xray\xray.exe")
            if not xray.exists():
                raise RuntimeError(f"local xray missing: {xray}")
            proc = subprocess.Popen(
                [str(xray), "run", "-c", str(cfg_path)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
            time.sleep(2.5)
            results = {"probe_port": probe_port, "tests": []}
            try:
                import urllib.request

                opener = urllib.request.build_opener(
                    urllib.request.ProxyHandler(
                        {
                            "http": f"http://127.0.0.1:{probe_port}",
                            "https": f"http://127.0.0.1:{probe_port}",
                        }
                    )
                )
                try:
                    body = opener.open("https://api.ipify.org", timeout=25).read().decode()
                    results["tests"].append(
                        {
                            "name": "egress",
                            "ok": body.strip() == HOST,
                            "body": body.strip(),
                        }
                    )
                except Exception as e:
                    results["tests"].append(
                        {"name": "egress", "ok": False, "error": str(e)}
                    )
                try:
                    body = (
                        opener.open(
                            "https://www.cloudflare.com/cdn-cgi/trace", timeout=25
                        )
                        .read()
                        .decode()
                    )
                    results["tests"].append(
                        {
                            "name": "https_trace",
                            "ok": "ip=" in body,
                            "snippet": body[:200],
                        }
                    )
                except Exception as e:
                    results["tests"].append(
                        {"name": "https_trace", "ok": False, "error": str(e)}
                    )
                ok_n = 0
                for _ in range(5):
                    try:
                        opener.open(
                            "https://www.cloudflare.com/cdn-cgi/trace", timeout=25
                        ).read()
                        ok_n += 1
                    except Exception:
                        pass
                results["tests"].append(
                    {
                        "name": "https_repeat_5",
                        "ok": ok_n == 5,
                        "ok_count": ok_n,
                    }
                )
                try:
                    data = opener.open(
                        "https://speed.cloudflare.com/__down?bytes=1000000", timeout=60
                    ).read()
                    results["tests"].append(
                        {
                            "name": "body_1MB",
                            "ok": len(data) == 1000000,
                            "bytes": len(data),
                        }
                    )
                except Exception as e:
                    results["tests"].append(
                        {"name": "body_1MB", "ok": False, "error": str(e)}
                    )
            finally:
                proc.terminate()
                try:
                    proc.wait(timeout=5)
                except Exception:
                    proc.kill()

            (WAVE / "probe-transport-results.json").write_text(
                json.dumps(results, indent=2), encoding="utf-8"
            )
            safe = {
                "test_id": "EQ-ALT-A-REALITY-VISION",
                "port": PORT,
                "dest": dest,
                "profile_display_name": PROFILE_DISPLAY,
                "transport_probe": results,
                "all_ok": all(t.get("ok") for t in results["tests"]),
            }
            sess = EVIDENCE_ROOT / time.strftime("EQ-ALT-A_%Y-%m-%d_%H%M%S_prep")
            sess.mkdir(parents=True, exist_ok=True)
            (sess / "server-transport-prep.json").write_text(
                json.dumps(safe, indent=2), encoding="utf-8"
            )
            (WAVE / "evidence-session.txt").write_text(str(sess), encoding="utf-8")
            log("PROBE " + json.dumps(safe))
            return 0 if safe["all_ok"] else 2

        return 1
    finally:
        c.close()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        log(f"FATAL {type(e).__name__}: {e}")
        raise
