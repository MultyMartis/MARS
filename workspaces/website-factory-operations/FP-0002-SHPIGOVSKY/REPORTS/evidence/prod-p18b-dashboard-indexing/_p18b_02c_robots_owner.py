# -*- coding: utf-8 -*-
"""Inspect robots owners: SFTP file vs HTTP vs WP."""
from __future__ import annotations
import io, json, re
from pathlib import Path
import paramiko, requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
UA = "FP-0002-P18B-robots-owner/1.0"

PHP = r"""<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$path = ABSPATH.'robots.txt';
$active = (array) get_option('active_plugins', array());
$seo = array();
foreach ($active as $p) {
    if (preg_match('/seo|robot|sitemap|rank|yoast|aioseo|squirrly/i', (string)$p)) $seo[] = $p;
}
echo json_encode(array(
    'blog_public'=>(int)get_option('blog_public'),
    'abspath'=>ABSPATH,
    'file_exists'=>is_file($path),
    'file'=>is_file($path)?file_get_contents($path):null,
    'file_bytes'=>is_file($path)?filesize($path):null,
    'seo_like_plugins'=>$seo,
    'active_plugins'=>$active,
    'has_robots_txt_filter'=>has_filter('robots_txt'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

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

pairs=parse_secrets(SECRETS.read_text(encoding="utf-8"))
http=[]
for url in [
    "https://shpigovsky.ru/robots.txt",
    "http://shpigovsky.ru/robots.txt",
    "http://shpigovsky.beget.tech/robots.txt",
]:
    r=requests.get(url, timeout=25, allow_redirects=True, headers={"User-Agent": UA})
    body=r.content
    http.append({
        "url": url,
        "status": r.status_code,
        "final": str(r.url),
        "ctype": r.headers.get("Content-Type"),
        "server": r.headers.get("Server"),
        "bytes": len(body),
        "sha_head": body[:120].decode("utf-8","replace"),
        "hex_head": body[:16].hex(),
    })

c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=getf(pairs,"ssh_host"), port=int(getf(pairs,"ssh_port") or "22"),
          username=getf(pairs,"ssh_username"), password=getf(pairs,"ssh_password_or_key_reference"),
          timeout=60, allow_agent=False, look_for_keys=False)
sftp=c.open_sftp()
bio=io.BytesIO()
try:
    sftp.getfo(f"{DOCROOT}/robots.txt", bio)
    disk=bio.getvalue()
except Exception as e:
    disk=None
    disk_err=str(e)
else:
    disk_err=None

# extra robots-like files
stdin,stdout,stderr=c.exec_command(f"ls -la {DOCROOT}/robots.txt {DOCROOT}/sitemap.xml {DOCROOT}/sitemap_index.xml 2>&1; find {DOCROOT} -maxdepth 2 -iname '*robot*' 2>/dev/null | head", timeout=30)
ls=stdout.read().decode("utf-8","replace")

sftp.putfo(io.BytesIO(PHP.encode("utf-8")), "/tmp/fp02_p18b_robots.php")
stdin,stdout,stderr=c.exec_command("php8.2 /tmp/fp02_p18b_robots.php 2>/dev/null || /usr/local/bin/php8.2 /tmp/fp02_p18b_robots.php", timeout=90)
wp=stdout.read().decode("utf-8","replace")
try: sftp.remove("/tmp/fp02_p18b_robots.php")
except OSError: pass
sftp.close(); c.close()
data={"http":http,"disk_err":disk_err,"disk_bytes": len(disk) if disk else None,
      "disk_hex_head": disk[:16].hex() if disk else None,
      "disk_text": disk.decode("utf-8","replace") if disk else None,
      "ls": ls, "wp": None}
for ln in wp.splitlines():
    if ln.startswith("{"):
        data["wp"]=json.loads(ln); break
else:
    data["wp_raw"]=wp[:2000]
(EV/"ROBOTS-OWNER.json").write_text(json.dumps(data, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
print(json.dumps({"http":[{k:x[k] for k in ("url","status","bytes","hex_head","sha_head")} for x in http],
                  "disk_text": data["disk_text"], "disk_hex": data["disk_hex_head"],
                  "wp_file": (data.get("wp") or {}).get("file"),
                  "plugins": (data.get("wp") or {}).get("seo_like_plugins"),
                  "blog_public": (data.get("wp") or {}).get("blog_public")}, indent=2, ensure_ascii=False))
