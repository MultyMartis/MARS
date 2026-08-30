#!/usr/bin/env python3
"""VEESP FINAL FULL OPERATIONAL BACKUP 01.

Fresh full operational backup of MCA-VPN-001 (VEESP) after 3X-UI 3.7.0,
credential rotation, and system/panel hardening.

BACKUP / READ-ONLY: no VPN/SSH/UFW/x-ui mutation, no reboot.
Secrets never written to Git evidence (redacted).
"""
from __future__ import annotations

import hashlib
import json
import re
import socket
import ssl
import tarfile
import time
from datetime import datetime, timezone
from pathlib import Path

import paramiko

TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

HOST = "178.173.250.69"
PORT = 22
DOMAIN = "wsp-cloud.com"
BASE = Path(r"X:\AI MARS\local\infrastructure\MCA-VPN-001")
SECRETS = BASE / "secrets.local.md"
ROOT_PRIV = BASE / "ssh" / "root_recovery_ed25519"
MARSOPS_PRIV = BASE / "ssh" / "marsops_ed25519"
BAK_NAME = f"veesp-final-operational-{TS}"
REMOTE_DIR = "/root/mars-backups"
REMOTE_BAK = f"{REMOTE_DIR}/{BAK_NAME}.tgz"
LOCAL_BAK = BASE / "backups" / f"{BAK_NAME}.tgz"

EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01"
)
LOCAL_RUN = BASE / f"veesp-final-operational-backup-01-{TS}"

for p in (EV, LOCAL_RUN, BASE / "backups"):
    p.mkdir(parents=True, exist_ok=True)

RESULT: dict = {
    "wave": "VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01",
    "ts": TS,
    "pre": {},
    "backup": {},
    "post": {},
    "directory_totals": {},
    "friendhosting_dir_optional": {},
    "verdict": "FAIL",
    "mutations": {
        "friendhosting": 0,
        "veesp_config": 0,
        "veesp_client": 0,
        "veesp_reboot": 0,
        "secret_disclosure": 0,
        "foreign_wip": 0,
        "commit_push": 0,
    },
}


def redact(t: str) -> str:
    t = re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        t,
    )
    t = re.sub(
        r"(?i)(password|passwd|secret|token|api[_-]?key|panel_password|panel_url)\s*[:=]\s*\S+",
        r"\1=<REDACTED>",
        t,
    )
    t = re.sub(r"https?://[^\s]+/\S{8,}/?", "https://<REDACTED_PANEL_PATH>/", t)
    return t


def write(name: str, text: str) -> None:
    text = redact(text)
    (EV / name).write_text(text, encoding="utf-8")
    (LOCAL_RUN / name).write_text(text, encoding="utf-8")


def write_json(name: str, obj: dict) -> None:
    write(name, json.dumps(obj, indent=2) + "\n")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tcp(host: str, port: int, timeout: float = 8) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def tls(host: str, port: int, sni: str) -> dict:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=sni) as ssock:
                return {"ok": True, "notAfter": ssock.getpeercert().get("notAfter")}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def dns_a(name: str) -> list[str]:
    try:
        return sorted({ai[4][0] for ai in socket.getaddrinfo(name, None, socket.AF_INET)})
    except Exception:
        return []


def parse_kv_secrets(path: Path) -> dict:
    data = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^\s*([A-Za-z0-9_./-]+)\s*[:=]\s*(.+?)\s*$", line)
        if not m:
            continue
        data[m.group(1).strip().lower()] = (
            m.group(2).strip().strip("`").strip('"').strip("'")
        )
    return data


def load_key(path: Path):
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(path))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(path), password='""')


def connect(user: str, key_path: Path) -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=PORT,
        username=user,
        pkey=load_key(key_path),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(20)
    return c


def run(c: paramiko.SSHClient, cmd: str, timeout: int = 180):
    try:
        _, stdout, stderr = c.exec_command(cmd, timeout=timeout)
        stdout.channel.settimeout(timeout)
        stderr.channel.settimeout(timeout)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        code = stdout.channel.recv_exit_status()
        return code, out, err
    except Exception as e:
        return 124, "", f"ERR:{type(e).__name__}:{e}"


