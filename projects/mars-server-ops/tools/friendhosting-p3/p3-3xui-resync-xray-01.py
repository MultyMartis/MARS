#!/usr/bin/env python3
"""Diagnose/fix FriendHosting xray sync after P3 UX mutation."""
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
    t = re.sub(r"vless://[^\s\"']+", "vless://<REDACTED>", t, flags=re.I)
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
python3 - <<'P'
import json, sqlite3
con = sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory = sqlite3.Row
row = con.execute('select id,settings,stream_settings from inbounds where port=8443').fetchone()
settings = json.loads(row['settings'] or '{}')
stream = json.loads(row['stream_settings'] or '{}')
clients = settings.get('clients') or []
print('DB_CLIENTS', len(clients))
for cl in clients:
    print('DB', cl.get('email'), 'keys=', sorted(cl.keys()), 'enable=', cl.get('enable'), 'flow=', repr(cl.get('flow') or ''))
print('STREAM_KEYS', sorted(stream.keys()))
tls = stream.get('tlsSettings') or {}
print('TLS_KEYS', sorted(tls.keys()))
print('TLS_FP', tls.get('fingerprint'))
print('TLS_ALPN', tls.get('alpn'))
print('TLS_SNI', tls.get('serverName'))
j = json.load(open('/usr/local/x-ui/bin/config.json'))
ibs = [ib for ib in j.get('inbounds') or [] if ib.get('port') == 8443]
print('XRAY_IB_N', len(ibs))
if ibs:
    xcl = (ibs[0].get('settings') or {}).get('clients') or []
    print('XRAY_CLIENTS', len(xcl))
    for cl in xcl:
        print('XRAY', cl.get('email'))
    xs = ibs[0].get('streamSettings') or {}
    print('XRAY_NET', xs.get('network'), 'SEC', xs.get('security'))
    xt = xs.get('tlsSettings') or {}
    print('XRAY_TLS_KEYS', sorted(xt.keys()))
    print('XRAY_FP', xt.get('fingerprint'))
P
"""
    )
    (EV / "D1-xray-sync-diagnose.txt").write_text(redact(out + "\n" + err), encoding="utf-8")
    print("--- DIAG ---")
    print(redact(out + "\n" + err)[:3500])

    # Try forcing x-ui to rebuild: x-ui setting -restart or binary restart + touch
    # Also check if fingerprint in inbound tlsSettings causes xray reject of full config
    # Fallback: remove fingerprint from SERVER stream (keep only for share via alternate),
    # and force restart; fingerprint is client-side for uTLS.

    code2, out2, err2 = run(
        r"""
set -e
# Snapshot current db
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p3ux-resync-$(date -u +%Y%m%dT%H%M%SZ)

python3 - <<'P'
import json, sqlite3, subprocess, time, os

con = sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory = sqlite3.Row
row = con.execute('select id, settings, stream_settings from inbounds where port=8443').fetchone()
settings = json.loads(row['settings'] or '{}')
stream = json.loads(row['stream_settings'] or '{}')
tls = stream.setdefault('tlsSettings', {})

# CRITICAL: inbound server tlsSettings.fingerprint is NOT a valid Xray inbound server field
# in the same sense as client outbound; 3X-UI may use it for SHARE link generation only.
# If present and it causes incomplete xray sync, remove from live stream and store share fp elsewhere.
# Keep alpn + serverName (legitimate inbound TLS).
fp = tls.pop('fingerprint', None)
print('REMOVED_SERVER_FP', fp)

# Ensure clients intact
clients = settings.get('clients') or []
print('DB_CLIENTS_BEFORE_WRITE', len(clients))
assert len(clients) == 7, clients

con.execute(
    'update inbounds set settings=?, stream_settings=? where id=?',
    (json.dumps(settings, ensure_ascii=False), json.dumps(stream, ensure_ascii=False), row['id']),
)
con.commit()
con.close()

# Restart x-ui to regenerate config
subprocess.check_call(['systemctl', 'restart', 'x-ui'])
time.sleep(5)
print('XUI', subprocess.check_output(['systemctl','is-active','x-ui'], text=True).strip())

j = json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
    if ib.get('port') == 8443:
        cls = (ib.get('settings') or {}).get('clients') or []
        print('XRAY_CLIENTS', len(cls))
        for cl in cls:
            print('XRAY', cl.get('email'))
        xs = ib.get('streamSettings') or {}
        print('XRAY_NET', xs.get('network'), 'SEC', xs.get('security'))
        xt = xs.get('tlsSettings') or {}
        print('XRAY_SNI', xt.get('serverName'), 'ALPN', xt.get('alpn'), 'FP', xt.get('fingerprint'))
P

# If still 1 client, try x-ui internal restart API via binary
python3 - <<'P'
import json
j=json.load(open('/usr/local/x-ui/bin/config.json'))
n=0
for ib in j.get('inbounds') or []:
  if ib.get('port')==8443:
    n=len((ib.get('settings') or {}).get('clients') or [])
print('FINAL_XRAY_N', n)
P
ss -lntp | egrep ':(8443|20901|443|3333)\b' || true
journalctl -u x-ui -n 30 --no-pager | sed -E 's/[0-9a-fA-F-]{36}/<UUID>/g' | tail -n 30
"""
    )
    (EV / "D2-xray-resync.txt").write_text(redact(out2 + "\n" + err2), encoding="utf-8")
    print("--- RESYNC ---")
    print(redact(out2 + "\n" + err2)[:4000])

    # If still broken, investigate enable field types / client schema
    code3, out3, err3 = run(
        r"""
python3 - <<'P'
import json, sqlite3
con=sqlite3.connect('/etc/x-ui/x-ui.db')
row=con.execute('select settings from inbounds where port=8443').fetchone()[0]
settings=json.loads(row)
# dump raw settings keys top-level
print('SETTINGS_TOP', sorted(settings.keys()))
print('CLIENTS_N', len(settings.get('clients') or []))
# show one new client full structure with uuid redacted
for cl in settings.get('clients') or []:
  if cl.get('email')=='WSP-ONE':
    d=dict(cl)
    if 'id' in d: d['id']='<UUID>'
    print('WSP_CLIENT', json.dumps(d, ensure_ascii=False))
  if cl.get('email') and 'MCA-ONE' in cl.get('email'):
    d=dict(cl)
    if 'id' in d: d['id']='<UUID>'
    print('LEGACY_CLIENT', json.dumps(d, ensure_ascii=False))
# compare with xray
j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
  if ib.get('port')==8443:
    print('XRAY_SETTINGS_TOP', sorted((ib.get('settings') or {}).keys()))
    print('XRAY_N', len((ib.get('settings') or {}).get('clients') or []))
P
"""
    )
    (EV / "D3-client-schema.txt").write_text(redact(out3 + "\n" + err3), encoding="utf-8")
    print("--- SCHEMA ---")
    print(redact(out3 + "\n" + err3)[:3000])
    c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
