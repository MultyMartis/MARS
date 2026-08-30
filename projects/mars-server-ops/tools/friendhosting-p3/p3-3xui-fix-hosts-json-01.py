#!/usr/bin/env python3
"""Fix invalid hosts JSON fields that crash x-ui 3.7; restore service + :8443."""
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

    def run(cmd, timeout=180):
        _, o, e = c.exec_command(cmd, timeout=timeout)
        out = o.read().decode("utf-8", "replace")
        err = e.read().decode("utf-8", "replace")
        return o.channel.recv_exit_status(), out, err

    code, out, err = run(
        r"""
set -e
TS=$(date -u +%Y%m%dT%H%M%SZ)
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p3ux-hosts-fix-$TS

python3 - <<'P'
import json, sqlite3, subprocess, time
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
cols=[r[1] for r in con.execute('pragma table_info(hosts)')]
print('COLS', cols)
for row in con.execute('select * from hosts'):
    d=dict(zip(cols,row))
    print('BEFORE', {k:d[k] for k in d})

# Fix JSON-ish fields: alpn must be JSON array string; empty objects for params
# fingerprint remains plain string 'chrome' (panel field)
for row in con.execute('select id, alpn, mux_params, sockopt_params, tags, exclude_from_sub_types, node_guids, ech_config_list from hosts'):
    hid=row['id']
    alpn=row['alpn']
    # if alpn is not valid JSON, convert
    fixed_alpn=alpn
    try:
        parsed=json.loads(alpn) if alpn not in (None,'') else []
        if isinstance(parsed, str):
            parsed=[parsed]
        if not isinstance(parsed, list):
            parsed=['http/1.1']
        fixed_alpn=json.dumps(parsed)
    except Exception:
        # plain http/1.1 -> ["http/1.1"]
        if alpn and alpn.startswith('http'):
            fixed_alpn=json.dumps([alpn])
        else:
            fixed_alpn=json.dumps(['http/1.1'])

    def as_json_or_empty(v, default):
        if v in (None,''):
            return default
        try:
            json.loads(v)
            return v
        except Exception:
            return default

    mux=as_json_or_empty(row['mux_params'], '')
    sock=as_json_or_empty(row['sockopt_params'], '')
    tags=as_json_or_empty(row['tags'], '')
    excl=as_json_or_empty(row['exclude_from_sub_types'], '')
    nodes=as_json_or_empty(row['node_guids'], '')
    ech=as_json_or_empty(row['ech_config_list'], '')

    con.execute(
        '''update hosts set alpn=?, mux_params=?, sockopt_params=?, tags=?,
           exclude_from_sub_types=?, node_guids=?, ech_config_list=?,
           fingerprint=?, address=?, port=8443, security=?, sni=?,
           is_disabled=0, allow_insecure=0 where id=?''',
        (fixed_alpn, mux, sock, tags, excl, nodes, ech,
         'chrome', 'metacode-cloud.com', 'tls', 'metacode-cloud.com', hid)
    )
    print('FIXED_ALPN', fixed_alpn)

con.commit()
for row in con.execute('select id, address, port, security, sni, alpn, fingerprint, mux_params, sockopt_params, tags from hosts'):
    print('AFTER', dict(row))
con.close()

subprocess.check_call(['systemctl','reset-failed','x-ui'])
subprocess.check_call(['systemctl','restart','x-ui'])
time.sleep(6)
st=subprocess.run(['systemctl','is-active','x-ui'], capture_output=True, text=True)
print('XUI', st.stdout.strip(), 'code', st.returncode)
if st.returncode != 0:
    print(subprocess.check_output(['journalctl','-u','x-ui','-n','20','--no-pager'], text=True))
    raise SystemExit(2)

# confirm listeners
print(subprocess.check_output("ss -lntp | egrep ':(8443|20901|443|3333|2096)\\b' || true", shell=True, text=True))
j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
  if ib.get('port')==8443:
    print('XRAY_N', len((ib.get('settings') or {}).get('clients') or []))
    for cl in (ib.get('settings') or {}).get('clients') or []:
      print('XRAY', cl.get('email'))
P
"""
    )
    text = redact(out + "\n" + err)
    (EV / "D12-hosts-json-fix.txt").write_text(text, encoding="utf-8")
    # avoid console unicode issues
    Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\p3-3xui-operator-ux-compare\D12-console.txt").write_text(
        text, encoding="utf-8"
    )
    print("EXIT", code)
    print("XUI_LINE", [ln for ln in text.splitlines() if ln.startswith("XUI ")][-1:])
    print("XRAY_N_LINE", [ln for ln in text.splitlines() if ln.startswith("XRAY_N")][-1:])

    probes = {}
    for p in (3333, 443, 8443, 2096, 20901):
        try:
            s = socket.create_connection((HOST, p), timeout=6)
            s.close()
            probes[str(p)] = "OPEN"
        except Exception as e:
            probes[str(p)] = f"FAIL:{type(e).__name__}"
    (EV / "D12-probes.json").write_text(json.dumps(probes, indent=2), encoding="utf-8")
    print("PROBES", json.dumps(probes))
    c.close()
    return 0 if code == 0 else code


if __name__ == "__main__":
    raise SystemExit(main())
