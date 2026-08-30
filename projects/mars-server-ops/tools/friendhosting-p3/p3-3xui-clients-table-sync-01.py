#!/usr/bin/env python3
"""Register P3 device identities into 3X-UI 3.7 clients + client_inbounds (canonical)."""
from __future__ import annotations

import json
import re
import time
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
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p3ux-clients-table-$TS

python3 - <<'P'
import json, sqlite3, time, subprocess
from pathlib import Path

DB='/etc/x-ui/x-ui.db'
now=int(time.time()*1000)
con=sqlite3.connect(DB)
con.row_factory=sqlite3.Row

inbound=con.execute('select id, settings, stream_settings from inbounds where port=8443').fetchone()
inbound_id=inbound['id']
settings=json.loads(inbound['settings'] or '{}')
stream=json.loads(inbound['stream_settings'] or '{}')
embedded=settings.get('clients') or []
print('EMBEDDED_N', len(embedded))

# Clear accidental server fingerprint (export-only concern; keep alpn/sni)
tls=stream.get('tlsSettings') or {}
if tls.get('fingerprint'):
    print('CLEAR_SERVER_FP', tls.get('fingerprint'))
    tls['fingerprint']=''
    stream['tlsSettings']=tls
    con.execute('update inbounds set stream_settings=? where id=?', (json.dumps(stream, ensure_ascii=False), inbound_id))

existing={r['email']: r for r in con.execute('select * from clients')}
print('CLIENTS_TABLE_BEFORE', list(existing))

# Map preferred comments
comments={
  'MCA-ONE-FRIENDHOSTING-DE-RAW-8443': 'LEGACY FALLBACK — DO NOT DELETE YET',
  'WSP-ONE': 'Workstation NEW identity (P3)',
  'MCA-PHONE': 'DEVICE_TEST_PENDING',
  'Unit-01': 'DEVICE_TEST_PENDING',
  'Unit-02': 'DEVICE_TEST_PENDING',
  'Unit-03': 'DEVICE_TEST_PENDING',
  'Unit-MichaelPhone': 'DEVICE_TEST_PENDING',
}

created=[]
linked=[]
updated=[]

for cl in embedded:
    email=cl.get('email')
    uuid=cl.get('id')
    if not email or not uuid:
        raise SystemExit('bad_client')
    flow=cl.get('flow') or ''
    enable=1 if cl.get('enable', True) else 0
    sub_id=cl.get('subId') or ''
    comment=comments.get(email, cl.get('comment') or '')
    limit_ip=int(cl.get('limitIp') or 0)
    total_gb=int(cl.get('totalGB') or 0)
    expiry=int(cl.get('expiryTime') or 0)

    if email in existing:
        cid=existing[email]['id']
        # update uuid/enable/comment/flow if needed (do not rotate uuid unless mismatch with embedded)
        con.execute(
            '''update clients set uuid=?, flow=?, enable=?, comment=?, sub_id=COALESCE(NULLIF(sub_id,''), ?),
               limit_ip=?, total_gb=?, expiry_time=?, updated_at=? where id=?''',
            (uuid, flow, enable, comment, sub_id, limit_ip, total_gb, expiry, now, cid)
        )
        updated.append(email)
    else:
        cur=con.execute(
            '''insert into clients
               (email, sub_id, uuid, password, auth, flow, security, reverse,
                wg_private_key, wg_public_key, wg_allowed_ips, wg_pre_shared_key, wg_keep_alive, wg_forwarded_ports,
                secret, ad_tag, limit_ip, limit_hwid, total_gb, expiry_time, enable, tg_id, group_name, comment,
                reset, reset_day, reset_max, traffic_reset, traffic_reset_day, created_at, updated_at, sync_orphaned_at)
               values (?,?,?, '', '', ?, '', '',
                       '', '', '', '', 0, '',
                       '', '', ?, 0, ?, ?, ?, NULL, '', ?,
                       0, 0, 0, 'never', 1, ?, ?, 0)''',
            (email, sub_id, uuid, flow, limit_ip, total_gb, expiry, enable, comment, now, now)
        )
        cid=cur.lastrowid
        created.append(email)

    # link to inbound
    link=con.execute(
        'select 1 from client_inbounds where client_id=? and inbound_id=?',
        (cid, inbound_id)
    ).fetchone()
    if not link:
        con.execute(
            'insert into client_inbounds (client_id, inbound_id, flow_override, created_at) values (?,?,NULL,?)',
            (cid, inbound_id, now)
        )
        linked.append(email)

    # ensure traffic row email matches
    tr=con.execute(
        'select id from client_traffics where inbound_id=? and email=?',
        (inbound_id, email)
    ).fetchone()
    if not tr:
        con.execute(
            '''insert into client_traffics
               (inbound_id, enable, email, up, down, expiry_time, total, reset, reset_day, reset_max, reset_count, last_online, last_sub_fetch)
               values (?,?,?,0,0,?,?,0,0,0,0,0,0)''',
            (inbound_id, enable, email, expiry, total_gb)
        )
    else:
        con.execute(
            'update client_traffics set enable=?, expiry_time=?, total=? where id=?',
            (enable, expiry, total_gb, tr['id'])
        )

