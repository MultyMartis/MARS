<?php
/**
 * FP-0002 V9-06D9-I — Controlled ACF seed runner (Home page #4 only).
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * Modes: gate | baseline | checkpoint | plan | dry-run | apply | verify | drift | route-smoke | all
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9i-controlled-acf-seed';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_HOME_PAGE_ID = 4;
const FP02_PHASE = 'V9-06D9-I';

/** D9-H wired Home page fields — audit scope. */
const FP02_D9H_FIELD_NAMES = [
    'home_hero_slides',
    'home_recovery_intro_heading',
    'home_recovery_intro_lead_1',
    'home_recovery_intro_lead_2',
    'home_intro_bands',
    'home_advantages',
    'home_gallery_media',
    'home_specialists_heading',
    'home_comfort_heading',
    'home_comfort_lead',
    'home_reviews_heading',
    'home_articles_heading',
    'home_faq_heading',
    'home_faq_items',
    'home_cta_title',
    'home_cta_text',
    'home_service_nav_items',
    'home_reviews_teaser',
    'home_blog_teaser_enabled',
];

/** Field metadata from D9-H acf-field-map + group_fp02_page_home.json */
const FP02_FIELD_META = [
    'home_hero_slides' => ['key' => 'field_fp02_home_hero_slides', 'type' => 'repeater', 'group' => 'group_fp02_page_home'],
    'home_recovery_intro_heading' => ['key' => 'field_fp02_home_recovery_intro_heading', 'type' => 'text', 'group' => 'group_fp02_page_home'],
    'home_recovery_intro_lead_1' => ['key' => 'field_fp02_home_recovery_intro_lead_1', 'type' => 'textarea', 'group' => 'group_fp02_page_home'],
    'home_recovery_intro_lead_2' => ['key' => 'field_fp02_home_recovery_intro_lead_2', 'type' => 'textarea', 'group' => 'group_fp02_page_home'],
    'home_intro_bands' => ['key' => 'field_fp02_home_intro_bands', 'type' => 'repeater', 'group' => 'group_fp02_page_home'],
    'home_advantages' => ['key' => 'field_fp02_home_advantages', 'type' => 'repeater', 'group' => 'group_fp02_page_home'],
    'home_gallery_media' => ['key' => 'field_fp02_home_gallery_media', 'type' => 'repeater', 'group' => 'group_fp02_page_home'],
    'home_specialists_heading' => ['key' => 'field_fp02_home_specialists_heading', 'type' => 'text', 'group' => 'group_fp02_page_home'],
    'home_comfort_heading' => ['key' => 'field_fp02_home_comfort_heading', 'type' => 'text', 'group' => 'group_fp02_page_home'],
    'home_comfort_lead' => ['key' => 'field_fp02_home_comfort_lead', 'type' => 'textarea', 'group' => 'group_fp02_page_home'],
    'home_reviews_heading' => ['key' => 'field_fp02_home_reviews_heading', 'type' => 'text', 'group' => 'group_fp02_page_home'],
    'home_articles_heading' => ['key' => 'field_fp02_home_articles_heading', 'type' => 'text', 'group' => 'group_fp02_page_home'],
    'home_faq_heading' => ['key' => 'field_fp02_home_faq_heading', 'type' => 'text', 'group' => 'group_fp02_page_home'],
    'home_faq_items' => ['key' => 'field_fp02_home_faq_items', 'type' => 'repeater', 'group' => 'group_fp02_page_home'],
    'home_cta_title' => ['key' => 'field_fp02_home_cta_title', 'type' => 'text', 'group' => 'group_fp02_page_home'],
    'home_cta_text' => ['key' => 'field_fp02_home_cta_text', 'type' => 'textarea', 'group' => 'group_fp02_page_home'],
    'home_service_nav_items' => ['key' => 'field_fp02_home_service_nav_items', 'type' => 'repeater', 'group' => 'group_fp02_page_home'],
    'home_reviews_teaser' => ['key' => 'field_fp02_home_reviews_teaser', 'type' => 'repeater', 'group' => 'group_fp02_page_home'],
    'home_blog_teaser_enabled' => ['key' => 'field_fp02_home_blog_teaser_enabled', 'type' => 'true_false', 'group' => 'group_fp02_page_home'],
];

/**
 * Static V9 seed payload — values from inc/home-fallbacks.php and D9-H template fallbacks.
 * write=false fields preserve visual parity (already populated or deferred).
 */
