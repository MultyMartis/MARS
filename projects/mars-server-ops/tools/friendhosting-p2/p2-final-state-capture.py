#!/usr/bin/env python3
from __future__ import annotations

import paramiko
from pathlib import Path

PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
EV = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01")


def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')


def main() -> None:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        "92.42.99.126",
        port=3333,
        username="root",
        pkey=load_key(),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    cmds = [
        "ss -lntp | egrep ':(80|443|3333|8443|2096|20901)\\b' || true",
        "free -h; swapon --show; grep -n swap /etc/fstab || true",
        "sshd -T 2>/dev/null | egrep 'passwordauthentication|permitrootlogin|pubkeyauthentication|^port '",
        "ufw status verbose",
        "systemctl is-enabled --quiet certbot.timer && echo certbot.timer=enabled; systemctl is-active certbot.timer",
        "openssl x509 -in /etc/letsencrypt/live/metacode-cloud.com/fullchain.pem -noout -dates -subject 2>/dev/null",
        "id marsops; getent passwd marsops; groups marsops",
        "test -f /etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf && echo HARDENING_DROPIN=yes; grep -v '^#' /etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf | sed '/^$/d'",
        "fail2ban-client status sshd 2>/dev/null | head -20",
        "ls -la /var/log/journal 2>/dev/null | head -3; grep SystemMaxUse /etc/systemd/journald.conf.d/* 2>/dev/null || grep SystemMaxUse /etc/systemd/journald.conf || true",
    ]
    chunks = []
    for cmd in cmds:
        stdin, stdout, stderr = c.exec_command(cmd, timeout=40)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        block = f"==== {cmd}\n{out}{err}"
        print(block)
        chunks.append(block)
    (EV / "R1-final-state.txt").write_text("\n".join(chunks), encoding="utf-8")
    c.close()


if __name__ == "__main__":
    main()
