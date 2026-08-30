#!/usr/bin/env python3
"""Final P3 3X-UI operator UX health audit (no secret print)."""
from __future__ import annotations

import json
import re
import subprocess
import urllib.parse
from pathlib import Path

KEY = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
HOST = "92.42.99.126"
PORT = "3333"
EVID = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-3XUI-OPERATOR-UX-01")
MARS_URI = Path(
    r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\WSP-ONE\friendhosting-de-raw-8443.vless.txt"
)
CMP = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\p3-3xui-operator-ux-compare")


def ssh(script: str) -> str:
    r = subprocess.run(
        [
            "ssh",
            "-i",
            str(KEY),
            "-p",
            PORT,
            "-o",
            "BatchMode=yes",
            "-o",
            "StrictHostKeyChecking=accept-new",
            f"root@{HOST}",
            script,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        raise SystemExit(f"SSH_FAIL {r.returncode}\n{r.stderr}\n{r.stdout}")
    return r.stdout


def safe_fields(uri: str) -> dict:
    # strip scheme userinfo for parse
    u = uri.strip()
    assert u.lower().startswith("vless://")
    rest = u[8:]
    user, _, hostpart = rest.partition("@")
    hostport, _, qfrag = hostpart.partition("?")
    query, _, frag = qfrag.partition("#")
    if ":" in hostport:
        host, port = hostport.rsplit(":", 1)
    else:
        host, port = hostport, ""
    qs = urllib.parse.parse_qs(query, keep_blank_values=True)
    flat = {k: (v[0] if v else "") for k, v in qs.items()}
    return {
        "scheme": "vless",
        "host": host,
        "port": port,
        "encryption": flat.get("encryption", ""),
        "security": flat.get("security", ""),
        "sni": flat.get("sni", ""),
        "alpn": flat.get("alpn", ""),
        "fp": flat.get("fp", ""),
        "type": flat.get("type", ""),
        "headerType": flat.get("headerType", ""),
        "flow": flat.get("flow", ""),
        "fragment": urllib.parse.unquote(frag),
        "uuid_present": bool(re.fullmatch(r"[0-9a-fA-F-]{36}", user)),
        "uuid_len": len(user),
    }


REMOTE = r"""
python3 - <<'PY'
import json, sqlite3, subprocess, urllib.parse
from pathlib import Path

db = sqlite3.connect('/etc/x-ui/x-ui.db')
db.row_factory = sqlite3.Row
print('XUI', subprocess.check_output(['systemctl','is-active','x-ui'], text=True).strip())
print('CLIENTS_N', db.execute('select count(*) from clients').fetchone()[0])
print('CI_N', db.execute('select count(*) from client_inbounds').fetchone()[0])
emails = [r[0] for r in db.execute('select email from clients order by id')]
print('CLIENT_EMAILS', '|'.join(emails))
comments = {r['email']: (r['comment'] or '') for r in db.execute('select email, comment from clients')}
for e, c in comments.items():
    print('COMMENT', e, '::', c[:80])
row = db.execute('select settings from inbounds where port=8443').fetchone()
settings = json.loads(row[0])
clients = settings.get('clients', [])
print('INBOUND_SETTINGS_N', len(clients))
uuids = [x.get('id') for x in clients]
print('UUID_UNIQUE', len(uuids) == len(set(uuids)) and all(uuids))
print('ENABLED_JSON', json.dumps({x.get('email'): bool(x.get('enable', True)) for x in clients}, ensure_ascii=False))
# host share fields
h = db.execute('select address,port,security,sni,alpn,fingerprint from hosts where inbound_id=1').fetchone()
print('HOST_JSON', json.dumps(dict(h) if h else {}, ensure_ascii=False))
# reconstruct share URI for WSP-ONE like 3x-ui would (structure only)
w = None
for x in clients:
    if x.get('email') == 'WSP-ONE':
        w = x
        break
assert w, 'WSP-ONE missing'
alpn = h['alpn']
try:
    alpn_list = json.loads(alpn) if alpn and alpn.startswith('[') else ([alpn] if alpn else [])
except Exception:
    alpn_list = [alpn] if alpn else []
alpn_q = ','.join(alpn_list)
params = {
    'encryption': 'none',
    'security': h['security'] or 'tls',
    'sni': h['sni'] or '',
    'alpn': alpn_q,
    'fp': h['fingerprint'] or '',
    'type': 'tcp',
    'headerType': 'none',
    'flow': w.get('flow') or '',
}
# drop empties like UI may
params = {k: v for k, v in params.items() if v != ''}
q = urllib.parse.urlencode(params, safe='/')
uri = f"vless://{w['id']}@{h['address']}:{h['port']}?{q}#{urllib.parse.quote(w.get('email') or 'WSP-ONE')}"
Path('/tmp/wsp-one-3xui-share.uri').write_text(uri + '\n', encoding='utf-8')
print('WSP_URI_WRITTEN', 1)
cfg = json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in cfg.get('inbounds', []):
    if ib.get('port') == 8443:
        cl = ib.get('settings', {}).get('clients', [])
        print('XRAY_N', len(cl))
        print('XRAY_EMAILS', '|'.join(x.get('email', '') for x in cl))
        stream = ib.get('streamSettings', {})
        print('STREAM_NETWORK', stream.get('network'))
        print('STREAM_SECURITY', stream.get('security'))
        tls = stream.get('tlsSettings') or {}
        print('STREAM_SNI', (tls.get('serverName') or ''))
        print('STREAM_ALPN', json.dumps(tls.get('alpn') or []))
        print('STREAM_FP', tls.get('fingerprint') or '')
print(subprocess.check_output(['ss','-lntp'], text=True))
print('---UFW---')
print(subprocess.check_output(['ufw','status'], text=True))
PY
"""


def main() -> None:
    EVID.mkdir(parents=True, exist_ok=True)
    CMP.mkdir(parents=True, exist_ok=True)
    out = ssh(REMOTE)
    (EVID / "D13-final-audit.txt").write_text(out, encoding="utf-8")
    # fetch URI secretly
    raw = ssh("cat /tmp/wsp-one-3xui-share.uri && rm -f /tmp/wsp-one-3xui-share.uri")
    mars = MARS_URI.read_text(encoding="utf-8").strip()
    ui = raw.strip()
    (CMP / "wsp-one-3xui-share.uri").write_text(ui + "\n", encoding="utf-8")
    a = safe_fields(mars)
    b = safe_fields(ui)
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
    ]
    diffs = {k: {"mars": a.get(k), "ui": b.get(k)} for k in keys if a.get(k) != b.get(k)}
    # uuid equality without print
    mars_uuid = mars.split("://", 1)[1].split("@", 1)[0]
    ui_uuid = ui.split("://", 1)[1].split("@", 1)[0]
    result = {
        "struct_keys_compared": keys,
        "diffs": diffs,
        "struct_match_core": len(diffs) == 0,
        "uuid_equal": mars_uuid == ui_uuid,
        "mars_fragment": a["fragment"],
        "ui_fragment": b["fragment"],
        "fragment_note": "display name may differ; not material for transport",
    }
    (EVID / "D13-wsp-share-compare.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print("AUDIT_OK")
    print("STRUCT_MATCH", result["struct_match_core"])
    print("UUID_EQUAL", result["uuid_equal"])
    print("DIFF_KEYS", list(diffs.keys()))
    # print safe summary lines from remote
    for line in out.splitlines():
        if line.startswith(
            (
                "XUI ",
                "CLIENTS_N",
                "CI_N",
                "CLIENT_EMAILS",
                "COMMENT ",
                "INBOUND_SETTINGS_N",
                "UUID_UNIQUE",
                "ENABLED_JSON",
                "HOST_JSON",
                "XRAY_N",
                "XRAY_EMAILS",
                "STREAM_",
            )
        ):
            print(line)


if __name__ == "__main__":
    main()
