# -*- coding: utf-8 -*-
from __future__ import annotations
import re
from pathlib import Path
import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing")

def parse_secrets(text):
    pairs = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs

def getf(pairs, *keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None

CMD = r"""
pwd
echo HOME=$HOME
echo USER=$USER
ls -la "$HOME" | head -30
echo '=== find robots ==='
find "$HOME" -name robots.txt 2>/dev/null
echo '=== docroot robots xxd ==='
xxd "$HOME/shpigovsky.ru/public_html/robots.txt" | head
echo '=== curl local host header ==='
curl -sI -H 'Host: shpigovsky.ru' http://127.0.0.1/robots.txt | head -25
echo '=== curl local body xxd ==='
curl -s -H 'Host: shpigovsky.ru' http://127.0.0.1/robots.txt | xxd | head
echo '=== curl beget host ==='
curl -sI -H 'Host: shpigovsky.beget.tech' http://127.0.0.1/robots.txt | head -15
curl -s -H 'Host: shpigovsky.beget.tech' http://127.0.0.1/robots.txt | xxd | head
"""

pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(
    hostname=getf(pairs, "ssh_host"),
    port=int(getf(pairs, "ssh_port") or "22"),
    username=getf(pairs, "ssh_username"),
    password=getf(pairs, "ssh_password_or_key_reference"),
    timeout=60,
    allow_agent=False,
    look_for_keys=False,
)
stdin, stdout, stderr = c.exec_command(CMD, timeout=45)
out = stdout.read().decode("utf-8", "replace")
err = stderr.read().decode("utf-8", "replace")
(EV / "ROBOTS-LOCAL-CURL.txt").write_text(out + "\n---stderr---\n" + err, encoding="utf-8")
print(out)
print("ERR", err[-800:])
c.close()
