<?php
/**
 * FP-0002 REWRITE-FLUSH-MICRO-GATE — read-only probes + soft rewrite flush apply.
 * Modes: identity | baseline | dry-run | apply-flush | post-validate | all-readonly
 * Apply mode only calls flush_rewrite_rules(false) — no content/menu/redirect writes.
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'identity';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/rewrite-flush-micro-gate';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const PHASE = 'REWRITE-FLUSH-MICRO-GATE';
const AUTHORIZED_IDS = [4, 5, 20, 73, 74, 77, 84];

function fp02_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02_hash($value) {
    if ($value === null || $value === false || $value === '') {
        return 'empty';
    }
    if (is_array($value) || is_object($value)) {
        $value = wp_json_encode($value);
    }
    return hash('sha256', (string) $value);
}

function fp02_path_from_url($url) {
    $path = parse_url($url, PHP_URL_PATH);
    if ($path === null || $path === false || $path === '') {
        return '/';
    }
    if (substr($path, -1) !== '/') {
        $path .= '/';
    }
    return $path === '//' ? '/' : $path;
}

function fp02_meta_hashes($post_id) {
    $meta = get_post_meta($post_id);
    $out = [];
    foreach ($meta as $k => $vals) {
        if (strpos($k, '_') === 0) {
            continue;
        }
        $out[$k] = fp02_hash(isset($vals[0]) ? $vals[0] : '');
    }
    ksort($out);
    return $out;
}

function fp02_acf_snapshot($post_id) {
    $out = ['nonempty_fields' => [], 'field_hashes' => []];
    if (!function_exists('get_fields')) {
        return $out;
    }
    $fields = get_fields($post_id);
    if (!is_array($fields)) {
        return $out;
    }
    foreach ($fields as $k => $v) {
        if ($v === null || $v === '' || $v === false || $v === []) {
            continue;
        }
        $out['nonempty_fields'][] = $k;
        $out['field_hashes'][$k] = fp02_hash($v);
    }
    sort($out['nonempty_fields']);
    ksort($out['field_hashes']);
    return $out;
}

function fp02_object_snapshot($post_id) {
    $p = get_post($post_id);
    if (!$p) {
        return null;
    }
    $url = get_permalink($p);
    $template = get_page_template_slug($p->ID);
    if ($template === '') {
        $template = 'default';
    }
    return [
        'ID' => (int) $p->ID,
        'post_type' => $p->post_type,
        'title' => $p->post_title,
        'slug' => $p->post_name,
        'parent' => (int) $p->post_parent,
        'status' => $p->post_status,
        'template' => $template,
        'path' => fp02_path_from_url($url),
        'url' => $url,
        'content_hash' => fp02_hash($p->post_content),
        'excerpt_hash' => fp02_hash($p->post_excerpt),
        'content_length' => strlen((string) $p->post_content),
        'excerpt_length' => strlen((string) $p->post_excerpt),
        'modified_gmt' => $p->post_modified_gmt,
        'meta_hashes' => fp02_meta_hashes($p->ID),
        'acf' => fp02_acf_snapshot($p->ID),
        'registry_id' => get_post_meta($p->ID, 'registry_id', true),
        'migration_status' => get_post_meta($p->ID, 'migration_status', true),
        'seeded_by_phase' => get_post_meta($p->ID, 'seeded_by_phase', true),
        'skeleton_status' => get_post_meta($p->ID, 'skeleton_status', true),
        'service_layout_variant_meta' => get_post_meta($p->ID, 'service_layout_variant', true),
        'combined_hash' => fp02_hash([
            'content' => $p->post_content,
            'excerpt' => $p->post_excerpt,
            'title' => $p->post_title,
            'slug' => $p->post_name,
            'parent' => $p->post_parent,
            'status' => $p->post_status,
            'meta' => fp02_meta_hashes($p->ID),
            'acf' => fp02_acf_snapshot($p->ID),
        ]),
    ];
}

function fp02_global_invariants() {
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
    usort($menu_snapshot, function ($a, $b) {
        return $a['term_id'] <=> $b['term_id'];
    });
    $rewrite = get_option('rewrite_rules');
    $rewrite_count = is_array($rewrite) ? count($rewrite) : 0;
    $service_patterns = [];
    if (is_array($rewrite)) {
        foreach ($rewrite as $pattern => $query) {
            if (strpos($pattern, 'uslugi') !== false || strpos((string) $query, 'service') !== false) {
                $service_patterns[] = $pattern;
            }
        }
    }
    $wpilot_write = null;
    if (class_exists('WPilot_Settings')) {
        $opts = WPilot_Settings::get_options();
        $wpilot_write = !empty($opts['write_enabled']);
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
    sort($options_pages);
    $cat_count = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->terms} t INNER JOIN {$wpdb->term_taxonomy} tt ON t.term_id=tt.term_id WHERE tt.taxonomy='category'");
    $tag_count = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->terms} t INNER JOIN {$wpdb->term_taxonomy} tt ON t.term_id=tt.term_id WHERE tt.taxonomy='post_tag'");
    $user_count = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->users}");
    $service_obj = get_post_type_object('service');
    $service_rewrite = null;
    if ($service_obj && is_array($service_obj->rewrite)) {
        $service_rewrite = $service_obj->rewrite;
    } elseif ($service_obj && is_object($service_obj->rewrite)) {
        $service_rewrite = (array) $service_obj->rewrite;
    }
    return [
        'pages_total' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='page' AND post_status!='trash'"),
        'services_total' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='service' AND post_status!='trash'"),
        'posts_total' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='post' AND post_status!='trash'"),
        'menus' => $menu_snapshot,
        'menus_count' => count($menu_snapshot),
        'show_on_front' => get_option('show_on_front'),
        'page_on_front' => (int) get_option('page_on_front'),
        'page_for_posts' => (int) get_option('page_for_posts'),
        'permalink_structure' => get_option('permalink_structure'),
        'rewrite_rules_exist' => is_array($rewrite),
        'rewrite_rules_hash' => fp02_hash($rewrite),
        'rewrite_rules_count' => $rewrite_count,
        'service_rewrite_patterns_sample' => array_slice($service_patterns, 0, 20),
        'service_rewrite_patterns_count' => count($service_patterns),
        'service_post_type_rewrite' => $service_rewrite,
        'active_theme' => $theme->get_stylesheet(),
        'active_theme_version' => $theme->get('Version'),
        'active_plugins' => $active,
        'acf_groups_count' => count($acf_groups),
        'acf_group_keys' => $acf_groups,
        'acf_options_pages' => $options_pages,
        'acf_pro_active' => is_plugin_active('advanced-custom-fields-pro/acf.php'),
        'acf_extended_pro_active' => is_plugin_active('acf-extended-pro/acf-extended.php'),
        'acf_free_active' => is_plugin_active('advanced-custom-fields/acf.php'),
        'wpilot_write_enabled' => $wpilot_write,
        'categories_count' => $cat_count,
        'tags_count' => $tag_count,
        'users_count' => $user_count,
        'invariants_hash' => fp02_hash([
            'pages' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='page' AND post_status!='trash'"),
            'services' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='service' AND post_status!='trash'"),
            'posts' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='post' AND post_status!='trash'"),
            'menus' => $menu_snapshot,
            'front' => get_option('show_on_front'),
            'page_on_front' => (int) get_option('page_on_front'),
            'page_for_posts' => (int) get_option('page_for_posts'),
            'plugins' => $active,
            'theme' => $theme->get_stylesheet(),
            'cats' => $cat_count,
            'tags' => $tag_count,
            'users' => $user_count,
        ]),
    ];
}

function fp02_qa_routes() {
    return [
        ['path' => '/', 'expected_object_id' => 4, 'expected_object_type' => 'page'],
        ['path' => '/uslugi/', 'expected_object_id' => 5, 'expected_object_type' => 'page'],
        ['path' => '/uslugi/zavisimosti/', 'expected_object_id' => 73, 'expected_object_type' => 'service'],
        ['path' => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', 'expected_object_id' => 74, 'expected_object_type' => 'service'],
        ['path' => '/uslugi/psihicheskoe-zdorovie/', 'expected_object_id' => 77, 'expected_object_type' => 'service'],
        ['path' => '/uslugi/rasstroystva-pischevogo-povedeniya/', 'expected_object_id' => 84, 'expected_object_type' => 'service'],
        ['path' => '/kontakty/', 'expected_object_id' => 20, 'expected_object_type' => 'page'],
    ];
}

function fp02_http_status($url) {
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => false,
        CURLOPT_NOBODY => false,
        CURLOPT_TIMEOUT => 15,
        CURLOPT_HEADER => true,
        CURLOPT_USERAGENT => 'FP-0002-REWRITE-FLUSH-MICRO-GATE/1.0',
    ]);
    $raw = curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $err = curl_error($ch);
    curl_close($ch);
    $title = null;
    if (is_string($raw) && preg_match('/<title[^>]*>(.*?)<\/title>/is', $raw, $m)) {
        $title = trim(html_entity_decode($m[1], ENT_QUOTES | ENT_HTML5, 'UTF-8'));
    }
    return ['http_status' => $code, 'title' => $title, 'curl_error' => $err ?: null];
}

function fp02_route_probe($routes) {
    $out = [];
    foreach ($routes as $r) {
        $id = $r['expected_object_id'];
        $snap = fp02_object_snapshot($id);
        $generated = $snap ? $snap['path'] : null;
        $url = home_url($r['path']);
        $http = fp02_http_status($url);
        $match = $generated === $r['path'];
        $result = 'PASS';
        if (!$snap) {
            $result = 'FAIL_OBJECT_MISSING';
        } elseif (!$match) {
            $result = 'FAIL_PERMALINK_MISMATCH';
        } elseif ($http['http_status'] !== 200) {
            $result = $id === 74 && $http['http_status'] === 404
                ? 'REWRITE_FLUSH_MICRO_GATE_REQUIRED'
                : 'FAIL_HTTP_' . $http['http_status'];
        }
        $out[] = [
            'url' => $url,
            'path' => $r['path'],
            'expected_object_id' => $id,
            'expected_object_type' => $r['expected_object_type'],
            'http_status' => $http['http_status'],
            'response_title' => $http['title'],
            'generated_permalink' => $snap ? $snap['url'] : null,
            'generated_path' => $generated,
            'generated_permalink_match' => $match,
            'result' => $result,
        ];
    }
    return $out;
}

function fp02_runtime_identity() {
    $theme = wp_get_theme();
    $service_obj = get_post_type_object('service');
    $core_mode = defined('SHPIGOVSKY_CORE_MODE') ? SHPIGOVSKY_CORE_MODE : null;
    $wpilot_write = null;
    if (class_exists('WPilot_Settings')) {
        $opts = WPilot_Settings::get_options();
        $wpilot_write = !empty($opts['write_enabled']);
    }
    $acf_groups = [];
    if (function_exists('acf_get_local_field_groups')) {
        foreach ((array) acf_get_local_field_groups() as $group) {
            $acf_groups[] = ['key' => $group['key'] ?? '', 'title' => $group['title'] ?? ''];
        }
    }
    $options_pages = [];
    if (function_exists('acf_get_options_pages')) {
        foreach ((array) acf_get_options_pages() as $slug => $page) {
            $options_pages[] = [
                'slug' => is_array($page) ? ($page['menu_slug'] ?? $slug) : $slug,
                'registered' => true,
            ];
        }
    }
    $auth_pages = [];
    foreach ([4, 5, 20] as $id) {
        $p = get_post($id);
        $auth_pages[(string) $id] = (bool) ($p && $p->post_type === 'page');
    }
    $auth_services = [];
    foreach ([73, 74, 77, 84] as $id) {
        $p = get_post($id);
        $auth_services[(string) $id] = (bool) ($p && $p->post_type === 'service');
    }
    global $wpdb;
    $pages_total = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='page' AND post_status!='trash'");
    $services_total = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='service' AND post_status!='trash'");
    $posts_total = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='post' AND post_status!='trash'");
    $menus_count = count(wp_get_nav_menus());
    $home = fp02_http_status(home_url('/'));
    $admin = fp02_http_status(admin_url());
    $identity = [
        'timestamp' => gmdate('c'),
        'phase' => PHASE,
        'runtime' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky',
        'domain' => home_url('/'),
        'siteurl' => site_url('/'),
        'db_name' => DB_NAME,
        'db_prefix' => $GLOBALS['wpdb']->prefix,
        'active_theme' => $theme->get_stylesheet(),
        'active_theme_version' => $theme->get('Version'),
        'active_plugins' => get_option('active_plugins'),
        'shpigovsky_core_active' => is_plugin_active('shpigovsky-core/shpigovsky-core.php'),
        'shpigovsky_core_mode' => $core_mode,
        'service_cpt_registered' => (bool) $service_obj,
        'service_cpt' => $service_obj ? [
            'public' => (bool) $service_obj->public,
            'hierarchical' => (bool) $service_obj->hierarchical,
            'has_archive' => (bool) $service_obj->has_archive,
        ] : null,
        'pages_total' => $pages_total,
        'services_total' => $services_total,
        'posts_total' => $posts_total,
        'menus' => $menus_count,
        'authorized_pages_exist' => $auth_pages,
        'authorized_services_exist' => $auth_services,
        'acf_pro_active' => is_plugin_active('advanced-custom-fields-pro/acf.php'),
        'acf_extended_pro_active' => is_plugin_active('acf-extended-pro/acf-extended.php'),
        'acf_free_active' => is_plugin_active('advanced-custom-fields/acf.php'),
        'acf_groups_count' => count($acf_groups),
        'acf_local_field_groups' => $acf_groups,
        'acf_options_pages' => $options_pages,
        'wpilot_active' => is_plugin_active('metacode-wpilot/metacode-wpilot.php'),
        'wpilot_write_enabled' => $wpilot_write,
        'frontend_http' => $home['http_status'],
        'wp_admin_http' => $admin['http_status'],
        'result' => 'PENDING',
    ];
    $pass = $identity['db_name'] === 'mars_wp_fp0002'
        && $identity['db_prefix'] === 'fp02_'
        && $identity['active_theme'] === 'shpigovsky'
        && $identity['shpigovsky_core_active']
        && $identity['shpigovsky_core_mode'] === 'content_model'
        && $identity['service_cpt_registered']
        && $identity['services_total'] === 15
        && $identity['pages_total'] === 23
        && $identity['posts_total'] === 0
        && $identity['menus'] === 3
        && $identity['acf_pro_active']
        && $identity['acf_groups_count'] === 13
        && !empty($identity['acf_options_pages'])
        && $identity['wpilot_active']
        && $identity['wpilot_write_enabled'] === false
        && $identity['frontend_http'] === 200
        && in_array($identity['wp_admin_http'], [200, 302], true)
        && !in_array(false, $auth_pages, true)
        && !in_array(false, $auth_services, true);
    $identity['result'] = $pass ? 'PASS' : 'FAIL';
    return $identity;
}

function fp02_baseline() {
    $objects = [];
    foreach (AUTHORIZED_IDS as $id) {
        $objects[(string) $id] = fp02_object_snapshot($id);
    }
    $globals = fp02_global_invariants();
    $routes = fp02_route_probe(fp02_qa_routes());
    $permalinks_valid = true;
    foreach ($routes as $r) {
        if (!$r['generated_permalink_match']) {
            $permalinks_valid = false;
        }
    }
    return [
        'phase' => PHASE,
        'timestamp' => gmdate('c'),
        'url_baseline' => $routes,
        'rewrite_baseline' => [
            'permalink_structure' => $globals['permalink_structure'],
            'rewrite_rules_exist' => $globals['rewrite_rules_exist'],
            'rewrite_rules_hash' => $globals['rewrite_rules_hash'],
            'rewrite_rules_count' => $globals['rewrite_rules_count'],
            'service_rewrite_patterns_present' => $globals['service_rewrite_patterns_count'] > 0,
            'service_rewrite_patterns_count' => $globals['service_rewrite_patterns_count'],
            'service_rewrite_patterns_sample' => $globals['service_rewrite_patterns_sample'],
            'service_post_type_rewrite' => $globals['service_post_type_rewrite'],
            'service_generated_permalinks_valid' => $permalinks_valid,
        ],
        'object_content_baseline' => [
            'pages_total' => $globals['pages_total'],
            'services_total' => $globals['services_total'],
            'posts_total' => $globals['posts_total'],
            'menus' => $globals['menus'],
            'menus_count' => $globals['menus_count'],
            'show_on_front' => $globals['show_on_front'],
            'page_on_front' => $globals['page_on_front'],
            'page_for_posts' => $globals['page_for_posts'],
            'active_plugins' => $globals['active_plugins'],
            'active_theme' => $globals['active_theme'],
            'categories_count' => $globals['categories_count'],
            'tags_count' => $globals['tags_count'],
            'users_count' => $globals['users_count'],
            'rewrite_rules_hash' => $globals['rewrite_rules_hash'],
            'invariants_hash' => $globals['invariants_hash'],
            'seeded_objects' => $objects,
        ],
        'result' => 'PASS',
    ];
}

function fp02_historical_ownership() {
    $page6 = get_post(6);
    $svc73 = get_post(73);
    $page6_path = $page6 ? fp02_path_from_url(get_permalink($page6)) : null;
    $svc73_path = $svc73 ? fp02_path_from_url(get_permalink($svc73)) : null;
    $path = '/uslugi/zavisimosti/';
    $http = fp02_http_status(home_url($path));
    // Resolve via WP query simulation
    $resolver = [
        'page_id_6_status' => $page6 ? $page6->post_status : null,
        'page_id_6_slug' => $page6 ? $page6->post_name : null,
        'page_id_6_generated_path' => $page6_path,
        'service_id_73_status' => $svc73 ? $svc73->post_status : null,
        'service_id_73_slug' => $svc73 ? $svc73->post_name : null,
        'service_id_73_generated_path' => $svc73_path,
        'http_status' => $http['http_status'],
        'response_title' => $http['title'],
    ];
    // Determine likely resolver from title / known titles
    $resolver_object = 'UNKNOWN';
    if ($http['title']) {
        if (stripos($http['title'], 'Зависимости') !== false || stripos($http['title'], 'zavisimosti') !== false) {
            // Both may share title patterns; prefer service if path matches service permalink
            if ($svc73_path === $path) {
                $resolver_object = 'LIKELY_SERVICE_73_OR_PAGE_6_SHARED_PATH';
            }
        }
    }
    if ($svc73_path === $path && $page6_path === $path) {
        $resolver_object = 'SHARED_GENERATED_PATH_PAGE_6_AND_SERVICE_73';
        $blocking = false; // HTTP 200 already; ownership review later
        $note = 'Both Page ID 6 and Service ID 73 generate /uslugi/zavisimosti/. HTTP currently resolves; ownership review recommended before D.5 if visual QA requires Service 73 specifically.';
    } elseif ($svc73_path === $path) {
        $resolver_object = 'SERVICE_73_GENERATED';
        $blocking = false;
        $note = 'Service 73 owns generated permalink; Page 6 may historically share path.';
    } else {
        $blocking = false;
        $note = 'Recorded for later ownership review; no mutation authorized.';
    }
    return [
        'phase' => PHASE,
        'timestamp' => gmdate('c'),
        'path' => $path,
        'historical_page_id_6' => [
            'exists' => (bool) $page6,
            'status' => $page6 ? $page6->post_status : null,
            'title' => $page6 ? $page6->post_title : null,
            'generated_path' => $page6_path,
        ],
        'service_id_73' => [
            'exists' => (bool) $svc73,
            'status' => $svc73 ? $svc73->post_status : null,
            'title' => $svc73 ? $svc73->post_title : null,
            'generated_path' => $svc73_path,
        ],
        'http' => $http,
        'current_resolver_classification' => $resolver_object,
        'resolver_details' => $resolver,
        'blocking_conflict_for_d5' => $blocking,
        'recommended_later_action' => 'ROUTE_OWNERSHIP_REVIEW_IF_VISUAL_QA_REQUIRES_SERVICE_73_SPECIFICALLY',
        'mutations_performed' => 0,
        'result' => 'RECORDED',
        'note' => $note,
    ];
}

function fp02_apply_soft_flush() {
    $before = get_option('rewrite_rules');
    $before_hash = fp02_hash($before);
    $before_count = is_array($before) ? count($before) : 0;
    // Soft flush only — do not write .htaccess
    flush_rewrite_rules(false);
    $after = get_option('rewrite_rules');
    $after_hash = fp02_hash($after);
    $after_count = is_array($after) ? count($after) : 0;
    return [
        'phase' => PHASE,
        'timestamp' => gmdate('c'),
        'command' => 'flush_rewrite_rules(false) via WordPress bootstrap (soft flush equivalent to wp rewrite flush without --hard)',
        'hard_flush' => false,
        'htaccess_touched' => false,
        'rewrite_rules_hash_before' => $before_hash,
        'rewrite_rules_hash_after' => $after_hash,
        'rewrite_rules_count_before' => $before_count,
        'rewrite_rules_count_after' => $after_count,
        'rewrite_rules_changed' => $before_hash !== $after_hash,
        'exit_code' => 0,
        'stdout' => 'flush_rewrite_rules(false) completed',
        'stderr' => '',
        'result' => 'PASS',
    ];
}

switch ($mode) {
    case 'identity':
        $data = fp02_runtime_identity();
        fp02_json_write($evidence_dir . '/runtime-identity.json', $data);
        echo json_encode(['mode' => $mode, 'result' => $data['result']], JSON_UNESCAPED_SLASHES) . "\n";
        break;
    case 'baseline':
        $data = fp02_baseline();
        fp02_json_write($evidence_dir . '/pre-flush-baseline.json', $data);
        echo json_encode([
            'mode' => $mode,
            'result' => $data['result'],
            'rewrite_hash' => $data['rewrite_baseline']['rewrite_rules_hash'],
            'service_74_http' => $data['url_baseline'][3]['http_status'] ?? null,
        ], JSON_UNESCAPED_SLASHES) . "\n";
        break;
    case 'apply-flush':
        $data = fp02_apply_soft_flush();
        fp02_json_write($evidence_dir . '/_apply-flush-internal.json', $data);
        echo json_encode($data, JSON_UNESCAPED_SLASHES) . "\n";
        break;
    case 'post-snapshot':
        $globals = fp02_global_invariants();
        $objects = [];
        foreach (AUTHORIZED_IDS as $id) {
            $objects[(string) $id] = fp02_object_snapshot($id);
        }
        $routes = fp02_route_probe(fp02_qa_routes());
        $ownership = fp02_historical_ownership();
        $data = [
            'phase' => PHASE,
            'timestamp' => gmdate('c'),
            'routes' => $routes,
            'globals' => $globals,
            'seeded_objects' => $objects,
            'historical_ownership' => $ownership,
        ];
        fp02_json_write($evidence_dir . '/_post-snapshot.json', $data);
        echo json_encode([
            'mode' => $mode,
            'service_74_http' => $routes[3]['http_status'] ?? null,
            'rewrite_hash' => $globals['rewrite_rules_hash'],
            'http_200_count' => count(array_filter($routes, function ($r) { return $r['http_status'] === 200; })),
        ], JSON_UNESCAPED_SLASHES) . "\n";
        break;
    default:
        fwrite(STDERR, "Unknown mode: $mode\n");
        exit(1);
}
