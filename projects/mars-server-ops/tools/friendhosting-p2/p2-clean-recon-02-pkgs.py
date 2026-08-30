#!/usr/bin/env python3
from pathlib import Path
import paramiko

PRIV = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\ssh\marsops_ed25519")
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02"
)
try:
    key = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
except Exception:
    key = paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(
    "92.42.99.126",
    port=3333,
    username="root",
    pkey=key,
    timeout=30,
    allow_agent=False,
    look_for_keys=False,
)
cmd = r"""
set +e
echo '===PKGS==='
apt list --upgradable 2>/dev/null | wc -l
apt list --upgradable 2>/dev/null | head -25
test -f /var/run/reboot-required && echo REBOOT_REQUIRED=yes || echo REBOOT_REQUIRED=no
echo '===TIMER==='
systemctl is-active certbot.timer; systemctl is-enabled certbot.timer
echo '===DRY2==='
certbot renew --dry-run --cert-name metacode-cloud.com
echo DRY2_EXIT:$?
"""
stdin, stdout, stderr = c.exec_command(cmd, timeout=420)
out = stdout.read().decode("utf-8", "replace")
err = stderr.read().decode("utf-8", "replace")
(EV / "E1-pkgs-dry2.txt").write_text(out + "\nERR:\n" + err, encoding="utf-8")
print(out[-2000:])
c.close()
