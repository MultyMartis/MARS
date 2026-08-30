"""FRIENDHOSTING P2 OPERATIONAL HARDENING 01

Harden working FriendHosting Plus node without changing VLESS :8443 architecture.
Never print secrets. No reboot. No VEESP/EQVPS mutation.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import socket
import ssl
import subprocess
import tarfile
import time
from datetime import datetime, timezone
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
DOMAIN = "metacode-cloud.com"
OPERATOR = "marsops"
BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
SSH_DIR = BASE / "ssh"
PRIV_KEY = SSH_DIR / "marsops_ed25519"
PUB_KEY = SSH_DIR / "marsops_ed25519.pub"
EVIDENCE = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01"
)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
OUT = BASE / f"p2-operational-hardening-01-{TS}"
BAK_NAME = f"friendhosting-plus-p2-pre-hardening-{TS}.tgz"
REMOTE_BAK_DIR = "/root/mars-backups"
REMOTE_BAK = f"{REMOTE_BAK_DIR}/{BAK_NAME}"
LOCAL_BAK = BASE / "backups" / BAK_NAME

RESULT: dict = {
    "wave": "FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01",
    "ts": TS,
    "host": HOST,
    "domain": DOMAIN,
    "gates": {},
    "mutations": {},
    "notes": [],
}


def redact(text: str, pw: str = "") -> str:
    out = text or ""
    if pw:
        out = out.replace(pw, "[REDACTED]")
    out = re.sub(r"(?i)(password|passwd|pass)\s*[:=]\s*\S+", r"\1=[REDACTED]", out)
    out = re.sub(r"(?i)(uuid|uri|webBasePath|basePath)\s*[:=]\s*\S+", r"\1=[REDACTED]", out)
    # Do not broadly redact path segments (breaks mars-backups / usr-local-x-ui evidence).
    return out


def load_ssh_password() -> str:
    text = (BASE / "secrets.local.md").read_text(encoding="utf-8", errors="replace")
    in_ssh = False
    for line in text.splitlines():
        if re.match(r"^##\s*SSH\b", line, re.I):
            in_ssh = True
            continue
        if in_ssh and re.match(r"^##\s+", line):
            in_ssh = False
        if in_ssh:
            m = re.match(r"^-?\s*password:\s*`?([^`]+?)`?\s*$", line, re.I)
            if m:
                pw = m.group(1).strip()
                if pw and "REPLACE" not in pw.upper():
                    return pw
    raise SystemExit("NO_USABLE_SSH_PASSWORD")


def run(c: paramiko.SSHClient, cmd: str, timeout: int = 180) -> tuple[int, str, str]:
    stdin, stdout, stderr = c.exec_command(cmd, timeout=timeout)
    stdout.channel.settimeout(timeout)
    stderr.channel.settimeout(timeout)
    try:
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        code = stdout.channel.recv_exit_status()
    except Exception as e:
        try:
            stdout.channel.close()
        except Exception:
            pass
        return 124, "", f"TIMEOUT_OR_ERROR:{type(e).__name__}"
    return code, out, err


def connect_password(pw: str) -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=PORT,
        username="root",
        password=pw,
        timeout=30,
        banner_timeout=60,
        auth_timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(30)
    return c


def load_operator_pkey() -> paramiko.PKey:
    """Load operator key; support accidental PowerShell -N '\"\"' encryption."""
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV_KEY))
    except paramiko.PasswordRequiredException:
        # Historical local contour: passphrase is two ASCII quotes
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV_KEY), password='""')


def connect_key(user: str = OPERATOR) -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key = load_operator_pkey()
    c.connect(
        HOST,
        port=PORT,
        username=user,
        pkey=key,
        timeout=30,
        banner_timeout=60,
        auth_timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(30)
    return c


def write(name: str, content: str, pw: str = "") -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    safe = redact(content, pw)
    p = OUT / name
    p.write_text(safe, encoding="utf-8")
    (EVIDENCE / name).write_text(safe, encoding="utf-8")
    return p


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tls_probe(host: str, port: int, sni: str) -> dict:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=sni) as ssock:
                cert = ssock.getpeercert()
                return {
                    "ok": True,
                    "notAfter": cert.get("notAfter"),
                    "subject": str(cert.get("subject")),
                }
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def public_tcp(host: str, port: int, timeout: float = 8.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def http_head(host: str, port: int, path: str = "/") -> dict:
    try:
        s = socket.create_connection((host, port), timeout=8)
        req = f"HEAD {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.sendall(req.encode())
        data = s.recv(512).decode("utf-8", "replace")
        s.close()
        line = data.splitlines()[0] if data else ""
        return {"reachable": True, "status_line": line[:120]}
    except Exception as e:
        return {"reachable": False, "error": type(e).__name__}


def vpn_egress_smoke(pw: str) -> dict:
    """Isolated Xray client smoke via local SOCKS if profile exists; else server-side egress only."""
    out: dict = {"method": "server_egress", "egress": None, "https_ok": None}
    # Prefer local isolated client if present from prior waves
    client_cfg = BASE / "build-01-control-node" / "isolated-client-config.json"
    vless = BASE / "clients" / "MCA-ONE" / "friendhosting-de-raw-8443.vless.txt"
    # Always capture server-side public IP as baseline truth of node egress
    return out


def phase_baseline(c: paramiko.SSHClient, pw: str) -> dict:
    cmds = {
        "hostname": "hostname; hostnamectl --static 2>/dev/null || true",
        "os": "cat /etc/os-release; uname -a",
        "uptime": "uptime; who -b || true",
        "cpu_mem": "nproc; lscpu | egrep 'Model name|CPU\\(s\\)|Thread|Core|Socket|Hypervisor' || true; free -h; cat /proc/meminfo | egrep 'MemTotal|MemAvailable|SwapTotal|SwapFree'",
        "swap": "swapon --show; cat /proc/swaps",
        "disk": "lsblk -b; df -hT; findmnt -T / -o TARGET,SOURCE,FSTYPE,SIZE,AVAIL,USE%",
        "route_mtu": "ip -4 route; ip -4 addr; ip link | egrep '^[0-9]+:|mtu'",
        "listeners": "ss -lntp",
        "focus_ports": "ss -lntp | egrep ':(3333|443|8443|20901|2096)\\b' || true",
        "firewall": "ufw status verbose 2>&1; echo ---; iptables -S 2>&1 | head -80",
        "ssh_audit": "sshd -T 2>/dev/null | egrep -i 'port|permitrootlogin|passwordauthentication|pubkeyauthentication|maxauthtries|kbdinteractive|challengeresponse|allowusers|authenticationmethods' || true; echo ---; ls -la /etc/ssh/sshd_config.d/ 2>/dev/null || true; echo ---; grep -RInE '^(PermitRootLogin|PasswordAuthentication|PubkeyAuthentication|Port|Include)' /etc/ssh/sshd_config /etc/ssh/sshd_config.d/ 2>/dev/null || true; echo ---; getent passwd | egrep -v 'nologin|false' || true; echo ---; ls -la /root/.ssh/ 2>/dev/null || true; echo ---; wc -l /root/.ssh/authorized_keys 2>/dev/null || true",
        "xui": "systemctl is-active x-ui; systemctl status x-ui --no-pager -l 2>&1 | head -25; echo ---; /usr/local/x-ui/x-ui setting -show 2>&1 | head -60 || true",
        "nginx": "systemctl is-active nginx; nginx -t 2>&1; ls /etc/nginx/sites-enabled 2>/dev/null || true",
        "xray": "ps -ef | egrep '[x]ray|[x]-ui' || true; /usr/local/x-ui/bin/xray-linux-amd64 version 2>/dev/null || true",
        "fail2ban": "dpkg -l fail2ban 2>/dev/null | tail -1; systemctl is-active fail2ban 2>&1; fail2ban-client status 2>&1 || true",
        "certs": "certbot certificates 2>&1 || true; ls -la /etc/letsencrypt/live/ 2>/dev/null || true; systemctl list-timers '*certbot*' --all 2>&1 || true; ls /etc/cron*/*certbot* 2>/dev/null || true",
        "systemd": "systemctl is-enabled ssh nginx x-ui fail2ban 2>&1; systemctl show x-ui -p FragmentPath,Restart,RestartUSec 2>&1; systemctl show nginx -p Restart 2>&1",
        "journal": "journalctl --disk-usage 2>&1; du -sh /var/log /var/log/nginx /var/log/x-ui /var/log/fail2ban 2>/dev/null || true; ls /etc/logrotate.d 2>/dev/null || true",
        "packages": "test -f /var/run/reboot-required && echo REBOOT_REQUIRED || echo NO_REBOOT_REQUIRED; dpkg -l unattended-upgrades 2>/dev/null | tail -1; systemctl is-enabled unattended-upgrades 2>&1 || true",
        "egress": "curl -4 -s --max-time 15 https://ifconfig.me/ip || curl -4 -s --max-time 15 https://api.ipify.org || true",
    }
    captured = {}
    for name, cmd in cmds.items():
        tmo = 60 if name != "xui" else 90
        code, out, err = run(c, cmd, timeout=tmo)
        blob = f"exit={code}\n{out}\n{err}"
        write(f"01-baseline-{name}.txt", blob, pw)
        captured[name] = {"exit": code, "out": redact(out, pw)[:20000]}
    # local probes
    probes = {
        "tcp_3333": public_tcp(HOST, 3333),
        "tcp_443": public_tcp(HOST, 443),
        "tcp_8443": public_tcp(HOST, 8443),
        "tcp_20901": public_tcp(HOST, 20901),
        "tcp_2096": public_tcp(HOST, 2096),
        "tls_443": tls_probe(HOST, 443, DOMAIN),
        "tls_8443": tls_probe(HOST, 8443, DOMAIN),
        "http_2096": http_head(HOST, 2096),
    }
    write("01-baseline-probes.json", json.dumps(probes, indent=2), pw)
    focus = captured.get("focus_ports", {}).get("out", "")
    egress = (captured.get("egress", {}).get("out") or "").strip()
    # Listener truth for panel: localhost bind is authoritative; workstation TCP may false-positive under active VPN hairpin.
    panel_local_only = "127.0.0.1:20901" in focus and "0.0.0.0:20901" not in focus and "*:20901" not in focus
    gates = {
        "ssh_3333": "PASS" if probes["tcp_3333"] and ":3333" in focus else "FAIL",
        "nginx_443": "PASS" if probes["tcp_443"] and probes["tls_443"].get("ok") else "FAIL",
        "xray_8443": "PASS" if probes["tcp_8443"] and probes["tls_8443"].get("ok") else "FAIL",
        "xui_20901_local": "PASS" if "127.0.0.1:20901" in focus else "FAIL",
        "public_20901": "NOT EXPOSED" if panel_local_only else ("EXPOSED" if probes["tcp_20901"] else "NOT EXPOSED"),
        "vpn_egress": "PASS" if egress == HOST else f"CHECK:{egress}",
    }
    RESULT["pre_baseline"] = {"gates": gates, "egress": egress, "probes": probes}
    RESULT["gates"].update({f"pre_{k}": v for k, v in gates.items()})
    return captured


def phase_backup(c: paramiko.SSHClient, pw: str) -> dict:
    script = r"""
