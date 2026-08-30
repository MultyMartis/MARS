#!/usr/bin/env python3
"""FriendHosting FINAL OPERATIONAL BACKUP 01.

Backup-only wave: health gate → scoped archive → local twin → hash/readability
→ post-backup regression. Does NOT mutate Xray/VLESS/nginx/SSH/UFW/fail2ban/
swap/certbot/DNS. Does NOT touch VEESP/EQVPS. No reboot.
Secrets stay out of Git evidence (redacted).
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

HOST = "92.42.99.126"
PORT = 3333
DOMAIN = "metacode-cloud.com"
KEEP = [
    "WSP-ONE",
    "MCA-PHONE",
    "Unit-01",
    "Unit-02",
    "Unit-03",
    "Unit-MichaelPhone",
]
LEGACY = "MCA-ONE-FRIENDHOSTING-DE-RAW-8443"
BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV = BASE / "ssh" / "marsops_ed25519"
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01"
)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
BAK_NAME = f"friendhosting-final-operational-{TS}"
REMOTE_DIR = "/root/mars-backups"
REMOTE_BAK = f"{REMOTE_DIR}/{BAK_NAME}.tgz"
LOCAL_BAK = BASE / "backups" / f"{BAK_NAME}.tgz"
LOCAL_RUN = BASE / f"final-operational-backup-01-{TS}"

EV.mkdir(parents=True, exist_ok=True)
LOCAL_RUN.mkdir(parents=True, exist_ok=True)
(BASE / "backups").mkdir(parents=True, exist_ok=True)

RESULT: dict = {
    "wave": "FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01",
    "ts": TS,
    "host": HOST,
    "domain": DOMAIN,
    "gates": {},
    "backup": {},
    "post": {},
    "verdict": "FAIL",
}


def redact(t: str) -> str:
    t = re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        t,
    )
    t = re.sub(r"(?i)(password|passwd|secret|token|api[_-]?key)\s*[:=]\s*\S+", r"\1=<REDACTED>", t)
    return t


def write(name: str, text: str, also_local: bool = True) -> None:
    text = redact(text)
    (EV / name).write_text(text, encoding="utf-8")
    if also_local:
        (LOCAL_RUN / name).write_text(text, encoding="utf-8")


def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')


def connect(user: str = "root") -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=PORT,
        username=user,
        pkey=load_key(),
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


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tcp(port: int, timeout: float = 8) -> bool:
    try:
        with socket.create_connection((HOST, port), timeout=timeout):
            return True
    except OSError:
        return False


def tls(port: int) -> dict:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((HOST, port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                return {"ok": True, "notAfter": ssock.getpeercert().get("notAfter")}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def dns_a(name: str) -> list[str]:
    try:
        return sorted({ai[4][0] for ai in socket.getaddrinfo(name, None, socket.AF_INET)})
    except Exception:
        return []


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


def health_gate(c: paramiko.SSHClient, label: str) -> dict:
    gates: dict = {}
    code, out, err = run(
        c,
        r"""
