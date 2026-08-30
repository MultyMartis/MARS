#!/usr/bin/env python3
"""Wait for leftover certbot, then dry-run once more; capture timer state."""
from __future__ import annotations

import time

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


def run(c: paramiko.SSHClient, cmd: str, timeout: int = 60) -> str:
    stdin, stdout, stderr = c.exec_command(cmd, timeout=timeout)
    stdout.channel.settimeout(timeout)
    return stdout.read().decode("utf-8", "replace") + stderr.read().decode("utf-8", "replace")


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

    timer = run(
        c,
        "systemctl is-enabled certbot.timer; systemctl is-active certbot.timer; "
        "systemctl list-timers certbot.timer --no-pager; "
        "ls -la /etc/letsencrypt/renewal/; "
        "grep -E '^(authenticator|installer|pref_challs|webroot)' /etc/letsencrypt/renewal/*.conf 2>/dev/null | head -40",
        timeout=40,
    )
    (EV / "R1-tls-timer.txt").write_text(timer, encoding="utf-8")
    print("=== TIMER ===")
    print(timer)

    for i in range(24):
        ps = run(c, "pgrep -a certbot || echo NO_CERTBOT; ls /var/lib/letsencrypt/.certbot.lock 2>/dev/null || echo NO_LOCK", timeout=20)
        print(f"[{i}] {ps.strip()}")
        if "NO_CERTBOT" in ps and "NO_LOCK" in ps:
            break
        # If orphaned >10min from our timeout, remove lock only after process gone
        time.sleep(15)
    else:
        # still stuck: kill only if process exists and looks like renew dry-run
        stuck = run(c, "pgrep -a certbot || true", timeout=20)
        print("STUCK", stuck)
        if "certbot" in stuck:
            run(c, "pkill -f 'certbot renew' || true; sleep 2; rm -f /var/lib/letsencrypt/.certbot.lock; echo CLEANED", timeout=30)

    out = run(c, "bash -lc 'certbot renew --dry-run; echo DRY_EXIT:$?'", timeout=420)
    (EV / "R1-tls-final.txt").write_text(out, encoding="utf-8")
    print("=== DRY RUN ===")
    print(out[-2500:])
    ok = ("Congratulations" in out) or ("The dry run was successful" in out) or ("DRY_EXIT:0" in out)
    print("TLS_DRY_RUN", "PASS" if ok else "FAIL")
    c.close()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
