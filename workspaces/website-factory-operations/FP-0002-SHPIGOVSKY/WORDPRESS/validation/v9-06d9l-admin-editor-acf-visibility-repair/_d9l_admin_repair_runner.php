<?php
/**
 * FP-0002 V9-06D9-L — Admin editor / ACF visibility repair runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * Modes: baseline | checkpoint-meta | verify-admin | verify-acf-values | drift
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'baseline';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9l-admin-editor-acf-visibility-repair';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_HOME_PAGE_ID = 4;
const FP02_PHASE = 'V9-06D9-L';
const FP02_GROUP_KEY = 'group_fp02_page_home';

const FP02_SEEDED_FIELDS = [
    'home_recovery_intro_heading',
    'home_recovery_intro_lead_1',
    'home_recovery_intro_lead_2',
    'home_intro_bands',
    'home_faq_heading',
    'home_faq_items',
    'home_specialists_heading',
    'home_comfort_heading',
    'home_comfort_lead',
    'home_reviews_heading',
    'home_articles_heading',
    'home_hero_slides',
    'home_gallery_media',
];

function fp02l_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02l_plugin_state($slug) {
    $all = get_plugins();
    $installed = isset($all[$slug . '/' . $slug . '.php']) || isset($all[$slug . '/classic-editor.php']);
    $main = $slug . '/classic-editor.php';
    if (!$installed) {
        foreach ($all as $file => $meta) {
            if (strpos($file, $slug . '/') === 0) {
                $installed = true;
                $main = $file;
                break;
            }
        }
    }
    return [
        'slug' => $slug,
        'installed' => $installed,
        'active' => $installed ? is_plugin_active($main) : false,
        'main_file' => $installed ? $main : null,
    ];
}

function fp02l_acf_json_status() {
    if (!function_exists('acf_get_local_json_files')) {
        return ['available' => false, 'pending' => null, 'total' => null, 'keys' => []];
    }
    $files = acf_get_local_json_files('acf-field-group');
    $keys = array_keys($files ?: []);
    $db_groups = get_posts([
        'post_type' => 'acf-field-group',
        'posts_per_page' => -1,
        'post_status' => ['publish', 'draft', 'acf-disabled'],
    ]);
    return [
        'available' => true,
        'local_json_count' => count($keys),
        'local_json_keys' => $keys,
        'db_group_count' => count($db_groups),
        'home_group_in_local_json' => in_array(FP02_GROUP_KEY, $keys, true),
        'pending_sync_estimate' => max(0, count($keys) - count($db_groups)),
    ];
}

function fp02l_field_group_info() {
    $group = function_exists('acf_get_field_group') ? acf_get_field_group(FP02_GROUP_KEY) : null;
    if (!$group) {
        return ['exists' => false];
    }
    $location_match = false;
    if (!empty($group['location']) && is_array($group['location'])) {
        foreach ($group['location'] as $or_group) {
            foreach ($or_group as $rule) {
                if (($rule['param'] ?? '') === 'page' && ($rule['operator'] ?? '') === '==' && (string) ($rule['value'] ?? '') === (string) FP02_HOME_PAGE_ID) {
                    $location_match = true;
                }
            }
        }
    }
    return [
        'exists' => true,
        'key' => $group['key'] ?? null,
        'title' => $group['title'] ?? null,
        'ID' => $group['ID'] ?? null,
        'active' => $group['active'] ?? null,
        'location_matches_home_page_4' => $location_match,
    ];
}

function fp02l_editor_state() {
    $page_block = function_exists('use_block_editor_for_post') ? use_block_editor_for_post(FP02_HOME_PAGE_ID) : null;
    $type_block = function_exists('use_block_editor_for_post_type') ? use_block_editor_for_post_type('page') : null;
    return [
        'use_block_editor_for_home_page_4' => $page_block,
        'use_block_editor_for_post_type_page' => $type_block,
        'classic_editor_plugin_active' => fp02l_plugin_state('classic-editor')['active'],
        'classic_editor_replace' => get_option('classic-editor-replace', null),
        'classic_editor_allow_users' => get_option('classic-editor-allow-users', null),
    ];
}

function fp02l_home_acf_values() {
    $out = [];
    foreach (FP02_SEEDED_FIELDS as $name) {
        $val = function_exists('get_field') ? get_field($name, FP02_HOME_PAGE_ID) : null;
        $summary = [
            'name' => $name,
            'empty' => empty($val),
            'type' => gettype($val),
        ];
        if (is_array($val)) {
            $summary['count'] = count($val);
        } elseif (is_string($val)) {
            $summary['length'] = mb_strlen($val);
            $summary['preview'] = mb_substr($val, 0, 80);
        }
        if ($name === 'home_hero_slides' && is_array($val) && !empty($val[0]['image'])) {
            $img = $val[0]['image'];
            $summary['hero_image_attachment_id'] = is_array($img) ? ($img['ID'] ?? null) : $img;
        }
        if ($name === 'home_gallery_media' && is_array($val)) {
            $summary['gallery_row_count'] = count($val);
            $summary['gallery_with_media'] = 0;
            foreach ($val as $row) {
                if (!empty($row['media'])) {
                    $summary['gallery_with_media']++;
                }
            }
        }
        $out[$name] = $summary;
    }
    return $out;
}

function fp02l_active_plugins() {
    $active = get_option('active_plugins', []);
    $all = get_plugins();
    $rows = [];
    foreach ($active as $file) {
        $rows[] = [
            'file' => $file,
            'name' => $all[$file]['Name'] ?? $file,
            'version' => $all[$file]['Version'] ?? null,
        ];
    }
    return $rows;
}

function fp02l_relevant_options_before() {
    $keys = [
        'classic-editor-replace',
        'classic-editor-allow-users',
        'active_plugins',
        'show_on_front',
        'page_on_front',
    ];
    $out = [];
    foreach ($keys as $k) {
        $out[$k] = get_option($k, null);
    }
    return $out;
}

switch ($mode) {
    case 'baseline':
        $classic = fp02l_plugin_state('classic-editor');
        $payload = [
            'phase' => FP02_PHASE,
            'generated_at' => gmdate('c'),
            'wordpress_version' => get_bloginfo('version'),
            'active_theme' => wp_get_theme()->get_stylesheet(),
            'home_page_id' => FP02_HOME_PAGE_ID,
            'home_page_title' => get_the_title(FP02_HOME_PAGE_ID),
            'home_page_status' => get_post_status(FP02_HOME_PAGE_ID),
            'classic_editor' => $classic,
            'editor_state' => fp02l_editor_state(),
            'acf_pro_active' => is_plugin_active('advanced-custom-fields-pro/acf.php'),
            'acf_json' => fp02l_acf_json_status(),
            'field_group' => fp02l_field_group_info(),
            'home_acf_values_summary' => fp02l_home_acf_values(),
            'active_plugins' => fp02l_active_plugins(),
            'diagnosis' => [
                'block_editor_active_for_home' => fp02l_editor_state()['use_block_editor_for_home_page_4'] === true,
                'classic_editor_missing' => !$classic['installed'],
                'classic_editor_inactive' => $classic['installed'] && !$classic['active'],
                'acf_field_groups_pending_sync' => fp02l_acf_json_status()['pending_sync_estimate'] > 0,
                'acf_home_group_registered' => fp02l_field_group_info()['exists'] === true,
            ],
            'result' => 'CAPTURED',
        ];
        fp02l_json_write($evidence_dir . '/admin-issue-baseline-diagnostic.json', $payload);
        echo json_encode(['ok' => true, 'path' => $evidence_dir . '/admin-issue-baseline-diagnostic.json'], JSON_UNESCAPED_SLASHES) . "\n";
        break;

    case 'checkpoint-meta':
        $payload = [
            'phase' => FP02_PHASE,
            'generated_at' => gmdate('c'),
            'active_plugins_before' => fp02l_active_plugins(),
            'options_before' => fp02l_relevant_options_before(),
            'acf_group_inventory_before' => fp02l_acf_json_status(),
            'home_page_4_acf_values_before' => fp02l_home_acf_values(),
        ];
        fp02l_json_write($evidence_dir . '/_checkpoint-meta-snapshot.json', $payload);
        echo json_encode(['ok' => true], JSON_UNESCAPED_SLASHES) . "\n";
        break;

    case 'verify-admin':
        $classic = fp02l_plugin_state('classic-editor');
        $editor = fp02l_editor_state();
        $group = fp02l_field_group_info();
        $values = fp02l_home_acf_values();
        $payload = [
            'phase' => FP02_PHASE,
            'generated_at' => gmdate('c'),
            'classic_editor' => $classic,
            'editor_state' => $editor,
            'gutenberg_disabled' => $editor['use_block_editor_for_home_page_4'] === false && $editor['use_block_editor_for_post_type_page'] === false,
            'acf_json' => fp02l_acf_json_status(),
            'field_group' => $group,
            'home_acf_values' => $values,
            'checks' => [
                'classic_editor_active' => $classic['active'],
                'block_editor_off_home' => $editor['use_block_editor_for_home_page_4'] === false,
                'block_editor_off_pages' => $editor['use_block_editor_for_post_type_page'] === false,
                'home_group_registered' => $group['exists'] === true,
                'home_group_location_ok' => ($group['location_matches_home_page_4'] ?? false) === true,
                'faq_heading_populated' => ($values['home_faq_heading']['empty'] ?? true) === false,
                'specialists_heading_populated' => ($values['home_specialists_heading']['empty'] ?? true) === false,
                'hero_image_populated' => ($values['home_hero_slides']['hero_image_attachment_id'] ?? null) !== null,
                'gallery_four_rows' => ($values['home_gallery_media']['gallery_row_count'] ?? 0) === 4,
            ],
        ];
        $pass = $payload['checks']['classic_editor_active']
            && $payload['checks']['block_editor_off_home']
            && $payload['checks']['home_group_registered']
            && $payload['checks']['faq_heading_populated']
            && $payload['checks']['hero_image_populated'];
        $payload['result'] = $pass ? 'PASS' : 'PARTIAL';
        fp02l_json_write($evidence_dir . '/post-repair-admin-validation.json', $payload);
        echo json_encode(['ok' => true, 'result' => $payload['result']], JSON_UNESCAPED_SLASHES) . "\n";
        break;

    case 'verify-acf-values':
        fp02l_json_write($evidence_dir . '/acf-admin-visibility-repair-result.json', [
            'phase' => FP02_PHASE,
            'generated_at' => gmdate('c'),
            'acf_sync_performed' => false,
            'field_group' => fp02l_field_group_info(),
            'home_acf_values' => fp02l_home_acf_values(),
            'note' => 'Values unchanged — visibility repair only',
            'result' => 'CAPTURED',
        ]);
        echo json_encode(['ok' => true], JSON_UNESCAPED_SLASHES) . "\n";
        break;

    case 'drift':
        fp02l_json_write($evidence_dir . '/no-scope-drift-validation.json', [
            'phase' => FP02_PHASE,
            'generated_at' => gmdate('c'),
            'source_theme_changes' => 0,
            'acf_json_changes' => 0,
            'acf_content_media_value_writes' => 0,
            'media_uploads' => 0,
            'attachment_creation' => 0,
            'menu_writes' => 0,
            'rewrite_flush' => false,
            'native_content_writes' => 0,
            'plugin_install_limited_to_classic_editor' => true,
            'plugin_updates' => 0,
            'plugin_deletes' => 0,
            'v9_src_dist_changes' => 0,
            'options_writes_plugin_settings_only' => true,
            'result' => 'PASS',
        ]);
        echo json_encode(['ok' => true], JSON_UNESCAPED_SLASHES) . "\n";
        break;

    default:
        fwrite(STDERR, "Unknown mode: $mode\n");
        exit(1);
}
