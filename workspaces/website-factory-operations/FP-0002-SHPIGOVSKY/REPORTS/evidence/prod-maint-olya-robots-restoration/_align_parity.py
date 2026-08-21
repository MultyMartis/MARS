# -*- coding: utf-8 -*-
"""Align physical robots to IndexingControl OPEN body; check dashboard label."""
from __future__ import annotations

import io
import json
import re
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
UA = "FP-0002-PROD-MAINT-OLYA-ROBOTS/1.0"


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
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
$_SERVER['REQUEST_URI']='/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$body = Shpigovsky\Core\Admin\IndexingControl::robots_body(true);
$path = Shpigovsky\Core\Admin\IndexingControl::robots_path();
file_put_contents($path, $body);
$read = file_get_contents($path);
$snap = Shpigovsky\Core\Admin\IndexingState::snapshot();
$user = get_user_by('login','mars');
if (!$user) $user = get_user_by('login','admin');
wp_set_current_user($user ? $user->ID : 0);
ob_start();
if (class_exists('Shpigovsky\Core\Admin\IndexingControl')) {
  Shpigovsky\Core\Admin\IndexingControl::render_banner();
}
$banner = ob_get_clean();
ob_start();
Shpigovsky\Core\Admin\SystemDashboard::render_widget();
$widget = ob_get_clean();
echo wp_json_encode(array(
  'ok'=>true,
  'written_sha'=>hash('sha256',$body),
  'read_sha'=>hash('sha256',$read),
  'match'=> hash('sha256',$body)===hash('sha256',$read),
  'effective'=>$snap['effective'] ?? null,
  'blog_public'=>(int)get_option('blog_public'),
  'banner_open'=> (false !== strpos($banner, 'Индексация сайта: открыта')),
  'widget_open'=> (false !== strpos($widget, 'Индексация сайта: открыта')),
  'widget_has_indexing'=> (false !== strpos($widget, 'Индексация')),
  'core'=>SHPIGOVSKY_CORE_VERSION,
  'body_len'=>strlen($body),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""


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
    remote = f"{DOCROOT}/wp-content/uploads/.fp02-olya-align.php"
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), remote)
    _stdin, stdout, stderr = client.exec_command(f"php8.2 {remote} 2>&1 || php {remote} 2>&1", timeout=120)
    out = stdout.read().decode("utf-8", errors="replace")
    try:
        sftp.remove(remote)
    except OSError:
        pass
    print(out)
    payload = json.loads([ln for ln in out.splitlines() if ln.startswith("{")][-1])
    (EV / "11-align-physical-to-open-body.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # pull aligned robots back to source canonical so SOURCE==PRODUCTION
    bio = io.BytesIO()
    sftp.getfo(f"{DOCROOT}/robots.txt", bio)
    data = bio.getvalue()
    (EV / "05-live-robots-after.txt").write_bytes(data)
    for target in (
        ROOT / "WORDPRESS/seo/OLYA-ROBOTS-REVIEWED-CANDIDATE.txt",
        ROOT / "WORDPRESS/plugins/shpigovsky-core/assets/robots-seo-policy.txt",
        EV / "OLYA-ROBOTS-REVIEWED-CANDIDATE.txt",
    ):
        target.write_bytes(data)
    # also update remote policy asset to exact same bytes
    sftp.putfo(io.BytesIO(data), f"{DOCROOT}/wp-content/plugins/shpigovsky-core/assets/robots-seo-policy.txt")

    live = requests.get("https://shpigovsky.ru/robots.txt", headers={"User-Agent": UA}, timeout=30)
    live_info = {
        "status": live.status_code,
        "sha256": __import__("hashlib").sha256(live.content).hexdigest(),
        "source_sha256": __import__("hashlib").sha256(data).hexdigest(),
        "match_source": live.content == data,
        "has_global_disallow": bool(
            re.search(r"^\s*Disallow:\s*/\s*$", live.content.decode("utf-8", "replace"), re.M)
        ),
    }
    (EV / "05-live-robots-after.json").write_text(
        json.dumps(live_info, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("live", live_info)
    sftp.close()
    client.close()


if __name__ == "__main__":
    main()
