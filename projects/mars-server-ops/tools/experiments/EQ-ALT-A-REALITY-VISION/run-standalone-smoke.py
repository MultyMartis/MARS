#!/usr/bin/env python3
"""Standalone Reality smoke — split steps, normalize LF."""
from __future__ import annotations

import json
import re
from pathlib import Path

import paramiko

BASE = Path(r"X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP")
WAVE = BASE / "eqvps-alt-a-reality-vision-2026-08-29"
SECRETS = BASE / "secrets.local.md"
KEY = BASE / "ssh" / "marsops_ed25519"
HOST = "95.216.126.173"
REMOTE_BODY = Path(
    r"X:\AI MARS\projects\mars-server-ops\tools\experiments\EQ-ALT-A-REALITY-VISION\standalone-body.py"
)


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"marsops sudo password[^\n]*\n+```[^\n]*\n([^\n]+)\n```", text, re.I)
    return m.group(1).strip().strip("`")


def sudo(c, cmd: str, pw: str, timeout: int = 120):
    full = f"sudo -S -p '' bash -lc {json.dumps(cmd)}"
    stdin, stdout, stderr = c.exec_command(full, get_pty=True, timeout=timeout)
    stdin.write(pw + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = (stdout.read() + stderr.read()).decode("utf-8", "replace").replace(pw, "<REDACTED>")
    return stdout.channel.recv_exit_status(), out


def main() -> int:
    pw = load_pw()
    body = REMOTE_BODY.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        22,
        username="marsops",
        key_filename=str(KEY),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    try:
        sftp = c.open_sftp()
        with sftp.file("/home/marsops/mars-standalone-reality.py", "w") as rf:
            rf.write(body)
        sftp.close()
        print("uploaded")
        code, out = sudo(c, "python3 /home/marsops/mars-standalone-reality.py", pw, timeout=90)
        print("smoke code", code)
        safe = re.sub(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
            "[UUID]",
            out,
            flags=re.I,
        )
        print(safe[-4000:])
        (WAVE / "standalone-reality-smoke.txt").write_text(safe, encoding="utf-8")
        return 0 if f"EGRESS={HOST}" in out else 2
    finally:
        c.close()


if __name__ == "__main__":
    raise SystemExit(main())