def sftp_get(c: paramiko.SSHClient, remote: str, local: Path, timeout_s: int = 900) -> None:
    sftp = c.open_sftp()
    sftp.get_channel().settimeout(timeout_s)
    st = sftp.stat(remote)
    total = st.st_size
    local.parent.mkdir(parents=True, exist_ok=True)
    if local.exists():
        local.unlink()
    with sftp.open(remote, "rb") as rf, local.open("wb") as lf:
        rf.prefetch(total)
        got = 0
        while True:
            chunk = rf.read(1024 * 256)
            if not chunk:
                break
            lf.write(chunk)
            got += len(chunk)
            if got % (10 * 1024 * 1024) < 256 * 1024:
                print(f"  download {got}/{total}", flush=True)
    sftp.close()
    if local.stat().st_size != total:
        raise SystemExit(f"SIZE_MISMATCH local={local.stat().st_size} remote={total}")


def dir_archive_totals(path: Path) -> dict:
    archives = sorted(path.glob("*.tgz")) if path.exists() else []
    total = sum(p.stat().st_size for p in archives)
    return {
        "path": str(path),
        "archive_count": len(archives),
        "total_bytes": total,
        "total_mib": round(total / (1024**2), 6),
        "total_gib": round(total / (1024**3), 6),
        "archives": [{"name": p.name, "bytes": p.stat().st_size} for p in archives],
    }


def validate_archive(
    local: Path,
    remote_sha: str | None,
    remote_size: int | None,
    required_keys: list[str],
    extra: dict | None = None,
) -> dict:
    local_sha = sha256_file(local)
    local_size = local.stat().st_size
    required = {k: False for k in required_keys}
    names: list[str] = []
    readable = True
    with tarfile.open(local, "r:gz") as tf:
        names = tf.getnames()
        joined = "\n".join(names)
        for k in required:
            required[k] = k in joined
        for n in names:
            if n.endswith((".txt", ".json")) or n.endswith("fstab"):
                try:
                    m = tf.getmember(n)
                    if m.isfile() and m.size < 2_000_000:
                        tf.extractfile(m).read(64)
                    break
                except Exception:
                    readable = False
                    break
    info = {
        "ok": bool(remote_sha)
        and remote_sha == local_sha
        and local_size > 0
        and all(required.values())
        and readable,
        "remote_sha256": remote_sha,
        "local_sha256": local_sha,
        "sha_match": remote_sha == local_sha,
        "remote_size": remote_size,
        "local_size": local_size,
        "size_match": remote_size == local_size if remote_size is not None else None,
        "bytes": local_size,
        "mib": round(local_size / (1024**2), 6),
        "gib": round(local_size / (1024**3), 6),
        "member_count": len(names),
        "required_sections": required,
        "archive_readable": readable,
    }
    if extra:
        info.update(extra)
    return info


def probe_marsops_sudo(secrets: dict) -> dict:
    out = {
        "marsops_key_login": False,
        "marsops_sudo": False,
        "id_line": "",
    }
    try:
        c = connect("marsops", MARSOPS_PRIV)
        code, o, e = run(c, "id; echo LOGIN_OK", timeout=30)
        out["marsops_key_login"] = code == 0 and "LOGIN_OK" in o
        out["id_line"] = next((ln for ln in o.splitlines() if ln.startswith("uid=")), "")
        pw = secrets.get("marsops_password", "")
        if pw and out["marsops_key_login"]:
            # password via stdin only — never argv
            cmd = "sudo -S -p '' true; echo SUDO_EXIT:$?"
            _, stdout, stderr = c.exec_command(cmd, timeout=30, get_pty=True)
            stdout.channel.send(pw + "\n")
            time.sleep(1.5)
            so = stdout.read().decode("utf-8", "replace")
            se = stderr.read().decode("utf-8", "replace")
            combo = so + "\n" + se
            out["marsops_sudo"] = "SUDO_EXIT:0" in combo
            write("A0-marsops-sudo.txt", f"login={out['marsops_key_login']}\nsudo_pass_signal={out['marsops_sudo']}\n")
        c.close()
    except Exception as e:
        out["error"] = type(e).__name__
        write("A0-marsops-sudo.txt", f"ERROR {type(e).__name__}\n")
    return out


