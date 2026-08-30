#!/usr/bin/env python3
"""MARS SERVER OPS DUAL LOCAL OPERATIONAL BACKUP 01.

Fresh verified operational backups of FRIENDHOSTING-DE and VEESP (MCA-VPN-001).
Backup / read-only wave: no VPN config mutation, no reboot, no admin credential change.
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

FH_HOST = "92.42.99.126"
FH_PORT = 3333
FH_DOMAIN = "metacode-cloud.com"
FH_KEEP = [
    "WSP-ONE",
    "MCA-PHONE",
    "Unit-01",
    "Unit-02",
    "Unit-03",
    "Unit-MichaelPhone",
]
FH_BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
FH_PRIV = FH_BASE / "ssh" / "marsops_ed25519"
FH_BAK_NAME = f"friendhosting-operational-{TS}"
FH_REMOTE_DIR = "/root/mars-backups"
FH_REMOTE_BAK = f"{FH_REMOTE_DIR}/{FH_BAK_NAME}.tgz"
FH_LOCAL_BAK = FH_BASE / "backups" / f"{FH_BAK_NAME}.tgz"

VE_HOST = "178.173.250.69"
VE_PORT = 22
VE_DOMAIN = "wsp-cloud.com"
VE_BASE = Path(r"X:\AI MARS\local\infrastructure\MCA-VPN-001")
VE_SECRETS = VE_BASE / "secrets.local.md"
VE_BAK_NAME = f"veesp-operational-{TS}"
VE_REMOTE_DIR = "/root/mars-backups"
VE_REMOTE_BAK = f"{VE_REMOTE_DIR}/{VE_BAK_NAME}.tgz"
VE_LOCAL_BAK = VE_BASE / "backups" / f"{VE_BAK_NAME}.tgz"

EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01"
)
LOCAL_RUN = VE_BASE / f"dual-local-backup-01-{TS}"
FH_LOCAL_RUN = FH_BASE / f"dual-local-backup-01-{TS}"

for p in (EV, LOCAL_RUN, FH_LOCAL_RUN, FH_BASE / "backups", VE_BASE / "backups"):
    p.mkdir(parents=True, exist_ok=True)

RESULT: dict = {
    "wave": "DUAL-LOCAL-OPERATIONAL-BACKUP-01",
    "ts": TS,
    "x_before": {},
    "x_after": {},
    "friendhosting": {},
    "veesp": {},
    "combined": {},
    "directory_totals": {},
    "verdict": "FAIL",
    "mutations": {
        "friendhosting_config": 0,
        "veesp_config": 0,
        "friendhosting_reboot": 0,
        "veesp_reboot": 0,
        "secret_disclosure": 0,
        "foreign_wip": 0,
        "commit_push": 0,
        "vpn_mutation": 0,
        "admin_credential_change": 0,
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


def write(name: str, text: str, *also: Path) -> None:
    text = redact(text)
    (EV / name).write_text(text, encoding="utf-8")
    for d in also:
        (d / name).write_text(text, encoding="utf-8")


def write_json(name: str, obj: dict, *also: Path) -> None:
    write(name, json.dumps(obj, indent=2) + "\n", *also)


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


def load_fh_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(FH_PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(FH_PRIV), password='""')


def connect_fh(user: str = "root") -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        FH_HOST,
        port=FH_PORT,
        username=user,
        pkey=load_fh_key(),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(20)
    return c


def connect_ve() -> paramiko.SSHClient:
    secrets = parse_kv_secrets(VE_SECRETS)
    password = secrets.get("password")
    if not password:
        raise SystemExit("VEESP password missing from local secret contour")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        secrets.get("host", VE_HOST),
        port=int(secrets.get("port", VE_PORT)),
        username=secrets.get("user", "root"),
        password=password,
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


def x_free() -> dict:
    # PowerShell-free: use ctypes GetDiskFreeSpaceExW
    import ctypes
    free_bytes = ctypes.c_ulonglong(0)
    total_bytes = ctypes.c_ulonglong(0)
    total_free = ctypes.c_ulonglong(0)
    root = ctypes.c_wchar_p("X:\\")
    ok = ctypes.windll.kernel32.GetDiskFreeSpaceExW(
        root,
        ctypes.byref(free_bytes),
        ctypes.byref(total_bytes),
        ctypes.byref(total_free),
    )
    if not ok:
        raise SystemExit("GetDiskFreeSpaceExW failed for X:")
    fb = int(free_bytes.value)
    tb = int(total_bytes.value)
    return {
        "captured_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_bytes": tb,
        "free_bytes": fb,
        "free_mib": round(fb / (1024**2), 6),
        "free_gib": round(fb / (1024**3), 6),
        "total_gib": round(tb / (1024**3), 6),
        "volume_label": "AI WS",
    }


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
    extra_checks: dict | None = None,
) -> dict:
    local_sha = sha256_file(local)
    local_size = local.stat().st_size
    required = {k: False for k in required_keys}
    names: list[str] = []
    with tarfile.open(local, "r:gz") as tf:
        names = tf.getnames()
        joined = "\n".join(names)
        for k in required:
            required[k] = k in joined
        # readability: can list and open first small text member if any
        readable = True
        for n in names:
            if n.endswith(".txt") or n.endswith(".json") or n.endswith("fstab"):
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
        "size_match": remote_size == local_size if remote_size is not None else True,
        "required_sections": required,
        "archive_readable": readable,
        "member_count": len(names),
    }
    if extra_checks:
        info.update(extra_checks)
        if not all(bool(v) for v in extra_checks.values() if isinstance(v, bool)):
            info["ok"] = False
    return info


# -------------------- FriendHosting --------------------


def fh_health(c: paramiko.SSHClient, label: str) -> dict:
    code, out, err = run(
        c,
        r"""
