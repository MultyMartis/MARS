# -*- coding: utf-8 -*-
"""Find the public apex robots.txt owner on disk."""
from __future__ import annotations
import re
from pathlib import Path
import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing")

def parse_secrets(text):
    pairs={}
    for line in text.splitlines():
        m=re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m: pairs[m.group(1)]=m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs

def getf(pairs,*keys):
    for k in keys:
        v=pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip(): return v.strip()
    return None

CMD = r"""
set +e
echo '=== grep Disallow /*? ==='
grep -Rsl --include='robots.txt' --include='*.txt' --include='*.conf' -e 'Disallow: /\*?' -e 'sitemap.xml' /home/s/shpigovsky 2>/dev/null | head -80
echo '=== find robots.txt ==='
find /home/s/shpigovsky -name 'robots.txt' 2>/dev/null | head -40
echo '=== hexdump public vs docroot ==='
python3 - <<'PY' 2>/dev/null || true
print('skip')
PY
echo '=== ls sites ==='
ls -la /home/s/shpigovsky | head -40
echo '=== nginx snippets if any ==='
ls -la /home/s/shpigovsky/*/public_html/robots.txt 2>/dev/null
ls -la /home/s/shpigovsky/*/*/robots.txt 2>/dev/null | head
"""

pairs=parse_secrets(SECRETS.read_text(encoding="utf-8"))
c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=getf(pairs,"ssh_host"), port=int(getf(pairs,"ssh_port") or "22"),
          username=getf(pairs,"ssh_username"), password=getf(pairs,"ssh_password_or_key_reference"),
          timeout=60, allow_agent=False, look_for_keys=False)
stdin,stdout,stderr=c.exec_command(CMD, timeout=60)
out=stdout.read().decode("utf-8","replace")
err=stderr.read().decode("utf-8","replace")
(EV/"ROBOTS-FIND.txt").write_text(out+"\n---stderr---\n"+err, encoding="utf-8")
print(out[-4000:])
c.close()