con.commit()

# Verify counts
n_clients=con.execute('select count(*) from clients').fetchone()[0]
n_links=con.execute('select count(*) from client_inbounds where inbound_id=?', (inbound_id,)).fetchone()[0]
n_traffic=con.execute('select count(*) from client_traffics where inbound_id=?', (inbound_id,)).fetchone()[0]
print('CREATED', created)
print('UPDATED', updated)
print('LINKED', linked)
print('N_CLIENTS', n_clients)
print('N_LINKS', n_links)
print('N_TRAFFIC', n_traffic)
for r in con.execute('select id,email,enable,comment from clients order by id'):
    print('CLIENT', r['id'], r['email'], 'enable='+str(r['enable']), 'comment='+(r['comment'] or ''))
for r in con.execute('select client_id, inbound_id from client_inbounds'):
    print('LINK', r['client_id'], '->', r['inbound_id'])

con.close()

subprocess.check_call(['systemctl','restart','x-ui'])
time.sleep(6)
print('XUI', subprocess.check_output(['systemctl','is-active','x-ui'], text=True).strip())

j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
    if ib.get('port')==8443:
        cls=(ib.get('settings') or {}).get('clients') or []
        print('XRAY_CLIENTS', len(cls))
        for cl in cls:
            print('XRAY', cl.get('email'), 'flow='+repr(cl.get('flow') or ''))
        xs=ib.get('streamSettings') or {}
        print('XRAY_NET', xs.get('network'), 'SEC', xs.get('security'))
        xt=xs.get('tlsSettings') or {}
        print('XRAY_SNI', xt.get('serverName'), 'ALPN', xt.get('alpn'), 'FP', xt.get('fingerprint'))

# hosts / share strategy
con=sqlite3.connect(DB)
print('SHARE_ADDR_STRATEGY', con.execute('select share_addr_strategy, share_addr from inbounds where id=?', (inbound_id,)).fetchone())
try:
    cols=[r[1] for r in con.execute('pragma table_info(hosts)')]
    print('HOSTS_COLS', cols)
    for row in con.execute('select * from hosts'):
        d=dict(zip(cols,row))
        print('HOST', {k:d[k] for k in d if 'pass' not in k.lower() and 'key' not in k.lower()})
except Exception as e:
    print('HOSTS_ERR', e)
con.close()
P

ss -lntp | egrep ':(8443|20901|443|3333|2096)\b' || true
ufw status | egrep -i '2096|20901|Status|DENY' || true
python3 - <<'P'
import socket,ssl
ctx=ssl.create_default_context()
for port in (443,8443):
  try:
    with socket.create_connection(('92.42.99.126',port),timeout=8) as s:
      with ctx.wrap_socket(s, server_hostname='metacode-cloud.com') as ss:
        print('TLS_EXT', port, 'OK')
  except Exception as e:
    print('TLS_EXT', port, 'FAIL', type(e).__name__)
for port in (2096,20901):
  try:
    with socket.create_connection(('92.42.99.126',port),timeout=5) as s:
      print('PUBLIC', port, 'OPEN')
  except Exception as e:
    print('PUBLIC', port, 'BLOCKED_OR_REFUSED', type(e).__name__)
P
"""
    )
    (EV / "D6-clients-table-sync.txt").write_text(redact(out + "\n" + err), encoding="utf-8")
    print(redact(out + "\n" + err))
    if code != 0:
        return code

    # Reconstruct WSP share URI structure from post-sync state vs local mars profile
    code2, out2, err2 = run(
        r"""