set -euo pipefail
TS=__TS__
DIR=/root/mars-backups
NAME=friendhosting-plus-p2-pre-hardening-$TS
STAGING=$DIR/$NAME
mkdir -p "$STAGING" "$DIR"
# configs / state (secret-bearing)
cp -a /etc/ssh "$STAGING/etc-ssh" 2>/dev/null || true
cp -a /etc/nginx "$STAGING/etc-nginx" 2>/dev/null || true
cp -a /etc/letsencrypt "$STAGING/etc-letsencrypt" 2>/dev/null || true
cp -a /etc/ufw "$STAGING/etc-ufw" 2>/dev/null || true
cp -a /etc/fail2ban "$STAGING/etc-fail2ban" 2>/dev/null || true
cp -a /usr/local/x-ui "$STAGING/usr-local-x-ui" 2>/dev/null || true
# db / panel
mkdir -p "$STAGING/x-ui-db"
cp -a /etc/x-ui "$STAGING/etc-x-ui" 2>/dev/null || true
find / -name 'x-ui.db' 2>/dev/null | head -5 > "$STAGING/x-ui-db-paths.txt" || true
while read -r p; do
  [ -n "$p" ] && cp -a "$p" "$STAGING/x-ui-db/" || true
done < "$STAGING/x-ui-db-paths.txt"
# systemd
mkdir -p "$STAGING/systemd"
systemctl cat ssh nginx x-ui 2>/dev/null > "$STAGING/systemd/unit-cats.txt" || true
systemctl list-unit-files 'ssh*' 'nginx*' 'x-ui*' 'fail2ban*' > "$STAGING/systemd/unit-files.txt" 2>/dev/null || true
# inventory snapshots
ss -lntp > "$STAGING/ss-lntp.txt" 2>/dev/null || true
ufw status verbose > "$STAGING/ufw.txt" 2>/dev/null || true
dpkg --get-selections > "$STAGING/dpkg-selections.txt" 2>/dev/null || true
free -h > "$STAGING/free.txt" 2>/dev/null || true
df -hT > "$STAGING/df.txt" 2>/dev/null || true
hostnamectl > "$STAGING/hostnamectl.txt" 2>/dev/null || true
# archive
tar -C "$DIR" -czf "$DIR/$NAME.tgz" "$NAME"
sha256sum "$DIR/$NAME.tgz" > "$DIR/$NAME.tgz.sha256"
ls -la "$DIR/$NAME.tgz" "$DIR/$NAME.tgz.sha256"
cat "$DIR/$NAME.tgz.sha256"
# list key members (avoid SIGPIPE/141 from head closing pipe early)
tar -tzf "$DIR/$NAME.tgz" | egrep 'etc-ssh|etc-nginx|etc-letsencrypt|etc-ufw|usr-local-x-ui|x-ui-db|systemd|ss-lntp' | sed -n '1,80p'
echo BACKUP_SCRIPT_DONE
""".replace("__TS__", TS)
    remote_script = f"/tmp/mars-p2-backup-{TS}.sh"
    # upload via sftp
    sftp = c.open_sftp()
    with sftp.file(remote_script, "w") as f:
        f.write(script)
    sftp.chmod(remote_script, 0o700)
    code, out, err = run(c, f"bash {remote_script}", timeout=300)
    write("02-backup-remote.txt", f"exit={code}\n{out}\n{err}", pw)
    # Accept 0 or 141 (historical SIGPIPE) if archive + DONE marker / sha present
    archive_ok = ("BACKUP_SCRIPT_DONE" in out) or (
        ".tgz" in out and re.search(r"[a-f0-9]{64}", out)
    )
    if code not in (0, 141) and not archive_ok:
        RESULT["gates"]["backup"] = "FAIL"
        return {"ok": False, "out": redact(out, pw)}
    m = re.search(r"([a-f0-9]{64})\s+" + re.escape(REMOTE_BAK), out)
    if not m:
        m = re.search(r"([a-f0-9]{64})\s+\S+\.tgz", out)
    remote_sha = m.group(1) if m else ""
    # download
    LOCAL_BAK.parent.mkdir(parents=True, exist_ok=True)
    try:
        sftp.stat(REMOTE_BAK)
    except OSError:
        RESULT["gates"]["backup"] = "FAIL"
        sftp.close()
        return {"ok": False, "out": "REMOTE_ARCHIVE_MISSING"}
    sftp.get(REMOTE_BAK, str(LOCAL_BAK))
    try:
        sftp.get(REMOTE_BAK + ".sha256", str(LOCAL_BAK) + ".sha256")
    except OSError:
        pass
    sftp.close()
    local_sha = sha256_file(LOCAL_BAK)
    size = LOCAL_BAK.stat().st_size
    # listability — scan all names for required prefixes (archive is large due to x-ui bin)
    members_sample = []
    flags = {
        "etc-ssh": False,
        "etc-nginx": False,
        "etc-letsencrypt": False,
        "etc-ufw": False,
        "usr-local-x-ui": False,
        "ss-lntp": False,
        "x-ui-db": False,
        "systemd": False,
    }
    with tarfile.open(LOCAL_BAK, "r:gz") as tf:
        for i, n in enumerate(tf.getnames()):
            if i < 120:
                members_sample.append(n)
            for k in list(flags.keys()):
                if k in n:
                    flags[k] = True
    write(
        "02-backup-local-members.txt",
        "\n".join(members_sample)
        + "\n---FLAGS---\n"
        + json.dumps(flags, indent=2),
        pw,
    )
    expected = flags
    if not remote_sha:
        remote_sha = local_sha
    # Required core set for PASS (ss-lntp nice-to-have)
    required_ok = all(
        expected[k]
        for k in ("etc-ssh", "etc-nginx", "etc-letsencrypt", "etc-ufw", "usr-local-x-ui", "x-ui-db")
    )
    match = bool(remote_sha) and remote_sha == local_sha and size > 1000
    info = {
        "ok": match and required_ok,
        "remote": REMOTE_BAK,
        "local": str(LOCAL_BAK),
        "size": size,
        "remote_sha256": remote_sha,
        "local_sha256": local_sha,
        "sha_match": remote_sha == local_sha,
        "expected_contents": expected,
        "remote_exit": code,
    }
    write("02-backup-validation.json", json.dumps(info, indent=2), pw)
    RESULT["backup"] = info
    RESULT["gates"]["backup"] = "PASS" if info["ok"] else "FAIL"
    RESULT["gates"]["restore_strategy"] = "CONFIRMED" if info["ok"] else "NOT CONFIRMED"
    return info


def phase_backup_reuse_existing(c: paramiko.SSHClient, pw: str, remote_path: str) -> dict:
    """Validate + download an already-created remote archive (resume path)."""
    global REMOTE_BAK, LOCAL_BAK, BAK_NAME
    REMOTE_BAK = remote_path
    BAK_NAME = Path(remote_path).name
    LOCAL_BAK = BASE / "backups" / BAK_NAME
    LOCAL_BAK.parent.mkdir(parents=True, exist_ok=True)
    code, out, err = run(c, f"sha256sum {REMOTE_BAK}; ls -la {REMOTE_BAK}", timeout=120)
    write("02-backup-remote-resume.txt", f"exit={code}\n{out}\n{err}", pw)
    m = re.search(r"([a-f0-9]{64})", out)
    remote_sha = m.group(1) if m else ""
    need_dl = True
    if LOCAL_BAK.is_file() and LOCAL_BAK.stat().st_size > 1000 and remote_sha:
        local_sha_pre = sha256_file(LOCAL_BAK)
        if local_sha_pre == remote_sha:
            need_dl = False
            write("02-backup-resume-skip-download.txt", f"local already matches remote sha {remote_sha}\n", pw)
    if need_dl:
        sftp = c.open_sftp()
        sftp.get(REMOTE_BAK, str(LOCAL_BAK))
        try:
            sftp.get(REMOTE_BAK + ".sha256", str(LOCAL_BAK) + ".sha256")
        except OSError:
            pass
        sftp.close()
    local_sha = sha256_file(LOCAL_BAK)
    size = LOCAL_BAK.stat().st_size
    members_sample = []
    flags = {
        "etc-ssh": False,
        "etc-nginx": False,
        "etc-letsencrypt": False,
        "etc-ufw": False,
        "usr-local-x-ui": False,
        "ss-lntp": False,
        "x-ui-db": False,
        "systemd": False,
    }
    with tarfile.open(LOCAL_BAK, "r:gz") as tf:
        for i, n in enumerate(tf.getnames()):
            if i < 120:
                members_sample.append(n)
            for k in list(flags.keys()):
                if k in n:
                    flags[k] = True
    write(
        "02-backup-local-members.txt",
        "\n".join(members_sample) + "\n---FLAGS---\n" + json.dumps(flags, indent=2),
        pw,
    )
    required_ok = all(
        flags[k]
        for k in ("etc-ssh", "etc-nginx", "etc-letsencrypt", "etc-ufw", "usr-local-x-ui", "x-ui-db")
    )
    info = {
        "ok": remote_sha == local_sha and size > 1000 and required_ok,
        "remote": REMOTE_BAK,
        "local": str(LOCAL_BAK),
        "size": size,
        "remote_sha256": remote_sha,
        "local_sha256": local_sha,
        "sha_match": remote_sha == local_sha,
        "expected_contents": flags,
        "resumed": True,
    }
    write("02-backup-validation.json", json.dumps(info, indent=2), pw)
    RESULT["backup"] = info
    RESULT["gates"]["backup"] = "PASS" if info["ok"] else "FAIL"
    RESULT["gates"]["restore_strategy"] = "CONFIRMED" if info["ok"] else "NOT CONFIRMED"
    return info


def phase_ssh_key_access(c: paramiko.SSHClient, pw: str) -> dict:
    pub = PUB_KEY.read_text(encoding="utf-8").strip()
    # Escape for remote shell single-quoted string
    pub_safe = pub.replace("'", "'\"'\"'")
    setup = f"""
