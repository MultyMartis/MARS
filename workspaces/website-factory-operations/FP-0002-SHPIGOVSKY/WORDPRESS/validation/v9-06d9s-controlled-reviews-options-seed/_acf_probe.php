<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;
$group = $wpdb->get_var("SELECT post_content FROM {$wpdb->posts} WHERE post_type='acf-field-group' AND post_name='group_fp02_site_options_reviews'");
$data = maybe_unserialize($group);
$items_field = null;
if (function_exists('acf_get_field')) {
    $f = acf_get_field('field_fp02_reviews_items');
    $items_field = $f;
}
$subfields = [];
if (!empty($items_field['sub_fields'])) {
    foreach ($items_field['sub_fields'] as $sf) {
        $subfields[] = ['key' => $sf['key'], 'name' => $sf['name'], 'label' => $sf['label'], 'type' => $sf['type']];
    }
}
$out = [
    'group_exists' => !empty($group),
    'items_field' => $items_field ? ['key' => $items_field['key'], 'name' => $items_field['name']] : null,
    'subfields' => $subfields,
];
file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9s-controlled-reviews-options-seed/_acf_probe.json', json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
