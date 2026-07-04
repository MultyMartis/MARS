<?php
/**
 * Read-only main-query simulation for route ownership.
 * No option/content writes.
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/route-ownership-investigation';

function roi_main_query_probe($path) {
    global $wp, $wp_query, $wp_the_query;

    $path = '/' . trim($path, '/') . '/';
    if ($path === '//') {
        $path = '/';
    }

    // Reset globals for a clean main query simulation.
    $wp->query_vars = [];
    $wp->matched_rule = '';
    $wp->matched_query = '';
    $wp->request = '';
    $wp->did_permalink = false;

    $_SERVER['REQUEST_URI'] = $path;
    $_SERVER['HTTP_HOST'] = 'shpigovsky.test';
    $_SERVER['HTTPS'] = '';
    $_SERVER['SERVER_NAME'] = 'shpigovsky.test';

    $wp->init();
    $wp->parse_request();
    $wp->query_posts();
    $wp->register_globals();

    $obj = get_queried_object();
    $out = [
        'path' => $path,
        'request' => $wp->request,
        'matched_rule' => $wp->matched_rule,
        'matched_query' => $wp->matched_query,
        'query_vars' => $wp->query_vars,
        'is_404' => (bool) is_404(),
        'is_page' => (bool) is_page(),
        'is_single' => (bool) is_single(),
        'is_singular' => (bool) is_singular(),
        'is_singular_service' => (bool) is_singular('service'),
        'queried_object_id' => $obj && isset($obj->ID) ? (int) $obj->ID : null,
        'queried_object_post_type' => $obj && isset($obj->post_type) ? $obj->post_type : null,
        'queried_object_title' => $obj && isset($obj->post_title) ? $obj->post_title : null,
    ];

    // Also test get_page_by_path variants for service.
    $segments = array_values(array_filter(explode('/', trim($path, '/'))));
    if (count($segments) >= 2 && $segments[0] === 'uslugi') {
        $leaf = $segments[count($segments) - 1];
        $full = implode('/', array_slice($segments, 1));
        $leaf_obj = get_page_by_path($leaf, OBJECT, 'service');
        $full_obj = get_page_by_path($full, OBJECT, 'service');
        $page_obj = get_page_by_path(implode('/', $segments), OBJECT, 'page');
        $out['lookups'] = [
            'service_leaf' => $leaf_obj ? (int) $leaf_obj->ID : null,
            'service_full_hierarchy' => $full_obj ? (int) $full_obj->ID : null,
            'page_full_path' => $page_obj ? (int) $page_obj->ID : null,
        ];
    }

    // Template hierarchy candidate (no include).
    if ($out['queried_object_post_type'] === 'service') {
        $out['template_candidate'] = 'single-service.php';
        $theme = get_stylesheet_directory();
        $out['template_exists'] = file_exists($theme . '/single-service.php');
    } elseif ($out['queried_object_post_type'] === 'page') {
        $slug = get_page_template_slug($out['queried_object_id']);
        $out['template_candidate'] = $slug !== '' ? $slug : 'page.php';
    } else {
        $out['template_candidate'] = is_404() ? '404.php' : null;
    }

    return $out;
}

$paths = [
    '/uslugi/zavisimosti/',
    '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
    '/uslugi/psihicheskoe-zdorovie/',
    '/uslugi/rasstroystva-pischevogo-povedeniya/',
];

$results = [];
foreach ($paths as $p) {
    $results[$p] = roi_main_query_probe($p);
}

// Explicit repair simulation: what if rewrite used full path?
$repair_leaf = get_page_by_path('lechenie-alkogolnoy-zavisimosti', OBJECT, 'service');
$repair_full = get_page_by_path('zavisimosti/lechenie-alkogolnoy-zavisimosti', OBJECT, 'service');

// Native CPT rule would set service=$matches[1] with full path from uslugi/(.+?)
// Custom top rule sets service=$matches[2] leaf only.

$payload = [
    'phase' => 'ROUTE-OWNERSHIP-INVESTIGATION',
    'timestamp' => date('c'),
    'main_query_probes' => $results,
    'repair_simulation' => [
        'current_rewrite_query_var' => 'lechenie-alkogolnoy-zavisimosti',
        'current_lookup_id' => $repair_leaf ? (int) $repair_leaf->ID : null,
        'repaired_rewrite_query_var' => 'zavisimosti/lechenie-alkogolnoy-zavisimosti',
        'repaired_lookup_id' => $repair_full ? (int) $repair_full->ID : null,
        'repair_would_resolve_service_74' => $repair_full && (int) $repair_full->ID === 74,
    ],
    'native_cpt_rule_note' => 'Native hierarchical CPT rule uslugi/(.+?)(?:/([0-9]+))?/?$ maps service=$matches[1] (full path). Custom top rule ^uslugi/([^/]+)/([^/]+)/?$ maps service=$matches[2] (leaf only) and shadows the native rule.',
];

file_put_contents(
    $evidence_dir . '/wp-request-diagnostics-main-query.json',
    json_encode($payload, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n"
);

echo json_encode([
    'zavisimosti' => [
        'id' => $results['/uslugi/zavisimosti/']['queried_object_id'],
        'type' => $results['/uslugi/zavisimosti/']['queried_object_post_type'],
        'rule' => $results['/uslugi/zavisimosti/']['matched_rule'],
        'is_404' => $results['/uslugi/zavisimosti/']['is_404'],
    ],
    'service_74' => [
        'id' => $results['/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/']['queried_object_id'],
        'type' => $results['/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/']['queried_object_post_type'],
        'rule' => $results['/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/']['matched_rule'],
        'query_vars_service' => $results['/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/']['query_vars']['service'] ?? null,
        'is_404' => $results['/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/']['is_404'],
        'lookups' => $results['/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/']['lookups'] ?? null,
    ],
    'control_77' => [
        'id' => $results['/uslugi/psihicheskoe-zdorovie/']['queried_object_id'],
        'is_404' => $results['/uslugi/psihicheskoe-zdorovie/']['is_404'],
    ],
    'control_84' => [
        'id' => $results['/uslugi/rasstroystva-pischevogo-povedeniya/']['queried_object_id'],
        'is_404' => $results['/uslugi/rasstroystva-pischevogo-povedeniya/']['is_404'],
    ],
    'repair' => $payload['repair_simulation'],
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n";