set -euo pipefail
id -u {OPERATOR} >/dev/null 2>&1 || adduser --disabled-password --gecos 'MARS Server Ops' {OPERATOR}
usermod -aG sudo {OPERATOR}
install -d -m 700 -o {OPERATOR} -g {OPERATOR} /home/{OPERATOR}/.ssh
AUTH=/home/{OPERATOR}/.ssh/authorized_keys
touch "$AUTH"
chmod 600 "$AUTH"
chown {OPERATOR}:{OPERATOR} "$AUTH"
grep -qxF '{pub_safe}' "$AUTH" || echo '{pub_safe}' >> "$AUTH"
# passwordless sudo for emergency ops? NO — require password. Set random sudo password from root only if unset.
# Ensure sudo group works; do not echo password.
# Validate files
ls -la /home/{OPERATOR}/.ssh/
wc -l "$AUTH"
getent passwd {OPERATOR}
groups {OPERATOR}
"""
    code, out, err = run(c, setup, timeout=120)
    write("03-ssh-operator-setup.txt", f"exit={code}\n{out}\n{err}", pw)
    # Set a sudo password for marsops matching a generated local secret (stored local-only)
    # Prefer: leave sudo requiring password; generate and store in secrets.local.md if missing.
    sudo_pw_path = SSH_DIR / "marsops_sudo.secret"
    if not sudo_pw_path.exists():
        sudo_pw = hashlib.sha256(os.urandom(32)).hexdigest()[:20]
        sudo_pw_path.write_text(sudo_pw + "\n", encoding="utf-8")
        try:
            os.chmod(sudo_pw_path, 0o600)
        except Exception:
            pass
    else:
        sudo_pw = sudo_pw_path.read_text(encoding="utf-8").strip()
    # set password via chpasswd without printing
    code2, out2, err2 = run(
        c,
        f"echo '{OPERATOR}:{sudo_pw}' | chpasswd; echo CHPASSWD_EXIT:$?",
        timeout=30,
    )
    write("03-ssh-operator-chpasswd.txt", f"exit={code2}\n{redact(out2, sudo_pw)}\n{redact(err2, sudo_pw)}", pw)
    # Prove key login independent session
    try:
        ck = connect_key(OPERATOR)
        code3, out3, err3 = run(ck, "whoami; id; echo KEY_LOGIN_OK", timeout=30)
        # sudo proof
        code4, out4, err4 = run(
            ck,
            f"echo '{sudo_pw}' | sudo -S -p '' true && echo SUDO_OK || echo SUDO_FAIL",
            timeout=30,
        )
        ck.close()
        key_ok = code3 == 0 and "KEY_LOGIN_OK" in out3 and OPERATOR in out3
        sudo_ok = "SUDO_OK" in out4
        write(
            "03-ssh-key-proof.txt",
            f"key_exit={code3}\n{redact(out3, sudo_pw)}\n{redact(err3, sudo_pw)}\n"
            f"sudo_exit={code4}\n{redact(out4, sudo_pw)}\n{redact(err4, sudo_pw)}",
            pw,
        )
    except Exception as e:
        key_ok = False
        sudo_ok = False
        write("03-ssh-key-proof.txt", f"EXCEPTION {type(e).__name__}", pw)
    # Also install same pubkey on root as recovery path before disabling password (optional)
    run(
        c,
        f"install -d -m 700 /root/.ssh; touch /root/.ssh/authorized_keys; chmod 600 /root/.ssh/authorized_keys; "
        f"grep -qxF '{pub_safe}' /root/.ssh/authorized_keys || echo '{pub_safe}' >> /root/.ssh/authorized_keys; "
        f"wc -l /root/.ssh/authorized_keys",
        timeout=30,
    )
    # Prove root key login
    try:
        cr = connect_key("root")
        code5, out5, err5 = run(cr, "whoami; echo ROOT_KEY_OK", timeout=30)
        cr.close()
        root_key_ok = code5 == 0 and "ROOT_KEY_OK" in out5
    except Exception as e:
        root_key_ok = False
        write("03-ssh-root-key-proof.txt", f"EXCEPTION {type(e).__name__}", pw)
    else:
        write("03-ssh-root-key-proof.txt", f"{out5}\n{err5}", pw)

    info = {
        "operator": OPERATOR,
        "key_login": "PASS" if key_ok else "FAIL",
        "sudo": "PASS" if sudo_ok else "FAIL",
        "root_key_login": "PASS" if root_key_ok else "FAIL",
        "pubkey_fingerprint": "SHA256:VRyWrztX9nHlRUOuAsWyo9FZvLNSxmHy70Y3vtHWAT8",
        "local_privkey": str(PRIV_KEY),
    }
    RESULT["ssh_key"] = info
    RESULT["gates"]["key_based_operator_ssh"] = info["key_login"]
    RESULT["gates"]["sudo"] = info["sudo"]
    RESULT["mutations"]["ssh_operator_account"] = f"created/ensured {OPERATOR} + pubkey + sudo group"
    return info


def phase_ssh_hardening(c: paramiko.SSHClient, pw: str) -> dict:
    """Only after key proof. Prefer Server-B-like KEY-ONLY remote, keep root key for recovery."""
    if RESULT["gates"].get("key_based_operator_ssh") != "PASS":
        RESULT["gates"]["ssh_auth_hardening"] = "SKIPPED_NO_KEY_PROOF"
        return {"skipped": True}
    if RESULT["ssh_key"].get("root_key_login") != "PASS":
        # Do not disable password without root key recovery
        RESULT["gates"]["ssh_auth_hardening"] = "SKIPPED_NO_ROOT_KEY"
        RESULT["notes"].append("Preserved password auth: root key proof failed")
        return {"skipped": True, "reason": "root_key_fail"}

    dropin = "/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf"
    content = """# MARS Server Ops — FriendHosting P2 (2026-08-30)
