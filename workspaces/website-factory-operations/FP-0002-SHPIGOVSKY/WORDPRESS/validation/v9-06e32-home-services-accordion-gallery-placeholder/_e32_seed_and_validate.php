<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$out = array(
  'seed' => array(),
  'home_gallery_included' => array(),
  'accordion' => array(),
  'admin' => array(),
  'routes' => array(),
  'placeholder' => array(),
  'home_checks' => array(),
);

// --- Seed service_show_on_home_gallery ---
$services = get_posts(array(
  'post_type' => 'service',
  'post_status' => 'publish',
  'posts_per_page' => -1,
  'orderby' => array('menu_order' => 'ASC', 'title' => 'ASC'),
));

$seeded = 0;
$skipped = 0;
foreach ($services as $p) {
  $eligible = function_exists('shpigovsky_service_is_home_gallery_depth_eligible')
    ? shpigovsky_service_is_home_gallery_depth_eligible($p->ID)
    : false;
  $value = $eligible ? 1 : 0;
  if (function_exists('update_field')) {
    update_field('field_fp02_service_show_on_home_gallery', $value, $p->ID);
  } else {
    update_post_meta($p->ID, 'service_show_on_home_gallery', $value);
    update_post_meta($p->ID, '_service_show_on_home_gallery', 'field_fp02_service_show_on_home_gallery');
  }
  $out['seed'][] = array('ID' => (int)$p->ID, 'title' => $p->post_title, 'eligible' => $eligible, 'value' => $value);
  if ($eligible) { $seeded++; } else { $skipped++; }
}
$out['seed_summary'] = array('eligible_true' => $seeded, 'non_eligible_false' => $skipped, 'total_publish' => count($services));

// Flush caches lightly
if (function_exists('wp_cache_flush')) { wp_cache_flush(); }

// --- Field presence ---
$field = function_exists('acf_get_field') ? acf_get_field('field_fp02_service_show_on_home_gallery') : null;
$nav = function_exists('acf_get_field') ? acf_get_field('field_fp02_home_service_nav_items') : null;
$out['admin']['home_gallery_flag_field'] = is_array($field) ? array('key' => $field['key'], 'label' => $field['label'], 'name' => $field['name']) : null;
$out['admin']['home_service_nav_items_field'] = $nav ? 'STILL_PRESENT' : 'REMOVED_OR_HIDDEN';
$out['admin']['uslugi_slider_field'] = function_exists('acf_get_field') && acf_get_field('field_fp02_service_show_in_slider') ? 'PRESENT' : 'MISSING';

// --- Home gallery slides inventory ---
$slides = function_exists('shpigovsky_get_home_gallery_service_slides') ? shpigovsky_get_home_gallery_service_slides() : array();
foreach ($slides as $s) {
  $resp = wp_remote_get($s['url'], array('timeout' => 12, 'redirection' => 5));
  $code = is_wp_error($resp) ? $resp->get_error_message() : (int) wp_remote_retrieve_response_code($resp);
  $parent = (int) get_post_field('post_parent', $s['id']);
  $out['home_gallery_included'][] = array(
    'ID' => $s['id'],
    'title' => $s['title'],
    'url' => $s['url'],
    'parent' => $parent,
    'depth' => 1,
    'flag' => get_post_meta($s['id'], 'service_show_on_home_gallery', true),
    'image_source' => $s['image_source'],
    'http' => $code,
  );
}

// --- Accordion groups ---
$groups = function_exists('shpigovsky_get_home_service_accordion_groups') ? shpigovsky_get_home_service_accordion_groups() : array();
foreach ($groups as $g) {
  $items = array();
  foreach ($g['items'] as $it) {
    $child_titles = array();
    foreach (($it['children'] ?? array()) as $c) { $child_titles[] = $c['title']; }
    $items[] = array('title' => $it['title'], 'url' => $it['url'], 'children' => $child_titles);
  }
  $out['accordion'][] = array('title' => $g['title'], 'item_count' => count($items), 'items' => $items);
}

// --- Placeholder ---
$ph = function_exists('shpigovsky_get_service_placeholder_image') ? shpigovsky_get_service_placeholder_image() : null;
$ph_http = null;
if ($ph && !empty($ph['url'])) {
  $resp = wp_remote_get($ph['url'], array('timeout' => 10));
  $ph_http = is_wp_error($resp) ? $resp->get_error_message() : (int) wp_remote_retrieve_response_code($resp);
}
$out['placeholder'] = array('asset' => $ph, 'http' => $ph_http);

