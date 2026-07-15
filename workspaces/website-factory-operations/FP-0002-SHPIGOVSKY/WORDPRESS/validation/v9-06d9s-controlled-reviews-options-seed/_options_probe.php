<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$groups = acf_get_field_groups(['options_page' => 'fp02-site-settings']);
$out = ['options_page_groups' => []];
foreach ($groups as $g) {
    $fields = acf_get_fields($g['key']);
    $field_names = [];
    if (is_array($fields)) {
        foreach ($fields as $f) {
            $subs = [];
            if (!empty($f['sub_fields'])) {
                foreach ($f['sub_fields'] as $sf) {
                    $subs[] = $sf['name'];
                }
            }
            $field_names[] = ['name' => $f['name'], 'key' => $f['key'], 'subfields' => $subs];
        }
    }
    $out['options_page_groups'][] = ['key' => $g['key'], 'title' => $g['title'], 'fields' => $field_names];
}

$opt_items = get_field('reviews_items', 'option');
$out['get_field_option_reviews_items'] = is_array($opt_items) ? count($opt_items) : $opt_items;
if (is_array($opt_items) && !empty($opt_items)) {
    $out['first_option_row'] = $opt_items[0];
}

$opt_resolved = shpigovsky_get_reviews_option_items();
$out['helper_option_items'] = count($opt_resolved);
if (!empty($opt_resolved)) {
    $out['helper_first'] = $opt_resolved[0];
}

file_put_contents('X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9s-controlled-reviews-options-seed/_options_probe.json', json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