set -euo pipefail
echo HOSTNAME=$(hostname)
echo UNAME=$(uname -a)
echo SWAP_KB=$(awk '/SwapTotal/{print $2}' /proc/meminfo)
ss -lntp | egrep ':(3333|443|8443|20901|2096|80)\b' || true
systemctl is-active ssh nginx x-ui fail2ban certbot.timer
ufw status verbose
fail2ban-client status 2>/dev/null || true
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
PY
curl -sS -o /dev/null -w 'NGINX443=%{http_code}\n' --resolve metacode-cloud.com:443:127.0.0.1 https://metacode-cloud.com/ || echo NGINX443=UNREACHABLE
curl -sS -o /dev/null -w 'XUI20901=%{http_code}\n' http://127.0.0.1:20901/ || echo XUI20901=UNREACHABLE
nginx -t 2>&1 | tail -n 3 || true
echo GATE_REMOTE_OK
""",
        timeout=120,
    )
    write(f"{label}-fh-remote.txt", f"exit={code}\n{out}\n{err}", FH_LOCAL_RUN)
    local = {
        "ssh_3333": tcp(FH_HOST, 3333),
        "tcp_443": tcp(FH_HOST, 443),
        "tcp_8443": tcp(FH_HOST, 8443),
        "tls_443": tls(FH_HOST, 443, FH_DOMAIN),
        "tls_8443": tls(FH_HOST, 8443, FH_DOMAIN),
        "dns_a": dns_a(FH_DOMAIN),
    }
    write_json(f"{label}-fh-local.json", local, FH_LOCAL_RUN)

    m_count = re.search(r"CLIENT_COUNT\s+(\d+)", out)
    m_labels = re.search(r"CLIENT_LABELS\s+(.+)", out)
    m_legacy = re.search(r"HAS_LEGACY\s+(\S+)", out)
    client_count = int(m_count.group(1)) if m_count else -1
    labels = sorted(m_labels.group(1).strip().split(",")) if m_labels else []
    has_legacy = (m_legacy.group(1) == "True") if m_legacy else True

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

    m_swap = re.search(r"SWAP_KB=(\d+)", out)
    swap_kb = int(m_swap.group(1)) if m_swap else 0
    nginx_http = bool(re.search(r"NGINX443=\d{3}", out)) and "NGINX443=UNREACHABLE" not in out
    xui_http = bool(re.search(r"XUI20901=\d{3}", out)) and "XUI20901=UNREACHABLE" not in out
    ufw_ok = "Status: active" in out and "3333" in out and "443" in out and "8443" in out
    clients_ok = client_count == 6 and labels == sorted(FH_KEEP) and not has_legacy

    gates = {
        "ssh_3333": local["ssh_3333"] and ssh_svc,
        "nginx_443": local["tcp_443"] and nginx_active and local["tls_443"].get("ok") and nginx_http,
        "xui": xui_active and xui_http,
        "xray_8443": local["tcp_8443"] and xui_active and local["tls_8443"].get("ok"),
        "tls_443": bool(local["tls_443"].get("ok")),
        "tls_8443": bool(local["tls_8443"].get("ok")),
        "dns": FH_HOST in local["dns_a"],
        "ufw": ufw_ok,
        "fail2ban": f2b_active,
        "swap_2g": swap_kb >= 1_800_000,
        "certbot_timer": certbot_timer,
        "client_count_6": clients_ok,
        "client_count": client_count,
        "client_labels": labels,
        "has_legacy": has_legacy,
        "remote_ok": "GATE_REMOTE_OK" in out and code == 0,
        "services_is_active": out2.strip(),
    }
    critical = [
        "ssh_3333",
        "nginx_443",
        "xui",
        "xray_8443",
        "tls_443",
        "tls_8443",
        "ufw",
        "fail2ban",
        "client_count_6",
        "remote_ok",
    ]
    gates["PASS"] = all(bool(gates[k]) for k in critical)
    write_json(f"{label}-fh-gates.json", gates, FH_LOCAL_RUN)
    return gates


def fh_backup(c: paramiko.SSHClient) -> dict:
    script = f"""
