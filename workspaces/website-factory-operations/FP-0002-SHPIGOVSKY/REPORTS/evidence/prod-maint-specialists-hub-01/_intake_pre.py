# -*- coding: utf-8 -*-
"""Fresh read-only production intake for Specialists Hub wave."""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
REMOTE_PROBE = f"{DOCROOT}/wp-content/uploads/.fp02-hub-intake-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}.php"


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


PROBE_PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');

$out = array();
$out['ts_utc'] = gmdate('c');
$out['blog_public'] = (int) get_option('blog_public');
$out['siteurl'] = get_option('siteurl');
$out['home'] = get_option('home');
$out['stylesheet'] = get_option('stylesheet');
$out['template'] = get_option('template');

$theme = wp_get_theme();
$out['theme'] = array(
  'name' => $theme->get('Name'),
  'version' => $theme->get('Version'),
  'stylesheet' => $theme->get_stylesheet(),
);

if (!function_exists('get_plugins')) {
  require_once ABSPATH . 'wp-admin/includes/plugin.php';
}
$plugins = get_plugins();
$core_key = 'shpigovsky-core/shpigovsky-core.php';
$out['core_plugin'] = isset($plugins[$core_key]) ? array(
  'Name' => $plugins[$core_key]['Name'] ?? '',
  'Version' => $plugins[$core_key]['Version'] ?? '',
  'active' => is_plugin_active($core_key),
) : null;
$wpilot_key = 'metacode-wpilot/metacode-wpilot.php';
$out['wpilot'] = isset($plugins[$wpilot_key]) ? array(
  'Version' => $plugins[$wpilot_key]['Version'] ?? '',
  'active' => is_plugin_active($wpilot_key),
) : null;
if (class_exists('MetaCODE\\WPilot\\Plugin') || defined('WPILOT_VERSION')) {
  // best-effort
}
$out['wpilot_write_probe'] = array(
  'option_write_enabled' => get_option('metacode_wpilot_write_enabled', null),
);

$page = get_post(1030);
$out['page_1030'] = null;
if ($page instanceof WP_Post) {
  $acf = array();
  $acf_keys = array(
    'generic_page_lead',
    'generic_page_body',
    'generic_page_reusable_blocks',
    'page_layout_mode',
    'seo_title',
    'seo_description',
  );
  foreach ($acf_keys as $k) {
    $acf[$k] = get_post_meta(1030, $k, true);
  }
  $out['page_1030'] = array(
    'ID' => (int) $page->ID,
    'post_title' => $page->post_title,
    'post_name' => $page->post_name,
    'post_status' => $page->post_status,
    'post_type' => $page->post_type,
    'guid' => $page->guid,
    'permalink' => get_permalink($page),
    'template' => get_page_template_slug($page->ID),
    'post_content' => $page->post_content,
    'post_content_sha256' => hash('sha256', (string) $page->post_content),
    'post_excerpt' => $page->post_excerpt,
    'menu_order' => (int) $page->menu_order,
    'post_modified_gmt' => $page->post_modified_gmt,
    'acf' => $acf,
    'seo_title' => get_post_meta($page->ID, '_yoast_wpseo_title', true),
    'seo_metadesc_yoast' => get_post_meta($page->ID, '_yoast_wpseo_metadesc', true),
    'rank_title' => get_post_meta($page->ID, 'rank_math_title', true),
    'rank_desc' => get_post_meta($page->ID, 'rank_math_description', true),
    'fp02_seo_title' => get_post_meta($page->ID, 'seo_title', true),
    'fp02_seo_description' => get_post_meta($page->ID, 'seo_description', true),
    'all_meta_keys' => array_keys(get_post_meta($page->ID)),
  );
}

$q = new WP_Query(array(
  'post_type' => 'specialist',
  'post_status' => 'publish',
  'posts_per_page' => 50,
  'orderby' => array('menu_order' => 'ASC', 'title' => 'ASC'),
  'no_found_rows' => true,
));
$specs = array();
foreach ($q->posts as $p) {
  $specs[] = array(
    'ID' => (int) $p->ID,
    'title' => $p->post_title,
    'slug' => $p->post_name,
    'status' => $p->post_status,
    'menu_order' => (int) $p->menu_order,
    'permalink' => get_permalink($p),
    'modified_gmt' => $p->post_modified_gmt,
  );
}
$out['specialists_published'] = $specs;
$out['specialists_count'] = count($specs);

$out['cards_helper'] = array('skipped' => 'acf_cli_init_issue');
$out['specialists_roles_meta'] = array();
foreach ($specs as $s) {
  $out['specialists_roles_meta'][] = array(
    'ID' => $s['ID'],
    'role_meta' => get_post_meta($s['ID'], 'specialist_role', true),
  );
}

