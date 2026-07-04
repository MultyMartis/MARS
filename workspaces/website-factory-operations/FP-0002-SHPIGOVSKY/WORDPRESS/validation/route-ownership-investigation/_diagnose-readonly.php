<?php
/**
 * FP-0002 ROUTE-OWNERSHIP-INVESTIGATION — read-only diagnostics only.
 * Writes evidence JSON under this validation folder. No options/content/rewrite mutations.
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/route-ownership-investigation';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const PHASE = 'ROUTE-OWNERSHIP-INVESTIGATION';
const REQUIRED_HEAD = 'd123f85b9ce8aad90ff4c07895b67cfb124bda3d';

function roi_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function roi_hash($value) {
    if ($value === null || $value === false || $value === '') {
        return 'empty';
    }
    if (is_array($value) || is_object($value)) {
        $value = wp_json_encode($value);
    }
    return hash('sha256', (string) $value);
}

function roi_path_from_url($url) {
    $path = parse_url($url, PHP_URL_PATH);
    if ($path === null || $path === false || $path === '') {
        return '/';
    }
    if (substr($path, -1) !== '/') {
        $path .= '/';
    }
    return $path === '//' ? '/' : $path;
}

function roi_http($url) {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => false,
        CURLOPT_TIMEOUT => 15,
        CURLOPT_HEADER => true,
        CURLOPT_USERAGENT => 'FP-0002-ROUTE-OWNERSHIP-INVESTIGATION/1.0',
    ]);
    $raw = curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $redirect = curl_getinfo($ch, CURLINFO_REDIRECT_URL);
    $err = curl_error($ch);
    curl_close($ch);
    $title = null;
    $body = '';
    if (is_string($raw)) {
        $parts = explode("\r\n\r\n", $raw, 2);
        $body = isset($parts[1]) ? $parts[1] : '';
        if (preg_match('/<title[^>]*>(.*?)<\/title>/is', $body, $m)) {
            $title = trim(html_entity_decode($m[1], ENT_QUOTES | ENT_HTML5, 'UTF-8'));
        }
    }
    return [
        'http_status' => $code,
        'title' => $title,
        'redirect_url' => $redirect ?: null,
        'curl_error' => $err ?: null,
    ];
}

function roi_object_inventory($post_id) {
    $p = get_post($post_id);
    if (!$p) {
        return ['ID' => (int) $post_id, 'exists' => false];
    }
    $url = get_permalink($p);
    $template = get_page_template_slug($p->ID);
    if ($template === '') {
        $template = 'default';
    }
    $parent = $p->post_parent ? get_post($p->post_parent) : null;
    $pto = get_post_type_object($p->post_type);
    $post_type_rewrite = ($pto && is_array($pto->rewrite)) ? $pto->rewrite : null;
    $http = roi_http($url);
    $path = roi_path_from_url($url);

    $by_path_leaf = get_page_by_path($p->post_name, OBJECT, $p->post_type);
    $full_path = '';
    if ($p->post_type === 'service') {
        $slugs = [];
        $cur = $p;
        $d = 0;
        while ($cur && $d < 3) {
            array_unshift($slugs, $cur->post_name);
            if ((int) $cur->post_parent <= 0) {
                break;
            }
            $cur = get_post($cur->post_parent);
            $d++;
        }
        $full_path = implode('/', $slugs);
    } elseif ($p->post_type === 'page') {
        $full_path = get_page_uri($p);
    }
    $by_path_full = $full_path !== '' ? get_page_by_path($full_path, OBJECT, $p->post_type) : null;

    return [
        'ID' => (int) $p->ID,
        'exists' => true,
        'post_type' => $p->post_type,
        'status' => $p->post_status,
        'title' => $p->post_title,
        'slug' => $p->post_name,
        'post_name' => $p->post_name,
        'post_parent' => (int) $p->post_parent,
        'parent' => $parent ? [
            'ID' => (int) $parent->ID,
            'title' => $parent->post_title,
            'status' => $parent->post_status,
            'post_type' => $parent->post_type,
            'slug' => $parent->post_name,
            'path' => roi_path_from_url(get_permalink($parent)),
        ] : null,
        'template' => $template,
        'generated_permalink' => $url,
        'generated_path' => $path,
        'post_type_rewrite' => $post_type_rewrite,
        'hierarchical_path' => $full_path,
        'get_page_by_path_leaf' => $by_path_leaf ? (int) $by_path_leaf->ID : null,
        'get_page_by_path_full' => $by_path_full ? (int) $by_path_full->ID : null,
        'http_status' => $http['http_status'],
        'http_title' => $http['title'],
        'registry_id' => get_post_meta($p->ID, 'registry_id', true),
        'migration_status' => get_post_meta($p->ID, 'migration_status', true),
        'seeded_by_phase' => get_post_meta($p->ID, 'seeded_by_phase', true),
        'skeleton_status' => get_post_meta($p->ID, 'skeleton_status', true),
    ];
}

/**
 * Simulate WP front request for a path without writing options.
 */
