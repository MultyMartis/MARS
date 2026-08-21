# -*- coding: utf-8 -*-
"""Repair post-deploy WP verification after PHP 255."""
from __future__ import annotations

import io
import json
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(__file__).resolve().parent
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
error_reporting(E_ALL);
ini_set('display_errors','1');
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
$_SERVER['REQUEST_URI']='/';
try {
  require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
} catch (Throwable $e) {
  echo json_encode(['ok'=>false,'stage'=>'wp-load','error'=>$e->getMessage()]);
  exit(1);
}
$path = ABSPATH.'robots.txt';
$body = is_file($path) ? file_get_contents($path) : '';
$out = array(
  'ok'=>true,
  'core'=> defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'blog_public'=>(int)get_option('blog_public'),
  'robots_exists'=>is_file($path),
  'robots_sha'=>is_file($path)?hash('sha256',$body):null,
  'robots_has_global_disallow'=>(bool)preg_match('/^\s*Disallow:\s*\/\s*$/mi',(string)$body),
  'robots_has_yandex'=> (false !== strpos((string)$body, 'User-agent: Yandex')),
);
try {
  if (class_exists('Shpigovsky\Core\Admin\IndexingState')) {
    $snap = Shpigovsky\Core\Admin\IndexingState::snapshot();
    $out['indexing_effective'] = $snap['effective'] ?? null;
    $out['human_decision'] = $snap['human_decision'] ?? null;
    $out['robots_owner'] = $snap['robots']['owner'] ?? null;
  }
  if (class_exists('Shpigovsky\Core\Admin\IndexingControl')) {
    $open_body = Shpigovsky\Core\Admin\IndexingControl::robots_body(true);
    $out['open_body_has_yandex'] = (false !== strpos($open_body, 'User-agent: Yandex'));
    $norm = trim(str_replace("\r\n","\n",$open_body));
    $out['open_body_not_generic_mars'] = (false === strpos($norm, "User-agent: *\nDisallow: /wp-admin/"));
    $out['open_body_sha'] = hash('sha256', $open_body);
  }
  if (class_exists('Shpigovsky\Core\Admin\ActivityLog')) {
    Shpigovsky\Core\Admin\ActivityLog::log_system_event(
      'seo_robots_restored',
      'setting',
      'SEO robots.txt восстановлен / актуализирован',
      0,
      'prod_maint_olya_robots',
      0
    );
    $out['activity_logged'] = true;
  }
  $user = get_user_by('login','admin');
  if (!$user) { $user = get_user_by('login','mars'); }
  wp_set_current_user($user ? $user->ID : 0);
  if (class_exists('Shpigovsky\Core\Admin\SystemDashboard')) {
    ob_start();
    Shpigovsky\Core\Admin\SystemDashboard::render_widget();
    $html = ob_get_clean();
    $out['dashboard_open_label'] = (false !== strpos($html, 'Индексация сайта: открыта'));
  }
  $out['watchdog_baseline'] = get_option('fp02_indexing_watchdog_baseline');
} catch (Throwable $e) {
  $out['ok'] = false;
  $out['error'] = $e->getMessage();
  $out['trace'] = $e->getFile().':'.$e->getLine();
}
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
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
    remote = f"{DOCROOT}/wp-content/uploads/.fp02-olya-post2.php"
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), remote)
    stdin, stdout, stderr = client.exec_command(
        f"php8.2 {remote} 2>&1 || php {remote} 2>&1", timeout=120
    )
    out = stdout.read().decode("utf-8", errors="replace")
    code = stdout.channel.recv_exit_status()
    try:
        sftp.remove(remote)
    except OSError:
        pass
    print("CODE", code)
    print(out[:4000])
    lines = [ln for ln in out.splitlines() if ln.strip().startswith("{")]
    if lines:
        payload = json.loads(lines[-1])
        (EV / "04-post-deploy-wp.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print("saved ok", payload.get("ok"), "core", payload.get("core"), "bp", payload.get("blog_public"))
    sftp.close()
    client.close()


if __name__ == "__main__":
    main()
