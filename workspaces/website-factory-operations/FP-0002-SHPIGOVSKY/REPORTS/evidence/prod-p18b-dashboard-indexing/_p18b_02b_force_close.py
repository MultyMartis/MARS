# -*- coding: utf-8 -*-
"""Emergency: restore indexing CLOSED after interrupted P18B QA."""
from __future__ import annotations
import io, json, re
from pathlib import Path
import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
PHP = r"""<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$r = \Shpigovsky\Core\Admin\IndexingControl::set_site_indexability(false);
$r['blog_public']=(int)get_option('blog_public');
$r['state']=\Shpigovsky\Core\Admin\IndexingControl::read_state();
echo json_encode($r, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

def parse_secrets(text):
    pairs={}
    for line in text.splitlines():
        m=re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)]=m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs

def getf(pairs,*keys):
    for k in keys:
        v=pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None

pairs=parse_secrets(SECRETS.read_text(encoding="utf-8"))
c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=getf(pairs,"ssh_host"), port=int(getf(pairs,"ssh_port") or "22"),
          username=getf(pairs,"ssh_username"), password=getf(pairs,"ssh_password_or_key_reference"),
          timeout=60, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()
sftp.putfo(io.BytesIO(PHP.encode("utf-8")), "/tmp/fp02_p18b_close.php")
stdin,stdout,stderr=c.exec_command("php8.2 /tmp/fp02_p18b_close.php 2>/dev/null || /usr/local/bin/php8.2 /tmp/fp02_p18b_close.php", timeout=90)
out=stdout.read().decode("utf-8", errors="replace")
print(out)
try: sftp.remove("/tmp/fp02_p18b_close.php")
except OSError: pass
sftp.close(); c.close()