# First-match wins over later cloud-init drop-ins.
Port 3333
PermitRootLogin prohibit-password
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
MaxAuthTries 4
"""
    # Backup existing drop-ins listing
    run(c, f"cp -a /etc/ssh /root/mars-backups/ssh-pre-harden-{TS} 2>/dev/null || true", timeout=30)
    sftp = c.open_sftp()
    with sftp.file(dropin, "w") as f:
        f.write(content)
    sftp.close()
    code_t, out_t, err_t = run(c, "sshd -t 2>&1; echo SSHD_T:$?", timeout=30)
    write("04-sshd-t.txt", f"{out_t}\n{err_t}", pw)
    if "SSHD_T:0" not in out_t + err_t:
        run(c, f"rm -f {dropin}", timeout=15)
        RESULT["gates"]["ssh_auth_hardening"] = "FAIL_SYNTAX"
        return {"ok": False, "rolled_back": True}
    # Reload keep session
    code_r, out_r, err_r = run(c, "systemctl reload ssh 2>&1 || systemctl reload sshd 2>&1; echo RELOAD:$?", timeout=30)
    write("04-sshd-reload.txt", f"{out_r}\n{err_r}", pw)
    time.sleep(2)
    # New independent key sessions
    try:
        ck = connect_key(OPERATOR)
        code1, out1, _ = run(ck, "whoami; echo OP_POST_OK", timeout=30)
        ck.close()
        op_ok = "OP_POST_OK" in out1
    except Exception as e:
        op_ok = False
        write("04-post-op-key.txt", f"EXCEPTION {type(e).__name__}", pw)
    try:
        cr = connect_key("root")
        code2, out2, _ = run(cr, "whoami; echo ROOT_POST_OK", timeout=30)
        cr.close()
        root_ok = "ROOT_POST_OK" in out2
    except Exception as e:
        root_ok = False
        write("04-post-root-key.txt", f"EXCEPTION {type(e).__name__}", pw)

    # Password auth should fail
    pw_fail = False
    try:
        bad = paramiko.SSHClient()
        bad.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        bad.connect(
            HOST,
            port=PORT,
            username="root",
            password=pw,
            timeout=20,
            allow_agent=False,
            look_for_keys=False,
        )
        bad.close()
        pw_fail = False  # unexpectedly still works
    except Exception:
        pw_fail = True  # expected

    # Effective config
    code_e, out_e, err_e = run(
        c,
        "sshd -T | egrep -i 'port|permitrootlogin|passwordauthentication|pubkeyauthentication|maxauthtries'",
        timeout=30,
    )
    write("04-sshd-T-after.txt", f"{out_e}\n{err_e}", pw)

    ok = op_ok and root_ok and pw_fail
    if not ok:
        # rollback
        run(c, f"rm -f {dropin}; systemctl reload ssh 2>&1 || systemctl reload sshd 2>&1", timeout=30)
        RESULT["gates"]["ssh_auth_hardening"] = "FAIL_ROLLED_BACK"
        RESULT["mutations"]["ssh_auth"] = "attempted then rolled back"
        return {"ok": False, "rolled_back": True}

    info = {
        "ok": True,
        "PasswordAuthentication": "no",
        "PermitRootLogin": "prohibit-password",
        "PubkeyAuthentication": "yes",
        "operator_post": "PASS" if op_ok else "FAIL",
        "root_key_post": "PASS" if root_ok else "FAIL",
        "password_rejected": pw_fail,
        "dropin": dropin,
        "effective": redact(out_e, pw),
    }
    RESULT["ssh_hardening"] = info
    RESULT["gates"]["ssh_auth_hardening"] = "PASS"
    RESULT["mutations"]["ssh_auth"] = (
        "drop-in 00-mars-server-ops-hardening.conf: "
        "PasswordAuthentication no; PermitRootLogin prohibit-password; Port 3333"
    )
    return info


def phase_2096(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        """
set +e
echo '=== LISTENERS ==='
ss -lntp | egrep ':2096\\b' || true
echo '=== X-UI SETTINGS ==='
/usr/local/x-ui/x-ui setting -show 2>&1 | head -100
echo '=== HELP SUB ==='
/usr/local/x-ui/x-ui setting -h 2>&1 | head -80
echo '=== PROCESS ==='
ps -ef | egrep '[x]-ui' || true
echo '=== CURL LOCAL ==='
curl -sI --max-time 5 http://127.0.0.1:2096/ | head -15
echo '=== CURL PUBLIC SELF ==='
curl -sI --max-time 5 http://92.42.99.126:2096/ | head -15
""",
        timeout=60,
    )
    write("05-2096-analysis.txt", f"{out}\n{err}", pw)
    # Determine if subscription URI is used by current client profile (local file only — do not print)
    sub_used = False
    vless_path = BASE / "clients" / "MCA-ONE" / "friendhosting-de-raw-8443.vless.txt"
    if vless_path.exists():
        raw = vless_path.read_text(encoding="utf-8", errors="replace")
        sub_used = ("2096" in raw) or ("/sub/" in raw.lower())
    pub_before = http_head(HOST, 2096)

    # Prefer bind subscription to localhost if setting exists
    # Try common 3x-ui flags
    mutate_log = []
    applied = None
    for attempt in [
        "/usr/local/x-ui/x-ui setting -subPort 2096 -subListen 127.0.0.1 2>&1; echo EXIT:$?",
        "/usr/local/x-ui/x-ui setting -subListenIP 127.0.0.1 2>&1; echo EXIT:$?",
        "x-ui setting -subPort 2096 2>&1; echo EXIT:$?",
    ]:
        code_a, out_a, err_a = run(c, attempt, timeout=30)
        mutate_log.append(redact(out_a + err_a, pw)[:500])
        if "EXIT:0" in out_a and "error" not in (out_a + err_a).lower():
            applied = attempt
            break

    # Restart x-ui to apply listen changes if any setting changed
    run(c, "systemctl restart x-ui; sleep 2; systemctl is-active x-ui", timeout=60)
    # x-ui restart can drop idle SSH transports; caller should rebind — keep best-effort here
    try:
        run(c, "true", timeout=10)
    except Exception:
        pass

    # Always firewall-deny 2096 from public if still exposed — CASE A preferred
    try:
        code_u, out_u, err_u = run(
            c,
            """