set -euo pipefail
DIR={FH_REMOTE_DIR}
NAME={FH_BAK_NAME}
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
cp -a /etc/letsencrypt/renewal-hooks "$STAGING/hooks/renewal-hooks" 2>/dev/null || true
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
python3 - <<'PY'
import json, sqlite3
from pathlib import Path
ST=Path("{FH_REMOTE_DIR}/{FH_BAK_NAME}")
con=sqlite3.connect("/etc/x-ui/x-ui.db")
con.row_factory=sqlite3.Row
row=con.execute("select id,remark,port,protocol,settings from inbounds where port=8443").fetchone()
settings=json.loads(row["settings"] or "{{}}")
clients=[{{"email":c.get("email"),"enable":c.get("enable",True),"flow":c.get("flow") or "","has_id":bool(c.get("id"))}} for c in (settings.get("clients") or [])]
safe={{
  "wave":"DUAL-LOCAL-OPERATIONAL-BACKUP-01",
  "created_utc":"{TS}",
  "inbound":{{"id":row["id"],"remark":row["remark"],"port":row["port"],"protocol":row["protocol"]}},
  "client_count":len(clients),
  "clients":clients,
}}
(ST/"meta/clients-safe.json").write_text(json.dumps(safe, indent=2)+"\\n")
assert len(clients)==6, len(clients)
print("SAFE_CLIENTS", len(clients))
PY

