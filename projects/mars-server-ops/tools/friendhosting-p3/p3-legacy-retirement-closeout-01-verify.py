#!/usr/bin/env python3
"""P3.1 post-delete verification + local mark (deletion already observed)."""
from __future__ import annotations

import hashlib
import json
import re
import socket
import ssl
import tarfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
DOMAIN = "metacode-cloud.com"
LEGACY = "MCA-ONE-FRIENDHOSTING-DE-RAW-8443"
KEEP = [
    "WSP-ONE",
    "MCA-PHONE",
    "Unit-01",
    "Unit-02",
    "Unit-03",
    "Unit-MichaelPhone",
]
EXPECTED = sorted(KEEP)
BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV = BASE / "ssh" / "marsops_ed25519"
CLIENTS_ROOT = BASE / "clients"
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01"
)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
REMOTE_FULL = "/root/mars-backups/friendhosting-p3-pre-legacy-retirement-20260830T120733Z.tgz"
REMOTE_SHA_FULL = "4952b6368ad884be1a6737506f7f81c8464aaa28cb2e44807c038049918abac8"
# Pre-delete essential twin from successful lean download before mutation
REMOTE_LEAN = "/root/mars-backups/friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz"
LOCAL_LEAN = BASE / "backups" / "friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz"


def redact(t: str) -> str:
    return re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        t,
    )


def write(name: str, text: str) -> None:
    (EV / name).write_text(text, encoding="utf-8")


def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')


def connect():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=PORT,
        username="root",
        pkey=load_key(),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(15)
    return c


def run(c, cmd, timeout=120):
    _, o, e = c.exec_command(cmd, timeout=timeout)
    out = o.read().decode("utf-8", "replace")
    err = e.read().decode("utf-8", "replace")
    return o.channel.recv_exit_status(), out, err


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tcp(port: int) -> bool:
    try:
        with socket.create_connection((HOST, port), timeout=8):
            return True
    except OSError:
        return False


