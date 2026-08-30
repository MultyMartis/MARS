#!/usr/bin/env python3
"""Narrow TLS renew dry-run retry after recovery TimeoutError."""
from __future__ import annotations

import paramiko
from pathlib import Path

HOST = "92.42.99.126"
PORT = 3333
PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
EV = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01")


def load_key() -> paramiko.PKey:
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')


def main() -> int:
    key = load_key()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=PORT,
        username="root",
        pkey=key,
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    c.get_transport().set_keepalive(30)
    cmd = "bash -lc 'certbot renew --dry-run; echo DRY_EXIT:$?'"
    stdin, stdout, stderr = c.exec_command(cmd, timeout=420)
    stdout.channel.settimeout(420)
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    text = out + "\n" + err
    (EV / "R1-tls-retry2.txt").write_text(text, encoding="utf-8")
    print(text[-2000:])
    ok = ("Congratulations" in text) or ("The dry run was successful" in text) or ("DRY_EXIT:0" in text)
    print("CLASS", "PASS" if ok else "FAIL_OR_PARTIAL")
    c.close()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