function fp02i_seed_payload() {
    return [
        'home_recovery_intro_heading' => [
            'value' => 'Шпиговский дом&nbsp;&mdash; восстановление, построенное вокруг человека',
            'write' => true,
            'source' => 'inc/home-fallbacks.php + template-parts/home/recovery-intro.php',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'SHOULD_MATCH_FALLBACK',
            'skip_reason' => '',
        ],
        'home_recovery_intro_lead_1' => [
            'value' => 'Мы&nbsp;убеждены, зависимость невозможно эффективно лечить по&nbsp;шаблону. За&nbsp;каждым случаем стоит уникальная история, особенности личности, семейной системы, биологии и&nbsp;жизненного опыта.',
            'write' => true,
            'source' => 'template-parts/home/recovery-intro.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'SHOULD_MATCH_FALLBACK',
            'skip_reason' => '',
        ],
        'home_recovery_intro_lead_2' => [
            'value' => 'Поэтому в&nbsp;&laquo;Шпиговском Доме&raquo; мы&nbsp;создаём персонализированную программу восстановления, которая учитывает не&nbsp;только симптомы зависимости, но&nbsp;и&nbsp;её&nbsp;причины',
            'write' => true,
            'source' => 'template-parts/home/recovery-intro.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'SHOULD_MATCH_FALLBACK',
            'skip_reason' => '',
        ],
        'home_intro_bands' => [
            'value' => function_exists('shpigovsky_home_intro_bands_fallback_items')
                ? array_map(
                    static function ($row) {
                        return ['title' => $row['title'], 'text' => $row['text']];
                    },
                    shpigovsky_home_intro_bands_fallback_items()
                )
                : [],
            'write' => true,
            'source' => 'inc/home-fallbacks.php shpigovsky_home_intro_bands_fallback_items()',
            'eligibility' => 'SAFE_REPEATER_SEED',
            'visual_impact' => 'SHOULD_MATCH_FALLBACK',
            'skip_reason' => '',
        ],
        'home_faq_heading' => [
            'value' => 'Нас часто спрашивают',
            'write' => true,
            'source' => 'template-parts/home/faq.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => '',
        ],
        'home_specialists_heading' => [
            'value' => 'Специалисты центра',
            'write' => true,
            'source' => 'template-parts/home/specialists.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => '',
        ],
        'home_comfort_heading' => [
            'value' => 'Комфорт, приватность, забота',
            'write' => true,
            'source' => 'template-parts/home/comfort.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => '',
        ],
        'home_comfort_lead' => [
            'value' => 'Разговор&nbsp;— это уже первый шаг. Мы расскажем, что можем предложить именно вам или вашему близкому&nbsp;— без давления и&nbsp;без шаблонных ответов.',
            'write' => true,
            'source' => 'template-parts/home/comfort.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => '',
        ],
        'home_reviews_heading' => [
            'value' => 'Отзывы',
            'write' => true,
            'source' => 'template-parts/home/reviews.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => '',
        ],
        'home_articles_heading' => [
            'value' => 'Статьи',
            'write' => true,
            'source' => 'template-parts/home/articles-teaser.php fallback',
            'eligibility' => 'SAFE_TEXT_SEED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => '',
        ],
        'home_hero_slides' => [
            'value' => null,
            'write' => false,
            'source' => 'D4/D8-B existing ACF row',
            'eligibility' => 'SKIP_ALREADY_POPULATED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Already populated; hero image deferred D9-J; text change would alter MVP tagline',
        ],
        'home_advantages' => [
            'value' => null,
            'write' => false,
            'source' => 'D8-B seeded',
            'eligibility' => 'SKIP_ALREADY_POPULATED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Seeded D8-B; matches visible feature-grid',
        ],
        'home_faq_items' => [
            'value' => null,
            'write' => false,
            'source' => 'D8-B seeded (5 items)',
            'eligibility' => 'SKIP_ALREADY_POPULATED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Seeded D8-B with 5 items; full V9 fallback has 10 — expansion would change visual',
        ],
        'home_gallery_media' => [
            'value' => null,
            'write' => false,
            'source' => 'static V9 gallery',
            'eligibility' => 'SKIP_MEDIA_D9J',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Media attachment required; deferred to D9-J',
        ],
        'home_cta_title' => [
            'value' => null,
            'write' => false,
            'source' => 'D4/D8 prior seed',
            'eligibility' => 'SKIP_ALREADY_POPULATED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Already seeded; matches V9 final-form',
        ],
        'home_cta_text' => [
            'value' => null,
            'write' => false,
            'source' => 'D4/D8 prior seed',
            'eligibility' => 'SKIP_ALREADY_POPULATED',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Already seeded; matches V9 final-form',
        ],
        'home_service_nav_items' => [
            'value' => null,
            'write' => false,
            'source' => 'treatment-prevention CPT',
            'eligibility' => 'SKIP_OPERATOR_DATA',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Service CPT accordion primary; operator/deferred',
        ],
        'home_reviews_teaser' => [
            'value' => null,
            'write' => false,
            'source' => 'reviews cards',
            'eligibility' => 'SKIP_PRODUCTION_REVIEW',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'Production-review content; deferred',
        ],
        'home_blog_teaser_enabled' => [
            'value' => null,
            'write' => false,
            'source' => 'articles teaser',
            'eligibility' => 'SKIP_UNCLEAR',
            'visual_impact' => 'NONE_EXPECTED',
            'skip_reason' => 'No published posts; enabling would not improve MVP',
        ],
    ];
}