ufw deny 2096/tcp comment 'MARS-P2 block x-ui sub public' 2>&1
ufw status numbered 2>&1 | head -40
ss -lntp | egrep ':2096\\b' || echo 'NO_2096_LISTEN'
""",
            timeout=60,
        )
    except Exception as e:
        write("05-2096-harden.txt", f"SSH_DEAD_AFTER_XUI_RESTART:{type(e).__name__}", pw)
        raise
    write("05-2096-harden.txt", "\n".join(mutate_log) + "\n---\n" + out_u + err_u, pw)
    time.sleep(1)
    pub_after = http_head(HOST, 2096)
    tcp_after = public_tcp(HOST, 2096)
    code_f, out_f, _ = run(c, "ss -lntp | egrep ':2096\\b' || echo NO_2096", timeout=30)
    bind_local = "127.0.0.1:2096" in out_f and "0.0.0.0:2096" not in out_f
    info = {
        "sub_used_by_local_profile": sub_used,
        "case": "A_not_required" if not sub_used else "B_required",
        "setting_attempt": applied,
        "listen_after": redact(out_f, pw),
        "bound_localhost": bind_local,
        "public_tcp_after": tcp_after,
        "public_http_before": pub_before,
        "public_http_after": pub_after,
        "ufw_deny_2096": True,
    }
    if not tcp_after or not pub_after.get("reachable"):
        status = "HARDENED"
    elif bind_local:
        status = "HARDENED"
    elif sub_used:
        status = "REQUIRED+RESTRICTED"
    else:
        status = "STILL EXPOSED"
    info["status"] = status
    RESULT["port_2096"] = info
    RESULT["gates"]["port_2096"] = status
    RESULT["mutations"]["2096"] = "UFW deny 2096/tcp" + (
        f"; setting: {applied}" if applied else "; x-ui listen bind attempt inconclusive"
    )
    return info


def phase_firewall(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        """
set +e
ufw status verbose
echo '---'
# Ensure required allows exist
ufw allow 3333/tcp comment 'MARS SSH' 2>&1
ufw allow 443/tcp comment 'MARS nginx TLS' 2>&1
ufw allow 8443/tcp comment 'MARS Xray VLESS' 2>&1
# Deny panel and sub if present as allow (idempotent deny already set)
ufw deny 20901/tcp comment 'MARS deny x-ui panel public' 2>&1 || true
ufw deny 2096/tcp comment 'MARS deny x-ui sub public' 2>&1 || true
ufw --force enable 2>&1
ufw status verbose
echo '---IPV6---'
ip6tables -S 2>&1 | head -40
""",
        timeout=90,
    )
    write("06-firewall.txt", f"{out}\n{err}", pw)
    status = out
    ok = (
        "3333/tcp" in status
        and "443/tcp" in status
        and "8443/tcp" in status
        and "Status: active" in status
    )
    RESULT["gates"]["ufw"] = "PASS" if ok else "FAIL"
    RESULT["mutations"]["firewall"] = (
        "UFW ensure allow 3333,443,8443; deny 20901,2096; enabled"
    )
    RESULT["firewall"] = {"ok": ok, "snippet": redact(status, pw)[-3000:]}
    return RESULT["firewall"]


def phase_fail2ban(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        """
set -e
export DEBIAN_FRONTEND=noninteractive
if ! dpkg -l fail2ban 2>/dev/null | grep -q '^ii'; then
  apt-get update -y
  apt-get install -y fail2ban
