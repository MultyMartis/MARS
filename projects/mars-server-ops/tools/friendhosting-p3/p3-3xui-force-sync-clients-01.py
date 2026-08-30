#!/usr/bin/env python3
"""Force-sync FriendHosting :8443 clients from x-ui.db into live Xray config."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
EV = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01")


def redact(t: str) -> str:
    t = re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        t,
    )
    return t


def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')


def main() -> int:
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

    def run(cmd, timeout=180):
        _, o, e = c.exec_command(cmd, timeout=timeout)
        out = o.read().decode("utf-8", "replace")
        err = e.read().decode("utf-8", "replace")
        code = o.channel.recv_exit_status()
        return code, out, err

    code, out, err = run(
        r"""
set -e
TS=$(date -u +%Y%m%dT%H%M%SZ)
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p3ux-forcesync-$TS
cp -a /usr/local/x-ui/bin/config.json /root/mars-backups/xray-config.p3ux-forcesync-$TS.json

python3 - <<'P'
import json, sqlite3, subprocess, time, shutil
from pathlib import Path

DB='/etc/x-ui/x-ui.db'
CFG='/usr/local/x-ui/bin/config.json'

con=sqlite3.connect(DB)
con.row_factory=sqlite3.Row
print('TABLES', [r[0] for r in con.execute("select name from sqlite_master where type='table'")])
# client_traffics
try:
    rows=con.execute('select email, inbound_id, enable from client_traffics').fetchall()
    print('TRAFFICS_N', len(rows))
    for r in rows:
        print('TRAFFIC', r['email'], 'inbound', r['inbound_id'], 'enable', r['enable'])
except Exception as e:
    print('TRAFFIC_ERR', e)

row=con.execute('select id, remark, port, protocol, settings, stream_settings, sniffing, listen, tag, enable from inbounds where port=8443').fetchone()
print('INBOUND_ID', row['id'], 'ENABLE', row['enable'], 'TAG', row['tag'])
settings=json.loads(row['settings'] or '{}')
stream=json.loads(row['stream_settings'] or '{}')
clients=settings.get('clients') or []
print('DB_CLIENTS', len(clients))

# Ensure client_traffics rows exist for each client (3X-UI often requires this)
inbound_id=row['id']
existing={r[0] for r in con.execute('select email from client_traffics where inbound_id=?', (inbound_id,))}
print('TRAFFIC_EXISTING', sorted(existing))
added=[]
for cl in clients:
    email=cl.get('email')
    if not email:
        continue
    if email not in existing:
        # insert minimal traffic row
        con.execute(
            '''insert into client_traffics
               (inbound_id, enable, email, up, down, expiry_time, total, reset, last_online)
               values (?, ?, ?, 0, 0, 0, 0, 0, 0)''',
            (inbound_id, 1 if cl.get('enable', True) else 0, email)
        )
        added.append(email)
    else:
        # keep enable in sync
        con.execute(
            'update client_traffics set enable=? where inbound_id=? and email=?',
            (1 if cl.get('enable', True) else 0, inbound_id, email)
        )
con.commit()
print('TRAFFIC_ADDED', added)

# Also rename traffic emails if old long names remain
rename_pairs=[
 ('WSP-ONE-FRIENDHOSTING-DE-RAW-8443','WSP-ONE'),
 ('MCA-PHONE-FRIENDHOSTING-DE-RAW-8443','MCA-PHONE'),
 ('Unit-01-FRIENDHOSTING-DE-RAW-8443','Unit-01'),
 ('Unit-02-FRIENDHOSTING-DE-RAW-8443','Unit-02'),
 ('Unit-03-FRIENDHOSTING-DE-RAW-8443','Unit-03'),
 ('Unit-MichaelPhone-FRIENDHOSTING-DE-RAW-8443','Unit-MichaelPhone'),
]
for old,new in rename_pairs:
    cur=con.execute('select count(*) from client_traffics where email=?', (old,)).fetchone()[0]
    if cur:
        # if new already exists, delete old; else rename
        exists_new=con.execute('select count(*) from client_traffics where email=?', (new,)).fetchone()[0]
        if exists_new:
            con.execute('delete from client_traffics where email=?', (old,))
            print('TRAFFIC_DEL_OLD', old)
        else:
            con.execute('update client_traffics set email=? where email=?', (new, old))
            print('TRAFFIC_RENAME', old, '->', new)
