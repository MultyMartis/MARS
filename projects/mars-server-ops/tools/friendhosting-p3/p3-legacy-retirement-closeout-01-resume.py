#!/usr/bin/env python3
"""P3.1 resume: finalize backup twin (lean+full), delete legacy, verify, mark local."""
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
LEGACY = "MCA-ONE-FRIENDHOSTING-DE-RAW-8443"
KEEP = [
    "WSP-ONE",
    "MCA-PHONE",
    "Unit-01",
    "Unit-02",
    "Unit-03",
    "Unit-MichaelPhone",
]
EXPECTED_POST = sorted(KEEP)
BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV = BASE / "ssh" / "marsops_ed25519"
CLIENTS_ROOT = BASE / "clients"
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01"
)
TS = "20260830T120733Z"  # pre-delete full remote already created
BAK_NAME = f"friendhosting-p3-pre-legacy-retirement-{TS}"
REMOTE_FULL = f"/root/mars-backups/{BAK_NAME}.tgz"
REMOTE_SHA = "4952b6368ad884be1a6737506f7f81c8464aaa28cb2e44807c038049918abac8"
LEAN_TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
LEAN_NAME = f"friendhosting-p3-pre-legacy-retirement-ESSENTIAL-{LEAN_TS}"
REMOTE_LEAN = f"/root/mars-backups/{LEAN_NAME}.tgz"
LOCAL_LEAN = BASE / "backups" / f"{LEAN_NAME}.tgz"
LOCAL_FULL = BASE / "backups" / f"{BAK_NAME}.tgz"


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


def run(c, cmd, timeout=180):
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


def sftp_get(c, remote: str, local: Path, timeout_s: int = 600) -> None:
    """Chunked SFTP get with progress."""
    sftp = c.open_sftp()
    sftp.get_channel().settimeout(timeout_s)
    st = sftp.stat(remote)
    total = st.st_size
    local.parent.mkdir(parents=True, exist_ok=True)
    # remove partial
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
            if got % (5 * 1024 * 1024) < 256 * 1024:
                print(f"  download {got}/{total}", flush=True)
    sftp.close()
    if local.stat().st_size != total:
        raise SystemExit(f"SIZE_MISMATCH local={local.stat().st_size} remote={total}")


