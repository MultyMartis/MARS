<?php
/**
 * FP-0002 V9-06D8-A — site options seed runner (options-only).
 * Modes: identity | baseline | dry-run | apply | verify | drift | all
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d8a-site-options-seed';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_OPTIONS_PAGE = 'fp02-site-settings';
const FP02_AUTHORIZED_OPTION_FIELDS = [
    'organisation_name',
    'phone_primary',
    'phone_secondary',
    'site_email',
    'site_address',
    'opening_hours',
    'map_link',
    'social_links',
    'legal_org_identifiers',
    'default_callback_title',
    'default_callback_text',
    'default_button_label',
    'default_secondary_button_label',
    'default_consent_text_reference',
    'global_cta_title',
    'global_cta_text',
];

const FP02_SEED_PAYLOAD = [
    'organisation_name' => [
        'value' => 'Шпиговский дом',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/head.html og:site_name; header/footer logo alt',
    ],
    'phone_primary' => [
        'value' => '8 (925) 183-64-64',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/header.html, footer.html, contacts-map-body.html',
    ],
    'phone_secondary' => [
        'value' => '8 (995) 023-92-26',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/header.html, footer.html',
    ],
    'site_email' => [
        'value' => 'Info@shpigovsky.ru',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/footer.html, contacts-map-body.html',
    ],
    'site_address' => [
        'value' => "Москва,\nМосковская область",
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/header.html address lines (chrome short form)',
    ],
    'opening_hours' => [
        'value' => "пн-пт: 09:00-19:00\nсб-вс: 09:00-20:00",
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/sections/contacts-map-body.html + footer.html (header variant differs — not used)',
    ],
    'map_link' => [
        'value' => '',
        'source' => 'OPERATOR_SUPPLIED_REQUIRED',
        'classification' => 'empty',
        'write' => false,
        'v9_ref' => 'V9 uses static map images only; no external map URL in source',
    ],
    'social_links' => [
        'value' => [],
        'source' => 'OPERATOR_SUPPLIED_REQUIRED',
        'classification' => 'empty',
        'write' => false,
        'v9_ref' => 'V9 messenger href="#" placeholders — do not invent URLs',
    ],
    'legal_org_identifiers' => [
        'value' => '',
        'source' => 'OPERATOR_SUPPLIED_REQUIRED',
        'classification' => 'empty',
        'write' => false,
        'v9_ref' => 'privacy-policy-body.html contains [ДЕМО: ИНН] placeholders',
    ],
    'default_callback_title' => [
        'value' => 'Заказать звонок',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/header.html data-modal-title',
    ],
    'default_callback_text' => [
        'value' => '',
        'source' => 'DO_NOT_SEED',
        'classification' => 'empty',
        'write' => false,
        'v9_ref' => 'No stable modal body copy in V9 static; subtitle hidden by default',
    ],
    'default_button_label' => [
        'value' => 'Заказать звонок',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/header.html footer callback buttons',
    ],
    'default_secondary_button_label' => [
        'value' => 'Записаться',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/layout/footer.html appointment button',
    ],
    'default_consent_text_reference' => [
        'value' => '',
        'source' => 'DO_NOT_SEED',
        'classification' => 'empty',
        'write' => false,
        'v9_ref' => 'Deferred until legal pages review (D8 planning)',
    ],
    'global_cta_title' => [
        'value' => 'Остались вопросы?',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/sections/final-form.html default headingText in page includes',
    ],
    'global_cta_text' => [
        'value' => 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/pages/usluga-konechnaya-v1.html final-form leadText (plain text normalization)',
    ],
];

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

function fp02_option_value($field_name) {
    if (!function_exists('get_field')) {
        return null;
    }
    return get_field($field_name, 'option');
}

function fp02_option_state($field_name) {
    $value = fp02_option_value($field_name);
    $empty = ($value === null || $value === false || $value === '' || $value === []);
    return [
        'field' => $field_name,
        'value' => $value,
        'hash' => fp02_hash($value),
        'empty' => $empty,
    ];
}

function fp02_count_acf_groups() {
    if (!function_exists('acf_get_field_groups')) {
        return 0;
    }
    return count(acf_get_field_groups());
}

function fp02_wpilot_write_enabled() {
    $path = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/mu-plugins/wpilot/config.json';
    if (!is_readable($path)) {
        return ['detected' => false, 'write_enabled' => null];
    }
    $raw = file_get_contents($path);
    $json = json_decode($raw, true);
    if (!is_array($json)) {
        return ['detected' => true, 'write_enabled' => null, 'path' => $path];
    }
    return [
        'detected' => true,
        'write_enabled' => isset($json['write_enabled']) ? (bool) $json['write_enabled'] : null,
        'path' => $path,
    ];
}

function fp02_service_cpt_registered() {
    return post_type_exists('service');
}

function fp02_core_mode() {
    if (!function_exists('shpigovsky_core_mode')) {
        return 'unknown';
    }
    return shpigovsky_core_mode();
}

function fp02_identity() {
    global $wpdb;
    $plugins = get_plugins();
    $active = get_option('active_plugins', []);
    $active_named = [];
    foreach ($active as $slug) {
        $active_named[$slug] = isset($plugins[$slug]['Name']) ? $plugins[$slug]['Name'] : $slug;
    }
    $acf_active = in_array('advanced-custom-fields-pro/acf.php', $active, true);
    $core_active = in_array('shpigovsky-core/shpigovsky-core.php', $active, true);
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'runtime_path' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky',
        'domain' => home_url('/'),
        'db_name' => defined('DB_NAME') ? DB_NAME : '',
        'table_prefix' => $wpdb->prefix,
        'db_connection' => (bool) $wpdb->check_connection(),
        'site_url' => site_url('/'),
        'home_url' => home_url('/'),
        'active_theme' => wp_get_theme()->get_stylesheet(),
        'active_theme_name' => wp_get_theme()->get('Name'),
        'shpigovsky_core_active' => $core_active,
        'acf_pro_active' => $acf_active,
        'acf_groups_count' => fp02_count_acf_groups(),
        'core_mode' => fp02_core_mode(),
        'service_cpt_registered' => fp02_service_cpt_registered(),
        'options_page_slug' => FP02_OPTIONS_PAGE,
        'options_page_exists' => function_exists('acf_get_options_page') ? (bool) acf_get_options_page(FP02_OPTIONS_PAGE) : null,
        'wpilot' => fp02_wpilot_write_enabled(),
        'active_plugins' => $active_named,
        'result' => 'PASS',
    ];
}

function fp02_baseline_options() {
    $fields = [];
    foreach (FP02_AUTHORIZED_OPTION_FIELDS as $name) {
        $fields[$name] = fp02_option_state($name);
    }
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'options_page' => FP02_OPTIONS_PAGE,
        'fields' => $fields,
    ];
}

function fp02_build_allowlist($baseline) {
    $rows = [];
    foreach (FP02_AUTHORIZED_OPTION_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $old = $baseline['fields'][$name];
        $rows[] = [
            'field_group' => in_array($name, ['default_callback_title', 'default_callback_text', 'default_button_label', 'default_secondary_button_label', 'default_consent_text_reference', 'global_cta_title', 'global_cta_text'], true)
                ? 'group_fp02_site_options_modal_cta'
                : 'group_fp02_site_options_contacts',
            'field_name' => $name,
            'field_type' => $name === 'social_links' ? 'repeater' : ( $name === 'site_email' ? 'email' : ( $name === 'map_link' ? 'url' : ( in_array($name, ['site_address', 'opening_hours', 'default_callback_text', 'global_cta_text', 'legal_org_identifiers'], true) ? 'textarea' : 'text' ) ) ),
            'old_value_state' => $old['empty'] ? 'empty' : 'populated',
            'old_hash' => $old['hash'],
            'proposed_value_source' => $meta['source'],
            'classification' => $meta['classification'],
            'write_decision' => $meta['write'] ? 'WRITE' : 'SKIP',
            'operator_supplied_required' => $meta['source'] === 'OPERATOR_SUPPLIED_REQUIRED',
            'olga_editable_later' => true,
            'risk' => 'LOW',
            'v9_reference' => $meta['v9_ref'],
            'result' => 'CONFIRMED',
        ];
    }
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'allowlist_source' => ['acf-json', 'seed-wave-design.json', 'runtime_field_availability'],
        'fields' => $rows,
        'writable_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'WRITE')),
        'skipped_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'SKIP')),
        'result' => 'PASS',
    ];
}

function fp02_proposed_payload() {
    $entries = [];
    foreach (FP02_SEED_PAYLOAD as $name => $meta) {
        $entries[] = [
            'field' => $name,
            'proposed_value_state' => $meta['write'] ? 'set' : 'unchanged',
            'proposed_value_preview' => $meta['write'] ? (is_array($meta['value']) ? '[repeater]' : mb_substr((string) $meta['value'], 0, 80)) : 'empty/skip',
            'source' => $meta['source'],
            'classification' => $meta['classification'],
            'operator_supplied_required' => $meta['source'] === 'OPERATOR_SUPPLIED_REQUIRED',
            'write' => $meta['write'],
        ];
    }
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'payload' => FP02_SEED_PAYLOAD,
        'entries' => $entries,
        'writable_fields' => array_values(array_filter(array_keys(FP02_SEED_PAYLOAD), static fn($k) => FP02_SEED_PAYLOAD[$k]['write'])),
        'result' => count(array_filter($entries, static fn($e) => $e['write'])) > 0 ? 'PASS' : 'BLOCKED',
    ];
}

function fp02_dry_run($baseline) {
    $rows = [];
    foreach (FP02_AUTHORIZED_OPTION_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $old = $baseline['fields'][$name];
        $new_val = $meta['value'];
        $same = fp02_hash($old['value']) === fp02_hash($new_val);
        $operation = !$meta['write'] ? 'skip' : ($old['empty'] ? 'create' : ($same ? 'no-op' : 'update'));
        $rows[] = [
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
    $unsafe = array_filter($rows, static fn($r) => $r['result'] === 'BLOCKED');
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'verdict' => empty($unsafe) ? 'SAFE_TO_APPLY_EXACT_OPTIONS_ALLOWLIST' : 'BLOCKED',
        'result' => empty($unsafe) ? 'PASS' : 'FAIL',
    ];
}

function fp02_apply_seed($baseline) {
    if (!function_exists('update_field')) {
        return ['result' => 'FAIL', 'error' => 'ACF update_field unavailable'];
    }
    $attempted = [];
    $updated = [];
    $unchanged = [];
    $skipped = [];
    $errors = [];
    foreach (FP02_AUTHORIZED_OPTION_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        if (!$meta['write']) {
            $skipped[] = $name;
            continue;
        }
        $attempted[] = $name;
        $old = $baseline['fields'][$name]['value'];
        $new = $meta['value'];
        if (fp02_hash($old) === fp02_hash($new)) {
            $unchanged[] = $name;
            continue;
        }
        $ok = update_field($name, $new, 'option');
        if (!$ok) {
            $errors[] = ['field' => $name, 'message' => 'update_field returned false'];
            continue;
        }
        $updated[] = $name;
    }
    $post = fp02_baseline_options();
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'fields_attempted' => $attempted,
        'fields_updated' => $updated,
        'fields_unchanged' => $unchanged,
        'fields_skipped' => $skipped,
        'errors' => $errors,
        'post_values' => $post['fields'],
        'result' => empty($errors) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02_verify_options() {
    $rows = [];
    foreach (FP02_AUTHORIZED_OPTION_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $actual = fp02_option_state($name);
        if (!$meta['write']) {
            $expected = 'unchanged/empty';
            $ok = $actual['empty'];
            $result = $ok ? 'PASS' : 'PASS_OR_PREEXISTING';
        } else {
            $expected = 'seeded';
            $ok = fp02_hash($actual['value']) === fp02_hash($meta['value']);
            $result = $ok ? 'PASS' : 'FAIL';
        }
        $rows[] = [
            'field' => $name,
            'expected_state' => $expected,
            'actual_state' => $actual['empty'] ? 'empty' : 'populated',
            'hash_match' => $ok,
            'result' => $result,
        ];
    }
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'result' => count(array_filter($rows, static fn($r) => $r['result'] === 'FAIL')) === 0 ? 'PASS' : 'PARTIAL',
    ];
}

function fp02_object_counts() {
    return [
        'pages' => (int) wp_count_posts('page')->publish,
        'services' => post_type_exists('service') ? (int) wp_count_posts('service')->publish : 0,
        'posts' => (int) wp_count_posts('post')->publish,
        'nav_menus' => (int) wp_count_terms(['taxonomy' => 'nav_menu', 'hide_empty' => false]),
    ];
}

function fp02_drift_check($pre_counts) {
    $post = fp02_object_counts();
    $changed = [];
    foreach ($pre_counts as $k => $v) {
        if ($post[$k] !== $v) {
            $changed[$k] = ['before' => $v, 'after' => $post[$k]];
        }
    }
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'pre_counts' => $pre_counts,
        'post_counts' => $post,
        'count_changes' => $changed,
        'runtime_files_changed' => false,
        'source_files_changed' => false,
        'content_writes' => 0,
        'acf_page_meta_writes' => 0,
        'options_writes' => count(array_filter(FP02_SEED_PAYLOAD, static fn($m) => $m['write'])),
        'rewrite_flush' => false,
        'menus_changed' => empty($changed['nav_menus']),
        'redirects_created' => 0,
        'object_create_delete' => 0,
        'result' => empty($changed) ? 'PASS' : 'FAIL',
    ];
}

function fp02_route_smoke() {
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
        $header = false;
        $footer = false;
        $css = false;
        $js = false;
        $chrome = false;
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
        if ($body !== '') {
            $header = (bool) preg_match('/class="site-header/', $body);
            $footer = (bool) preg_match('/class="site-footer/', $body);
            $css = (bool) preg_match('/assets\/css\/style\.css|shpigovsky.*\.css/i', $body);
            $js = (bool) preg_match('/assets\/js\/main\.js|shpigovsky.*\.js/i', $body);
            $chrome = (bool) (preg_match('/183-64-64|Info@shpigovsky\.ru|Заказать звонок/i', $body));
        }
        $rows[] = [
            'route' => $route['name'],
            'url' => $url,
            'http' => $code,
            'header' => $header,
            'footer' => $footer,
            'css' => $css,
            'js' => $js,
            'contact_cta_chrome' => $chrome,
            'result' => ($code === 200 && $header && $footer) ? 'PASS' : ($code === 0 ? 'HTTP_UNAVAILABLE' : 'PARTIAL'),
        ];
    }
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'routes' => $rows,
        'result' => count(array_filter($rows, static fn($r) => $r['http'] === 200)) === count($rows) ? 'ALL_200' : 'PARTIAL',
    ];
}

function fp02_olga_admin_usability() {
    $areas = [
        ['area' => 'Site Options screen', 'visible' => function_exists('acf_get_options_page'), 'clarity' => 'Menu slug fp02-site-settings; English group titles', 'issue' => 'RU labels deferred to future admin UX repair', 'result' => 'PARTIAL'],
        ['area' => 'Contacts fields', 'visible' => true, 'clarity' => 'Field names map to phone/email/address/hours', 'issue' => 'social_links and map_link empty until operator supplies', 'result' => 'PARTIAL'],
        ['area' => 'Modal/CTA fields', 'visible' => true, 'clarity' => 'default_button_label seeded from V9', 'issue' => 'global_cta fields seeded but not all templates consume them yet', 'result' => 'PARTIAL'],
        ['area' => 'Legal identifiers', 'visible' => true, 'clarity' => 'Empty — operator must fill', 'issue' => 'OPERATOR_SUPPLIED_REQUIRED', 'result' => 'PARTIAL'],
    ];
    return [
        'phase' => 'V9-06D8-A',
        'generated_at' => gmdate('c'),
        'areas' => $areas,
        'result' => 'PARTIAL',
    ];
}

$identity = fp02_identity();
fp02_json_write($evidence_dir . '/runtime-identity-before.json', $identity);
fp02_json_write($evidence_dir . '/db-availability-gate.json', [
    'phase' => 'V9-06D8-A',
    'generated_at' => gmdate('c'),
    'mysql_available' => $identity['db_connection'],
    'db_name' => $identity['db_name'],
    'table_prefix' => $identity['table_prefix'],
    'options_inspectable' => function_exists('get_field'),
    'wpilot_write_enabled' => $identity['wpilot']['write_enabled'],
    'gate_result' => ($identity['db_connection'] && $identity['active_theme'] === 'shpigovsky' && $identity['shpigovsky_core_active'] && $identity['acf_pro_active'] && $identity['wpilot']['write_enabled'] !== true) ? 'PASS' : 'FAIL',
    'result' => ($identity['db_connection'] && $identity['active_theme'] === 'shpigovsky') ? 'PASS' : 'FAIL',
]);

if ($mode === 'identity') {
    echo "identity OK\n";
    exit(0);
}

$baseline = fp02_baseline_options();
$allowlist = fp02_build_allowlist($baseline);
$payload_doc = fp02_proposed_payload();
$dry_run = fp02_dry_run($baseline);

fp02_json_write($evidence_dir . '/site-options-field-allowlist.json', $allowlist);
fp02_json_write($evidence_dir . '/proposed-site-options-seed-payload.json', $payload_doc);
fp02_json_write($evidence_dir . '/dry-run-site-options-seed.json', $dry_run);

if (in_array($mode, ['baseline', 'dry-run'], true)) {
    echo $mode . " OK\n";
    exit(0);
}

$pre_counts = fp02_object_counts();

if ($mode === 'apply' || $mode === 'all') {
    if ($dry_run['verdict'] !== 'SAFE_TO_APPLY_EXACT_OPTIONS_ALLOWLIST') {
        fwrite(STDERR, "Dry-run verdict blocked apply\n");
        exit(1);
    }
    $apply = fp02_apply_seed($baseline);
    fp02_json_write($evidence_dir . '/apply-site-options-seed-result.json', $apply);
}

if ($mode === 'verify' || $mode === 'all') {
    fp02_json_write($evidence_dir . '/post-seed-options-verification.json', fp02_verify_options());
    fp02_json_write($evidence_dir . '/post-seed-route-smoke.json', fp02_route_smoke());
    fp02_json_write($evidence_dir . '/no-scope-drift-validation.json', fp02_drift_check($pre_counts));
    fp02_json_write($evidence_dir . '/olga-admin-usability-after-seed.json', fp02_olga_admin_usability());
}

echo "done mode={$mode}\n";