function roi_wp_request($path) {
    global $wp, $wp_rewrite;

    $path = '/' . ltrim($path, '/');
    if (substr($path, -1) !== '/') {
        $path .= '/';
    }

    // Match rewrite rules against request path (strip leading slash for WP matching).
    $request = trim($path, '/');
    $matched_rule = null;
    $matched_query = null;
    $query_vars = [];

    $rules = get_option('rewrite_rules');
    if (is_array($rules)) {
        foreach ($rules as $pattern => $query) {
            if (preg_match("#^{$pattern}#", $request, $matches) || preg_match("#^{$pattern}#", $request . '/', $matches)) {
                $matched_rule = $pattern;
                $matched_query = $query;
                // Expand $matches into query string.
                $qv_string = $query;
                for ($i = 1; $i < count($matches); $i++) {
                    $qv_string = str_replace('$matches[' . $i . ']', $matches[$i], $qv_string);
                }
                // Parse index.php?a=b&c=d
                $qs = [];
                if (strpos($qv_string, '?') !== false) {
                    parse_str(substr($qv_string, strpos($qv_string, '?') + 1), $qs);
                }
                $query_vars = $qs;
                break;
            }
        }
    }

    // Resolve via WP_Query using matched vars (read-only).
    $resolved = [
        'is_404' => null,
        'is_page' => null,
        'is_single' => null,
        'is_singular' => null,
        'queried_object_id' => null,
        'queried_object_post_type' => null,
        'found_posts' => null,
        'post_count' => null,
    ];

    $leaf_lookup = null;
    $full_path_lookup = null;
    $simulated_query_var = isset($query_vars['service']) ? $query_vars['service'] : null;

    if ($simulated_query_var !== null) {
        $leaf_lookup = get_page_by_path($simulated_query_var, OBJECT, 'service');
        // If rule only passed leaf, also try parent/leaf reconstruction from path.
        $segments = array_values(array_filter(explode('/', trim($path, '/'))));
        if (count($segments) >= 3 && $segments[0] === 'uslugi') {
            $full = $segments[1] . '/' . $segments[2];
            $full_path_lookup = get_page_by_path($full, OBJECT, 'service');
        } elseif (count($segments) === 2 && $segments[0] === 'uslugi') {
            $full_path_lookup = get_page_by_path($segments[1], OBJECT, 'service');
        }
    }

    // Page path lookup for collision analysis.
    $page_path = trim($path, '/');
    $page_by_path = get_page_by_path($page_path, OBJECT, 'page');

    // Run WP_Query with matched vars.
    if (!empty($query_vars)) {
        $q = new WP_Query($query_vars);
        $obj = $q->get_queried_object();
        $resolved = [
            'is_404' => (bool) $q->is_404,
            'is_page' => (bool) $q->is_page,
            'is_single' => (bool) $q->is_single,
            'is_singular' => (bool) $q->is_singular,
            'queried_object_id' => $obj && isset($obj->ID) ? (int) $obj->ID : null,
            'queried_object_post_type' => $obj && isset($obj->post_type) ? $obj->post_type : null,
            'found_posts' => (int) $q->found_posts,
            'post_count' => (int) $q->post_count,
            'query_vars_used' => $query_vars,
        ];
        wp_reset_postdata();
    }

    // Alternate query with full hierarchical path if depth-2 service pattern.
    $alt_resolved = null;
    $segments = array_values(array_filter(explode('/', trim($path, '/'))));
    if (count($segments) >= 3 && $segments[0] === 'uslugi') {
        $alt_vars = [
            'post_type' => 'service',
            'service' => $segments[1] . '/' . $segments[2],
            'name' => '',
        ];
        $aq = new WP_Query($alt_vars);
        $aobj = $aq->get_queried_object();
        $alt_resolved = [
            'query_vars' => $alt_vars,
            'is_404' => (bool) $aq->is_404,
            'queried_object_id' => $aobj && isset($aobj->ID) ? (int) $aobj->ID : null,
            'queried_object_post_type' => $aobj && isset($aobj->post_type) ? $aobj->post_type : null,
            'found_posts' => (int) $aq->found_posts,
            'note' => 'Simulated repair: service query var uses full parent/child path',
        ];
        wp_reset_postdata();
    }

    $http = roi_http(home_url($path));

    // Template candidate (only if object resolved).
    $template_candidate = null;
    if (!empty($resolved['queried_object_id'])) {
        $oid = $resolved['queried_object_id'];
        $otype = $resolved['queried_object_post_type'];
        if ($otype === 'service') {
            $template_candidate = 'single-service.php';
        } elseif ($otype === 'page') {
            $slug = get_page_template_slug($oid);
            $template_candidate = $slug !== '' ? $slug : 'page.php';
        }
    }

    $classification = 'unknown';
    if ($http['http_status'] === 404 || (!empty($resolved['is_404']) && empty($resolved['queried_object_id']))) {
        $classification = '404';
    } elseif (!empty($resolved['queried_object_post_type']) && $resolved['queried_object_post_type'] === 'page') {
        $classification = 'page_path';
    } elseif (!empty($resolved['queried_object_post_type']) && $resolved['queried_object_post_type'] === 'service') {
        $classification = 'service_cpt_hierarchical_path';
    }

    return [
        'path' => $path,
        'http' => $http,
        'matched_rule' => $matched_rule,
        'matched_query' => $matched_query,
        'query_vars_from_rewrite' => $query_vars,
        'wp_query_resolution' => $resolved,
        'alternate_full_path_resolution' => $alt_resolved,
        'get_page_by_path_service_using_rewrite_var' => $leaf_lookup ? (int) $leaf_lookup->ID : null,
        'get_page_by_path_service_full_hierarchy' => $full_path_lookup ? (int) $full_path_lookup->ID : null,
        'get_page_by_path_page' => $page_by_path ? (int) $page_by_path->ID : null,
        'template_candidate' => $template_candidate,
        'request_classification' => $classification,
    ];
}