con.commit()

# Ensure no server-side fingerprint
tls=stream.get('tlsSettings') or {}
if 'fingerprint' in tls and tls.get('fingerprint'):
    print('CLEAR_FP', tls.get('fingerprint'))
    tls['fingerprint']=''
    stream['tlsSettings']=tls
    con.execute('update inbounds set stream_settings=? where id=?', (json.dumps(stream, ensure_ascii=False), inbound_id))
    con.commit()

# Method A: restart x-ui and hope generator picks up traffics
subprocess.check_call(['systemctl','restart','x-ui'])
time.sleep(6)
j=json.load(open(CFG))
n=0
emails=[]
for ib in j.get('inbounds') or []:
    if ib.get('port')==8443:
        cls=(ib.get('settings') or {}).get('clients') or []
        n=len(cls); emails=[c.get('email') for c in cls]
print('AFTER_RESTART_XRAY_N', n, emails)

if n < 7:
    # Method B: manually patch config.json clients from DB, then ask x-ui to restart xray
    print('MANUAL_PATCH')
    # Build xray-compatible client objects (id, email, flow)
    xclients=[]
    for cl in clients:
        xc={'id': cl['id'], 'email': cl.get('email')}
        flow=cl.get('flow') or ''
        if flow:
            xc['flow']=flow
        xclients.append(xc)
    changed=False
    for ib in j.get('inbounds') or []:
        if ib.get('port')==8443:
            ib.setdefault('settings', {})['clients']=xclients
            # keep decryption/fallbacks
            changed=True
    assert changed
    Path(CFG).write_text(json.dumps(j, indent=2, ensure_ascii=False)+'\n')
    # restart xray via x-ui
    subprocess.check_call(['systemctl','restart','x-ui'])
    time.sleep(6)
    j2=json.load(open(CFG))
    for ib in j2.get('inbounds') or []:
        if ib.get('port')==8443:
            cls=(ib.get('settings') or {}).get('clients') or []
            print('AFTER_PATCH_XRAY_N', len(cls))
            for c in cls:
                print('XRAY', c.get('email'))
else:
    for e in emails:
        print('XRAY', e)

# verify traffics final
rows=con.execute('select email, enable from client_traffics where inbound_id=? order by email', (inbound_id,)).fetchall()
print('TRAFFIC_FINAL_N', len(rows))
for r in rows:
    print('TRAFFIC', r['email'], 'enable', r['enable'])
con.close()

# health
import socket
print('XUI', subprocess.check_output(['systemctl','is-active','x-ui'], text=True).strip())
print('NGINX', subprocess.check_output(['systemctl','is-active','nginx'], text=True).strip())
P
ss -lntp | egrep ':(8443|20901|443|3333)\b' || true
# TLS probe
python3 - <<'P'
import socket,ssl
ctx=ssl.create_default_context()
for port in (443,8443):
  try:
    with socket.create_connection(('127.0.0.1',port),timeout=5) as s:
      with ctx.wrap_socket(s, server_hostname='metacode-cloud.com') as ss:
        print('TLS_LOCAL', port, 'OK', ss.version())
  except Exception as e:
    print('TLS_LOCAL', port, 'FAIL', type(e).__name__)
P
"""
    )
    (EV / "D4-force-sync.txt").write_text(redact(out + "\n" + err), encoding="utf-8")
    print(redact(out + "\n" + err))
    c.close()
    return 0 if code == 0 else code


if __name__ == "__main__":
    raise SystemExit(main())
