<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;
$rows = $wpdb->get_results("SELECT option_name, LEFT(option_value, 120) AS preview FROM {$wpdb->options} WHERE option_name LIKE '%reviews%' ORDER BY option_name");
$out = ['options_keys' => $rows];

$raw = get_field('reviews_items', 'option');
$out['get_field_reviews_items'] = is_array($raw) ? count($raw) : $raw;
if (is_array($raw) && !empty($raw)) {
    $out['first_row_keys'] = array_keys($raw[0]);
    $out['first_row'] = $raw[0];
}

$opt = shpigovsky_get_reviews_option_items();
$items = shpigovsky_get_reviews_items(['limit' => 10, 'featured_only' => true]);
$out['option_items_count'] = count($opt);
$out['resolved_count'] = count($items);
$out['first_resolved'] = $items[0] ?? null;
$out['source_mode'] = empty($opt) ? 'FALLBACK' : ((!empty($items[0]['is_demo'])) ? 'FALLBACK' : 'OPTIONS');

file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9s-controlled-reviews-options-seed/_probe.json', json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
