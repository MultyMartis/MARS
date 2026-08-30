#!/usr/bin/env python3
"""FriendHosting P3 — per-device VLESS identities on accepted :8443 inbound.

Mutates FriendHosting only: adds independent clients; preserves legacy MCA-ONE.
Does NOT alter port/TLS/SNI/transport, VEESP, EQVPS, or :24443.
Secrets stay under local/infrastructure/FRIENDHOSTING-GERMANY/ — never printed.
"""
from __future__ import annotations

import hashlib
import json
import re
import socket
import ssl
import tarfile
import time
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
DOMAIN = "metacode-cloud.com"
VPN_PORT = 8443
BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV = BASE / "ssh" / "marsops_ed25519"
CLIENTS_ROOT = BASE / "clients"
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01"
)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
OUT = BASE / f"p3-per-device-identities-01-{TS}"
BAK_NAME = f"friendhosting-p3-pre-device-identities-{TS}"
REMOTE_BAK_DIR = "/root/mars-backups"
REMOTE_BAK = f"{REMOTE_BAK_DIR}/{BAK_NAME}.tgz"
LOCAL_BAK = BASE / "backups" / f"{BAK_NAME}.tgz"

# Authoritative EQVPS fleet (local clients/) + P3 naming for NEW FH identities.
# MCA-ONE physical workstation: NEW label WSP-ONE (avoids colliding with LEGACY MCA-ONE email).
LEGACY_EMAIL = "MCA-ONE-FRIENDHOSTING-DE-RAW-8443"
NEW_DEVICES = [
    # (device_folder, display_email, maps_to_eqvps_device, is_current_workstation)
    ("WSP-ONE", "WSP-ONE-FRIENDHOSTING-DE-RAW-8443", "MCA-ONE", True),
    ("MCA-PHONE", "MCA-PHONE-FRIENDHOSTING-DE-RAW-8443", "MCA-PHONE", False),
    ("Unit-01", "Unit-01-FRIENDHOSTING-DE-RAW-8443", "Unit-01", False),
    ("Unit-02", "Unit-02-FRIENDHOSTING-DE-RAW-8443", "Unit-02", False),
    ("Unit-03", "Unit-03-FRIENDHOSTING-DE-RAW-8443", "Unit-03", False),
    ("Unit-MichaelPhone", "Unit-MichaelPhone-FRIENDHOSTING-DE-RAW-8443", "Unit-MichaelPhone", False),
]

OUT.mkdir(parents=True, exist_ok=True)
EV.mkdir(parents=True, exist_ok=True)
(BASE / "backups").mkdir(parents=True, exist_ok=True)
CLIENTS_ROOT.mkdir(parents=True, exist_ok=True)

