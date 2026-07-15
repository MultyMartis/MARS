<?php
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$json_path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_site_options_reviews.json';
$raw = json_decode(file_get_contents($json_path), true);

$group = acf_get_field_group('group_fp02_site_options_reviews');
$deleted = [];
if ($group && !empty($group['ID'])) {
    $fields = acf_get_fields($group['key']);
    if (is_array($fields)) {
        foreach ($fields as $field) {
            if (!empty($field['ID'])) {
                acf_delete_field($field['ID']);
                $deleted[] = $field['name'] . ':' . $field['key'];
            }
            if (!empty($field['sub_fields'])) {
                foreach ($field['sub_fields'] as $sub) {
                    if (!empty($sub['ID'])) {
                        acf_delete_field($sub['ID']);
                        $deleted[] = $sub['name'] . ':' . $sub['key'];
                    }
                }
            }
        }
    }
    acf_delete_field_group($group['ID']);
    $deleted[] = 'group:' . $group['key'];
}

$result = acf_import_field_group($raw);
$after = acf_get_field('field_fp02_reviews_items');
$after_subs = [];
if (!empty($after['sub_fields'])) {
    foreach ($after['sub_fields'] as $sf) {
        $after_subs[] = $sf['name'];
    }
}

echo json_encode([
    'deleted' => $deleted,
    'after_subfield_names' => $after_subs,
    'result' => in_array('review_author', $after_subs, true) ? 'PASS' : 'FAIL',
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
