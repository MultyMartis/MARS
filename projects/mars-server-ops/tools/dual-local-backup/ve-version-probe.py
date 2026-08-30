#!/usr/bin/env python3
import re
from pathlib import Path
import paramiko

p = Path(r"X:\AI MARS\local\infrastructure\MCA-VPN-001\secrets.local.md")
d = {}
for line in p.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^\s*([A-Za-z0-9_./-]+)\s*[:=]\s*(.+?)\s*$", line)
    if m:
        d[m.group(1).lower()] = m.group(2).strip().strip("`").strip('"').strip("'")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(
    d.get("host"),
    port=int(d.get("port", 22)),
    username=d.get("user", "root"),
    password=d["password"],
    timeout=30,
    allow_agent=False,
    look_for_keys=False,
)
cmd = r"""
/usr/local/x-ui/bin/xray version 2>&1 | head -n 5
echo ---
ls -la /usr/local/x-ui/bin/xray
echo ---
stat -c '%y %s' /usr/local/x-ui/x-ui /usr/local/x-ui/bin/xray
"""
_, o, e = c.exec_command(cmd, timeout=60)
out = Path(r"X:\AI MARS\projects\mars-server-ops\evidence\DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01\ve-versions.txt")
out.write_text(o.read().decode("utf-8", "replace") + e.read().decode("utf-8", "replace"), encoding="utf-8")
print(out.read_text(encoding="utf-8"))
c.close()
