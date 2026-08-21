# -*- coding: utf-8 -*-
"""Redeploy IndexingControl with P18J banner UX restored; verify dashboard label."""
from __future__ import annotations

import hashlib
import io
import json
import re
from pathlib import Path

import paramiko

ROOT = Path(__file__).resolve().parents[3]
EV = Path(__file__).resolve().parent
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
LOCAL = ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingControl.php"
REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Admin/IndexingControl.php"


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
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$user=get_user_by('login','mars'); if(!$user) $user=get_user_by('login','admin');
wp_set_current_user($user?$user->ID:0);
ob_start(); Shpigovsky\Core\Admin\IndexingControl::render_banner(); $banner=ob_get_clean();
ob_start(); Shpigovsky\Core\Admin\SystemDashboard::render_widget(); $widget=ob_get_clean();
$snap=Shpigovsky\Core\Admin\IndexingState::snapshot();
echo wp_json_encode(array(
  'core'=>SHPIGOVSKY_CORE_VERSION,
  'blog_public'=>(int)get_option('blog_public'),
  'effective'=>$snap['effective']??null,
  'banner_open_label'=>(false!==strpos($banner,'Индексация сайта: открыта')),
  'widget_open_label'=>(false!==strpos($widget,'Индексация сайта: открыта')),
  'open_body_yandex'=>(false!==strpos(Shpigovsky\Core\Admin\IndexingControl::robots_body(true),'User-agent: Yandex')),
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
    data = LOCAL.read_bytes()
    sftp.putfo(io.BytesIO(data), REMOTE)
    after = io.BytesIO()
    sftp.getfo(REMOTE, after)
    manifest = {
        "remote": REMOTE,
        "local_sha256": hashlib.sha256(data).hexdigest(),
        "after_sha256": hashlib.sha256(after.getvalue()).hexdigest(),
        "match": after.getvalue() == data,
    }
    (EV / "13-redeploy-indexingcontrol-ux.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    remote_php = f"{DOCROOT}/wp-content/uploads/.fp02-banner2.php"
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), remote_php)
    _stdin, stdout, _stderr = client.exec_command(f"php8.2 {remote_php} 2>&1", timeout=60)
    out = stdout.read().decode("utf-8", errors="replace")
    print(out)
    payload = json.loads([ln for ln in out.splitlines() if ln.startswith("{")][-1])
    (EV / "14-dashboard-open-label.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    # refresh post-deploy wp json fields
    prev = {}
    prev_path = EV / "04-post-deploy-wp.json"
    if prev_path.exists():
        prev = json.loads(prev_path.read_text(encoding="utf-8"))
    prev.update(
        {
            "dashboard_open_label": payload.get("banner_open_label") or payload.get("widget_open_label"),
            "indexing_effective": payload.get("effective"),
            "blog_public": payload.get("blog_public"),
            "core": payload.get("core"),
        }
    )
    prev_path.write_text(json.dumps(prev, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        sftp.remove(remote_php)
    except OSError:
        pass
    sftp.close()
    client.close()
    print("manifest", manifest)


if __name__ == "__main__":
    main()
