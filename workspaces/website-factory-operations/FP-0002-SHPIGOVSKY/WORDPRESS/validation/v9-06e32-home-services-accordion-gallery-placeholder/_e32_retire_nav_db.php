<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out = array('actions' => array(), 'before' => array(), 'after' => array());

// Find all acf-field posts for home_service_nav*
$fields = get_posts(array(
  'post_type' => 'acf-field',
  'post_status' => 'any',
  'posts_per_page' => 100,
  'name' => '',
));
$targets = array();
foreach (get_posts(array('post_type'=>'acf-field','post_status'=>'any','posts_per_page'=>-1)) as $f) {
  $key = $f->post_excerpt; // ACF stores field key in post_name sometimes; name in post_excerpt
  // Actually for ACF: post_excerpt = field name, post_name = field key
  $fname = $f->post_excerpt;
  $fkey = $f->post_name;
  if (false !== strpos($fname, 'home_service_nav') || false !== strpos($fkey, 'home_service_nav')) {
    $targets[] = array('ID'=>(int)$f->ID,'status'=>$f->post_status,'name'=>$fname,'key'=>$fkey,'parent'=>(int)$f->post_parent,'title'=>$f->post_title);
  }
}
$out['before']['nav_field_posts'] = $targets;

// Also check group 114 fields via raw children
foreach (array(114,483,581,639) as $gid) {
  $kids = get_posts(array('post_type'=>'acf-field','post_parent'=>$gid,'post_status'=>'any','posts_per_page'=>50,'orderby'=>'menu_order','order'=>'ASC'));
  $names = array();
  foreach ($kids as $k) { $names[] = $k->post_excerpt . ':' . $k->post_status; }
  $out['before']['group_'.$gid] = $names;
}

// Retire: move matching field posts to trash (not permanent delete)
foreach ($targets as $t) {
  if ('trash' === $t['status']) {
    $out['actions'][] = array('ID'=>$t['ID'], 'action'=>'already_trash');
    continue;
  }
  $r = wp_trash_post($t['ID']);
  $out['actions'][] = array('ID'=>$t['ID'], 'action'=>'trash', 'result'=> (bool)$r, 'name'=>$t['name']);
}

// Clear ACF caches
if (function_exists('acf_get_store')) {
  // best-effort
}
if (function_exists('wp_cache_flush')) { wp_cache_flush(); }

// Re-check
$field = function_exists('acf_get_field') ? acf_get_field('field_fp02_home_service_nav_items') : null;
$out['after']['acf_get_field'] = $field ? array('ID'=>$field['ID']??0,'key'=>$field['key']??'','local'=>$field['local']??'') : null;

// Local JSON fields still without nav?
if (function_exists('acf_get_fields')) {
  $fields = acf_get_fields('group_fp02_page_home');
  $names = array();
  foreach ((array)$fields as $f) { $names[] = $f['name'] ?? ''; }
  $out['after']['group_fields'] = $names;
  $out['after']['has_nav'] = in_array('home_service_nav_items', $names, true);
}

file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-nav-retire.json', wp_json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
echo wp_json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