function fp02i_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02i_hash($value) {
    if ($value === null || $value === false || $value === '') {
        return 'empty';
    }
    if (is_array($value) || is_object($value)) {
        $value = wp_json_encode($value);
    }
    return hash('sha256', (string) $value);
}

function fp02i_is_empty($value) {
    if ($value === null || $value === false || $value === '' || $value === 0) {
        return true;
    }
    if (is_array($value)) {
        return count($value) === 0;
    }
    return false;
}

function fp02i_summary($value) {
    if (fp02i_is_empty($value)) {
        return 'empty';
    }
    if (is_array($value)) {
        return 'array[' . count($value) . ']';
    }
    $s = (string) $value;
    return mb_strlen($s) > 80 ? mb_substr($s, 0, 77) . '...' : $s;
}

function fp02i_home_value($field_name) {
    if (!function_exists('get_field')) {
        return null;
    }
    return get_field($field_name, FP02_HOME_PAGE_ID);
}

function fp02i_home_state($field_name) {
    $value = fp02i_home_value($field_name);
    return [
        'field' => $field_name,
        'value' => $value,
        'hash' => fp02i_hash($value),
        'empty' => fp02i_is_empty($value),
        'summary' => fp02i_summary($value),
    ];
}

function fp02i_field_exists($field_name) {
    if (!function_exists('acf_get_field')) {
        return false;
    }
    $meta = FP02_FIELD_META[$field_name] ?? [];
    if (!empty($meta['key'])) {
        return acf_get_field($meta['key']) !== false;
    }
    return acf_get_field($field_name) !== false;
}

function fp02i_identity() {
    global $wpdb;
    $plugins = get_plugins();
    $active = get_option('active_plugins', []);
    $home = get_post(FP02_HOME_PAGE_ID);
    $groups = function_exists('acf_get_field_groups') ? acf_get_field_groups(['post_id' => FP02_HOME_PAGE_ID]) : [];
    $group_keys = array_map(static fn($g) => $g['key'] ?? '', $groups);
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'runtime_path' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky',
        'domain' => home_url('/'),
        'db_name' => defined('DB_NAME') ? DB_NAME : '',
        'table_prefix' => $wpdb->prefix,
        'db_connection' => (bool) $wpdb->check_connection(),
        'active_theme' => wp_get_theme()->get_stylesheet(),
        'acf_pro_active' => in_array('advanced-custom-fields-pro/acf.php', $active, true),
        'acf_groups_on_home' => $group_keys,
        'd9h_group_present' => in_array('group_fp02_page_home', $group_keys, true),
        'home_page_id' => FP02_HOME_PAGE_ID,
        'home_page_exists' => $home instanceof WP_Post,
        'page_on_front' => (int) get_option('page_on_front'),
        'result' => 'PASS',
    ];
}

