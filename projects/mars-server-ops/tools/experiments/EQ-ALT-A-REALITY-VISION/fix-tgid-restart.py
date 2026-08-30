#!/usr/bin/env python3
"""Fix tg_id type on EQ-ALT-A client and restart x-ui. LOCAL ONLY."""
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
            "import sqlite3\n"
            "conn=sqlite3.connect('/etc/x-ui/x-ui.db')\n"
            "cur=conn.cursor()\n"
            "print('SCHEMA', list(cur.execute('PRAGMA table_info(clients)')))\n"
            "print('BEFORE', list(cur.execute(\"SELECT id,email,tg_id,typeof(tg_id) FROM clients WHERE email='MCA-ONE-EQ-ALT-A-REALITY-VISION'\")))\n"
            # Prefer integer 0 for tg_id; also null empty strings elsewhere if needed
            "cur.execute(\"UPDATE clients SET tg_id=0 WHERE email='MCA-ONE-EQ-ALT-A-REALITY-VISION'\")\n"
            "print('AFTER', list(cur.execute(\"SELECT id,email,tg_id,typeof(tg_id) FROM clients WHERE email='MCA-ONE-EQ-ALT-A-REALITY-VISION'\")))\n"
            "conn.commit(); conn.close()\n"
            "print('TG_ID_FIX_OK')\n"
        )
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-alt-a-fix-tgid.py", "w") as rf:
            rf.write(fix)
        sftp.close()
        code, out = sudo(c, "python3 /home/marsops/mars-alt-a-fix-tgid.py", pw)
        print(out)
        (WAVE / "fix-tgid.txt").write_text(out, encoding="utf-8")
        if "TG_ID_FIX_OK" not in out:
            return 2
        code, out = sudo(
            c,
            "systemctl restart x-ui && sleep 7 && systemctl is-active x-ui && ss -lntp | awk 'NR==1 || /:22|:443|:8443|:24443|:9443|:20901|:2096/' && journalctl -u x-ui -n 20 --no-pager | tail -20",
            pw,
        )
        print(out)
        (WAVE / "post-tgid-fix-ss.txt").write_text(out, encoding="utf-8")
        ok = (
            ":8443" in out
            and ":443" in out
            and ":9443" in out
            and "Restart xray failed" not in out
            and "active" in out
        )
        print("RECOVERY_OK" if ok else "RECOVERY_INCOMPLETE")
        return 0 if ok else 3
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