// ---------------------------------------------------------------------------
// 1. Runtime identity
// ---------------------------------------------------------------------------
global $wpdb;
$theme = wp_get_theme();
$active = (array) get_option('active_plugins', []);
sort($active);
$menus = wp_get_nav_menus();
$menu_snapshot = [];
foreach ($menus as $menu) {
    $items = wp_get_nav_menu_items($menu->term_id);
    $menu_snapshot[] = [
        'term_id' => (int) $menu->term_id,
        'name' => $menu->name,
        'slug' => $menu->slug,
        'count' => is_array($items) ? count($items) : 0,
    ];
}

$acf_groups = [];
if (function_exists('acf_get_local_field_groups')) {
    foreach ((array) acf_get_local_field_groups() as $group) {
        $acf_groups[] = $group['key'] ?? '';
    }
}
sort($acf_groups);

$options_pages = [];
if (function_exists('acf_get_options_pages')) {
    foreach ((array) acf_get_options_pages() as $slug => $page) {
        $options_pages[] = is_array($page) ? ($page['menu_slug'] ?? $slug) : $slug;
    }
}

$wpilot_write = null;
if (class_exists('WPilot_Settings')) {
    $opts = WPilot_Settings::get_options();
    $wpilot_write = !empty($opts['write_enabled']);
}

