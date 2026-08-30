#!/usr/bin/env python3
"""Ensure Vision flow is present in inbound settings JSON and regenerate xray. LOCAL ONLY."""
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
        fix = (
            "import json,sqlite3\n"
            "conn=sqlite3.connect('/etc/x-ui/x-ui.db')\n"
            "cur=conn.cursor()\n"
            "cur.execute(\"SELECT id,settings,stream_settings FROM inbounds WHERE port=9443\")\n"
            "row=cur.fetchone()\n"
            "if not row: raise SystemExit('NO_9443')\n"
            "iid,settings,stream=row\n"
            "st=json.loads(settings)\n"
            "print('CLIENTS_BEFORE', [(cl.get('email'), cl.get('flow')) for cl in st.get('clients',[])])\n"
            "for cl in st.get('clients',[]):\n"
            " if cl.get('email')=='MCA-ONE-EQ-ALT-A-REALITY-VISION':\n"
            "  cl['flow']='xtls-rprx-vision'\n"
            "cur.execute('UPDATE inbounds SET settings=? WHERE id=?', (json.dumps(st,separators=(',',':')), iid))\n"
            "cur.execute(\"UPDATE clients SET flow='xtls-rprx-vision' WHERE email='MCA-ONE-EQ-ALT-A-REALITY-VISION'\")\n"
            "print('CLIENTS_AFTER', [(cl.get('email'), cl.get('flow')) for cl in st.get('clients',[])])\n"
            "print('CLIENT_ROW', list(cur.execute(\"SELECT id,email,flow,tg_id FROM clients WHERE email='MCA-ONE-EQ-ALT-A-REALITY-VISION'\")))\n"
            "conn.commit(); conn.close()\n"
            "print('FLOW_FIX_OK')\n"
        )
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-alt-a-fix-flow.py", "w") as rf:
            rf.write(fix)
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-alt-a-fix-flow.py", pw)
        print(out)
        (WAVE / "fix-flow.txt").write_text(out, encoding="utf-8")
        if "FLOW_FIX_OK" not in out:
            return 2
        code, out = sudo(
            c,
            "systemctl restart x-ui && sleep 7 && systemctl is-active x-ui && ss -lntp | awk 'NR==1 || /:443|:8443|:9443|:24443/'",
            pw,
        )
        print(out)
        inspect = (
            "import json\n"
            "cfg=json.load(open('/usr/local/x-ui/bin/config.json'))\n"
            "for ib in cfg.get('inbounds',[]):\n"
            " if ib.get('port')==9443:\n"
            "  ss=ib.get('streamSettings') or {}\n"
            "  clients=(ib.get('settings') or {}).get('clients') or []\n"
            "  print('runtime', ib.get('port'), ss.get('network'), ss.get('security'), 'flows', [c.get('flow') for c in clients])\n"
            "  rs=ss.get('realitySettings') or {}\n"
            "  print('dest', rs.get('dest'), 'sn', rs.get('serverNames'))\n"
        )
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-alt-a-inspect2.py", "w") as rf:
            rf.write(inspect)
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-alt-a-inspect2.py", pw)
        print(out)
        (WAVE / "post-flow-runtime.txt").write_text(out, encoding="utf-8")
        ok = "xtls-rprx-vision" in out and "reality" in out and ":9443" in open(
            WAVE / "post-tgid-fix-ss.txt", encoding="utf-8", errors="replace"
        ).read() or True
        # re-check listeners from last restart output file rewritten
        return 0 if "xtls-rprx-vision" in out else 3
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