def main() -> int:
    print("RESUME P3.1", flush=True)
    c = connect()

    # Verify full remote still intact
    code, out, err = run(
        c,
        f"test -f {REMOTE_FULL} && sha256sum {REMOTE_FULL} && python3 - <<'P'\n"
        f"import tarfile\n"
        f"t=tarfile.open('{REMOTE_FULL}','r:gz')\n"
        f"names=t.getnames()\n"
        f"assert any('x-ui.db' in n for n in names)\n"
        f"assert any('clients-safe.json' in n for n in names)\n"
        f"print('FULL_TAR_OK', len(names))\n"
        f"P\n",
        timeout=120,
    )
    write("B1b-full-remote-verify.txt", redact(out + "\n" + err))
    if code != 0 or REMOTE_SHA not in out:
        raise SystemExit(f"FULL remote verify fail: {out} {err}")
    print("FULL remote OK", flush=True)

    # Build lean essential twin (DB + xray config + safe clients + service snaps)
    code, out, err = run(
        c,
        f"""
set -euo pipefail
D=/root/mars-backups/{LEAN_NAME}
rm -rf "$D"
mkdir -p "$D/meta" "$D/etc"
cp -a /etc/x-ui "$D/etc/x-ui"
cp -a /etc/x-ui/x-ui.db "$D/meta/x-ui.db"
cp -a /usr/local/x-ui/bin/config.json "$D/meta/xray-config.json"
python3 - <<PY
import json, sqlite3
from pathlib import Path
D=Path("/root/mars-backups/{LEAN_NAME}")
con=sqlite3.connect("/etc/x-ui/x-ui.db")
con.row_factory=sqlite3.Row
row=con.execute("select id,remark,port,protocol,settings from inbounds where port=8443").fetchone()
settings=json.loads(row["settings"] or "{{}}")
clients=[{{"email":c.get("email"),"enable":c.get("enable",True),"flow":c.get("flow") or "","has_id":bool(c.get("id"))}} for c in (settings.get("clients") or [])]
assert len(clients)==7
assert sum(1 for c in clients if c["email"]=="{LEGACY}")==1
safe={{"inbound":{{"id":row["id"],"remark":row["remark"],"port":row["port"],"protocol":row["protocol"]}},"client_count":len(clients),"clients":clients}}
(D/"meta/clients-safe.json").write_text(json.dumps(safe, indent=2)+"\\n")
print("LEAN_SAFE_N", len(clients))
PY
systemctl is-active x-ui nginx ssh > "/root/mars-backups/{LEAN_NAME}/meta/services.txt" || true
ss -lntp > "/root/mars-backups/{LEAN_NAME}/meta/ss-lntp.txt" || true
ufw status numbered > "/root/mars-backups/{LEAN_NAME}/meta/ufw.txt" || true
tar -C /root/mars-backups -czf {REMOTE_LEAN} {LEAN_NAME}
sha256sum {REMOTE_LEAN} | tee {REMOTE_LEAN}.sha256
stat -c '%s' {REMOTE_LEAN}
""",
        timeout=180,
    )
    write("B1c-lean-backup-remote.txt", redact(out + "\n" + err))
    if code != 0 or "LEAN_SAFE_N 7" not in out:
        raise SystemExit(f"LEAN backup fail: {out}\n{err}")
    lean_sha = re.search(r"([0-9a-f]{64})\s+" + re.escape(REMOTE_LEAN), out).group(1)
    print("LEAN remote OK", lean_sha, flush=True)

    print("Downloading LEAN twin...", flush=True)
    sftp_get(c, REMOTE_LEAN, LOCAL_LEAN, timeout_s=300)
    local_lean_sha = sha256_file(LOCAL_LEAN)
    lean_match = local_lean_sha == lean_sha
    print("LEAN match", lean_match, LOCAL_LEAN.stat().st_size, flush=True)

    # Validate lean contents
    with tarfile.open(LOCAL_LEAN, "r:gz") as t:
        names = t.getnames()
        assert any(n.endswith("x-ui.db") for n in names)
        safe_m = next(n for n in names if n.endswith("clients-safe.json"))
        safe = json.loads(t.extractfile(safe_m).read().decode())
    assert safe["client_count"] == 7
    assert sorted(c["email"] for c in safe["clients"]) == sorted(KEEP + [LEGACY])

    # Full remote archive verified by SHA on server. Local primary twin is ESSENTIAL
    # (avoids multi-hour hairpin SFTP of ~80MB binaries).
    full_match = False
    full_local_sha = None
    if LOCAL_FULL.exists() and LOCAL_FULL.stat().st_size > 80_000_000:
        full_local_sha = sha256_file(LOCAL_FULL)
        full_match = full_local_sha == REMOTE_SHA
    write(
        "B1d-full-download-note.txt",
        "FULL remote archive verified on server (SHA match remote file).\n"
        f"Remote full: {REMOTE_FULL}\nSHA: {REMOTE_SHA}\n"
        "Local primary twin: ESSENTIAL archive (x-ui.db + xray config + clients-safe + snaps).\n"
        f"Partial local full present={LOCAL_FULL.exists()} "
        f"size={LOCAL_FULL.stat().st_size if LOCAL_FULL.exists() else 0} match={full_match}\n",
    )
    print("FULL local twin deferred; remote full authoritative", flush=True)

    restore_md = f"""# Restore strategy — pre-legacy-retirement ({TS} / essential {LEAN_TS})
# inventory_ref: FRIENDHOSTING-DE
# remote_full: {REMOTE_FULL}
# sha256_full: {REMOTE_SHA}
# local_full: {LOCAL_FULL} (match={full_match})
# remote_essential: {REMOTE_LEAN}
# sha256_essential: {lean_sha}
# local_essential: {LOCAL_LEAN}
# sha_match_essential: {lean_match}

## Scope
Pre-delete seven-client checkpoint:
- Full remote archive includes /etc/x-ui + /usr/local/x-ui + meta
- Essential twin (local+remote) includes /etc/x-ui, x-ui.db, xray-config.json, clients-safe.json, service snaps

## Procedure
1. STOP mutation.
2. Prefer restore from essential or full: extract under `/root/mars-backups/`.
3. `systemctl stop x-ui`
4. Restore `/etc/x-ui` (and optional generated config) from staging after review.
5. `systemctl start x-ui`
6. Verify **7** clients including `{LEGACY}`; confirm **WSP-ONE** enabled; SSH :3333; Xray :8443; nginx :443.

## Post-restore
- seven clients restored
- WSP-ONE smoke
"""
    write("B1-RESTORE-STRATEGY.md", restore_md)
    (BASE / "backups" / f"{LEAN_NAME}-RESTORE-STRATEGY.md").write_text(
        restore_md, encoding="utf-8"
    )
    (BASE / "backups" / f"{LEAN_NAME}.tgz.sha256").write_text(
        f"{lean_sha}  {LEAN_NAME}.tgz\n", encoding="utf-8"
    )
    (BASE / "backups" / f"{BAK_NAME}.tgz.sha256").write_text(
        f"{REMOTE_SHA}  {BAK_NAME}.tgz\n", encoding="utf-8"
    )

    bak = {
        "remote_full": REMOTE_FULL,
        "sha256_full_remote": REMOTE_SHA,
        "local_full": str(LOCAL_FULL),
        "sha256_full_local": full_local_sha,
        "sha_match_full": full_match,
        "remote_essential": REMOTE_LEAN,
        "local_essential": str(LOCAL_LEAN),
        "sha256_essential": lean_sha,
        "sha_match_essential": lean_match,
        "size_essential": LOCAL_LEAN.stat().st_size,
        "restore_strategy": "CONFIRMED" if lean_match else "NOT CONFIRMED",
        "primary_local_twin": str(LOCAL_LEAN if lean_match else LOCAL_FULL),
    }
    write("B1-backup-validation.json", json.dumps(bak, indent=2) + "\n")
    if not lean_match:
        raise SystemExit("STOP — essential twin SHA mismatch")
    print("BACKUP + RESTORE STRATEGY CONFIRMED", flush=True)

    # Re-confirm still 7 before delete
    code, out, err = run(
        c,
        r"""
python3 - <<'P'
import json, sqlite3
LEGACY='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'
KEEP=['WSP-ONE','MCA-PHONE','Unit-01','Unit-02','Unit-03','Unit-MichaelPhone']
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select settings from inbounds where port=8443').fetchone()
emails=[c.get('email') for c in json.loads(row['settings']).get('clients') or []]
print('PREDEL_N', len(emails))
print('PREDEL_EMAILS', json.dumps(sorted(emails)))
print('LEGACY_N', emails.count(LEGACY))
print('TABLE_N', con.execute('select count(*) from clients').fetchone()[0])
print('TABLE_LEGACY', con.execute('select count(*) from clients where email=?', (LEGACY,)).fetchone()[0])
P
""",
    )
    write("C0-predelete-reconfirm.txt", redact(out + "\n" + err))
    if "PREDEL_N 7" not in out or "LEGACY_N 1" not in out or "TABLE_LEGACY 1" not in out:
        raise SystemExit("STOP — pre-delete reconfirm fail")

    # DELETE
    print("Deleting legacy...", flush=True)
    code, out, err = run(
        c,
        r"""
set -euo pipefail
TS=$(date -u +%Y%m%dT%H%M%SZ)
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p31-pre-delete-$TS
python3 - <<'P'
import json, sqlite3
LEGACY='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'
KEEP={'WSP-ONE','MCA-PHONE','Unit-01','Unit-02','Unit-03','Unit-MichaelPhone'}
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select id,settings from inbounds where port=8443').fetchone()
inbound_id=row['id']
settings=json.loads(row['settings'] or '{}')
clients=settings.get('clients') or []
if [c.get('email') for c in clients].count(LEGACY)!=1:
    raise SystemExit('ERR_LEGACY_SETTINGS')
new_clients=[c for c in clients if c.get('email')!=LEGACY]
got={c.get('email') for c in new_clients}
if got!=KEEP or len(new_clients)!=6:
    raise SystemExit(f'ERR_KEEP {sorted(got)}')
settings['clients']=new_clients
con.execute('update inbounds set settings=? where id=?', (json.dumps(settings, ensure_ascii=False), inbound_id))
crow=con.execute('select id from clients where email=?', (LEGACY,)).fetchall()
if len(crow)!=1:
    raise SystemExit('ERR_LEGACY_TABLE')
cid=crow[0]['id']
ci_n=con.execute('delete from client_inbounds where client_id=?', (cid,)).rowcount
print('CI_DELETED', ci_n)
con.execute('delete from clients where id=?', (cid,))
tr=con.execute('delete from client_traffics where email=?', (LEGACY,)).rowcount
print('TRAFFIC_DELETED', tr)
tables={r[0] for r in con.execute("select name from sqlite_master where type='table'")}
if 'hosts' in tables:
    cols=[r[1] for r in con.execute('pragma table_info(hosts)')]
    dh=0
    for col in ('remark','email','inboundEmail','inbound_email'):
        if col in cols:
            dh += con.execute(f'delete from hosts where {col}=?', (LEGACY,)).rowcount
    print('HOSTS_DELETED', dh)
keep=[r['email'] for r in con.execute('select email from clients order by email')]
print('POST_TABLE', json.dumps(keep))
if sorted(keep)!=sorted(KEEP):
    raise SystemExit('ERR_POST_TABLE')
for r in con.execute('select email,enable from clients'):
    if not r['enable']:
        raise SystemExit('ERR_DISABLED '+r['email'])
orph=con.execute('''select count(*) from client_inbounds ci left join clients c on c.id=ci.client_id where c.id is null''').fetchone()[0]
print('ORPHAN_CI', orph)
ids=[c.get('id') for c in new_clients]
print('UUID_UNIQUE', len(ids)==len(set(ids)) and all(ids))
con.commit()
print('DELETE_OK', LEGACY)
print('REMAINING', json.dumps(sorted(got)))
P
systemctl restart x-ui
sleep 5
systemctl is-active x-ui
""",
        timeout=120,
    )
    write("C1-delete-legacy.txt", redact(out + "\n" + err))
    if code != 0 or "DELETE_OK" not in out:
        raise SystemExit(f"DELETE FAIL: {out}\n{err}")
    print("DELETE OK", flush=True)

    # Post audit
    code, out, err = run(
        c,
        r"""
python3 - <<'P'
import json, sqlite3, pathlib
LEGACY='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'
KEEP=['MCA-PHONE','Unit-01','Unit-02','Unit-03','Unit-MichaelPhone','WSP-ONE']
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select settings,stream_settings from inbounds where port=8443').fetchone()
settings=json.loads(row['settings'] or '{}')
stream=json.loads(row['stream_settings'] or '{}')
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
ct=sorted(r['email'] for r in con.execute('select email from clients'))
print('TABLE_N', len(ct))
print('TABLE_EMAILS', json.dumps(ct))
print('LEGACY_ABSENT_TABLE', LEGACY not in ct)
print('CLIENT_INBOUNDS_N', con.execute('select count(*) from client_inbounds').fetchone()[0])
print('ORPHAN_CI', con.execute('''select count(*) from client_inbounds ci left join clients c on c.id=ci.client_id where c.id is null''').fetchone()[0])
print('TRAFFIC_LEGACY_LEFT', con.execute('select count(*) from client_traffics where email=?', (LEGACY,)).fetchone()[0])
j=json.loads(pathlib.Path('/usr/local/x-ui/bin/config.json').read_text())
for ib in j.get('inbounds') or []:
    if ib.get('port')==8443:
        xe=sorted(c.get('email') for c in (ib.get('settings') or {}).get('clients') or [])
        print('XRAY_LIVE_N', len(xe))
        print('XRAY_LIVE_EMAILS', json.dumps(xe))
        print('XRAY_LEGACY_ABSENT', LEGACY not in xe)
        print('WSP_PRESENT', 'WSP-ONE' in xe)
        print('PHONE_PRESENT', 'MCA-PHONE' in xe)
P
systemctl is-active x-ui nginx
ss -lntp | egrep ':(80|3333|443|8443|20901)\b' || true
ufw status | egrep '2096|20901|3333|443|8443|80' || true
""",
        timeout=60,
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
        },
    }
    write("D1-post-client-audit.json", json.dumps(post, indent=2) + "\n")
    if not (
        post["settings_n"] == 6
        and post["legacy_absent"]
        and post["uuid_unique"]
        and post["all_enabled"]
        and post["wsp"]
        and post["phone"]
        and post["orphan_ci"] == 0
        and post["settings_emails"] == EXPECTED_POST
        and post["xray_emails"] == EXPECTED_POST
    ):
        raise SystemExit(f"POST FAIL {post}")

    local = {
        "tcp_3333": tcp(3333),
        "tcp_443": tcp(443),
        "tcp_8443": tcp(8443),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
    }
    reg = {
        "ssh": local["tcp_3333"],
        "nginx": local["tcp_443"] and local["tls_443"].get("ok"),
        "xray": local["tcp_8443"] and local["tls_8443"].get("ok"),
        "xui": out.splitlines()[-20:] and "active" in out,
        "local": local,
    }
    # tighter
    code2, out2, _ = run(c, "systemctl is-active x-ui nginx")
    reg["xui_active"] = out2.splitlines()[0].strip() == "active"
    reg["nginx_active"] = out2.splitlines()[1].strip() == "active"
    reg["pass"] = all(
        [reg["ssh"], reg["nginx"], reg["xray"], reg["xui_active"], reg["nginx_active"]]
    )
    write("D2-regression.json", json.dumps(reg, indent=2) + "\n")
    write("D2-regression.txt", redact(out + "\n" + out2))
    if not reg["pass"]:
        raise SystemExit("REGRESSION FAIL")

    try:
        eg = urllib.request.urlopen("https://api.ipify.org", timeout=12).read().decode()
    except Exception as e:
        eg = f"ERR:{type(e).__name__}"
    write(
        "D3-egress-post.json",
        json.dumps(
            {
                "egress": eg,
                "on_fh": eg == HOST,
                "wsp_server_side": "PASS",
                "mca_phone_server_side": "PASS",
            },
            indent=2,
        )
        + "\n",
    )

    # Local legacy mark
    mca = CLIENTS_ROOT / "MCA-ONE"
    meta = {
        "device": "MCA-ONE",
        "server_email": LEGACY,
        "status": "RETIRED — SERVER IDENTITY REMOVED",
        "wave": "FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01",
        "ts": LEAN_TS,
        "policy": "preserve files temporarily; not an active profile",
        "destructive_cleanup": False,
    }
    (mca / "meta.local.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (mca / "RETIRED.txt").write_text(
        "RETIRED — SERVER IDENTITY REMOVED\n"
        f"wave=FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01\nts={LEAN_TS}\n",
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
        "retired_ts": LEAN_TS,
        "visible_in_3xui": False,
    }
    registry["ts"] = LEAN_TS
    registry["wave"] = "P3.1"
    registry["client_count_server"] = 6
    registry["canonical_identity_model"] = "six per-device identities on :8443"
    for d in registry.get("devices") or []:
        if d.get("device") in ("WSP-ONE", "MCA-PHONE"):
            d["status"] = "SERVER_IDENTITY_READY / PHYSICAL_ACCEPTANCE_KNOWN_PASS_PER_CHARTER"
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
        },
    }
    write("Z-summary.json", json.dumps(summary, indent=2) + "\n")
    c.close()
    print("DONE PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
