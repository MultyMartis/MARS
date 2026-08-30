#!/usr/bin/env python3
import json
from pathlib import Path
import paramiko

PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
try:
    k = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
except paramiko.PasswordRequiredException:
    k = paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(
    "92.42.99.126",
    port=3333,
    username="root",
    pkey=k,
    timeout=30,
    allow_agent=False,
    look_for_keys=False,
)
_, o, e = c.exec_command(
    r"""
python3 - <<'P'
import json, sqlite3
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select settings from inbounds where port=8443').fetchone()
emails=[c.get('email') for c in json.loads(row['settings']).get('clients') or []]
print('N', len(emails))
print('EMAILS', json.dumps(emails))
print('TABLE', json.dumps([r['email'] for r in con.execute('select email from clients')]))
print('LEGACY_SETTINGS', emails.count('MCA-ONE-FRIENDHOSTING-DE-RAW-8443'))
print('LEGACY_TABLE', con.execute("select count(*) from clients where email='MCA-ONE-FRIENDHOSTING-DE-RAW-8443'").fetchone()[0])
P
ls -la /root/mars-backups/friendhosting-p3-pre-legacy-retirement-ESSENTIAL-*.tgz 2>/dev/null | tail -n 5
"""
)
print(o.read().decode())
print(e.read().decode())
c.close()
