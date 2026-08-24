# -*- coding: utf-8 -*-
"""Read-only production intake — specialists nav + SEO meta + contacts maps wave."""
from __future__ import annotations

import hashlib
import io
import json
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
LAYER_B = Path(
    r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-specialists-nav-seo-maps-01"
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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');

function fp02_seo_fields($post_id) {
  $out = array('ID' => (int)$post_id);
  if (!$post_id) return $out;
  foreach (array('fp02_seo_title','fp02_seo_description') as $k) {
    $v = function_exists('get_field') ? get_field($k, $post_id) : get_post_meta($post_id, $k, true);
    $out[$k] = is_string($v) ? $v : '';
  }
  $out['post_title'] = get_the_title($post_id);
  $out['post_type'] = get_post_type($post_id);
  $out['permalink'] = get_permalink($post_id);
  $out['template'] = get_page_template_slug($post_id);
  return $out;
}

$front = (int) get_option('page_on_front');
$posts_page = (int) get_option('page_for_posts');
$contacts = get_page_by_path('kontakty');
$uslugi = get_page_by_path('uslugi');
$o_centre = get_page_by_path('o-centre');
$reviews = get_page_by_path('otzyvy');
$privacy = get_page_by_path('politika-konfidencialnosti');

$services = get_posts(array('post_type'=>'service','post_status'=>'publish','numberposts'=>1,'orderby'=>'menu_order','order'=>'ASC'));
$specialists = get_posts(array('post_type'=>'specialist','post_status'=>'publish','numberposts'=>1,'orderby'=>'menu_order','order'=>'ASC'));
$articles = get_posts(array('post_type'=>'post','post_status'=>'publish','numberposts'=>1,'orderby'=>'date','order'=>'DESC'));
$generic = get_posts(array(
  'post_type'=>'page','post_status'=>'publish','numberposts'=>1,
  'meta_query'=>array(array('key'=>'_wp_page_template','value'=>'page-templates/generic-content.php')),
));

$contacts_locations = array();
if ($contacts && function_exists('get_field')) {
  $rows = get_field('contacts_locations', $contacts->ID);
  if (is_array($rows)) {
    foreach ($rows as $i => $row) {
      if (!is_array($row)) continue;
      $code = isset($row['map_embed_code']) ? (string)$row['map_embed_code'] : '';
      $contacts_locations[] = array(
        'index' => $i,
        'title' => isset($row['title']) ? (string)$row['title'] : '',
        'has_map_embed_code' => '' !== trim($code),
        'map_embed_code_len' => strlen($code),
        'map_embed_code_sha256' => '' !== trim($code) ? hash('sha256', $code) : null,
        'map_scroll' => !empty($row['map_scroll']),
        'simplified' => !empty($row['simplified']),
      );
    }
  }
}

$activity = array();
if (function_exists('acf_get_store')) {
  // noop — keep for future
}
global $wpdb;
$log_rows = $wpdb->get_results(
  "SELECT ID, post_date_gmt, post_title FROM {$wpdb->posts}
   WHERE post_type='fp02_activity_log' AND post_status='publish'
   ORDER BY post_date_gmt DESC LIMIT 8",
  ARRAY_A
);
if ($log_rows) {
  foreach ($log_rows as $r) {
    $activity[] = array('ID'=>$r['ID'],'date_gmt'=>$r['post_date_gmt'],'title'=>$r['post_title']);
  }
}

$out = array(
  'blog_public' => (int)get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'theme_version' => wp_get_theme('shpigovsky')->get('Version'),
  'page_on_front' => $front,
  'page_for_posts' => $posts_page,
  'seo' => array(
    'front_page' => fp02_seo_fields($front),
    'posts_page' => fp02_seo_fields($posts_page),
    'specialists_hub_1030' => fp02_seo_fields(1030),
    'contacts' => $contacts ? fp02_seo_fields($contacts->ID) : null,
    'services_hub' => $uslugi ? fp02_seo_fields($uslugi->ID) : null,
    'o_centre' => $o_centre ? fp02_seo_fields($o_centre->ID) : null,
    'reviews' => $reviews ? fp02_seo_fields($reviews->ID) : null,
    'privacy' => $privacy ? fp02_seo_fields($privacy->ID) : null,
    'service_sample' => !empty($services) ? fp02_seo_fields($services[0]->ID) : null,
    'specialist_sample' => !empty($specialists) ? fp02_seo_fields($specialists[0]->ID) : null,
    'article_sample' => !empty($articles) ? fp02_seo_fields($articles[0]->ID) : null,
    'generic_content_sample' => !empty($generic) ? fp02_seo_fields($generic[0]->ID) : null,
  ),
  'page_1030' => get_post(1030) ? array(
    'ID'=>1030,
    'post_name'=>get_post_field('post_name',1030),
    'template'=>get_page_template_slug(1030),
    'permalink'=>get_permalink(1030),
  ) : null,
  'contacts_page' => $contacts ? array(
    'ID'=>$contacts->ID,
    'permalink'=>get_permalink($contacts),
    'template'=>get_page_template_slug($contacts),
    'locations'=>$contacts_locations,
  ) : null,
  'activity_log_recent' => $activity,
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

    # robots.txt snapshot
    robots_remote = f"{DOCROOT}/robots.txt"
    with sftp.open(robots_remote, "rb") as rf:
        robots = rf.read()
    OUT.joinpath("01-robots-before.txt").write_bytes(robots)
    OUT.joinpath("01-robots-before.sha256").write_text(sha256_bytes(robots), encoding="utf-8")
    print("ROBOTS_SHA", sha256_bytes(robots))

    probe = f"{DOCROOT}/wp-content/uploads/.fp02-nav-seo-maps-intake.php"
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
    print(data[:12000])
    if err.strip():
        print("ERR", err[:800])

    snaps = [
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/page-templates/specialists-hub.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/seo-entity-meta.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/yandex-map-embed.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/contacts/location-card.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/contacts-helpers.php",
        f"{DOCROOT}/wp-content/acf-json/group_fp02_page_contacts.json",
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
