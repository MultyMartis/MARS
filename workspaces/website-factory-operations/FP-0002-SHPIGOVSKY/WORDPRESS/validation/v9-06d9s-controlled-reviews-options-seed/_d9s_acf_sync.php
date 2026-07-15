<?php
/**
 * FP-0002 V9-06D9-S — sync reviews ACF group from canonical JSON (TEMP — NOT FOR GIT).
 * Prerequisite: runtime DB had legacy author_label schema; canonical D9-R schema required for seed.
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$json_path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_site_options_reviews.json';
$raw = json_decode(file_get_contents($json_path), true);
if (!is_array($raw) || !function_exists('acf_import_field_group')) {
    echo json_encode(['result' => 'FAIL', 'error' => 'acf_import_field_group unavailable']);
    exit(1);
}

$before = acf_get_field('field_fp02_reviews_items');
$before_subs = [];
if (!empty($before['sub_fields'])) {
    foreach ($before['sub_fields'] as $sf) {
        $before_subs[] = $sf['name'];
    }
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
    'phase' => 'V9-06D9-S',
    'generated_at' => gmdate('c'),
    'before_subfield_names' => $before_subs,
    'after_subfield_names' => $after_subs,
    'import_result' => $result,
    'result' => in_array('review_author', $after_subs, true) ? 'PASS' : 'FAIL',
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
