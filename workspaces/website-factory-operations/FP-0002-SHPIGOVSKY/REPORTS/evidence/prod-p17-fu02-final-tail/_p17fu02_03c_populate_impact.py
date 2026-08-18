# -*- coding: utf-8 -*-
"""Verify whether GET of populate-fp-0002-pages.php mutated live options/menus. Restore if needed."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p17-fu02-final-tail")
SNAP = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-fu02-db-snapshots\fp02_options.sql")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
REMOTE_PHP = "/tmp/fp02_p17fu02_menu_check.php"

PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$keys = array('show_on_front','page_on_front','page_for_posts','wp_page_for_privacy_policy','theme_mods_shpigovsky');
$opts = array();
foreach ($keys as $k) { $opts[$k] = get_option($k); }
$front = (int) get_option('page_on_front');
$blog = (int) get_option('page_for_posts');
$out = array(
  'utc' => gmdate('c'),
  'options' => array(
    'show_on_front' => get_option('show_on_front'),
    'page_on_front' => $front,
    'page_on_front_slug' => $front ? get_post_field('post_name', $front) : null,
    'page_on_front_title' => $front ? get_the_title($front) : null,
    'page_for_posts' => $blog,
    'page_for_posts_slug' => $blog ? get_post_field('post_name', $blog) : null,
    'wp_page_for_privacy_policy' => get_option('wp_page_for_privacy_policy'),
  ),
  'menus' => array(),
  'recent_menu_items' => array(),
  'recent_activity' => array(),
);
$menus = wp_get_nav_menus();
foreach ($menus as $m) {
    $items = wp_get_nav_menu_items($m->term_id) ?: array();
    $titles = array();
    foreach ($items as $it) { $titles[] = $it->title; }
    $out['menus'][] = array('term_id'=>(int)$m->term_id,'name'=>$m->name,'count'=>count($items),'titles'=>$titles);
}
$out['recent_menu_items'] = $wpdb->get_results(
    "SELECT ID, post_title, post_date_gmt, post_modified_gmt FROM {$wpdb->posts}
     WHERE post_type='nav_menu_item' AND post_date_gmt >= '2026-08-18 10:00:00'
     ORDER BY ID DESC LIMIT 50", ARRAY_A);
$t = $wpdb->prefix . 'user_activity_log';
$out['recent_activity'] = $wpdb->get_results(
    "SELECT id, user_id, action, object_id, object_type, object_title, created_at
     FROM `{$t}` WHERE created_at >= '2026-08-18 10:00:00' ORDER BY id DESC LIMIT 30", ARRAY_A);
$out['nav_menu_item_total'] = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='nav_menu_item' AND post_status='publish'");
echo json_encode($out, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""


def parse_secrets(text: str) -> dict:
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


def extract_option_from_sql(sql: str, name: str) -> str | None:
    # mysqldump INSERT format
    m = re.search(rf"\('{re.escape(name)}','((?:\\.|[^'\\])*)'", sql)
    if m:
        return m.group(1).replace("\\'", "'").replace("\\\\", "\\")
    # alternative dumped as INSERT INTO ... VALUES (id, 'name', 'value'
    m = re.search(rf",'{re.escape(name)}','((?:\\.|[^'\\])*)'", sql)
    return m.group(1).replace("\\'", "'").replace("\\\\", "\\") if m else None


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
    with sftp.file(REMOTE_PHP, "wb") as fh:
        fh.write(PHP.encode("utf-8"))
    stdin, stdout, stderr = client.exec_command(f"php8.2 {REMOTE_PHP} 2>/dev/null || php {REMOTE_PHP}", timeout=60)
    out = stdout.read().decode("utf-8", errors="replace")
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    sftp.close()
    client.close()
    inv = None
    for ln in out.splitlines():
        if ln.startswith("{"):
            inv = json.loads(ln)
            break
    snap = {}
    if SNAP.exists():
        sql = SNAP.read_text(encoding="utf-8", errors="replace")
        for k in ("show_on_front", "page_on_front", "page_for_posts", "wp_page_for_privacy_policy"):
            snap[k] = extract_option_from_sql(sql, k)
    payload = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "live": inv,
        "pre_get_snapshot_options": snap,
        "menu_items_created_after_probe": len((inv or {}).get("recent_menu_items") or []),
        "activity_after_probe": len((inv or {}).get("recent_activity") or []),
    }
    (EV / "POPULATE-SCRIPT-GET-IMPACT.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2)[:4000])
    return 0 if inv else 2


if __name__ == "__main__":
    raise SystemExit(main())