// --- Routes ---
$routes = array('/', '/uslugi/', '/uslugi/zavisimosti/', '/uslugi/psihicheskoe-zdorovie/', '/uslugi/rasstroystva-pischevogo-povedeniya/', '/o-centre/', '/o-centre/programma-lecheniya/', '/blog/', '/kontakty/');
foreach ($routes as $r) {
  $resp = wp_remote_get(home_url($r), array('timeout' => 20));
  $code = is_wp_error($resp) ? $resp->get_error_message() : (int) wp_remote_retrieve_response_code($resp);
  $body = is_wp_error($resp) ? '' : wp_remote_retrieve_body($resp);
  $fatal = (false !== stripos($body, 'Fatal error') || false !== stripos($body, 'Uncaught Error'));
  $out['routes'][$r] = array('http' => $code, 'fatal' => $fatal, 'bytes' => strlen($body));
}

// --- Home HTML checks ---
$home = wp_remote_get(home_url('/'), array('timeout' => 25));
$body = is_wp_error($home) ? '' : wp_remote_retrieve_body($home);
$out['home_checks']['http'] = is_wp_error($home) ? $home->get_error_message() : (int) wp_remote_retrieve_response_code($home);
$out['home_checks']['has_accordion'] = (false !== strpos($body, 'home-treatment-prevention__accordion'));
$out['home_checks']['has_gallery'] = (false !== strpos($body, 'home-gallery'));
$out['home_checks']['has_gallery_link'] = (false !== strpos($body, 'home-gallery__link'));
$out['home_checks']['has_placeholder'] = (false !== strpos($body, 'service-placeholder.svg'));
$out['home_checks']['static_specialistam'] = (false !== strpos($body, 'Специалистам'));
$out['home_checks']['has_povedencheskie'] = (false !== strpos($body, 'Поведенческие зависимости'));
$out['home_checks']['has_depressiya'] = (false !== strpos($body, 'Депрессия'));
$out['home_checks']['has_narkoticheskoy'] = (false !== strpos($body, 'наркотической') || false !== strpos($body, 'Наркотической') || false !== strpos($body, 'Лечение наркотической'));
preg_match_all('/home-treatment-prevention__toggle-label">([^<]+)/', $body, $labs);
$out['home_checks']['accordion_groups'] = $labs[1] ?? array();
preg_match_all('/class="home-gallery__link"[^>]*href="([^"]+)"/', $body, $glinks);
$out['home_checks']['gallery_link_count'] = count($glinks[1] ?? array());
$out['home_checks']['gallery_link_sample'] = array_slice($glinks[1] ?? array(), 0, 5);
preg_match_all('/home-treatment-prevention__service-name">([^<]+)/', $body, $names);
$out['home_checks']['accordion_service_count'] = count($names[1] ?? array());
$out['home_checks']['accordion_service_sample'] = array_slice($names[1] ?? array(), 0, 12);

// Accordion link HTTP sample
$acc_links_ok = 0; $acc_links_fail = 0; $acc_checked = array();
preg_match_all('/class="home-treatment-prevention__service-item"[^>]*href="([^"]+)"/', $body, $alinks);
foreach (array_slice(array_unique($alinks[1] ?? array()), 0, 25) as $u) {
  $resp = wp_remote_get($u, array('timeout' => 10));
  $code = is_wp_error($resp) ? 0 : (int) wp_remote_retrieve_response_code($resp);
  $acc_checked[] = array('url' => $u, 'http' => $code);
  if (200 === $code) { $acc_links_ok++; } else { $acc_links_fail++; }
}
$out['home_checks']['accordion_links_checked'] = $acc_checked;
$out['home_checks']['accordion_links_ok'] = $acc_links_ok;
$out['home_checks']['accordion_links_fail'] = $acc_links_fail;

$dest = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e32-home-services-accordion-gallery-placeholder/e32-validation.json';
file_put_contents($dest, wp_json_encode($out, JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
echo "SEED_VALIDATE_OK gallery=".count($out['home_gallery_included'])." accordion_groups=".count($out['accordion'])." home=".$out['home_checks']['http']."\n";