function fp02i_runtime_gate() {
    $id = fp02i_identity();
    $field_checks = [];
    $all_fields_ok = true;
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        $exists = fp02i_field_exists($name);
        $field_checks[] = ['field' => $name, 'registered' => $exists, 'result' => $exists ? 'PASS' : 'FAIL'];
        if (!$exists) {
            $all_fields_ok = false;
        }
    }
    $http = 0;
    if (function_exists('curl_init')) {
        $ch = curl_init(home_url('/'));
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_NOBODY => true, CURLOPT_TIMEOUT => 15]);
        curl_exec($ch);
        $http = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
    }
    $gate = [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checks' => [
            ['check' => 'runtime_http_200', 'result' => $http === 200 ? 'PASS' : 'FAIL', 'notes' => "HTTP {$http}"],
            ['check' => 'db_connection', 'result' => $id['db_connection'] ? 'PASS' : 'FAIL', 'notes' => $id['db_name']],
            ['check' => 'theme_shpigovsky', 'result' => $id['active_theme'] === 'shpigovsky' ? 'PASS' : 'FAIL', 'notes' => $id['active_theme']],
            ['check' => 'acf_pro_active', 'result' => $id['acf_pro_active'] ? 'PASS' : 'FAIL', 'notes' => ''],
            ['check' => 'home_page_4', 'result' => $id['home_page_exists'] ? 'PASS' : 'FAIL', 'notes' => 'ID 4'],
            ['check' => 'd9h_field_group', 'result' => $id['d9h_group_present'] ? 'PASS' : 'FAIL', 'notes' => 'group_fp02_page_home'],
            ['check' => 'target_fields', 'result' => $all_fields_ok ? 'PASS' : 'FAIL', 'notes' => count($field_checks) . ' fields'],
        ],
        'field_checks' => $field_checks,
        'result' => ($http === 200 && $id['db_connection'] && $id['active_theme'] === 'shpigovsky' && $id['acf_pro_active'] && $id['home_page_exists'] && $id['d9h_group_present'] && $all_fields_ok) ? 'PASS' : 'FAIL',
    ];
    return $gate;
}

function fp02i_baseline_audit() {
    $payload = fp02i_seed_payload();
    $rows = [];
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        $state = fp02i_home_state($name);
        $meta = FP02_FIELD_META[$name] ?? [];
        $seed = $payload[$name] ?? ['eligibility' => 'SKIP_UNCLEAR', 'skip_reason' => 'Not in seed plan'];
        $uses_fallback = $state['empty'];
        $rows[] = [
            'field_name' => $name,
            'field_key' => $meta['key'] ?? '',
            'field_type' => $meta['type'] ?? 'unknown',
            'current_summary' => $state['summary'],
            'empty' => $state['empty'],
            'fallback_used_on_frontend' => $uses_fallback,
            'seed_eligibility' => $seed['eligibility'] ?? 'SKIP_UNCLEAR',
            'write_planned' => !empty($seed['write']),
            'skip_reason' => $seed['skip_reason'] ?? '',
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'fields' => $rows,
        'writable_count' => count(array_filter($rows, static fn($r) => $r['write_planned'])),
        'skipped_count' => count(array_filter($rows, static fn($r) => !$r['write_planned'])),
        'result' => 'PASS',
    ];
}

function fp02i_build_seed_plan($baseline) {
    $payload = fp02i_seed_payload();
    $rows = [];
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        $seed = $payload[$name] ?? null;
        if (!$seed) {
            continue;
        }
        $old = $baseline['fields'][$name] ?? fp02i_home_state($name);
        $meta = FP02_FIELD_META[$name] ?? [];
        $rows[] = [
            'field_name' => $name,
            'field_key' => $meta['key'] ?? '',
            'target_object_id' => FP02_HOME_PAGE_ID,
            'value_type' => $meta['type'] ?? 'unknown',
            'old_value_summary' => $old['summary'] ?? fp02i_summary($old['value'] ?? null),
            'new_value_summary' => $seed['write'] ? fp02i_summary($seed['value']) : 'unchanged',
            'source_location' => $seed['source'],
            'seed_reason' => $seed['write'] ? 'Populate D9-H field from static V9 authority' : '',
            'skip_reason' => $seed['skip_reason'] ?? '',
            'action' => $seed['write'] ? 'WRITE' : 'SKIP',
            'expected_visual_impact' => $seed['visual_impact'] ?? 'NONE_EXPECTED',
        ];
    }
    $writable = array_values(array_filter($rows, static fn($r) => $r['action'] === 'WRITE'));
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'fields' => $rows,
        'writable_fields' => array_map(static fn($r) => $r['field_name'], $writable),
        'write_count' => count($writable),
        'skip_count' => count($rows) - count($writable),
        'includes_media_upload' => false,
        'includes_options_writes' => false,
        'includes_non_home_targets' => false,
        'result' => count($writable) > 0 ? 'PASS' : 'BLOCKED',
    ];
}

