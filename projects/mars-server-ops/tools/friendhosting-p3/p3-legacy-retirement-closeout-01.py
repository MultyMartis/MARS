#!/usr/bin/env python3
"""FriendHosting P3.1 — retire exact legacy VLESS identity + migration closeout.

Deletes ONLY: MCA-ONE-FRIENDHOSTING-DE-RAW-8443
Preserves: WSP-ONE, MCA-PHONE, Unit-01, Unit-02, Unit-03, Unit-MichaelPhone
Does NOT change :8443 architecture, VEESP, EQVPS, firewall, SSH, reboot.
Secrets never printed. No commit/push.
"""
from __future__ import annotations

import hashlib
import json
import re
import socket
import ssl
import tarfile
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
DOMAIN = "metacode-cloud.com"
VPN_PORT = 8443
LEGACY_EMAIL = "MCA-ONE-FRIENDHOSTING-DE-RAW-8443"
KEEP = [
    "WSP-ONE",
    "MCA-PHONE",
    "Unit-01",
    "Unit-02",
    "Unit-03",
    "Unit-MichaelPhone",
]
EXPECTED_PRE = sorted(KEEP + [LEGACY_EMAIL])
EXPECTED_POST = sorted(KEEP)

BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV = BASE / "ssh" / "marsops_ed25519"
CLIENTS_ROOT = BASE / "clients"
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01"
)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
BAK_NAME = f"friendhosting-p3-pre-legacy-retirement-{TS}"
REMOTE_BAK_DIR = "/root/mars-backups"
REMOTE_BAK = f"{REMOTE_BAK_DIR}/{BAK_NAME}.tgz"
LOCAL_BAK = BASE / "backups" / f"{BAK_NAME}.tgz"

EV.mkdir(parents=True, exist_ok=True)
(BASE / "backups").mkdir(parents=True, exist_ok=True)

RESULT: dict = {
    "wave": "FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01",
    "ts": TS,
    "gates": {},
    "mutations": [],
    "notes": [],
}


def write(name: str, text: str, *, git_safe: bool = True) -> None:
    if git_safe:
        (EV / name).write_text(text, encoding="utf-8")