tar -C "$DIR" -czf "$DIR/$NAME.tgz" "$NAME"
sha256sum "$DIR/$NAME.tgz" | tee "$DIR/$NAME.tgz.sha256"
stat -c '%s' "$DIR/$NAME.tgz"
echo BACKUP_OK
"""
    remote_script = f"/tmp/mars-dual-fh-backup-{TS}.sh"
    sftp = c.open_sftp()
    with sftp.file(remote_script, "w") as f:
        f.write(script)
    sftp.close()
    code, out, err = run(c, f"bash {remote_script}; rm -f {remote_script}", timeout=420)
    write("fh-backup-remote.txt", f"exit={code}\n{out}\n{err}", FH_LOCAL_RUN)
    if "BACKUP_OK" not in out or code != 0:
        return {"ok": False, "error": "remote backup failed", "out_tail": out[-3000:]}

    m = re.search(r"([a-f0-9]{64})\s+" + re.escape(FH_REMOTE_BAK), out)
    remote_sha = m.group(1) if m else None
    if not remote_sha:
        _, out2, _ = run(c, f"sha256sum {FH_REMOTE_BAK}", timeout=60)
        remote_sha = out2.split()[0] if out2.strip() else None
    sizes = re.findall(r"(?m)^(\d{4,})$", out)
    remote_size = int(sizes[-1]) if sizes else None

    print("Downloading FriendHosting twin...", flush=True)
    sftp_get(c, FH_REMOTE_BAK, FH_LOCAL_BAK, timeout_s=900)
    try:
        sftp = c.open_sftp()
        sftp.get(FH_REMOTE_BAK + ".sha256", str(FH_LOCAL_BAK) + ".sha256")
        sftp.close()
    except Exception:
        pass

    with tarfile.open(FH_LOCAL_BAK, "r:gz") as tf:
        names = tf.getnames()
        safe_m = next((n for n in names if n.endswith("clients-safe.json")), None)
        client_meta = {}
        if safe_m:
            client_meta = json.loads(tf.extractfile(safe_m).read().decode())

    info = validate_archive(
        FH_LOCAL_BAK,
        remote_sha,
        remote_size,
        [
            "etc-ssh",
            "etc-nginx",
            "etc-letsencrypt",
            "etc-ufw",
            "etc-fail2ban",
            "usr-local-x-ui",
            "x-ui-db",
            "fstab",
            "clients-safe.json",
            "journald",
            "sudoers",
        ],
        {
            "client_count_ok": client_meta.get("client_count") == 6,
            "client_count": client_meta.get("client_count"),
            "client_labels": [c.get("email") for c in client_meta.get("clients", [])],
        },
    )
    info["remote_path"] = FH_REMOTE_BAK
    info["local_path"] = str(FH_LOCAL_BAK)
    write_json("fh-backup-validation.json", info, FH_LOCAL_RUN)
    FH_LOCAL_BAK.with_suffix(FH_LOCAL_BAK.suffix + ".sha256").write_text(
        f"{info['local_sha256']}  {FH_LOCAL_BAK.name}\n", encoding="utf-8"
    )
    return info


# -------------------- VEESP --------------------


def ve_audit(c: paramiko.SSHClient, label: str) -> dict:
    code, out, err = run(
        c,
        r"""
