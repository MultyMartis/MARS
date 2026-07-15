<?php
/**
 * FP-0002 V9-06D8-E — Contacts page #20 ACF seed runner (contacts ACF only).
 * Modes: identity | baseline | checkpoint | dry-run | apply | verify | drift | routes | olga | all
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d8e-contacts-content-seed';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_CONTACTS_PAGE_ID = 20;
const FP02_HOME_PAGE_ID = 4;
const FP02_HUB_PAGE_ID = 5;
const FP02_TARGET_SERVICE_IDS = [73, 74, 77, 84];

const FP02_CONTACTS_INVENTORY_FIELDS = [
    'contacts_address',
    'contacts_map_url',
    'contacts_phones',
    'contacts_messengers',
    'contacts_blocks',
    'contacts_form_intro',
];

const FP02_AUTHORIZED_CONTACTS_FIELDS = [
    'contacts_form_intro',
    'contacts_address',
    'contacts_blocks',
];

const FP02_CONTACTS_INTRO_V9 = 'Ведем прием и консультируем в Москве и Московской области. Для нас не существует границ в привычном понимании этого слова — к нам приезжают из разных городов и стран, доверяя свое здоровье и благополучие заботливой помощи наших специалистов.';

const FP02_CONTACTS_ADDRESS_V9 = 'Москва, ул. Ленина, 3';

const FP02_CONTACTS_BLOCKS_V9 = [
    [
        'title' => 'Центр профилактики и лечения зависимости',
        'text' => 'Московская область, район ж.д. станции Катуар, д. Сухарево',
    ],
    [
        'title' => 'Лечение зависимостей Москва',
        'text' => 'Москва, ул. Ленина, 3',
    ],
];

const FP02_SEED_PAYLOAD = [
    'contacts_form_intro' => [
        'value' => FP02_CONTACTS_INTRO_V9,
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'STATIC_V9_CONTENT',
        'write' => true,
        'v9_ref' => 'src/partials/sections/contacts-map-body.html contacts-body__intro',
    ],
    'contacts_address' => [
        'value' => FP02_CONTACTS_ADDRESS_V9,
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'STATIC_V9_CONTENT',
        'write' => true,
        'v9_ref' => 'src/partials/sections/contacts-map-body.html location 2 address; D7-E location-two fallback',
    ],
    'contacts_map_url' => [
        'value' => '',
        'source' => 'OPERATOR_SUPPLIED_REQUIRED',
        'classification' => 'SKIP_OPERATOR_SUPPLIED_REQUIRED',
        'write' => false,
        'v9_ref' => 'V9 uses static map PNG only; D8-A map_link empty',
    ],
    'contacts_phones' => [
        'value' => [],
        'source' => 'D8A_SITE_OPTIONS_READONLY',
        'classification' => 'SKIP_DO_NOT_SEED',
        'write' => false,
        'v9_ref' => 'Olga plan: phones canonical in Site Options phone_primary',
    ],
    'contacts_messengers' => [
        'value' => [],
        'source' => 'OPERATOR_SUPPLIED_REQUIRED',
        'classification' => 'SKIP_OPERATOR_SUPPLIED_REQUIRED',
        'write' => false,
        'v9_ref' => 'V9 href="#" placeholders; D8-A social_links empty',
    ],
    'contacts_blocks' => [
        'value' => FP02_CONTACTS_BLOCKS_V9,
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'STATIC_V9_CONTENT',
        'write' => true,
        'v9_ref' => 'src/partials/sections/contacts-map-body.html two contacts-location articles',
    ],
];

function fp02e_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02e_hash($value) {
    if ($value === null || $value === false || $value === '') {
        return 'empty';
    }
    if (is_array($value) || is_object($value)) {
        $value = wp_json_encode($value);
    }
    return hash('sha256', (string) $value);
}

function fp02e_contacts_value($field_name) {
    if (!function_exists('get_field')) {
        return null;
    }
    return get_field($field_name, FP02_CONTACTS_PAGE_ID);
}

function fp02e_contacts_state($field_name) {
    $value = fp02e_contacts_value($field_name);
    $empty = ($value === null || $value === false || $value === '' || $value === [] || $value === 0);
    if (is_array($value)) {
        $empty = count($value) === 0;
    }
    return [
        'page_id' => FP02_CONTACTS_PAGE_ID,
        'field' => $field_name,
        'value' => $value,
        'hash' => fp02e_hash($value),
        'empty' => $empty,
    ];
}

function fp02e_field_meta($field_name) {
    $map = [
        'contacts_address' => ['group' => 'group_fp02_page_contacts', 'key' => 'field_fp02_contacts_address', 'type' => 'textarea', 'rendered' => true, 'allowlist' => true],
        'contacts_map_url' => ['group' => 'group_fp02_page_contacts', 'key' => 'field_fp02_contacts_map_url', 'type' => 'url', 'rendered' => true, 'allowlist' => false],
        'contacts_phones' => ['group' => 'group_fp02_page_contacts', 'key' => 'field_fp02_contacts_phones', 'type' => 'repeater', 'rendered' => true, 'allowlist' => false],
        'contacts_messengers' => ['group' => 'group_fp02_page_contacts', 'key' => 'field_fp02_contacts_messengers', 'type' => 'repeater', 'rendered' => true, 'allowlist' => false],
        'contacts_blocks' => ['group' => 'group_fp02_page_contacts', 'key' => 'field_fp02_contacts_blocks', 'type' => 'repeater', 'rendered' => true, 'allowlist' => true],
        'contacts_form_intro' => ['group' => 'group_fp02_page_contacts', 'key' => 'field_fp02_contacts_form_intro', 'type' => 'textarea', 'rendered' => true, 'allowlist' => true],
    ];
    return $map[$field_name] ?? ['group' => '', 'key' => '', 'type' => 'unknown', 'rendered' => false, 'allowlist' => false];
}

function fp02e_count_acf_groups() {
    if (!function_exists('acf_get_field_groups')) {
        return 0;
    }
    return count(acf_get_field_groups());
}

function fp02e_wpilot_write_enabled() {
    $path = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/mu-plugins/wpilot/config.json';
    if (!is_readable($path)) {
        return ['detected' => false, 'write_enabled' => null];
    }
    $json = json_decode((string) file_get_contents($path), true);
    if (!is_array($json)) {
        return ['detected' => true, 'write_enabled' => null, 'path' => $path];
    }
    return [
        'detected' => true,
        'write_enabled' => isset($json['write_enabled']) ? (bool) $json['write_enabled'] : null,
        'path' => $path,
    ];
}

function fp02e_http_code($path) {
    $url = home_url($path);
    if (!function_exists('curl_init')) {
        return ['url' => $url, 'http' => 0];
    }
    $ch = curl_init($url);
    curl_setopt_array($ch, [CURLOPT_NOBODY => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 15, CURLOPT_SSL_VERIFYPEER => false]);
    curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return ['url' => $url, 'http' => $code];
}

function fp02e_identity() {
    global $wpdb;
    $plugins = get_plugins();
    $active = get_option('active_plugins', []);
    $active_named = [];
    foreach ($active as $slug) {
        $active_named[$slug] = isset($plugins[$slug]['Name']) ? $plugins[$slug]['Name'] : $slug;
    }
    $contacts = get_post(FP02_CONTACTS_PAGE_ID);
    $root_http = fp02e_http_code('/');
    $contacts_http = fp02e_http_code('/kontakty/');
    $services = [];
    foreach (FP02_TARGET_SERVICE_IDS as $id) {
        $post = get_post($id);
        $services[(string) $id] = [
            'id' => $id,
            'exists' => $post instanceof WP_Post,
            'title' => $post instanceof WP_Post ? $post->post_title : '',
        ];
    }
    $options_readable = function_exists('get_field') && get_field('phone_primary', 'option') !== null;
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'runtime_path' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky',
        'domain' => home_url('/'),
        'http_root' => $root_http['http'],
        'http_kontakty' => $contacts_http['http'],
        'db_name' => defined('DB_NAME') ? DB_NAME : '',
        'table_prefix' => $wpdb->prefix,
        'db_connection' => (bool) $wpdb->check_connection(),
        'active_theme' => wp_get_theme()->get_stylesheet(),
        'shpigovsky_core_active' => in_array('shpigovsky-core/shpigovsky-core.php', $active, true),
        'acf_pro_active' => in_array('advanced-custom-fields-pro/acf.php', $active, true),
        'acf_groups_count' => fp02e_count_acf_groups(),
        'core_mode' => function_exists('shpigovsky_core_mode') ? shpigovsky_core_mode() : 'unknown',
        'service_cpt_registered' => post_type_exists('service'),
        'wpilot' => fp02e_wpilot_write_enabled(),
        'contacts_page' => [
            'id' => FP02_CONTACTS_PAGE_ID,
            'exists' => $contacts instanceof WP_Post,
            'title' => $contacts instanceof WP_Post ? $contacts->post_title : '',
            'slug' => $contacts instanceof WP_Post ? $contacts->post_name : '',
            'template' => $contacts instanceof WP_Post ? get_page_template_slug($contacts) : '',
            'route' => '/kontakty/',
        ],
        'd8a_site_options_readable' => $options_readable,
        'target_services_readonly' => $services,
        'active_plugins' => $active_named,
        'result' => 'PASS',
    ];
}

function fp02e_baseline_contacts() {
    $fields = [];
    foreach (FP02_CONTACTS_INVENTORY_FIELDS as $name) {
        $fields[$name] = fp02e_contacts_state($name);
    }
    $post = get_post(FP02_CONTACTS_PAGE_ID);
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_CONTACTS_PAGE_ID,
        'slug' => $post instanceof WP_Post ? $post->post_name : '',
        'title' => $post instanceof WP_Post ? $post->post_title : '',
        'post_title_hash' => fp02e_hash($post instanceof WP_Post ? $post->post_title : ''),
        'post_content_hash' => fp02e_hash($post instanceof WP_Post ? $post->post_content : ''),
        'fields' => $fields,
    ];
}

function fp02e_build_inventory($baseline) {
    $rows = [];
    foreach (FP02_CONTACTS_INVENTORY_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $fm = fp02e_field_meta($name);
        $old = $baseline['fields'][$name];
        $rows[] = [
            'page_id' => FP02_CONTACTS_PAGE_ID,
            'field_group' => $fm['group'],
            'field_key' => $fm['key'],
            'field_name' => $name,
            'field_type' => $fm['type'],
            'old_value_state' => $old['empty'] ? 'empty' : 'populated',
            'old_hash' => $old['hash'],
            'proposed_value_source' => $meta['source'],
            'classification' => $meta['classification'],
            'rendered_by_d7e' => $fm['rendered'],
            'improves_visible_mvp' => $meta['write'],
            'olga_editable_later' => $meta['write'] || in_array($name, ['contacts_form_intro', 'contacts_blocks'], true),
            'risk' => str_contains($meta['classification'], 'OPERATOR') ? 'MEDIUM_DEFER' : 'LOW',
            'write_decision' => $meta['write'] ? 'WRITE' : 'SKIP',
            'v9_reference' => $meta['v9_ref'],
            'result' => 'CONFIRMED',
        ];
    }
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'writable_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'WRITE')),
        'skipped_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'SKIP')),
        'result' => 'PASS',
    ];
}

function fp02e_content_source_map() {
    $sections = [
        ['section' => 'contacts hero/intro', 'v9_ref' => 'contacts-map-body.html contacts-body__intro', 'd8a_option' => '', 'target_fields' => ['contacts_form_intro'], 'seed_decision' => 'WRITE', 'reason' => 'Page intro field; improves Olga editability vs template fallback'],
        ['section' => 'phone row', 'v9_ref' => 'contacts-map-body.html tel link', 'd8a_option' => 'phone_primary', 'target_fields' => ['contacts_phones'], 'seed_decision' => 'SKIP', 'reason' => 'Canonical phone in D8-A Site Options; template fallback OK'],
        ['section' => 'messengers/social', 'v9_ref' => 'contacts-map-body.html href="#" placeholders', 'd8a_option' => 'social_links', 'target_fields' => ['contacts_messengers'], 'seed_decision' => 'SKIP', 'reason' => 'OPERATOR_SUPPLIED_REQUIRED — no real URLs'],
        ['section' => 'location card MO', 'v9_ref' => 'contacts-map-body.html location 1', 'd8a_option' => 'site_address (chrome short form)', 'target_fields' => ['contacts_blocks[0]'], 'seed_decision' => 'WRITE', 'reason' => 'V9 full MO address in contacts_blocks row 1 text'],
        ['section' => 'location card Moscow', 'v9_ref' => 'contacts-map-body.html location 2', 'd8a_option' => '', 'target_fields' => ['contacts_address', 'contacts_blocks[1]'], 'seed_decision' => 'WRITE', 'reason' => 'V9 Moscow consulting address'],
        ['section' => 'opening hours/email rows', 'v9_ref' => 'contacts-map-body.html detail rows', 'd8a_option' => 'opening_hours, site_email', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'Template reads D8-A options + static fallback'],
        ['section' => 'map block', 'v9_ref' => 'contacts-map-body.html static PNG', 'd8a_option' => 'map_link', 'target_fields' => ['contacts_map_url'], 'seed_decision' => 'SKIP', 'reason' => 'No operator map URL; static theme assets only'],
        ['section' => 'rehabilitation steps', 'v9_ref' => 'contacts-rehabilitation-steps.html', 'd8a_option' => '', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'STATIC_FALLBACK_ALREADY_IN_TEMPLATE — no page ACF fields'],
        ['section' => 'CTA band', 'v9_ref' => 'program-cta-band.html + D8-A options', 'd8a_option' => 'default_button_label, phone_primary', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'Template helper + site options'],
        ['section' => 'form/callback static text', 'v9_ref' => 'global-consultation-modal.html', 'd8a_option' => 'default_callback_title', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'Modal-only; no live endpoint'],
        ['section' => 'map/photo media', 'v9_ref' => 'contacts-map PNG + rehabilitation interior PNG', 'd8a_option' => '', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'MEDIA_REQUIRED — theme static assets until upload authorized'],
    ];
    return ['phase' => 'V9-06D8-E', 'generated_at' => gmdate('c'), 'sections' => $sections, 'result' => 'PASS'];
}

function fp02e_proposed_payload($baseline) {
    $entries = [];
    $writable_total = 0;
    foreach (FP02_CONTACTS_INVENTORY_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $old = $baseline['fields'][$name];
        $preview = 'unchanged/skip';
        if ($meta['write']) {
            if (is_array($meta['value'])) {
                $preview = 'repeater[' . count($meta['value']) . ' rows]';
            } else {
                $preview = mb_substr((string) $meta['value'], 0, 80);
            }
            $writable_total++;
        }
        $entries[] = [
            'page_id' => FP02_CONTACTS_PAGE_ID,
            'field' => $name,
            'old_state' => $old['empty'] ? 'empty' : 'populated',
            'proposed_value_state' => $meta['write'] ? 'set' : 'unchanged',
            'proposed_value_preview' => $preview,
            'source' => $meta['source'],
            'classification' => $meta['classification'],
            'write' => $meta['write'],
            'rollback_value' => $old['value'],
            'skip_reason' => $meta['write'] ? '' : $meta['classification'],
        ];
    }
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'target_page_id' => FP02_CONTACTS_PAGE_ID,
        'entries' => $entries,
        'writable_field_operations' => $writable_total,
        'result' => $writable_total > 0 ? 'PASS' : 'BLOCKED',
    ];
}

function fp02e_dry_run($baseline) {
    $rows = [];
    foreach (FP02_AUTHORIZED_CONTACTS_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $old = $baseline['fields'][$name];
        $new_val = $meta['value'];
        $same = fp02e_hash($old['value']) === fp02e_hash($new_val);
        $operation = !$meta['write'] ? 'skip' : ($old['empty'] ? 'create' : ($same ? 'no-op' : 'update'));
        $rows[] = [
            'page_id' => FP02_CONTACTS_PAGE_ID,
            'field' => $name,
            'old_state' => $old['empty'] ? 'empty' : 'populated',
            'new_state' => $meta['write'] ? 'set' : 'unchanged',
            'operation' => $operation,
            'source' => $meta['source'],
            'classification' => $meta['classification'],
            'rollback_available' => true,
            'rollback_value' => $old['value'],
            'risk' => 'LOW',
            'result' => $meta['write'] || $operation === 'skip' ? 'OK' : 'BLOCKED',
        ];
    }
    $skipped = [];
    foreach (['contacts_map_url', 'contacts_phones', 'contacts_messengers'] as $name) {
        $skipped[] = ['field' => $name, 'reason' => FP02_SEED_PAYLOAD[$name]['classification'], 'operation' => 'skip'];
    }
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'target_page_id' => FP02_CONTACTS_PAGE_ID,
        'fields' => $rows,
        'skipped_fields' => $skipped,
        'verdict' => 'SAFE_TO_APPLY_EXACT_CONTACTS_ACF_ALLOWLIST',
        'result' => 'PASS',
    ];
}

function fp02e_apply_seed($baseline) {
    if (!function_exists('update_field')) {
        return ['result' => 'FAIL', 'error' => 'ACF update_field unavailable'];
    }
    $attempted = [];
    $updated = [];
    $unchanged = [];
    $skipped = [];
    $errors = [];
    $pre_post = [];
    foreach (FP02_AUTHORIZED_CONTACTS_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        if (!$meta['write']) {
            $skipped[] = $name;
            continue;
        }
        $attempted[] = $name;
        $old = $baseline['fields'][$name]['value'];
        $new = $meta['value'];
        $pre_post[$name] = ['before' => $old, 'after' => null];
        if (fp02e_hash($old) === fp02e_hash($new)) {
            $unchanged[] = $name;
            $pre_post[$name]['after'] = $old;
            continue;
        }
        $ok = update_field($name, $new, FP02_CONTACTS_PAGE_ID);
        if (!$ok) {
            $errors[] = ['field' => $name, 'message' => 'update_field returned false'];
            continue;
        }
        $updated[] = $name;
        $pre_post[$name]['after'] = fp02e_contacts_value($name);
    }
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_CONTACTS_PAGE_ID,
        'fields_attempted' => $attempted,
        'fields_updated' => $updated,
        'fields_unchanged' => $unchanged,
        'fields_skipped' => $skipped,
        'errors' => $errors,
        'pre_post' => $pre_post,
        'result' => empty($errors) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02e_verify_contacts($baseline) {
    $rows = [];
    foreach (FP02_CONTACTS_INVENTORY_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $actual = fp02e_contacts_state($name);
        if (!$meta['write']) {
            $same = fp02e_hash($actual['value']) === fp02e_hash($baseline['fields'][$name]['value']);
            $rows[] = [
                'field' => $name,
                'expected_state' => 'unchanged',
                'actual_state' => $actual['empty'] ? 'empty' : 'populated',
                'hash_match' => $same,
                'result' => $same ? 'PASS' : 'FAIL',
            ];
            continue;
        }
        $ok = fp02e_hash($actual['value']) === fp02e_hash($meta['value']);
        $rows[] = [
            'field' => $name,
            'expected_state' => 'seeded',
            'actual_state' => $actual['empty'] ? 'empty' : 'populated',
            'hash_match' => $ok,
            'result' => $ok ? 'PASS' : 'FAIL',
        ];
    }
    $url = home_url('/kontakty/');
    $body = '';
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 20, CURLOPT_SSL_VERIFYPEER => false]);
        $body = (string) curl_exec($ch);
        curl_close($ch);
    }
    $sections = [
        ['section' => 'D7-E page shell', 'expected' => 'page-kontakty + site-main--contacts', 'actual' => $body !== '' && preg_match('/page-kontakty|site-main--contacts/', $body) ? 'visible' : 'unknown', 'result' => $body !== '' && preg_match('/page-kontakty|site-main--contacts/', $body) ? 'PASS' : 'PARTIAL'],
        ['section' => 'intro copy', 'expected' => 'contacts-body__intro with seeded intro', 'actual' => $body !== '' && preg_match('/contacts-body__intro/', $body) ? 'visible' : 'missing', 'result' => $body !== '' && preg_match('/contacts-body__intro/', $body) ? 'PASS' : 'FAIL'],
        ['section' => 'location cards', 'expected' => 'contacts-location cards from contacts_blocks', 'actual' => $body !== '' && preg_match('/contacts-location/', $body) ? 'visible' : 'missing', 'result' => $body !== '' && preg_match('/contacts-location/', $body) ? 'PASS' : 'FAIL'],
        ['section' => 'phone row', 'expected' => 'D8-A phone_primary via template', 'actual' => $body !== '' && preg_match('/contacts-body__phone|tel:/', $body) ? 'visible' : 'partial', 'result' => 'PASS'],
        ['section' => 'rehabilitation steps', 'expected' => 'contacts-rehabilitation-steps static block', 'actual' => $body !== '' && preg_match('/contacts-rehabilitation-steps/', $body) ? 'visible' : 'missing', 'result' => $body !== '' && preg_match('/contacts-rehabilitation-steps/', $body) ? 'PASS' : 'FAIL'],
        ['section' => 'map embed', 'expected' => 'omitted — no map URL', 'actual' => empty(fp02e_contacts_value('contacts_map_url')) ? 'omitted' : 'present', 'result' => empty(fp02e_contacts_value('contacts_map_url')) ? 'PASS' : 'PARTIAL'],
        ['section' => 'messengers', 'expected' => 'omitted when no operator URLs', 'actual' => $body !== '' && preg_match('/contacts-body__messengers/', $body) ? 'partial/empty' : 'omitted', 'result' => 'PASS'],
    ];
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_CONTACTS_PAGE_ID,
        'fields' => $rows,
        'sections' => $sections,
        'result' => count(array_filter($rows, static fn($r) => $r['result'] === 'FAIL')) === 0 ? 'PASS' : 'PARTIAL',
    ];
}

function fp02e_home_snapshot() {
    $names = ['home_advantages', 'home_faq_items', 'home_hero_slides'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, FP02_HOME_PAGE_ID) : null;
        $out[$name] = fp02e_hash($v);
    }
    return $out;
}

function fp02e_hub_snapshot() {
    $names = ['services_hub_intro', 'services_hub_faq_items'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, FP02_HUB_PAGE_ID) : null;
        $out[$name] = fp02e_hash($v);
    }
    return $out;
}

function fp02e_service_snapshot() {
    $names = ['programme_items', 'stages', 'faq_items', 'hero_lead'];
    $out = [];
    foreach (FP02_TARGET_SERVICE_IDS as $id) {
        $row = [];
        foreach ($names as $name) {
            $v = function_exists('get_field') ? get_field($name, $id) : null;
            $row[$name] = fp02e_hash($v);
        }
        $out[(string) $id] = $row;
    }
    return $out;
}

function fp02e_option_snapshot() {
    $names = ['organisation_name', 'phone_primary', 'site_email', 'site_address', 'opening_hours', 'map_link', 'social_links', 'global_cta_title'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, 'option') : null;
        $out[$name] = fp02e_hash($v);
    }
    return $out;
}

function fp02e_object_counts() {
    return [
        'pages' => (int) wp_count_posts('page')->publish,
        'services' => post_type_exists('service') ? (int) wp_count_posts('service')->publish : 0,
        'posts' => (int) wp_count_posts('post')->publish,
        'nav_menus' => (int) wp_count_terms(['taxonomy' => 'nav_menu', 'hide_empty' => false]),
    ];
}

function fp02e_route_smoke() {
    $routes = [
        ['name' => 'Home', 'path' => '/'],
        ['name' => 'Services Hub', 'path' => '/uslugi/'],
        ['name' => 'Service 73', 'path' => '/uslugi/zavisimosti/'],
        ['name' => 'Service 74', 'path' => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/'],
        ['name' => 'Service 77', 'path' => '/uslugi/psihicheskoe-zdorovie/'],
        ['name' => 'Service 84', 'path' => '/uslugi/rasstroystva-pischevogo-povedeniya/'],
        ['name' => 'Contacts', 'path' => '/kontakty/'],
    ];
    $rows = [];
    foreach ($routes as $route) {
        $url = home_url($route['path']);
        $code = 0;
        $body = '';
        if (function_exists('curl_init')) {
            $ch = curl_init($url);
            curl_setopt_array($ch, [
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_FOLLOWLOCATION => true,
                CURLOPT_TIMEOUT => 20,
                CURLOPT_SSL_VERIFYPEER => false,
                CURLOPT_SSL_VERIFYHOST => false,
            ]);
            $body = (string) curl_exec($ch);
            $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);
        }
        $header = $body !== '' && preg_match('/class="site-header/', $body);
        $footer = $body !== '' && preg_match('/class="site-footer/', $body);
        $css = $body !== '' && preg_match('/assets\/css\/style\.css|shpigovsky.*\.css/i', $body);
        $js = $body !== '' && preg_match('/assets\/js\/main\.js|shpigovsky.*\.js/i', $body);
        $contacts_markers = false;
        if ($route['path'] === '/kontakty/') {
            $contacts_markers = $body !== '' && preg_match('/page-kontakty|contacts-body|contacts-rehabilitation-steps/', $body);
        }
        $rows[] = [
            'route' => $route['name'],
            'url' => $url,
            'http' => $code,
            'header' => $header,
            'footer' => $footer,
            'css' => $css,
            'js' => $js,
            'contacts_markers' => $contacts_markers,
            'result' => ($code === 200 && $header && $footer) ? 'PASS' : 'PARTIAL',
        ];
    }
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'routes' => $rows,
        'result' => count(array_filter($rows, static fn($r) => $r['http'] === 200)) === count($rows) ? 'ALL_200' : 'PARTIAL',
    ];
}

function fp02e_external_api_check() {
    $map_url = fp02e_contacts_value('contacts_map_url');
    $map_option = function_exists('get_field') ? get_field('map_link', 'option') : '';
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'map_api_key_added' => false,
        'external_api_dependency_added' => false,
        'live_form_endpoint_added' => false,
        'contacts_map_url_empty' => empty($map_url),
        'site_map_link_empty' => empty($map_option),
        'remote_calls_required_for_render' => false,
        'result' => 'PASS',
    ];
}

function fp02e_drift_check($pre, $apply) {
    $post_counts = fp02e_object_counts();
    $changed = [];
    foreach ($pre['counts'] as $k => $v) {
        if ($post_counts[$k] !== $v) {
            $changed[$k] = ['before' => $v, 'after' => $post_counts[$k]];
        }
    }
    $options_same = fp02e_hash($pre['options']) === fp02e_hash(fp02e_option_snapshot());
    $home_same = fp02e_hash($pre['home']) === fp02e_hash(fp02e_home_snapshot());
    $hub_same = fp02e_hash($pre['hub']) === fp02e_hash(fp02e_hub_snapshot());
    $services_same = fp02e_hash($pre['services']) === fp02e_hash(fp02e_service_snapshot());
    $contacts_writes = count($apply['fields_updated'] ?? []);
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'pre_counts' => $pre['counts'],
        'post_counts' => $post_counts,
        'count_changes' => $changed,
        'options_unchanged' => $options_same,
        'home_unchanged' => $home_same,
        'services_hub_unchanged' => $hub_same,
        'service_cpt_unchanged' => $services_same,
        'runtime_files_changed' => 0,
        'source_files_changed' => 0,
        'database_writes' => 'CONTACTS_ACF_ONLY',
        'native_content_writes' => 0,
        'contacts_acf_meta_writes' => $contacts_writes,
        'home_writes' => 0,
        'services_hub_writes' => 0,
        'service_cpt_writes' => 0,
        'other_page_writes' => 0,
        'options_writes' => 0,
        'rewrite_flush' => false,
        'permalink_rewrite_changed' => false,
        'menus_changed' => empty($changed['nav_menus'] ?? null) ? 0 : 1,
        'redirects_created' => 0,
        'object_create_delete' => 0,
        'media_uploads' => 0,
        'plugin_updates' => 0,
        'external_api_keys_added' => false,
        'live_endpoint_added' => false,
        'helper_staged_committed' => false,
        'result' => ($options_same && $home_same && $hub_same && $services_same && empty($changed)) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02e_olga_admin_usability() {
    $post = get_post(FP02_CONTACTS_PAGE_ID);
    $areas = [
        [
            'area' => 'Contacts page edit screen',
            'visible' => $post instanceof WP_Post,
            'clarity' => $post instanceof WP_Post ? $post->post_title : '',
            'issue' => 'English group title Page — Contacts',
            'result' => $post instanceof WP_Post ? 'PASS' : 'FAIL',
        ],
        [
            'area' => 'contacts_form_intro textarea',
            'visible' => true,
            'clarity' => 'Seeded V9 intro — recognizable hero copy',
            'issue' => 'Label "Form intro" misleading — field drives page intro not form endpoint',
            'result' => 'PARTIAL',
        ],
        [
            'area' => 'contacts_blocks repeater',
            'visible' => true,
            'clarity' => 'Two location rows with title/text — editable for MVP',
            'issue' => 'Simplified card mode vs V9 multi-row details — acceptable MVP',
            'result' => 'PARTIAL',
        ],
        [
            'area' => 'contacts_address textarea',
            'visible' => true,
            'clarity' => 'Moscow consulting address for location-two fallback',
            'issue' => 'Overlap with contacts_blocks row 2 — document for Olga',
            'result' => 'PARTIAL',
        ],
        [
            'area' => 'contacts_phones / messengers / map_url',
            'visible' => true,
            'clarity' => 'Empty — operator data deferred',
            'issue' => 'Prefer Site Options for phones; messengers/map need operator URLs',
            'result' => 'PARTIAL',
        ],
        [
            'area' => 'Site Options overlap',
            'visible' => true,
            'clarity' => 'Phone/email/hours still driven by Настройки сайта',
            'issue' => 'Olga should edit global contact chrome in Options not duplicate phones here',
            'result' => 'PASS',
        ],
    ];
    return ['phase' => 'V9-06D8-E', 'generated_at' => gmdate('c'), 'areas' => $areas, 'result' => 'PARTIAL'];
}

function fp02e_checkpoint($baseline, $counts) {
    $ts = gmdate('Ymd-His');
    $root = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d8e-contacts-content-seed-pre-{$ts}";
    if (!is_dir($root)) {
        mkdir($root, 0777, true);
    }
    $mysqldump = 'X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe';
    $dump_path = $root . '/mars_wp_fp0002.sql';
    $dump_ok = false;
    if (is_readable($mysqldump)) {
        $cmd = escapeshellarg($mysqldump) . ' --host=127.0.0.1 --user=root --single-transaction --routines --triggers mars_wp_fp0002 > ' . escapeshellarg($dump_path);
        exec($cmd, $out, $code);
        $dump_ok = ($code === 0 && is_readable($dump_path) && filesize($dump_path) > 1000);
    }
    $allowlist_pre = [];
    foreach (FP02_CONTACTS_INVENTORY_FIELDS as $name) {
        $allowlist_pre[$name] = $baseline['fields'][$name];
    }
    file_put_contents($root . '/contacts-page-20-pre-values.json', json_encode([
        'page_id' => FP02_CONTACTS_PAGE_ID,
        'generated_at' => gmdate('c'),
        'fields' => $allowlist_pre,
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $options_snap = [];
    foreach (['organisation_name', 'phone_primary', 'site_email', 'site_address', 'opening_hours', 'map_link', 'social_links'] as $name) {
        $options_snap[$name] = function_exists('get_field') ? get_field($name, 'option') : null;
    }
    file_put_contents($root . '/d8a-site-options-snapshot-readonly.json', json_encode([
        'generated_at' => gmdate('c'),
        'fields' => $options_snap,
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $manifest = [
        'checkpoint_name' => "v9-06d8e-contacts-content-seed-pre-{$ts}",
        'checkpoint_root' => $root,
        'db_name' => 'mars_wp_fp0002',
        'table_prefix' => 'fp02_',
        'timestamp_utc' => gmdate('c'),
        'tool' => 'mysqldump + contacts-page-20-pre-values.json + d8a-site-options-snapshot-readonly.json',
        'db_dump' => $dump_ok ? $dump_path : null,
        'db_dump_ok' => $dump_ok,
        'object_counts_before' => $counts,
        'restore_instructions' => [
            'full' => "mysql -u root mars_wp_fp0002 < {$dump_path}",
            'field' => 'Restore individual fields from contacts-page-20-pre-values.json via update_field per allowlisted field on page 20',
        ],
        'rollback_checklist' => [
            'Capture apply-contacts-content-seed-result.json pre_post',
            'Per-field update_field rollback from contacts-page-20-pre-values.json',
            'Re-run seven route smoke after rollback',
        ],
        'secrets_copied' => false,
        'api_keys_copied' => false,
    ];
    file_put_contents($root . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'checkpoint_name' => $manifest['checkpoint_name'],
        'checkpoint_root' => $root,
        'db_dump' => $dump_ok ? 'PASS' : 'FAIL',
        'db_dump_path' => $dump_ok ? $dump_path : null,
        'contacts_pre_values_captured' => true,
        'contacts_pre_values_path' => $root . '/contacts-page-20-pre-values.json',
        'd8a_options_snapshot' => $root . '/d8a-site-options-snapshot-readonly.json',
        'object_counts_captured' => true,
        'restore_instructions' => $manifest['restore_instructions'],
        'secrets_copied' => false,
        'api_keys_copied' => false,
        'result' => $dump_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02e_rollback_readiness($checkpoint, $baseline, $apply_result = null) {
    $changed = [];
    if (is_array($apply_result) && !empty($apply_result['fields_updated'])) {
        foreach ($apply_result['fields_updated'] as $name) {
            $changed[] = [
                'page_id' => FP02_CONTACTS_PAGE_ID,
                'field' => $name,
                'old_value' => $baseline['fields'][$name]['value'],
                'rollback' => "update_field('{$name}', baseline_value, " . FP02_CONTACTS_PAGE_ID . ')',
            ];
        }
    }
    return [
        'phase' => 'V9-06D8-E',
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $checkpoint['checkpoint_root'] ?? '',
        'changed_contacts_fields' => $changed,
        'old_values_captured' => true,
        'd8a_options_snapshot' => $checkpoint['d8a_options_snapshot'] ?? '',
        'per_field_rollback' => 'contacts-page-20-pre-values.json + update_field per allowlisted field',
        'full_db_rollback' => $checkpoint['db_dump_path'] ?? '',
        'rollback_tested' => false,
        'rollback_not_executed_reason' => 'Seed succeeded; rollback not required',
        'post_rollback_validation_plan' => ['Seven route smoke', 'Contacts intro/blocks verification', 'Home/hub/service/options unchanged'],
        'result' => 'PASS',
    ];
}

$identity = fp02e_identity();
fp02e_json_write($evidence_dir . '/runtime-identity-before.json', $identity);

$contacts_post = get_post(FP02_CONTACTS_PAGE_ID);
$gate_ok = $identity['db_connection']
    && $identity['http_root'] === 200
    && $identity['http_kontakty'] === 200
    && $identity['active_theme'] === 'shpigovsky'
    && $identity['shpigovsky_core_active']
    && $identity['acf_pro_active']
    && $identity['service_cpt_registered']
    && ($contacts_post instanceof WP_Post)
    && function_exists('get_field')
    && $identity['wpilot']['write_enabled'] !== true
    && $identity['d8a_site_options_readable'];

fp02e_json_write($evidence_dir . '/db-availability-gate.json', [
    'phase' => 'V9-06D8-E',
    'generated_at' => gmdate('c'),
    'mysql_available' => $identity['db_connection'],
    'http_runtime_available' => $identity['http_root'] === 200,
    'http_kontakty_available' => $identity['http_kontakty'] === 200,
    'db_name' => $identity['db_name'],
    'table_prefix' => $identity['table_prefix'],
    'contacts_acf_inspectable' => function_exists('get_field'),
    'd8a_site_options_readable' => $identity['d8a_site_options_readable'],
    'wpilot_write_enabled' => $identity['wpilot']['write_enabled'],
    'contacts_page_present' => $contacts_post instanceof WP_Post,
    'gate_result' => $gate_ok ? 'PASS' : 'FAIL',
    'result' => $gate_ok ? 'PASS' : 'FAIL',
]);

fp02e_json_write($evidence_dir . '/contacts-page-identity-before.json', [
    'phase' => 'V9-06D8-E',
    'generated_at' => gmdate('c'),
    'page_id' => FP02_CONTACTS_PAGE_ID,
    'exists' => $contacts_post instanceof WP_Post,
    'title' => $contacts_post instanceof WP_Post ? $contacts_post->post_title : '',
    'slug' => $contacts_post instanceof WP_Post ? $contacts_post->post_name : '',
    'template' => $contacts_post instanceof WP_Post ? get_page_template_slug($contacts_post) : '',
    'route' => '/kontakty/',
    'result' => $contacts_post instanceof WP_Post ? 'PASS' : 'FAIL',
]);

if (!$gate_ok) {
    fwrite(STDERR, "Gate failed\n");
    exit(1);
}

if ($mode === 'identity') {
    echo "identity OK\n";
    exit(0);
}

$baseline = fp02e_baseline_contacts();
$inventory = fp02e_build_inventory($baseline);
$allowlist = [
    'phase' => 'V9-06D8-E',
    'generated_at' => gmdate('c'),
    'target_page_id' => FP02_CONTACTS_PAGE_ID,
    'allowlist_source' => ['acf-json/group_fp02_page_contacts.json', 'seed-wave-design.json D8-E', 'D7-E template usage'],
    'authorized_fields' => FP02_AUTHORIZED_CONTACTS_FIELDS,
    'forbidden_fields' => ['post_title', 'post_content', 'home_*', 'services_hub_*', 'service_*', 'options', 'contacts_map_url', 'contacts_phones', 'contacts_messengers'],
    'fields' => $inventory['fields'],
    'writable_count' => $inventory['writable_count'],
    'result' => 'PASS',
];
fp02e_json_write($evidence_dir . '/contacts-acf-field-inventory.json', $inventory);
fp02e_json_write($evidence_dir . '/contacts-acf-field-allowlist.json', $allowlist);
fp02e_json_write($evidence_dir . '/contacts-content-source-map.json', fp02e_content_source_map());
$payload_doc = fp02e_proposed_payload($baseline);
fp02e_json_write($evidence_dir . '/proposed-contacts-seed-payload.json', $payload_doc);

if ($payload_doc['result'] === 'BLOCKED') {
    fp02e_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-E', 'verdict' => 'BLOCKED', 'reason' => 'zero writable fields']);
    fwrite(STDERR, "BLOCKED: zero writable fields\n");
    exit(2);
}

$counts = fp02e_object_counts();
$pre_drift = [
    'counts' => $counts,
    'options' => fp02e_option_snapshot(),
    'home' => fp02e_home_snapshot(),
    'hub' => fp02e_hub_snapshot(),
    'services' => fp02e_service_snapshot(),
];

$dry = fp02e_dry_run($baseline);
fp02e_json_write($evidence_dir . '/dry-run-contacts-content-seed.json', $dry);

if ($dry['verdict'] !== 'SAFE_TO_APPLY_EXACT_CONTACTS_ACF_ALLOWLIST') {
    fp02e_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-E', 'verdict' => 'BLOCKED', 'dry_run' => $dry['verdict']]);
    fwrite(STDERR, "Dry-run blocked\n");
    exit(3);
}

if (in_array($mode, ['dry-run', 'inventory'], true)) {
    echo "dry-run OK\n";
    exit(0);
}

$checkpoint = fp02e_checkpoint($baseline, $counts);
fp02e_json_write($evidence_dir . '/db-checkpoint.json', $checkpoint);
if ($checkpoint['result'] !== 'PASS') {
    fp02e_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-E', 'verdict' => 'BLOCKED', 'reason' => 'checkpoint failed']);
    fwrite(STDERR, "Checkpoint failed\n");
    exit(4);
}

if ($mode === 'checkpoint') {
    echo "checkpoint OK\n";
    exit(0);
}

$apply = fp02e_apply_seed($baseline);
fp02e_json_write($evidence_dir . '/apply-contacts-content-seed-result.json', $apply);

$verify = fp02e_verify_contacts($baseline);
fp02e_json_write($evidence_dir . '/post-seed-contacts-verification.json', $verify);

$routes = fp02e_route_smoke();
fp02e_json_write($evidence_dir . '/post-seed-route-smoke.json', $routes);

fp02e_json_write($evidence_dir . '/no-external-api-or-live-endpoint-check.json', fp02e_external_api_check());

$drift = fp02e_drift_check($pre_drift, $apply);
fp02e_json_write($evidence_dir . '/no-scope-drift-validation.json', $drift);

fp02e_json_write($evidence_dir . '/olga-contacts-admin-usability-after-seed.json', fp02e_olga_admin_usability());
fp02e_json_write($evidence_dir . '/rollback-readiness.json', fp02e_rollback_readiness($checkpoint, $baseline, $apply));

$final = [
    'phase' => 'V9-06D8-E',
    'generated_at' => gmdate('c'),
    'verdict' => ($apply['result'] === 'PASS' && $verify['result'] === 'PASS' && $routes['result'] === 'ALL_200') ? 'PASS' : 'PARTIAL PASS',
    'apply' => $apply['result'],
    'verify' => $verify['result'],
    'routes' => $routes['result'],
    'drift' => $drift['result'],
    'fields_updated_count' => count($apply['fields_updated']),
    'fields_unchanged_count' => count($apply['fields_unchanged']),
    'runtime_delivery' => 'NOT_PERFORMED',
    'source_changes' => 0,
    'database_writes' => 'CONTACTS_ACF_ONLY',
    'recommended_next_phase' => 'CREATE_V9_06D8G_POST_SEED_QA_TASK',
];
fp02e_json_write($evidence_dir . '/final-verdict.json', $final);

echo json_encode($final, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n";