python3 - <<'P'
import json, sqlite3, urllib.parse
from pathlib import Path
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute('select * from inbounds where port=8443').fetchone()
stream=json.loads(row['stream_settings'] or '{}')
tls=stream.get('tlsSettings') or {}
tcp=stream.get('tcpSettings') or {}
network=stream.get('network') or 'tcp'
security=stream.get('security') or 'tls'
sni=tls.get('serverName') or ''
alpn_list=tls.get('alpn') or []
alpn=','.join(alpn_list) if isinstance(alpn_list,list) else str(alpn_list)
fp=tls.get('fingerprint') or ''
header=((tcp.get('header') or {}).get('type')) if isinstance(tcp,dict) else 'none'
# 3X-UI share may also use hosts / share_addr
share_host = row['share_addr'] or sni or 'metacode-cloud.com'
# clients table WSP
wsp=con.execute("select * from clients where email='WSP-ONE'").fetchone()
assert wsp, 'no_wsp'
# Build URI like panel (common 3.x)
q={'encryption':'none','security':security,'type':network}
if sni: q['sni']=sni
if alpn: q['alpn']=alpn
if fp: q['fp']=fp
if network=='tcp': q['headerType']=header or 'none'
flow=wsp['flow'] or ''
if flow: q['flow']=flow
query=urllib.parse.urlencode(q, quote_via=urllib.parse.quote)
uri=f"vless://{wsp['uuid']}@{share_host}:{row['port']}?{query}#{urllib.parse.quote('WSP-ONE', safe='')}"
Path('/root/mars-backups/p3-ux-wsp-after-clients-table.SECRET.txt').write_text(uri+'\n')
print('WSP_IN_CLIENTS', 1)
print('SHARE_HOST', share_host)
print('QUERY_KEYS', sorted(q.keys()))
print('SNI', sni)
print('ALPN', alpn)
print('FP', fp or '<empty>')
print('TYPE', network)
print('SECURITY', security)
print('FLOW', repr(flow))
print('HEADER', header or 'none')
# count
print('CLIENTS_N', con.execute('select count(*) from clients').fetchone()[0])
print('XRAY_CHECK')
j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
  if ib.get('port')==8443:
    print('XRAY_N', len((ib.get('settings') or {}).get('clients') or []))
P
"""
    )
    (EV / "D7-wsp-share-structure.txt").write_text(redact(out2 + "\n" + err2), encoding="utf-8")
    print(redact(out2 + "\n" + err2))

    # fetch secret uri and compare locally without printing
    sftp = c.open_sftp()
    local = EV.parent.parent.parent / "local"  # unused
    dest = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\p3-3xui-operator-ux-compare")
    dest.mkdir(parents=True, exist_ok=True)
    secret = dest / "wsp-ui-after-clients-table.SECRET.txt"
    sftp.get("/root/mars-backups/p3-ux-wsp-after-clients-table.SECRET.txt", str(secret))
    run("rm -f /root/mars-backups/p3-ux-wsp-after-clients-table.SECRET.txt")
    sftp.close()

    from urllib.parse import parse_qs, urlparse, unquote

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
            "uuid_ok": bool(p.username) and len(p.username) == 36,
        }

    mars = struct(
        Path(
            r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\WSP-ONE\friendhosting-de-raw-8443.vless.txt"
        ).read_text(encoding="utf-8")
    )
    ui = struct(secret.read_text(encoding="utf-8"))
    # UUID equality
    mars_u = urlparse(
        Path(
            r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\WSP-ONE\friendhosting-de-raw-8443.vless.txt"
        )
        .read_text(encoding="utf-8")
        .strip()
    ).username
    ui_u = urlparse(secret.read_text(encoding="utf-8").strip()).username
    keys = ["host", "port", "encryption", "security", "sni", "alpn", "fp", "type", "headerType", "flow"]
    diffs = [{"field": k, "ui": ui.get(k), "mars": mars.get(k)} for k in keys if ui.get(k) != mars.get(k)]
    cmp = {
        "struct_match_ignoring_optional_fp": all(
            ui.get(k) == mars.get(k) for k in keys if k != "fp"
        ),
        "struct_match_full": len(diffs) == 0,
        "diffs": diffs,
        "uuid_equal": mars_u == ui_u,
        "ui": ui,
        "mars": {k: mars[k] for k in mars if k != "fragment"} | {"fragment": mars["fragment"]},
    }
    (EV / "D8-final-compare.json").write_text(json.dumps(cmp, indent=2), encoding="utf-8")
    print("COMPARE", json.dumps({k: cmp[k] for k in cmp if k not in ("ui", "mars")}))
    c.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
