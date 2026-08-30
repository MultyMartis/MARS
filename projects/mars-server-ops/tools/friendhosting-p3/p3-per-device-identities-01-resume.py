#!/usr/bin/env python3
"""FriendHosting P3 resume — after clients already added on server.

1) Ensure x-ui/xray healthy
2) Export per-device local profiles from live DB (secrets local-only)
3) Post regression (safe)
Does not re-add clients; does not delete legacy.
"""
from __future__ import annotations

import json
import re
import socket
import ssl
import urllib.request
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
OUT = BASE / f"p3-per-device-identities-01-resume-{TS}"
LEGACY_EMAIL = "MCA-ONE-FRIENDHOSTING-DE-RAW-8443"

# display email -> (folder, eqvps_map, is_ws)
DEVICE_MAP = {
    "WSP-ONE-FRIENDHOSTING-DE-RAW-8443": ("WSP-ONE", "MCA-ONE", True),
    "MCA-PHONE-FRIENDHOSTING-DE-RAW-8443": ("MCA-PHONE", "MCA-PHONE", False),
    "Unit-01-FRIENDHOSTING-DE-RAW-8443": ("Unit-01", "Unit-01", False),
    "Unit-02-FRIENDHOSTING-DE-RAW-8443": ("Unit-02", "Unit-02", False),
    "Unit-03-FRIENDHOSTING-DE-RAW-8443": ("Unit-03", "Unit-03", False),
    "Unit-MichaelPhone-FRIENDHOSTING-DE-RAW-8443": (
        "Unit-MichaelPhone",
        "Unit-MichaelPhone",
        False,
    ),
}

OUT.mkdir(parents=True, exist_ok=True)
EV.mkdir(parents=True, exist_ok=True)


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
        port=PORT,
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


def run(c, cmd, timeout=120):
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