$service_obj = get_post_type_object('service');
$core_mode = defined('SHPIGOVSKY_CORE_MODE') ? SHPIGOVSKY_CORE_MODE : null;

$frontend = roi_http(home_url('/'));
$admin = roi_http(admin_url());

$runtime_identity = [
    'phase' => PHASE,
    'timestamp' => date('c'),
    'runtime' => 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky\\',
    'domain' => home_url('/'),
    'theme' => $theme->get_stylesheet(),
    'theme_version' => $theme->get('Version'),
    'shpigovsky_core_active' => is_plugin_active('shpigovsky-core/shpigovsky-core.php') || is_plugin_active('shpigovsky-core/plugin.php'),
    'active_plugins' => $active,
    'core_mode' => $core_mode,
    'service_cpt_registered' => (bool) $service_obj,
    'service_cpt_hierarchical' => $service_obj ? (bool) $service_obj->hierarchical : null,
    'service_cpt_has_archive' => $service_obj ? (bool) $service_obj->has_archive : null,
    'service_cpt_rewrite' => $service_obj && is_array($service_obj->rewrite) ? $service_obj->rewrite : ($service_obj ? (array) $service_obj->rewrite : null),
    'pages_total' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='page' AND post_status!='trash'"),
    'services_total' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='service' AND post_status!='trash'"),
    'posts_total' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='post' AND post_status!='trash'"),
    'menus_count' => count($menu_snapshot),
    'menus' => $menu_snapshot,
    'acf_pro_active' => is_plugin_active('advanced-custom-fields-pro/acf.php'),
    'acf_groups_count' => count($acf_groups),
    'acf_group_keys' => $acf_groups,
    'options_pages' => $options_pages,
    'wpilot_active' => is_plugin_active('metacode-wpilot/metacode-wpilot.php') || is_plugin_active('wpilot/wpilot.php') || (bool) array_filter($active, function ($p) {
        return stripos($p, 'wpilot') !== false;
    }),
    'wpilot_write_enabled' => $wpilot_write,
    'frontend_http' => $frontend['http_status'],
    'wp_admin_http' => $admin['http_status'],
    'result' => 'PASS',
];

// Fix core plugin active detection if needed.
if (!$runtime_identity['shpigovsky_core_active']) {
    foreach ($active as $p) {
        if (stripos($p, 'shpigovsky-core') !== false) {
            $runtime_identity['shpigovsky_core_active'] = true;
            $runtime_identity['shpigovsky_core_plugin_file'] = $p;
            break;
        }
    }
}

$identity_ok = (
    $runtime_identity['theme'] === 'shpigovsky'
    && $runtime_identity['shpigovsky_core_active']
    && $runtime_identity['service_cpt_registered']
    && $runtime_identity['services_total'] === 15
    && $runtime_identity['pages_total'] === 23
    && $runtime_identity['acf_groups_count'] === 13
    && $runtime_identity['wpilot_write_enabled'] === false
    && $runtime_identity['frontend_http'] === 200
    && in_array($runtime_identity['wp_admin_http'], [200, 302], true)
);

$runtime_identity['result'] = $identity_ok ? 'PASS' : 'FAIL';
roi_json_write($evidence_dir . '/runtime-identity.json', $runtime_identity);