set -euo pipefail
echo HOSTNAME=$(hostname)
echo UNAME=$(uname -a)
echo UPTIME=$(uptime -p 2>/dev/null || uptime)
echo NPROC=$(nproc)
echo MEM_KB=$(awk '/MemTotal/{print $2}' /proc/meminfo)
echo SWAP_KB=$(awk '/SwapTotal/{print $2}' /proc/meminfo)
free -h
swapon --show || true
df -hT /
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT
ip -4 addr show scope global | sed -n '1,40p'
ip route | sed -n '1,20p'
ip link show | sed -n '1,40p'
ss -lntp | egrep ':(3333|443|8443|20901|2096|80)\b' || true
systemctl is-active ssh nginx x-ui fail2ban certbot.timer
systemctl is-enabled ssh nginx x-ui fail2ban certbot.timer 2>/dev/null || true
ufw status verbose
fail2ban-client status 2>/dev/null || true
certbot certificates 2>/dev/null || true
systemctl is-active certbot.timer
ls -la /etc/letsencrypt/renewal/ 2>/dev/null || true
grep -E 'authenticator|webroot|deploy|renew' /etc/letsencrypt/renewal/*.conf 2>/dev/null | head -n 40 || true
python3 - <<'PY'
import json, sqlite3
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select id,remark,port,protocol,settings from inbounds where port=8443').fetchone()
assert row, 'no 8443 inbound'
settings=json.loads(row['settings'] or '{}')
clients=settings.get('clients') or []
emails=[c.get('email') for c in clients]
print('CLIENT_COUNT', len(clients))
print('CLIENT_LABELS', ','.join(sorted(str(e) for e in emails)))
print('HAS_LEGACY', 'MCA-ONE-FRIENDHOSTING-DE-RAW-8443' in emails)
print('INBOUND_PROTOCOL', row['protocol'])
print('INBOUND_REMARK', row['remark'])
PY
# Panel/root may 404; accept any TCP HTTP response code as reachability.
curl -sS -o /dev/null -w 'NGINX443=%{http_code}\n' --resolve metacode-cloud.com:443:127.0.0.1 https://metacode-cloud.com/ || echo NGINX443=UNREACHABLE
curl -sS -o /dev/null -w 'XUI20901=%{http_code}\n' http://127.0.0.1:20901/ || echo XUI20901=UNREACHABLE
ss -lntp | egrep '127\\.0\\.0\\.1:20901|:8443\\b|:443\\b' || true
nginx -t 2>&1 | tail -n 3 || true
echo GATE_REMOTE_OK
""",
        timeout=120,
    )
    write(f"{label}-remote.txt", f"exit={code}\n{out}\n{err}")
    local = {
        "ssh_3333": tcp(3333),
        "tcp_443": tcp(443),
        "tcp_8443": tcp(8443),
        "tcp_80": tcp(80),
        "tcp_2096_should_fail_or_filter": tcp(2096),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
        "dns_a": dns_a(DOMAIN),
    }
    write(f"{label}-local.json", json.dumps(local, indent=2) + "\n")

    m_count = re.search(r"CLIENT_COUNT\s+(\d+)", out)
    m_labels = re.search(r"CLIENT_LABELS\s+(.+)", out)
    m_legacy = re.search(r"HAS_LEGACY\s+(\S+)", out)
    client_count = int(m_count.group(1)) if m_count else -1
    labels = sorted(m_labels.group(1).strip().split(",")) if m_labels else []
    has_legacy = (m_legacy.group(1) == "True") if m_legacy else True

    ssh_active = "GATE_REMOTE_OK" in out and code == 0
    # Any HTTP code from nginx/x-ui localhost proves listener answers (404 OK for panel root).
    nginx_http = bool(re.search(r"NGINX443=\d{3}", out)) and "NGINX443=UNREACHABLE" not in out
    xui_http = bool(re.search(r"XUI20901=\d{3}", out)) and "XUI20901=UNREACHABLE" not in out
    xui_listen = "127.0.0.1:20901" in out
    ufw_ok = "Status: active" in out and "3333" in out and "443" in out and "8443" in out
    m_swap = re.search(r"SWAP_KB=(\d+)", out)
    swap_kb = int(m_swap.group(1)) if m_swap else 0
    swap_ok = swap_kb >= 1_800_000
    code2, out2, _ = run(
        c,
        "systemctl is-active certbot.timer; systemctl is-active fail2ban; systemctl is-active x-ui; systemctl is-active nginx; systemctl is-active ssh",
        timeout=30,
    )
    parts = [p.strip() for p in out2.strip().splitlines()]
    certbot_timer = len(parts) >= 1 and parts[0] == "active"
    f2b_active = len(parts) >= 2 and parts[1] == "active"
    xui_active = len(parts) >= 3 and parts[2] == "active"
    nginx_active = len(parts) >= 4 and parts[3] == "active"
    ssh_svc = len(parts) >= 5 and parts[4] == "active"

    dns_ok = HOST in local["dns_a"]
    tls443_ok = bool(local["tls_443"].get("ok"))
    tls8443_ok = bool(local["tls_8443"].get("ok"))
    clients_ok = client_count == 6 and labels == sorted(KEEP) and not has_legacy
    webroot_hint = "webroot" in out.lower() or "authenticator = webroot" in out

    gates = {
        "ssh_3333": local["ssh_3333"] and ssh_svc,
        "nginx_443": local["tcp_443"] and nginx_active and tls443_ok and nginx_http,
        "xui_20901_localhost": xui_active and xui_listen and xui_http,
        "xray_8443": local["tcp_8443"] and xui_active and tls8443_ok,
        "tls_443": tls443_ok,
        "tls_8443": tls8443_ok,
        "dns": dns_ok,
        "ufw": ufw_ok,
        "fail2ban": f2b_active,
        "swap_2g": swap_ok,
        "certbot_timer": certbot_timer,
        "acme_webroot_signal": webroot_hint,
        "client_count_6": clients_ok,
        "client_count": client_count,
        "client_labels": labels,
        "has_legacy": has_legacy,
        "remote_ok": ssh_active,
        "services_is_active": out2.strip(),
        "swap_kb": swap_kb,
        "dns_a": local["dns_a"],
        "nginx_http_code_signal": nginx_http,
        "xui_http_code_signal": xui_http,
    }
    critical = [
        "ssh_3333",
        "nginx_443",
        "xui_20901_localhost",
        "xray_8443",
        "tls_443",
        "tls_8443",
        "dns",
        "ufw",
        "fail2ban",
        "swap_2g",
        "certbot_timer",
        "client_count_6",
        "remote_ok",
    ]
    gates["PASS"] = all(bool(gates[k]) for k in critical)
    write(f"{label}-gates.json", json.dumps(gates, indent=2) + "\n")
    return gates


def capture_safe_baseline(c: paramiko.SSHClient) -> None:
    code, out, err = run(
        c,
        r"""
set -euo pipefail
echo ===UTC===; date -u
echo ===HOSTNAME===; hostname
echo ===OS===; . /etc/os-release; echo "$PRETTY_NAME"
echo ===KERNEL===; uname -r
echo ===UPTIME===; uptime
echo ===CPU===; nproc; lscpu | egrep 'Model name|CPU\(s\)|Thread|Core' || true
echo ===MEM===; free -h
echo ===SWAP===; swapon --show; free -h | grep -i swap || true
echo ===BLOCK===; lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT
echo ===FS===; df -hT
echo ===IP===; ip -4 addr; ip route; ip link
echo ===LISTEN===; ss -lntp
echo ===VERS===;
/usr/local/x-ui/x-ui version 2>/dev/null || true
/usr/local/x-ui/bin/xray version 2>/dev/null | head -n 3 || true
nginx -v 2>&1 || true
ssh -V 2>&1 || true
fail2ban-client version 2>/dev/null || true
certbot --version 2>/dev/null || true
echo ===ENABLED===; systemctl is-enabled ssh nginx x-ui fail2ban certbot.timer 2>&1 || true
echo ===UFW===; ufw status verbose
echo ===F2B===; fail2ban-client status 2>&1 || true
echo ===CERT===; certbot certificates 2>&1 || true
echo ===RENEW===; grep -E '^(authenticator|webroot_path|deploy_hook|post_hook|renew_hook)' /etc/letsencrypt/renewal/*.conf 2>/dev/null || true
echo BASELINE_OK
""",
        timeout=120,
    )
    write("A1-safe-baseline.txt", f"exit={code}\n{out}\n{err}")


def create_backup(c: paramiko.SSHClient) -> dict:
    script = f"""
set -euo pipefail
DIR={REMOTE_DIR}
NAME={BAK_NAME}
STAGING="$DIR/$NAME"
mkdir -p "$DIR"
rm -rf "$STAGING"
mkdir -p "$STAGING/meta" "$STAGING/systemd" "$STAGING/package" "$STAGING/hooks"

cp -a /etc/ssh "$STAGING/etc-ssh"
cp -a /etc/sudoers "$STAGING/etc-sudoers" 2>/dev/null || true
cp -a /etc/sudoers.d "$STAGING/etc-sudoers.d" 2>/dev/null || true
cp -a /etc/ufw "$STAGING/etc-ufw" 2>/dev/null || true
cp -a /etc/fail2ban "$STAGING/etc-fail2ban" 2>/dev/null || true
cp -a /etc/systemd/journald.conf "$STAGING/journald.conf" 2>/dev/null || true
cp -a /etc/systemd/journald.conf.d "$STAGING/journald.conf.d" 2>/dev/null || true
cp -a /etc/nginx "$STAGING/etc-nginx"
cp -a /etc/letsencrypt "$STAGING/etc-letsencrypt"
# certbot hooks if present
cp -a /etc/letsencrypt/renewal-hooks "$STAGING/hooks/renewal-hooks" 2>/dev/null || true
ls -la /etc/letsencrypt/renewal-hooks 2>/dev/null > "$STAGING/meta/renewal-hooks-ls.txt" || true
cp -a /usr/local/x-ui "$STAGING/usr-local-x-ui" 2>/dev/null || true
mkdir -p "$STAGING/x-ui-db"
cp -a /etc/x-ui "$STAGING/x-ui-db/etc-x-ui" 2>/dev/null || true
cp -a /etc/fstab "$STAGING/fstab"
ls -la /swapfile > "$STAGING/meta/swapfile-ls.txt" 2>/dev/null || true
ss -lntup > "$STAGING/meta/ss-lntp.txt"
ufw status verbose > "$STAGING/meta/ufw-status.txt" 2>&1 || true
systemctl list-unit-files 'ssh*' 'nginx*' 'x-ui*' 'fail2ban*' 'certbot*' > "$STAGING/systemd/unit-files.txt" 2>&1 || true
systemctl status ssh nginx x-ui fail2ban certbot.timer --no-pager > "$STAGING/systemd/status.txt" 2>&1 || true
dpkg -l > "$STAGING/package/dpkg-l.txt"
getent passwd root marsops > "$STAGING/meta/passwd-slice.txt"
id marsops > "$STAGING/meta/marsops-id.txt" 2>&1 || true
ls -la /root/.ssh /home/marsops/.ssh > "$STAGING/meta/ssh-dirs.txt" 2>&1 || true
ssh-keygen -lf /root/.ssh/authorized_keys > "$STAGING/meta/root-authorized-fingerprints.txt" 2>&1 || true
ssh-keygen -lf /home/marsops/.ssh/authorized_keys > "$STAGING/meta/marsops-authorized-fingerprints.txt" 2>&1 || true
sshd -T > "$STAGING/meta/sshd-T.txt" 2>/dev/null || true
fail2ban-client status > "$STAGING/meta/fail2ban-status.txt" 2>&1 || true
certbot certificates > "$STAGING/meta/certbot-certificates.txt" 2>&1 || true
date -u > "$STAGING/meta/created-utc.txt"
uname -a > "$STAGING/meta/uname.txt"
free -h > "$STAGING/meta/free.txt"
df -hT > "$STAGING/meta/df.txt"
hostname > "$STAGING/meta/hostname.txt"
nproc > "$STAGING/meta/nproc.txt"
cat /proc/meminfo > "$STAGING/meta/meminfo.txt"
swapon --show > "$STAGING/meta/swapon.txt" 2>&1 || true
ip -4 addr > "$STAGING/meta/ip-addr.txt"
ip route > "$STAGING/meta/ip-route.txt"
ip link > "$STAGING/meta/ip-link.txt"
# safe client inventory (no UUID values)
python3 - <<'PY'
import json, sqlite3
from pathlib import Path
ST=Path("{REMOTE_DIR}/{BAK_NAME}")
con=sqlite3.connect("/etc/x-ui/x-ui.db")
con.row_factory=sqlite3.Row
row=con.execute("select id,remark,port,protocol,settings from inbounds where port=8443").fetchone()
settings=json.loads(row["settings"] or "{{}}")
clients=[{{"email":c.get("email"),"enable":c.get("enable",True),"flow":c.get("flow") or "","has_id":bool(c.get("id"))}} for c in (settings.get("clients") or [])]
safe={{
  "wave":"FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01",
  "created_utc":"{TS}",
  "inbound":{{"id":row["id"],"remark":row["remark"],"port":row["port"],"protocol":row["protocol"]}},
  "client_count":len(clients),
  "clients":clients,
}}
(ST/"meta/clients-safe.json").write_text(json.dumps(safe, indent=2)+"\\n")
assert len(clients)==6, len(clients)
assert "MCA-ONE-FRIENDHOSTING-DE-RAW-8443" not in [c["email"] for c in clients]
print("SAFE_CLIENTS", len(clients))
PY

tar -C "$DIR" -czf "$DIR/$NAME.tgz" "$NAME"
sha256sum "$DIR/$NAME.tgz" | tee "$DIR/$NAME.tgz.sha256"
stat -c '%s' "$DIR/$NAME.tgz"
tar -tzf "$DIR/$NAME.tgz" | egrep 'etc-ssh|etc-nginx|etc-letsencrypt|etc-ufw|etc-fail2ban|usr-local-x-ui|x-ui-db|systemd|ss-lntp|fstab|clients-safe|journald|sudoers' | sed -n '1,120p'
echo BACKUP_OK
"""
    remote_script = f"/tmp/mars-final-op-backup-{TS}.sh"
    sftp = c.open_sftp()
    with sftp.file(remote_script, "w") as f:
        f.write(script)
    sftp.close()
    code, out, err = run(c, f"bash {remote_script}; rm -f {remote_script}", timeout=420)
    write("B1-backup-remote.txt", f"exit={code}\n{out}\n{err}")
    if "BACKUP_OK" not in out or code != 0:
        return {"ok": False, "error": "remote backup failed", "out_tail": out[-3000:]}

    m = re.search(r"([a-f0-9]{64})\s+" + re.escape(REMOTE_BAK), out)
    remote_sha = m.group(1) if m else None
    if not remote_sha:
        _, out2, _ = run(c, f"sha256sum {REMOTE_BAK}", timeout=60)
        remote_sha = out2.split()[0] if out2.strip() else None
    m_sz = re.search(r"(?m)^(\d+)$", out)
    # prefer stat line after sha
    sizes = re.findall(r"(?m)^(\d{4,})$", out)
    remote_size = int(sizes[-1]) if sizes else None

    print("Downloading final backup twin...", flush=True)
    sftp_get(c, REMOTE_BAK, LOCAL_BAK, timeout_s=900)
    try:
        sftp = c.open_sftp()
        sftp.get(REMOTE_BAK + ".sha256", str(LOCAL_BAK) + ".sha256")
        sftp.close()
    except Exception:
        pass

    local_sha = sha256_file(LOCAL_BAK)
    local_size = LOCAL_BAK.stat().st_size
    required = {
        "etc-ssh": False,
        "etc-nginx": False,
        "etc-letsencrypt": False,
        "etc-ufw": False,
        "etc-fail2ban": False,
        "usr-local-x-ui": False,
        "x-ui-db": False,
        "fstab": False,
        "clients-safe.json": False,
        "journald": False,
        "sudoers": False,
    }
    member_sample = []
    client_meta = {}
    with tarfile.open(LOCAL_BAK, "r:gz") as tf:
        names = tf.getnames()
        member_sample = names[:250]
        joined = "\n".join(names)
        for k in required:
            required[k] = k in joined
        safe_m = next((n for n in names if n.endswith("clients-safe.json")), None)
        if safe_m:
            client_meta = json.loads(tf.extractfile(safe_m).read().decode())
    write("B1-backup-local-members.txt", "\n".join(member_sample) + f"\n...\ntotal_members={len(names)}\n")
    write("B1-clients-safe-redacted.json", json.dumps(client_meta, indent=2) + "\n")

    info = {
        "ok": bool(remote_sha)
        and remote_sha == local_sha
        and local_size > 0
        and all(required.values())
        and client_meta.get("client_count") == 6,
        "remote_path": REMOTE_BAK,
        "local_path": str(LOCAL_BAK),
        "remote_sha256": remote_sha,
        "local_sha256": local_sha,
        "sha_match": remote_sha == local_sha,
        "remote_size": remote_size,
        "local_size": local_size,
        "size_match": remote_size == local_size if remote_size else True,
        "required_sections": required,
        "archive_readable": True,
        "client_count": client_meta.get("client_count"),
        "client_labels": [c.get("email") for c in client_meta.get("clients", [])],
        "member_count": len(names),
    }
    write("B1-backup-validation.json", json.dumps(info, indent=2) + "\n")
    (LOCAL_BAK.with_suffix(LOCAL_BAK.suffix + ".sha256")).write_text(
        f"{local_sha}  {LOCAL_BAK.name}\n", encoding="utf-8"
    )
    return info


def main() -> int:
    print(f"FINAL OPERATIONAL BACKUP 01 ts={TS}", flush=True)
    print("Connecting...", flush=True)
    c = connect("root")

    print("Pre-backup health gate...", flush=True)
    pre = health_gate(c, "A0-pre")
    RESULT["gates"]["pre"] = pre
    if not pre.get("PASS"):
        RESULT["verdict"] = "FAIL"
        write("Z-summary.json", json.dumps(RESULT, indent=2) + "\n")
        print("STOP — pre-backup health gate FAIL", json.dumps(pre, indent=2))
        return 2

    print("Safe baseline capture...", flush=True)
    capture_safe_baseline(c)

    print("Creating remote archive...", flush=True)
    bak = create_backup(c)
    RESULT["backup"] = bak
    if not bak.get("ok"):
        RESULT["verdict"] = "FAIL"
        write("Z-summary.json", json.dumps(RESULT, indent=2) + "\n")
        print("STOP — backup validation FAIL", bak)
        return 3

    print("Post-backup regression...", flush=True)
    # reconnect in case long download
    try:
        c.close()
    except Exception:
        pass
    time.sleep(1)
    c = connect("root")
    post = health_gate(c, "C1-post")
    RESULT["post"] = post
    try:
        c.close()
    except Exception:
        pass

    RESULT["verdict"] = "PASS" if bak.get("ok") and post.get("PASS") else "PARTIAL"
    RESULT["mutations"] = {
        "veesp": 0,
        "eqvps": 0,
        "friendhosting_config": 0,
        "friendhosting_clients": 0,
        "friendhosting_firewall": 0,
        "friendhosting_ssh": 0,
        "friendhosting_reboot": 0,
        "secret_disclosure": 0,
        "foreign_wip": 0,
        "commit_push": 0,
    }
    write("Z-summary.json", json.dumps(RESULT, indent=2) + "\n")
    print("VERDICT", RESULT["verdict"])
    print("SHA", bak.get("local_sha256"))
    print("SIZE", bak.get("local_size"))
    print("LOCAL", LOCAL_BAK)
    print("REMOTE", REMOTE_BAK)
    return 0 if RESULT["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