set -euo pipefail
echo HOSTNAME=$(hostname)
echo OS=$(. /etc/os-release; echo "$PRETTY_NAME")
echo KERNEL=$(uname -r)
echo UPTIME=$(uptime -p 2>/dev/null || uptime)
echo ===VERSIONS===
/usr/local/x-ui/x-ui version 2>/dev/null || true
/usr/local/x-ui/bin/xray version 2>/dev/null | head -n 3 || true
nginx -v 2>&1 || echo nginx_absent
fail2ban-client version 2>/dev/null || echo fail2ban_absent
echo ===SERVICES===
systemctl is-active ssh x-ui fail2ban docker 2>/dev/null || true
systemctl is-enabled ssh x-ui fail2ban docker 2>/dev/null || true
echo ===LISTEN===
ss -lntp | egrep ':(22|8443|443|80|2096|20901|5928)\b' || true
echo ===FIREWALL===
ufw status verbose 2>/dev/null || echo UFW_INACTIVE_OR_ABSENT
iptables -S 2>/dev/null | head -n 40 || true
echo ===PATHS===
ls -la /etc/x-ui 2>/dev/null || true
ls -la /usr/local/x-ui 2>/dev/null | head -n 20 || true
ls -la /etc/xray 2>/dev/null || true
ls -la /root/cert 2>/dev/null || true
ls -la /etc/letsencrypt 2>/dev/null || echo letsencrypt_absent
ls -la /etc/nginx 2>/dev/null || echo nginx_etc_absent
echo ===CERT===
if [ -d /root/cert ]; then find /root/cert -maxdepth 3 -type f | sed -n '1,40p'; fi
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
PY
curl -sS -o /dev/null -w 'XUI_LOCAL=%{http_code}\n' http://127.0.0.1:20901/ 2>/dev/null || echo XUI_LOCAL=UNREACHABLE
echo GATE_REMOTE_OK
""",
        timeout=150,
    )
    write(f"{label}-ve-remote.txt", f"exit={code}\n{out}\n{err}", LOCAL_RUN)
    local = {
        "ssh_22": tcp(VE_HOST, 22),
        "tcp_8443": tcp(VE_HOST, 8443),
        "tls_8443": tls(VE_HOST, 8443, VE_DOMAIN),
        "dns_a": dns_a(VE_DOMAIN),
    }
    write_json(f"{label}-ve-local.json", local, LOCAL_RUN)

    xui_active = "active" in out  # coarse; refine below
    code2, out2, _ = run(
        c,
        "systemctl is-active ssh; systemctl is-active x-ui; systemctl is-active fail2ban 2>/dev/null || echo inactive",
        timeout=30,
    )
    parts = [p.strip() for p in out2.strip().splitlines()]
    ssh_svc = len(parts) >= 1 and parts[0] == "active"
    xui_svc = len(parts) >= 2 and parts[1] == "active"
    f2b = len(parts) >= 3 and parts[2] == "active"

    m_clients = re.search(r"CLIENTS_8443\s+(\d+)", out)
    clients_8443 = int(m_clients.group(1)) if m_clients else -1
    has_8443 = "port=8443" in out and "protocol=vless" in out.lower() or (
        "port=8443" in out and "vless" in out.lower()
    )
    # protocol line format: protocol=vless
    has_vless_8443 = bool(re.search(r"port=8443\s+protocol=vless", out, re.I))

    nginx_present = "nginx_absent" not in out and "nginx version" in out.lower()
    letsencrypt_present = "letsencrypt_absent" not in out
    cert_root = "/root/cert" in out

    gates = {
        "ssh_22": local["ssh_22"] and ssh_svc,
        "xui": xui_svc,
        "xray_8443_listen": local["tcp_8443"] and xui_svc,
        "tls_8443": bool(local["tls_8443"].get("ok")),
        "dns": VE_HOST in local["dns_a"],
        "vless_8443_inbound": has_vless_8443,
        "clients_8443": clients_8443,
        "fail2ban_active": f2b,
        "nginx_present": nginx_present,
        "letsencrypt_present": letsencrypt_present,
        "cert_root_present": cert_root,
        "remote_ok": "GATE_REMOTE_OK" in out and code == 0,
        "hostname": (re.search(r"HOSTNAME=(.+)", out) or [None, ""])[1],
        "os": (re.search(r"OS=(.+)", out) or [None, ""])[1],
        "kernel": (re.search(r"KERNEL=(.+)", out) or [None, ""])[1],
        "services_is_active": out2.strip(),
        "tls_notAfter": local["tls_8443"].get("notAfter"),
    }
    critical = [
        "ssh_22",
        "xui",
        "xray_8443_listen",
        "tls_8443",
        "dns",
        "vless_8443_inbound",
        "remote_ok",
    ]
    gates["PASS"] = all(bool(gates[k]) for k in critical) and clients_8443 >= 1
    write_json(f"{label}-ve-gates.json", gates, LOCAL_RUN)
    return gates


def ve_backup(c: paramiko.SSHClient) -> dict:
    # Discover optional paths first
    code_d, out_d, _ = run(
        c,
        r"""
set -euo pipefail
for p in /etc/x-ui /usr/local/x-ui /etc/xray /root/cert /etc/letsencrypt /etc/nginx /etc/ssh /etc/ufw /etc/fail2ban /etc/fstab; do
  if [ -e "$p" ]; then echo PRESENT:$p; else echo ABSENT:$p; fi