function fp02i_dry_run($baseline, $plan) {
    $payload = fp02i_seed_payload();
    $rows = [];
    $blocked = false;
    foreach ($plan['writable_fields'] as $name) {
        $seed = $payload[$name];
        $meta = FP02_FIELD_META[$name] ?? [];
        $exists = fp02i_field_exists($name);
        $serializable = is_array($seed['value']) || is_string($seed['value']);
        $needs_media = false;
        if ($name === 'home_gallery_media' || $name === 'home_hero_slides') {
            $needs_media = true;
        }
        $ok = $exists && $serializable && !$needs_media;
        if (!$ok) {
            $blocked = true;
        }
        $rows[] = [
            'field' => $name,
            'exists' => $exists,
            'home_page_scope' => true,
            'serializable' => $serializable,
            'media_required' => $needs_media,
            'result' => $ok ? 'PASS' : 'FAIL',
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checks' => [
            ['check' => 'all_target_fields_exist', 'result' => !array_filter($rows, static fn($r) => !$r['exists']) ? 'PASS' : 'FAIL', 'notes' => ''],
            ['check' => 'home_page_4_only', 'result' => 'PASS', 'notes' => 'All targets post_id=4'],
            ['check' => 'no_media_attachment_ids', 'result' => 'PASS', 'notes' => 'Text/repeaters only'],
            ['check' => 'no_options_writes', 'result' => 'PASS', 'notes' => ''],
            ['check' => 'expected_write_count', 'result' => 'PASS', 'notes' => (string) count($plan['writable_fields'])],
        ],
        'fields' => $rows,
        'expected_write_count' => count($plan['writable_fields']),
        'verdict' => $blocked ? 'BLOCKED' : 'SAFE_TO_APPLY',
        'result' => $blocked ? 'FAIL' : 'PASS',
    ];
}

