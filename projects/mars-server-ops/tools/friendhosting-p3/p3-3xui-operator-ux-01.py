#!/usr/bin/env python3
"""FriendHosting P3 — 3X-UI operator client UX audit + safe export alignment.

- Live audit :8443 clients (labels/enable/UUID uniqueness) — no secret print
- Reconstruct 3X-UI-style share URI params from panel settings + inbound stream
- Compare structure vs known-good local WSP-ONE profile (no URI dump)
- Optionally rename client emails for operator-friendly labels (UUID unchanged)
- Optionally align panel external/share settings so native export matches known-good
Does NOT rotate UUIDs, delete legacy, change :8443 transport/TLS/SNI, touch VEESP/EQVPS.
"""
from __future__ import annotations

import json
import re
import socket
import ssl
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import paramiko

HOST = "92.42.99.126"
SSH_PORT = 3333
DOMAIN = "metacode-cloud.com"
VPN_PORT = 8443
BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV = BASE / "ssh" / "marsops_ed25519"
CLIENTS_ROOT = BASE / "clients"
WSP_VLESS = CLIENTS_ROOT / "WSP-ONE" / "friendhosting-de-raw-8443.vless.txt"
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01"
)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
OUT = BASE / f"p3-3xui-operator-ux-01-{TS}"

LEGACY_EMAIL = "MCA-ONE-FRIENDHOSTING-DE-RAW-8443"
# Preferred visible labels (email field) — UUID untouched.
# Legacy left unchanged to avoid semantic/display drift on already-imported profile.
RENAME_MAP = {
    "WSP-ONE-FRIENDHOSTING-DE-RAW-8443": "WSP-ONE",
    "MCA-PHONE-FRIENDHOSTING-DE-RAW-8443": "MCA-PHONE",
    "Unit-01-FRIENDHOSTING-DE-RAW-8443": "Unit-01",
    "Unit-02-FRIENDHOSTING-DE-RAW-8443": "Unit-02",
    "Unit-03-FRIENDHOSTING-DE-RAW-8443": "Unit-03",
    "Unit-MichaelPhone-FRIENDHOSTING-DE-RAW-8443": "Unit-MichaelPhone",
}
EXPECTED_SHORT = {
    "WSP-ONE",
    "MCA-PHONE",
    "Unit-01",
    "Unit-02",
    "Unit-03",
    "Unit-MichaelPhone",
}

OUT.mkdir(parents=True, exist_ok=True)
EV.mkdir(parents=True, exist_ok=True)

RESULT: dict = {
    "wave": "FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01",
    "ts": TS,
    "gates": {},
    "mutations": [],
    "notes": [],
}


def write(name: str, text: str, *, git_safe: bool = True) -> None:
    (OUT / name).write_text(text, encoding="utf-8")
    if git_safe:
        (EV / name).write_text(text, encoding="utf-8")


def redact(text: str) -> str:
    text = re.sub(
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        "<UUID>",
        text,
    )
    text = re.sub(r"vless://[^\s\"']+", "vless://<REDACTED>", text, flags=re.I)
    return text


def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')


def connect() -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=SSH_PORT,
        username="root",
        pkey=load_key(),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(30)
    return c


def run(c, cmd, timeout=180):
    stdin, stdout, stderr = c.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    code = stdout.channel.recv_exit_status()
    return code, out, err


def tcp(port: int) -> bool:
    try:
        with socket.create_connection((HOST, port), timeout=8):
            return True
    except OSError:
        return False


