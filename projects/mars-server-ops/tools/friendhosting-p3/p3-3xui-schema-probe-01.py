#!/usr/bin/env python3
"""Sync FriendHosting P3 device clients into 3X-UI 3.7 clients/client_inbounds tables."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
EV = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01")
LOCAL_CLIENTS = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients")


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

    # Probe schemas first
    code, out, err = run(
        r"""
python3 - <<'P'
import sqlite3
con=sqlite3.connect('/etc/x-ui/x-ui.db')
for table in ['clients','client_inbounds','client_traffics','inbounds','client_external_links']:
    cols=con.execute(f'pragma table_info({table})').fetchall()
    print('TABLE', table)
    for col in cols:
        print('  COL', col[1], col[2], 'notnull', col[3], 'pk', col[5], 'default', col[4])
    n=con.execute(f'select count(*) from {table}').fetchone()[0]
    print('  COUNT', n)
print('---CLIENTS_ROWS---')
cols=[r[1] for r in con.execute('pragma table_info(clients)')]
print('COLS', cols)
for row in con.execute('select * from clients'):
    d=dict(zip(cols,row))
    for k in list(d):
        if k.lower() in ('uuid','id','password','subid') or 'uuid' in k.lower():
            if isinstance(d[k], str) and len(d[k])>=32:
                d[k]='<SECRET>'
    print('ROW', d)
print('---CLIENT_INBOUNDS---')
cols2=[r[1] for r in con.execute('pragma table_info(client_inbounds)')]
print('COLS', cols2)
for row in con.execute('select * from client_inbounds'):
    print('ROW', dict(zip(cols2,row)))
P
"""
    )
    (EV / "D5-schema-probe.txt").write_text(redact(out + "\n" + err), encoding="utf-8")
    print(redact(out + "\n" + err)[:5000])
    c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
