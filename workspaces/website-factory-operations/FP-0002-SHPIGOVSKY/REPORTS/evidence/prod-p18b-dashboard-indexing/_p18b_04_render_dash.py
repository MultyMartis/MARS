# -*- coding: utf-8 -*-
"""Render Dashboard widget via php8.2 as Administrator. No HTTP login. No indexing mutation."""
from __future__ import annotations

import io
import json
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing")

PHP = r"""<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
$_SERVER['REQUEST_URI']='/wp-admin/index.php';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$user = get_user_by('login', 'admin');
if (!$user) { $user = get_user_by('login', 'mars'); }
wp_set_current_user($user ? $user->ID : 0);
$caps = array(
  'login' => $user ? $user->user_login : null,
  'roles' => $user ? $user->roles : array(),
  'manage_options' => current_user_can('manage_options'),
  'olya_is_admin' => ($user && $user->user_login === 'admin' && in_array('administrator', (array)$user->roles, true)),
);
ob_start();
\Shpigovsky\Core\Admin\SystemDashboard::render_widget();
$html = ob_get_clean();
$state = \Shpigovsky\Core\Admin\IndexingControl::read_state();
$logs = $GLOBALS['wpdb']->get_results("SELECT id, actor_login, action, object_type, created_at FROM fp02_user_activity_log WHERE action IN ('indexing_opened','indexing_closed') ORDER BY id DESC LIMIT 8", ARRAY_A);
echo "---JSON---\n";
echo json_encode(array(
  'caps'=>$caps,
  'state'=>$state,
  'blog_public'=>(int)get_option('blog_public'),
  'html_bytes'=>strlen($html),
  'has_closed_banner'=>(false !== strpos($html, 'закрыт от индексации')),
  'has_open_button'=>(false !== strpos($html, 'Открыть индексацию')),
  'has_close_button'=>(false !== strpos($html, 'Закрыть индексацию')),
  'has_stale_ns'=>(false !== strpos($html, 'READY FOR MANUAL NS SWITCH') || false !== strpos($html, 'Future host')),
  'has_p18b'=>(false !== strpos($html, 'P18B')),
  'has_noreply'=>(false !== strpos($html, 'noreply@shpigovsky.ru')),
  'has_nonce'=>(false !== strpos($html, 'fp02_set_indexability') && false !== strpos($html, '_wpnonce')),
  'has_confirm'=>(false !== strpos($html, 'fp02_confirm')),
  'has_post_form'=>(false !== strpos($html, 'method="post"') && false !== strpos($html, 'admin-post.php')),
  'has_craftum'=>(false !== strpos($html, 'Craftum') || false !== strpos($html, 'старый сайт')),
  'has_smtp'=>(false !== strpos($html, 'SMTP PENDING')),
  'has_fresh_backup'=>(false !== strpos($html, 'FRESH BEGET BACKUP')),
  'activity_log_rows'=>$logs,
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n---HTML---\n";
echo $html;
echo "\n";
"""


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


def main() -> int:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host"),
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username"),
        password=getf(pairs, "ssh_password_or_key_reference"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), "/tmp/fp02_p18b_render.php")
    stdin, stdout, stderr = client.exec_command(
        "php8.2 /tmp/fp02_p18b_render.php 2>/dev/null || /usr/local/bin/php8.2 /tmp/fp02_p18b_render.php",
        timeout=90,
    )
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    try:
        sftp.remove("/tmp/fp02_p18b_render.php")
    except OSError:
        pass
    sftp.close()
    client.close()
    if "---JSON---" not in out:
        (EV / "DASHBOARD-RENDER-RAW.txt").write_text(out + "\nERR\n" + err, encoding="utf-8")
        print("FAIL no json", out[:800], err[:400])
        return 2
    js, html = out.split("---HTML---", 1)
    js = js.split("---JSON---", 1)[1].strip()
    data = json.loads(js.splitlines()[0])
    (EV / "DASHBOARD-RENDER.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (EV / "dashboard-after-snippet.html").write_text(html.strip() + "\n", encoding="utf-8")
    print("OK", {k: data.get(k) for k in (
        "has_closed_banner", "has_open_button", "has_nonce", "has_stale_ns",
        "has_p18b", "has_craftum", "blog_public", "caps"
    )})
    return 0 if data.get("has_closed_banner") and data.get("has_nonce") and not data.get("has_stale_ns") else 2


if __name__ == "__main__":
    raise SystemExit(main())
