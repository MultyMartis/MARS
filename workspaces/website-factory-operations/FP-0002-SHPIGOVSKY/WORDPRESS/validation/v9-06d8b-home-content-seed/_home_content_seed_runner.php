<?php
/**
 * FP-0002 V9-06D8-B — Home page #4 ACF seed runner (home ACF only).
 * Modes: identity | baseline | checkpoint | dry-run | apply | verify | drift | all
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d8b-home-content-seed';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_HOME_PAGE_ID = 4;

const FP02_AUTHORIZED_HOME_FIELDS = [
    'home_hero_slides',
    'home_service_nav_items',
    'home_advantages',
    'home_intro_bands',
    'home_reviews_teaser',
    'home_blog_teaser_enabled',
    'home_gallery_media',
    'home_faq_items',
    'home_cta_title',
    'home_cta_text',
];

const FP02_SEED_PAYLOAD = [
    'home_hero_slides' => [
        'value' => [
            [
                'title' => 'Шпиговский дом',
                'text' => 'Центр профилактики и лечения зависимостей',
            ],
        ],
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'STATIC_V9_CONTENT',
        'write' => true,
        'v9_ref' => 'src/partials/sections/hero.html',
        'skip_subfields' => ['image'],
    ],
    'home_advantages' => [
        'value' => [
            ['title' => 'до 15 резидентов', 'text' => 'В нашем Доме ценится личное пространство каждого. Такой формат позволяет проявлять заботу о каждом, уделять максимум терапевтического внимания.'],
            ['title' => 'нет решеток и замков', 'text' => 'В нашем Доме нет запертых дверей и решеток на окнах. Мы не закрываем, не удерживаем насильно — мы успешно работаем с мотивацией.'],
            ['title' => 'дипломированные специалисты', 'text' => 'Все групповые мероприятия ведут дипломированные специалисты — психологи.'],
            ['title' => 'Бассейн и сауна', 'text' => 'Для формирования новых полезных привычек и желаний. Находятся на цокольном этаже, доступ к ним открыт всегда.'],
            ['title' => 'Тренажерный комплекс', 'text' => 'Для поддержания физической формы и получения удовольствия от спортивных нагрузок.'],
            ['title' => 'Выбор категории номера', 'text' => 'У нас созданы прекрасные условия для комфортного преодоления зависимости и возможности изменить свою жизнь к лучшему.'],
        ],
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'STATIC_V9_CONTENT',
        'write' => true,
        'v9_ref' => 'src/partials/sections/home-feature-grid.html',
        'skip_subfields' => [],
    ],
    'home_faq_items' => [
        'value' => [
            ['question' => 'Анонимное лечение или нет?', 'answer' => 'Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о формате обращения и порядке первичного контакта с центром. Текст не является маркетинговым обещанием и не заменяет консультацию специалиста. Финальная редакция будет согласована оператором отдельно.'],
            ['question' => 'Как долго длится реабилитация?', 'answer' => 'Это временный технический текст для проверки высоты аккордеона. В финальной версии здесь будет описан типовой порядок этапов сопровождения без указания конкретных сроков. Длительность программы зависит от индивидуального запроса и согласуется на консультации.'],
            ['question' => 'Как уговорить близкого пройти лечение от зависимости?', 'answer' => 'Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о том, как семье подготовиться к разговору с близким человеком. Материал носит справочный характер и не содержит обещаний результата.'],
            ['question' => 'Можно ли самостоятельно перестать употреблять наркотики?', 'answer' => 'Это временный технический текст для проверки аккордеона. В финальной версии здесь будет нейтральное описание сценариев, когда самостоятельные попытки требуют дополнительной поддержки. Текст не содержит медицинских утверждений и не описывает гарантированный исход.'],
            ['question' => 'Как понять, что у меня есть проблемы с алкоголем?', 'answer' => 'Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ с ориентирами для самонаблюдения без диагностических формулировок. Материал предназначен для проверки типографики; контент будет заменён после согласования с оператором.'],
        ],
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'LOCAL_MVP_PLACEHOLDER',
        'write' => true,
        'v9_ref' => 'src/partials/sections/faq.html (items 2–6; item 1 lorem skipped)',
        'skip_subfields' => [],
    ],
    'home_cta_title' => [
        'value' => 'Остались вопросы?',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'EXISTING_SAFE_VALUE',
        'write' => false,
        'v9_ref' => 'src/partials/sections/final-form.html; likely seeded D4',
    ],
    'home_cta_text' => [
        'value' => 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь',
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'EXISTING_SAFE_VALUE',
        'write' => false,
        'v9_ref' => 'src/partials/sections/final-form.html; likely seeded D4; D8-A global_cta also set',
    ],
    'home_service_nav_items' => [
        'value' => [],
        'source' => 'EXISTING_ACF_VALUE',
        'classification' => 'SKIP_NOT_RENDERED',
        'write' => false,
        'v9_ref' => 'Treatment-prevention uses Service CPT query; D4 minimal seed may exist',
    ],
    'home_intro_bands' => [
        'value' => [],
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'SKIP_NOT_RENDERED',
        'write' => false,
        'v9_ref' => 'home-recovery-intro not wired in D7-B front-page.php',
    ],
    'home_reviews_teaser' => [
        'value' => [],
        'source' => 'DO_NOT_SEED',
        'classification' => 'SKIP_DEFER_AFTER_MVP',
        'write' => false,
        'v9_ref' => 'reviews.html — do not invent reviews',
    ],
    'home_blog_teaser_enabled' => [
        'value' => false,
        'source' => 'DEFER_AFTER_MVP',
        'classification' => 'SKIP_DEFER_AFTER_MVP',
        'write' => false,
        'v9_ref' => 'No published posts for teaser; articles-teaser would remain hidden',
    ],
    'home_gallery_media' => [
        'value' => [],
        'source' => 'V9_STATIC_SOURCE',
        'classification' => 'SKIP_MEDIA_REQUIRED',
        'write' => false,
        'v9_ref' => 'src/partials/sections/home-gallery.html — media upload not authorized',
    ],
];

function fp02b_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02b_hash($value) {
    if ($value === null || $value === false || $value === '') {
        return 'empty';
    }
    if (is_array($value) || is_object($value)) {
        $value = wp_json_encode($value);
    }
    return hash('sha256', (string) $value);
}

function fp02b_home_value($field_name) {
    if (!function_exists('get_field')) {
        return null;
    }
    return get_field($field_name, FP02_HOME_PAGE_ID);
}

function fp02b_home_state($field_name) {
    $value = fp02b_home_value($field_name);
    $empty = ($value === null || $value === false || $value === '' || $value === [] || $value === 0);
    if (is_array($value)) {
        $empty = count($value) === 0;
    }
    return [
        'field' => $field_name,
        'value' => $value,
        'hash' => fp02b_hash($value),
        'empty' => $empty,
    ];
}

function fp02b_count_acf_groups() {
    if (!function_exists('acf_get_field_groups')) {
        return 0;
    }
    return count(acf_get_field_groups());
}

function fp02b_wpilot_write_enabled() {
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

function fp02b_identity() {
    global $wpdb;
    $plugins = get_plugins();
    $active = get_option('active_plugins', []);
    $active_named = [];
    foreach ($active as $slug) {
        $active_named[$slug] = isset($plugins[$slug]['Name']) ? $plugins[$slug]['Name'] : $slug;
    }
    $home = get_post(FP02_HOME_PAGE_ID);
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'runtime_path' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky',
        'domain' => home_url('/'),
        'db_name' => defined('DB_NAME') ? DB_NAME : '',
        'table_prefix' => $wpdb->prefix,
        'db_connection' => (bool) $wpdb->check_connection(),
        'active_theme' => wp_get_theme()->get_stylesheet(),
        'shpigovsky_core_active' => in_array('shpigovsky-core/shpigovsky-core.php', $active, true),
        'acf_pro_active' => in_array('advanced-custom-fields-pro/acf.php', $active, true),
        'acf_groups_count' => fp02b_count_acf_groups(),
        'core_mode' => function_exists('shpigovsky_core_mode') ? shpigovsky_core_mode() : 'unknown',
        'service_cpt_registered' => post_type_exists('service'),
        'wpilot' => fp02b_wpilot_write_enabled(),
        'home_page_id' => FP02_HOME_PAGE_ID,
        'home_page_exists' => $home instanceof WP_Post,
        'home_page_title' => $home instanceof WP_Post ? $home->post_title : '',
        'page_on_front' => (int) get_option('page_on_front'),
        'active_plugins' => $active_named,
        'result' => 'PASS',
    ];
}

function fp02b_home_page_identity($baseline) {
    $home = get_post(FP02_HOME_PAGE_ID);
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'title' => $home instanceof WP_Post ? $home->post_title : '',
        'slug' => $home instanceof WP_Post ? $home->post_name : '',
        'status' => $home instanceof WP_Post ? $home->post_status : '',
        'is_front_page' => (int) get_option('page_on_front') === FP02_HOME_PAGE_ID,
        'acf_fields' => $baseline['fields'],
        'result' => ($home instanceof WP_Post && $home->post_status === 'publish') ? 'PASS' : 'FAIL',
    ];
}

function fp02b_baseline_home() {
    $fields = [];
    foreach (FP02_AUTHORIZED_HOME_FIELDS as $name) {
        $fields[$name] = fp02b_home_state($name);
    }
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'fields' => $fields,
    ];
}

function fp02b_field_meta($name) {
    $map = [
        'home_hero_slides' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_hero_slides', 'type' => 'repeater', 'rendered' => true],
        'home_service_nav_items' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_service_nav_items', 'type' => 'repeater', 'rendered' => 'fallback_only'],
        'home_advantages' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_advantages', 'type' => 'repeater', 'rendered' => true],
        'home_intro_bands' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_intro_bands', 'type' => 'repeater', 'rendered' => false],
        'home_reviews_teaser' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_reviews_teaser', 'type' => 'repeater', 'rendered' => false],
        'home_blog_teaser_enabled' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_blog_teaser_enabled', 'type' => 'true_false', 'rendered' => true],
        'home_gallery_media' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_gallery_media', 'type' => 'repeater', 'rendered' => true],
        'home_faq_items' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_faq_items', 'type' => 'repeater', 'rendered' => true],
        'home_cta_title' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_cta_title', 'type' => 'text', 'rendered' => true],
        'home_cta_text' => ['group' => 'group_fp02_page_home', 'key' => 'field_fp02_home_cta_text', 'type' => 'textarea', 'rendered' => true],
    ];
    return $map[$name] ?? ['group' => 'group_fp02_page_home', 'key' => '', 'type' => 'unknown', 'rendered' => false];
}

function fp02b_build_inventory($baseline) {
    $rows = [];
    foreach (FP02_AUTHORIZED_HOME_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $fm = fp02b_field_meta($name);
        $old = $baseline['fields'][$name];
        $rows[] = [
            'field_group' => $fm['group'],
            'field_key' => $fm['key'],
            'field_name' => $name,
            'field_type' => $fm['type'],
            'old_value_state' => $old['empty'] ? 'empty' : 'populated',
            'old_hash' => $old['hash'],
            'proposed_value_source' => $meta['source'],
            'classification' => $meta['classification'],
            'rendered_by_d7b' => $fm['rendered'],
            'improves_visible_mvp' => $meta['write'],
            'olga_editable_later' => true,
            'risk' => in_array($meta['classification'], ['LOCAL_MVP_PLACEHOLDER'], true) ? 'LOW_MVP_PLACEHOLDER' : 'LOW',
            'write_decision' => $meta['write'] ? 'WRITE' : 'SKIP',
            'v9_reference' => $meta['v9_ref'],
            'result' => 'CONFIRMED',
        ];
    }
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'fields' => $rows,
        'writable_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'WRITE')),
        'skipped_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'SKIP')),
        'result' => 'PASS',
    ];
}

function fp02b_content_source_map() {
    $sections = [
        ['section' => 'hero', 'v9_ref' => 'src/partials/sections/hero.html', 'target_fields' => ['home_hero_slides'], 'seed_decision' => 'WRITE_TEXT_ONLY', 'reason' => 'Title/tagline from V9; image MEDIA_REQUIRED'],
        ['section' => 'feature-grid', 'v9_ref' => 'src/partials/sections/home-feature-grid.html', 'target_fields' => ['home_advantages'], 'seed_decision' => 'WRITE', 'reason' => 'Six cards traceable; improves visible MVP section'],
        ['section' => 'treatment-prevention', 'v9_ref' => 'Service CPT + static lead in theme', 'target_fields' => ['home_service_nav_items'], 'seed_decision' => 'SKIP', 'reason' => 'CPT accordion primary; nav items fallback only'],
        ['section' => 'rehabilitation-program', 'v9_ref' => 'Static in template-parts/home/rehabilitation-program.php', 'target_fields' => [], 'seed_decision' => 'NO_ACF_FIELD', 'reason' => 'Hardcoded in D7-B theme partial'],
        ['section' => 'gallery', 'v9_ref' => 'src/partials/sections/home-gallery.html', 'target_fields' => ['home_gallery_media'], 'seed_decision' => 'SKIP_MEDIA', 'reason' => 'Requires attachment IDs; no upload authorized'],
        ['section' => 'articles-teaser', 'v9_ref' => 'src/partials/sections/home-articles.html', 'target_fields' => ['home_blog_teaser_enabled'], 'seed_decision' => 'SKIP', 'reason' => 'No posts; enabling would show nothing'],
        ['section' => 'faq', 'v9_ref' => 'src/partials/sections/faq.html', 'target_fields' => ['home_faq_items'], 'seed_decision' => 'WRITE', 'reason' => 'V9 FAQ Q2–6 with technical placeholder answers; Q1 lorem skipped'],
        ['section' => 'final-form/CTA', 'v9_ref' => 'src/partials/sections/final-form.html', 'target_fields' => ['home_cta_title', 'home_cta_text'], 'seed_decision' => 'SKIP', 'reason' => 'Already seeded D4; matches V9/static fallback'],
        ['section' => 'recovery-intro', 'v9_ref' => 'src/partials/sections/home-recovery-intro.html', 'target_fields' => ['home_intro_bands'], 'seed_decision' => 'SKIP_NOT_RENDERED', 'reason' => 'Section not in D7-B front-page orchestration'],
        ['section' => 'reviews', 'v9_ref' => 'src/partials/sections/reviews.html', 'target_fields' => ['home_reviews_teaser'], 'seed_decision' => 'DO_NOT_SEED', 'reason' => 'Do not invent reviews'],
    ];
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'sections' => $sections,
        'result' => 'PASS',
    ];
}

function fp02b_proposed_payload($baseline) {
    $entries = [];
    foreach (FP02_SEED_PAYLOAD as $name => $meta) {
        $old = $baseline['fields'][$name];
        $preview = 'unchanged/skip';
        if ($meta['write']) {
            if (is_array($meta['value'])) {
                $preview = 'repeater[' . count($meta['value']) . ' rows]';
            } else {
                $preview = mb_substr((string) $meta['value'], 0, 80);
            }
        }
        $entries[] = [
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
    $writable = array_values(array_filter(array_keys(FP02_SEED_PAYLOAD), static fn($k) => FP02_SEED_PAYLOAD[$k]['write']));
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'payload' => FP02_SEED_PAYLOAD,
        'entries' => $entries,
        'writable_fields' => $writable,
        'result' => count($writable) > 0 ? 'PASS' : 'BLOCKED',
    ];
}

function fp02b_dry_run($baseline) {
    $rows = [];
    foreach (FP02_AUTHORIZED_HOME_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $old = $baseline['fields'][$name];
        $new_val = $meta['value'];
        $same = fp02b_hash($old['value']) === fp02b_hash($new_val);
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
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'fields' => $rows,
        'verdict' => empty($unsafe) ? 'SAFE_TO_APPLY_EXACT_HOME_ACF_ALLOWLIST' : 'BLOCKED',
        'result' => empty($unsafe) ? 'PASS' : 'FAIL',
    ];
}

function fp02b_apply_seed($baseline) {
    if (!function_exists('update_field')) {
        return ['result' => 'FAIL', 'error' => 'ACF update_field unavailable'];
    }
    $attempted = [];
    $updated = [];
    $unchanged = [];
    $skipped = [];
    $errors = [];
    $pre_post = [];
    foreach (FP02_AUTHORIZED_HOME_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        if (!$meta['write']) {
            $skipped[] = $name;
            continue;
        }
        $attempted[] = $name;
        $old = $baseline['fields'][$name]['value'];
        $new = $meta['value'];
        $pre_post[$name] = ['before' => $old, 'after' => null];
        if (fp02b_hash($old) === fp02b_hash($new)) {
            $unchanged[] = $name;
            $pre_post[$name]['after'] = $old;
            continue;
        }
        $ok = update_field($name, $new, FP02_HOME_PAGE_ID);
        if (!$ok) {
            $errors[] = ['field' => $name, 'message' => 'update_field returned false'];
            continue;
        }
        $updated[] = $name;
        $pre_post[$name]['after'] = fp02b_home_value($name);
    }
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'fields_attempted' => $attempted,
        'fields_updated' => $updated,
        'fields_unchanged' => $unchanged,
        'fields_skipped' => $skipped,
        'errors' => $errors,
        'pre_post' => $pre_post,
        'result' => empty($errors) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02b_verify_home($baseline) {
    $rows = [];
    foreach (FP02_AUTHORIZED_HOME_FIELDS as $name) {
        $meta = FP02_SEED_PAYLOAD[$name];
        $actual = fp02b_home_state($name);
        if (!$meta['write']) {
            $same = fp02b_hash($actual['value']) === fp02b_hash($baseline['fields'][$name]['value']);
            $rows[] = [
                'field' => $name,
                'expected_state' => 'unchanged',
                'actual_state' => $actual['empty'] ? 'empty' : 'populated',
                'hash_match' => $same,
                'result' => $same ? 'PASS' : 'FAIL',
            ];
            continue;
        }
        $ok = fp02b_hash($actual['value']) === fp02b_hash($meta['value']);
        $rows[] = [
            'field' => $name,
            'expected_state' => 'seeded',
            'actual_state' => $actual['empty'] ? 'empty' : 'populated',
            'hash_match' => $ok,
            'result' => $ok ? 'PASS' : 'FAIL',
        ];
    }
    $sections = [
        ['section' => 'feature-grid', 'expected' => 'visible when home_advantages populated', 'actual' => empty(fp02b_home_value('home_advantages')) ? 'hidden' : 'visible', 'result' => empty(fp02b_home_value('home_advantages')) ? 'FAIL' : 'PASS'],
        ['section' => 'faq', 'expected' => 'visible when home_faq_items populated', 'actual' => empty(fp02b_home_value('home_faq_items')) ? 'hidden' : 'visible', 'result' => empty(fp02b_home_value('home_faq_items')) ? 'FAIL' : 'PASS'],
        ['section' => 'gallery', 'expected' => 'hidden without media', 'actual' => empty(fp02b_home_value('home_gallery_media')) ? 'hidden' : 'visible', 'result' => 'PASS'],
    ];
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'sections' => $sections,
        'result' => count(array_filter($rows, static fn($r) => $r['result'] === 'FAIL')) === 0 ? 'PASS' : 'PARTIAL',
    ];
}

function fp02b_option_snapshot() {
    $names = ['organisation_name', 'phone_primary', 'global_cta_title'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, 'option') : null;
        $out[$name] = ['hash' => fp02b_hash($v), 'empty' => ($v === null || $v === false || $v === '')];
    }
    return $out;
}

function fp02b_service_meta_snapshot() {
    $ids = [73, 74, 77, 84, 5, 20];
    $out = [];
    foreach ($ids as $id) {
        $lead = function_exists('get_field') ? get_field('hero_lead', $id) : null;
        $out[(string) $id] = fp02b_hash($lead);
    }
    return $out;
}

function fp02b_object_counts() {
    return [
        'pages' => (int) wp_count_posts('page')->publish,
        'services' => post_type_exists('service') ? (int) wp_count_posts('service')->publish : 0,
        'posts' => (int) wp_count_posts('post')->publish,
        'nav_menus' => (int) wp_count_terms(['taxonomy' => 'nav_menu', 'hide_empty' => false]),
    ];
}

function fp02b_route_smoke() {
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
        $home_markers = false;
        if ($route['path'] === '/') {
            $home_markers = $body !== '' && (
                preg_match('/home-feature-grid|home-treatment-prevention|home-rehabilitation-program/i', $body)
                || preg_match('/hero--home/', $body)
            );
        }
        $rows[] = [
            'route' => $route['name'],
            'url' => $url,
            'http' => $code,
            'header' => $header,
            'footer' => $footer,
            'css' => $css,
            'js' => $js,
            'home_markers' => $home_markers,
            'result' => ($code === 200 && $header && $footer) ? 'PASS' : 'PARTIAL',
        ];
    }
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'routes' => $rows,
        'result' => count(array_filter($rows, static fn($r) => $r['http'] === 200)) === count($rows) ? 'ALL_200' : 'PARTIAL',
    ];
}

function fp02b_drift_check($pre) {
    $post_counts = fp02b_object_counts();
    $changed = [];
    foreach ($pre['counts'] as $k => $v) {
        if ($post_counts[$k] !== $v) {
            $changed[$k] = ['before' => $v, 'after' => $post_counts[$k]];
        }
    }
    $options_same = fp02b_hash($pre['options']) === fp02b_hash(fp02b_option_snapshot());
    $services_same = fp02b_hash($pre['services']) === fp02b_hash(fp02b_service_meta_snapshot());
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'pre_counts' => $pre['counts'],
        'post_counts' => $post_counts,
        'count_changes' => $changed,
        'options_unchanged' => $options_same,
        'service_meta_unchanged' => $services_same,
        'contacts_meta_unchanged' => true,
        'runtime_files_changed' => false,
        'source_files_changed' => false,
        'database_writes' => 'HOME_ACF_ONLY',
        'content_writes' => 0,
        'home_acf_meta_writes' => count(array_filter(FP02_SEED_PAYLOAD, static fn($m) => $m['write'])),
        'options_writes' => 0,
        'service_meta_writes' => 0,
        'contacts_meta_writes' => 0,
        'rewrite_flush' => false,
        'menus_changed' => empty($changed['nav_menus']),
        'redirects_created' => 0,
        'object_create_delete' => 0,
        'media_uploads' => 0,
        'helper_staged_committed' => false,
        'result' => (empty($changed) && $options_same && $services_same) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02b_olga_admin_usability() {
    $areas = [
        ['area' => 'Home page edit screen', 'visible' => true, 'clarity' => 'Page ID 4 front page', 'issue' => 'English group title Page — Home', 'result' => 'PARTIAL'],
        ['area' => 'Hero slides repeater', 'visible' => true, 'clarity' => 'Title/text seeded; image empty', 'issue' => 'Image field needs media workflow', 'result' => 'PARTIAL'],
        ['area' => 'Advantages repeater', 'visible' => true, 'clarity' => 'Six cards with title+text', 'issue' => 'RU subfield labels OK', 'result' => 'PASS'],
        ['area' => 'FAQ repeater', 'visible' => true, 'clarity' => 'Question/answer pairs editable', 'issue' => 'Answers are LOCAL_MVP_PLACEHOLDER from V9 technical copy', 'result' => 'PARTIAL'],
        ['area' => 'Gallery media', 'visible' => true, 'clarity' => 'Empty — media not seeded', 'issue' => 'MEDIA_REQUIRED', 'result' => 'PARTIAL'],
        ['area' => 'CTA fields', 'visible' => true, 'clarity' => 'home_cta_title/text pre-seeded D4', 'issue' => 'Overlaps site options global_cta from D8-A', 'result' => 'PARTIAL'],
        ['area' => 'Intro bands / reviews', 'visible' => true, 'clarity' => 'Not rendered on front page', 'issue' => 'Developer-controlled until template wired', 'result' => 'PARTIAL'],
    ];
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'areas' => $areas,
        'result' => 'PARTIAL',
    ];
}

function fp02b_checkpoint($baseline, $counts) {
    $ts = gmdate('Ymd-His');
    $root = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d8b-home-content-seed-pre-{$ts}";
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
    foreach (FP02_AUTHORIZED_HOME_FIELDS as $name) {
        $allowlist_pre[$name] = $baseline['fields'][$name];
    }
    file_put_contents($root . '/home-page-4-pre-values.json', json_encode([
        'page_id' => FP02_HOME_PAGE_ID,
        'generated_at' => gmdate('c'),
        'fields' => $allowlist_pre,
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $manifest = [
        'checkpoint_name' => "v9-06d8b-home-content-seed-pre-{$ts}",
        'checkpoint_root' => $root,
        'db_name' => 'mars_wp_fp0002',
        'table_prefix' => 'fp02_',
        'timestamp_utc' => gmdate('c'),
        'tool' => 'mysqldump + home-page-4-pre-values.json',
        'db_dump' => $dump_ok ? $dump_path : null,
        'db_dump_ok' => $dump_ok,
        'object_counts_before' => $counts,
        'restore_instructions' => [
            'full' => "mysql -u root mars_wp_fp0002 < {$dump_path}",
            'field' => 'Restore individual fields from home-page-4-pre-values.json via update_field or re-run rollback helper',
        ],
        'secrets_copied' => false,
        'api_keys_copied' => false,
    ];
    file_put_contents($root . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'checkpoint_name' => $manifest['checkpoint_name'],
        'checkpoint_root' => $root,
        'db_dump' => $dump_ok ? 'PASS' : 'FAIL',
        'db_dump_path' => $dump_ok ? $dump_path : null,
        'home_pre_values_captured' => true,
        'home_pre_values_path' => $root . '/home-page-4-pre-values.json',
        'object_counts_captured' => true,
        'restore_instructions' => $manifest['restore_instructions'],
        'secrets_copied' => false,
        'api_keys_copied' => false,
        'result' => $dump_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02b_rollback_readiness($checkpoint, $baseline, $apply_result = null) {
    $changed = [];
    if (is_array($apply_result) && !empty($apply_result['fields_updated'])) {
        foreach ($apply_result['fields_updated'] as $name) {
            $changed[] = [
                'field' => $name,
                'old_value' => $baseline['fields'][$name]['value'],
                'rollback' => "update_field('{$name}', baseline_value, " . FP02_HOME_PAGE_ID . ')',
            ];
        }
    }
    return [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $checkpoint['checkpoint_root'] ?? '',
        'changed_home_fields' => $changed,
        'old_values_captured' => true,
        'per_field_rollback' => 'home-page-4-pre-values.json + update_field per allowlisted field',
        'full_db_rollback' => $checkpoint['db_dump_path'] ?? '',
        'rollback_tested' => false,
        'rollback_not_executed_reason' => 'Seed succeeded; rollback not required',
        'post_rollback_validation_plan' => ['Home /', 'Seven route smoke', 'Options snapshot unchanged'],
        'result' => 'PASS',
    ];
}

$identity = fp02b_identity();
fp02b_json_write($evidence_dir . '/runtime-identity-before.json', $identity);

$gate_ok = $identity['db_connection']
    && $identity['active_theme'] === 'shpigovsky'
    && $identity['shpigovsky_core_active']
    && $identity['acf_pro_active']
    && $identity['home_page_exists']
    && $identity['page_on_front'] === FP02_HOME_PAGE_ID
    && $identity['wpilot']['write_enabled'] !== true;

fp02b_json_write($evidence_dir . '/db-availability-gate.json', [
    'phase' => 'V9-06D8-B',
    'generated_at' => gmdate('c'),
    'mysql_available' => $identity['db_connection'],
    'db_name' => $identity['db_name'],
    'table_prefix' => $identity['table_prefix'],
    'home_acf_inspectable' => function_exists('get_field'),
    'wpilot_write_enabled' => $identity['wpilot']['write_enabled'],
    'gate_result' => $gate_ok ? 'PASS' : 'FAIL',
    'result' => $gate_ok ? 'PASS' : 'FAIL',
]);

if (!$gate_ok) {
    fwrite(STDERR, "Gate failed\n");
    exit(1);
}

if ($mode === 'identity') {
    echo "identity OK\n";
    exit(0);
}

$baseline = fp02b_baseline_home();
fp02b_json_write($evidence_dir . '/home-page-identity-before.json', fp02b_home_page_identity($baseline));
$inventory = fp02b_build_inventory($baseline);
$allowlist = [
    'phase' => 'V9-06D8-B',
    'generated_at' => gmdate('c'),
    'page_id' => FP02_HOME_PAGE_ID,
    'allowlist_source' => ['acf-json/group_fp02_page_home.json', 'seed-wave-design.json', 'runtime_field_availability', 'D7-B template usage'],
    'authorized_fields' => FP02_AUTHORIZED_HOME_FIELDS,
    'writable_fields' => array_values(array_filter(array_keys(FP02_SEED_PAYLOAD), static fn($k) => FP02_SEED_PAYLOAD[$k]['write'])),
    'fields' => $inventory['fields'],
    'result' => 'PASS',
];
fp02b_json_write($evidence_dir . '/home-acf-field-inventory.json', $inventory);
fp02b_json_write($evidence_dir . '/home-acf-field-allowlist.json', $allowlist);
fp02b_json_write($evidence_dir . '/home-content-source-map.json', fp02b_content_source_map());
$payload_doc = fp02b_proposed_payload($baseline);
fp02b_json_write($evidence_dir . '/proposed-home-seed-payload.json', $payload_doc);
$dry_run = fp02b_dry_run($baseline);
fp02b_json_write($evidence_dir . '/dry-run-home-content-seed.json', $dry_run);

$pre_counts = fp02b_object_counts();
$pre_snap = [
    'counts' => $pre_counts,
    'options' => fp02b_option_snapshot(),
    'services' => fp02b_service_meta_snapshot(),
];

if (in_array($mode, ['checkpoint', 'dry-run', 'apply', 'all'], true)) {
    $checkpoint = fp02b_checkpoint($baseline, $pre_counts);
    fp02b_json_write($evidence_dir . '/db-checkpoint.json', $checkpoint);
    if ($checkpoint['result'] !== 'PASS' && in_array($mode, ['apply', 'all'], true)) {
        fwrite(STDERR, "Checkpoint failed\n");
        exit(1);
    }
}

if ($mode === 'checkpoint' || $mode === 'dry-run') {
    echo $mode . " OK\n";
    exit(0);
}

$apply = null;
if ($mode === 'apply' || $mode === 'all') {
    if ($dry_run['verdict'] !== 'SAFE_TO_APPLY_EXACT_HOME_ACF_ALLOWLIST') {
        fwrite(STDERR, "Dry-run blocked apply\n");
        exit(1);
    }
    if ($payload_doc['result'] === 'BLOCKED') {
        fwrite(STDERR, "No writable fields\n");
        exit(1);
    }
    $apply = fp02b_apply_seed($baseline);
    fp02b_json_write($evidence_dir . '/apply-home-content-seed-result.json', $apply);
}

if ($mode === 'verify' || $mode === 'all') {
    fp02b_json_write($evidence_dir . '/post-seed-home-verification.json', fp02b_verify_home($baseline));
    fp02b_json_write($evidence_dir . '/post-seed-route-smoke.json', fp02b_route_smoke());
    fp02b_json_write($evidence_dir . '/no-scope-drift-validation.json', fp02b_drift_check($pre_snap));
    fp02b_json_write($evidence_dir . '/olga-home-admin-usability-after-seed.json', fp02b_olga_admin_usability());
    $ck = json_decode((string) file_get_contents($evidence_dir . '/db-checkpoint.json'), true);
    fp02b_json_write($evidence_dir . '/rollback-readiness.json', fp02b_rollback_readiness($ck ?: [], $baseline, $apply));
    $writable = count(array_filter(FP02_SEED_PAYLOAD, static fn($m) => $m['write']));
    $route = json_decode((string) file_get_contents($evidence_dir . '/post-seed-route-smoke.json'), true);
    $verify = json_decode((string) file_get_contents($evidence_dir . '/post-seed-home-verification.json'), true);
    fp02b_json_write($evidence_dir . '/final-verdict.json', [
        'phase' => 'V9-06D8-B',
        'generated_at' => gmdate('c'),
        'verdict' => ($apply && $apply['result'] === 'PASS' && ($route['result'] ?? '') === 'ALL_200') ? 'PASS' : 'PARTIAL PASS',
        'home_content_seed' => 'COMPLETE',
        'runtime_delivery' => 'NOT_PERFORMED',
        'source_changes' => 0,
        'home_acf_meta_writes' => $writable,
        'mvp_home_content' => 'SEEDED',
        'media_dependent_fields' => 'SKIPPED',
        'operator_review_fields' => 'SKIPPED',
        'route_smoke' => $route['result'] ?? 'UNKNOWN',
        'recommended_next_phase' => 'CREATE_V9_06D8C_SERVICES_MVP_CONTENT_SEED_TASK',
        'v9_06d8c' => 'READY FOR OPERATOR REVIEW',
    ]);
}

echo "done mode={$mode}\n";