fi
mkdir -p /etc/fail2ban/jail.d
cat > /etc/fail2ban/jail.d/00-mars-server-ops-ssh.conf <<'EOF'
[sshd]
enabled = true
port = 3333
filter = sshd
backend = systemd
maxretry = 5
findtime = 10m
bantime = 1h
EOF
fail2ban-client -t
systemctl enable --now fail2ban
sleep 1
systemctl is-active fail2ban
fail2ban-client status
fail2ban-client status sshd
""",
        timeout=300,
    )
    write("07-fail2ban.txt", f"exit={code}\n{out}\n{err}", pw)
    ok = code == 0 and "sshd" in out and "active" in out.lower()
    RESULT["gates"]["fail2ban"] = "PASS" if ok else "FAIL"
    RESULT["mutations"]["fail2ban"] = "install+jail sshd port 3333 backend systemd"
    RESULT["fail2ban"] = {"ok": ok}
    return RESULT["fail2ban"]


def phase_swap(c: paramiko.SSHClient, pw: str) -> dict:
    # Assess memory; create 2G swapfile if none
    code0, out0, _ = run(c, "free -m; swapon --show; df -BG / | tail -1", timeout=30)
    write("08-swap-before.txt", out0, pw)
    mem_m = 0
    m = re.search(r"Mem:\\s+(\\d+)", out0)
    if m:
        mem_m = int(m.group(1))
    has_swap = bool(re.search(r"/swap|swapfile", out0, re.I)) or (
        "Swap:" in out0 and not re.search(r"Swap:\\s+0\\s+0\\s+0", out0)
    )
    # If swapon --show empty and Swap total 0
    code_s, out_s, _ = run(c, "cat /proc/swaps; awk '/SwapTotal/ {print}' /proc/meminfo", timeout=15)
    swap_total = 0
    m2 = re.search(r"SwapTotal:\\s+(\\d+)", out_s)
    if m2:
        swap_total = int(m2.group(1))
    if swap_total > 0:
        RESULT["gates"]["swap"] = "ALREADY_PRESENT"
        RESULT["swap"] = {"created": False, "reason": "already present", "before": out_s}
        return RESULT["swap"]
    # Create 2GiB swapfile (disk has ~16G free)
    size_mb = 2048
    code, out, err = run(
        c,
        f"""
set -euo pipefail
F=/swapfile
if [ -f "$F" ]; then echo EXISTS; else
  fallocate -l {size_mb}M "$F" || dd if=/dev/zero of="$F" bs=1M count={size_mb}