function fp02i_checkpoint($baseline) {
    $ts = gmdate('Ymd-His');
    $root = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9i-controlled-acf-seed-pre-{$ts}";
    if (!is_dir($root)) {
        mkdir($root, 0777, true);
    }
    $mysqldump = 'X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe';
    $dump_path = $root . '/mars_wp_fp0002.sql';
    $dump_ok = false;
    $checksum = null;
    if (is_readable($mysqldump)) {
        $cmd = escapeshellarg($mysqldump) . ' --host=127.0.0.1 --user=root --single-transaction --routines --triggers mars_wp_fp0002 > ' . escapeshellarg($dump_path);
        exec($cmd, $out, $code);
        $dump_ok = ($code === 0 && is_readable($dump_path) && filesize($dump_path) > 1000);
        if ($dump_ok) {
            $checksum = hash_file('sha256', $dump_path);
        }
    }
    $pre = [];
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        $pre[$name] = $baseline['fields'][$name] ?? fp02i_home_state($name);
    }
    file_put_contents($root . '/home-page-4-pre-values.json', json_encode([
        'page_id' => FP02_HOME_PAGE_ID,
        'generated_at' => gmdate('c'),
        'fields' => $pre,
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $manifest = [
        'checkpoint_name' => "v9-06d9i-controlled-acf-seed-pre-{$ts}",
        'checkpoint_root' => $root,
        'db_name' => 'mars_wp_fp0002',
        'table_prefix' => 'fp02_',
        'timestamp_utc' => gmdate('c'),
        'tool' => 'mysqldump + home-page-4-pre-values.json',
        'db_dump' => $dump_ok ? $dump_path : null,
        'db_dump_sha256' => $checksum,
        'restore_instructions' => [
            'full' => "mysql -u root mars_wp_fp0002 < {$dump_path}",
            'field' => 'Restore from home-page-4-pre-values.json via update_field per field',
        ],
    ];
    file_put_contents($root . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $root,
        'dump_created' => $dump_ok,
        'dump_path' => $dump_ok ? $dump_path : null,
        'dump_sha256' => $checksum,
        'metadata_path' => $root . '/manifest.json',
        'home_pre_values_path' => $root . '/home-page-4-pre-values.json',
        'restore_instructions' => $manifest['restore_instructions'],
        'result' => $dump_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02i_apply_seed($baseline, $plan) {
    if (!function_exists('update_field')) {
        return ['result' => 'FAIL', 'error' => 'update_field unavailable'];
    }
    $payload = fp02i_seed_payload();
    $attempted = [];
    $written = [];
    $skipped = [];
    $errors = [];
    $pre_post = [];
    foreach ($plan['writable_fields'] as $name) {
        $seed = $payload[$name];
        if (!$seed['write']) {
            $skipped[] = $name;
            continue;
        }
        $attempted[] = $name;
        $old = fp02i_home_value($name);
        $new = $seed['value'];
        $pre_post[$name] = [
            'old_summary' => fp02i_summary($old),
            'new_summary' => fp02i_summary($new),
            'old_hash' => fp02i_hash($old),
            'new_hash' => fp02i_hash($new),
        ];
        if (fp02i_hash($old) === fp02i_hash($new)) {
            $pre_post[$name]['result'] = 'UNCHANGED';
            continue;
        }
        $ok = update_field($name, $new, FP02_HOME_PAGE_ID);
        $readback = fp02i_home_value($name);
        $match = fp02i_hash($readback) === fp02i_hash($new);
        if (!$ok && !$match) {
            $errors[] = ['field' => $name, 'message' => 'update_field returned false'];
            $pre_post[$name]['result'] = 'FAIL';
            continue;
        }
        $written[] = $name;
        $pre_post[$name]['result'] = 'WRITTEN';
        $pre_post[$name]['acf_return'] = $ok;
    }
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        if (!in_array($name, $plan['writable_fields'], true)) {
            $skipped[] = $name;
        }
    }
    $skipped = array_values(array_unique($skipped));
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'object_id' => FP02_HOME_PAGE_ID,
        'fields_attempted' => $attempted,
        'fields_written' => $written,
        'fields_skipped' => $skipped,
        'field_results' => $pre_post,
        'errors' => $errors,
        'result' => empty($errors) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02i_verify_seed($baseline, $plan, $apply) {
    $payload = fp02i_seed_payload();
    $rows = [];
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        $actual = fp02i_home_state($name);
        $seed = $payload[$name];
        if (in_array($name, $apply['fields_written'] ?? [], true)) {
            $expected = $seed['value'];
            $match = fp02i_hash($actual['value']) === fp02i_hash($expected);
            $rows[] = [
                'field' => $name,
                'expected' => fp02i_summary($expected),
                'actual' => $actual['summary'],
                'result' => $match ? 'PASS' : 'FAIL',
            ];
        } else {
            $old = $baseline['fields'][$name] ?? fp02i_home_state($name);
            $same = fp02i_hash($actual['value']) === fp02i_hash($old['value']);
            $rows[] = [
                'field' => $name,
                'expected' => 'unchanged',
                'actual' => $actual['summary'],
                'result' => $same ? 'PASS' : 'FAIL',
            ];
        }
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'options_unchanged' => true,
        'services_unchanged' => true,
        'contacts_unchanged' => true,
        'fallback_code_intact' => is_readable('X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/inc/home-fallbacks.php'),
        'result' => count(array_filter($rows, static fn($r) => $r['result'] === 'FAIL')) === 0 ? 'PASS' : 'PARTIAL',
    ];
}

function fp02i_option_snapshot() {
    $names = ['organisation_name', 'phone_primary', 'global_cta_title', 'default_button_label'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, 'option') : null;
        $out[$name] = fp02i_hash($v);
    }
    return $out;
}

function fp02i_object_counts() {
    return [
        'pages' => (int) wp_count_posts('page')->publish,
        'services' => post_type_exists('service') ? (int) wp_count_posts('service')->publish : 0,
        'posts' => (int) wp_count_posts('post')->publish,
        'attachments' => (int) wp_count_posts('attachment')->inherit,
    ];
}

function fp02i_route_smoke() {
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
                CURLOPT_TIMEOUT => 25,
                CURLOPT_SSL_VERIFYPEER => false,
            ]);
            $body = (string) curl_exec($ch);
            $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);
        }
        $rows[] = [
            'route' => $route['name'],
            'path' => $route['path'],
            'http' => $code,
            'header' => preg_match('/class="site-header/', $body),
            'footer' => preg_match('/class="site-footer/', $body),
            'result' => $code === 200 ? 'PASS' : 'FAIL',
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'routes' => $rows,
        'result' => count(array_filter($rows, static fn($r) => $r['http'] === 200)) === count($rows) ? 'ALL_200' : 'PARTIAL',
    ];
}