$out['activity_log_recent'] = array();
global $wpdb;
$table = $wpdb->prefix . 'fp02_user_activity_log';
$exists = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $table));
if ($exists === $table) {
  $rows = $wpdb->get_results(
    "SELECT id, created_at, user_id, action, object_type, object_id, summary FROM {$table} ORDER BY id DESC LIMIT 25",
    ARRAY_A
  );
  $out['activity_log_recent'] = is_array($rows) ? $rows : array();
}

$files = array(
  'theme/page-templates/generic.php' => 'wp-content/themes/shpigovsky/page-templates/generic.php',
  'theme/page-templates/services-hub.php' => 'wp-content/themes/shpigovsky/page-templates/services-hub.php',
  'theme/inc/reusable-blocks-helpers.php' => 'wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php',
  'theme/template-parts/home/specialists.php' => 'wp-content/themes/shpigovsky/template-parts/home/specialists.php',
  'theme/template-parts/generic/content-page.php' => 'wp-content/themes/shpigovsky/template-parts/generic/content-page.php',
  'plugin/FieldGroups.php' => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
  'plugin/shpigovsky-core.php' => 'wp-content/plugins/shpigovsky-core/shpigovsky-core.php',
  'robots.txt' => 'robots.txt',
);
$out['prod_files'] = array();
foreach ($files as $label => $rel) {
  $abs = ABSPATH . $rel;
  if (is_readable($abs)) {
    $raw = file_get_contents($abs);
    $out['prod_files'][$label] = array(
      'path' => $abs,
      'bytes' => strlen($raw),
      'sha256' => hash('sha256', $raw),
      'mtime' => gmdate('c', filemtime($abs)),
      'exists_specialists_hub' => false,
    );
  } else {
    $out['prod_files'][$label] = array('missing' => true, 'path' => $abs);
  }
}
$hub = ABSPATH . 'wp-content/themes/shpigovsky/page-templates/specialists-hub.php';
$out['specialists_hub_template_exists'] = is_readable($hub);

echo wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
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

    def run(cmd: str) -> str:
        _i, o, e = client.exec_command(cmd, timeout=180)
        out = o.read().decode("utf-8", errors="replace")
        err = e.read().decode("utf-8", errors="replace")
        code = o.channel.recv_exit_status()
        return out + (("\n[stderr]\n" + err) if err else "") + f"\n[exit]={code}\n"

    sftp.putfo(io.BytesIO(PROBE_PHP.encode("utf-8")), REMOTE_PROBE)
    raw = run(f"cd {DOCROOT}; /usr/local/bin/php8.2 -d display_errors=1 -d error_reporting=E_ALL {REMOTE_PROBE}")
    try:
        sftp.remove(REMOTE_PROBE)
    except OSError:
        pass

    # Strip exit trailer for JSON parse.
    body = raw
    if "[exit]=" in body:
        body = body.rsplit("[exit]=", 1)[0]
    if "[stderr]" in body:
        body = body.split("[stderr]", 1)[0]
    body = body.strip()
    OUT.joinpath("01-intake-raw.txt").write_text(raw, encoding="utf-8")
    # Extract JSON object even if PHP prints warnings before it.
    start = body.find("{")
    end = body.rfind("}")
    if start < 0 or end <= start:
        print("INTAKE_PARSE_FAIL no_json")
        print(raw[:2000])
        return
    body = body[start : end + 1]
    try:
        data = json.loads(body)
        OUT.joinpath("01-intake.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("INTAKE_OK")
        print("blog_public=", data.get("blog_public"))
        p = data.get("page_1030") or {}
        print("page=", p.get("ID"), p.get("post_title"), p.get("post_name"), p.get("template"))
        print("content_sha=", p.get("post_content_sha256"))
        print("content=", repr((p.get("post_content") or "")[:300]))
        print("acf=", json.dumps(p.get("acf") or {}, ensure_ascii=False)[:500])
        print("specialists=", data.get("specialists_count"))
        for s in data.get("specialists_published") or []:
            print("  ", s.get("menu_order"), s.get("ID"), s.get("slug"), s.get("title"))
        print("hub_tpl_exists=", data.get("specialists_hub_template_exists"))
        print("core=", data.get("core_plugin"))
        print("activity_n=", len(data.get("activity_log_recent") or []))
    except Exception as exc:
        print("INTAKE_PARSE_FAIL", exc)
        print(raw[:2000])

    sftp.close()
    client.close()


if __name__ == "__main__":
    main()