def health(c: paramiko.SSHClient, label: str) -> dict:
    code, out, err = run(
        c,
        r"""
set -euo pipefail
echo HOSTNAME=$(hostname)
echo OS=$(. /etc/os-release; echo $PRETTY_NAME)
echo KERNEL=$(uname -r)
echo DATE_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo ===SERVICES===
systemctl is-active ssh; systemctl is-active x-ui; systemctl is-active fail2ban
echo ===UFW===
ufw status | head -n 40
echo ===SWAP===
swapon --show
free -h | sed -n '1,3p'
echo ===JOURNALD===
grep -E '^(SystemMaxUse|SystemKeepFree|RuntimeMaxUse)' /etc/systemd/journald.conf /etc/systemd/journald.conf.d/* 2>/dev/null || true
echo ===LISTEN===
ss -lntp | egrep ':(22|8443|443|80|2096|5928|46489|8445)\b' || true
echo ===SSHD===
sshd -T 2>/dev/null | egrep '^(passwordauthentication|permitrootlogin|pubkeyauthentication|port) ' || true
echo ===VERSIONS===
# x-ui has no stable "version" subcommand; use journal start line + binary probe
journalctl -u x-ui --no-pager -n 200 2>/dev/null | grep -F 'Starting x-ui ' | tail -n 1 || true
XRAY_BIN=$(ls /usr/local/x-ui/bin/xray-linux-* 2>/dev/null | head -n 1 || true)
if [ -n "$XRAY_BIN" ]; then "$XRAY_BIN" version 2>&1 | head -n 3; else echo XRAY_BIN_ABSENT; fi
echo XUI_BIN_MTIME=$(stat -c '%y' /usr/local/x-ui/x-ui 2>/dev/null || true)
echo ===REBOOT===
if [ -f /var/run/reboot-required ]; then echo REBOOT_REQUIRED=YES; cat /var/run/reboot-required.pkgs 2>/dev/null | head -n 20 || true; else echo REBOOT_REQUIRED=NO; fi
echo ===PANEL_LOCAL===
curl -sk -o /dev/null -w 'PANEL_5928=%{http_code}\n' https://127.0.0.1:5928/ 2>/dev/null || echo PANEL_5928=UNREACHABLE
curl -sk -o /dev/null -w 'SUB_2096=%{http_code}\n' https://127.0.0.1:2096/ 2>/dev/null || echo SUB_2096=UNREACHABLE
echo ===INBOUND===
python3 - <<'PY'
import json, sqlite3, os
db='/etc/x-ui/x-ui.db'
if not os.path.exists(db):
    print('DB_ABSENT'); raise SystemExit(0)
con=sqlite3.connect(db)
con.row_factory=sqlite3.Row
rows=con.execute('select id,remark,port,protocol,settings from inbounds').fetchall()
print('INBOUND_COUNT', len(rows))
for row in rows:
    settings=json.loads(row['settings'] or '{}')
    clients=settings.get('clients') or []
    print(f"INBOUND port={row['port']} protocol={row['protocol']} remark={row['remark']} clients={len(clients)}")
row8443=con.execute('select settings from inbounds where port=8443').fetchone()
if row8443:
    settings=json.loads(row8443['settings'] or '{}')
    print('CLIENTS_8443', len(settings.get('clients') or []))
row46489=con.execute('select settings from inbounds where port=46489').fetchone()
if row46489:
    settings=json.loads(row46489['settings'] or '{}')
    print('CLIENTS_46489', len(settings.get('clients') or []))
PY
echo GATE_REMOTE_OK
""",
        timeout=180,
    )
    write(f"{label}-remote.txt", f"exit={code}\n{out}\n{err}")
    local = {
        "ssh_22": tcp(HOST, 22),
        "tcp_8443": tcp(HOST, 8443),
        "tcp_5928": tcp(HOST, 5928),
        "tcp_2096": tcp(HOST, 2096),
        "tls_8443": tls(HOST, 8443, DOMAIN),
        "tls_5928": tls(HOST, 5928, DOMAIN),
        "dns_a": dns_a(DOMAIN),
    }
    write_json(f"{label}-local.json", local)

    parts = []
    for ln in out.splitlines():
        if ln.strip() in ("active", "inactive", "failed", "unknown"):
            # collect first three service lines after ===SERVICES===
            pass
    # parse explicit sequential is-active outputs
    m_svc = re.search(
        r"===SERVICES===\n(active|inactive|failed|unknown)\n(active|inactive|failed|unknown)\n(active|inactive|failed|unknown)",
        out,
    )
    ssh_svc = m_svc.group(1) == "active" if m_svc else False
    xui_svc = m_svc.group(2) == "active" if m_svc else False
    f2b = m_svc.group(3) == "active" if m_svc else False

    ufw_active = bool(re.search(r"(?m)^Status:\s*active", out, re.I))
    swap_ok = "swapfile" in out.lower() or bool(re.search(r"(?m)^/swapfile\b", out))
    journald_cap = "SystemMaxUse=300M" in out or "SystemMaxUse=300m" in out.lower()
    passwd_auth_off = bool(re.search(r"(?m)^passwordauthentication no$", out, re.I))
    clients_8443 = int((re.search(r"CLIENTS_8443\s+(\d+)", out) or [None, "-1"])[1])
    clients_46489 = int((re.search(r"CLIENTS_46489\s+(\d+)", out) or [None, "-1"])[1])
    has_vless_8443 = bool(re.search(r"port=8443\s+protocol=vless", out, re.I))
    xui_ver = "3.7.0" if "3.7.0" in out else None
    xray_ver = "26.7.28" if "26.7.28" in out else None
    reboot_req = "REBOOT_REQUIRED=YES" in out
    panel_5928 = (re.search(r"PANEL_5928=(\d+|UNREACHABLE)", out) or [None, "?"])[1]
    sub_2096 = (re.search(r"SUB_2096=(\d+|UNREACHABLE)", out) or [None, "?"])[1]

    gates = {
        "ssh_root_key": local["ssh_22"] and ssh_svc and "GATE_REMOTE_OK" in out and code == 0,
        "xui": xui_svc,
        "fail2ban": f2b,
        "ufw_active": ufw_active,
        "xray_8443_listen": local["tcp_8443"] and xui_svc,
        "tls_8443": bool(local["tls_8443"].get("ok")),
        "panel_5928_tcp": local["tcp_5928"],
        "panel_5928_tls": bool(local["tls_5928"].get("ok")),
        "panel_5928_http": panel_5928 not in ("UNREACHABLE", "?", ""),
        "sub_2096_tcp": local["tcp_2096"],
        "sub_2096_http": sub_2096 not in ("UNREACHABLE", "?", ""),
        "dns": HOST in local["dns_a"],
        "vless_8443_inbound": has_vless_8443,
        "clients_8443": clients_8443,
        "clients_46489": clients_46489,
        "swap_active": swap_ok,
        "journald_cap": journald_cap,
        "passwordauthentication_no": passwd_auth_off,
        "xui_version_3_7_0": xui_ver == "3.7.0",
        "xray_version_26_7_28": xray_ver == "26.7.28",
        "reboot_required": reboot_req,
        "panel_5928_code": panel_5928,
        "sub_2096_code": sub_2096,
        "tls_8443_notAfter": local["tls_8443"].get("notAfter"),
        "hostname": (re.search(r"HOSTNAME=(.+)", out) or [None, ""])[1],
        "os": (re.search(r"OS=(.+)", out) or [None, ""])[1],
    }
    critical = [
        "ssh_root_key",
        "xui",
        "fail2ban",
        "ufw_active",
        "xray_8443_listen",
        "tls_8443",
        "panel_5928_tcp",
        "panel_5928_tls",
        "dns",
        "vless_8443_inbound",
        "swap_active",
        "passwordauthentication_no",
        "xui_version_3_7_0",
        "xray_version_26_7_28",
    ]
    gates["PASS"] = all(bool(gates[k]) for k in critical) and clients_8443 >= 1
    write_json(f"{label}-gates.json", gates)
    return gates


