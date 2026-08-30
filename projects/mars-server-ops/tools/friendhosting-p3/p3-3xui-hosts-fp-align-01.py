#!/usr/bin/env python3
"""Align 3X-UI hosts fingerprint for share/QR export; verify UFW 2096 without mutating firewall."""
from __future__ import annotations

import json
import re
import socket
import time
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import paramiko

HOST = "92.42.99.126"
PORT = 3333
PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
EV = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01")
WSP_LOCAL = Path(
    r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\WSP-ONE\friendhosting-de-raw-8443.vless.txt"
)


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


def struct(uri: str) -> dict:
    p = urlparse(uri.strip())
    qs = {k: (v[0] if v else "") for k, v in parse_qs(p.query, keep_blank_values=True).items()}
    return {
        "host": p.hostname,
        "port": p.port,
        "encryption": qs.get("encryption", ""),
        "security": qs.get("security", ""),
        "sni": qs.get("sni", ""),
        "alpn": unquote(qs.get("alpn", "")),
        "fp": qs.get("fp", ""),
        "type": qs.get("type", ""),
        "headerType": qs.get("headerType", ""),
        "flow": qs.get("flow", ""),
        "fragment": unquote(p.fragment or ""),
    }


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
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p3ux-hosts-$TS

python3 - <<'P'
import json, sqlite3, time, subprocess, urllib.parse
from pathlib import Path

now=int(time.time()*1000)
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
inbound_id=con.execute('select id from inbounds where port=8443').fetchone()['id']
n=con.execute('select count(*) from hosts where inbound_id=?', (inbound_id,)).fetchone()[0]
print('HOSTS_BEFORE', n)

# Upsert a single share host used by 3X-UI QR/link generation
# fingerprint=chrome aligns native export with known-good MARS profile (client uTLS hint only)
if n == 0:
    con.execute(
        '''insert into hosts
           (group_id, inbound_id, sort_order, remark, server_description, is_disabled, is_hidden, tags,
            address, port, security, sni, host_header, path, alpn, fingerprint,
            override_sni_from_address, keep_sni_blank, pinned_peer_cert_sha256, verify_peer_cert_by_name,
            allow_insecure, ech_config_list, mux_params, sockopt_params, final_mask, vless_route,
            exclude_from_sub_types, mihomo_ip_version, mihomo_x25519, shuffle_host, node_guids,
            created_at, updated_at)
           values (NULL, ?, 1, 'FRIENDHOSTING-DE-RAW-8443', '', 0, 0, '',
                   'metacode-cloud.com', 8443, 'tls', 'metacode-cloud.com', '', '', 'http/1.1', 'chrome',
                   0, 0, '', 1,
                   0, '', '', '', '', '',
                   '', '', 0, 0, '',
                   ?, ?)''',
        (inbound_id, now, now)
    )
    print('HOST_INSERTED', 1)
else:
    con.execute(
        '''update hosts set address=?, port=8443, security='tls', sni='metacode-cloud.com',
           alpn='http/1.1', fingerprint='chrome', is_disabled=0, updated_at=?
           where inbound_id=?''',
        ('metacode-cloud.com', now, inbound_id)
    )
    print('HOST_UPDATED', n)

con.commit()
for r in con.execute('select id, inbound_id, address, port, security, sni, alpn, fingerprint, is_disabled from hosts'):
    print('HOST', dict(r))

# Build share URI using hosts fingerprint (how panel typically exports)
wsp=con.execute("select uuid, email, flow from clients where email='WSP-ONE'").fetchone()
host=con.execute('select * from hosts where inbound_id=? order by sort_order limit 1', (inbound_id,)).fetchone()
q={
  'encryption':'none',
  'security': host['security'] or 'tls',
  'type': 'tcp',
  'sni': host['sni'] or 'metacode-cloud.com',
  'alpn': host['alpn'] or 'http/1.1',
  'fp': host['fingerprint'] or '',
  'headerType': 'none',
}
# drop empty fp
q={k:v for k,v in q.items() if v!=''}
query=urllib.parse.urlencode(q, quote_via=urllib.parse.quote)
uri=f"vless://{wsp['uuid']}@{host['address']}:{host['port']}?{query}#{urllib.parse.quote(wsp['email'], safe='')}"
Path('/root/mars-backups/p3-ux-wsp-host-share.SECRET.txt').write_text(uri+'\n')
print('SHARE_KEYS', sorted(q.keys()))
print('SHARE_FP', q.get('fp','<empty>'))

con.close()
# restart not strictly required for hosts (share-time), but refresh panel state
subprocess.check_call(['systemctl','restart','x-ui'])
time.sleep(5)
print('XUI', subprocess.check_output(['systemctl','is-active','x-ui'], text=True).strip())
j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
  if ib.get('port')==8443:
    print('XRAY_N', len((ib.get('settings') or {}).get('clients') or []))
    xs=ib.get('streamSettings') or {}
    print('XRAY_NET', xs.get('network'), xs.get('security'))
    print('XRAY_FP', (xs.get('tlsSettings') or {}).get('fingerprint'))

# UFW detail (read-only)
print('---UFW---')
print(subprocess.check_output(['ufw','status','verbose'], text=True))
print('---IPTABLES_2096---')
print(subprocess.check_output("iptables -S | egrep '2096|20901' || true", shell=True, text=True))
P
"""
    )
    (EV / "D9-hosts-fp-align.txt").write_text(redact(out + "\n" + err), encoding="utf-8")
    print(redact(out + "\n" + err)[:4500])

    # External probes from this workstation
    probes = {}
    for p in (3333, 443, 8443, 2096, 20901):
        try:
            with socket.create_connection((HOST, p), timeout=5):
                probes[p] = "OPEN"
        except Exception as e:
            probes[p] = f"CLOSED:{type(e).__name__}"
    (EV / "D9-external-probes.json").write_text(json.dumps(probes, indent=2), encoding="utf-8")
    print("PROBES", probes)

    sftp = c.open_sftp()
    dest = Path(
        r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\p3-3xui-operator-ux-compare\wsp-host-share.SECRET.txt"
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    sftp.get("/root/mars-backups/p3-ux-wsp-host-share.SECRET.txt", str(dest))
    run("rm -f /root/mars-backups/p3-ux-wsp-host-share.SECRET.txt")
    sftp.close()

    mars = struct(WSP_LOCAL.read_text(encoding="utf-8"))
    ui = struct(dest.read_text(encoding="utf-8"))
    mars_u = urlparse(WSP_LOCAL.read_text(encoding="utf-8").strip()).username
    ui_u = urlparse(dest.read_text(encoding="utf-8").strip()).username
    keys = ["host", "port", "encryption", "security", "sni", "alpn", "fp", "type", "headerType", "flow"]
    diffs = [{"field": k, "ui": ui.get(k), "mars": mars.get(k)} for k in keys if ui.get(k) != mars.get(k)]
    cmp = {
        "struct_match_full": len(diffs) == 0,
        "diffs": diffs,
        "uuid_equal": mars_u == ui_u,
        "ui_fp": ui.get("fp"),
        "mars_fp": mars.get("fp"),
        "ui_fragment": ui.get("fragment"),
    }
    (EV / "D10-host-share-compare.json").write_text(json.dumps(cmp, indent=2), encoding="utf-8")
    print("FINAL_COMPARE", json.dumps(cmp))
    c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