def main() -> int:
    print("P3 RESUME", TS)
    c = connect()
    try:
        # ensure x-ui running / regenerate config
        code, out, err = run(
            c,
            r"""
set +e
systemctl is-active x-ui || systemctl restart x-ui
sleep 2
systemctl restart x-ui
sleep 3
echo XUI=$(systemctl is-active x-ui)
ss -lntp | egrep ':(8443|20901|443|3333)\b' || true
""",
            timeout=60,
        )
        write("R0-xui-restart.txt", redact(out + "\n" + err))
        if "XUI=active" not in out:
            print("XUI_NOT_ACTIVE")
            return 2

        # export clients JSON to remote temp then sftp (secret)
        remote_json = f"/root/mars-backups/p3-clients-export-{TS}.json"
        code, out, err = run(
            c,
            f"""
python3 - <<'PY'
import json, sqlite3
from pathlib import Path
con=sqlite3.connect('/etc/x-ui/x-ui.db')
con.row_factory=sqlite3.Row
cur=con.cursor()
row=cur.execute("select remark,port,protocol,enable,settings,stream_settings,sniffing from inbounds where port=8443").fetchone()
settings=json.loads(row['settings'])
stream=json.loads(row['stream_settings'] or '{{}}')
sniff=json.loads(row['sniffing'] or '{{}}')
export={{
  'inbound': {{
    'remark': row['remark'],
    'port': row['port'],
    'protocol': row['protocol'],
    'enable': row['enable'],
    'network': stream.get('network'),
    'security': stream.get('security'),
    'sni': (stream.get('tlsSettings') or {{}}).get('serverName'),
    'sniff_enabled': sniff.get('enabled'),
  }},
  'clients': settings.get('clients') or [],
}}
Path({remote_json!r}).write_text(json.dumps(export))
# safe summary to stdout
print('CLIENTS_N', len(export['clients']))
print('NETWORK', export['inbound']['network'])
print('SECURITY', export['inbound']['security'])
print('SNI', export['inbound']['sni'])
print('SNIFF', export['inbound']['sniff_enabled'])
for cl in export['clients']:
    print('CLIENT', cl.get('email'), 'enable='+str(cl.get('enable')), 'flow='+repr(cl.get('flow','')), 'has_id='+str(bool(cl.get('id'))))
ids=[cl.get('id') for cl in export['clients']]
print('UUID_UNIQUE', len(ids)==len(set(ids)))
# xray config emails
j=json.load(open('/usr/local/x-ui/bin/config.json'))
for ib in j.get('inbounds') or []:
    if ib.get('port')==8443:
        for cl in (ib.get('settings') or {{}}).get('clients') or []:
            print('XRAY_EMAIL', cl.get('email'))
PY
""",
            timeout=60,
        )
        write("R1-export-safe.txt", redact(out + "\n" + err))
        if code != 0:
            print("EXPORT_FAIL", code)
            return 3

        local_export = OUT / "clients-export.SECRET.json"
        sftp = c.open_sftp()
        sftp.get(remote_json, str(local_export))
        run(c, f"rm -f {remote_json}")
        sftp.close()

        export = json.loads(local_export.read_text(encoding="utf-8"))
        clients = export["clients"]
        emails = {cl.get("email") for cl in clients}
        if LEGACY_EMAIL not in emails:
            print("LEGACY_MISSING")
            return 4
        missing = [e for e in DEVICE_MAP if e not in emails]
        if missing:
            print("MISSING", missing)
            return 5

        validation = []
        registry = {
            "wave": "P3",
            "ts": TS,
            "inbound": export["inbound"],
            "legacy_fallback": {
                "email": LEGACY_EMAIL,
                "status": "LEGACY-FALLBACK / MIGRATION SAFETY NET",
                "path": str(CLIENTS_ROOT / "MCA-ONE"),
                "delete_in_p3": False,
            },
            "devices": [],
        }

        for cl in clients:
            email = cl.get("email")
            if email not in DEVICE_MAP:
                if email == LEGACY_EMAIL:
                    continue
                registry.setdefault("other_clients", []).append(email)
                continue
            folder, eqvps, is_ws = DEVICE_MAP[email]
            ddir = CLIENTS_ROOT / folder
            ddir.mkdir(parents=True, exist_ok=True)
            profile = {
                "remarks": email,
                "address": DOMAIN,
                "port": VPN_PORT,
                "protocol": "vless",
                "id": cl["id"],
                "encryption": "none",
                "flow": cl.get("flow") or "",
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
            uri = (
                f"vless://{cl['id']}@{DOMAIN}:{VPN_PORT}"
                f"?encryption=none&security=tls&sni={DOMAIN}&alpn=http%2F1.1&fp=chrome"
                f"&type=tcp&headerType=none#{email}"
            )
            vless_path.write_text(uri + "\n", encoding="utf-8")
            status = (
                "PROFILE_READY / SERVER_CLIENT_CREATED / CURRENT_WORKSTATION_SMOKE_PENDING"
                if is_ws
                else "PROFILE_READY / SERVER_CLIENT_CREATED / DEVICE_TEST_PENDING"
            )
            meta_path.write_text(
                json.dumps(
                    {
                        "device": folder,
                        "display_name": email,
                        "eqvps_map": eqvps,
                        "is_current_workstation": is_ws,
                        "status": status,
                        "legacy_fallback_preserved": LEGACY_EMAIL,
                        "architecture": "VLESS+TLS+RAW :8443",
                        "created_ts": TS,
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            checks = {
                "device": folder,
                "display_name": email,
                "server": profile["address"] == DOMAIN,
                "port": profile["port"] == VPN_PORT,
                "protocol": profile["protocol"] == "vless",
                "security": profile["security"] == "tls",
                "transport_tcp": profile["network"] == "tcp",
                "sni": profile["sni"] == DOMAIN,
                "flow_empty": profile["flow"] == "",
                "uuid_present": bool(profile["id"]) and len(profile["id"]) == 36,
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
                )
            )
            validation.append(checks)
            registry["devices"].append(
                {
                    "device": folder,
                    "display_name": email,
                    "eqvps_map": eqvps,
                    "is_current_workstation": is_ws,
                    "status": status,
                    "dir": str(ddir),
                }
            )

        # uniqueness vs legacy local
        new_ids = {
            json.loads((CLIENTS_ROOT / DEVICE_MAP[e][0] / "friendhosting-de-raw-8443.json").read_text())[
                "id"
            ]
            for e in DEVICE_MAP
        }
        assert len(new_ids) == len(DEVICE_MAP)
        legacy_json = CLIENTS_ROOT / "MCA-ONE" / "friendhosting-de-raw-8443.json"
        if legacy_json.exists():
            lid = json.loads(legacy_json.read_text()).get("id")
            if lid in new_ids:
                raise SystemExit("UUID_COLLISION_LEGACY")

        (CLIENTS_ROOT / "REGISTRY.local.json").write_text(
            json.dumps(registry, indent=2) + "\n", encoding="utf-8"
        )
        write(
            "R2-profile-validation.json",
            json.dumps({"all_pass": all(v["struct_pass"] for v in validation), "profiles": validation}, indent=2),
        )
        write("R2-registry-safe.json", json.dumps(registry, indent=2))

        gates = {
            "ssh_tcp": tcp(3333),
            "nginx_tcp": tcp(443),
            "xray_tcp": tcp(8443),
            "tls_8443": tls_ok(8443),
            "legacy_present": LEGACY_EMAIL in emails,
            "uuid_unique": "UUID_UNIQUE True" in out,
            "all_new_present": all(e in emails for e in DEVICE_MAP),
            "profiles_pass": all(v["struct_pass"] for v in validation),
        }
        write("R3-post-gates.json", json.dumps(gates, indent=2))
        ws_email = "WSP-ONE-FRIENDHOSTING-DE-RAW-8443"
        summary = {
            "ts": TS,
            "gates": gates,
            "new_identities": len(DEVICE_MAP),
            "total_clients_server": len(clients),
            "workstation_display": ws_email,
            "workstation_json": str(CLIENTS_ROOT / "WSP-ONE" / "friendhosting-de-raw-8443.json"),
            "workstation_vless": str(CLIENTS_ROOT / "WSP-ONE" / "friendhosting-de-raw-8443.vless.txt"),
            "operator_smoke": "PENDING",
            "backup_local": str(
                BASE
                / "backups"
                / "friendhosting-p3-pre-device-identities-20260830T105341Z.tgz"
            ),
            "backup_remote": "/root/mars-backups/friendhosting-p3-pre-device-identities-20260830T105341Z.tgz",
        }
        write("Z-summary.json", json.dumps(summary, indent=2))
        print("RESUME_OK")
        print("WORKSTATION_NEW_DISPLAY", ws_email)
        print("WORKSTATION_NEW_PATH", summary["workstation_json"])
        print("GATES", gates)
        return 0 if all(gates.values()) else 6
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
