#!/usr/bin/env python3
"""Deep-inspect why 3X-UI drops Vision flow for 9443. LOCAL ONLY."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd: str, pw: str):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=180)
    stdin.write(pw + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return stdout.channel.recv_exit_status(), out


def main() -> int:
    pw = load_pw()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        "95.216.126.173",
        22,
        username="marsops",
        key_filename=str(KEY),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    try:
        script = (
            "import json,sqlite3\n"
            "conn=sqlite3.connect('/etc/x-ui/x-ui.db')\n"
            "cur=conn.cursor()\n"
            "print('IB_COLS', [r[1] for r in cur.execute('PRAGMA table_info(inbounds)')])\n"
            "cur.execute('SELECT * FROM inbounds WHERE port=9443')\n"
            "cols=[r[1] for r in cur.execute('PRAGMA table_info(inbounds)')]\n"
            "cur.execute('SELECT * FROM inbounds WHERE port=9443')\n"
            "row=cur.fetchone()\n"
            "d=dict(zip(cols,row))\n"
            "safe={k:d[k] for k in d if k not in ('settings','stream_settings','sniffing')}\n"
            "print('IB_SAFE', json.dumps(safe, default=str))\n"
            "print('DISABLE_FLOW', d.get('disable_flow'))\n"
            "st=json.loads(d['settings'])\n"
            "print('SETTINGS_CLIENT', json.dumps(st.get('clients'), indent=2)[:800])\n"
            "ci_cols=[r[1] for r in cur.execute('PRAGMA table_info(client_inbounds)')]\n"
            "print('CI_COLS', ci_cols)\n"
            "print('CI', list(cur.execute('SELECT * FROM client_inbounds WHERE inbound_id=?', (d['id'],))))\n"
            "cfg=json.load(open('/usr/local/x-ui/bin/config.json'))\n"
            "for ib in cfg.get('inbounds',[]):\n"
            " if ib.get('port')==9443:\n"
            "  print('CFG_CLIENT', json.dumps((ib.get('settings') or {}).get('clients'), indent=2)[:1000])\n"
            "conn.close()\n"
        )
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-alt-a-flow-deep.py", "w") as rf:
            rf.write(script)
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-alt-a-flow-deep.py", pw)
        # redact uuids
        out2 = re.sub(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
            "[UUID]",
            out,
            flags=re.I,
        )
        print(out2)
        (WAVE / "flow-deep.txt").write_text(out2, encoding="utf-8")
        return 0
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