RESULT: dict = {
    "wave": "FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01",
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


def connect(user: str = "root") -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=PORT,
        username=user,
        pkey=load_key(),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(30)
    return c


def run(c: paramiko.SSHClient, cmd: str, timeout: int = 180):
    try:
        stdin, stdout, stderr = c.exec_command(cmd, timeout=timeout)
        stdout.channel.settimeout(timeout)
        stderr.channel.settimeout(timeout)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        code = stdout.channel.recv_exit_status()
        return code, out, err
    except Exception as e:
        return 124, "", f"ERR:{type(e).__name__}:{e}"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tcp(port: int, timeout: float = 8) -> bool:
    try:
        with socket.create_connection((HOST, port), timeout=timeout):
            return True
    except OSError:
        return False


def tls(port: int) -> dict:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((HOST, port), timeout=10) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                cert = ssock.getpeercert()
                return {
                    "ok": True,
                    "notAfter": cert.get("notAfter"),
                    "subject": str(cert.get("subject")),
                }
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def http_get(port: int, path: str = "/", host: str | None = None) -> dict:
    url = f"http://{HOST}:{port}{path}"
    req = urllib.request.Request(url, method="GET")
    if host:
        req.add_header("Host", host)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            return {"reachable": True, "status": r.status}
    except Exception as e:
        code = getattr(e, "code", None)
        return {
            "reachable": code is not None,
            "status": code,
            "error": type(e).__name__,
        }


def sub_id_for(email: str) -> str:
    # stable short subId from email, alphanumeric
    slug = re.sub(r"[^a-zA-Z0-9]", "", email.lower())[:24]
    return f"fhde{slug}"[:32]


def phase_health(c: paramiko.SSHClient) -> dict:
    gates = {
        "ssh_tcp": tcp(3333),
        "nginx_tcp": tcp(443),
        "xray_tcp": tcp(8443),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
        "http_20901_public": http_get(20901, "/"),
    }
    code, out, err = run(
        c,
        r"""
set +e
echo WHOAMI=$(whoami)
echo XUI=$(systemctl is-active x-ui)
echo XRAY=$(systemctl is-active x-ui)  # xray managed by x-ui
ss -lntp | egrep ':(3333|443|8443|20901|2096|80)\b' || true
curl -s -o /dev/null -w 'LOCAL_XUI_HTTP=%{http_code}\n' http://127.0.0.1:20901/ || echo LOCAL_XUI_HTTP=FAIL
curl -sk -o /dev/null -w 'LOCAL_XUI_HTTPS=%{http_code}\n' https://127.0.0.1:20901/ || echo LOCAL_XUI_HTTPS=FAIL
ss -lntp | grep -q '127.0.0.1:20901' && echo LOCAL_XUI_LISTEN=YES || echo LOCAL_XUI_LISTEN=NO
python3 - <<'PY'
import sqlite3, json
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
cur=con.cursor()
rows=cur.execute('select id,remark,port,protocol,enable from inbounds').fetchall()
print('INBOUNDS', len(rows))
for r in rows:
    print('INBOUND', dict(r))
    s=cur.execute('select settings,stream_settings,sniffing from inbounds where id=?', (r['id'],)).fetchone()
    settings=json.loads(s[0])
    stream=json.loads(s[1]) if s[1] else {}
    sniff=json.loads(s[2]) if s[2] else {}
    clients=settings.get('clients') or []
    print('CLIENTS_N', len(clients))
    for cl in clients:
        print('CLIENT', {
            'email': cl.get('email'),
            'enable': cl.get('enable'),
            'flow': cl.get('flow', ''),
            'has_id': bool(cl.get('id')),
        })
    print('STREAM', {
        'network': stream.get('network'),
        'security': stream.get('security'),
        'sni': (stream.get('tlsSettings') or {}).get('serverName'),
    })
    print('SNIFF', {'enabled': sniff.get('enabled'), 'routeOnly': sniff.get('routeOnly')})
con.close()
PY
""",
        timeout=60,
    )
    safe = redact(out + "\n" + err)
    write("A0-pre-health.txt", safe)
    http_ok = bool(re.search(r"LOCAL_XUI_HTTP=([1-5]\d\d)", out))
    https_ok = bool(re.search(r"LOCAL_XUI_HTTPS=([1-5]\d\d)", out))
    listen_ok = "LOCAL_XUI_LISTEN=YES" in out
    gates["local_xui"] = bool((http_ok or https_ok or listen_ok) and "XUI=active" in out)
    gates["xui_active"] = "XUI=active" in out
    # parse client emails safely
    emails = re.findall(r"'email': '([^']+)'", out)
    if not emails:
        emails = re.findall(r'"email": "([^"]+)"', out)
    gates["legacy_present"] = LEGACY_EMAIL in emails or LEGACY_EMAIL in out
    gates["client_count_before"] = len(emails) if emails else out.count("CLIENT ")
    RESULT["gates"]["pre"] = {
        k: (v if not isinstance(v, dict) else {"ok": v.get("ok"), "notAfter": v.get("notAfter")})
        for k, v in gates.items()
    }
    write("A0-pre-health-gates.json", json.dumps(RESULT["gates"]["pre"], indent=2))
    critical = (
        gates["ssh_tcp"]
        and gates["nginx_tcp"]
        and gates["xray_tcp"]
        and gates["tls_8443"].get("ok")
        and gates["local_xui"]
        and gates["legacy_present"]
    )
    gates["critical_pass"] = bool(critical)
    return gates


def phase_backup(c: paramiko.SSHClient) -> dict:
    remote_script = f"""
set -euo pipefail
STAGING=/root/mars-backups/{BAK_NAME}
rm -rf "$STAGING"
mkdir -p "$STAGING"/meta "$STAGING"/etc "$STAGING"/usr-local "$STAGING"/var-lib
cp -a /etc/ssh "$STAGING/etc/" || true
cp -a /etc/nginx "$STAGING/etc/" || true
cp -a /etc/letsencrypt "$STAGING/etc/" || true
cp -a /etc/ufw "$STAGING/etc/" || true
cp -a /etc/fail2ban "$STAGING/etc/" || true
cp -a /etc/systemd "$STAGING/etc/" 2>/dev/null || true
cp -a /etc/x-ui "$STAGING/etc/" || true
cp -a /usr/local/x-ui "$STAGING/usr-local/" || true
# runtime xray config if present
cp -a /usr/local/x-ui/bin/config.json "$STAGING/meta/xray-config.json" 2>/dev/null || true
cp -a /etc/x-ui/x-ui.db "$STAGING/meta/x-ui.db" || true
ss -lntp > "$STAGING/meta/listeners.txt" || true
systemctl status x-ui --no-pager -l > "$STAGING/meta/x-ui-status.txt" 2>&1 || true
systemctl status nginx --no-pager -l > "$STAGING/meta/nginx-status.txt" 2>&1 || true
systemctl status ssh --no-pager -l > "$STAGING/meta/ssh-status.txt" 2>&1 || true
python3 - <<'PY'
import sqlite3, json
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
cur=con.cursor()
rows=[]
for r in cur.execute('select id,remark,port,protocol,enable,settings from inbounds'):
    settings=json.loads(r['settings'])
    clients=[{{'email':c.get('email'),'enable':c.get('enable'),'flow':c.get('flow','')}} for c in (settings.get('clients') or [])]
    rows.append({{'id':r['id'],'remark':r['remark'],'port':r['port'],'protocol':r['protocol'],'enable':r['enable'],'clients':clients}})
open('/root/mars-backups/{BAK_NAME}/meta/clients-safe.json','w').write(json.dumps(rows, indent=2))
con.close()
PY
tar -C /root/mars-backups -czf {REMOTE_BAK} {BAK_NAME}
sha256sum {REMOTE_BAK} | tee {REMOTE_BAK}.sha256
ls -la {REMOTE_BAK}
"""
    code, out, err = run(c, remote_script, timeout=240)
    write("B0-backup-remote.txt", redact(out + "\n" + err))
    if code != 0:
        raise SystemExit(f"BACKUP_FAIL code={code}")

    # sftp pull
    sftp = c.open_sftp()
    sftp.get(REMOTE_BAK, str(LOCAL_BAK))
    try:
        sftp.get(f"{REMOTE_BAK}.sha256", str(LOCAL_BAK) + ".sha256")
    except Exception:
        pass
    sftp.close()

    remote_sha = ""
    m = re.search(r"([0-9a-f]{64})\s+" + re.escape(REMOTE_BAK), out)
    if m:
        remote_sha = m.group(1)
    local_sha = sha256_file(LOCAL_BAK)
    members_ok = {
        "etc-x-ui": False,
        "x-ui-db": False,
        "usr-local-x-ui": False,
        "xray-config": False,
        "clients-safe": False,
    }
    member_list = []
    with tarfile.open(LOCAL_BAK, "r:gz") as tf:
        names = tf.getnames()
        member_list = names[:300]
        joined = "\n".join(names)
        members_ok["etc-x-ui"] = "etc/x-ui" in joined
        members_ok["x-ui-db"] = "x-ui.db" in joined
        members_ok["usr-local-x-ui"] = "usr-local/x-ui" in joined
        members_ok["xray-config"] = "xray-config.json" in joined
        members_ok["clients-safe"] = "clients-safe.json" in joined
    write("B1-backup-local-members.txt", "\n".join(member_list))
    info = {
        "ok": bool(remote_sha)
        and remote_sha == local_sha
        and LOCAL_BAK.stat().st_size > 0
        and all(members_ok.values()),
        "remote": REMOTE_BAK,
        "local": str(LOCAL_BAK),
        "remote_sha256": remote_sha,
        "local_sha256": local_sha,
        "sha_match": remote_sha == local_sha,
        "size": LOCAL_BAK.stat().st_size,
        "members_ok": members_ok,
    }
    write("B1-backup-validation.json", json.dumps(info, indent=2))
    restore = f"""# Restore strategy — {BAK_NAME}
# inventory_ref: FRIENDHOSTING-DE
# created: {TS}
# remote: {REMOTE_BAK}
# local: {LOCAL_BAK}
# sha256: {local_sha}
# sha_match: {info['sha_match']}

## Scope
Pre-mutation P3 checkpoint covering:
- /etc/x-ui (panel DB)
- /usr/local/x-ui (panel + generated Xray)
- meta/x-ui.db + meta/xray-config.json + meta/clients-safe.json
- nginx, letsencrypt, ufw, fail2ban, ssh snapshots (same class as P2)

Does NOT restore RAM/kernel/disk/provider panel.
Does NOT auto-apply later client additions made after this backup.

## Procedure (human-operated)
1. STOP active mutation; confirm charter rollback section.
2. Copy archive: scp -P 3333 {BAK_NAME}.tgz root@{HOST}:/root/mars-backups/
3. Verify: sha256sum -c {BAK_NAME}.tgz.sha256
4. Extract staging: tar -C /root/mars-backups -xzf /root/mars-backups/{BAK_NAME}.tgz
5. Review diffs (esp. x-ui.db, xray config, nginx, sshd, ufw).
6. Restore scoped trees from staging after review.
7. nginx -t && systemctl reload nginx; systemctl restart x-ui
8. Validate: SSH :3333, nginx :443, Xray :8443, legacy client {LEGACY_EMAIL} present.
9. File evidence under evidence/FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01/

## Post-restore validation
- ssh key login root on :3333
- systemctl is-active x-ui nginx ssh
- TLS :8443 OK
- inbound :8443 still VLESS+TLS+RAW; SNI {DOMAIN}
- legacy fallback client still enabled
"""
    write("B1-RESTORE-STRATEGY.md", restore)
    (BASE / "backups" / f"{BAK_NAME}-RESTORE-STRATEGY.md").write_text(
        restore, encoding="utf-8"
    )
    RESULT["gates"]["backup"] = {
        "ok": info["ok"],
        "sha_match": info["sha_match"],
        "size": info["size"],
        "local": info["local"],
        "remote": info["remote"],
    }
    if not info["ok"]:
        raise SystemExit("BACKUP_VALIDATION_FAIL")
    return info


def phase_add_clients(c: paramiko.SSHClient) -> dict:
    # Build client specs locally (UUIDs never written to EV/git evidence)
    specs = []
    for folder, email, eqvps, is_ws in NEW_DEVICES:
        specs.append(
            {
                "folder": folder,
                "email": email,
                "eqvps_map": eqvps,
                "is_current_workstation": is_ws,
                "id": str(uuid.uuid4()),
                "flow": "",
                "enable": True,
                "limitIp": 0,
                "totalGB": 0,
                "expiryTime": 0,
                "tgId": "",
                "subId": sub_id_for(email),
                "comment": "P3 per-device; LEGACY MCA-ONE preserved",
                "reset": 0,
            }
        )

    # uniqueness among new
    ids = [s["id"] for s in specs]
    emails = [s["email"] for s in specs]
    assert len(ids) == len(set(ids)), "UUID_COLLISION_NEW"
    assert len(emails) == len(set(emails)), "EMAIL_COLLISION_NEW"
    assert LEGACY_EMAIL not in emails, "LEGACY_EMAIL_COLLISION"

    # Push mutation via remote python reading JSON over stdin (base64)
    payload = json.dumps(
        {
            "legacy_email": LEGACY_EMAIL,
            "new_clients": [
                {
                    "id": s["id"],
                    "flow": s["flow"],
                    "email": s["email"],
                    "limitIp": s["limitIp"],
                    "totalGB": s["totalGB"],
                    "expiryTime": s["expiryTime"],
                    "enable": s["enable"],
                    "tgId": s["tgId"],
                    "subId": s["subId"],
                    "comment": s["comment"],
                    "reset": s["reset"],
                }
                for s in specs
            ],
        }
    )
    # write payload to remote temp via sftp (not echoed)
    remote_payload = f"/root/mars-backups/{BAK_NAME}-p3-clients.json"
    sftp = c.open_sftp()
    with sftp.file(remote_payload, "w") as rf:
        rf.write(payload)
    sftp.close()

    code, out, err = run(
        c,
        f"""
set -euo pipefail
python3 - <<'PY'
import json, sqlite3, sys
from pathlib import Path
payload=json.loads(Path({remote_payload!r}).read_text())
legacy=payload['legacy_email']
new_clients=payload['new_clients']
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
cur=con.cursor()
rows=cur.execute("select id,remark,port,protocol,enable,settings,stream_settings,sniffing from inbounds where port=8443").fetchall()
if len(rows)!=1:
    print('ERR_INBOUND_COUNT', len(rows))
    sys.exit(2)
row=rows[0]
settings=json.loads(row['settings'])
stream=json.loads(row['stream_settings'] or '{{}}')
clients=settings.get('clients') or []
existing_emails={{c.get('email') for c in clients}}
existing_ids={{c.get('id') for c in clients}}
if legacy not in existing_emails:
    print('ERR_LEGACY_MISSING')
    sys.exit(3)
# refuse architecture drift
if stream.get('network') not in ('tcp','raw'):
    print('ERR_NETWORK', stream.get('network'))
    sys.exit(4)
if stream.get('security')!='tls':
    print('ERR_SECURITY', stream.get('security'))
    sys.exit(5)
tls=(stream.get('tlsSettings') or {{}})
sni=tls.get('serverName') or ''
if sni and sni!='metacode-cloud.com':
    print('ERR_SNI', sni)
    sys.exit(6)
added=[]
skipped=[]
for nc in new_clients:
    if nc['email'] in existing_emails:
        skipped.append(nc['email'])
        continue
    if nc['id'] in existing_ids:
        print('ERR_UUID_COLLISION_WITH_EXISTING')
        sys.exit(7)
    clients.append(nc)
    existing_emails.add(nc['email'])
    existing_ids.add(nc['id'])
    added.append(nc['email'])
settings['clients']=clients
cur.execute('update inbounds set settings=? where id=?', (json.dumps(settings, ensure_ascii=False), row['id']))
con.commit()
con.close()
print('ADDED', len(added))
for e in added:
    print('ADDED_EMAIL', e)
print('SKIPPED', len(skipped))
for e in skipped:
    print('SKIPPED_EMAIL', e)
print('TOTAL_CLIENTS', len(clients))
print('LEGACY_OK', legacy in existing_emails)
# wipe payload secrets on disk
Path({remote_payload!r}).unlink(missing_ok=True)
print('PAYLOAD_WIPED')
PY
systemctl restart x-ui
sleep 3
systemctl is-active x-ui
ss -lntp | egrep ':(8443|20901)\\b' || true
""",
        timeout=120,
    )
    write("C1-add-clients.txt", redact(out + "\n" + err))
    if code != 0 or "ERR_" in out:
        raise SystemExit(f"ADD_CLIENTS_FAIL code={code}")
    RESULT["mutations"].append("add_clients_to_8443_inbound")
    RESULT["gates"]["add"] = {
        "added": int(re.search(r"ADDED (\d+)", out).group(1)) if re.search(r"ADDED (\d+)", out) else 0,
        "total": int(re.search(r"TOTAL_CLIENTS (\d+)", out).group(1))
        if re.search(r"TOTAL_CLIENTS (\d+)", out)
        else None,
        "legacy_ok": "LEGACY_OK True" in out,
        "xui_restart": "active" in out.splitlines()[-5:],
    }
    return {"specs": specs, "remote_out": out}


def write_local_profiles(specs: list) -> dict:
    registry = {
        "wave": "P3",
        "ts": TS,
        "inbound": {
            "server": DOMAIN,
            "port": VPN_PORT,
            "protocol": "vless",
            "security": "tls",
            "transport": "tcp/raw",
            "sni": DOMAIN,
            "flow": "empty",
        },
        "legacy_fallback": {
            "email": LEGACY_EMAIL,
            "status": "LEGACY-FALLBACK / MIGRATION SAFETY NET",
            "path": str(CLIENTS_ROOT / "MCA-ONE"),
            "delete_in_p3": False,
        },
        "devices": [],
    }
    validation = []
    for s in specs:
        ddir = CLIENTS_ROOT / s["folder"]
        ddir.mkdir(parents=True, exist_ok=True)
        remarks = s["email"]
        # v2rayN-style JSON (local secret)
        profile = {
            "remarks": remarks,
            "address": DOMAIN,
            "port": VPN_PORT,
            "protocol": "vless",
            "id": s["id"],
            "encryption": "none",
            "flow": "",
            "network": "tcp",
            "headerType": "none",
            "security": "tls",
            "sni": DOMAIN,
            "alpn": "http/1.1",
            "fp": "chrome",
            "mux": False,
            "allowInsecure": False,
        }
        json_path = ddir / "friendhosting-de-raw-8443.json"
        vless_path = ddir / "friendhosting-de-raw-8443.vless.txt"
        meta_path = ddir / "meta.local.json"
        json_path.write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8")
        # VLESS URI (local secret) — flow empty, security=tls, type=tcp
        uri = (
            f"vless://{s['id']}@{DOMAIN}:{VPN_PORT}"
            f"?encryption=none&security=tls&sni={DOMAIN}&alpn=http%2F1.1&fp=chrome"
            f"&type=tcp&headerType=none#{remarks}"
        )
        vless_path.write_text(uri + "\n", encoding="utf-8")
        meta = {
            "device": s["folder"],
            "display_name": remarks,
            "eqvps_map": s["eqvps_map"],
            "is_current_workstation": s["is_current_workstation"],
            "status": "PROFILE_READY / SERVER_CLIENT_CREATED / DEVICE_TEST_PENDING"
            if not s["is_current_workstation"]
            else "PROFILE_READY / SERVER_CLIENT_CREATED / CURRENT_WORKSTATION_SMOKE_PENDING",
            "legacy_fallback_preserved": LEGACY_EMAIL,
            "architecture": "VLESS+TLS+RAW :8443",
            "created_ts": TS,
            "files": [json_path.name, vless_path.name],
        }
        meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

        # structural validation without exposing UUID
        checks = {
            "device": s["folder"],
            "display_name": remarks,
            "server": profile["address"] == DOMAIN,
            "port": profile["port"] == VPN_PORT,
            "protocol": profile["protocol"] == "vless",
            "security": profile["security"] == "tls",
            "transport_tcp": profile["network"] == "tcp",
            "sni": profile["sni"] == DOMAIN,
            "flow_empty": profile["flow"] == "",
            "uuid_present": bool(profile["id"]) and len(profile["id"]) == 36,
            "reality_absent": "reality" not in json.dumps(profile).lower(),
            "ws_absent": profile["network"] != "ws",
            "grpc_absent": profile["network"] != "grpc",
            "xhttp_absent": profile["network"] != "xhttp",
            "json_path": str(json_path),
            "vless_path": str(vless_path),
        }
        checks["struct_pass"] = all(
            checks[k]
            for k in (
                "server",
                "port",
                "protocol",
                "security",
                "transport_tcp",
                "sni",
                "flow_empty",
                "uuid_present",
                "reality_absent",
            )
        )
        validation.append(checks)
        registry["devices"].append(
            {
                "device": s["folder"],
                "display_name": remarks,
                "eqvps_map": s["eqvps_map"],
                "is_current_workstation": s["is_current_workstation"],
                "status": meta["status"],
                "dir": str(ddir),
            }
        )

    # UUID uniqueness among new + vs legacy local file if readable
    new_ids = {s["id"] for s in specs}
    assert len(new_ids) == len(specs)
    legacy_json = CLIENTS_ROOT / "MCA-ONE" / "friendhosting-de-raw-8443.json"
    if legacy_json.exists():
        try:
            leg = json.loads(legacy_json.read_text(encoding="utf-8"))
            lid = leg.get("id")
            if lid and lid in new_ids:
                raise SystemExit("UUID_COLLISION_WITH_LEGACY_LOCAL")
        except json.JSONDecodeError:
            RESULT["notes"].append("legacy_json_parse_warn")

    registry_path = CLIENTS_ROOT / "REGISTRY.local.json"
    registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    write(
        "C2-profile-validation.json",
        json.dumps(
            {
                "all_pass": all(v["struct_pass"] for v in validation),
                "uuid_unique_among_new": True,
                "profiles": [
                    {k: v[k] for k in v if k not in ()}
                    for v in validation
                ],
            },
            indent=2,
        ),
    )
    write(
        "C2-registry-safe.json",
        json.dumps(registry, indent=2),
    )
    return {"registry": registry, "validation": validation, "specs": specs}


def phase_post_regression(c: paramiko.SSHClient) -> dict:
    code, out, err = run(
        c,
        r"""
set +e
echo XUI=$(systemctl is-active x-ui)
ss -lntp | egrep ':(3333|443|8443|20901|80)\b' || true
curl -s -o /dev/null -w 'LOCAL_XUI_HTTP=%{http_code}\n' http://127.0.0.1:20901/ || true
ss -lntp | grep -q '127.0.0.1:20901' && echo LOCAL_XUI_LISTEN=YES || echo LOCAL_XUI_LISTEN=NO
python3 - <<'PY'
import sqlite3, json
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
cur=con.cursor()
row=cur.execute("select remark,port,protocol,enable,settings,stream_settings,sniffing from inbounds where port=8443").fetchone()
settings=json.loads(row['settings'])
stream=json.loads(row['stream_settings'] or '{}')
sniff=json.loads(row['sniffing'] or '{}')
clients=settings.get('clients') or []
print('REMARK', row['remark'])
print('PORT', row['port'])
print('PROTOCOL', row['protocol'])
print('ENABLE', row['enable'])
print('NETWORK', stream.get('network'))
print('SECURITY', stream.get('security'))
print('SNI', (stream.get('tlsSettings') or {}).get('serverName'))
print('SNIFF_ENABLED', sniff.get('enabled'))
print('CLIENTS_N', len(clients))
for c in clients:
    print('CLIENT', c.get('email'), 'enable='+str(c.get('enable')), 'flow='+repr(c.get('flow','')), 'has_id='+str(bool(c.get('id'))))
ids=[c.get('id') for c in clients]
print('UUID_UNIQUE', len(ids)==len(set(ids)))
con.close()
# also confirm generated config has same emails (no uuid dump)
j=json.load(open('/usr/local/x-ui/bin/config.json'))
inbounds=j.get('inbounds') or []
for ib in inbounds:
    if ib.get('port')==8443:
        cs=((ib.get('settings') or {}).get('clients') or [])
        print('XRAY_CLIENTS_N', len(cs))
        for c in cs:
            print('XRAY_CLIENT_EMAIL', c.get('email'))
PY
""",
        timeout=60,
    )
    write("D0-post-regression.txt", redact(out + "\n" + err))
    gates = {
        "ssh_tcp": tcp(3333),
        "nginx_tcp": tcp(443),
        "xray_tcp": tcp(8443),
        "tls_8443": tls(8443).get("ok"),
        "xui_active": "XUI=active" in out,
        "legacy_enabled": f"{LEGACY_EMAIL} enable=True" in out or f"{LEGACY_EMAIL} enable=true" in out,
        "uuid_unique": "UUID_UNIQUE True" in out,
        "network_tcp": "NETWORK tcp" in out or "NETWORK raw" in out,
        "security_tls": "SECURITY tls" in out,
        "sni_ok": f"SNI {DOMAIN}" in out or "SNI metacode-cloud.com" in out,
    }
    # all new emails present
    for _, email, _, _ in NEW_DEVICES:
        gates[f"present_{email}"] = email in out
    gates["all_new_present"] = all(gates[f"present_{e}"] for _, e, _, _ in NEW_DEVICES)
    RESULT["gates"]["post"] = gates
    write("D0-post-regression-gates.json", json.dumps(gates, indent=2))
    return gates


def main() -> int:
    print("P3 START", TS)
    c = connect("root")
    try:
        health = phase_health(c)
        if not health.get("critical_pass"):
            write("STOP-health-fail.json", json.dumps(health, indent=2, default=str))
            print("STOP — PRE-MUTATION HEALTH FAIL")
            return 2
        print("HEALTH PASS")
        bak = phase_backup(c)
        print("BACKUP PASS", bak["sha_match"], bak["size"])
        added = phase_add_clients(c)
        print("CLIENTS ADDED", RESULT["gates"]["add"])
        local = write_local_profiles(added["specs"])
        print("LOCAL PROFILES", len(local["validation"]))
        post = phase_post_regression(c)
        print("POST", {k: post[k] for k in post if not k.startswith("present_")})
        # workstation path
        ws = next(s for s in added["specs"] if s["is_current_workstation"])
        summary = {
            "ts": TS,
            "health_critical": health["critical_pass"],
            "backup_ok": bak["ok"],
            "sha_match": bak["sha_match"],
            "backup_local": str(LOCAL_BAK),
            "backup_remote": REMOTE_BAK,
            "new_clients_added": RESULT["gates"]["add"]["added"],
            "legacy_preserved": RESULT["gates"]["add"]["legacy_ok"] and post.get("legacy_enabled"),
            "post_all_new_present": post.get("all_new_present"),
            "post_uuid_unique": post.get("uuid_unique"),
            "workstation_display": ws["email"],
            "workstation_json": str(CLIENTS_ROOT / ws["folder"] / "friendhosting-de-raw-8443.json"),
            "workstation_vless": str(CLIENTS_ROOT / ws["folder"] / "friendhosting-de-raw-8443.vless.txt"),
            "operator_smoke": "PENDING",
            "architecture_mutation": 0,
        }
        write("Z-summary.json", json.dumps(summary, indent=2))
        RESULT["summary"] = summary
        write("Z-result-safe.json", json.dumps({k: RESULT[k] for k in RESULT if k != "summary"} | {"summary": summary}, indent=2))
        print("SUMMARY_WRITTEN")
        print("WORKSTATION_NEW_DISPLAY", ws["email"])
        print("WORKSTATION_NEW_PATH", summary["workstation_json"])
        return 0 if post.get("all_new_present") and post.get("uuid_unique") and post.get("legacy_enabled") else 3
    finally:
        try:
            c.close()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
