<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out = array();

// Where does Специалистам appear on home?
$home = wp_remote_get(home_url('/'), array('timeout' => 20));
$body = is_wp_error($home) ? '' : wp_remote_retrieve_body($home);
$pos = mb_strpos($body, 'Специалистам');
$out['specialistam_pos'] = $pos === false ? null : $pos;
if ($pos !== false) {
  $out['specialistam_context'] = mb_substr($body, max(0, $pos - 200), 400);
}
$out['in_accordion_block'] = false;
if (preg_match('/class="home-treatment-prevention__accordion".*?<\/div>\s*<\/div>\s*<\/section>/s', $body, $m)) {
  $out['in_accordion_block'] = false !== mb_strpos($m[0], 'Специалистам');
  $out['accordion_has_specialistam'] = $out['in_accordion_block'];
}

// Inspect ACF field source for home_service_nav_items
$field = acf_get_field('field_fp02_home_service_nav_items');
$out['nav_field'] = is_array($field) ? array(
  'key' => $field['key'] ?? '',
  'ID' => $field['ID'] ?? 0,
  'parent' => $field['parent'] ?? '',
  'local' => $field['local'] ?? '',
) : null;

// Find ACF field group posts
$groups = get_posts(array(
  'post_type' => array('acf-field-group', 'acf'),
  'post_status' => 'any',
  'posts_per_page' => 100,
  's' => 'Page — Home',
));
$out['acf_groups_search'] = array();
foreach ($groups as $g) {
  $out['acf_groups_search'][] = array('ID'=>$g->ID,'title'=>$g->post_title,'status'=>$g->post_status,'name'=>$g->post_name);
}

// Broader: all local groups keys
if (function_exists('acf_get_local_field_groups')) {
  foreach (acf_get_local_field_groups() as $g) {
    if (($g['key'] ?? '') === 'group_fp02_page_home') {
      $out['local_page_home'] = array(
        'title' => $g['title'] ?? '',
        'local' => $g['local'] ?? '',
        'modified' => $g['modified'] ?? '',
      );
      $fields = acf_get_fields($g['key']);
      $names = array();
      if (is_array($fields)) {
        foreach ($fields as $f) { $names[] = $f['name'] ?? $f['key']; }
      }
      $out['local_page_home_fields'] = $names;
      $out['local_has_nav'] = in_array('home_service_nav_items', $names, true);
    }
  }
}

// DB field group by key
$db_group = null;
if (function_exists('acf_get_field_group')) {
  $db_group = acf_get_field_group('group_fp02_page_home');
}
$out['acf_get_field_group'] = is_array($db_group) ? array(
  'ID' => $db_group['ID'] ?? 0,
  'key' => $db_group['key'] ?? '',
  'title' => $db_group['title'] ?? '',
  'local' => $db_group['local'] ?? '',
  'active' => $db_group['active'] ?? null,
) : null;

if (is_array($db_group) && !empty($db_group['ID'])) {
  $db_fields = acf_get_fields($db_group['ID']);
  $names = array();
  foreach ((array)$db_fields as $f) { $names[] = $f['name'] ?? ''; }
  $out['db_group_fields'] = $names;
  $out['db_has_nav'] = in_array('home_service_nav_items', $names, true);
}

file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-nav-field-probe.json', wp_json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
echo wp_json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
