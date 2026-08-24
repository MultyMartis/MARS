# -*- coding: utf-8 -*-
import re
from pathlib import Path
import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
pairs = {}
for line in SECRETS.read_text(encoding="utf-8", errors="replace").splitlines():
    m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
    if m:
        pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")


def getf(*keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None


c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(
    hostname=getf("ssh_host", "sftp_host") or "shpigovsky.beget.tech",
    port=int(getf("ssh_port") or "22"),
    username=getf("ssh_username", "sftp_user"),
    password=getf("ssh_password_or_key_reference", "sftp_password", "ftp_or_sftp_password"),
    timeout=60,
    allow_agent=False,
    look_for_keys=False,
)
cmd = "php -v 2>&1 | head -3; which php; ls /usr/bin/php* 2>/dev/null; command -v php8.2; command -v php8.3; ls /usr/local/bin/php* 2>/dev/null"
i, o, e = c.exec_command(cmd, timeout=60)
print(o.read().decode("utf-8", "replace"))
print(e.read().decode("utf-8", "replace"))
c.close()
