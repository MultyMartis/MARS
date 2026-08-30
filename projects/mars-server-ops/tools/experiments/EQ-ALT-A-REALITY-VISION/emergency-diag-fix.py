#!/usr/bin/env python3
"""Emergency diagnose/fix for EQ-ALT-A after listener loss. LOCAL ONLY."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
USER = "marsops"
XRAY_BIN = "/usr/local/x-ui/bin/xray-linux-amd64"


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    if not m:
        raise RuntimeError("sudo password parse failed")
    return m.group(1).strip().strip("`")


def connect():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST, 22, username=USER, key_filename=str(KEY), timeout=30, allow_agent=False, look_for_keys=False
    )
    return c


def sudo(c, cmd: str, pw: str, timeout: int = 180):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=timeout)
    stdin.write(pw + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return stdout.channel.recv_exit_status(), out


def main() -> int:
    action = sys.argv[1] if len(sys.argv) > 1 else "diagnose"
    pw = load_pw()
    c = connect()
    try:
        if action == "diagnose":
            cmds = [
                "systemctl is-active x-ui; ss -lntp",
                f"{XRAY_BIN} run -test -c /usr/local/x-ui/bin/config.json 2>&1 | tail -60",
                "journalctl -u x-ui -n 100 --no-pager",
                "python3 /dev/stdin <<'PY'\nimport json,sqlite3\nconn=sqlite3.connect('/etc/x-ui/x-ui.db')\nprint('DB', list(conn.execute('SELECT id,remark,port,enable,protocol FROM inbounds ORDER BY port')))\ncfg=json.load(open('/usr/local/x-ui/bin/config.json'))\nprint('CFG_PORTS', [(ib.get('port'), ib.get('protocol'), (ib.get('streamSettings') or {}).get('security')) for ib in cfg.get('inbounds',[])])\nPY",
            ]
            # avoid heredoc with sudo — upload inspect
            inspect = (
                "import json,sqlite3\n"
                "conn=sqlite3.connect('/etc/x-ui/x-ui.db')\n"
                "print('DB', list(conn.execute('SELECT id,remark,port,enable,protocol FROM inbounds ORDER BY port')))\n"
                "cfg=json.load(open('/usr/local/x-ui/bin/config.json'))\n"
                "print('CFG_PORTS', [(ib.get('port'), ib.get('protocol'), (ib.get('streamSettings') or {}).get('security'), (ib.get('streamSettings') or {}).get('network')) for ib in cfg.get('inbounds',[])])\n"
                "for ib in cfg.get('inbounds',[]):\n"
                " if ib.get('port')==9443:\n"
                "  print('IB9443_KEYS', sorted((ib.get('streamSettings') or {}).keys()))\n"
                "  rs=(ib.get('streamSettings') or {}).get('realitySettings') or {}\n"
                "  print('RS_KEYS', sorted(rs.keys()))\n"
                "  print('RS_DEST', rs.get('dest'), 'SN', rs.get('serverNames'), 'SID_N', len(rs.get('shortIds') or []))\n"
            )
            sftp = c.open_sftp()
            with sftp.file("/home/marsops/mars-alt-a-diag.py", "w") as rf:
                rf.write(inspect)
            sftp.close()
            for cmd in [
                "systemctl is-active x-ui; ss -lntp",
                f"{XRAY_BIN} run -test -c /usr/local/x-ui/bin/config.json 2>&1 | tail -80",
                "journalctl -u x-ui -n 120 --no-pager",
                "python3 /home/marsops/mars-alt-a-diag.py",
            ]:
                code, out = sudo(c, cmd, pw)
                print("====", cmd[:70], "code", code)
                print(out[-3500:])
                (WAVE / "diag-latest.txt").write_text(out, encoding="utf-8")
            return 0

        if action == "restart_xui":
            code, out = sudo(c, "systemctl restart x-ui && sleep 6 && systemctl is-active x-ui && ss -lntp", pw)
            print(out)
            return code

        if action == "rollback_inbound_only":
            # Remove only 9443 inbound + client link; keep backup available for full restore
            script = (
                "import sqlite3\n"
                "conn=sqlite3.connect('/etc/x-ui/x-ui.db')\n"
                "cur=conn.cursor()\n"
                "cur.execute(\"SELECT id FROM inbounds WHERE port=9443 OR remark='EQVPS-ALT-A-REALITY-VISION'\")\n"
                "ids=[r[0] for r in cur.fetchall()]\n"
                "print('INBOUND_IDS', ids)\n"
                "for iid in ids:\n"
                " cur.execute('DELETE FROM client_inbounds WHERE inbound_id=?', (iid,))\n"
                " cur.execute('DELETE FROM inbounds WHERE id=?', (iid,))\n"
                "cur.execute(\"SELECT id FROM clients WHERE email='MCA-ONE-EQ-ALT-A-REALITY-VISION'\")\n"
                "cids=[r[0] for r in cur.fetchall()]\n"
                "print('CLIENT_IDS', cids)\n"
                "for cid in cids:\n"
                " cur.execute('DELETE FROM client_inbounds WHERE client_id=?', (cid,))\n"
                " cur.execute('DELETE FROM clients WHERE id=?', (cid,))\n"
                "conn.commit(); conn.close()\n"
                "print('ROLLBACK_INBOUND_OK')\n"
            )
            sftp = c.open_sftp()
            with sftp.file("/home/marsops/mars-alt-a-rollback-inbound.py", "w") as rf:
                rf.write(script)
            sftp.close()
            code, out = sudo(c, "python3 /home/marsops/mars-alt-a-rollback-inbound.py", pw)
            print(out)
            if "ROLLBACK_INBOUND_OK" not in out:
                return 2
            code, out = sudo(
                c,
                "ufw status numbered | grep 9443 || true; ufw --force delete allow 9443/tcp || true; systemctl restart x-ui; sleep 6; systemctl is-active x-ui; ss -lntp | awk 'NR==1 || /:22|:443|:8443|:24443|:9443|:20901|:2096/'",
                pw,
            )
            print(out)
            (WAVE / "rollback-inbound-result.txt").write_text(out, encoding="utf-8")
            return 0 if ":8443" in out and ":443" in out else 3

        if action == "full_restore_from_backup":
            meta = json.loads((WAVE / "backup-meta.json").read_text(encoding="utf-8"))
            name = meta["backup_name"]
            remote = f"/root/mars-backups/{name}"
            cmds = f"""
set -e
systemctl stop x-ui
cp -a {remote}/etc-x-ui/. /etc/x-ui/
cp -a {remote}/config.json /usr/local/x-ui/bin/config.json
ufw --force delete allow 9443/tcp || true
systemctl start x-ui
sleep 6
systemctl is-active x-ui
ss -lntp | awk 'NR==1 || /:22|:443|:8443|:24443|:9443|:20901|:2096/'
echo FULL_RESTORE_DONE
"""
            # write remote script
            sftp = c.open_sftp()
            with sftp.file("/home/marsops/mars-alt-a-full-restore.sh", "w") as rf:
                rf.write(cmds)
            sftp.close()
            code, out = sudo(c, "bash /home/marsops/mars-alt-a-full-restore.sh", pw)
            print(out)
            (WAVE / "full-restore-result.txt").write_text(out, encoding="utf-8")
            return 0 if "FULL_RESTORE_DONE" in out and ":8443" in out else 4

        return 1
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
