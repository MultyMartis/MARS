# -*- coding: utf-8 -*-
from pathlib import Path
import io
import re
import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if match:
            pairs[match.group(1)] = match.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$v = $wpdb->get_var("SELECT option_value FROM {$wpdb->options} WHERE option_name='fp02-block-specialists_specialists_all_link_url'");
$ht = file_get_contents(ABSPATH . '.htaccess');
echo wp_json_encode(array('opt' => $v, 'htaccess' => $ht), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
"""

pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname=getf(pairs, "ssh_host") or "shpigovsky.beget.tech",
    port=int(getf(pairs, "ssh_port") or "22"),
    username=getf(pairs, "ssh_username"),
    password=getf(pairs, "ssh_password_or_key_reference"),
    timeout=60,
    allow_agent=False,
    look_for_keys=False,
)
sftp = client.open_sftp()
probe = f"{DOCROOT}/wp-content/uploads/.fp02-opt.php"
sftp.putfo(io.BytesIO(PHP.encode("utf-8")), probe)
_i, o, e = client.exec_command(f"/usr/local/bin/php8.2 -d display_errors=0 {probe}", timeout=60)
print(o.read().decode("utf-8", "replace"))
print(e.read().decode("utf-8", "replace")[:300])
try:
    sftp.remove(probe)
except OSError:
    pass
sftp.close()
client.close()
