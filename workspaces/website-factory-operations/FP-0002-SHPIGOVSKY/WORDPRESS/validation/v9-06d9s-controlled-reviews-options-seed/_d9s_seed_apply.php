<?php
/**
 * FP-0002 V9-06D9-S — reviews options seed apply (TEMPORARY — NOT FOR GIT).
 * Writes only reviews ACF option fields via update_field().
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$payload_path = $argv[1] ?? '';
if (!is_readable($payload_path)) {
    fwrite(STDERR, "Payload JSON path required\n");
    exit(1);
}

$payload = json_decode(file_get_contents($payload_path), true);
if (!is_array($payload)) {
    fwrite(STDERR, "Invalid payload JSON\n");
    exit(1);
}

if (!function_exists('update_field')) {
    echo json_encode(['result' => 'FAIL', 'error' => 'ACF update_field unavailable'], JSON_UNESCAPED_UNICODE);
    exit(1);
}

$before = [
    'reviews_enabled' => get_field('reviews_enabled', 'option'),
    'reviews_section_heading' => get_field('reviews_section_heading', 'option'),
    'reviews_items' => get_field('reviews_items', 'option'),
];

$writes = [];
$errors = [];

foreach (['reviews_enabled', 'reviews_section_heading', 'reviews_items'] as $field) {
    if (!array_key_exists($field, $payload)) {
        continue;
    }
    $ok = update_field($field, $payload[$field], 'option');
    $writes[] = [
        'field' => $field,
        'ok' => (bool) $ok,
    ];
    if (!$ok) {
        $errors[] = ['field' => $field, 'message' => 'update_field returned false'];
    }
}

$after = [
    'reviews_enabled' => get_field('reviews_enabled', 'option'),
    'reviews_section_heading' => get_field('reviews_section_heading', 'option'),
    'reviews_items' => get_field('reviews_items', 'option'),
];

$option_items = function_exists('shpigovsky_get_reviews_option_items')
    ? shpigovsky_get_reviews_option_items()
    : [];
$resolved = function_exists('shpigovsky_get_reviews_items')
    ? shpigovsky_get_reviews_items(['limit' => 10, 'featured_only' => true])
    : [];

$source_mode = 'UNKNOWN';
if (!empty($option_items)) {
    $first = reset($resolved);
    $source_mode = (!empty($first['is_demo'])) ? 'FALLBACK' : 'OPTIONS';
}

echo json_encode([
    'phase' => 'V9-06D9-S',
    'generated_at' => gmdate('c'),
    'writes' => $writes,
    'errors' => $errors,
    'before' => [
        'reviews_enabled' => $before['reviews_enabled'],
        'reviews_section_heading' => $before['reviews_section_heading'],
        'reviews_items_count' => is_array($before['reviews_items']) ? count($before['reviews_items']) : 0,
    ],
    'after' => [
        'reviews_enabled' => $after['reviews_enabled'],
        'reviews_section_heading' => $after['reviews_section_heading'],
        'reviews_items_count' => is_array($after['reviews_items']) ? count($after['reviews_items']) : 0,
    ],
    'option_items_resolved_count' => count($option_items),
    'resolved_items_count' => count($resolved),
    'source_mode' => $source_mode,
    'result' => empty($errors) ? 'PASS' : 'PARTIAL',
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
