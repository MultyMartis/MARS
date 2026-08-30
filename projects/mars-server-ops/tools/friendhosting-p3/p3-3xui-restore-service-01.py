#!/usr/bin/env python3
"""Emergency restore x-ui after hosts mutation; verify listeners + clients."""
from __future__ import annotations

import json
import re
import socket
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
EV = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01")


def redact(t: str) -> str:
    return re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        t,
    )


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

    def run(cmd, timeout=120):
        _, o, e = c.exec_command(cmd, timeout=timeout)
        out = o.read().decode("utf-8", "replace")
        err = e.read().decode("utf-8", "replace")
        code = o.channel.recv_exit_status()
        return code, out, err

    code, out, err = run(
        r"""
set +e
echo STATE_BEFORE
systemctl is-active x-ui nginx
systemctl status x-ui --no-pager -l | head -n 40
journalctl -u x-ui -n 50 --no-pager | sed -E 's/[0-9a-fA-F-]{36}/<UUID>/g'
echo RESTART
systemctl restart x-ui
sleep 5
systemctl is-active x-ui
systemctl is-active nginx
ss -lntp | egrep ':(8443|20901|443|3333|2096)\b' || true
python3 - <<'P'
import json, sqlite3
con=sqlite3.connect('/etc/x-ui/x-ui.db')
print('CLIENTS', con.execute('select count(*) from clients').fetchone()[0])
print('LINKS', con.execute('select count(*) from client_inbounds').fetchone()[0])
print('HOSTS', con.execute('select count(*) from hosts').fetchone()[0])
for r in con.execute('select email from clients order by id'):
    print('EMAIL', r[0])
j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
  if ib.get('port')==8443:
    cls=(ib.get('settings') or {}).get('clients') or []
    print('XRAY_N', len(cls))
    for cl in cls: print('XRAY', cl.get('email'))
    xs=ib.get('streamSettings') or {}
    print('NET', xs.get('network'), 'SEC', xs.get('security'))
    print('SNI', (xs.get('tlsSettings') or {}).get('serverName'))
P
ufw status | egrep -i '2096|20901|Status'
"""
    )
    (EV / "D11-xui-restore.txt").write_text(redact(out + "\n" + err), encoding="utf-8")
    print(redact(out + "\n" + err)[:6000])

    probes = {}
    for p in (3333, 443, 8443, 2096, 20901):
        try:
            sock = socket.create_connection((HOST, p), timeout=6)
            sock.close()
            probes[p] = "OPEN"
        except Exception as e:
            probes[p] = f"FAIL:{type(e).__name__}"
    (EV / "D11-probes.json").write_text(json.dumps(probes, indent=2), encoding="utf-8")
    print("PROBES", probes)
    c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