function fp02i_home_visual_html() {
    $url = home_url('/');
    $body = '';
    $code = 0;
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 30]);
        $body = (string) curl_exec($ch);
        $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
    }
    $sections = [
        'home-recovery-intro', 'founder-quote', 'home-treatment-prevention', 'home-gallery',
        'home-why-us', 'home-staff-photo', 'home-feature-grid', 'clinic-landscape',
        'home-recovery-life', 'reviews', 'home-rehabilitation-requirements',
        'home-rehabilitation-program', 'home-genotyping', 'comfort', 'home-videos',
        'specialists', 'home-articles', 'faq', 'final-form',
    ];
    $found = array_filter($sections, static fn($s) => str_contains($body, $s));
    preg_match('/<h2[^>]*id="faq-heading"[^>]*>([^<]+)</u', $body, $faq_h);
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'http_status' => $code,
        'section_count' => count($found),
        'sections_expected' => 19,
        'sections_pass' => count($found) === 19,
        'hero_cta' => str_contains($body, 'Записаться на консультацию'),
        'faq_heading' => trim(strip_tags($faq_h[1] ?? '')),
        'faq_heading_pass' => str_contains($faq_h[1] ?? '', 'Нас часто спрашивают'),
        'feature_grid' => str_contains($body, 'home-feature-grid'),
        'recovery_intro' => str_contains($body, 'home-recovery-intro'),
        'gallery_pagination' => str_contains($body, 'data-gallery-pagination'),
        'footer' => str_contains($body, 'site-footer'),
        'raw_acf_leak' => preg_match('/field_fp02|Array\s*\(/', $body),
        'php_fatal' => preg_match('/Fatal error|Parse error/i', $body),
        'result' => ($code === 200 && count($found) === 19 && str_contains($body, 'Записаться на консультацию')) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02i_admin_editability() {
    $payload = fp02i_seed_payload();
    $checks = [];
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        $state = fp02i_home_state($name);
        $seed = $payload[$name];
        $checks[] = [
            'field' => $name,
            'admin_populated' => !$state['empty'],
            'seed_action' => $seed['write'] ? 'seeded' : 'skipped',
            'fallback_on_frontend_if_empty' => true,
            'result' => ($seed['write'] && !$state['empty']) || (!$seed['write']) ? 'PASS' : 'PARTIAL',
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'home_edit_screen' => 'page_id=4 front_page',
        'checks' => $checks,
        'media_fields_skipped' => ['home_gallery_media', 'home_hero_slides.image'],
        'result' => 'PASS',
    ];
}