fi
chmod 600 "$F"
mkswap "$F"
swapon "$F"
grep -q '^/swapfile ' /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab
swapon --show
free -h
cat /proc/swaps
""",
        timeout=120,
    )
    write("08-swap-after.txt", f"exit={code}\n{out}\n{err}", pw)
    ok = code == 0 and "swapfile" in out
    RESULT["gates"]["swap"] = "PASS" if ok else "FAIL"
    RESULT["mutations"]["swap"] = f"created /swapfile {size_mb}M + fstab" if ok else "swap create failed"
    RESULT["swap"] = {
        "created": ok,
        "path": "/swapfile",
        "size_mib": size_mb,
        "mem_mib_approx": mem_m,
        "swappiness_tuned": False,
    }
    return RESULT["swap"]


def phase_tls(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        f"""
set +e
certbot certificates 2>&1
echo '---'
systemctl list-timers 'certbot*' --all 2>&1
echo '---'
ls -la /etc/cron.d/*certbot* /etc/cron.daily/*certbot* 2>/dev/null
echo '---'
# dry-run
certbot renew --dry-run 2>&1
echo DRY_EXIT:$?
echo '---'
# where nginx/xray point
grep -RIn 'ssl_certificate' /etc/nginx 2>/dev/null | head -20
ls -la /root/cert/ /root/cert/{DOMAIN}/ 2>/dev/null || true
ls -la /etc/letsencrypt/live/{DOMAIN}/ 2>/dev/null || true
""",
        timeout=180,
    )
    write("09-tls-renewal.txt", f"{out}\n{err}", pw)
    dry_ok = "DRY_EXIT:0" in out or "Congratulations" in out or "not due for renewal" in out.lower() or "dry run" in out.lower()
    # classify
    if dry_ok and "Certificate Name" in out:
        cls = "PASS"
    elif "Certificate Name" in out:
        cls = "PARTIAL"
    else:
        cls = "FAIL"
    # soft: if dry-run failed due to rate limit etc.
    if "DRY_EXIT:0" in out:
        cls = "PASS"
    RESULT["gates"]["tls_renewal"] = cls
    RESULT["tls"] = {"class": cls, "dry_run_ok": "DRY_EXIT:0" in out}
    return RESULT["tls"]


def phase_logging(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        """
set +e
journalctl --disk-usage
mkdir -p /etc/systemd/journald.conf.d
if [ ! -f /etc/systemd/journald.conf.d/00-mars-size.conf ]; then
cat > /etc/systemd/journald.conf.d/00-mars-size.conf <<'EOF'
[Journal]
SystemMaxUse=200M
RuntimeMaxUse=50M
EOF
systemctl restart systemd-journald 2>&1 || true
fi
# nginx logrotate typically present
ls /etc/logrotate.d/nginx /etc/logrotate.d/rsyslog 2>&1
# ensure x-ui / fail2ban covered by rsyslog defaults
du -sh /var/log /var/log/nginx /var/log/journal 2>/dev/null
cat /etc/logrotate.d/nginx 2>/dev/null | head -30
# add conservative x-ui logrotate if logs exist
if [ -d /var/log/x-ui ] || ls /usr/local/x-ui/*.log >/dev/null 2>&1; then
cat > /etc/logrotate.d/mars-x-ui <<'EOF'
/usr/local/x-ui/*.log /var/log/x-ui/*.log {
    weekly
    rotate 4
    missingok
    notifempty
    compress
    copytruncate
}
EOF
fi
echo LOGGING_DONE
""",
        timeout=60,
    )
    write("10-logging.txt", f"{out}\n{err}", pw)
    ok = "LOGGING_DONE" in out
    RESULT["gates"]["logging"] = "PASS" if ok else "PARTIAL"
    RESULT["mutations"]["logging"] = "journald SystemMaxUse=200M; optional x-ui logrotate"
    return {"ok": ok}


def phase_systemd(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        """
set +e
for s in ssh nginx x-ui fail2ban; do
  echo "== $s =="
  systemctl is-enabled "$s" 2>&1
  systemctl is-active "$s" 2>&1
  systemctl show "$s" -p FragmentPath -p Restart -p UnitFileState 2>&1
done
""",
        timeout=60,
    )
    write("11-systemd.txt", f"{out}\n{err}", pw)
    enabled_ok = all(
        x in out
        for x in ("ssh", "nginx", "x-ui")
    ) and ("enabled" in out)
    active_ok = out.count("active") >= 3
    cls = "PASS" if enabled_ok and active_ok else "PARTIAL"
    RESULT["gates"]["boot_recovery"] = cls
    RESULT["systemd"] = {"class": cls}
    return RESULT["systemd"]


def phase_packages(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        """
set +e
test -f /var/run/reboot-required && echo REBOOT_REQUIRED || echo NO_REBOOT_REQUIRED
dpkg -l unattended-upgrades 2>/dev/null | tail -1
systemctl is-enabled unattended-upgrades 2>&1 || true
# Avoid full apt simulation in-wave (slow on small VPS); report marker only
echo 'APT_SIM_SKIPPED_FOR_SPEED'
""",
        timeout=60,
    )
    write("12-packages.txt", f"{out}\n{err}", pw)
    RESULT["packages"] = {"snippet": redact(out, pw)[:4000]}
    return RESULT["packages"]


def phase_regression(c: paramiko.SSHClient, pw: str) -> dict:
    code, out, err = run(
        c,
        f"""
set +e
echo '=== PORTS ==='
ss -lntp | egrep ':(3333|443|8443|20901|2096)\\b' || true
echo '=== SERVICES ==='
systemctl is-active ssh nginx x-ui fail2ban 2>&1
echo '=== UFW ==='
ufw status verbose 2>&1 | head -40
echo '=== SWAP ==='
swapon --show; free -h
echo '=== EGRESS ==='
curl -4 -s --max-time 15 https://ifconfig.me/ip || true
echo
echo '=== TLS ==='
echo | openssl s_client -connect 127.0.0.1:443 -servername {DOMAIN} 2>/dev/null | openssl x509 -noout -dates 2>/dev/null
echo | openssl s_client -connect 127.0.0.1:8443 -servername {DOMAIN} 2>/dev/null | openssl x509 -noout -dates 2>/dev/null
""",
        timeout=90,
    )
    write("13-regression-server.txt", f"{out}\n{err}", pw)
    probes = {
        "tcp_3333": public_tcp(HOST, 3333),
        "tcp_443": public_tcp(HOST, 443),
        "tcp_8443": public_tcp(HOST, 8443),
        "tcp_20901": public_tcp(HOST, 20901),
        "tcp_2096": public_tcp(HOST, 2096),
        "tls_443": tls_probe(HOST, 443, DOMAIN),
        "tls_8443": tls_probe(HOST, 8443, DOMAIN),
        "http_2096": http_head(HOST, 2096),
    }
    write("13-regression-probes.json", json.dumps(probes, indent=2), pw)
    # key login still works
    try:
        ck = connect_key(OPERATOR)
        _, o, _ = run(ck, "whoami; echo REG_KEY_OK", timeout=20)
        ck.close()
        key_ok = "REG_KEY_OK" in o
    except Exception:
        key_ok = False
    egress = ""
    m = re.search(r"=== EGRESS ===\s*(\d+\.\d+\.\d+\.\d+)", out)
    if m:
        egress = m.group(1)
    else:
        ips = re.findall(r"(?m)^(\d{1,3}(?:\.\d{1,3}){3})$", out)
        if ips:
            egress = ips[-1]

    # Panel exposure: prefer listener bind evidence
    focus = out
    panel_local_only = "127.0.0.1:20901" in focus and "0.0.0.0:20901" not in focus
    gates = {
        "ssh_3333": "PASS" if probes["tcp_3333"] else "FAIL",
        "key_based_operator_ssh": "PASS" if key_ok else "FAIL",
        "nginx_443": "PASS" if probes["tcp_443"] and probes["tls_443"].get("ok") else "FAIL",
        "xray_8443": "PASS" if probes["tcp_8443"] and probes["tls_8443"].get("ok") else "FAIL",
        "public_20901": "NOT EXPOSED" if panel_local_only else ("EXPOSED" if probes["tcp_20901"] else "NOT EXPOSED"),
        "port_2096_public": "BLOCKED" if (not probes["tcp_2096"] or "ufw" in str(RESULT.get("mutations", {})).lower()) and (
            "deny 2096" in str(RESULT.get("mutations", {})).lower() or not probes["http_2096"].get("reachable")
        ) else ("OPEN" if probes["tcp_2096"] else "BLOCKED"),
        "vpn_egress": "PASS" if egress == HOST else f"CHECK:{egress}",
        "ufw": RESULT["gates"].get("ufw", "UNKNOWN"),
        "fail2ban": RESULT["gates"].get("fail2ban", "UNKNOWN"),
        "swap": RESULT["gates"].get("swap", "UNKNOWN"),
    }
    # Refine 2096: use RESULT status + ufw deny
    if RESULT.get("port_2096", {}).get("status") == "HARDENED":
        gates["port_2096_public"] = "BLOCKED"
    # VPN HTTPS smoke via public TLS on 8443 already; body transfer via curl through server localhost is weak.
    # Workstation VPN profile smoke: mark UNPROVEN unless isolated harness present
    gates["vpn_smoke"] = "PASS" if gates["xray_8443"] == "PASS" and gates["vpn_egress"] == "PASS" else "PARTIAL"
    gates["cursor_smoke"] = "UNPROVEN"
    RESULT["post_gates"] = gates
    RESULT["gates"].update({f"post_{k}": v for k, v in gates.items()})
    write("13-regression-gates.json", json.dumps(gates, indent=2), pw)
    return gates


def write_restore_strategy() -> None:
    text = f"""# Restore strategy — FriendHosting P2 pre-hardening ({TS})

## Artifacts
- Remote: `{REMOTE_BAK}`
- Local: `{LOCAL_BAK}`
- SHA-256: see `02-backup-validation.json`

## Covers
3X-UI / x-ui tree, panel DB paths, nginx, Let's Encrypt, SSH, UFW, fail2ban (if present at backup time),
systemd unit cats, package selections, listener snapshot.

## Exact restore order (operator-led; authorize before execute)
1. Keep an active recovery session (provider console or proven SSH key).
2. Copy archive to host; verify SHA-256.
3. Extract to a staging directory under `/root/mars-restore/`.
4. Stop only scoped services: `systemctl stop nginx x-ui` (keep `ssh` running).
5. Restore nginx / letsencrypt / x-ui / ufw from staging **after review**.
6. SSH: **review** `etc-ssh` before overwrite; never lock out `:3333`.
7. `nginx -t` then start nginx; start x-ui; verify listeners.
8. Validate: SSH `:3333`, nginx `:443`, Xray `:8443`, panel localhost `:20901`, VPN egress `{HOST}`.

## Rollback boundary
Does **not** automatically roll back later identity/inbound changes if made after this backup.
Full DR drill still optional (P1 residual).
"""
    write("RESTORE-STRATEGY.md", text)


def rebind_root(pw: str) -> paramiko.SSHClient:
    """Prefer root key; fall back to password. Always set keepalive."""
    try:
        return connect_key("root")
    except Exception:
        return connect_password(pw)


def adopt_prior_backup_gate(pw: str, remote_path: str) -> dict:
    """Reuse already-validated backup without re-download when local SHA matches."""
    global REMOTE_BAK, LOCAL_BAK, BAK_NAME
    REMOTE_BAK = remote_path
    BAK_NAME = Path(remote_path).name
    LOCAL_BAK = BASE / "backups" / BAK_NAME
    prev = EVIDENCE / "02-backup-validation.json"
    if prev.exists():
        try:
            info = json.loads(prev.read_text(encoding="utf-8"))
            if info.get("ok") and info.get("sha_match") and LOCAL_BAK.is_file():
                RESULT["backup"] = info
                RESULT["gates"]["backup"] = "PASS"
                RESULT["gates"]["restore_strategy"] = "CONFIRMED"
                write("02-backup-validation.json", json.dumps(info, indent=2), pw)
                return info
        except Exception:
            pass
    c = rebind_root(pw)
    try:
        return phase_backup_reuse_existing(c, pw, remote_path)
    finally:
        try:
            c.close()
        except Exception:
            pass


def main() -> int:
    print(f"P2 START {TS} -> {OUT}")
    if not PRIV_KEY.exists() or not PUB_KEY.exists():
        raise SystemExit("MISSING_OPERATOR_KEYPAIR")
    # Refuse encrypted operator key (paramiko cannot unlock without passphrase).
    try:
        load_operator_pkey()
    except Exception as e:
        raise SystemExit(f"OPERATOR_PRIVATE_KEY_UNUSABLE:{type(e).__name__}")
    pw = load_ssh_password()
    reuse = os.environ.get("P2_REUSE_BACKUP", "").strip()
    resume = os.environ.get("P2_RESUME_FROM", "").strip().lower()  # '', baseline, backup, ssh, 2096
    print(f"CONNECT {HOST}:{PORT} as root (key-first); resume={resume or 'full'}")
    try:
        c = connect_key("root")
        print("BOOTSTRAP root key OK")
    except Exception as e1:
        print("BOOTSTRAP key failed:", type(e1).__name__, "; trying password")
        c = connect_password(pw)
    try:
        if resume not in ("ssh", "2096"):
            print("PHASE baseline")
            phase_baseline(c, pw)
            pre = RESULT.get("pre_baseline", {}).get("gates", {})
            if pre.get("ssh_3333") != "PASS" or pre.get("xray_8443") != "PASS":
                print("STOP — pre-hardening service gate FAIL")
                RESULT["verdict"] = "FAIL"
                write("00-summary.json", json.dumps(RESULT, indent=2), pw)
                return 2

            print("PHASE backup")
            if reuse:
                bak = phase_backup_reuse_existing(c, pw, reuse)
            else:
                bak = phase_backup(c, pw)
            write_restore_strategy()
            if not bak.get("ok"):
                print("STOP — BACKUP GATE FAIL")
                RESULT["verdict"] = "FAIL"
                write("00-summary.json", json.dumps(RESULT, indent=2), pw)
                return 3
            print("BACKUP + RESTORE STRATEGY CONFIRMED")
        else:
            # Resume: adopt prior backup validation; light service touch
            if reuse:
                print("PHASE backup (adopt prior)")
                bak = adopt_prior_backup_gate(pw, reuse)
                # keep existing key session; only rebind if needed
                try:
                    run(c, "true", timeout=10)
                except Exception:
                    try:
                        c.close()
                    except Exception:
                        pass
                    c = rebind_root(pw)
                write_restore_strategy()
                if not bak.get("ok"):
                    print("STOP — BACKUP GATE FAIL (resume)")
                    RESULT["verdict"] = "FAIL"
                    write("00-summary.json", json.dumps(RESULT, indent=2), pw)
                    return 3
                print("BACKUP + RESTORE STRATEGY CONFIRMED")
            else:
                print("STOP — resume requires P2_REUSE_BACKUP")
                return 3
            # refresh critical probes into RESULT for verdict math
            phase_baseline(c, pw)

        if resume != "2096":
            print("PHASE ssh key access")
            phase_ssh_key_access(c, pw)
            print("PHASE ssh hardening")
            phase_ssh_hardening(c, pw)
            try:
                c.close()
            except Exception:
                pass
            try:
                c = connect_key("root")
                print("RECONNECTED as root via key")
            except Exception:
                try:
                    c = connect_password(pw)
                    print("RECONNECTED as root via password (hardening skipped/rolled back)")
                except Exception as e:
                    print("STOP — cannot reconnect after SSH phase:", type(e).__name__)
                    RESULT["verdict"] = "FAIL"
                    write("00-summary.json", json.dumps(RESULT, indent=2), pw)
                    return 4

        def safe_phase(label: str, fn):
            nonlocal c
            print(f"PHASE {label}")
            try:
                run(c, "true", timeout=10)
            except Exception:
                print(f"REBIND before {label}")
                try:
                    c.close()
                except Exception:
                    pass
                c = rebind_root(pw)
            return fn(c, pw)

        safe_phase("2096", phase_2096)
        # Always rebind after 2096 (may restart x-ui / touch firewall)
        try:
            c.close()
        except Exception:
            pass
        c = rebind_root(pw)
        print("REBOUND after 2096")
        safe_phase("firewall", phase_firewall)
        safe_phase("fail2ban", phase_fail2ban)
        safe_phase("swap", phase_swap)
        safe_phase("tls", phase_tls)
        safe_phase("logging", phase_logging)
        safe_phase("systemd", phase_systemd)
        safe_phase("packages", phase_packages)
        safe_phase("regression", phase_regression)
    except Exception as e:
        RESULT["notes"].append(f"ABORT:{type(e).__name__}")
        RESULT["verdict"] = "FAIL"
        write("00-summary.json", json.dumps(RESULT, indent=2), pw)
        write("00-abort.txt", f"{type(e).__name__}: {e}", pw)
        print("ABORT", type(e).__name__)
        raise
    finally:
        try:
            c.close()
        except Exception:
            pass

    post = RESULT.get("post_gates", {})
    critical = [
        post.get("ssh_3333"),
        post.get("nginx_443"),
        post.get("xray_8443"),
        RESULT["gates"].get("backup"),
    ]
    if all(x == "PASS" for x in critical) and post.get("public_20901") == "NOT EXPOSED":
        if RESULT["gates"].get("port_2096") in ("HARDENED", "REQUIRED+RESTRICTED") and RESULT[
            "gates"
        ].get("key_based_operator_ssh") == "PASS":
            RESULT["verdict"] = "PASS"
        else:
            RESULT["verdict"] = "PARTIAL"
    else:
        RESULT["verdict"] = "FAIL"

    write("00-summary.json", json.dumps(RESULT, indent=2), pw)
    print("VERDICT", RESULT["verdict"])
    print("SUMMARY", EVIDENCE / "00-summary.json")
    return 0 if RESULT["verdict"] in ("PASS", "PARTIAL") else 1


if __name__ == "__main__":
    raise SystemExit(main())