def tls(port: int) -> dict:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((HOST, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                return {"ok": True, "notAfter": ssock.getpeercert().get("notAfter")}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def main() -> int:
    c = connect()

    # Confirm backup integrity
    code, out, err = run(
        c,
        f"""
sha256sum {REMOTE_FULL} {REMOTE_LEAN}
python3 - <<'P'
import tarfile, json
from pathlib import Path
# full
t=tarfile.open('{REMOTE_FULL}','r:gz')
names=t.getnames()
assert any('x-ui.db' in n for n in names)
sm=next(n for n in names if n.endswith('clients-safe.json'))
safe=json.loads(t.extractfile(sm).read().decode())
print('FULL_SAFE_N', safe['client_count'])
print('FULL_HAS_LEGACY', any(x['email']=='{LEGACY}' for x in safe['clients']))
# lean
t2=tarfile.open('{REMOTE_LEAN}','r:gz')
names2=t2.getnames()
sm2=next(n for n in names2 if n.endswith('clients-safe.json'))
safe2=json.loads(t2.extractfile(sm2).read().decode())
print('LEAN_SAFE_N', safe2['client_count'])
print('LEAN_HAS_LEGACY', any(x['email']=='{LEGACY}' for x in safe2['clients']))
print('LEAN_EMAILS', json.dumps(sorted(x['email'] for x in safe2['clients'])))
# check if delete already applied - look for pre-delete db snapshots
import glob
print('PREDELETE_DB_SNAPS', glob.glob('/root/mars-backups/x-ui.db.p31-pre-delete-*'))
P
""",
    )
    write("B2-backup-integrity.txt", redact(out + "\n" + err))
    print(out)

    lean_sha_remote = None
    for line in out.splitlines():
        if REMOTE_LEAN in line and re.match(r"[0-9a-f]{64}", line):
            lean_sha_remote = line.split()[0]
    if not LOCAL_LEAN.exists():
        # re-download lean quickly
        sftp = c.open_sftp()
        sftp.get(REMOTE_LEAN, str(LOCAL_LEAN))
        sftp.close()
    lean_sha_local = sha256_file(LOCAL_LEAN)
    lean_match = lean_sha_local == lean_sha_remote if lean_sha_remote else False

    with tarfile.open(LOCAL_LEAN, "r:gz") as t:
        sm = next(n for n in t.getnames() if n.endswith("clients-safe.json"))
        safe = json.loads(t.extractfile(sm).read().decode())
    assert safe["client_count"] == 7
    assert any(x["email"] == LEGACY for x in safe["clients"])

    bak = {
        "remote_full": REMOTE_FULL,
        "sha256_full_remote": REMOTE_SHA_FULL,
        "remote_essential": REMOTE_LEAN,
        "local_essential": str(LOCAL_LEAN),
        "sha256_essential_remote": lean_sha_remote,
        "sha256_essential_local": lean_sha_local,
        "sha_match_essential": lean_match,
        "size_essential": LOCAL_LEAN.stat().st_size,
        "essential_pre_delete_clients": 7,
        "essential_has_legacy": True,
        "restore_strategy": "CONFIRMED" if lean_match else "NOT CONFIRMED",
        "primary_local_twin": str(LOCAL_LEAN),
    }
    write("B1-backup-validation.json", json.dumps(bak, indent=2) + "\n")
    restore_md = f"""# Restore strategy — pre-legacy-retirement
# inventory_ref: FRIENDHOSTING-DE
# remote_full: {REMOTE_FULL}
# sha256_full: {REMOTE_SHA_FULL}
# remote_essential: {REMOTE_LEAN}
# local_essential: {LOCAL_LEAN}
# sha256_essential: {lean_sha_local}
# sha_match_essential: {lean_match}

## Scope
Pre-delete seven-client checkpoint (includes legacy `{LEGACY}`).

## Procedure
1. STOP mutation.
2. Verify SHA of essential or full archive.
3. Extract staging under `/root/mars-backups/`.
4. `systemctl stop x-ui`
5. Restore `/etc/x-ui` (from essential or full) after review.
6. Optionally restore `meta/xray-config.json` into `/usr/local/x-ui/bin/config.json` if generator lag.
7. `systemctl start x-ui`
8. Verify **7** clients including legacy; WSP-ONE enabled; SSH :3333; Xray :8443; nginx :443.

## Post-restore
- seven clients
- WSP-ONE smoke
"""
    write("B1-RESTORE-STRATEGY.md", restore_md)
    (BASE / "backups" / "friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z-RESTORE-STRATEGY.md").write_text(
        restore_md, encoding="utf-8"
    )
    (BASE / "backups" / "friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz.sha256").write_text(
        f"{lean_sha_local}  friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz\n",
        encoding="utf-8",
    )
    if not lean_match:
        raise SystemExit("STOP — lean SHA mismatch")
    print("BACKUP CONFIRMED", lean_match)

    # Post state audit
    code, out, err = run(
        c,
        r"""
python3 - <<'P'
import json, sqlite3, pathlib
LEGACY='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'
KEEP=['MCA-PHONE','Unit-01','Unit-02','Unit-03','Unit-MichaelPhone','WSP-ONE']
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select settings,stream_settings,sniffing,remark,port,protocol from inbounds where port=8443').fetchone()
settings=json.loads(row['settings'] or '{}')
stream=json.loads(row['stream_settings'] or '{}')
sniff=json.loads(row['sniffing'] or '{}') if row['sniffing'] else {}
clients=settings.get('clients') or []
emails=sorted(c.get('email') for c in clients)
uuids=[c.get('id') for c in clients]
print('SETTINGS_N', len(clients))
print('SETTINGS_EMAILS', json.dumps(emails))
print('LEGACY_ABSENT_SETTINGS', LEGACY not in emails)
print('UUID_UNIQUE', len(uuids)==len(set(uuids)) and all(uuids))
print('ALL_ENABLED', all(c.get('enable', True) for c in clients))
print('NETWORK', stream.get('network'))
print('SECURITY', stream.get('security'))
print('SNI', (stream.get('tlsSettings') or {}).get('serverName'))
print('SNIFF', sniff.get('enabled'))
print('REMARK', row['remark'])
ct=sorted(r['email'] for r in con.execute('select email from clients'))
print('TABLE_N', len(ct))
print('TABLE_EMAILS', json.dumps(ct))
print('LEGACY_ABSENT_TABLE', LEGACY not in ct)
print('CLIENT_INBOUNDS_N', con.execute('select count(*) from client_inbounds').fetchone()[0])
print('ORPHAN_CI', con.execute('''select count(*) from client_inbounds ci left join clients c on c.id=ci.client_id where c.id is null''').fetchone()[0])
print('TRAFFIC_LEGACY_LEFT', con.execute('select count(*) from client_traffics where email=?', (LEGACY,)).fetchone()[0])
tables={r[0] for r in con.execute("select name from sqlite_master where type='table'")}
if 'hosts' in tables:
    cols=[r[1] for r in con.execute('pragma table_info(hosts)')]
    left=0
    for col in ('remark','email','inboundEmail','inbound_email'):
        if col in cols:
            left += con.execute(f'select count(*) from hosts where {col}=?', (LEGACY,)).fetchone()[0]
    print('HOSTS_LEGACY_LEFT', left)
j=json.loads(pathlib.Path('/usr/local/x-ui/bin/config.json').read_text())
for ib in j.get('inbounds') or []:
    if ib.get('port')==8443:
        xe=sorted(c.get('email') for c in (ib.get('settings') or {}).get('clients') or [])
        print('XRAY_LIVE_N', len(xe))
        print('XRAY_LIVE_EMAILS', json.dumps(xe))
        print('XRAY_LEGACY_ABSENT', LEGACY not in xe)
        print('WSP_PRESENT', 'WSP-ONE' in xe)
        print('PHONE_PRESENT', 'MCA-PHONE' in xe)
# find how deletion happened
import glob, os
snaps=sorted(glob.glob('/root/mars-backups/x-ui.db.p31-pre-delete-*'))
print('DELETE_SNAPS', json.dumps(snaps))
P
systemctl is-active x-ui nginx
ss -lntp | egrep ':(80|3333|443|8443|20901|2096)\b' || true
ufw status numbered | head -n 40
""",
    )
    write("D1-post-client-audit.txt", redact(out + "\n" + err))
    post = {
        "settings_n": int(re.search(r"SETTINGS_N (\d+)", out).group(1)),
        "settings_emails": json.loads(re.search(r"SETTINGS_EMAILS (.+)", out).group(1)),
        "table_emails": json.loads(re.search(r"TABLE_EMAILS (.+)", out).group(1)),
        "xray_emails": json.loads(re.search(r"XRAY_LIVE_EMAILS (.+)", out).group(1)),
        "legacy_absent": all(
            x in out
            for x in (
                "LEGACY_ABSENT_SETTINGS True",
                "LEGACY_ABSENT_TABLE True",
                "XRAY_LEGACY_ABSENT True",
            )
        ),
        "uuid_unique": "UUID_UNIQUE True" in out,
        "all_enabled": "ALL_ENABLED True" in out,
        "wsp": "WSP_PRESENT True" in out,
        "phone": "PHONE_PRESENT True" in out,
        "orphan_ci": int(re.search(r"ORPHAN_CI (\d+)", out).group(1)),
        "architecture": {
            "network": re.search(r"NETWORK (.+)", out).group(1).strip(),
            "security": re.search(r"SECURITY (.+)", out).group(1).strip(),
            "sni": re.search(r"SNI (.+)", out).group(1).strip(),
            "remark": re.search(r"REMARK (.+)", out).group(1).strip(),
        },
        "delete_snaps": json.loads(re.search(r"DELETE_SNAPS (.+)", out).group(1))
        if re.search(r"DELETE_SNAPS (.+)", out)
        else [],
    }
    write("D1-post-client-audit.json", json.dumps(post, indent=2) + "\n")
    print("POST", json.dumps(post, indent=2))
    if not (
        post["settings_n"] == 6
        and post["legacy_absent"]
        and post["uuid_unique"]
        and post["all_enabled"]
        and post["wsp"]
        and post["phone"]
        and post["orphan_ci"] == 0
        and post["settings_emails"] == EXPECTED
        and post["xray_emails"] == EXPECTED
        and post["architecture"]["security"] == "tls"
        and post["architecture"]["sni"] == "metacode-cloud.com"
    ):
        raise SystemExit(f"POST FAIL {post}")

    # If deletion snaps empty but state is correct — check C1 evidence from earlier run
    c1 = EV / "C1-delete-legacy.txt"
    deletion_method = "observed_post_state_six_clients"
    if c1.exists() and "DELETE_OK" in c1.read_text(encoding="utf-8", errors="replace"):
        deletion_method = "canonical sqlite (inbounds.settings + clients + client_inbounds + traffics) + x-ui restart"
    elif post["delete_snaps"]:
        deletion_method = "canonical sqlite via p31 script (pre-delete db snap present)"

    local = {
        "tcp_3333": tcp(3333),
        "tcp_443": tcp(443),
        "tcp_8443": tcp(8443),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
    }
    code2, out2, _ = run(c, "systemctl is-active x-ui nginx")
    reg = {
        "ssh_3333": local["tcp_3333"],
        "nginx_443": local["tcp_443"] and local["tls_443"].get("ok"),
        "xray_8443": local["tcp_8443"] and local["tls_8443"].get("ok"),
        "xui_active": out2.splitlines()[0].strip() == "active",
        "nginx_active": out2.splitlines()[1].strip() == "active",
        "local": local,
        "ufw_excerpt_in_D1": True,
    }
    reg["pass"] = all(
        [reg["ssh_3333"], reg["nginx_443"], reg["xray_8443"], reg["xui_active"], reg["nginx_active"]]
    )
    write("D2-regression.json", json.dumps(reg, indent=2) + "\n")
    write("D2-regression.txt", redact(out2 + "\n" + out))
    if not reg["pass"]:
        raise SystemExit("REGRESSION FAIL")

    try:
        eg = urllib.request.urlopen("https://api.ipify.org", timeout=12).read().decode()
    except Exception as e:
        eg = f"ERR:{type(e).__name__}"
    write(
        "D3-egress-post.json",
        json.dumps({"egress": eg, "on_fh": eg == HOST, "wsp_server": "PASS", "phone_server": "PASS"}, indent=2)
        + "\n",
    )

    # Local legacy mark
    mca = CLIENTS_ROOT / "MCA-ONE"
    meta = {
        "device": "MCA-ONE",
        "server_email": LEGACY,
        "status": "RETIRED — SERVER IDENTITY REMOVED",
        "wave": "FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01",
        "ts": TS,
        "policy": "preserve files temporarily; not an active profile",
        "destructive_cleanup": False,
    }
    (mca / "meta.local.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (mca / "RETIRED.txt").write_text(
        "RETIRED — SERVER IDENTITY REMOVED\n"
        f"wave=FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01\nts={TS}\n"
        "Do not present as active FriendHosting profile.\n",
        encoding="utf-8",
    )
    reg_path = CLIENTS_ROOT / "REGISTRY.local.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    registry["legacy_fallback"] = {
        "email": LEGACY,
        "status": "RETIRED — SERVER IDENTITY REMOVED",
        "path": str(mca),
        "delete_in_p3": True,
        "retired_wave": "FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01",
        "retired_ts": TS,
        "visible_in_3xui": False,
    }
    registry["ts"] = TS
    registry["wave"] = "P3.1"
    registry["client_count_server"] = 6
    registry["canonical_identity_model"] = "six per-device identities on :8443"
    for d in registry.get("devices") or []:
        if d.get("device") in ("WSP-ONE", "MCA-PHONE"):
            d["status"] = "SERVER_IDENTITY_READY / CHARTER_PHYSICAL_PASS"
        else:
            d["status"] = "SERVER_IDENTITY_READY / DEVICE_TEST_PENDING"
    reg_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    write(
        "E1-local-legacy.json",
        json.dumps(
            {
                "local_legacy_artifact": "PRESERVED+MARKED",
                "path": str(mca),
                "status": "RETIRED — SERVER IDENTITY REMOVED",
            },
            indent=2,
        )
        + "\n",
    )

    summary = {
        "wave": "FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01",
        "ts": TS,
        "legacy_removed": True,
        "deletion_method": deletion_method,
        "backup": bak,
        "post": post,
        "regression": reg,
        "egress": eg,
        "mutations": {
            "veesp": 0,
            "eqvps": 0,
            "legacy_deletion": 1,
            "remaining_client_mutation": 0,
            "architecture": 0,
            "firewall": 0,
            "ssh": 0,
            "reboot": 0,
            "secret_disclosure": 0,
            "foreign_wip": 0,
            "commit_push": 0,
        },
    }
    write("Z-summary.json", json.dumps(summary, indent=2) + "\n")
    write("C1-deletion-method.json", json.dumps({"method": deletion_method, "legacy": LEGACY}, indent=2) + "\n")
    c.close()
    print("DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