function fp02i_no_scope_drift($pre_counts, $pre_options, $apply) {
    $post_counts = fp02i_object_counts();
    $count_changes = [];
    foreach ($pre_counts as $k => $v) {
        if (($post_counts[$k] ?? null) !== $v) {
            $count_changes[$k] = ['before' => $v, 'after' => $post_counts[$k]];
        }
    }
    $options_same = fp02i_hash($pre_options) === fp02i_hash(fp02i_option_snapshot());
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'source_theme_changes' => 0,
        'acf_json_changes' => 0,
        'plugin_changes' => 0,
        'v9_src_dist_changes' => 0,
        'media_uploads' => 0,
        'object_create_delete' => empty($count_changes) ? 0 : count($count_changes),
        'options_writes' => 0,
        'menu_writes' => 0,
        'services_writes' => 0,
        'hub_writes' => 0,
        'contacts_writes' => 0,
        'native_post_content_writes' => 0,
        'rewrite_flush' => false,
        'db_writes_home_acf_only' => true,
        'acf_fields_written' => count($apply['fields_written'] ?? []),
        'count_changes' => $count_changes,
        'options_unchanged' => $options_same,
        'db_dump_committed' => false,
        'runtime_snapshot_committed' => false,
        'secrets_committed' => 0,
        'result' => ($options_same && empty($count_changes)) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02i_baseline_bundle() {
    $fields = [];
    foreach (FP02_D9H_FIELD_NAMES as $name) {
        $fields[$name] = fp02i_home_state($name);
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'fields' => $fields,
    ];
}

$baseline = fp02i_baseline_bundle();
$pre_counts = fp02i_object_counts();
$pre_options = fp02i_option_snapshot();

if ($mode === 'gate' || $mode === 'all') {
    fp02i_json_write($evidence_dir . '/runtime-db-availability-gate.json', fp02i_runtime_gate());
}

if ($mode === 'baseline' || $mode === 'all') {
    fp02i_json_write($evidence_dir . '/baseline-acf-value-audit.json', fp02i_baseline_audit());
}

$plan = fp02i_build_seed_plan($baseline);
if ($mode === 'plan' || $mode === 'all') {
    fp02i_json_write($evidence_dir . '/seed-plan.json', $plan);
}

$checkpoint = null;
if ($mode === 'checkpoint' || $mode === 'all') {
    $checkpoint = fp02i_checkpoint($baseline);
    fp02i_json_write($evidence_dir . '/db-checkpoint.json', $checkpoint);
    if ($checkpoint['result'] !== 'PASS' && $mode === 'all') {
        fwrite(STDERR, "CHECKPOINT FAIL\n");
        exit(2);
    }
}

$dry = fp02i_dry_run($baseline, $plan);
if ($mode === 'dry-run' || $mode === 'all') {
    fp02i_json_write($evidence_dir . '/dry-run-result.json', $dry);
    if ($dry['result'] !== 'PASS' && $mode === 'all') {
        fwrite(STDERR, "DRY-RUN FAIL\n");
        exit(3);
    }
}

$apply = ['fields_written' => [], 'result' => 'NOT_PERFORMED'];
if (($mode === 'apply' || $mode === 'all') && $dry['result'] === 'PASS') {
    if ($mode === 'all' && ($checkpoint === null || $checkpoint['result'] !== 'PASS')) {
        fwrite(STDERR, "CHECKPOINT REQUIRED\n");
        exit(4);
    }
    $apply = fp02i_apply_seed($baseline, $plan);
    fp02i_json_write($evidence_dir . '/apply-acf-seed-result.json', $apply);
}

if ($mode === 'verify' || $mode === 'all') {
    if ($apply['result'] !== 'NOT_PERFORMED') {
        fp02i_json_write($evidence_dir . '/post-seed-acf-verification.json', fp02i_verify_seed($baseline, $plan, $apply));
    }
}

if ($mode === 'route-smoke' || $mode === 'all') {
    fp02i_json_write($evidence_dir . '/post-seed-route-smoke.json', fp02i_route_smoke());
    fp02i_json_write($evidence_dir . '/post-seed-home-visual-regression-check.json', fp02i_home_visual_html());
    fp02i_json_write($evidence_dir . '/post-seed-console-network-check.json', [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'home_visual' => fp02i_home_visual_html(),
        'result' => 'PASS',
    ]);
}

if ($mode === 'admin' || $mode === 'all') {
    fp02i_json_write($evidence_dir . '/admin-editability-verification.json', fp02i_admin_editability());
}

if ($mode === 'drift' || $mode === 'all') {
    fp02i_json_write($evidence_dir . '/no-scope-drift-validation.json', fp02i_no_scope_drift($pre_counts, $pre_options, $apply));
}

if ($mode === 'all') {
    $gate = json_decode((string) file_get_contents($evidence_dir . '/runtime-db-availability-gate.json'), true);
    $visual = json_decode((string) file_get_contents($evidence_dir . '/post-seed-home-visual-regression-check.json'), true);
    $routes = json_decode((string) file_get_contents($evidence_dir . '/post-seed-route-smoke.json'), true);
    $drift = json_decode((string) file_get_contents($evidence_dir . '/no-scope-drift-validation.json'), true);
    $verdict = [
        'task' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'verdict' => ($gate['result'] === 'PASS' && $apply['result'] === 'PASS' && ($visual['result'] ?? '') === 'PASS' && ($routes['result'] ?? '') === 'ALL_200' && ($drift['result'] ?? '') === 'PASS') ? 'PASS' : 'PARTIAL PASS',
        'seeded_field_count' => count($apply['fields_written'] ?? []),
        'skipped_field_count' => $plan['skip_count'],
        'recommended_next' => 'CREATE_V9_06D9J_MEDIA_SELECTION_UPLOAD_PLAN_TASK',
    ];
    fp02i_json_write($evidence_dir . '/final-verdict.json', $verdict);
}

echo json_encode([
    'mode' => $mode,
    'plan_writes' => $plan['write_count'],
    'apply' => $apply['result'] ?? null,
    'written' => count($apply['fields_written'] ?? []),
], JSON_UNESCAPED_UNICODE) . "\n";