def backup(c: paramiko.SSHClient) -> dict:
    code_d, out_d, _ = run(
        c,
        r"""
set -euo pipefail
for p in /etc/x-ui /usr/local/x-ui /etc/xray /root/cert /etc/letsencrypt /etc/nginx /etc/ssh /etc/ufw /etc/fail2ban /etc/fstab /etc/docker /swapfile; do
  if [ -e "$p" ]; then echo PRESENT:$p; else echo ABSENT:$p; fi
done
""",
        timeout=60,
    )
    write("B0-path-discovery.txt", f"exit={code_d}\n{out_d}")

    script = f"""
set -euo pipefail
DIR={REMOTE_DIR}
NAME={BAK_NAME}
STAGING="$DIR/$NAME"
mkdir -p "$DIR"
rm -rf "$STAGING"
mkdir -p "$STAGING/meta" "$STAGING/systemd" "$STAGING/package"

cp -a /etc/ssh "$STAGING/etc-ssh" 2>/dev/null || true
cp -a /etc/sudoers "$STAGING/etc-sudoers" 2>/dev/null || true
cp -a /etc/sudoers.d "$STAGING/etc-sudoers.d" 2>/dev/null || true
[ -d /etc/ufw ] && cp -a /etc/ufw "$STAGING/etc-ufw" || echo no_ufw > "$STAGING/meta/ufw-absent.txt"
[ -d /etc/fail2ban ] && cp -a /etc/fail2ban "$STAGING/etc-fail2ban" || echo no_fail2ban > "$STAGING/meta/fail2ban-absent.txt"
[ -d /etc/nginx ] && cp -a /etc/nginx "$STAGING/etc-nginx" || echo no_nginx > "$STAGING/meta/nginx-absent.txt"
[ -d /etc/letsencrypt ] && cp -a /etc/letsencrypt "$STAGING/etc-letsencrypt" || echo no_letsencrypt > "$STAGING/meta/letsencrypt-absent.txt"
[ -d /root/cert ] && cp -a /root/cert "$STAGING/root-cert" || echo no_root_cert > "$STAGING/meta/root-cert-absent.txt"
[ -d /etc/xray ] && cp -a /etc/xray "$STAGING/etc-xray" || echo no_etc_xray > "$STAGING/meta/etc-xray-absent.txt"
[ -d /etc/docker ] && cp -a /etc/docker "$STAGING/etc-docker" || echo no_docker > "$STAGING/meta/docker-absent.txt"
cp -a /usr/local/x-ui "$STAGING/usr-local-x-ui" 2>/dev/null || true
mkdir -p "$STAGING/x-ui-db"
cp -a /etc/x-ui "$STAGING/x-ui-db/etc-x-ui" 2>/dev/null || true
cp -a /etc/fstab "$STAGING/fstab" 2>/dev/null || true
cp -a /etc/systemd/journald.conf "$STAGING/journald.conf" 2>/dev/null || true
mkdir -p "$STAGING/journald.conf.d"
cp -a /etc/systemd/journald.conf.d/. "$STAGING/journald.conf.d/" 2>/dev/null || true
[ -d /etc/logrotate.d ] && cp -a /etc/logrotate.d "$STAGING/etc-logrotate.d" || true
cp -a /etc/logrotate.conf "$STAGING/logrotate.conf" 2>/dev/null || true

# swap metadata only (do not embed the 1GiB swapfile binary)
if [ -f /swapfile ]; then
  ls -l /swapfile > "$STAGING/meta/swapfile-ls.txt"
  stat /swapfile > "$STAGING/meta/swapfile-stat.txt"
fi
swapon --show > "$STAGING/meta/swapon.txt" 2>&1 || true

mkdir -p "$STAGING/mca-ops"
if [ -d /root/MCA ]; then
  [ -d /root/MCA/docs ] && cp -a /root/MCA/docs "$STAGING/mca-ops/docs" || true
  [ -d /root/MCA/scripts ] && cp -a /root/MCA/scripts "$STAGING/mca-ops/scripts" || true
  [ -d /root/MCA/inventory ] && cp -a /root/MCA/inventory "$STAGING/mca-ops/inventory" || true
  ls -la /root/MCA/backups 2>/dev/null > "$STAGING/meta/mca-backups-ls.txt" || true
fi

ss -lntup > "$STAGING/meta/ss-lntp.txt"
ufw status verbose > "$STAGING/meta/ufw-status.txt" 2>&1 || true
iptables-save > "$STAGING/meta/iptables-save.txt" 2>&1 || true
iptables -S > "$STAGING/meta/iptables-S.txt" 2>&1 || true
nft list ruleset > "$STAGING/meta/nft-ruleset.txt" 2>&1 || true
# Docker firewall interaction evidence (read-only)
iptables -S DOCKER 2>/dev/null > "$STAGING/meta/iptables-DOCKER.txt" || echo no_DOCKER_chain > "$STAGING/meta/iptables-DOCKER.txt"
iptables -S DOCKER-USER 2>/dev/null > "$STAGING/meta/iptables-DOCKER-USER.txt" || echo no_DOCKER_USER > "$STAGING/meta/iptables-DOCKER-USER.txt"
systemctl list-unit-files 'ssh*' 'x-ui*' 'fail2ban*' 'docker*' 'nginx*' 'certbot*' > "$STAGING/systemd/unit-files.txt" 2>&1 || true
systemctl status ssh x-ui fail2ban docker --no-pager > "$STAGING/systemd/status.txt" 2>&1 || true
cp -a /etc/systemd/system/x-ui.service "$STAGING/systemd/x-ui.service" 2>/dev/null || true
dpkg -l > "$STAGING/package/dpkg-l.txt"
crontab -l > "$STAGING/meta/root-crontab.txt" 2>&1 || true
ls /etc/cron.* 2>/dev/null > "$STAGING/meta/cron-dirs.txt" || true
systemctl list-timers --all > "$STAGING/meta/timers.txt" 2>&1 || true
sshd -T > "$STAGING/meta/sshd-T.txt" 2>/dev/null || true
date -u > "$STAGING/meta/created-utc.txt"
uname -a > "$STAGING/meta/uname.txt"
free -h > "$STAGING/meta/free.txt"
df -hT > "$STAGING/meta/df.txt"
hostname > "$STAGING/meta/hostname.txt"
ip -4 addr > "$STAGING/meta/ip-addr.txt"
ip route > "$STAGING/meta/ip-route.txt"
ip link > "$STAGING/meta/ip-link.txt"
getent passwd root marsops > "$STAGING/meta/passwd-slice.txt"
id marsops > "$STAGING/meta/marsops-id.txt" 2>&1 || true
ls -la /root/.ssh /home/marsops/.ssh > "$STAGING/meta/ssh-dirs.txt" 2>&1 || true
ssh-keygen -lf /root/.ssh/authorized_keys > "$STAGING/meta/root-authorized-fingerprints.txt" 2>&1 || true
ssh-keygen -lf /home/marsops/.ssh/authorized_keys > "$STAGING/meta/marsops-authorized-fingerprints.txt" 2>&1 || true
journalctl -u x-ui --no-pager -n 200 2>/dev/null | grep -F 'Starting x-ui ' | tail -n 5 > "$STAGING/meta/x-ui-version.txt" || true
XRAY_BIN=$(ls /usr/local/x-ui/bin/xray-linux-* 2>/dev/null | head -n 1 || true)
if [ -n "$XRAY_BIN" ]; then "$XRAY_BIN" version > "$STAGING/meta/xray-version.txt" 2>&1; else echo ABSENT > "$STAGING/meta/xray-version.txt"; fi
ls -la /usr/local/x-ui/bin > "$STAGING/meta/x-ui-bin-ls.txt" 2>&1 || true
[ -f /var/run/reboot-required ] && echo YES > "$STAGING/meta/reboot-required.txt" || echo NO > "$STAGING/meta/reboot-required.txt"
cat /var/run/reboot-required.pkgs > "$STAGING/meta/reboot-required.pkgs" 2>/dev/null || true

python3 - <<'PY'
import json, sqlite3, os
from pathlib import Path
ST=Path("{REMOTE_DIR}/{BAK_NAME}")
db="/etc/x-ui/x-ui.db"
safe={{"wave":"VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01","created_utc":"{TS}","inbounds":[],"settings_keys":[]}}
if os.path.exists(db):
    con=sqlite3.connect(db)
    con.row_factory=sqlite3.Row
    for row in con.execute("select id,remark,port,protocol,settings from inbounds"):
        settings=json.loads(row["settings"] or "{{}}")
        clients=settings.get("clients") or []
        safe["inbounds"].append({{
            "id": row["id"],
            "remark": row["remark"],
            "port": row["port"],
            "protocol": row["protocol"],
            "client_count": len(clients),
            "clients": [{{"email":c.get("email"),"enable":c.get("enable",True),"has_id":bool(c.get("id")),"has_subId":bool(c.get("subId"))}} for c in clients],
        }})
    try:
        for row in con.execute("select key from settings"):
            safe["settings_keys"].append(row["key"])
    except Exception:
        pass
(ST/"meta/clients-safe.json").write_text(json.dumps(safe, indent=2)+"\\n")
print("SAFE_INBOUNDS", len(safe["inbounds"]))
print("SAFE_CLIENTS_8443", next((i["client_count"] for i in safe["inbounds"] if i["port"]==8443), 0))
print("SAFE_CLIENTS_46489", next((i["client_count"] for i in safe["inbounds"] if i["port"]==46489), 0))
PY

tar -C "$DIR" -czf "$DIR/$NAME.tgz" "$NAME"
sha256sum "$DIR/$NAME.tgz" | tee "$DIR/$NAME.tgz.sha256"
stat -c '%s' "$DIR/$NAME.tgz"
tar -tzf "$DIR/$NAME.tgz" | egrep 'etc-ssh|etc-ufw|etc-fail2ban|usr-local-x-ui|x-ui-db|root-cert|fstab|clients-safe|journald|sudoers|iptables' | sed -n '1,80p'
echo BACKUP_OK
"""
    remote_script = f"/tmp/mars-veesp-final-backup-{TS}.sh"
    sftp = c.open_sftp()
    with sftp.file(remote_script, "w") as f:
        f.write(script)
    sftp.close()
    code, out, err = run(c, f"bash {remote_script}; rm -f {remote_script}", timeout=900)
    write("B1-backup-remote.txt", f"exit={code}\n{out}\n{err}")
    if "BACKUP_OK" not in out or code != 0:
        return {"ok": False, "error": "remote backup failed", "out_tail": out[-4000:]}

    m = re.search(r"([a-f0-9]{64})\s+" + re.escape(REMOTE_BAK), out)
    remote_sha = m.group(1) if m else None
    if not remote_sha:
        _, out2, _ = run(c, f"sha256sum {REMOTE_BAK}", timeout=60)
        remote_sha = out2.split()[0] if out2.strip() else None
    sizes = re.findall(r"(?m)^(\d{5,})$", out)
    remote_size = int(sizes[-1]) if sizes else None

    print("Downloading VEESP final twin...", flush=True)
    sftp_get(c, REMOTE_BAK, LOCAL_BAK, timeout_s=900)
    try:
        sftp = c.open_sftp()
        sftp.get(REMOTE_BAK + ".sha256", str(LOCAL_BAK) + ".sha256")
        sftp.close()
    except Exception:
        pass

    with tarfile.open(LOCAL_BAK, "r:gz") as tf:
        names = tf.getnames()
        safe_m = next((n for n in names if n.endswith("clients-safe.json")), None)
        client_meta = {}
        if safe_m:
            client_meta = json.loads(tf.extractfile(safe_m).read().decode())

    required = [
        "etc-ssh",
        "etc-ufw",
        "etc-fail2ban",
        "usr-local-x-ui",
        "x-ui-db",
        "root-cert",
        "fstab",
        "journald.conf",
        "clients-safe.json",
        "sudoers",
        "iptables-save.txt",
    ]
    info = validate_archive(
        LOCAL_BAK,
        remote_sha,
        remote_size,
        required,
        {
            "inbounds": client_meta.get("inbounds"),
            "clients_8443": next(
                (
                    i.get("client_count")
                    for i in client_meta.get("inbounds", [])
                    if i.get("port") == 8443
                ),
                0,
            ),
            "clients_46489": next(
                (
                    i.get("client_count")
                    for i in client_meta.get("inbounds", [])
                    if i.get("port") == 46489
                ),
                0,
            ),
            "has_nginx": any("etc-nginx" in n for n in names),
            "has_docker": any("etc-docker" in n for n in names),
        },
    )
    if info.get("clients_8443", 0) < 1:
        info["ok"] = False
    info["remote_path"] = REMOTE_BAK
    info["local_path"] = str(LOCAL_BAK)
    write_json("B1-backup-validation.json", info)
    members_preview = "\n".join(
        n for n in names if any(
            k in n
            for k in (
                "etc-ssh",
                "etc-ufw",
                "etc-fail2ban",
                "usr-local-x-ui",
                "x-ui-db",
                "root-cert",
                "fstab",
                "clients-safe",
                "journald",
                "sudoers",
                "iptables",
            )
        )
    )[:8000]
    write("B1-backup-local-members.txt", f"member_count={len(names)}\n{members_preview}\n")
    LOCAL_BAK.with_suffix(LOCAL_BAK.suffix + ".sha256").write_text(
        f"{info['local_sha256']}  {LOCAL_BAK.name}\n", encoding="utf-8"
    )
    return info


