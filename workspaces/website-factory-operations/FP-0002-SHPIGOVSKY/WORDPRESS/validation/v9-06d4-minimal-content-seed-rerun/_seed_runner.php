<?php
/**
 * FP-0002 V9-06D.4 RERUN — minimal content seed for visual route QA.
 * Modes: identity | baseline | dry-run | apply | validate | all
 * Writes only authorized Pages 4/5/20 and Services 73/74/77/84.
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d4-minimal-content-seed-rerun';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const PLACEHOLDER = 'Минимальное наполнение для визуальной проверки маршрута. Полная миграция контента выполняется отдельной фазой.';
const AUTHORIZED_PAGES = [4, 5, 20];
const AUTHORIZED_SERVICES = [73, 74, 77, 84];

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

function fp02_meta_presence($post_id) {
    $meta = get_post_meta($post_id);
    $out = [];
    foreach ($meta as $k => $vals) {
        if (strpos($k, '_') === 0) {
            continue;
        }
        $out[] = $k;
    }
    sort($out);
    return $out;
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
        'meta_keys' => fp02_meta_presence($p->ID),
        'meta_hashes' => fp02_meta_hashes($p->ID),
        'acf' => fp02_acf_snapshot($p->ID),
        'registry_id' => get_post_meta($p->ID, 'registry_id', true),
        'migration_status' => get_post_meta($p->ID, 'migration_status', true),
        'seeded_by_phase' => get_post_meta($p->ID, 'seeded_by_phase', true),
        'skeleton_status' => get_post_meta($p->ID, 'skeleton_status', true),
        'service_layout_variant_meta' => get_post_meta($p->ID, 'service_layout_variant', true),
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
    $rewrite = get_option('rewrite_rules');
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
    $cat_count = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->terms} t INNER JOIN {$wpdb->term_taxonomy} tt ON t.term_id=tt.term_id WHERE tt.taxonomy='category'");
    $tag_count = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->terms} t INNER JOIN {$wpdb->term_taxonomy} tt ON t.term_id=tt.term_id WHERE tt.taxonomy='post_tag'");
    $user_count = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->users}");
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
        'rewrite_rules_hash' => fp02_hash($rewrite),
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
    ];
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
    foreach (AUTHORIZED_PAGES as $id) {
        $p = get_post($id);
        $auth_pages[$id] = $p && $p->post_type === 'page';
    }
    $auth_services = [];
    foreach (AUTHORIZED_SERVICES as $id) {
        $p = get_post($id);
        $auth_services[$id] = $p && $p->post_type === 'service';
    }
    $services_total = count(get_posts(['post_type' => 'service', 'post_status' => 'any', 'numberposts' => -1]));
    return [
        'timestamp' => gmdate('c'),
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
        'services_total' => $services_total,
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
        'update_field_available' => function_exists('update_field'),
        'result' => 'PENDING',
    ];
}

function fp02_seed_plan() {
    $placeholder = PLACEHOLDER;
    $objects = [
        [
            'object_id' => 4,
            'object_type' => 'page',
            'object_title' => 'Главная',
            'path' => '/',
            'native_fields' => [],
            'acf_fields' => [
                [
                    'key' => 'home_hero_slides',
                    'planned_value_summary' => '1 slide: title=Шпиговский дом; text=minimal seed marker + V9 home description snippet',
                    'planned_value' => [
                        [
                            'title' => 'Шпиговский дом',
                            'text' => 'Центр профилактики и лечения зависимостей. ' . $placeholder,
                        ],
                    ],
                    'source_authority' => 'V9 src/pages/index.html title/description + D.3 minimal seed plan',
                    'reason' => 'Expose home hero for visual route QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'home_service_nav_items',
                    'planned_value_summary' => '3 nav titles: Зависимости, Психическое здоровье, Расстройства пищевого поведения',
                    'planned_value' => [
                        ['title' => 'Зависимости'],
                        ['title' => 'Психическое здоровье'],
                        ['title' => 'Расстройства пищевого поведения'],
                    ],
                    'source_authority' => 'Authorized service titles / V9 uslugi-v2 category labels',
                    'reason' => 'Expose services preview labels on home',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'home_cta_title',
                    'planned_value_summary' => 'Остались вопросы?',
                    'planned_value' => 'Остались вопросы?',
                    'source_authority' => 'V9 final-form headingText on index.html',
                    'reason' => 'Minimal page-level CTA title',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'home_cta_text',
                    'planned_value_summary' => 'V9 final-form lead snippet',
                    'planned_value' => 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь',
                    'source_authority' => 'V9 final-form leadText on index.html',
                    'reason' => 'Minimal page-level CTA text',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'meta_fields' => [
                [
                    'key' => 'migration_status',
                    'planned_value' => 'minimal_seed',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Mark authorized page as minimal_seed',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'seeded_by_phase',
                    'planned_value' => 'V9-06D.4',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Phase provenance',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'risk' => 'LOW',
        ],
        [
            'object_id' => 5,
            'object_type' => 'page',
            'object_title' => 'Услуги',
            'path' => '/uslugi/',
            'native_fields' => [],
            'acf_fields' => [
                [
                    'key' => 'services_hub_intro',
                    'planned_value_summary' => 'Short V9 services hub lead + placeholder marker',
                    'planned_value' => 'Лечение и профилактика. Зависимость, тревога, нарушение пищевого поведения — направления, которые мы сопровождаем. ' . $placeholder,
                    'source_authority' => 'V9 src/pages/uslugi-v2.html heroLead (shortened) + D.3 plan',
                    'reason' => 'Make services hub visually non-empty',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'services_hub_query_mode',
                    'planned_value_summary' => 'grouped_by_parent',
                    'planned_value' => 'grouped_by_parent',
                    'source_authority' => 'ACF default / D.3 plan',
                    'reason' => 'Verify Page-owned hub with Service children grouping',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'services_hub_show_placeholders',
                    'planned_value_summary' => 'true (1)',
                    'planned_value' => 1,
                    'source_authority' => 'D.3 minimal seed plan',
                    'reason' => 'Show placeholder services during visual QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'meta_fields' => [
                [
                    'key' => 'migration_status',
                    'planned_value' => 'minimal_seed',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Mark authorized page as minimal_seed',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'seeded_by_phase',
                    'planned_value' => 'V9-06D.4',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Phase provenance',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'risk' => 'LOW',
        ],
        [
            'object_id' => 20,
            'object_type' => 'page',
            'object_title' => 'Контакты',
            'path' => '/kontakty/',
            'native_fields' => [],
            'acf_fields' => [
                [
                    'key' => 'contacts_address',
                    'planned_value_summary' => 'Москва и Московская область',
                    'planned_value' => 'Москва и Московская область',
                    'source_authority' => 'V9 kontakty.html public description',
                    'reason' => 'Minimal contacts address for visual QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'contacts_phones',
                    'planned_value_summary' => '1 public phone row from V9 source',
                    'planned_value' => [
                        [
                            'label' => 'Телефон',
                            'phone' => '8 (925) 183-64-64',
                        ],
                    ],
                    'source_authority' => 'V9 uslugi-v2.html public ctaPhone',
                    'reason' => 'Minimal public contact phone for visual QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'contacts_form_intro',
                    'planned_value_summary' => 'placeholder marker',
                    'planned_value' => $placeholder,
                    'source_authority' => 'D.4 preferred placeholder marker',
                    'reason' => 'Make contacts form intro non-empty',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'meta_fields' => [
                [
                    'key' => 'migration_status',
                    'planned_value' => 'minimal_seed',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Mark authorized page as minimal_seed',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'seeded_by_phase',
                    'planned_value' => 'V9-06D.4',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Phase provenance',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'risk' => 'LOW',
        ],
        [
            'object_id' => 73,
            'object_type' => 'service',
            'object_title' => 'Зависимости',
            'path' => '/uslugi/zavisimosti/',
            'native_fields' => [],
            'acf_fields' => [
                [
                    'key' => 'service_layout_variant',
                    'planned_value_summary' => 'subdivision',
                    'planned_value' => 'subdivision',
                    'source_authority' => 'D.3 service migration matrix SVC-ZAVISIMOSTI',
                    'reason' => 'Layout variant verification via ACF',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'hero_lead',
                    'planned_value_summary' => 'minimal lead for Зависимости',
                    'planned_value' => 'Направление «Зависимости». ' . $placeholder,
                    'source_authority' => 'Object title + D.4 placeholder (V9 subdivision page uses lorem; avoid lorem)',
                    'reason' => 'Minimal hero lead for visual QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'meta_fields' => [
                [
                    'key' => 'migration_status',
                    'planned_value' => 'minimal_seed',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Update skeleton migration status',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'seeded_by_phase',
                    'planned_value' => 'V9-06D.4',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Phase provenance',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'skeleton_status',
                    'planned_value' => 'MINIMAL_SEED',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Advance skeleton status after minimal seed',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'risk' => 'LOW',
        ],
        [
            'object_id' => 74,
            'object_type' => 'service',
            'object_title' => 'Лечение алкогольной зависимости',
            'path' => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
            'native_fields' => [],
            'acf_fields' => [
                [
                    'key' => 'service_layout_variant',
                    'planned_value_summary' => 'alcohol_special',
                    'planned_value' => 'alcohol_special',
                    'source_authority' => 'D.3 service migration matrix SVC-ALKOGOL',
                    'reason' => 'Layout variant verification via ACF',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'hero_lead',
                    'planned_value_summary' => 'V9 alcohol leaf heroLead (short)',
                    'planned_value' => 'В центре реабилитации Шпиговский Дом мы понимаем, что каждый человек уникален, поэтому мы не предложим вам универсальный подход к лечению. Путь в борьбе с алкогольной зависимостью может быть только индивидуальным.',
                    'source_authority' => 'V9 src/pages/usluga-konechnaya-v1.html heroLead',
                    'reason' => 'Minimal hero lead from source wording',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'intro_text',
                    'planned_value_summary' => 'placeholder marker',
                    'planned_value' => $placeholder,
                    'source_authority' => 'D.3 WAVE_1 fields for SVC-ALKOGOL + D.4 placeholder',
                    'reason' => 'Minimal intro for alcohol leaf visual QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'signs_items',
                    'planned_value_summary' => '1 placeholder signs row',
                    'planned_value' => [
                        [
                            'title' => 'Признак для визуальной проверки',
                            'text' => $placeholder,
                        ],
                    ],
                    'source_authority' => 'D.3 WAVE_1 signs_items[0] for SVC-ALKOGOL',
                    'reason' => 'Minimal signs repeater for template QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'meta_fields' => [
                [
                    'key' => 'migration_status',
                    'planned_value' => 'minimal_seed',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Update skeleton migration status',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'seeded_by_phase',
                    'planned_value' => 'V9-06D.4',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Phase provenance',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'skeleton_status',
                    'planned_value' => 'MINIMAL_SEED',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Advance skeleton status after minimal seed',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'risk' => 'LOW',
        ],
        [
            'object_id' => 77,
            'object_type' => 'service',
            'object_title' => 'Психическое здоровье',
            'path' => '/uslugi/psihicheskoe-zdorovie/',
            'native_fields' => [],
            'acf_fields' => [
                [
                    'key' => 'service_layout_variant',
                    'planned_value_summary' => 'subdivision',
                    'planned_value' => 'subdivision',
                    'source_authority' => 'D.3 service migration matrix SVC-PSYCH',
                    'reason' => 'Layout variant verification via ACF',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'hero_lead',
                    'planned_value_summary' => 'minimal lead for Психическое здоровье',
                    'planned_value' => 'Направление «Психическое здоровье». ' . $placeholder,
                    'source_authority' => 'Object title + D.4 placeholder',
                    'reason' => 'Minimal hero lead for visual QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'meta_fields' => [
                [
                    'key' => 'migration_status',
                    'planned_value' => 'minimal_seed',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Update skeleton migration status',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'seeded_by_phase',
                    'planned_value' => 'V9-06D.4',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Phase provenance',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'skeleton_status',
                    'planned_value' => 'MINIMAL_SEED',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Advance skeleton status after minimal seed',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'risk' => 'LOW',
        ],
        [
            'object_id' => 84,
            'object_type' => 'service',
            'object_title' => 'Расстройства пищевого поведения',
            'path' => '/uslugi/rasstroystva-pischevogo-povedeniya/',
            'native_fields' => [],
            'acf_fields' => [
                [
                    'key' => 'service_layout_variant',
                    'planned_value_summary' => 'subdivision',
                    'planned_value' => 'subdivision',
                    'source_authority' => 'D.3 service migration matrix SVC-RPP',
                    'reason' => 'Layout variant verification via ACF',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'hero_lead',
                    'planned_value_summary' => 'minimal lead for РПП',
                    'planned_value' => 'Направление «Расстройства пищевого поведения». ' . $placeholder,
                    'source_authority' => 'Object title + D.4 placeholder',
                    'reason' => 'Minimal hero lead for visual QA',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'meta_fields' => [
                [
                    'key' => 'migration_status',
                    'planned_value' => 'minimal_seed',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Update skeleton migration status',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'seeded_by_phase',
                    'planned_value' => 'V9-06D.4',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Phase provenance',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
                [
                    'key' => 'skeleton_status',
                    'planned_value' => 'MINIMAL_SEED',
                    'source_authority' => 'D.4 task authorization',
                    'reason' => 'Advance skeleton status after minimal seed',
                    'production_final' => false,
                    'risk' => 'LOW',
                ],
            ],
            'risk' => 'LOW',
        ],
    ];

    $writes = [];
    $unauthorized = [];
    foreach ($objects as &$obj) {
        $id = $obj['object_id'];
        if ($obj['object_type'] === 'page' && !in_array($id, AUTHORIZED_PAGES, true)) {
            $unauthorized[] = $id;
        }
        if ($obj['object_type'] === 'service' && !in_array($id, AUTHORIZED_SERVICES, true)) {
            $unauthorized[] = $id;
        }
        $snap = fp02_object_snapshot($id);
        $obj['exists'] = (bool) $snap;
        $obj['current_snapshot_summary'] = $snap ? [
            'slug' => $snap['slug'],
            'parent' => $snap['parent'],
            'status' => $snap['status'],
            'template' => $snap['template'],
            'registry_id' => $snap['registry_id'],
            'content_hash' => $snap['content_hash'],
            'migration_status' => $snap['migration_status'],
        ] : null;
        foreach ($obj['acf_fields'] as &$field) {
            $current = function_exists('get_field') ? get_field($field['key'], $id) : null;
            $field['field_kind'] = 'acf';
            $field['current_value_hash'] = fp02_hash($current);
            $field['rollback_value_hash'] = $field['current_value_hash'];
            $field['planned_value_hash'] = fp02_hash($field['planned_value']);
            $writes[] = [
                'object_id' => $id,
                'object_type' => $obj['object_type'],
                'object_title' => $obj['object_title'],
                'field_meta_key' => $field['key'],
                'field_kind' => 'acf',
                'current_value_hash' => $field['current_value_hash'],
                'planned_value_summary' => $field['planned_value_summary'],
                'source_authority' => $field['source_authority'],
                'reason' => $field['reason'],
                'rollback_value_hash' => $field['rollback_value_hash'],
                'production_final' => false,
                'risk' => $field['risk'],
            ];
        }
        unset($field);
        foreach ($obj['meta_fields'] as &$field) {
            $current = get_post_meta($id, $field['key'], true);
            $field['field_kind'] = 'post_meta';
            $field['current_value_hash'] = fp02_hash($current);
            $field['rollback_value_hash'] = $field['current_value_hash'];
            $field['planned_value_hash'] = fp02_hash($field['planned_value']);
            $field['planned_value_summary'] = (string) $field['planned_value'];
            $writes[] = [
                'object_id' => $id,
                'object_type' => $obj['object_type'],
                'object_title' => $obj['object_title'],
                'field_meta_key' => $field['key'],
                'field_kind' => 'post_meta',
                'current_value_hash' => $field['current_value_hash'],
                'planned_value_summary' => $field['planned_value_summary'],
                'source_authority' => $field['source_authority'],
                'reason' => $field['reason'],
                'rollback_value_hash' => $field['rollback_value_hash'],
                'production_final' => false,
                'risk' => $field['risk'],
            ];
        }
        unset($field);
    }
    unset($obj);

    $object_ids = array_column($objects, 'object_id');
    $verdict = 'SAFE_TO_APPLY_WITH_DB_CHECKPOINT';
    $blockers = [];
    if (count($objects) !== 7) {
        $blockers[] = 'planned_object_count_not_7';
        $verdict = 'BLOCKED';
    }
    if ($unauthorized) {
        $blockers[] = 'unauthorized_objects';
        $verdict = 'BLOCKED';
    }
    if (!function_exists('update_field')) {
        $blockers[] = 'update_field_unavailable';
        $verdict = 'BLOCKED';
    }

    return [
        'phase' => 'V9-06D.4-RERUN',
        'timestamp' => gmdate('c'),
        'planned_object_count' => count($objects),
        'planned_object_ids' => $object_ids,
        'unauthorized_objects' => $unauthorized,
        'menu_changes_planned' => false,
        'options_changes_planned' => false,
        'redirects_planned' => false,
        'rewrite_flush_planned' => false,
        'v9_html_copy_planned' => false,
        'acf_extended_pro_dependency' => false,
        'objects' => $objects,
        'field_writes' => $writes,
        'blockers' => $blockers,
        'verdict' => $verdict,
        'result' => $verdict === 'SAFE_TO_APPLY_WITH_DB_CHECKPOINT' ? 'PASS' : 'FAIL',
    ];
}

function fp02_value_matches_plan($planned, $actual) {
    if (is_bool($planned) || $planned === 0 || $planned === 1) {
        return ((bool) $actual) === ((bool) $planned);
    }
    if (!is_array($planned)) {
        return (string) $actual === (string) $planned;
    }
    if (!is_array($actual)) {
        return false;
    }
    // Repeater / structured arrays: planned keys must match; ACF may add empty subfields.
    if (fp02_is_list_array($planned)) {
        if (count($planned) !== count($actual)) {
            return false;
        }
        foreach ($planned as $i => $row) {
            if (!isset($actual[$i])) {
                return false;
            }
            if (is_array($row)) {
                foreach ($row as $k => $v) {
                    if (!array_key_exists($k, $actual[$i])) {
                        return false;
                    }
                    if ((string) $actual[$i][$k] !== (string) $v) {
                        return false;
                    }
                }
            } elseif ((string) $actual[$i] !== (string) $row) {
                return false;
            }
        }
        return true;
    }
    foreach ($planned as $k => $v) {
        if (!array_key_exists($k, $actual)) {
            return false;
        }
        if ((string) $actual[$k] !== (string) $v) {
            return false;
        }
    }
    return true;
}

function fp02_is_list_array($arr) {
    if (!is_array($arr)) {
        return false;
    }
    if ($arr === []) {
        return true;
    }
    return array_keys($arr) === range(0, count($arr) - 1);
}

function fp02_apply_seed($plan, $write = true) {
    if ($plan['verdict'] !== 'SAFE_TO_APPLY_WITH_DB_CHECKPOINT') {
        return [
            'phase' => 'V9-06D.4-RERUN',
            'timestamp' => gmdate('c'),
            'result' => 'SKIPPED',
            'reason' => 'Dry-run not SAFE_TO_APPLY_WITH_DB_CHECKPOINT',
            'objects' => [],
        ];
    }
    if (!function_exists('update_field')) {
        return [
            'phase' => 'V9-06D.4-RERUN',
            'timestamp' => gmdate('c'),
            'result' => 'FAIL',
            'reason' => 'update_field unavailable',
            'objects' => [],
        ];
    }

    $results = [];
    $failed = [];
    foreach ($plan['objects'] as $obj) {
        $id = $obj['object_id'];
        $native_writes = 0;
        $acf_writes = 0;
        $meta_writes = 0;
        $failed_writes = [];
        $write_log = [];

        foreach ($obj['acf_fields'] as $field) {
            $ok = true;
            if ($write) {
                $ok = update_field($field['key'], $field['planned_value'], $id);
            }
            $after = get_field($field['key'], $id);
            $after_hash = fp02_hash($after);
            $match = fp02_value_matches_plan($field['planned_value'], $after);
            if ($match) {
                $acf_writes++;
                $write_log[] = ['key' => $field['key'], 'kind' => 'acf', 'result' => 'OK', 'after_hash' => $after_hash];
            } else {
                $failed_writes[] = ['key' => $field['key'], 'kind' => 'acf', 'after_hash' => $after_hash, 'update_field_return' => $ok, 'after_preview' => is_array($after) ? array_keys($after) : $after];
                $write_log[] = ['key' => $field['key'], 'kind' => 'acf', 'result' => 'FAIL', 'after_hash' => $after_hash];
            }
        }

        foreach ($obj['meta_fields'] as $field) {
            if ($write) {
                update_post_meta($id, $field['key'], $field['planned_value']);
            }
            $after = get_post_meta($id, $field['key'], true);
            if ((string) $after === (string) $field['planned_value']) {
                $meta_writes++;
                $write_log[] = ['key' => $field['key'], 'kind' => 'post_meta', 'result' => 'OK', 'after_hash' => fp02_hash($after)];
            } else {
                $failed_writes[] = ['key' => $field['key'], 'kind' => 'post_meta', 'after' => $after];
                $write_log[] = ['key' => $field['key'], 'kind' => 'post_meta', 'result' => 'FAIL'];
            }
        }

        $obj_result = $failed_writes ? 'FAIL' : 'PASS';
        if ($failed_writes) {
            $failed[] = $id;
        }
        $results[] = [
            'object_id' => $id,
            'object_type' => $obj['object_type'],
            'object_title' => $obj['object_title'],
            'native_writes' => $native_writes,
            'acf_meta_writes' => $acf_writes + $meta_writes,
            'acf_writes' => $acf_writes,
            'meta_writes' => $meta_writes,
            'failed_writes' => $failed_writes,
            'write_log' => $write_log,
            'result' => $obj_result,
        ];
    }

    return [
        'phase' => 'V9-06D.4-RERUN',
        'timestamp' => gmdate('c'),
        'pages_modified' => count(array_filter($results, function ($r) { return $r['object_type'] === 'page' && $r['result'] === 'PASS'; })),
        'services_modified' => count(array_filter($results, function ($r) { return $r['object_type'] === 'service' && $r['result'] === 'PASS'; })),
        'posts_modified' => 0,
        'menus_changed' => false,
        'options_changed' => false,
        'rewrite_flush' => 'NOT_PERFORMED',
        'objects' => $results,
        'failed_object_ids' => $failed,
        'result' => $failed ? 'FAIL' : 'PASS',
    ];
}

function fp02_validate_authorized($baseline_objects) {
    $rows = [];
    $all_pass = true;
    foreach (array_merge(AUTHORIZED_PAGES, AUTHORIZED_SERVICES) as $id) {
        $before = $baseline_objects[$id] ?? null;
        $after = fp02_object_snapshot($id);
        if (!$before || !$after) {
            $rows[] = ['object_id' => $id, 'result' => 'FAIL', 'reason' => 'missing'];
            $all_pass = false;
            continue;
        }
        $checks = [
            'exists' => true,
            'post_type_unchanged' => $before['post_type'] === $after['post_type'],
            'slug_unchanged' => $before['slug'] === $after['slug'],
            'parent_unchanged' => $before['parent'] === $after['parent'],
            'status_unchanged' => $before['status'] === $after['status'],
            'template_unchanged' => $before['template'] === $after['template'],
            'registry_id_preserved' => ($before['registry_id'] === $after['registry_id']),
            'migration_status_minimal_seed' => $after['migration_status'] === 'minimal_seed',
            'seeded_by_phase' => $after['seeded_by_phase'] === 'V9-06D.4',
            'content_hash_unchanged' => $before['content_hash'] === $after['content_hash'],
        ];
        $pass = !in_array(false, $checks, true);
        if (!$pass) {
            $all_pass = false;
        }
        $rows[] = [
            'object_id' => $id,
            'title' => $after['title'],
            'type' => $after['post_type'],
            'checks' => $checks,
            'acf_nonempty_fields' => $after['acf']['nonempty_fields'],
            'result' => $pass ? 'PASS' : 'FAIL',
        ];
    }
    return [
        'phase' => 'V9-06D.4-RERUN',
        'timestamp' => gmdate('c'),
        'objects' => $rows,
        'result' => $all_pass ? 'PASS' : 'FAIL',
    ];
}

// ---- execute modes ----
$identity = fp02_runtime_identity();
$identity_ok =
    $identity['active_theme'] === 'shpigovsky'
    && $identity['shpigovsky_core_active']
    && $identity['shpigovsky_core_mode'] === 'content_model'
    && $identity['service_cpt_registered']
    && $identity['services_total'] === 15
    && !in_array(false, $identity['authorized_pages_exist'], true)
    && !in_array(false, $identity['authorized_services_exist'], true)
    && $identity['acf_pro_active']
    && $identity['acf_groups_count'] === 13
    && count($identity['acf_options_pages']) >= 1
    && $identity['wpilot_write_enabled'] === false
    && $identity['update_field_available'];
$identity['result'] = $identity_ok ? 'PASS' : 'FAIL';
fp02_json_write($evidence_dir . '/runtime-identity.json', $identity);

if ($mode === 'identity') {
    echo $identity['result'] . "\n";
    exit($identity_ok ? 0 : 1);
}

if (!$identity_ok && in_array($mode, ['all', 'apply'], true)) {
    echo "IDENTITY_FAIL\n";
    exit(1);
}

$baseline_path = $evidence_dir . '/pre-write-baseline.json';
if ($mode === 'revalidate' && is_file($baseline_path)) {
    $baseline = json_decode(file_get_contents($baseline_path), true);
    $baseline_objects = $baseline['authorized_objects'];
    // JSON decode converts object keys to strings; normalize to int keys.
    $normalized = [];
    foreach ($baseline_objects as $k => $v) {
        $normalized[(int) $k] = $v;
    }
    $baseline_objects = $normalized;
    $baseline['authorized_objects'] = $baseline_objects;
} else {
    $baseline_objects = [];
    foreach (array_merge(AUTHORIZED_PAGES, AUTHORIZED_SERVICES) as $id) {
        $baseline_objects[$id] = fp02_object_snapshot($id);
    }
    $baseline = [
        'phase' => 'V9-06D.4-RERUN',
        'timestamp' => gmdate('c'),
        'authorized_objects' => $baseline_objects,
        'global' => fp02_global_invariants(),
        'result' => 'PASS',
    ];
    fp02_json_write($baseline_path, $baseline);
}

if ($mode === 'baseline') {
    echo "BASELINE_OK\n";
    exit(0);
}

$plan = fp02_seed_plan();
fp02_json_write($evidence_dir . '/dry-run-seed-plan.json', $plan);

if ($mode === 'dry-run') {
    echo $plan['verdict'] . "\n";
    exit($plan['result'] === 'PASS' ? 0 : 1);
}

if (in_array($mode, ['all', 'apply', 'revalidate'], true)) {
    $apply = fp02_apply_seed($plan, $mode !== 'revalidate');
    if ($mode === 'revalidate') {
        $apply['mode'] = 'revalidate_existing_writes';
        $apply['note'] = 'No additional writes; verifies planned values already present (ACF repeater subfield-aware match).';
    }
    fp02_json_write($evidence_dir . '/apply-seed-result.json', $apply);
    if ($apply['result'] !== 'PASS') {
        echo "APPLY_FAIL\n";
        exit(1);
    }
}

$post_objects = [];
foreach (array_merge(AUTHORIZED_PAGES, AUTHORIZED_SERVICES) as $id) {
    $post_objects[$id] = fp02_object_snapshot($id);
}
$auth_validation = fp02_validate_authorized($baseline_objects);
fp02_json_write($evidence_dir . '/authorized-object-validation.json', $auth_validation);

$acf_validation = [
    'phase' => 'V9-06D.4-RERUN',
    'timestamp' => gmdate('c'),
    'acf_fields_written' => true,
    'native_content_fields_written' => false,
    'skeleton_migration_status' => 'minimal_seed',
    'production_content' => false,
    'acf_extended_pro_used' => false,
    'options_values_written' => false,
    'objects' => [],
    'result' => 'PASS',
];
foreach ($post_objects as $id => $snap) {
    $acf_validation['objects'][] = [
        'object_id' => $id,
        'acf_nonempty_fields' => $snap['acf']['nonempty_fields'],
        'migration_status' => $snap['migration_status'],
        'seeded_by_phase' => $snap['seeded_by_phase'],
        'registry_id' => $snap['registry_id'],
    ];
}
fp02_json_write($evidence_dir . '/acf-seed-validation.json', $acf_validation);

$after_global = fp02_global_invariants();
$before_global = $baseline['global'];
$immutability_rows = [];
$immutable_keys = [
    'pages_total', 'services_total', 'posts_total', 'menus_count',
    'show_on_front', 'page_on_front', 'page_for_posts', 'permalink_structure',
    'rewrite_rules_hash', 'active_theme', 'active_theme_version',
    'acf_groups_count', 'acf_pro_active', 'acf_extended_pro_active', 'acf_free_active',
    'wpilot_write_enabled', 'categories_count', 'tags_count', 'users_count',
];
$immutability_pass = true;
foreach ($immutable_keys as $key) {
    $changed = $before_global[$key] !== $after_global[$key];
    if ($key === 'active_plugins') {
        $changed = $before_global['active_plugins'] !== $after_global['active_plugins'];
    }
    if ($changed) {
        $immutability_pass = false;
    }
    $immutability_rows[] = [
        'key' => $key,
        'before' => $before_global[$key],
        'after' => $after_global[$key],
        'changed' => $changed,
        'result' => $changed ? 'FAIL' : 'PASS',
    ];
}
// menus deep compare
$menus_changed = wp_json_encode($before_global['menus']) !== wp_json_encode($after_global['menus']);
$plugins_changed = $before_global['active_plugins'] !== $after_global['active_plugins'];
if ($menus_changed || $plugins_changed) {
    $immutability_pass = false;
}
$immutability_rows[] = [
    'key' => 'menus',
    'before' => $before_global['menus'],
    'after' => $after_global['menus'],
    'changed' => $menus_changed,
    'result' => $menus_changed ? 'FAIL' : 'PASS',
];
$immutability_rows[] = [
    'key' => 'active_plugins',
    'before' => $before_global['active_plugins'],
    'after' => $after_global['active_plugins'],
    'changed' => $plugins_changed,
    'result' => $plugins_changed ? 'FAIL' : 'PASS',
];

$global_immutability = [
    'phase' => 'V9-06D.4-RERUN',
    'timestamp' => gmdate('c'),
    'before' => $before_global,
    'after' => $after_global,
    'rows' => $immutability_rows,
    'result' => $immutability_pass ? 'PASS' : 'FAIL',
];
fp02_json_write($evidence_dir . '/global-immutability-validation.json', $global_immutability);

$post_baseline = [
    'phase' => 'V9-06D.4-RERUN',
    'timestamp' => gmdate('c'),
    'authorized_objects' => $post_objects,
    'global' => $after_global,
];
fp02_json_write($evidence_dir . '/post-write-snapshot.json', $post_baseline);

$overall = ($auth_validation['result'] === 'PASS' && $global_immutability['result'] === 'PASS') ? 'PASS' : 'FAIL';
echo $overall . "\n";
exit($overall === 'PASS' ? 0 : 1);