done
""",
        timeout=60,
    )
    write("ve-path-discovery.txt", f"exit={code_d}\n{out_d}", LOCAL_RUN)

    script = f"""
set -euo pipefail
DIR={VE_REMOTE_DIR}
NAME={VE_BAK_NAME}
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
cp -a /usr/local/x-ui "$STAGING/usr-local-x-ui" 2>/dev/null || true
mkdir -p "$STAGING/x-ui-db"
cp -a /etc/x-ui "$STAGING/x-ui-db/etc-x-ui" 2>/dev/null || true
cp -a /etc/fstab "$STAGING/fstab" 2>/dev/null || true
cp -a /etc/systemd/journald.conf "$STAGING/journald.conf" 2>/dev/null || true

# Optional MCA operational tree (docs/scripts only; skip huge historical backups to keep scope operational)
mkdir -p "$STAGING/mca-ops"
if [ -d /root/MCA ]; then
  [ -d /root/MCA/docs ] && cp -a /root/MCA/docs "$STAGING/mca-ops/docs" || true
  [ -d /root/MCA/scripts ] && cp -a /root/MCA/scripts "$STAGING/mca-ops/scripts" || true
  [ -d /root/MCA/inventory ] && cp -a /root/MCA/inventory "$STAGING/mca-ops/inventory" || true
  ls -la /root/MCA/backups 2>/dev/null > "$STAGING/meta/mca-backups-ls.txt" || true
fi

ss -lntup > "$STAGING/meta/ss-lntp.txt"
ufw status verbose > "$STAGING/meta/ufw-status.txt" 2>&1 || true
iptables -S > "$STAGING/meta/iptables-S.txt" 2>&1 || true
systemctl list-unit-files 'ssh*' 'x-ui*' 'fail2ban*' 'docker*' 'nginx*' 'certbot*' > "$STAGING/systemd/unit-files.txt" 2>&1 || true
systemctl status ssh x-ui fail2ban --no-pager > "$STAGING/systemd/status.txt" 2>&1 || true
dpkg -l > "$STAGING/package/dpkg-l.txt"
crontab -l > "$STAGING/meta/root-crontab.txt" 2>&1 || true
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
/usr/local/x-ui/x-ui version > "$STAGING/meta/x-ui-version.txt" 2>&1 || true
/usr/local/x-ui/bin/xray version > "$STAGING/meta/xray-version.txt" 2>&1 || true

python3 - <<'PY'
import json, sqlite3, os
from pathlib import Path
ST=Path("{VE_REMOTE_DIR}/{VE_BAK_NAME}")
db="/etc/x-ui/x-ui.db"
safe={{"wave":"DUAL-LOCAL-OPERATIONAL-BACKUP-01","created_utc":"{TS}","inbounds":[]}}
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
            "clients": [{{"email":c.get("email"),"enable":c.get("enable",True),"has_id":bool(c.get("id"))}} for c in clients],
        }})
(ST/"meta/clients-safe.json").write_text(json.dumps(safe, indent=2)+"\\n")
print("SAFE_INBOUNDS", len(safe["inbounds"]))
print("SAFE_CLIENTS_8443", next((i["client_count"] for i in safe["inbounds"] if i["port"]==8443), 0))
PY