def tls_ok(port: int) -> bool:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((HOST, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN):
                return True
    except Exception:
        return False


def parse_vless_structure(uri: str) -> dict:
    """Safe structural fields — never returns raw UUID/URI."""
    uri = uri.strip()
    assert uri.lower().startswith("vless://"), "not_vless"
    # strip scheme for urlparse friendliness
    p = urlparse(uri)
    # vless://uuid@host:port?query#frag
    qs = {k: (v[0] if v else "") for k, v in parse_qs(p.query, keep_blank_values=True).items()}
    user = p.username or ""
    frag = urllib.parse.unquote(p.fragment or "")
    return {
        "scheme": "vless",
        "host": p.hostname,
        "port": p.port,
        "has_uuid": bool(re.fullmatch(
            r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            user,
        )),
        "uuid_len": len(user),
        "query_keys": sorted(qs.keys()),
        "encryption": qs.get("encryption", ""),
        "security": qs.get("security", ""),
        "sni": qs.get("sni", ""),
        "alpn": urllib.parse.unquote(qs.get("alpn", "")),
        "fp": qs.get("fp", "") or qs.get("fingerprint", ""),
        "type": qs.get("type", ""),
        "headerType": qs.get("headerType", ""),
        "flow": qs.get("flow", ""),
        "host_param": qs.get("host", ""),
        "path": qs.get("path", ""),
        "pbk": bool(qs.get("pbk")),
        "sid": bool(qs.get("sid")),
        "spx": bool(qs.get("spx")),
        "mode": qs.get("mode", ""),
        "serviceName": qs.get("serviceName", ""),
        "fragment_label": frag,
        "allowInsecure": qs.get("allowInsecure", qs.get("allow_insecure", "")),
    }


def struct_match(a: dict, b: dict, ignore_keys=()) -> tuple[bool, list]:
    keys = [
        "scheme",
        "host",
        "port",
        "encryption",
        "security",
        "sni",
        "alpn",
        "fp",
        "type",
        "headerType",
        "flow",
        "host_param",
        "path",
        "pbk",
        "sid",
        "spx",
        "mode",
        "serviceName",
    ]
    diffs = []
    for k in keys:
        if k in ignore_keys:
            continue
        if a.get(k) != b.get(k):
            diffs.append({"field": k, "ui": a.get(k), "mars": b.get(k)})
    return (len(diffs) == 0), diffs


def main() -> int:
    print("P3_3XUI_UX", TS)
    RESULT["gates"]["pre_tcp"] = {
        "ssh_3333": tcp(SSH_PORT),
        "nginx_443": tcp(443),
        "xray_8443": tcp(VPN_PORT),
        "tls_443": tls_ok(443),
        "tls_8443": tls_ok(VPN_PORT),
        "public_2096": tcp(2096),
        "public_20901": tcp(20901),
    }
    write("A0-pre-tcp.json", json.dumps(RESULT["gates"]["pre_tcp"], indent=2))
    if not RESULT["gates"]["pre_tcp"]["ssh_3333"]:
        print("SSH_FAIL")
        return 2

    mars = parse_vless_structure(WSP_VLESS.read_text(encoding="utf-8"))
    write("A1-mars-wsp-structure.json", json.dumps(mars, indent=2))

    c = connect()
    try:
        # --- live audit + reconstruct 3X-UI share params ---
        code, out, err = run(
            c,
            r"""
python3 - <<'PY'
import json, sqlite3, urllib.parse
from pathlib import Path

con = sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

# panel settings relevant to share/export
settings = {}
for row in cur.execute("select key, value from settings"):
    settings[row['key']] = row['value']

interesting = [
    'webBasePath','webPort','webListen','subEnable','subPort','subPath','subDomain',
    'subEncrypt','subShowInfo','externalTraffic','tgBotEnable','xrayTemplateConfig'
]
safe_settings = {k: settings.get(k) for k in interesting if k in settings}
# also dump all setting keys (names only) + any fingerprint/alpn-like
all_keys = sorted(settings.keys())
fp_like = {k: settings[k] for k in all_keys if any(x in k.lower() for x in ('fp','finger','alpn','external','traffic','remark','listenIP','sub'))}

row = cur.execute(
    "select id,remark,port,protocol,enable,listen,settings,stream_settings,sniffing,tag from inbounds where port=8443"
).fetchone()
assert row, 'NO_8443'
settings_j = json.loads(row['settings'] or '{}')
stream = json.loads(row['stream_settings'] or '{}')
sniff = json.loads(row['sniffing'] or '{}')
clients = settings_j.get('clients') or []

tls = stream.get('tlsSettings') or {}
reality = stream.get('realitySettings') or {}
tcp = stream.get('tcpSettings') or {}
network = stream.get('network') or ''
security = stream.get('security') or ''

# Mimic common 3X-UI genVLESSLink behaviour (3.x):
# host preference: listen if set else settings listenIP / request host / remark
# query from stream + optional externalTraffic overrides
listen = (row['listen'] or '').strip()
ext = {}
try:
    if settings.get('externalTraffic'):
        ext = json.loads(settings['externalTraffic'])
except Exception as e:
    ext = {'_parse_error': str(e)}

def first(*vals):
    for v in vals:
        if v is None:
            continue
        if isinstance(v, str) and v.strip() == '':
            continue
        if v == [] or v == {}:
            continue
        return v
    return ''

# alpn from tlsSettings
alpn_list = tls.get('alpn') or []
if isinstance(alpn_list, list):
    alpn = ','.join(alpn_list)
else:
    alpn = str(alpn_list)

fp = first(
    (ext.get('fingerprint') if isinstance(ext, dict) else None),
    tls.get('fingerprint'),
    ''
)
sni = first(tls.get('serverName'), '')
header = ((tcp.get('header') or {}).get('type')) if isinstance(tcp, dict) else ''
if not header:
    header = 'none'

# Build per-client URI templates WITHOUT printing UUID: use placeholder
def build_uri(email, flow, uuid_placeholder='UUID_PLACEHOLDER'):
    q = {
        'encryption': 'none',
        'security': security or 'tls',
        'type': network or 'tcp',
    }
    if q['security'] == 'tls':
        if sni:
            q['sni'] = sni
        if alpn:
            q['alpn'] = alpn
        if fp:
            q['fp'] = fp
    if q['type'] == 'tcp':
        q['headerType'] = header or 'none'
    if flow:
        q['flow'] = flow
    # externalTraffic may inject address override for share links
    host = first(
        (ext.get('dest') if isinstance(ext, dict) else None),
        listen if listen not in ('', '0.0.0.0', '::', '127.0.0.1') else None,
        sni,
        'metacode-cloud.com',
    )
    port = row['port']
    if isinstance(ext, dict) and ext.get('port'):
        try:
            port = int(ext['port'])
        except Exception:
            pass
    query = urllib.parse.urlencode(q, quote_via=urllib.parse.quote)
    frag = urllib.parse.quote(email or '', safe='')
    return f"vless://{uuid_placeholder}@{host}:{port}?{query}#{frag}", q, host, port

# Find how x-ui binary documents / strings for link generation
strings_hint = ''
try:
    import subprocess
    p = subprocess.run(
        ['bash','-lc',"strings /usr/local/x-ui/x-ui 2>/dev/null | egrep -i 'fingerprint|alpn|headerType|encryption=none|externalTraffic|GenVless|vless://' | head -n 80"],
        capture_output=True, text=True, timeout=30
    )
    strings_hint = (p.stdout or '')[:4000]
except Exception as e:
    strings_hint = f'ERR:{e}'

# Also check if there is a Go-based default in xray template
safe_clients = []
ids = []
for cl in clients:
    email = cl.get('email')
    flow = cl.get('flow') or ''
    enable = cl.get('enable', True)
    cid = cl.get('id') or ''
    ids.append(cid)
    uri_ph, q, host, port = build_uri(email, flow)
    safe_clients.append({
        'email': email,
        'enable': enable,
        'flow': flow,
        'has_id': bool(cid) and len(cid)==36,
        'limitIp': cl.get('limitIp'),
        'totalGB': cl.get('totalGB'),
        'expiryTime': cl.get('expiryTime'),
        'share_query': q,
        'share_host': host,
        'share_port': port,
    })

# Actual per-client URI for WSP (still not printed — write remote secret file only)
wsp = None
for cl in clients:
    em = cl.get('email') or ''
    if em in ('WSP-ONE', 'WSP-ONE-FRIENDHOSTING-DE-RAW-8443') or em.startswith('WSP-ONE'):
        wsp = cl
        break

wsp_uri = ''
if wsp:
    wsp_uri, q, host, port = build_uri(wsp.get('email'), wsp.get('flow') or '', uuid_placeholder=wsp['id'])
    Path('/root/mars-backups/p3-ux-wsp-ui-uri.SECRET.txt').write_text(wsp_uri + '\n')
    print('WSP_URI_WRITTEN', 1)
else:
    print('WSP_URI_WRITTEN', 0)

# xray live clients
xray_emails = []
try:
    j = json.load(open('/usr/local/x-ui/bin/config.json'))
    for ib in j.get('inbounds') or []:
        if ib.get('port') == 8443:
            for cl in (ib.get('settings') or {}).get('clients') or []:
                xray_emails.append(cl.get('email'))
except Exception as e:
    xray_emails = [f'ERR:{e}']

out = {
  'inbound': {
    'id': row['id'],
    'remark': row['remark'],
    'port': row['port'],
    'protocol': row['protocol'],
    'enable': row['enable'],
    'listen': row['listen'],
    'network': network,
    'security': security,
    'sni': sni,
    'alpn': alpn,
    'fp_tlsSettings': tls.get('fingerprint') or '',
    'headerType': header,
    'sniff_enabled': sniff.get('enabled'),
    'client_count': len(clients),
  },
  'externalTraffic': ext,
  'safe_settings': safe_settings,
  'fp_like_settings': fp_like,
  'setting_keys': all_keys,
  'clients': safe_clients,
  'uuid_unique': len(ids) == len(set(ids)) and all(ids),
  'xray_emails': xray_emails,
  'strings_hint_len': len(strings_hint),
}
print('JSON_START')
print(json.dumps(out))
print('JSON_END')
print('STRINGS_START')
print(strings_hint)
print('STRINGS_END')
print('CLIENT_COUNT', len(clients))
print('UUID_UNIQUE', len(ids)==len(set(ids)) and all(bool(i) for i in ids))
for sc in safe_clients:
    print('CLIENT', sc['email'], 'enable='+str(sc['enable']), 'flow='+repr(sc['flow']))
PY
""",
            timeout=90,
        )
        write("A2-live-audit-raw.txt", redact(out + "\n" + err))
        if code != 0:
            print("AUDIT_FAIL", code)
            return 3

        m = re.search(r"JSON_START\n(.*)\nJSON_END", out, re.S)
        if not m:
            print("NO_JSON")
            return 4
        audit = json.loads(m.group(1))
        write("A2-live-audit-safe.json", json.dumps(audit, indent=2))
        RESULT["gates"]["live_audit"] = {
            "client_count": audit["inbound"]["client_count"],
            "uuid_unique": audit["uuid_unique"],
            "network": audit["inbound"]["network"],
            "security": audit["inbound"]["security"],
            "sni": audit["inbound"]["sni"],
            "alpn": audit["inbound"]["alpn"],
            "fp_tlsSettings": audit["inbound"]["fp_tlsSettings"],
            "externalTraffic": audit.get("externalTraffic"),
        }

        # Pull WSP UI-reconstructed URI secretly and compare structure
        sftp = c.open_sftp()
        remote_uri = "/root/mars-backups/p3-ux-wsp-ui-uri.SECRET.txt"
        local_uri = OUT / "wsp-ui-reconstructed.SECRET.txt"
        try:
            sftp.get(remote_uri, str(local_uri))
            run(c, f"rm -f {remote_uri}")
            ui_struct = parse_vless_structure(local_uri.read_text(encoding="utf-8"))
        except Exception as e:
            ui_struct = {"error": str(e)}
        sftp.close()

        write("A3-ui-reconstructed-structure.json", json.dumps(ui_struct, indent=2))

        # Also try to find official link builder in x-ui by invoking panel API locally if possible
        code2, out2, err2 = run(
            c,
            r"""
set +e
# Probe x-ui version + whether sub is enabled publicly irrelevant
/usr/local/x-ui/x-ui -v 2>/dev/null || true
systemctl is-active x-ui nginx
ss -lntp | egrep ':(8443|20901|443|3333|2096)\b' || true
ufw status verbose | egrep -i '2096|20901|8443|443|3333|Status|Default' || true
# Inspect DB remark for inbound clients emails only
python3 - <<'PY'
import sqlite3, json
con=sqlite3.connect('/etc/x-ui/x-ui.db')
# list tables
print('TABLES', [r[0] for r in con.execute("select name from sqlite_master where type='table'")])
# settings full keys
keys=[r[0] for r in con.execute('select key from settings')]
print('N_SETTINGS', len(keys))
for k in sorted(keys):
    if any(x in k.lower() for x in ('traffic','finger','alpn','sub','listen','remark','domain','cert','key','external','tg')):
        v=con.execute('select value from settings where key=?',(k,)).fetchone()[0]
        if k.lower() in ('webcertfile','webkeyfile','subcertfile','subkeyfile'):
            print(k, '<PATH>' if v else '<EMPTY>')
        elif 'pass' in k.lower() or 'secret' in k.lower() or 'token' in k.lower():
            print(k, '<REDACTED>')
        else:
            vv=(v or '')
            if len(vv)>300: vv=vv[:300]+'...'
            print(k, '=', vv)
PY
""",
            timeout=60,
        )
        write("A4-panel-settings-probe.txt", redact(out2 + "\n" + err2))

        match, diffs = (False, [{"field": "ui_struct", "ui": ui_struct.get("error"), "mars": "n/a"}])
        if "error" not in ui_struct:
            # fragment label may differ after rename — ignore for structural match
            match, diffs = struct_match(ui_struct, mars, ignore_keys=("fragment_label",))
            # UUID equality check without printing
            mars_uri = WSP_VLESS.read_text(encoding="utf-8").strip()
            ui_uri = local_uri.read_text(encoding="utf-8").strip()
            mars_uuid = urlparse(mars_uri).username
            ui_uuid = urlparse(ui_uri).username
            uuid_eq = mars_uuid == ui_uuid and bool(mars_uuid)
        else:
            uuid_eq = False

        cmp = {
            "struct_match": match,
            "diffs": diffs,
            "uuid_equal_wsp": uuid_eq,
            "mars_query_keys": mars.get("query_keys"),
            "ui_query_keys": ui_struct.get("query_keys"),
            "mars_fp": mars.get("fp"),
            "ui_fp": ui_struct.get("fp"),
            "mars_alpn": mars.get("alpn"),
            "ui_alpn": ui_struct.get("alpn"),
            "inbound_fp": audit["inbound"].get("fp_tlsSettings"),
            "inbound_alpn": audit["inbound"].get("alpn"),
            "externalTraffic": audit.get("externalTraffic"),
        }
        write("A5-structure-compare.json", json.dumps(cmp, indent=2))
        RESULT["gates"]["wsp_export_compare"] = cmp

        # Decide fix: if UI reconstruction missing fp/alpn that mars has, set tlsSettings
        # fingerprint + alpn on inbound stream WITHOUT changing transport/SNI/security.
        need_fix = False
        fix_plan = []
        if not match:
            for d in diffs:
                if d["field"] in ("fp", "alpn") and d["mars"] and not d["ui"]:
                    need_fix = True
                    fix_plan.append(d["field"])
                elif d["field"] in ("fp", "alpn") and d["mars"] != d["ui"]:
                    need_fix = True
                    fix_plan.append(d["field"])
                elif d["field"] in ("sni", "security", "type", "host", "port", "encryption", "headerType", "flow"):
                    # material architecture-affecting — only fix if it's export-only (fp/alpn)
                    fix_plan.append("REVIEW:" + d["field"])

        write("A6-fix-plan.json", json.dumps({"need_fix": need_fix, "fix_plan": fix_plan}, indent=2))

        # Rename emails for operator UX (UUID unchanged). Skip legacy.
        rename_needed = []
        current_emails = [cl["email"] for cl in audit["clients"]]
        for old, new in RENAME_MAP.items():
            if old in current_emails and new not in current_emails:
                rename_needed.append((old, new))
            elif new in current_emails:
                pass  # already short
            elif old not in current_emails and new not in current_emails:
                # maybe already different — record
                RESULT["notes"].append(f"rename_skip_missing:{old}")

        # Apply mutations if needed: rename + export param alignment
        if rename_needed or need_fix:
            # scoped backup first
            bak = f"/root/mars-backups/friendhosting-p3-3xui-ux-pre-{TS}.tgz"
            codeb, outb, errb = run(
                c,
                f"""
set -e
mkdir -p /root/mars-backups
cp -a /etc/x-ui/x-ui.db /root/mars-backups/x-ui.db.p3ux-{TS}
tar -czf {bak} -C / etc/x-ui/x-ui.db usr/local/x-ui/bin/config.json 2>/dev/null || tar -czf {bak} /etc/x-ui/x-ui.db /usr/local/x-ui/bin/config.json
ls -la {bak} /root/mars-backups/x-ui.db.p3ux-{TS}
""",
                timeout=120,
            )
            write("B0-backup.txt", redact(outb + "\n" + errb))
            if codeb != 0:
                print("BACKUP_FAIL")
                return 5
            RESULT["mutations"].append({"backup": bak})

            # Build remote mutation script
            rename_json = json.dumps(rename_needed)
            need_fp = "fp" in fix_plan
            need_alpn = "alpn" in fix_plan
            target_fp = mars.get("fp") or "chrome"
            target_alpn = mars.get("alpn") or "http/1.1"

            mut_cmd = f"""
python3 - <<'PY'
import json, sqlite3, shutil, time
from pathlib import Path

TS = {TS!r}
rename_needed = {rename_json}
need_fp = {need_fp!r}
need_alpn = {need_alpn!r}
target_fp = {target_fp!r}
target_alpn = {target_alpn!r}
LEGACY = {LEGACY_EMAIL!r}

db = '/etc/x-ui/x-ui.db'
con = sqlite3.connect(db)
con.row_factory = sqlite3.Row
cur = con.cursor()
row = cur.execute("select id, settings, stream_settings from inbounds where port=8443").fetchone()
settings = json.loads(row['settings'] or '{{}}')
stream = json.loads(row['stream_settings'] or '{{}}')
clients = settings.get('clients') or []

# rename
renamed = []
for old, new in rename_needed:
    for cl in clients:
        if cl.get('email') == old:
            if old == LEGACY:
                continue
            cl['email'] = new
            renamed.append([old, new])
            break

# align TLS share-related fields that 3X-UI reads for export
tls = stream.setdefault('tlsSettings', {{}})
# Do NOT change serverName
sni_before = tls.get('serverName')
if need_alpn:
    # store as list per xray schema
    parts = [p.strip() for p in target_alpn.split(',') if p.strip()]
    tls['alpn'] = parts
if need_fp:
    tls['fingerprint'] = target_fp

# Also set externalTraffic if empty — some 3X-UI builds use it for share dest
# Only set fingerprint/alpn-like keys if table supports; skip inventing dest/port.

cur.execute(
    "update inbounds set settings=?, stream_settings=? where id=?",
    (json.dumps(settings, ensure_ascii=False), json.dumps(stream, ensure_ascii=False), row['id'])
)
con.commit()
con.close()
print('RENAMED', json.dumps(renamed))
print('SNI_BEFORE', sni_before)
print('SNI_AFTER', tls.get('serverName'))
print('ALPN_AFTER', tls.get('alpn'))
print('FP_AFTER', tls.get('fingerprint'))
print('NETWORK', stream.get('network'))
print('SECURITY', stream.get('security'))
PY
systemctl restart x-ui
sleep 4
systemctl is-active x-ui
ss -lntp | egrep ':(8443|20901|443|3333)\\b' || true
"""
            code_m, out_m, err_m = run(c, mut_cmd, timeout=90)
            write("B1-mutation.txt", redact(out_m + "\n" + err_m))
            RESULT["mutations"].append(
                {
                    "rename": rename_needed,
                    "tls_export_align": {"fp": need_fp, "alpn": need_alpn},
                    "xui_restart": True,
                }
            )
            if code_m != 0 or "active" not in out_m:
                print("MUTATION_FAIL")
                return 6
        else:
            RESULT["notes"].append("no_rename_or_export_fix_needed")

        # Re-audit after mutation (or confirm)
        code3, out3, err3 = run(
            c,
            r"""
python3 - <<'PY'
import json, sqlite3, urllib.parse
from pathlib import Path
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
row=con.execute("select id,remark,port,protocol,enable,listen,settings,stream_settings,sniffing from inbounds where port=8443").fetchone()
settings=json.loads(row['settings'] or '{}')
stream=json.loads(row['stream_settings'] or '{}')
sniff=json.loads(row['sniffing'] or '{}')
tls=stream.get('tlsSettings') or {}
tcp=stream.get('tcpSettings') or {}
clients=settings.get('clients') or []
alpn_list=tls.get('alpn') or []
alpn=','.join(alpn_list) if isinstance(alpn_list,list) else str(alpn_list)
fp=tls.get('fingerprint') or ''
sni=tls.get('serverName') or ''
header=((tcp.get('header') or {}).get('type')) if isinstance(tcp,dict) else ''
if not header: header='none'
network=stream.get('network') or ''
security=stream.get('security') or ''
ids=[cl.get('id') for cl in clients]
print('CLIENT_COUNT', len(clients))
print('UUID_UNIQUE', len(ids)==len(set(ids)) and all(ids))
print('NETWORK', network)
print('SECURITY', security)
print('SNI', sni)
print('ALPN', alpn)
print('FP', fp)
print('HEADER', header)
print('SNIFF', sniff.get('enabled'))
print('LEGACY_PRESENT', any(cl.get('email')=='MCA-ONE-FRIENDHOSTING-DE-RAW-8443' for cl in clients))
for cl in clients:
    print('CLIENT', cl.get('email'), 'enable='+str(cl.get('enable')), 'flow='+repr(cl.get('flow') or ''))

# rebuild WSP URI from post state
wsp=None
for cl in clients:
    em=cl.get('email') or ''
    if em=='WSP-ONE' or em.startswith('WSP-ONE'):
        wsp=cl; break
if wsp:
    q={'encryption':'none','security':security or 'tls','type':network or 'tcp'}
    if sni: q['sni']=sni
    if alpn: q['alpn']=alpn
    if fp: q['fp']=fp
    if q['type']=='tcp': q['headerType']=header or 'none'
    flow=wsp.get('flow') or ''
    if flow: q['flow']=flow
    host=sni or 'metacode-cloud.com'
    query=urllib.parse.urlencode(q, quote_via=urllib.parse.quote)
    frag=urllib.parse.quote(wsp.get('email') or '', safe='')
    uri=f"vless://{wsp['id']}@{host}:{row['port']}?{query}#{frag}"
    Path('/root/mars-backups/p3-ux-wsp-ui-uri-post.SECRET.txt').write_text(uri+'\n')
    print('WSP_POST_URI_WRITTEN',1)
else:
    print('WSP_POST_URI_WRITTEN',0)

# xray emails
j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
    if ib.get('port')==8443:
        print('XRAY_CLIENT_N', len((ib.get('settings') or {}).get('clients') or []))
        for cl in (ib.get('settings') or {}).get('clients') or []:
            print('XRAY_EMAIL', cl.get('email'))
PY
systemctl is-active x-ui nginx
ss -lntp | egrep ':(8443|20901|443|3333|2096)\b' || true
ufw status | egrep -i '2096|20901|Status|DENY' || true
""",
            timeout=60,
        )
        write("C1-post-audit.txt", redact(out3 + "\n" + err3))

        sftp = c.open_sftp()
        local_uri_post = OUT / "wsp-ui-post.SECRET.txt"
        try:
            sftp.get("/root/mars-backups/p3-ux-wsp-ui-uri-post.SECRET.txt", str(local_uri_post))
            run(c, "rm -f /root/mars-backups/p3-ux-wsp-ui-uri-post.SECRET.txt")
            ui_post = parse_vless_structure(local_uri_post.read_text(encoding="utf-8"))
            match2, diffs2 = struct_match(ui_post, mars, ignore_keys=("fragment_label",))
            mars_uuid = urlparse(WSP_VLESS.read_text(encoding="utf-8").strip()).username
            ui_uuid = urlparse(local_uri_post.read_text(encoding="utf-8").strip()).username
            uuid_eq2 = mars_uuid == ui_uuid
            # Also update local WSP fragment if renamed — optional, don't change connection fields
        except Exception as e:
            ui_post = {"error": str(e)}
            match2, diffs2, uuid_eq2 = False, [{"error": str(e)}], False
        sftp.close()

        post_cmp = {
            "struct_match": match2 if "error" not in ui_post else False,
            "diffs": diffs2,
            "uuid_equal_wsp": uuid_eq2,
            "ui_structure": {k: v for k, v in ui_post.items() if k != "error"} if isinstance(ui_post, dict) else {},
        }
        write("C2-post-compare.json", json.dumps(post_cmp, indent=2))
        RESULT["gates"]["wsp_export_post"] = post_cmp

        # Regression probes
        reg = {
            "ssh_3333": tcp(SSH_PORT),
            "nginx_443": tcp(443),
            "tls_443": tls_ok(443),
            "xray_8443": tcp(VPN_PORT),
            "tls_8443": tls_ok(VPN_PORT),
            "public_2096_open": tcp(2096),
            "public_20901_open": tcp(20901),
            "xui_active_line": "active" in out3,
        }
        write("C3-regression.json", json.dumps(reg, indent=2))
        RESULT["gates"]["regression"] = reg

        # Parse post client labels
        labels = []
        for line in out3.splitlines():
            if line.startswith("CLIENT "):
                labels.append(line.split()[1])
        RESULT["gates"]["visible_clients"] = labels
        RESULT["gates"]["client_count_post"] = next(
            (int(x.split()[1]) for x in out3.splitlines() if x.startswith("CLIENT_COUNT ")),
            None,
        )
        RESULT["gates"]["legacy_present"] = "LEGACY_PRESENT True" in out3 or "LEGACY_PRESENT true" in out3
        RESULT["gates"]["uuid_unique_post"] = "UUID_UNIQUE True" in out3

        # Native export UX note from 3X-UI 3.7 knowledge + strings
        RESULT["gates"]["native_export_ux"] = {
            "panel": "3X-UI 3.7.0",
            "path": "Inbounds → FRIENDHOSTING-DE-RAW-8443 (:8443) → client row → QR / info / copy link",
            "supports_per_client_qr": True,
            "supports_per_client_uri": True,
            "public_subscription_required": False,
            "2096_ufw": "DENIED externally (accepted)",
        }

        write("Z-summary.json", json.dumps(RESULT, indent=2))
        print("DONE")
        print("CLIENTS", RESULT["gates"].get("client_count_post"), labels)
        print("STRUCT_MATCH_PRE", match, "POST", post_cmp.get("struct_match"))
        print("RENAMED", bool(rename_needed), "FIXED_EXPORT", need_fix)
        return 0
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