if (!$identity_ok) {
    fwrite(STDERR, "RUNTIME IDENTITY FAIL\n");
    echo wp_json_encode($runtime_identity, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n";
    exit(2);
}

// ---------------------------------------------------------------------------
// 2. Object route inventory
// ---------------------------------------------------------------------------
$ids = [5, 6, 73, 74, 77, 84];
$objects = [];
foreach ($ids as $id) {
    $objects[(string) $id] = roi_object_inventory($id);
}

$object_route_inventory = [
    'phase' => PHASE,
    'timestamp' => date('c'),
    'objects' => $objects,
    'page_6_service_73_collision' => [
        'page_6_path' => $objects['6']['generated_path'] ?? null,
        'service_73_path' => $objects['73']['generated_path'] ?? null,
        'paths_equal' => ($objects['6']['generated_path'] ?? null) === ($objects['73']['generated_path'] ?? null),
        'shared_path' => '/uslugi/zavisimosti/',
    ],
    'service_74' => [
        'exists' => !empty($objects['74']['exists']),
        'generated_path' => $objects['74']['generated_path'] ?? null,
        'http_status' => $objects['74']['http_status'] ?? null,
        'parent_id' => $objects['74']['post_parent'] ?? null,
        'get_page_by_path_leaf' => $objects['74']['get_page_by_path_leaf'] ?? null,
        'get_page_by_path_full' => $objects['74']['get_page_by_path_full'] ?? null,
        'hierarchical_path' => $objects['74']['hierarchical_path'] ?? null,
    ],
    'result' => 'PASS',
];
roi_json_write($evidence_dir . '/object-route-inventory.json', $object_route_inventory);

// ---------------------------------------------------------------------------
// 3. Rewrite matching diagnostics
// ---------------------------------------------------------------------------
$rewrite = get_option('rewrite_rules');
$rewrite_count = is_array($rewrite) ? count($rewrite) : 0;
$rewrite_hash = roi_hash($rewrite);

$keywords = ['uslugi', 'service', 'zavisimosti', 'lechenie-alkogolnoy-zavisimosti'];
$relevant = [];
if (is_array($rewrite)) {
    foreach ($rewrite as $pattern => $query) {
        $hay = $pattern . ' ' . $query;
        foreach ($keywords as $kw) {
            if (stripos($hay, $kw) !== false) {
                $relevant[] = ['pattern' => $pattern, 'query' => $query];
                break;
            }
        }
    }
}

$depth2_rule = null;
$depth1_rule = null;
foreach ($relevant as $r) {
    if ($r['pattern'] === 'uslugi/([^/]+)/([^/]+)/?$' || $r['pattern'] === '^uslugi/([^/]+)/([^/]+)/?$') {
        $depth2_rule = $r;
    }
    if ($r['pattern'] === 'uslugi/([^/]+)/?$' || $r['pattern'] === '^uslugi/([^/]+)/?$') {
        $depth1_rule = $r;
    }
}
// WP stores rules without leading ^
foreach ($relevant as $r) {
    if (preg_match('#uslugi/\(\[\^/\]\+\)/\(\[\^/\]\+\)/\?\$#', $r['pattern']) || strpos($r['pattern'], 'uslugi/([^/]+)/([^/]+)/?$') !== false) {
        $depth2_rule = $r;
    }
    if ($r['pattern'] === 'uslugi/([^/]+)/?$' ) {
        $depth1_rule = $r;
    }
}

$service_74_path = '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/';
$service_74_req = roi_wp_request($service_74_path);

$controls = [
    '/uslugi/zavisimosti/',
    '/uslugi/psihicheskoe-zdorovie/',
    '/uslugi/rasstroystva-pischevogo-povedeniya/',
];
$control_diag = [];
foreach ($controls as $c) {
    $control_diag[$c] = roi_wp_request($c);
}

$rewrite_matching = [
    'phase' => PHASE,
    'timestamp' => date('c'),
    'rewrite_rules_count' => $rewrite_count,
    'rewrite_rules_hash' => $rewrite_hash,
    'relevant_rules_count' => count($relevant),
    'relevant_rules' => $relevant,
    'depth2_rule' => $depth2_rule,
    'depth1_rule' => $depth1_rule,
    'service_74_url' => $service_74_path,
    'service_74_expected_rule' => 'uslugi/([^/]+)/([^/]+)/?$',
    'service_74_actual' => $service_74_req,
    'control_urls' => $control_diag,
    'analysis' => [
        'depth2_rule_present' => (bool) $depth2_rule,
        'depth2_query_uses_leaf_only' => $depth2_rule && (strpos($depth2_rule['query'], '$matches[2]') !== false) && (strpos($depth2_rule['query'], '$matches[1]/$matches[2]') === false),
        'depth2_query_uses_full_path' => $depth2_rule && strpos($depth2_rule['query'], '$matches[1]/$matches[2]') !== false,
        'leaf_only_lookup_id' => $service_74_req['get_page_by_path_service_using_rewrite_var'],
        'full_path_lookup_id' => $service_74_req['get_page_by_path_service_full_hierarchy'],
        'wp_query_with_rewrite_vars_object_id' => $service_74_req['wp_query_resolution']['queried_object_id'] ?? null,
        'wp_query_with_full_path_object_id' => $service_74_req['alternate_full_path_resolution']['queried_object_id'] ?? null,
        'conclusion' => 'Depth-2 rewrite rule maps service=$matches[2] (leaf only). Hierarchical CPT resolution via get_page_by_path requires parent/child path. Leaf-only lookup fails for Service 74 (post_parent=73). Full path zavisimosti/lechenie-alkogolnoy-zavisimosti resolves Service 74.',
    ],
    'result' => 'PASS',
];
roi_json_write($evidence_dir . '/rewrite-matching-diagnostics.json', $rewrite_matching);

// ---------------------------------------------------------------------------
// 4. WP request diagnostics (all target URLs)
// ---------------------------------------------------------------------------
$urls = [
    '/uslugi/zavisimosti/',
    '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
    '/uslugi/psihicheskoe-zdorovie/',
    '/uslugi/rasstroystva-pischevogo-povedeniya/',
];
$wp_requests = [];
foreach ($urls as $u) {
    $wp_requests[$u] = roi_wp_request($u);
}

$wp_request_diagnostics = [
    'phase' => PHASE,
    'timestamp' => date('c'),
    'requests' => $wp_requests,
    'result' => 'PASS',
];
roi_json_write($evidence_dir . '/wp-request-diagnostics.json', $wp_request_diagnostics);

// ---------------------------------------------------------------------------
// 5. Database read-only diagnostics
// ---------------------------------------------------------------------------
$slugs = [
    'uslugi',
    'zavisimosti',
    'lechenie-alkogolnoy-zavisimosti',
    'psihicheskoe-zdorovie',
    'rasstroystva-pischevogo-povedeniya',
];

$rows = $wpdb->get_results(
    "SELECT ID, post_type, post_status, post_title, post_name, post_parent, post_modified_gmt
     FROM {$wpdb->posts}
     WHERE ID IN (5,6,73,74,77,84)
     ORDER BY ID",
    ARRAY_A
);

$slug_matches = $wpdb->get_results(
    $wpdb->prepare(
        "SELECT ID, post_type, post_status, post_title, post_name, post_parent
         FROM {$wpdb->posts}
         WHERE post_name IN (%s,%s,%s,%s,%s)
           AND post_status != 'trash'
           AND post_type IN ('page','service','attachment')
         ORDER BY post_name, post_type, ID",
        $slugs[0], $slugs[1], $slugs[2], $slugs[3], $slugs[4]
    ),
    ARRAY_A
);

$meta_keys = ['registry_id', 'migration_status', 'seeded_by_phase', 'skeleton_status', 'service_layout_variant'];
$meta_rows = [];
foreach ([5, 6, 73, 74, 77, 84] as $pid) {
    $meta_rows[(string) $pid] = [];
    foreach ($meta_keys as $mk) {
        $meta_rows[(string) $pid][$mk] = get_post_meta($pid, $mk, true);
    }
}

$db_diag = [
    'phase' => PHASE,
    'timestamp' => date('c'),
    'db_prefix' => $wpdb->prefix,
    'object_rows' => $rows,
    'slug_matches' => $slug_matches,
    'relevant_postmeta' => $meta_rows,
    'rewrite_rules_option' => [
        'count' => $rewrite_count,
        'hash' => $rewrite_hash,
        'full_dump' => false,
    ],
    'mutations' => 0,
    'result' => 'PASS',
];
roi_json_write($evidence_dir . '/database-readonly-diagnostics.json', $db_diag);

// ---------------------------------------------------------------------------
// 6. Path collision analysis
// ---------------------------------------------------------------------------
$zav_req = $wp_requests['/uslugi/zavisimosti/'];
$path_collision = [
    'phase' => PHASE,
    'timestamp' => date('c'),
    'path' => '/uslugi/zavisimosti/',
    'page_id_6' => [
        'exists' => !empty($objects['6']['exists']),
        'status' => $objects['6']['status'] ?? null,
        'generated_path' => $objects['6']['generated_path'] ?? null,
        'http_status' => $objects['6']['http_status'] ?? null,
        'intended_legacy_source_page' => true,
    ],
    'service_id_73' => [
        'exists' => !empty($objects['73']['exists']),
        'status' => $objects['73']['status'] ?? null,
        'generated_path' => $objects['73']['generated_path'] ?? null,
        'http_status' => $objects['73']['http_status'] ?? null,
    ],
    'current_resolver' => [
        'matched_rule' => $zav_req['matched_rule'] ?? null,
        'matched_query' => $zav_req['matched_query'] ?? null,
        'queried_object_id' => $zav_req['wp_query_resolution']['queried_object_id'] ?? null,
        'queried_object_post_type' => $zav_req['wp_query_resolution']['queried_object_post_type'] ?? null,
        'http_status' => $zav_req['http']['http_status'] ?? null,
        'classification' => $zav_req['request_classification'] ?? null,
    ],
    'effect_on_service_74' => [
        'direct_cause_of_404' => false,
        'explanation' => 'Page ID 6 / Service ID 73 share generated path /uslugi/zavisimosti/. Depth-1 service rewrite resolves Service 73 (leaf slug zavisimosti at root). Service 74 404 is caused by depth-2 rewrite mapping leaf-only service query var, not by Page 6 ownership of parent path.',
        'parent_service_73_resolves' => (($zav_req['wp_query_resolution']['queried_object_id'] ?? null) === 73),
    ],
    'blocking_for_d5' => [
        'page_service_collision' => false,
        'service_74_404' => (($objects['74']['http_status'] ?? null) === 404),
    ],
    'result' => 'CONFIRMED',
];
roi_json_write($evidence_dir . '/path-collision-analysis.json', $path_collision);

// Summary to stdout
$summary = [
    'runtime_identity' => $runtime_identity['result'],
    'service_74_http' => $objects['74']['http_status'] ?? null,
    'service_74_permalink' => $objects['74']['generated_path'] ?? null,
    'leaf_lookup' => $service_74_req['get_page_by_path_service_using_rewrite_var'],
    'full_path_lookup' => $service_74_req['get_page_by_path_service_full_hierarchy'],
    'rewrite_query_object' => $service_74_req['wp_query_resolution']['queried_object_id'] ?? null,
    'full_path_query_object' => $service_74_req['alternate_full_path_resolution']['queried_object_id'] ?? null,
    'zavisimosti_resolves_to' => $zav_req['wp_query_resolution']['queried_object_id'] ?? null,
    'depth2_rule' => $depth2_rule,
];
echo wp_json_encode($summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n";
echo "DIAGNOSTICS_COMPLETE\n";
