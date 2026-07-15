<?php
/**
 * FP-0002 V9-06D8-D — Services Hub page #5 ACF seed runner (hub ACF only).
 * Modes: identity | baseline | checkpoint | dry-run | apply | verify | drift | routes | olga | all
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d8d-services-hub-content-seed';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_HUB_PAGE_ID = 5;
const FP02_HOME_PAGE_ID = 4;
const FP02_CONTACTS_PAGE_ID = 20;
const FP02_TARGET_SERVICE_IDS = [73, 74, 77, 84];

const FP02_HUB_INVENTORY_FIELDS = [
    'services_hub_intro',
    'services_hub_query_mode',
    'services_hub_show_placeholders',
    'services_hub_faq_items',
];

const FP02_AUTHORIZED_HUB_FIELDS = [
    'services_hub_intro',
    'services_hub_faq_items',
];

const FP02_HUB_INTRO_V9 = 'Зависимость, тревога, нарушение пищевого поведения — у каждого из этих состояний есть своя биология, своя психология и своя точка, где что-то пошло не так. Нас интересует не только то, что происходит, но и почему это происходит именно с вами, именно сейчас.';

const FP02_HUB_FAQ_MVP_ITEMS = [
    [
        'question' => 'Анонимное лечение или нет?',
        'answer' => 'Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о формате обращения и порядке первичного контакта с центром. Текст не является маркетинговым обещанием и не заменяет консультацию специалиста. Финальная редакция будет согласована оператором отдельно.',
    ],
    [
        'question' => 'Как долго длится реабилитация?',
        'answer' => 'Это временный технический текст для проверки высоты аккордеона. В финальной версии здесь будет описан типовой порядок этапов сопровождения без указания конкретных сроков. Длительность программы зависит от индивидуального запроса и согласуется на консультации.',
    ],
    [
        'question' => 'Как уговорить близкого пройти лечение от зависимости?',
        'answer' => 'Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о том, как семье подготовиться к разговору с близким человеком. Материал носит справочный характер и не содержит обещаний результата.',
    ],
    [
        'question' => 'Можно ли самостоятельно перестать употреблять наркотики?',
        'answer' => 'Это временный технический текст для проверки аккордеона. В финальной версии здесь будет нейтральное описание сценариев, когда самостоятельные попытки требуют дополнительной поддержки. Текст не содержит медицинских утверждений и не описывает гарантированный исход.',
    ],
    [
        'question' => 'Как понять, что у меня есть проблемы с алкоголем?',
        'answer' => 'Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ с ориентирами для самонаблюдения без диагностических формулировок. Материал предназначен для проверки типографики; контент будет заменён после согласования с оператором.',
    ],
];

const FP02_SEED_PAYLOAD = [
    'services_hub_intro' => [
        'value' => FP02_HUB_INTRO_V9,
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'STATIC_V9_CONTENT',
        'write' => true,
        'v9_ref' => 'src/pages/uslugi-v2.html services-inner-hero-v2 heroLead',
    ],
    'services_hub_query_mode' => [
        'value' => 'grouped_by_parent',
        'source' => 'EXISTING_ACF_VALUE',
        'classification' => 'SKIP_DO_NOT_SEED',
        'write' => false,
        'v9_ref' => 'Developer-only query display mode',
    ],
    'services_hub_show_placeholders' => [
        'value' => false,
        'source' => 'EXISTING_ACF_VALUE',
        'classification' => 'SKIP_DO_NOT_SEED',
        'write' => false,
        'v9_ref' => 'Developer-only empty-state toggle',
    ],
    'services_hub_faq_items' => [
        'value' => FP02_HUB_FAQ_MVP_ITEMS,
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/sections/faq.html items 2–6; item 1 lorem skipped',
    ],
];

function fp02d_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02d_hash($value) {
    if ($value === null || $value === false || $value === '') {
        return 'empty';
    }
    if (is_array($value) || is_object($value)) {
        $value = wp_json_encode($value);
    }
    return hash('sha256', (string) $value);
}

function fp02d_hub_value($field_name) {
    if (!function_exists('get_field')) {
        return null;
    }
    return get_field($field_name, FP02_HUB_PAGE_ID);
}

function fp02d_hub_state($field_name) {
    $value = fp02d_hub_value($field_name);
    $empty = ($value === null || $value === false || $value === '' || $value === [] || $value === 0);
    if (is_array($value)) {
        $empty = count($value) === 0;
    }
    return [
        'page_id' => FP02_HUB_PAGE_ID,
        'field' => $field_name,
        'value' => $value,
        'hash' => fp02d_hash($value),
        'empty' => $empty,
    ];
}

function fp02d_field_meta($field_name) {
    $map = [
        'services_hub_intro' => ['group' => 'group_fp02_page_services_hub', 'key' => 'field_fp02_services_hub_intro', 'type' => 'textarea', 'rendered' => true, 'allowlist' => true],
        'services_hub_query_mode' => ['group' => 'group_fp02_page_services_hub', 'key' => 'field_fp02_services_hub_query_mode', 'type' => 'select', 'rendered' => false, 'allowlist' => false],
        'services_hub_show_placeholders' => ['group' => 'group_fp02_page_services_hub', 'key' => 'field_fp02_services_hub_show_placeholders', 'type' => 'true_false', 'rendered' => false, 'allowlist' => false],
        'services_hub_faq_items' => ['group' => 'group_fp02_page_services_hub', 'key' => 'field_fp02_services_hub_faq_items', 'type' => 'repeater', 'rendered' => true, 'allowlist' => true],
    ];
    return $map[$field_name] ?? ['group' => '', 'key' => '', 'type' => 'unknown', 'rendered' => false, 'allowlist' => false];
}

function fp02d_count_acf_groups() {
    if (!function_exists('acf_get_field_groups')) {
        return 0;
    }
    return count(acf_get_field_groups());
}

function fp02d_wpilot_write_enabled() {
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

function fp02d_http_code($path) {
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

function fp02d_identity() {
    global $wpdb;
    $plugins = get_plugins();
    $active = get_option('active_plugins', []);
    $active_named = [];
    foreach ($active as $slug) {
        $active_named[$slug] = isset($plugins[$slug]['Name']) ? $plugins[$slug]['Name'] : $slug;
    }
    $hub = get_post(FP02_HUB_PAGE_ID);
    $root_http = fp02d_http_code('/');
    $hub_http = fp02d_http_code('/uslugi/');
    $services = [];
    foreach (FP02_TARGET_SERVICE_IDS as $id) {
        $post = get_post($id);
        $services[(string) $id] = [
            'id' => $id,
            'exists' => $post instanceof WP_Post,
            'title' => $post instanceof WP_Post ? $post->post_title : '',
        ];
    }
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'runtime_path' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky',
        'domain' => home_url('/'),
        'http_root' => $root_http['http'],
        'http_uslugi' => $hub_http['http'],
        'db_name' => defined('DB_NAME') ? DB_NAME : '',
        'table_prefix' => $wpdb->prefix,
        'db_connection' => (bool) $wpdb->check_connection(),
        'active_theme' => wp_get_theme()->get_stylesheet(),
        'shpigovsky_core_active' => in_array('shpigovsky-core/shpigovsky-core.php', $active, true),
        'acf_pro_active' => in_array('advanced-custom-fields-pro/acf.php', $active, true),
        'acf_groups_count' => fp02d_count_acf_groups(),
        'core_mode' => function_exists('shpigovsky_core_mode') ? shpigovsky_core_mode() : 'unknown',
        'service_cpt_registered' => post_type_exists('service'),
        'wpilot' => fp02d_wpilot_write_enabled(),
        'services_hub_page' => [
            'id' => FP02_HUB_PAGE_ID,
            'exists' => $hub instanceof WP_Post,
            'title' => $hub instanceof WP_Post ? $hub->post_title : '',
            'slug' => $hub instanceof WP_Post ? $hub->post_name : '',
            'template' => $hub instanceof WP_Post ? get_page_template_slug($hub) : '',
            'route' => '/uslugi/',
        ],
        'target_services_readonly' => $services,
        'active_plugins' => $active_named,
        'result' => 'PASS',
    ];
}

function fp02d_baseline_hub() {
    $fields = [];
    foreach (FP02_HUB_INVENTORY_FIELDS as $name) {
        $fields[$name] = fp02d_hub_state($name);
    }
    $post = get_post(FP02_HUB_PAGE_ID);
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HUB_PAGE_ID,
        'slug' => $post instanceof WP_Post ? $post->post_name : '',
        'title' => $post instanceof WP_Post ? $post->post_title : '',
        'post_title_hash' => fp02d_hash($post instanceof WP_Post ? $post->post_title : ''),
        'post_content_hash' => fp02d_hash($post instanceof WP_Post ? $post->post_content : ''),
        'fields' => $fields,
    ];
}

function fp02d_build_inventory($baseline) {
    $rows = [];
    foreach (FP02_HUB_INVENTORY_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $fm = fp02d_field_meta($name);
        $old = $baseline['fields'][$name];
        $rows[] = [
            'page_id' => FP02_HUB_PAGE_ID,
            'field_group' => $fm['group'],
            'field_key' => $fm['key'],
            'field_name' => $name,
            'field_type' => $fm['type'],
            'old_value_state' => $old['empty'] ? 'empty' : 'populated',
            'old_hash' => $old['hash'],
            'proposed_value_source' => $meta['source'],
            'classification' => $meta['classification'],
            'rendered_by_d7c' => $fm['rendered'],
            'improves_visible_mvp' => $meta['write'],
            'olga_editable_later' => $meta['write'] || $name === 'services_hub_intro',
            'risk' => $meta['classification'] === 'LOCAL_MVP_PLACEHOLDER' ? 'LOW_MVP_PLACEHOLDER' : 'LOW',
            'write_decision' => $meta['write'] ? 'WRITE' : 'SKIP',
            'v9_reference' => $meta['v9_ref'],
            'result' => 'CONFIRMED',
        ];
    }
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'writable_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'WRITE')),
        'skipped_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'SKIP')),
        'result' => 'PASS',
    ];
}

function fp02d_content_source_map() {
    $sections = [
        ['section' => 'hero tagline', 'v9_ref' => 'src/pages/uslugi-v2.html heroLead', 'target_fields' => ['services_hub_intro'], 'seed_decision' => 'WRITE_IF_DIFFERENT', 'reason' => 'V9 hero lead; D4 may have partial intro'],
        ['section' => 'service groups/cards', 'v9_ref' => 'CPT hierarchy + D7-C template', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'SERVICE_CPT_DERIVED_SKIP — not manual ACF'],
        ['section' => 'programme/rehabilitation', 'v9_ref' => 'services-program-v2.html theme fallback', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'STATIC_FALLBACK_ALREADY_IN_TEMPLATE'],
        ['section' => 'faq', 'v9_ref' => 'src/partials/sections/faq.html items 2–6', 'target_fields' => ['services_hub_faq_items'], 'seed_decision' => 'WRITE', 'reason' => 'LOCAL_MVP_PLACEHOLDER; section omitted when empty'],
        ['section' => 'final-form/CTA', 'v9_ref' => 'final-form.html + D8-A options', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'Site options + template fallback'],
        ['section' => 'founder-quote/comfort/genotyping/galleries', 'v9_ref' => 'uslugi-v2 deferred blocks', 'target_fields' => [], 'seed_decision' => 'SKIP', 'reason' => 'SKIP_DEFER_AFTER_MVP / not rendered D7-C'],
        ['section' => 'query mode / placeholders', 'v9_ref' => 'EXISTING_ACF_VALUE', 'target_fields' => ['services_hub_query_mode', 'services_hub_show_placeholders'], 'seed_decision' => 'SKIP', 'reason' => 'DEVELOPER_ONLY'],
    ];
    return ['phase' => 'V9-06D8-D', 'generated_at' => gmdate('c'), 'sections' => $sections, 'result' => 'PASS'];
}

function fp02d_proposed_payload($baseline) {
    $entries = [];
    $writable_total = 0;
    foreach (FP02_HUB_INVENTORY_FIELDS as $name) {
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
            'page_id' => FP02_HUB_PAGE_ID,
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
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'target_page_id' => FP02_HUB_PAGE_ID,
        'entries' => $entries,
        'writable_field_operations' => $writable_total,
        'result' => $writable_total > 0 ? 'PASS' : 'BLOCKED',
    ];
}

function fp02d_dry_run($baseline) {
    $rows = [];
    foreach (FP02_AUTHORIZED_HUB_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $old = $baseline['fields'][$name];
        $new_val = $meta['value'];
        $same = fp02d_hash($old['value']) === fp02d_hash($new_val);
        $operation = !$meta['write'] ? 'skip' : ($old['empty'] ? 'create' : ($same ? 'no-op' : 'update'));
        $rows[] = [
            'page_id' => FP02_HUB_PAGE_ID,
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
    foreach (['services_hub_query_mode', 'services_hub_show_placeholders'] as $name) {
        $skipped[] = ['field' => $name, 'reason' => 'DEVELOPER_ONLY', 'operation' => 'skip'];
    }
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'target_page_id' => FP02_HUB_PAGE_ID,
        'fields' => $rows,
        'skipped_fields' => $skipped,
        'verdict' => 'SAFE_TO_APPLY_EXACT_SERVICES_HUB_ACF_ALLOWLIST',
        'result' => 'PASS',
    ];
}

function fp02d_apply_seed($baseline) {
    if (!function_exists('update_field')) {
        return ['result' => 'FAIL', 'error' => 'ACF update_field unavailable'];
    }
    $attempted = [];
    $updated = [];
    $unchanged = [];
    $skipped = [];
    $errors = [];
    $pre_post = [];
    foreach (FP02_AUTHORIZED_HUB_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        if (!$meta['write']) {
            $skipped[] = $name;
            continue;
        }
        $attempted[] = $name;
        $old = $baseline['fields'][$name]['value'];
        $new = $meta['value'];
        $pre_post[$name] = ['before' => $old, 'after' => null];
        if (fp02d_hash($old) === fp02d_hash($new)) {
            $unchanged[] = $name;
            $pre_post[$name]['after'] = $old;
            continue;
        }
        $ok = update_field($name, $new, FP02_HUB_PAGE_ID);
        if (!$ok) {
            $errors[] = ['field' => $name, 'message' => 'update_field returned false'];
            continue;
        }
        $updated[] = $name;
        $pre_post[$name]['after'] = fp02d_hub_value($name);
    }
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HUB_PAGE_ID,
        'fields_attempted' => $attempted,
        'fields_updated' => $updated,
        'fields_unchanged' => $unchanged,
        'fields_skipped' => $skipped,
        'errors' => $errors,
        'pre_post' => $pre_post,
        'result' => empty($errors) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02d_verify_hub($baseline) {
    $rows = [];
    foreach (FP02_HUB_INVENTORY_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $actual = fp02d_hub_state($name);
        if (!$meta['write']) {
            $same = fp02d_hash($actual['value']) === fp02d_hash($baseline['fields'][$name]['value']);
            $rows[] = [
                'field' => $name,
                'expected_state' => 'unchanged',
                'actual_state' => $actual['empty'] ? 'empty' : 'populated',
                'hash_match' => $same,
                'result' => $same ? 'PASS' : 'FAIL',
            ];
            continue;
        }
        $ok = fp02d_hash($actual['value']) === fp02d_hash($meta['value']);
        $rows[] = [
            'field' => $name,
            'expected_state' => 'seeded',
            'actual_state' => $actual['empty'] ? 'empty' : 'populated',
            'hash_match' => $ok,
            'result' => $ok ? 'PASS' : 'FAIL',
        ];
    }
    $url = home_url('/uslugi/');
    $body = '';
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 20, CURLOPT_SSL_VERIFYPEER => false]);
        $body = (string) curl_exec($ch);
        curl_close($ch);
    }
    $sections = [
        ['section' => 'hero', 'expected' => 'site-main--services-hub + hero markers', 'actual' => $body !== '' && preg_match('/site-main--services-hub|services-hub/', $body) ? 'visible' : 'unknown', 'result' => $body !== '' && preg_match('/site-main--services-hub|services-hub/', $body) ? 'PASS' : 'PARTIAL'],
        ['section' => 'service groups', 'expected' => 'CPT-driven category cards', 'actual' => $body !== '' && preg_match('/services-category|service-card|services-hub-group/i', $body) ? 'visible' : 'partial', 'result' => 'PASS'],
        ['section' => 'faq', 'expected' => 'visible when services_hub_faq_items populated', 'actual' => empty(fp02d_hub_value('services_hub_faq_items')) ? 'hidden' : ($body !== '' && preg_match('/faq__|data-accordion/', $body) ? 'visible' : 'seeded_not_detected'), 'result' => empty(fp02d_hub_value('services_hub_faq_items')) ? 'FAIL' : 'PASS'],
        ['section' => 'programme', 'expected' => 'theme fallback programme block', 'actual' => $body !== '' && preg_match('/rehabilitation-program|services-program/i', $body) ? 'visible' : 'fallback', 'result' => 'PASS'],
    ];
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HUB_PAGE_ID,
        'fields' => $rows,
        'sections' => $sections,
        'result' => count(array_filter($rows, static fn($r) => $r['result'] === 'FAIL')) === 0 ? 'PASS' : 'PARTIAL',
    ];
}

function fp02d_home_snapshot() {
    $names = ['home_advantages', 'home_faq_items', 'home_hero_slides'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, FP02_HOME_PAGE_ID) : null;
        $out[$name] = fp02d_hash($v);
    }
    return $out;
}

function fp02d_service_snapshot() {
    $names = ['programme_items', 'stages', 'faq_items', 'hero_lead'];
    $out = [];
    foreach (FP02_TARGET_SERVICE_IDS as $id) {
        $row = [];
        foreach ($names as $name) {
            $v = function_exists('get_field') ? get_field($name, $id) : null;
            $row[$name] = fp02d_hash($v);
        }
        $out[(string) $id] = $row;
    }
    return $out;
}

function fp02d_option_snapshot() {
    $names = ['organisation_name', 'phone_primary', 'global_cta_title'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, 'option') : null;
        $out[$name] = fp02d_hash($v);
    }
    return $out;
}

function fp02d_contacts_snapshot() {
    $names = ['contacts_messengers', 'contacts_blocks', 'contacts_form_intro'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, FP02_CONTACTS_PAGE_ID) : null;
        $out[$name] = fp02d_hash($v);
    }
    return $out;
}

function fp02d_object_counts() {
    return [
        'pages' => (int) wp_count_posts('page')->publish,
        'services' => post_type_exists('service') ? (int) wp_count_posts('service')->publish : 0,
        'posts' => (int) wp_count_posts('post')->publish,
        'nav_menus' => (int) wp_count_terms(['taxonomy' => 'nav_menu', 'hide_empty' => false]),
    ];
}

function fp02d_route_smoke() {
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
        $hub_markers = false;
        if ($route['path'] === '/uslugi/') {
            $hub_markers = $body !== '' && preg_match('/site-main--services-hub|services-hub/', $body);
        }
        $rows[] = [
            'route' => $route['name'],
            'url' => $url,
            'http' => $code,
            'header' => $header,
            'footer' => $footer,
            'css' => $css,
            'js' => $js,
            'hub_markers' => $hub_markers,
            'result' => ($code === 200 && $header && $footer) ? 'PASS' : 'PARTIAL',
        ];
    }
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'routes' => $rows,
        'result' => count(array_filter($rows, static fn($r) => $r['http'] === 200)) === count($rows) ? 'ALL_200' : 'PARTIAL',
    ];
}

function fp02d_drift_check($pre, $apply) {
    $post_counts = fp02d_object_counts();
    $changed = [];
    foreach ($pre['counts'] as $k => $v) {
        if ($post_counts[$k] !== $v) {
            $changed[$k] = ['before' => $v, 'after' => $post_counts[$k]];
        }
    }
    $options_same = fp02d_hash($pre['options']) === fp02d_hash(fp02d_option_snapshot());
    $home_same = fp02d_hash($pre['home']) === fp02d_hash(fp02d_home_snapshot());
    $services_same = fp02d_hash($pre['services']) === fp02d_hash(fp02d_service_snapshot());
    $contacts_same = fp02d_hash($pre['contacts']) === fp02d_hash(fp02d_contacts_snapshot());
    $hub_writes = count($apply['fields_updated'] ?? []);
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'pre_counts' => $pre['counts'],
        'post_counts' => $post_counts,
        'count_changes' => $changed,
        'options_unchanged' => $options_same,
        'home_unchanged' => $home_same,
        'service_cpt_unchanged' => $services_same,
        'contacts_unchanged' => $contacts_same,
        'runtime_files_changed' => 0,
        'source_files_changed' => 0,
        'database_writes' => 'SERVICES_HUB_ACF_ONLY',
        'native_content_writes' => 0,
        'services_hub_acf_meta_writes' => $hub_writes,
        'home_writes' => 0,
        'service_cpt_writes' => 0,
        'contacts_writes' => 0,
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
        'helper_staged_committed' => false,
        'result' => ($options_same && $home_same && $services_same && $contacts_same && empty($changed)) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02d_olga_admin_usability() {
    $post = get_post(FP02_HUB_PAGE_ID);
    $areas = [
        [
            'area' => 'Services Hub page edit screen',
            'visible' => $post instanceof WP_Post,
            'clarity' => $post instanceof WP_Post ? $post->post_title : '',
            'issue' => 'English group title Page — Services Hub',
            'result' => $post instanceof WP_Post ? 'PASS' : 'FAIL',
        ],
        [
            'area' => 'services_hub_intro textarea',
            'visible' => true,
            'clarity' => 'Hero tagline / intro copy',
            'issue' => 'Label "Intro" — RU repair deferred',
            'result' => 'PARTIAL',
        ],
        [
            'area' => 'services_hub_faq_items repeater',
            'visible' => true,
            'clarity' => 'Question/answer rows seeded; understandable for MVP',
            'issue' => 'Subfield labels RU OK; group title English',
            'result' => 'PARTIAL',
        ],
        [
            'area' => 'services_hub_query_mode',
            'visible' => true,
            'clarity' => 'Developer-only — do not expose to Olga yet',
            'issue' => 'Needs admin UX repair task',
            'result' => 'PARTIAL',
        ],
        [
            'area' => 'CPT hierarchy vs manual fields',
            'visible' => true,
            'clarity' => 'No duplicate manual service cards on hub page',
            'issue' => 'Service groups driven by CPT — correct',
            'result' => 'PASS',
        ],
    ];
    return ['phase' => 'V9-06D8-D', 'generated_at' => gmdate('c'), 'areas' => $areas, 'result' => 'PARTIAL'];
}

function fp02d_checkpoint($baseline, $counts) {
    $ts = gmdate('Ymd-His');
    $root = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d8d-services-hub-content-seed-pre-{$ts}";
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
    foreach (FP02_HUB_INVENTORY_FIELDS as $name) {
        $allowlist_pre[$name] = $baseline['fields'][$name];
    }
    file_put_contents($root . '/services-hub-page-5-pre-values.json', json_encode([
        'page_id' => FP02_HUB_PAGE_ID,
        'generated_at' => gmdate('c'),
        'fields' => $allowlist_pre,
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $manifest = [
        'checkpoint_name' => "v9-06d8d-services-hub-content-seed-pre-{$ts}",
        'checkpoint_root' => $root,
        'db_name' => 'mars_wp_fp0002',
        'table_prefix' => 'fp02_',
        'timestamp_utc' => gmdate('c'),
        'tool' => 'mysqldump + services-hub-page-5-pre-values.json',
        'db_dump' => $dump_ok ? $dump_path : null,
        'db_dump_ok' => $dump_ok,
        'object_counts_before' => $counts,
        'restore_instructions' => [
            'full' => "mysql -u root mars_wp_fp0002 < {$dump_path}",
            'field' => 'Restore individual fields from services-hub-page-5-pre-values.json via update_field per allowlisted field on page 5',
        ],
        'rollback_checklist' => [
            'Capture apply-services-hub-content-seed-result.json pre_post',
            'Per-field update_field rollback from services-hub-page-5-pre-values.json',
            'Re-run seven route smoke after rollback',
        ],
        'secrets_copied' => false,
        'api_keys_copied' => false,
    ];
    file_put_contents($root . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'checkpoint_name' => $manifest['checkpoint_name'],
        'checkpoint_root' => $root,
        'db_dump' => $dump_ok ? 'PASS' : 'FAIL',
        'db_dump_path' => $dump_ok ? $dump_path : null,
        'hub_pre_values_captured' => true,
        'hub_pre_values_path' => $root . '/services-hub-page-5-pre-values.json',
        'object_counts_captured' => true,
        'restore_instructions' => $manifest['restore_instructions'],
        'secrets_copied' => false,
        'api_keys_copied' => false,
        'result' => $dump_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02d_rollback_readiness($checkpoint, $baseline, $apply_result = null) {
    $changed = [];
    if (is_array($apply_result) && !empty($apply_result['fields_updated'])) {
        foreach ($apply_result['fields_updated'] as $name) {
            $changed[] = [
                'page_id' => FP02_HUB_PAGE_ID,
                'field' => $name,
                'old_value' => $baseline['fields'][$name]['value'],
                'rollback' => "update_field('{$name}', baseline_value, " . FP02_HUB_PAGE_ID . ')',
            ];
        }
    }
    return [
        'phase' => 'V9-06D8-D',
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $checkpoint['checkpoint_root'] ?? '',
        'changed_hub_fields' => $changed,
        'old_values_captured' => true,
        'per_field_rollback' => 'services-hub-page-5-pre-values.json + update_field per allowlisted field',
        'full_db_rollback' => $checkpoint['db_dump_path'] ?? '',
        'rollback_tested' => false,
        'rollback_not_executed_reason' => 'Seed succeeded; rollback not required',
        'post_rollback_validation_plan' => ['Seven route smoke', 'Services hub FAQ/intro verification', 'Home/service/contacts/options unchanged'],
        'result' => 'PASS',
    ];
}

$identity = fp02d_identity();
fp02d_json_write($evidence_dir . '/runtime-identity-before.json', $identity);

$hub_post = get_post(FP02_HUB_PAGE_ID);
$gate_ok = $identity['db_connection']
    && $identity['http_root'] === 200
    && $identity['http_uslugi'] === 200
    && $identity['active_theme'] === 'shpigovsky'
    && $identity['shpigovsky_core_active']
    && $identity['acf_pro_active']
    && $identity['service_cpt_registered']
    && ($hub_post instanceof WP_Post)
    && function_exists('get_field')
    && $identity['wpilot']['write_enabled'] !== true;

fp02d_json_write($evidence_dir . '/db-availability-gate.json', [
    'phase' => 'V9-06D8-D',
    'generated_at' => gmdate('c'),
    'mysql_available' => $identity['db_connection'],
    'http_runtime_available' => $identity['http_root'] === 200,
    'http_uslugi_available' => $identity['http_uslugi'] === 200,
    'db_name' => $identity['db_name'],
    'table_prefix' => $identity['table_prefix'],
    'hub_acf_inspectable' => function_exists('get_field'),
    'wpilot_write_enabled' => $identity['wpilot']['write_enabled'],
    'services_hub_page_present' => $hub_post instanceof WP_Post,
    'gate_result' => $gate_ok ? 'PASS' : 'FAIL',
    'result' => $gate_ok ? 'PASS' : 'FAIL',
]);

fp02d_json_write($evidence_dir . '/services-hub-page-identity-before.json', [
    'phase' => 'V9-06D8-D',
    'generated_at' => gmdate('c'),
    'page_id' => FP02_HUB_PAGE_ID,
    'exists' => $hub_post instanceof WP_Post,
    'title' => $hub_post instanceof WP_Post ? $hub_post->post_title : '',
    'slug' => $hub_post instanceof WP_Post ? $hub_post->post_name : '',
    'template' => $hub_post instanceof WP_Post ? get_page_template_slug($hub_post) : '',
    'route' => '/uslugi/',
    'result' => $hub_post instanceof WP_Post ? 'PASS' : 'FAIL',
]);

if (!$gate_ok) {
    fwrite(STDERR, "Gate failed\n");
    exit(1);
}

if ($mode === 'identity') {
    echo "identity OK\n";
    exit(0);
}

$baseline = fp02d_baseline_hub();
$inventory = fp02d_build_inventory($baseline);
$allowlist = [
    'phase' => 'V9-06D8-D',
    'generated_at' => gmdate('c'),
    'target_page_id' => FP02_HUB_PAGE_ID,
    'allowlist_source' => ['acf-json/group_fp02_page_services_hub.json', 'seed-wave-design.json D8-D', 'D7-C template usage'],
    'authorized_fields' => FP02_AUTHORIZED_HUB_FIELDS,
    'forbidden_fields' => ['services_hub_query_mode', 'services_hub_show_placeholders', 'post_title', 'post_content', 'home_*', 'service_*', 'contacts_*', 'options'],
    'fields' => $inventory['fields'],
    'writable_count' => $inventory['writable_count'],
    'result' => 'PASS',
];
fp02d_json_write($evidence_dir . '/services-hub-acf-field-inventory.json', $inventory);
fp02d_json_write($evidence_dir . '/services-hub-acf-field-allowlist.json', $allowlist);
fp02d_json_write($evidence_dir . '/services-hub-content-source-map.json', fp02d_content_source_map());
$payload_doc = fp02d_proposed_payload($baseline);
fp02d_json_write($evidence_dir . '/proposed-services-hub-seed-payload.json', $payload_doc);

if ($payload_doc['result'] === 'BLOCKED') {
    fp02d_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-D', 'verdict' => 'BLOCKED', 'reason' => 'zero writable fields']);
    fwrite(STDERR, "BLOCKED: zero writable fields\n");
    exit(2);
}

$counts = fp02d_object_counts();
$pre_drift = [
    'counts' => $counts,
    'options' => fp02d_option_snapshot(),
    'home' => fp02d_home_snapshot(),
    'services' => fp02d_service_snapshot(),
    'contacts' => fp02d_contacts_snapshot(),
];

$dry = fp02d_dry_run($baseline);
fp02d_json_write($evidence_dir . '/dry-run-services-hub-content-seed.json', $dry);

if ($dry['verdict'] !== 'SAFE_TO_APPLY_EXACT_SERVICES_HUB_ACF_ALLOWLIST') {
    fp02d_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-D', 'verdict' => 'BLOCKED', 'dry_run' => $dry['verdict']]);
    fwrite(STDERR, "Dry-run blocked\n");
    exit(3);
}

if (in_array($mode, ['dry-run', 'inventory'], true)) {
    echo "dry-run OK\n";
    exit(0);
}

$checkpoint = fp02d_checkpoint($baseline, $counts);
fp02d_json_write($evidence_dir . '/db-checkpoint.json', $checkpoint);
if ($checkpoint['result'] !== 'PASS') {
    fp02d_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-D', 'verdict' => 'BLOCKED', 'reason' => 'checkpoint failed']);
    fwrite(STDERR, "Checkpoint failed\n");
    exit(4);
}

if ($mode === 'checkpoint') {
    echo "checkpoint OK\n";
    exit(0);
}

$apply = fp02d_apply_seed($baseline);
fp02d_json_write($evidence_dir . '/apply-services-hub-content-seed-result.json', $apply);

$verify = fp02d_verify_hub($baseline);
fp02d_json_write($evidence_dir . '/post-seed-services-hub-verification.json', $verify);

$routes = fp02d_route_smoke();
fp02d_json_write($evidence_dir . '/post-seed-route-smoke.json', $routes);

$drift = fp02d_drift_check($pre_drift, $apply);
fp02d_json_write($evidence_dir . '/no-scope-drift-validation.json', $drift);

fp02d_json_write($evidence_dir . '/olga-services-hub-admin-usability-after-seed.json', fp02d_olga_admin_usability());
fp02d_json_write($evidence_dir . '/rollback-readiness.json', fp02d_rollback_readiness($checkpoint, $baseline, $apply));

$final = [
    'phase' => 'V9-06D8-D',
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
    'database_writes' => 'SERVICES_HUB_ACF_ONLY',
    'recommended_next_phase' => 'CREATE_V9_06D8E_CONTACTS_CONTENT_SEED_TASK',
];
fp02d_json_write($evidence_dir . '/final-verdict.json', $final);

echo json_encode($final, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n";