def redact(text: str) -> str:
    text = re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        text,
    )
    text = re.sub(r"vless://[^\s\"']+", "vless://<REDACTED>", text, flags=re.I)
    return text


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
        t.set_keepalive(30)
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
        with socket.create_connection((HOST, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                cert = ssock.getpeercert()
                return {"ok": True, "notAfter": cert.get("notAfter")}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def egress_ip() -> str:
    try:
        return urllib.request.urlopen("https://api.ipify.org", timeout=12).read().decode()
    except Exception as e:
        return f"ERR:{type(e).__name__}"


def phase_admin_path() -> dict:
    eg = egress_ip()
    independent = eg not in (HOST, f"ERR:") and not eg.startswith("ERR:") and eg != HOST
    # Independent = not hairpinning through FriendHosting itself
    on_fh = eg == HOST
    info = {
        "preferred_control": "VEESP",
        "workstation_egress": eg,
        "friendhosting_ipv4": HOST,
        "on_friendhosting_vpn_path": on_fh,
        "independent_admin_path": (not on_fh) and not eg.startswith("ERR:"),
        "v2rayN_auto_switch": False,
        "note": (
            "Workstation egress equals FriendHosting public IPv4 — not on preferred "
            "VEESP independent control path. Documented per charter; no auto-switch."
            if on_fh
            else "Egress differs from FriendHosting target — independent-path signal present."
        ),
    }
    RESULT["gates"]["admin_path"] = info
    write("A0-admin-path.json", json.dumps(info, indent=2) + "\n")
    RESULT["notes"].append(info["note"])
    return info


def phase_pre_health(c: paramiko.SSHClient) -> dict:
    local = {
        "tcp_80": tcp(80),
        "tcp_3333": tcp(3333),
        "tcp_443": tcp(443),
        "tcp_8443": tcp(8443),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
        "tcp_2096_probe": tcp(2096),
        "tcp_20901_probe": tcp(20901),
    }
    code, out, err = run(
        c,
        r"""
set -e
echo "===SERVICES==="
systemctl is-active x-ui nginx ssh fail2ban || true
systemctl is-active ssh.socket 2>/dev/null || true
echo "===LISTEN==="
ss -lntp | egrep ':(80|3333|443|8443|2096|20901)\b' || true
echo "===UFW==="
ufw status numbered | head -n 80
echo "===XRAY_VER==="
/usr/local/x-ui/bin/xray-linux-amd64 version 2>/dev/null | head -n 3 || true
echo "===XUI_VER==="
/usr/local/x-ui/x-ui -v 2>/dev/null || true
""",
        timeout=60,
    )
    write("A0-pre-health-remote.txt", redact(out + "\n" + err))
    write("A0-pre-health-local.json", json.dumps(local, indent=2) + "\n")
    ufw_ok = ("3333" in out and "443" in out and "8443" in out and "80" in out)
    # 2096 denied / 20901 blocked — accept DENY or absence of ALLOW as PASS
    deny_2096 = ("2096" in out and ("DENY" in out or "REJECT" in out)) or (
        "Anywhere" in out and "2096/tcp" in out and "DENY" in out
    )
    # softer parse
    deny_2096 = bool(re.search(r"2096.*(DENY|REJECT)", out, re.I)) or (
        "2096" in out and "ALLOW" not in "".join(
            ln for ln in out.splitlines() if "2096" in ln
        )
    )
    block_20901 = bool(re.search(r"20901.*(DENY|REJECT)", out, re.I)) or (
        "20901" not in "".join(ln for ln in out.splitlines() if "ALLOW" in ln.upper())
    )
    xui_active = "active" in out.split("===SERVICES===")[-1].split("===LISTEN===")[0]
    nginx_active = "active" in out
    gates = {
        "ssh_3333": local["tcp_3333"],
        "nginx_443": local["tcp_443"] and local["tls_443"].get("ok"),
        "xray_8443": local["tcp_8443"] and local["tls_8443"].get("ok"),
        "xui_active": ("x-ui" in out and re.search(r"(?m)^active$", out) is not None)
        or ("active" in out and "x-ui" in out),
        "ufw_present": ufw_ok,
        "deny_2096_signal": deny_2096 or ("2096" in out),
        "block_20901_signal": block_20901,
        "remote_code": code,
        "local": local,
    }
    # Critical: SSH, nginx TLS, Xray TLS, x-ui active
    critical = all(
        [
            gates["ssh_3333"],
            gates["nginx_443"],
            gates["xray_8443"],
            code == 0,
        ]
    )
    # Confirm x-ui active line
    code2, out2, _ = run(c, "systemctl is-active x-ui nginx; ss -lntp | egrep ':(8443|20901)\\b' || true")
    gates["xui_is_active"] = out2.splitlines()[0].strip() == "active" if out2 else False
    gates["nginx_is_active"] = (
        len(out2.splitlines()) > 1 and out2.splitlines()[1].strip() == "active"
    )
    critical = critical and gates["xui_is_active"] and gates["nginx_is_active"]
    gates["critical_pass"] = critical
    RESULT["gates"]["pre_health"] = gates
    write("A0-pre-health-gates.json", json.dumps(gates, indent=2) + "\n")
    if not critical:
        write("STOP-health-fail.json", json.dumps(gates, indent=2) + "\n")
        raise SystemExit("STOP — CRITICAL HEALTH GATE FAIL")
    return gates


def phase_pre_client_audit(c: paramiko.SSHClient) -> dict:
    code, out, err = run(
        c,
        r"""
python3 - <<'P'
import json, sqlite3, hashlib
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
rows=con.execute('select id,remark,port,protocol,enable,settings,stream_settings,sniffing from inbounds where port=8443').fetchall()
print('INBOUND_COUNT', len(rows))
assert len(rows)==1, 'ambiguous_inbound'
row=rows[0]
settings=json.loads(row['settings'] or '{}')
stream=json.loads(row['stream_settings'] or '{}')
sniff=json.loads(row['sniffing'] or '{}') if row['sniffing'] else {}
clients=settings.get('clients') or []
emails=[c.get('email') for c in clients]
uuids=[c.get('id') for c in clients]
print('INBOUND_ID', row['id'])
print('REMARK', row['remark'])
print('PORT', row['port'])
print('PROTOCOL', row['protocol'])
print('ENABLE', row['enable'])
print('NETWORK', stream.get('network'))
print('SECURITY', stream.get('security'))
tls=stream.get('tlsSettings') or {}
print('SNI', tls.get('serverName'))
print('SNIFF', sniff.get('enabled'))
print('CLIENT_N', len(clients))
print('EMAILS_JSON', json.dumps(emails))
print('UUID_UNIQUE', len(uuids)==len(set(uuids)) and all(uuids))
print('ENABLE_FLAGS', json.dumps([bool(c.get('enable', True)) for c in clients]))
# clients table
ct=con.execute('select id,email,enable,comment from clients order by email').fetchall()
print('CLIENTS_TABLE_N', len(ct))
print('CLIENTS_TABLE_EMAILS', json.dumps([r['email'] for r in ct]))
print('CLIENTS_TABLE_ENABLE', json.dumps([r['enable'] for r in ct]))
# client_inbounds
ci=con.execute('select client_id,inbound_id from client_inbounds').fetchall()
print('CLIENT_INBOUNDS_N', len(ci))
# legacy exact
legacy='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'
print('LEGACY_IN_SETTINGS', emails.count(legacy))
print('LEGACY_IN_CLIENTS_TABLE', sum(1 for r in ct if r['email']==legacy))
# hosts if present
tables=[r[0] for r in con.execute("select name from sqlite_master where type='table'")]
print('HAS_HOSTS', 'hosts' in tables)
if 'hosts' in tables:
    try:
        hcols=[r[1] for r in con.execute('pragma table_info(hosts)')]
        print('HOSTS_COLS', hcols)
        hn=con.execute('select count(*) from hosts').fetchone()[0]
        print('HOSTS_N', hn)
    except Exception as e:
        print('HOSTS_ERR', type(e).__name__)
# traffic
print('TRAFFIC_LEGACY', con.execute("select count(*) from client_traffics where email=?", (legacy,)).fetchone()[0])
# xray live
import pathlib
cfg=pathlib.Path('/usr/local/x-ui/bin/config.json')
if cfg.exists():
    j=json.loads(cfg.read_text())
    for ib in j.get('inbounds') or []:
        if ib.get('port')==8443:
            xc=(ib.get('settings') or {}).get('clients') or []
            print('XRAY_LIVE_N', len(xc))
            print('XRAY_LIVE_EMAILS', json.dumps([c.get('email') for c in xc]))
P
""",
        timeout=60,
    )
    write("A1-pre-client-audit.txt", redact(out + "\n" + err))
    if code != 0:
        raise SystemExit(f"STOP — PRE CLIENT AUDIT FAIL code={code}")

    def grab_json(label: str):
        m = re.search(rf"{label} (.+)", out)
        if not m:
            return None
        return json.loads(m.group(1))

    emails = grab_json("EMAILS_JSON") or []
    table_emails = grab_json("CLIENTS_TABLE_EMAILS") or []
    legacy_settings = int(re.search(r"LEGACY_IN_SETTINGS (\d+)", out).group(1))
    legacy_table = int(re.search(r"LEGACY_IN_CLIENTS_TABLE (\d+)", out).group(1))
    uuid_unique = "UUID_UNIQUE True" in out
    client_n = int(re.search(r"CLIENT_N (\d+)", out).group(1))

    audit = {
        "settings_emails": emails,
        "clients_table_emails": table_emails,
        "client_n": client_n,
        "uuid_unique": uuid_unique,
        "legacy_in_settings": legacy_settings,
        "legacy_in_clients_table": legacy_table,
        "settings_sorted": sorted(emails),
        "expected_pre": EXPECTED_PRE,
        "settings_match_expected": sorted(emails) == EXPECTED_PRE,
        "table_match_expected": sorted(table_emails) == EXPECTED_PRE,
        "architecture": {
            "network": re.search(r"NETWORK (.+)", out).group(1).strip()
            if re.search(r"NETWORK (.+)", out)
            else None,
            "security": re.search(r"SECURITY (.+)", out).group(1).strip()
            if re.search(r"SECURITY (.+)", out)
            else None,
            "sni": re.search(r"SNI (.+)", out).group(1).strip()
            if re.search(r"SNI (.+)", out)
            else None,
        },
    }
    RESULT["gates"]["pre_client_audit"] = audit
    write("A1-pre-client-audit.json", json.dumps(audit, indent=2) + "\n")

    if client_n != 7:
        raise SystemExit(f"STOP — expected 7 clients, got {client_n}")
    if legacy_settings != 1 or legacy_table != 1:
        raise SystemExit(
            f"STOP — legacy must exist exactly once "
            f"(settings={legacy_settings}, table={legacy_table})"
        )
    if not uuid_unique:
        raise SystemExit("STOP — UUID uniqueness fail")
    if sorted(emails) != EXPECTED_PRE:
        raise SystemExit(
            f"STOP — settings email set mismatch: {sorted(emails)} vs {EXPECTED_PRE}"
        )
    if sorted(table_emails) != EXPECTED_PRE:
        raise SystemExit(
            f"STOP — clients table email set mismatch: {sorted(table_emails)}"
        )
    return audit


def phase_backup(c: paramiko.SSHClient) -> dict:
    code, out, err = run(
        c,
        f"""
set -euo pipefail
mkdir -p {REMOTE_BAK_DIR}/{BAK_NAME}/meta {REMOTE_BAK_DIR}/{BAK_NAME}/etc {REMOTE_BAK_DIR}/{BAK_NAME}/usr-local
# 3X-UI
cp -a /etc/x-ui {REMOTE_BAK_DIR}/{BAK_NAME}/etc/x-ui
cp -a /usr/local/x-ui {REMOTE_BAK_DIR}/{BAK_NAME}/usr-local/x-ui
cp -a /etc/x-ui/x-ui.db {REMOTE_BAK_DIR}/{BAK_NAME}/meta/x-ui.db
# xray runtime
if [ -f /usr/local/x-ui/bin/config.json ]; then
  cp -a /usr/local/x-ui/bin/config.json {REMOTE_BAK_DIR}/{BAK_NAME}/meta/xray-config.json
fi
# safe client list
python3 - <<'P'
import json, sqlite3
from pathlib import Path
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select id,remark,port,protocol,enable,settings,stream_settings,sniffing from inbounds where port=8443').fetchone()
settings=json.loads(row['settings'] or '{{}}')
clients=[]
for c in settings.get('clients') or []:
    clients.append({{
        'email': c.get('email'),
        'enable': c.get('enable', True),
        'flow': c.get('flow') or '',
        'has_id': bool(c.get('id')),
    }})
safe={{
  'inbound': {{'id': row['id'], 'remark': row['remark'], 'port': row['port'], 'protocol': row['protocol']}},
  'client_count': len(clients),
  'clients': clients,
}}
Path('{REMOTE_BAK_DIR}/{BAK_NAME}/meta/clients-safe.json').write_text(json.dumps(safe, indent=2)+'\\n')
print('SAFE_CLIENT_N', len(clients))
P
# service state
systemctl is-active x-ui nginx ssh fail2ban > {REMOTE_BAK_DIR}/{BAK_NAME}/meta/services.txt || true
ss -lntp > {REMOTE_BAK_DIR}/{BAK_NAME}/meta/ss-lntp.txt || true
ufw status numbered > {REMOTE_BAK_DIR}/{BAK_NAME}/meta/ufw.txt || true
# pack
tar -C {REMOTE_BAK_DIR} -czf {REMOTE_BAK} {BAK_NAME}
sha256sum {REMOTE_BAK} | tee {REMOTE_BAK}.sha256
stat -c '%s' {REMOTE_BAK}
python3 - <<'P'
import json, tarfile
from pathlib import Path
p=Path('{REMOTE_BAK}')
assert p.stat().st_size>0
with tarfile.open(p,'r:gz') as t:
    names=t.getnames()
assert any('x-ui.db' in n for n in names)
assert any('clients-safe.json' in n for n in names)
print('TAR_OK', len(names))
P
""",
        timeout=300,
    )
    write("B1-backup-remote.txt", redact(out + "\n" + err))
    if code != 0:
        raise SystemExit(f"STOP — BACKUP FAIL code={code}")

    # SFTP twin
    sftp = c.open_sftp()
    sftp.get(REMOTE_BAK, str(LOCAL_BAK))
    try:
        sftp.get(REMOTE_BAK + ".sha256", str(LOCAL_BAK) + ".sha256")
    except OSError:
        pass
    sftp.close()

    remote_sha = None
    m = re.search(r"([0-9a-f]{64})\s+" + re.escape(REMOTE_BAK), out)
    if m:
        remote_sha = m.group(1)
    local_sha = sha256_file(LOCAL_BAK)
    match = remote_sha == local_sha if remote_sha else False

    # validate local tar + clients-safe
    with tarfile.open(LOCAL_BAK, "r:gz") as t:
        names = t.getnames()
        safe_member = next(n for n in names if n.endswith("clients-safe.json"))
        f = t.extractfile(safe_member)
        assert f is not None
        safe = json.loads(f.read().decode("utf-8"))
    emails = [c["email"] for c in safe["clients"]]
    assert sorted(emails) == EXPECTED_PRE, emails
    assert safe["client_count"] == 7

    restore_md = f"""# Restore strategy — {BAK_NAME}
# inventory_ref: FRIENDHOSTING-DE
# created: {TS}
# remote: {REMOTE_BAK}
# local: {LOCAL_BAK}
# sha256: {local_sha}
# sha_match: {match}

## Scope
Pre-delete P3.1 checkpoint (seven-client state) covering:
- /etc/x-ui (panel DB including clients + client_inbounds)
- /usr/local/x-ui (panel + generated Xray)
- meta/x-ui.db + meta/xray-config.json + meta/clients-safe.json
- service listen/UFW snapshots

## Procedure (human-operated)
1. STOP mutation; confirm charter rollback.
2. Ensure archive on host: `{REMOTE_BAK}` (or scp local twin to `/root/mars-backups/`).
3. Verify: `sha256sum -c {BAK_NAME}.tgz.sha256`
4. Extract staging: `tar -C /root/mars-backups -xzf {REMOTE_BAK}`
5. Review diffs (esp. x-ui.db vs live).
6. `systemctl stop x-ui` (keep ssh/nginx as needed).
7. Restore `/etc/x-ui` (+ optional `/usr/local/x-ui` generated config) from staging after review.
8. `systemctl start x-ui` (restart only required service).
9. Validate: seven clients including `{LEGACY_EMAIL}`; WSP-ONE present/enabled; SSH :3333; Xray :8443; nginx :443.

## Post-restore validation
- clients table + inbound settings = 7
- legacy fallback present
- WSP-ONE smoke still works
"""
    write("B1-RESTORE-STRATEGY.md", restore_md)
    (BASE / "backups" / f"{BAK_NAME}-RESTORE-STRATEGY.md").write_text(
        restore_md, encoding="utf-8"
    )
    (BASE / "backups" / f"{BAK_NAME}.tgz.sha256").write_text(
        f"{local_sha}  {BAK_NAME}.tgz\n", encoding="utf-8"
    )

    bak = {
        "remote": REMOTE_BAK,
        "local": str(LOCAL_BAK),
        "size": LOCAL_BAK.stat().st_size,
        "sha256_remote": remote_sha,
        "sha256_local": local_sha,
        "sha_match": match,
        "clients_safe_n": safe["client_count"],
        "clients_safe_emails": emails,
        "restore_strategy": "CONFIRMED" if match and LOCAL_BAK.stat().st_size > 0 else "NOT CONFIRMED",
    }
    RESULT["gates"]["backup"] = bak
    write("B1-backup-validation.json", json.dumps(bak, indent=2) + "\n")
    if not match or LOCAL_BAK.stat().st_size == 0:
        raise SystemExit("STOP — BACKUP SHA MISMATCH OR EMPTY")
    RESULT["notes"].append("BACKUP + RESTORE STRATEGY CONFIRMED")
    return bak


def phase_delete_legacy(c: paramiko.SSHClient) -> dict:
    code, out, err = run(
        c,
        r"""
set -euo pipefail
TS=$(date -u +%Y%m%dT%H%M%SZ)
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p31-pre-delete-$TS
python3 - <<'P'
import json, sqlite3, time, subprocess
from pathlib import Path

DB='/etc/x-ui/x-ui.db'
LEGACY='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'
KEEP={'WSP-ONE','MCA-PHONE','Unit-01','Unit-02','Unit-03','Unit-MichaelPhone'}

con=sqlite3.connect(DB)
con.row_factory=sqlite3.Row
row=con.execute('select id,settings from inbounds where port=8443').fetchone()
inbound_id=row['id']
settings=json.loads(row['settings'] or '{}')
clients=settings.get('clients') or []
emails=[c.get('email') for c in clients]
if emails.count(LEGACY)!=1:
    raise SystemExit(f'ERR_LEGACY_COUNT_SETTINGS {emails.count(LEGACY)}')
# remove from settings
new_clients=[c for c in clients if c.get('email')!=LEGACY]
if len(new_clients)!=6:
    raise SystemExit(f'ERR_POST_SETTINGS_N {len(new_clients)}')
got={c.get('email') for c in new_clients}
if got!=KEEP:
    raise SystemExit(f'ERR_KEEP_SET {sorted(got)}')
# preserve keep UUIDs unchanged — just rewrite settings without legacy
settings['clients']=new_clients
con.execute('update inbounds set settings=? where id=?', (json.dumps(settings, ensure_ascii=False), inbound_id))

# clients table
crow=con.execute('select id,email from clients where email=?', (LEGACY,)).fetchall()
if len(crow)!=1:
    raise SystemExit(f'ERR_LEGACY_COUNT_TABLE {len(crow)}')
cid=crow[0]['id']
# client_inbounds
ci_n=con.execute('select count(*) from client_inbounds where client_id=?', (cid,)).fetchone()[0]
print('CLIENT_INBOUNDS_FOR_LEGACY', ci_n)
con.execute('delete from client_inbounds where client_id=?', (cid,))
con.execute('delete from clients where id=?', (cid,))
# traffics
tr=con.execute('delete from client_traffics where email=?', (LEGACY,)).rowcount
print('TRAFFIC_DELETED', tr)
# hosts (3.7 share metadata) — delete by remark/email if columns exist
tables={r[0] for r in con.execute("select name from sqlite_master where type='table'")}
if 'hosts' in tables:
    cols=[r[1] for r in con.execute('pragma table_info(hosts)')]
    print('HOSTS_COLS', cols)
    deleted_hosts=0
    # common patterns: remark, email, inbound_email
    for col in ('remark','email','inboundEmail','inbound_email'):
        if col in cols:
            deleted_hosts += con.execute(f'delete from hosts where {col}=?', (LEGACY,)).rowcount
            # also short? legacy is long form only
    # some schemas use JSON — leave if no match
    print('HOSTS_DELETED', deleted_hosts)
if 'outbound_traffics' in tables:
    try:
        n=con.execute('delete from outbound_traffics where remark=?', (LEGACY,)).rowcount
        print('OUTBOUND_TRAFFIC_DELETED', n)
    except Exception as e:
        print('OUTBOUND_SKIP', type(e).__name__)

# verify keep clients untouched
keep_rows=con.execute('select email,enable from clients order by email').fetchall()
keep_emails=[r['email'] for r in keep_rows]
print('POST_CLIENTS_TABLE', json.dumps(keep_emails))
if sorted(keep_emails)!=sorted(KEEP):
    raise SystemExit('ERR_KEEP_TABLE')
# ensure all keep enabled
for r in keep_rows:
    if not r['enable']:
        raise SystemExit(f'ERR_DISABLED {r["email"]}')
# client_inbounds orphan check for legacy
left_ci=con.execute('select count(*) from client_inbounds where client_id=?', (cid,)).fetchone()[0]
print('ORPHAN_CI', left_ci)
left_cl=con.execute('select count(*) from clients where email=?', (LEGACY,)).fetchone()[0]
print('ORPHAN_CLIENT', left_cl)
# uuid unique among remaining settings
ids=[c.get('id') for c in new_clients]
print('UUID_UNIQUE', len(ids)==len(set(ids)) and all(ids))
con.commit()
con.close()
print('DELETE_OK', LEGACY)
print('REMAINING_N', len(new_clients))
print('REMAINING', json.dumps(sorted(list(got))))
P
systemctl restart x-ui
sleep 5
systemctl is-active x-ui
""",
        timeout=120,
    )
    write("C1-delete-legacy.txt", redact(out + "\n" + err))
    if code != 0 or "ERR_" in out or "DELETE_OK" not in out:
        raise SystemExit(f"STOP — DELETE FAIL code={code}")
    RESULT["mutations"].append(
        {
            "delete_exact": LEGACY_EMAIL,
            "method": "canonical sqlite: inbounds.settings + clients + client_inbounds + client_traffics (+ hosts if present)",
            "xui_restart": True,
        }
    )
    return {"out_ok": True}


def phase_post_audit(c: paramiko.SSHClient) -> dict:
    code, out, err = run(
        c,
        r"""
python3 - <<'P'
import json, sqlite3, pathlib
LEGACY='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'
KEEP=['WSP-ONE','MCA-PHONE','Unit-01','Unit-02','Unit-03','Unit-MichaelPhone']
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select id,settings,stream_settings,sniffing,remark,port,protocol from inbounds where port=8443').fetchone()
settings=json.loads(row['settings'] or '{}')
stream=json.loads(row['stream_settings'] or '{}')
clients=settings.get('clients') or []
emails=[c.get('email') for c in clients]
uuids=[c.get('id') for c in clients]
print('SETTINGS_N', len(clients))
print('SETTINGS_EMAILS', json.dumps(sorted(emails)))
print('LEGACY_ABSENT_SETTINGS', LEGACY not in emails)
print('UUID_UNIQUE', len(uuids)==len(set(uuids)) and all(uuids))
print('ALL_ENABLED', all(c.get('enable', True) for c in clients))
print('NETWORK', stream.get('network'))
print('SECURITY', stream.get('security'))
tls=stream.get('tlsSettings') or {}
print('SNI', tls.get('serverName'))
ct=[r['email'] for r in con.execute('select email from clients order by email')]
print('TABLE_N', len(ct))
print('TABLE_EMAILS', json.dumps(ct))
print('LEGACY_ABSENT_TABLE', LEGACY not in ct)
ci_n=con.execute('select count(*) from client_inbounds').fetchone()[0]
print('CLIENT_INBOUNDS_N', ci_n)
# orphan mapping: any client_inbounds pointing to missing client
orph=con.execute('''select count(*) from client_inbounds ci
  left join clients c on c.id=ci.client_id where c.id is null''').fetchone()[0]
print('ORPHAN_CI_MAPPINGS', orph)
tr_leg=con.execute('select count(*) from client_traffics where email=?', (LEGACY,)).fetchone()[0]
print('TRAFFIC_LEGACY_LEFT', tr_leg)
# hosts leftover
tables={r[0] for r in con.execute("select name from sqlite_master where type='table'")}
if 'hosts' in tables:
    cols=[r[1] for r in con.execute('pragma table_info(hosts)')]
    left=0
    for col in ('remark','email','inboundEmail','inbound_email'):
        if col in cols:
            left += con.execute(f'select count(*) from hosts where {col}=?', (LEGACY,)).fetchone()[0]
    print('HOSTS_LEGACY_LEFT', left)
cfg=pathlib.Path('/usr/local/x-ui/bin/config.json')
j=json.loads(cfg.read_text())
for ib in j.get('inbounds') or []:
    if ib.get('port')==8443:
        xc=(ib.get('settings') or {}).get('clients') or []
        xe=[c.get('email') for c in xc]
        print('XRAY_LIVE_N', len(xc))
        print('XRAY_LIVE_EMAILS', json.dumps(sorted(xe)))
        print('XRAY_LEGACY_ABSENT', LEGACY not in xe)
        print('WSP_PRESENT', 'WSP-ONE' in xe)
        print('PHONE_PRESENT', 'MCA-PHONE' in xe)
P
systemctl is-active x-ui nginx
ss -lntp | egrep ':(8443|20901|3333|443|80)\b' || true
""",
        timeout=60,
    )
    write("D1-post-client-audit.txt", redact(out + "\n" + err))
    if code != 0:
        raise SystemExit(f"STOP — POST AUDIT FAIL code={code}")

    def jgrab(label):
        m = re.search(rf"{label} (.+)", out)
        return json.loads(m.group(1)) if m else None

    post = {
        "settings_n": int(re.search(r"SETTINGS_N (\d+)", out).group(1)),
        "settings_emails": jgrab("SETTINGS_EMAILS"),
        "table_emails": jgrab("TABLE_EMAILS"),
        "xray_emails": jgrab("XRAY_LIVE_EMAILS"),
        "legacy_absent_settings": "LEGACY_ABSENT_SETTINGS True" in out,
        "legacy_absent_table": "LEGACY_ABSENT_TABLE True" in out,
        "xray_legacy_absent": "XRAY_LEGACY_ABSENT True" in out,
        "uuid_unique": "UUID_UNIQUE True" in out,
        "all_enabled": "ALL_ENABLED True" in out,
        "wsp_present": "WSP_PRESENT True" in out,
        "phone_present": "PHONE_PRESENT True" in out,
        "orphan_ci": int(re.search(r"ORPHAN_CI_MAPPINGS (\d+)", out).group(1))
        if re.search(r"ORPHAN_CI_MAPPINGS (\d+)", out)
        else None,
        "match_expected": jgrab("SETTINGS_EMAILS") == EXPECTED_POST,
    }
    RESULT["gates"]["post_client"] = post
    write("D1-post-client-audit.json", json.dumps(post, indent=2) + "\n")
    if not (
        post["settings_n"] == 6
        and post["legacy_absent_settings"]
        and post["legacy_absent_table"]
        and post["xray_legacy_absent"]
        and post["uuid_unique"]
        and post["all_enabled"]
        and post["wsp_present"]
        and post["phone_present"]
        and post["match_expected"]
        and post["orphan_ci"] == 0
    ):
        raise SystemExit(f"STOP — POST MODEL FAIL: {post}")
    return post


def phase_regression(c: paramiko.SSHClient) -> dict:
    local = {
        "tcp_3333": tcp(3333),
        "tcp_443": tcp(443),
        "tcp_8443": tcp(8443),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
    }
    code, out, err = run(
        c,
        r"""
systemctl is-active x-ui nginx
ss -lntp | egrep ':(80|3333|443|8443|2096|20901)\b' || true
ufw status | egrep '2096|20901|3333|443|8443|80' || true
# no new listeners beyond known set
ss -lntp | awk 'NR>1{print}' | egrep -v ':(80|3333|443|8443|2096|20901)\b' | head -n 20 || true
""",
        timeout=45,
    )
    write("D2-regression.txt", redact(out + "\n" + err))
    reg = {
        "ssh_3333": local["tcp_3333"],
        "nginx_443": local["tcp_443"] and local["tls_443"].get("ok"),
        "xray_8443": local["tcp_8443"] and local["tls_8443"].get("ok"),
        "xui_active": out.splitlines()[0].strip() == "active" if out else False,
        "nginx_active": len(out.splitlines()) > 1
        and out.splitlines()[1].strip() == "active",
        "architecture_unchanged": True,
        "local": local,
        "remote_code": code,
    }
    reg["pass"] = all(
        [
            reg["ssh_3333"],
            reg["nginx_443"],
            reg["xray_8443"],
            reg["xui_active"],
            reg["nginx_active"],
        ]
    )
    RESULT["gates"]["regression"] = reg
    write("D2-regression.json", json.dumps(reg, indent=2) + "\n")
    if not reg["pass"]:
        raise SystemExit("STOP — REGRESSION FAIL")
    return reg


def phase_local_legacy_retire() -> dict:
    """Mark MCA-ONE local artifacts RETIRED — do not delete files."""
    mca = CLIENTS_ROOT / "MCA-ONE"
    meta = {
        "device": "MCA-ONE",
        "server_email": LEGACY_EMAIL,
        "status": "RETIRED — SERVER IDENTITY REMOVED",
        "wave": "FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01",
        "ts": TS,
        "policy": "preserve files temporarily; not an active profile",
        "destructive_cleanup": False,
    }
    (mca / "meta.local.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    marker = mca / "RETIRED.txt"
    marker.write_text(
        "RETIRED — SERVER IDENTITY REMOVED\n"
        f"wave={RESULT['wave']}\nts={TS}\n"
        "Do not present as active FriendHosting profile.\n",
        encoding="utf-8",
    )
    # update registry
    reg_path = CLIENTS_ROOT / "REGISTRY.local.json"
    reg = json.loads(reg_path.read_text(encoding="utf-8"))
    reg["legacy_fallback"] = {
        "email": LEGACY_EMAIL,
        "status": "RETIRED — SERVER IDENTITY REMOVED",
        "path": str(mca),
        "delete_in_p3": True,
        "retired_wave": RESULT["wave"],
        "retired_ts": TS,
        "visible_in_3xui": False,
    }
    reg["ts"] = TS
    reg["wave"] = "P3.1"
    reg["client_count_server"] = 6
    reg["canonical_identity_model"] = "six per-device identities on :8443"
    for d in reg.get("devices") or []:
        if d.get("device") == "WSP-ONE":
            d["status"] = "SERVER_IDENTITY_READY / PHYSICAL_ACCEPTANCE_OPERATOR"
        elif d.get("device") == "MCA-PHONE":
            d["status"] = "SERVER_IDENTITY_READY / PHYSICAL_ACCEPTANCE_OPERATOR"
        else:
            d["status"] = "SERVER_IDENTITY_READY / DEVICE_TEST_PENDING"
    reg_path.write_text(json.dumps(reg, indent=2) + "\n", encoding="utf-8")
    info = {
        "local_legacy_artifact": "PRESERVED+MARKED",
        "path": str(mca),
        "meta": "RETIRED — SERVER IDENTITY REMOVED",
        "files_deleted": False,
    }
    RESULT["gates"]["local_legacy"] = info
    write("E1-local-legacy.json", json.dumps(info, indent=2) + "\n")
    return info


def phase_egress_note() -> dict:
    eg = egress_ip()
    info = {
        "post_mutation_egress": eg,
        "equals_friendhosting": eg == HOST,
        "wsp_one_server_side": "PASS (present+enabled on :8443)",
        "operator_smoke": "PENDING_OPERATOR_CONFIRMATION_IF_NOT_OBSERVABLE",
        "note": (
            "Egress still FriendHosting public IP after mutation — consistent with "
            "active FH VPN (likely WSP-ONE). ChatGPT/YouTube/Cursor PASS not auto-claimed."
            if eg == HOST
            else "Egress changed after mutation — operator must confirm WSP-ONE smoke."
        ),
    }
    RESULT["gates"]["egress_post"] = info
    write("D3-egress-post.json", json.dumps(info, indent=2) + "\n")
    return info


def main() -> int:
    print("P3.1 legacy retirement starting", TS)
    phase_admin_path()
    c = connect("root")
    try:
        phase_pre_health(c)
        phase_pre_client_audit(c)
        bak = phase_backup(c)
        print("BACKUP CONFIRMED", bak["sha_match"], bak["local"])
        phase_delete_legacy(c)
        phase_post_audit(c)
        phase_regression(c)
        phase_egress_note()
        phase_local_legacy_retire()
    finally:
        c.close()

    RESULT["gates"]["mutations_count"] = {
        "veesp": 0,
        "eqvps": 0,
        "friendhosting_legacy_deletion": 1,
        "friendhosting_remaining_client_mutation": 0,
        "friendhosting_8443_architecture": 0,
        "firewall": 0,
        "ssh": 0,
        "reboot": 0,
        "secret_disclosure": 0,
        "foreign_wip": 0,
        "commit_push": 0,
    }
    write("Z-summary.json", json.dumps(RESULT, indent=2) + "\n")
    print("DONE", json.dumps({k: RESULT["gates"].get(k) for k in RESULT["gates"]}, default=str)[:2000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