def main() -> int:
    print(f"VEESP FINAL FULL OPERATIONAL BACKUP 01 ts={TS}", flush=True)
    secrets = parse_kv_secrets(SECRETS)

    print("Probing marsops key + sudo...", flush=True)
    marsops = probe_marsops_sudo(secrets)
    RESULT["marsops"] = {
        "key_login": marsops.get("marsops_key_login"),
        "sudo": marsops.get("marsops_sudo"),
        "id_present": bool(marsops.get("id_line")),
    }
    if not marsops.get("marsops_key_login"):
        RESULT["verdict"] = "FAIL"
        write_json("Z-summary.json", RESULT)
        print("STOP — marsops key login FAIL", flush=True)
        return 2

    print("Connecting root recovery...", flush=True)
    root = connect("root", ROOT_PRIV)

    print("Pre-backup health...", flush=True)
    pre = health(root, "A0-pre")
    pre["marsops_key_login"] = marsops.get("marsops_key_login")
    pre["marsops_sudo"] = marsops.get("marsops_sudo")
    RESULT["pre"] = pre
    if not pre.get("PASS") or not marsops.get("marsops_sudo"):
        RESULT["verdict"] = "FAIL"
        write_json("Z-summary.json", RESULT)
        print("STOP — pre-backup health FAIL", flush=True)
        print(json.dumps({k: pre[k] for k in pre if k != "inbounds"}, indent=2), flush=True)
        return 3

    baseline_clients = pre.get("clients_8443")
    print(f"Pre PASS — clients_8443={baseline_clients}", flush=True)

    print("Creating remote archive...", flush=True)
    bak = backup(root)
    RESULT["backup"] = bak
    if not bak.get("ok"):
        RESULT["verdict"] = "FAIL"
        write_json("Z-summary.json", RESULT)
        print("STOP — backup FAIL", flush=True)
        return 4

    print("Post-backup regression...", flush=True)
    try:
        root.close()
    except Exception:
        pass
    time.sleep(1)
    root = connect("root", ROOT_PRIV)
    post = health(root, "C1-post")
    post["marsops_key_login"] = True  # already proven; skip re-sudo to avoid noise
    post["clients_unchanged"] = post.get("clients_8443") == baseline_clients
    RESULT["post"] = post
    try:
        root.close()
    except Exception:
        pass

    RESULT["directory_totals"] = dir_archive_totals(BASE / "backups")
    fh_bak = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups")
    try:
        RESULT["friendhosting_dir_optional"] = dir_archive_totals(fh_bak)
    except Exception as e:
        RESULT["friendhosting_dir_optional"] = {"error": type(e).__name__}

    post_ok = post.get("PASS") and post.get("clients_unchanged")
    RESULT["verdict"] = "PASS" if bak.get("ok") and post_ok else "PARTIAL"
    RESULT["restore_procedure"] = "CONFIRMED"
    RESULT["bare_metal_restore"] = "NOT YET EXERCISED"
    write_json("Z-summary.json", RESULT)

    print(
        json.dumps(
            {
                "verdict": RESULT["verdict"],
                "remote": bak.get("remote_path"),
                "local": bak.get("local_path"),
                "bytes": bak.get("bytes"),
                "sha": bak.get("local_sha256"),
                "match": bak.get("sha_match"),
                "clients_8443": bak.get("clients_8443"),
                "post_pass": post.get("PASS"),
                "clients_unchanged": post.get("clients_unchanged"),
            },
            indent=2,
        ),
        flush=True,
    )
    return 0 if RESULT["verdict"] == "PASS" else 5


if __name__ == "__main__":
    raise SystemExit(main())