tar -C "$DIR" -czf "$DIR/$NAME.tgz" "$NAME"
sha256sum "$DIR/$NAME.tgz" | tee "$DIR/$NAME.tgz.sha256"
stat -c '%s' "$DIR/$NAME.tgz"
echo BACKUP_OK
"""
    remote_script = f"/tmp/mars-dual-ve-backup-{TS}.sh"
    sftp = c.open_sftp()
    with sftp.file(remote_script, "w") as f:
        f.write(script)
    sftp.close()
    code, out, err = run(c, f"bash {remote_script}; rm -f {remote_script}", timeout=600)
    write("ve-backup-remote.txt", f"exit={code}\n{out}\n{err}", LOCAL_RUN)
    if "BACKUP_OK" not in out or code != 0:
        return {"ok": False, "error": "remote backup failed", "out_tail": out[-3000:]}

    m = re.search(r"([a-f0-9]{64})\s+" + re.escape(VE_REMOTE_BAK), out)
    remote_sha = m.group(1) if m else None
    if not remote_sha:
        _, out2, _ = run(c, f"sha256sum {VE_REMOTE_BAK}", timeout=60)
        remote_sha = out2.split()[0] if out2.strip() else None
    sizes = re.findall(r"(?m)^(\d{4,})$", out)
    remote_size = int(sizes[-1]) if sizes else None

    print("Downloading VEESP twin...", flush=True)
    sftp_get(c, VE_REMOTE_BAK, VE_LOCAL_BAK, timeout_s=900)
    try:
        sftp = c.open_sftp()
        sftp.get(VE_REMOTE_BAK + ".sha256", str(VE_LOCAL_BAK) + ".sha256")
        sftp.close()
    except Exception:
        pass

    with tarfile.open(VE_LOCAL_BAK, "r:gz") as tf:
        names = tf.getnames()
        safe_m = next((n for n in names if n.endswith("clients-safe.json")), None)
        client_meta = {}
        if safe_m:
            client_meta = json.loads(tf.extractfile(safe_m).read().decode())
        has_root_cert = any("root-cert" in n for n in names)
        has_xui = any("usr-local-x-ui" in n for n in names)
        has_db = any("x-ui-db" in n for n in names)

    required = [
        "etc-ssh",
        "usr-local-x-ui",
        "x-ui-db",
        "fstab",
        "clients-safe.json",
    ]
    # TLS material: either root-cert or letsencrypt
    info = validate_archive(
        VE_LOCAL_BAK,
        remote_sha,
        remote_size,
        required,
        {
            "tls_material_present": has_root_cert
            or any("etc-letsencrypt" in n for n in names),
            "xui_present": has_xui,
            "db_present": has_db,
            "inbounds": client_meta.get("inbounds"),
            "clients_8443": next(
                (
                    i.get("client_count")
                    for i in client_meta.get("inbounds", [])
                    if i.get("port") == 8443
                ),
                0,
            ),
        },
    )
    info["remote_path"] = VE_REMOTE_BAK
    info["local_path"] = str(VE_LOCAL_BAK)
    if info.get("clients_8443", 0) < 1:
        info["ok"] = False
    write_json("ve-backup-validation.json", info, LOCAL_RUN)
    VE_LOCAL_BAK.with_suffix(VE_LOCAL_BAK.suffix + ".sha256").write_text(
        f"{info['local_sha256']}  {VE_LOCAL_BAK.name}\n", encoding="utf-8"
    )
    return info


def main() -> int:
    print(f"DUAL LOCAL OPERATIONAL BACKUP 01 ts={TS}", flush=True)

    before = x_free()
    RESULT["x_before"] = before
    write_json("X-free-before.json", before, LOCAL_RUN)
    print(f"X free before: {before['free_bytes']} bytes ({before['free_gib']} GiB)", flush=True)

    # ---- FriendHosting ----
    print("Connecting FriendHosting...", flush=True)
    fh = connect_fh("root")
    print("FriendHosting pre-health...", flush=True)
    fh_pre = fh_health(fh, "A0-pre")
    RESULT["friendhosting"]["pre"] = fh_pre
    if not fh_pre.get("PASS"):
        RESULT["verdict"] = "FAIL"
        RESULT["friendhosting"]["backup"] = {"ok": False, "error": "pre-health FAIL"}
        write_json("Z-summary.json", RESULT, LOCAL_RUN)
        print("STOP — FriendHosting pre-health FAIL", flush=True)
        return 2

    print("FriendHosting backup...", flush=True)
    fh_bak = fh_backup(fh)
    RESULT["friendhosting"]["backup"] = fh_bak
    if not fh_bak.get("ok"):
        RESULT["verdict"] = "FAIL"
        write_json("Z-summary.json", RESULT, LOCAL_RUN)
        print("STOP — FriendHosting backup FAIL", flush=True)
        return 3

    print("FriendHosting post-health...", flush=True)
    try:
        fh.close()
    except Exception:
        pass
    time.sleep(1)
    fh = connect_fh("root")
    fh_post = fh_health(fh, "C1-post")
    RESULT["friendhosting"]["post"] = fh_post
    try:
        fh.close()
    except Exception:
        pass

    # ---- VEESP ----
    print("Connecting VEESP...", flush=True)
    ve = connect_ve()
    print("VEESP live audit...", flush=True)
    ve_pre = ve_audit(ve, "A0-pre")
    RESULT["veesp"]["pre"] = ve_pre
    if not ve_pre.get("PASS"):
        RESULT["verdict"] = "PARTIAL"
        RESULT["veesp"]["backup"] = {"ok": False, "error": "pre-audit FAIL"}
        write_json("Z-summary.json", RESULT, LOCAL_RUN)
        print("STOP — VEESP pre-audit FAIL (FriendHosting backup already done)", flush=True)
        # still record X after
        RESULT["x_after"] = x_free()
        write_json("X-free-after.json", RESULT["x_after"], LOCAL_RUN)
        write_json("Z-summary.json", RESULT, LOCAL_RUN)
        return 4

    print("VEESP backup...", flush=True)
    ve_bak = ve_backup(ve)
    RESULT["veesp"]["backup"] = ve_bak
    if not ve_bak.get("ok"):
        RESULT["verdict"] = "PARTIAL"
        write_json("Z-summary.json", RESULT, LOCAL_RUN)
        print("STOP — VEESP backup FAIL", flush=True)
        RESULT["x_after"] = x_free()
        write_json("X-free-after.json", RESULT["x_after"], LOCAL_RUN)
        write_json("Z-summary.json", RESULT, LOCAL_RUN)
        return 5

    print("VEESP post-health...", flush=True)
    try:
        ve.close()
    except Exception:
        pass
    time.sleep(1)
    ve = connect_ve()
    ve_post = ve_audit(ve, "C1-post")
    RESULT["veesp"]["post"] = ve_post
    try:
        ve.close()
    except Exception:
        pass

    after = x_free()
    RESULT["x_after"] = after
    write_json("X-free-after.json", after, LOCAL_RUN)

    fh_bytes = fh_bak["local_size"]
    ve_bytes = ve_bak["local_size"]
    combined = fh_bytes + ve_bytes
    RESULT["combined"] = {
        "friendhosting_bytes": fh_bytes,
        "veesp_bytes": ve_bytes,
        "combined_bytes": combined,
        "combined_mib": round(combined / (1024**2), 6),
        "combined_gib": round(combined / (1024**3), 6),
        "x_free_delta_bytes": before["free_bytes"] - after["free_bytes"],
    }
    RESULT["directory_totals"] = {
        "friendhosting": dir_archive_totals(FH_BASE / "backups"),
        "veesp": dir_archive_totals(VE_BASE / "backups"),
    }
    both = (
        RESULT["directory_totals"]["friendhosting"]["total_bytes"]
        + RESULT["directory_totals"]["veesp"]["total_bytes"]
    )
    RESULT["directory_totals"]["combined_bytes"] = both
    RESULT["directory_totals"]["combined_gib"] = round(both / (1024**3), 6)

    fh_ok = fh_bak.get("ok") and fh_post.get("PASS")
    ve_ok = ve_bak.get("ok") and ve_post.get("PASS")
    RESULT["verdict"] = "PASS" if fh_ok and ve_ok else "PARTIAL"
    write_json("Z-summary.json", RESULT, LOCAL_RUN, FH_LOCAL_RUN)

    print("VERDICT", RESULT["verdict"], flush=True)
    print("FH", FH_LOCAL_BAK, fh_bytes, fh_bak.get("local_sha256"), flush=True)
    print("VE", VE_LOCAL_BAK, ve_bytes, ve_bak.get("local_sha256"), flush=True)
    print("COMBINED", combined, flush=True)
    return 0 if RESULT["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
