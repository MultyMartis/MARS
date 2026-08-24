# -*- coding: utf-8 -*-
"""Read-only production intake for specialists canonical URL migration."""
from __future__ import annotations

import io
import json
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
LAYER_B = Path(
    r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-specialists-canonical-url-migration-01"
)
LAYER_B.mkdir(parents=True, exist_ok=True)


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
header('Content-Type: application/json; charset=utf-8');
global $wpdb;
$p = get_post(1030);
$rewrite = get_option('rewrite_rules');
$spec_rules = array();
if (is_array($rewrite)) {
  foreach ($rewrite as $k => $v) {
    if (strpos($k, 'specyalisty') !== false || strpos($k, 'specialisty') !== false || strpos((string)$v, 'specialist') !== false) {
      $spec_rules[$k] = $v;
    }
  }
}
$specs = get_posts(array(
  'post_type'=>'specialist','post_status'=>'publish','numberposts'=>50,
  'orderby'=>array('menu_order'=>'ASC','title'=>'ASC')
));
$spec_out = array();
foreach ($specs as $s) {
  $spec_out[] = array(
    'ID'=>$s->ID,'post_name'=>$s->post_name,'title'=>$s->post_title,
    'menu_order'=>$s->menu_order,'permalink'=>get_permalink($s),
  );
}
$menus = wp_get_nav_menus();
$menu_hits = array();
foreach ($menus as $m) {
  $items = wp_get_nav_menu_items($m->term_id);
  if (!$items) continue;
  foreach ($items as $it) {
    $url = (string)$it->url;
    if (strpos($url, 'specyalisty') !== false || strpos($url, 'specialisty') !== false || (int)$it->object_id === 1030) {
      $menu_hits[] = array('menu'=>$m->name,'item_id'=>$it->ID,'title'=>$it->title,'url'=>$url,'type'=>$it->type,'object'=>$it->object,'object_id'=>$it->object_id);
    }
  }
}
$opt_all = null;
if (function_exists('get_field')) {
  $opt_all = get_field('specialists_all_link_url', 'option');
}
$like = '%' . $wpdb->esc_like('specyalisty') . '%';
$db = array(
  'posts_content' => (int)$wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_content LIKE %s AND post_status IN ('publish','draft','private')", $like)),
  'postmeta' => (int)$wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->postmeta} WHERE meta_value LIKE %s", $like)),
  'options' => (int)$wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->options} WHERE option_value LIKE %s", $like)),
);
$opt_rows = $wpdb->get_results($wpdb->prepare("SELECT option_name FROM {$wpdb->options} WHERE option_value LIKE %s LIMIT 50", $like), ARRAY_A);
$meta_rows = $wpdb->get_results($wpdb->prepare("SELECT post_id, meta_key FROM {$wpdb->postmeta} WHERE meta_value LIKE %s LIMIT 50", $like), ARRAY_A);
$post_rows = $wpdb->get_results($wpdb->prepare("SELECT ID, post_type, post_name, post_status FROM {$wpdb->posts} WHERE post_content LIKE %s AND post_status IN ('publish','draft','private') LIMIT 30", $like), ARRAY_A);
$cpt = get_post_type_object('specialist');
$out = array(
  'blog_public' => (int)get_option('blog_public'),
  'home' => get_option('home'),
  'siteurl' => get_option('siteurl'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'page_1030' => $p ? array(
    'ID'=>$p->ID,'post_name'=>$p->post_name,'post_title'=>$p->post_title,'post_status'=>$p->post_status,
    'post_parent'=>$p->post_parent,'permalink'=>get_permalink($p),
    'template'=>get_page_template_slug($p),
    'reusable_enabled'=>get_post_meta(1030,'generic_page_reusable_blocks_enabled',true),
    'reusable'=>get_post_meta(1030,'generic_page_reusable_blocks',true),
  ) : null,
  'specialists' => $spec_out,
  'menu_hits' => $menu_hits,
  'specialists_all_link_url' => $opt_all,
  'rewrite_spec_rules_count' => count($spec_rules),
  'rewrite_spec_rules_sample' => array_slice($spec_rules, 0, 20, true),
  'db_specyalisty' => $db,
  'db_option_names' => $opt_rows,
  'db_meta_keys' => $meta_rows,
  'db_posts_with_old_url' => $post_rows,
  'cpt_obj' => $cpt ? array(
    'name'=>$cpt->name,
    'has_archive'=>$cpt->has_archive,
    'rewrite'=>$cpt->rewrite,
  ) : null,
);
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
"""


def main() -> None:
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
    probe = f"{DOCROOT}/wp-content/uploads/.fp02-url-intake.php"
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), probe)
    _i, o, e = client.exec_command(
        f"/usr/local/bin/php8.2 -d display_errors=0 {probe}", timeout=180
    )
    raw = o.read().decode("utf-8", "replace")
    err = e.read().decode("utf-8", "replace")
    try:
        sftp.remove(probe)
    except OSError:
        pass
    start, end = raw.find("{"), raw.rfind("}")
    data = raw[start : end + 1] if start >= 0 and end > start else raw
    OUT.joinpath("01-prod-intake.json").write_text(data, encoding="utf-8")
    print(data[:8000])
    if err.strip():
        print("ERR", err[:800])

    snaps = [
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/ContentTypes/Specialist.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/search-helpers.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/sitemap-helpers.php",
        f"{DOCROOT}/.htaccess",
    ]
    for rem in snaps:
        try:
            with sftp.open(rem, "rb") as rf:
                blob = rf.read()
            safe = rem.replace("/", "__").lstrip("_")
            (LAYER_B / safe).write_bytes(blob)
            print("SNAP", rem, len(blob))
        except OSError as ex:
            print("SNAP_FAIL", rem, ex)

    sftp.close()
    client.close()
    print("INTAKE_OK")


if __name__ == "__main__":
    main()
