# -*- coding: utf-8 -*-
from __future__ import annotations

import io
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
EV = Path(__file__).resolve().parent

PHP = r"""<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$user=get_user_by('login','mars'); if(!$user) $user=get_user_by('login','admin');
wp_set_current_user($user?$user->ID:0);
ob_start();
Shpigovsky\Core\Admin\IndexingControl::render_banner();
$h=ob_get_clean();
file_put_contents('/tmp/fp02-banner-snip.html', $h);
if (preg_match('/fp02-indexing-banner__title[^>]*>([^<]+)/u', $h, $m)) {
  echo 'TITLE='.$m[1]."\n";
  echo 'HEX='.bin2hex($m[1])."\n";
}
echo 'CLASS=';
if (preg_match('/fp02-indexing-banner\s+([a-z-]+)/', $h, $m)) echo $m[1];
echo "\n";
$snap=Shpigovsky\Core\Admin\IndexingState::snapshot();
echo 'EFF='.$snap['effective']."\n";
echo 'HAS_OPEN='.(false!==strpos($h,'открыта')?'1':'0')."\n";
echo 'HAS_CHECK='.(false!==strpos($h,'проверки')?'1':'0')."\n";
echo 'BYTES='.strlen($h)."\n";
"""


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


def main() -> None:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port", "sftp_port") or "22"),
        username=getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
        password=getf(
            pairs,
            "ssh_password_or_key_reference",
            "ssh_password",
            "sftp_password",
            "ftp_or_sftp_password",
            "ftp_password",
        ),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()
    remote = f"{DOCROOT}/wp-content/uploads/.fp02-banner.php"
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), remote)
    _stdin, stdout, _stderr = client.exec_command(f"php8.2 {remote} 2>&1", timeout=60)
    out = stdout.read().decode("utf-8", errors="replace")
    print(out)
    (EV / "12-banner-check.txt").write_text(out, encoding="utf-8")
    try:
        bio = io.BytesIO()
        sftp.getfo("/tmp/fp02-banner-snip.html", bio)
        (EV / "12-banner-snip.html").write_bytes(bio.getvalue())
    except OSError as exc:
        print("snip err", exc)
    try:
        sftp.remove(remote)
    except OSError:
        pass
    sftp.close()
    client.close()


if __name__ == "__main__":
    main()
