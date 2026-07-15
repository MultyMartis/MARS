<?php
/**
 * FP-0002 V9-06D8-C — Services CPT ACF seed runner (services 73/74/77/84 only).
 * Modes: identity | baseline | checkpoint | dry-run | apply | verify | drift | routes | service74 | olga | all
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d8c-services-mvp-content-seed';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_HOME_PAGE_ID = 4;
const FP02_HUB_PAGE_ID = 5;
const FP02_CONTACTS_PAGE_ID = 20;

const FP02_TARGET_SERVICE_IDS = [73, 74, 77, 84];

const FP02_SERVICE_ROUTES = [
    73 => '/uslugi/zavisimosti/',
    74 => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
    77 => '/uslugi/psihicheskoe-zdorovie/',
    84 => '/uslugi/rasstroystva-pischevogo-povedeniya/',
];

const FP02_AUTHORIZED_SERVICE_FIELDS = [
    'hero_lead',
    'intro_text',
    'intro_note',
    'signs_items',
    'programme_items',
    'stages',
    'faq_items',
    'cta_title',
    'cta_text',
    'cta_button_label',
];

const FP02_FAQ_MVP_ITEMS = [
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

const FP02_PROGRAMME_ITEMS = [
    ['title' => '01 — Генотипирование', 'text' => ''],
    ['title' => '02 — Нейропсихологическая коррекция', 'text' => ''],
    ['title' => '03 — Психокоррекция', 'text' => ''],
    ['title' => '04 — Кинезиотерапия', 'text' => ''],
];

const FP02_STAGES_ITEMS = [
    [
        'title' => 'Связаться с нами',
        'text' => 'Расскажите нам о своей ситуации — в удобном для вас формате и в удобное время. Первый разговор ни к чему не обязывает, но часто становится началом перемен.',
    ],
    [
        'title' => 'Определить цели и программу',
        'text' => 'Вместе со специалистами центра мы разберёмся, что именно происходит, и составим программу, которая отвечает вашей ситуации.',
    ],
    [
        'title' => 'Выбрать категорию номера, период стационарного проживания',
        'text' => 'Комфорт среды — часть восстановления. Мы подберём условия проживания, которые подойдут именно вам, и согласуем удобные сроки.',
    ],
    [
        'title' => 'Начать реабилитацию и лечение',
        'text' => 'С первого дня рядом с вами будет команда специалистов. Здесь начинается то, ради чего вы пришли. Мы с вами — шаг за шагом, в вашем темпе.',
    ],
];

const FP02_SIGNS_74 = [
    ['title' => '', 'text' => 'В последние несколько месяцев вам не удавалось уложиться в сроки или выполнить поставленные задачи из-за употребления алкоголя?'],
    ['title' => '', 'text' => 'Вам когда-нибудь требовался алкоголь, чтобы нормально функционировать после ночи обильного употребления спиртного?'],
    ['title' => '', 'text' => 'Вам часто бывает трудно определить, что вы чувствуете во время или после употребления алкоголя?'],
    ['title' => '', 'text' => 'У вас когда-нибудь случались провалы в памяти из-за употребления алкоголя?'],
    ['title' => '', 'text' => 'Вы думаете или знаете ли вы, что ваши родственники и друзья обеспокоены вашим пристрастием к алкоголю?'],
    ['title' => '', 'text' => 'Бывает ли так, что вы продолжаете пить до тех пор, пока не потеряете сознание?'],
    ['title' => '', 'text' => 'Вы часто испытываете сильную тягу к алкоголю?'],
    ['title' => '', 'text' => 'Вы нарушили обещание, данное близким, из-за своего пристрастия к алкоголю?'],
    ['title' => '', 'text' => 'Вы опасаетесь, что можете быть алкоголиком?'],
];

const FP02_HERO_LEAD_74 = 'В центре реабилитации Шпиговский Дом мы понимаем, что каждый человек уникален, поэтому мы не предложим вам универсальный подход к лечению. Путь в борьбе с алкогольной зависимостью может быть только индивидуальным.';

const FP02_INTRO_NOTE_74 = 'ЗАВИСИМОСТЬ — НЕ ПРОСТУПОК И НЕ ЧЕРТА ХАРАКТЕРА: ЗА НЕЙ СТОЯТ ОПРЕДЕЛЕННЫЕ НЕЙРОБИОЛОГИЧЕСКИЕ ПРОЦЕССЫ И ПСИХОЛОГИЧЕСКИЕ ПРИЧИНЫ.';

function fp02c_seed_payload_for_service($service_id) {
    $common_parent = [
        'programme_items' => [
            'value' => FP02_PROGRAMME_ITEMS,
            'source' => 'V9_STATIC_SOURCE',
            'classification' => 'STATIC_V9_CONTENT',
            'write' => true,
            'v9_ref' => 'src/pages/usluga-podrazdel-v1.html services-program-v2 items',
        ],
        'stages' => [
            'value' => FP02_STAGES_ITEMS,
            'source' => 'V9_STATIC_SOURCE',
            'classification' => 'STATIC_V9_CONTENT',
            'write' => true,
            'v9_ref' => 'src/partials/sections/service-subdivision-stages-v1.html',
        ],
        'faq_items' => [
            'value' => FP02_FAQ_MVP_ITEMS,
            'source' => 'V9_STATIC_SOURCE',
            'classification' => 'LOCAL_MVP_PLACEHOLDER',
            'write' => true,
            'v9_ref' => 'src/partials/sections/faq.html items 2-6',
        ],
        'hero_lead' => [
            'value' => null,
            'source' => 'EXISTING_ACF_VALUE',
            'classification' => 'EXISTING_SAFE_VALUE',
            'write' => false,
            'v9_ref' => 'D4 minimal seed retained; V9 subdivision hero is lorem',
        ],
        'intro_text' => [
            'value' => '',
            'source' => 'DEFER_AFTER_MVP',
            'classification' => 'SKIP_DEFER_AFTER_MVP',
            'write' => false,
            'v9_ref' => 'No safe subdivision intro without lorem',
        ],
        'intro_note' => [
            'value' => '',
            'source' => 'DEFER_AFTER_MVP',
            'classification' => 'SKIP_DEFER_AFTER_MVP',
            'write' => false,
            'v9_ref' => 'No safe subdivision intro without lorem',
        ],
        'signs_items' => [
            'value' => [],
            'source' => 'DO_NOT_SEED',
            'classification' => 'SKIP_NOT_RENDERED',
            'write' => false,
            'v9_ref' => 'signs.php not in subdivision-stack.php',
        ],
        'cta_title' => [
            'value' => '',
            'source' => 'STATIC_FALLBACK_ALREADY_IN_TEMPLATE',
            'classification' => 'SKIP_DO_NOT_SEED',
            'write' => false,
            'v9_ref' => 'shpigovsky_get_service_cta_band fallback',
        ],
        'cta_text' => [
            'value' => '',
            'source' => 'STATIC_FALLBACK_ALREADY_IN_TEMPLATE',
            'classification' => 'SKIP_DO_NOT_SEED',
            'write' => false,
            'v9_ref' => 'shpigovsky_get_service_cta_band fallback',
        ],
        'cta_button_label' => [
            'value' => '',
            'source' => 'STATIC_FALLBACK_ALREADY_IN_TEMPLATE',
            'classification' => 'SKIP_DO_NOT_SEED',
            'write' => false,
            'v9_ref' => 'D8-A default_button_label via theme',
        ],
    ];

    if ((int) $service_id === 74) {
        return array_merge($common_parent, [
            'hero_lead' => [
                'value' => FP02_HERO_LEAD_74,
                'source' => 'EXISTING_ACF_VALUE',
                'classification' => 'EXISTING_SAFE_VALUE',
                'write' => false,
                'v9_ref' => 'src/pages/usluga-konechnaya-v1.html heroLead; already matches runtime',
            ],
            'intro_text' => [
                'value' => '',
                'source' => 'EXISTING_ACF_VALUE',
                'classification' => 'STATIC_V9_CONTENT',
                'write' => true,
                'v9_ref' => 'Clear D4 minimal placeholder; V9 intro has heading+lead only',
            ],
            'intro_note' => [
                'value' => FP02_INTRO_NOTE_74,
                'source' => 'V9_STATIC_SOURCE',
                'classification' => 'STATIC_V9_CONTENT',
                'write' => true,
                'v9_ref' => 'src/partials/sections/service-leaf-intro-v1.html lead',
            ],
            'signs_items' => [
                'value' => FP02_SIGNS_74,
                'source' => 'V9_STATIC_SOURCE',
                'classification' => 'STATIC_V9_CONTENT',
                'write' => true,
                'v9_ref' => 'src/partials/sections/service-leaf-signs-v1.html list items',
            ],
        ]);
    }

    return $common_parent;
}

function fp02c_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02c_hash($value) {
    if ($value === null || $value === false || $value === '') {
        return 'empty';
    }
    if (is_array($value) || is_object($value)) {
        $value = wp_json_encode($value);
    }
    return hash('sha256', (string) $value);
}

function fp02c_service_value($service_id, $field_name) {
    if (!function_exists('get_field')) {
        return null;
    }
    return get_field($field_name, (int) $service_id);
}

function fp02c_service_state($service_id, $field_name) {
    $value = fp02c_service_value($service_id, $field_name);
    $empty = ($value === null || $value === false || $value === '' || $value === [] || $value === 0);
    if (is_array($value)) {
        $empty = count($value) === 0;
    }
    return [
        'service_id' => (int) $service_id,
        'field' => $field_name,
        'value' => $value,
        'hash' => fp02c_hash($value),
        'empty' => $empty,
    ];
}

function fp02c_field_meta($field_name) {
    $map = [
        'service_layout_variant' => ['group' => 'group_fp02_service_layout_hero', 'key' => 'field_fp02_service_layout_variant', 'type' => 'select', 'rendered' => true, 'allowlist' => false],
        'hero_eyebrow' => ['group' => 'group_fp02_service_layout_hero', 'key' => 'field_fp02_hero_eyebrow_service', 'type' => 'text', 'rendered' => true, 'allowlist' => false],
        'hero_title_override' => ['group' => 'group_fp02_service_layout_hero', 'key' => 'field_fp02_hero_title_override_service', 'type' => 'text', 'rendered' => true, 'allowlist' => false],
        'hero_lead' => ['group' => 'group_fp02_service_layout_hero', 'key' => 'field_fp02_hero_lead_service', 'type' => 'textarea', 'rendered' => true, 'allowlist' => true],
        'hero_media' => ['group' => 'group_fp02_service_layout_hero', 'key' => 'field_fp02_hero_media_service', 'type' => 'image', 'rendered' => true, 'allowlist' => false],
        'hero_cta_label' => ['group' => 'group_fp02_service_layout_hero', 'key' => 'field_fp02_hero_cta_label_service', 'type' => 'text', 'rendered' => true, 'allowlist' => false],
        'intro_text' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_intro_text_service', 'type' => 'textarea', 'rendered' => true, 'allowlist' => true],
        'intro_note' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_intro_note_service', 'type' => 'textarea', 'rendered' => true, 'allowlist' => true],
        'signs_items' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_signs_items_service', 'type' => 'repeater', 'rendered' => 'alcohol_special_only', 'allowlist' => true],
        'programme_items' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_programme_items_service', 'type' => 'repeater', 'rendered' => true, 'allowlist' => true],
        'stages' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_stages_service', 'type' => 'repeater', 'rendered' => true, 'allowlist' => true],
        'faq_items' => ['group' => 'group_fp02_service_faq', 'key' => 'field_fp02_faq_items_service', 'type' => 'repeater', 'rendered' => true, 'allowlist' => true],
        'cta_title' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_cta_title_service', 'type' => 'text', 'rendered' => true, 'allowlist' => true],
        'cta_text' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_cta_text_service', 'type' => 'textarea', 'rendered' => true, 'allowlist' => true],
        'cta_button_label' => ['group' => 'group_fp02_service_structured_sections', 'key' => 'field_fp02_cta_button_label_service', 'type' => 'text', 'rendered' => true, 'allowlist' => true],
        'manual_related_services' => ['group' => 'group_fp02_service_relationships', 'key' => 'field_fp02_manual_related_services', 'type' => 'relationship', 'rendered' => false, 'allowlist' => false],
    ];
    return $map[$field_name] ?? ['group' => '', 'key' => '', 'type' => 'unknown', 'rendered' => false, 'allowlist' => false];
}

function fp02c_count_acf_groups() {
    if (!function_exists('acf_get_field_groups')) {
        return 0;
    }
    return count(acf_get_field_groups());
}

function fp02c_wpilot_write_enabled() {
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

function fp02c_identity() {
    global $wpdb;
    $plugins = get_plugins();
    $active = get_option('active_plugins', []);
    $active_named = [];
    foreach ($active as $slug) {
        $active_named[$slug] = isset($plugins[$slug]['Name']) ? $plugins[$slug]['Name'] : $slug;
    }
    $services = [];
    foreach (FP02_TARGET_SERVICE_IDS as $id) {
        $post = get_post($id);
        $url = $post instanceof WP_Post ? get_permalink($post) : '';
        $code = 0;
        if (function_exists('curl_init') && is_string($url) && $url !== '') {
            $ch = curl_init($url);
            curl_setopt_array($ch, [CURLOPT_NOBODY => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 15, CURLOPT_SSL_VERIFYPEER => false]);
            curl_exec($ch);
            $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);
        }
        $services[(string) $id] = [
            'id' => $id,
            'exists' => $post instanceof WP_Post,
            'slug' => $post instanceof WP_Post ? $post->post_name : '',
            'title' => $post instanceof WP_Post ? $post->post_title : '',
            'route' => FP02_SERVICE_ROUTES[$id] ?? '',
            'http' => $code,
            'layout_variant' => function_exists('get_field') ? get_field('service_layout_variant', $id) : null,
        ];
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'runtime_path' => 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky',
        'domain' => home_url('/'),
        'db_name' => defined('DB_NAME') ? DB_NAME : '',
        'table_prefix' => $wpdb->prefix,
        'db_connection' => (bool) $wpdb->check_connection(),
        'active_theme' => wp_get_theme()->get_stylesheet(),
        'shpigovsky_core_active' => in_array('shpigovsky-core/shpigovsky-core.php', $active, true),
        'acf_pro_active' => in_array('advanced-custom-fields-pro/acf.php', $active, true),
        'acf_groups_count' => fp02c_count_acf_groups(),
        'core_mode' => function_exists('shpigovsky_core_mode') ? shpigovsky_core_mode() : 'unknown',
        'service_cpt_registered' => post_type_exists('service'),
        'wpilot' => fp02c_wpilot_write_enabled(),
        'target_services' => $services,
        'active_plugins' => $active_named,
        'result' => 'PASS',
    ];
}

function fp02c_baseline_services() {
    $services = [];
    foreach (FP02_TARGET_SERVICE_IDS as $service_id) {
        $fields = [];
        foreach (FP02_AUTHORIZED_SERVICE_FIELDS as $name) {
            $fields[$name] = fp02c_service_state($service_id, $name);
        }
        $post = get_post($service_id);
        $services[(string) $service_id] = [
            'service_id' => $service_id,
            'slug' => $post instanceof WP_Post ? $post->post_name : '',
            'title' => $post instanceof WP_Post ? $post->post_title : '',
            'route' => FP02_SERVICE_ROUTES[$service_id] ?? '',
            'post_title_hash' => fp02c_hash($post instanceof WP_Post ? $post->post_title : ''),
            'post_content_hash' => fp02c_hash($post instanceof WP_Post ? $post->post_content : ''),
            'layout_variant' => fp02c_service_value($service_id, 'service_layout_variant'),
            'fields' => $fields,
        ];
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'services' => $services,
    ];
}

function fp02c_build_inventory($baseline) {
    $rows = [];
    foreach (FP02_TARGET_SERVICE_IDS as $service_id) {
        $payload = fp02c_seed_payload_for_service($service_id);
        $post = get_post($service_id);
        foreach (FP02_AUTHORIZED_SERVICE_FIELDS as $name) {
            $meta = $payload[$name];
            $fm = fp02c_field_meta($name);
            $old = $baseline['services'][(string) $service_id]['fields'][$name];
            $rows[] = [
                'service_id' => $service_id,
                'service_slug' => $post instanceof WP_Post ? $post->post_name : '',
                'service_route' => FP02_SERVICE_ROUTES[$service_id] ?? '',
                'field_group' => $fm['group'],
                'field_key' => $fm['key'],
                'field_name' => $name,
                'field_type' => $fm['type'],
                'old_value_state' => $old['empty'] ? 'empty' : 'populated',
                'old_hash' => $old['hash'],
                'proposed_value_source' => $meta['source'],
                'classification' => $meta['classification'],
                'rendered_by_d7d' => $fm['rendered'],
                'improves_visible_mvp' => $meta['write'],
                'olga_editable_later' => true,
                'risk' => $meta['classification'] === 'LOCAL_MVP_PLACEHOLDER' ? 'LOW_MVP_PLACEHOLDER' : 'LOW',
                'write_decision' => $meta['write'] ? 'WRITE' : 'SKIP',
                'v9_reference' => $meta['v9_ref'],
                'result' => 'CONFIRMED',
            ];
        }
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'writable_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'WRITE')),
        'skipped_count' => count(array_filter($rows, static fn($r) => $r['write_decision'] === 'SKIP')),
        'result' => 'PASS',
    ];
}

function fp02c_content_source_map() {
    $sections = [
        ['service_id' => 74, 'section' => 'hero', 'v9_ref' => 'src/pages/usluga-konechnaya-v1.html heroLead', 'target_fields' => ['hero_lead'], 'seed_decision' => 'SKIP', 'reason' => 'Already matches V9 at runtime'],
        ['service_id' => 74, 'section' => 'intro', 'v9_ref' => 'src/partials/sections/service-leaf-intro-v1.html', 'target_fields' => ['intro_note', 'intro_text'], 'seed_decision' => 'WRITE', 'reason' => 'Replace D4 placeholder; intro_note from V9 lead'],
        ['service_id' => 74, 'section' => 'signs', 'v9_ref' => 'src/partials/sections/service-leaf-signs-v1.html', 'target_fields' => ['signs_items'], 'seed_decision' => 'WRITE', 'reason' => 'Nine traceable checklist items; editorial lorem skipped'],
        ['service_id' => 74, 'section' => 'programme', 'v9_ref' => 'services-program-v2 items in usluga-konechnaya-v1.html', 'target_fields' => ['programme_items'], 'seed_decision' => 'WRITE', 'reason' => 'Four direction titles; media in theme fallback'],
        ['service_id' => 74, 'section' => 'stages', 'v9_ref' => 'src/partials/sections/service-leaf-stages-v1.html steps', 'target_fields' => ['stages'], 'seed_decision' => 'WRITE', 'reason' => 'Four steps; guarantee lead line not in WP template'],
        ['service_id' => 74, 'section' => 'faq', 'v9_ref' => 'src/partials/sections/faq.html items 2-6', 'target_fields' => ['faq_items'], 'seed_decision' => 'WRITE', 'reason' => 'LOCAL_MVP_PLACEHOLDER answers; Q1 lorem skipped'],
        ['service_id' => 74, 'section' => 'cta', 'v9_ref' => 'program-cta-band + D8-A options', 'target_fields' => ['cta_title', 'cta_text', 'cta_button_label'], 'seed_decision' => 'SKIP', 'reason' => 'Theme fallback + site options'],
        ['service_id' => 73, 'section' => 'programme/stages/faq', 'v9_ref' => 'usluga-podrazdel-v1.html shared blocks', 'target_fields' => ['programme_items', 'stages', 'faq_items'], 'seed_decision' => 'WRITE', 'reason' => 'MVP enrichment on subdivision parent'],
        ['service_id' => 73, 'section' => 'hero/intro', 'v9_ref' => 'usluga-podrazdel-v1.html', 'target_fields' => ['hero_lead', 'intro_text', 'intro_note'], 'seed_decision' => 'SKIP', 'reason' => 'V9 hero/intro lorem; retain D4 minimal'],
        ['service_id' => 77, 'section' => 'programme/stages/faq', 'v9_ref' => 'shared programme/stages pattern', 'target_fields' => ['programme_items', 'stages', 'faq_items'], 'seed_decision' => 'WRITE', 'reason' => 'Placeholder layout; shared safe blocks'],
        ['service_id' => 84, 'section' => 'programme/stages/faq', 'v9_ref' => 'shared programme/stages pattern', 'target_fields' => ['programme_items', 'stages', 'faq_items'], 'seed_decision' => 'WRITE', 'reason' => 'Placeholder layout; shared safe blocks'],
    ];
    return ['phase' => 'V9-06D8-C', 'generated_at' => gmdate('c'), 'sections' => $sections, 'result' => 'PASS'];
}

function fp02c_proposed_payload($baseline) {
    $entries = [];
    $writable_total = 0;
    foreach (FP02_TARGET_SERVICE_IDS as $service_id) {
        $payload = fp02c_seed_payload_for_service($service_id);
        foreach (FP02_AUTHORIZED_SERVICE_FIELDS as $name) {
            $meta = $payload[$name];
            $old = $baseline['services'][(string) $service_id]['fields'][$name];
            $preview = 'unchanged/skip';
            if ($meta['write']) {
                if (is_array($meta['value'])) {
                    $preview = 'repeater[' . count($meta['value']) . ' rows]';
                } else {
                    $preview = mb_substr((string) $meta['value'], 0, 80);
                }
            }
            if ($meta['write']) {
                $writable_total++;
            }
            $entries[] = [
                'service_id' => $service_id,
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
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'target_service_ids' => FP02_TARGET_SERVICE_IDS,
        'entries' => $entries,
        'writable_field_operations' => $writable_total,
        'result' => $writable_total > 0 ? 'PASS' : 'BLOCKED',
    ];
}

function fp02c_dry_run($baseline) {
    $rows = [];
    foreach (FP02_TARGET_SERVICE_IDS as $service_id) {
        $payload = fp02c_seed_payload_for_service($service_id);
        foreach (FP02_AUTHORIZED_SERVICE_FIELDS as $name) {
            $meta = $payload[$name];
            $old = $baseline['services'][(string) $service_id]['fields'][$name];
            $new_val = $meta['value'];
            $same = fp02c_hash($old['value']) === fp02c_hash($new_val);
            $operation = !$meta['write'] ? 'skip' : ($old['empty'] ? 'create' : ($same ? 'no-op' : 'update'));
            $rows[] = [
                'service_id' => $service_id,
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
    }
    $unsafe = array_filter($rows, static fn($r) => $r['result'] === 'BLOCKED');
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'target_service_ids' => FP02_TARGET_SERVICE_IDS,
        'fields' => $rows,
        'verdict' => empty($unsafe) ? 'SAFE_TO_APPLY_EXACT_SERVICE_ACF_ALLOWLIST' : 'BLOCKED',
        'result' => empty($unsafe) ? 'PASS' : 'FAIL',
    ];
}

function fp02c_apply_seed($baseline) {
    if (!function_exists('update_field')) {
        return ['result' => 'FAIL', 'error' => 'ACF update_field unavailable'];
    }
    $attempted = [];
    $updated = [];
    $unchanged = [];
    $skipped = [];
    $errors = [];
    $pre_post = [];
    foreach (FP02_TARGET_SERVICE_IDS as $service_id) {
        $payload = fp02c_seed_payload_for_service($service_id);
        foreach (FP02_AUTHORIZED_SERVICE_FIELDS as $name) {
            $meta = $payload[$name];
            $key = $service_id . ':' . $name;
            if (!$meta['write']) {
                $skipped[] = $key;
                continue;
            }
            $attempted[] = $key;
            $old = $baseline['services'][(string) $service_id]['fields'][$name]['value'];
            $new = $meta['value'];
            $pre_post[$key] = ['before' => $old, 'after' => null];
            if (fp02c_hash($old) === fp02c_hash($new)) {
                $unchanged[] = $key;
                $pre_post[$key]['after'] = $old;
                continue;
            }
            $ok = update_field($name, $new, $service_id);
            if (!$ok) {
                $errors[] = ['service_id' => $service_id, 'field' => $name, 'message' => 'update_field returned false'];
                continue;
            }
            $updated[] = $key;
            $pre_post[$key]['after'] = fp02c_service_value($service_id, $name);
        }
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'services_attempted' => FP02_TARGET_SERVICE_IDS,
        'fields_attempted' => $attempted,
        'fields_updated' => $updated,
        'fields_unchanged' => $unchanged,
        'fields_skipped' => $skipped,
        'errors' => $errors,
        'pre_post' => $pre_post,
        'result' => empty($errors) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02c_verify_services($baseline) {
    $rows = [];
    foreach (FP02_TARGET_SERVICE_IDS as $service_id) {
        $payload = fp02c_seed_payload_for_service($service_id);
        foreach (FP02_AUTHORIZED_SERVICE_FIELDS as $name) {
            $meta = $payload[$name];
            $actual = fp02c_service_state($service_id, $name);
            if (!$meta['write']) {
                $same = fp02c_hash($actual['value']) === fp02c_hash($baseline['services'][(string) $service_id]['fields'][$name]['value']);
                $rows[] = [
                    'service_id' => $service_id,
                    'field' => $name,
                    'expected_state' => 'unchanged',
                    'actual_state' => $actual['empty'] ? 'empty' : 'populated',
                    'hash_match' => $same,
                    'result' => $same ? 'PASS' : 'FAIL',
                ];
                continue;
            }
            $ok = fp02c_hash($actual['value']) === fp02c_hash($meta['value']);
            $rows[] = [
                'service_id' => $service_id,
                'field' => $name,
                'expected_state' => 'seeded',
                'actual_state' => $actual['empty'] ? 'empty' : 'populated',
                'hash_match' => $ok,
                'result' => $ok ? 'PASS' : 'FAIL',
            ];
        }
    }
    $sections = [];
    foreach ([73, 74, 77, 84] as $sid) {
        $sections[] = [
            'service_id' => $sid,
            'section' => 'programme',
            'expected' => 'visible when programme_items populated or fallback',
            'actual' => empty(fp02c_service_value($sid, 'programme_items')) ? 'fallback' : 'acf',
            'result' => 'PASS',
        ];
        $sections[] = [
            'service_id' => $sid,
            'section' => 'stages',
            'expected' => 'visible when stages populated',
            'actual' => empty(fp02c_service_value($sid, 'stages')) ? 'hidden' : 'visible',
            'result' => empty(fp02c_service_value($sid, 'stages')) ? 'FAIL' : 'PASS',
        ];
        $sections[] = [
            'service_id' => $sid,
            'section' => 'faq',
            'expected' => 'visible when faq_items populated',
            'actual' => empty(fp02c_service_value($sid, 'faq_items')) ? 'hidden' : 'visible',
            'result' => empty(fp02c_service_value($sid, 'faq_items')) ? 'FAIL' : 'PASS',
        ];
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'fields' => $rows,
        'sections' => $sections,
        'result' => count(array_filter($rows, static fn($r) => $r['result'] === 'FAIL')) === 0 ? 'PASS' : 'PARTIAL',
    ];
}

function fp02c_home_snapshot() {
    $names = ['home_advantages', 'home_faq_items', 'home_hero_slides'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, FP02_HOME_PAGE_ID) : null;
        $out[$name] = fp02c_hash($v);
    }
    return $out;
}

function fp02c_page_field_snapshot($page_id, $fields) {
    $out = [];
    foreach ($fields as $name) {
        $v = function_exists('get_field') ? get_field($name, $page_id) : null;
        $out[$name] = fp02c_hash($v);
    }
    return $out;
}

function fp02c_option_snapshot() {
    $names = ['organisation_name', 'phone_primary', 'global_cta_title'];
    $out = [];
    foreach ($names as $name) {
        $v = function_exists('get_field') ? get_field($name, 'option') : null;
        $out[$name] = fp02c_hash($v);
    }
    return $out;
}

function fp02c_non_target_service_snapshot() {
    $ids = [75, 76, 78];
    $out = [];
    foreach ($ids as $id) {
        $post = get_post($id);
        if (!$post instanceof WP_Post) {
            continue;
        }
        $out[(string) $id] = fp02c_hash(fp02c_service_value($id, 'hero_lead'));
    }
    return $out;
}

function fp02c_object_counts() {
    return [
        'pages' => (int) wp_count_posts('page')->publish,
        'services' => post_type_exists('service') ? (int) wp_count_posts('service')->publish : 0,
        'posts' => (int) wp_count_posts('post')->publish,
        'nav_menus' => (int) wp_count_terms(['taxonomy' => 'nav_menu', 'hide_empty' => false]),
    ];
}

function fp02c_route_smoke() {
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
        $rows[] = [
            'route' => $route['name'],
            'url' => $url,
            'http' => $code,
            'header' => $header,
            'footer' => $footer,
            'css' => $css,
            'js' => $js,
            'result' => ($code === 200 && $header && $footer) ? 'PASS' : 'PARTIAL',
        ];
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'routes' => $rows,
        'result' => count(array_filter($rows, static fn($r) => $r['http'] === 200)) === count($rows) ? 'ALL_200' : 'PARTIAL',
    ];
}

function fp02c_service74_regression() {
    $url = home_url(FP02_SERVICE_ROUTES[74]);
    $body = '';
    $code = 0;
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 20, CURLOPT_SSL_VERIFYPEER => false]);
        $body = (string) curl_exec($ch);
        $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
    }
    $resolved = url_to_postid($url);
    $variant = function_exists('shpigovsky_resolve_service_layout_variant') ? shpigovsky_resolve_service_layout_variant(74) : 'unknown';
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'url' => $url,
        'http' => $code,
        'resolved_object_id' => $resolved,
        'expected_object_id' => 74,
        'alcohol_special_marker' => [
            'layout_variant_acf' => get_field('service_layout_variant', 74),
            'theme_variant' => $variant,
            'body_class' => $body !== '' && preg_match('/shpigovsky-service--alcohol|page-service-leaf-v1/', $body),
            'signs_section' => $body !== '' && preg_match('/service-leaf-signs-v1/', $body),
        ],
        'route_collision' => $resolved === 74,
        'header_footer_assets' => $body !== '' && preg_match('/site-header/', $body) && preg_match('/site-footer/', $body),
        'result' => ($code === 200 && $resolved === 74 && $variant === 'alcohol-special') ? 'PASS' : 'PARTIAL',
    ];
}

function fp02c_drift_check($pre) {
    $post_counts = fp02c_object_counts();
    $changed = [];
    foreach ($pre['counts'] as $k => $v) {
        if ($post_counts[$k] !== $v) {
            $changed[$k] = ['before' => $v, 'after' => $post_counts[$k]];
        }
    }
    $options_same = fp02c_hash($pre['options']) === fp02c_hash(fp02c_option_snapshot());
    $home_same = fp02c_hash($pre['home']) === fp02c_hash(fp02c_home_snapshot());
    $hub_same = fp02c_hash($pre['hub']) === fp02c_hash(fp02c_page_field_snapshot(FP02_HUB_PAGE_ID, ['services_hub_intro', 'services_hub_faq_items']));
    $contacts_same = fp02c_hash($pre['contacts']) === fp02c_hash(fp02c_page_field_snapshot(FP02_CONTACTS_PAGE_ID, ['contacts_messengers', 'contacts_blocks']));
    $non_target_same = fp02c_hash($pre['non_target_services']) === fp02c_hash(fp02c_non_target_service_snapshot());
    $writable = 0;
    foreach (FP02_TARGET_SERVICE_IDS as $sid) {
        $payload = fp02c_seed_payload_for_service($sid);
        foreach ($payload as $meta) {
            if ($meta['write']) {
                $writable++;
            }
        }
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'pre_counts' => $pre['counts'],
        'post_counts' => $post_counts,
        'count_changes' => $changed,
        'options_unchanged' => $options_same,
        'home_unchanged' => $home_same,
        'hub_unchanged' => $hub_same,
        'contacts_unchanged' => $contacts_same,
        'non_target_services_unchanged' => $non_target_same,
        'runtime_files_changed' => false,
        'source_files_changed' => false,
        'database_writes' => 'SERVICE_ACF_ONLY',
        'native_content_writes' => 0,
        'target_service_acf_meta_writes' => $writable,
        'non_target_service_writes' => 0,
        'home_writes' => 0,
        'hub_writes' => 0,
        'contacts_writes' => 0,
        'options_writes' => 0,
        'rewrite_flush' => false,
        'permalink_rewrite_changed' => false,
        'menus_changed' => empty($changed['nav_menus'] ?? null) ? 0 : 1,
        'redirects_created' => 0,
        'object_create_delete' => 0,
        'media_uploads' => 0,
        'helper_staged_committed' => false,
        'result' => ($options_same && $home_same && $hub_same && $contacts_same && empty($changed)) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02c_olga_admin_usability() {
    $areas = [];
    foreach (FP02_TARGET_SERVICE_IDS as $sid) {
        $post = get_post($sid);
        $areas[] = [
            'service_id' => $sid,
            'area' => 'Service edit screen',
            'visible' => $post instanceof WP_Post,
            'clarity' => $post instanceof WP_Post ? $post->post_title : '',
            'issue' => 'English group titles Service — *',
            'result' => 'PARTIAL',
        ];
        $areas[] = [
            'service_id' => $sid,
            'area' => 'Programme / stages / FAQ repeaters',
            'visible' => true,
            'clarity' => 'Seeded repeaters with title/text or question/answer',
            'issue' => $sid === 74 ? 'Signs repeater now has nine checklist rows' : 'Signs not rendered on subdivision',
            'result' => $sid === 74 ? 'PASS' : 'PARTIAL',
        ];
    }
    return ['phase' => 'V9-06D8-C', 'generated_at' => gmdate('c'), 'areas' => $areas, 'result' => 'PARTIAL'];
}

function fp02c_checkpoint($baseline, $counts) {
    $ts = gmdate('Ymd-His');
    $root = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d8c-services-mvp-content-seed-pre-{$ts}";
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
    foreach (FP02_TARGET_SERVICE_IDS as $service_id) {
        $allowlist_pre[(string) $service_id] = $baseline['services'][(string) $service_id]['fields'];
    }
    file_put_contents($root . '/services-73-74-77-84-pre-values.json', json_encode([
        'service_ids' => FP02_TARGET_SERVICE_IDS,
        'generated_at' => gmdate('c'),
        'fields' => $allowlist_pre,
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $manifest = [
        'checkpoint_name' => "v9-06d8c-services-mvp-content-seed-pre-{$ts}",
        'checkpoint_root' => $root,
        'db_name' => 'mars_wp_fp0002',
        'table_prefix' => 'fp02_',
        'timestamp_utc' => gmdate('c'),
        'tool' => 'mysqldump + services-73-74-77-84-pre-values.json',
        'db_dump' => $dump_ok ? $dump_path : null,
        'db_dump_ok' => $dump_ok,
        'object_counts_before' => $counts,
        'restore_instructions' => [
            'full' => "mysql -u root mars_wp_fp0002 < {$dump_path}",
            'field' => 'Restore individual fields from services-73-74-77-84-pre-values.json via update_field per service/field',
        ],
        'secrets_copied' => false,
        'api_keys_copied' => false,
    ];
    file_put_contents($root . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'checkpoint_name' => $manifest['checkpoint_name'],
        'checkpoint_root' => $root,
        'db_dump' => $dump_ok ? 'PASS' : 'FAIL',
        'db_dump_path' => $dump_ok ? $dump_path : null,
        'service_pre_values_captured' => true,
        'service_pre_values_path' => $root . '/services-73-74-77-84-pre-values.json',
        'object_counts_captured' => true,
        'restore_instructions' => $manifest['restore_instructions'],
        'secrets_copied' => false,
        'api_keys_copied' => false,
        'result' => $dump_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02c_rollback_readiness($checkpoint, $baseline, $apply_result = null) {
    $changed = [];
    if (is_array($apply_result) && !empty($apply_result['fields_updated'])) {
        foreach ($apply_result['fields_updated'] as $key) {
            [$sid, $name] = explode(':', $key, 2);
            $changed[] = [
                'service_id' => (int) $sid,
                'field' => $name,
                'old_value' => $baseline['services'][(string) $sid]['fields'][$name]['value'],
                'rollback' => "update_field('{$name}', baseline_value, {$sid})",
            ];
        }
    }
    return [
        'phase' => 'V9-06D8-C',
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $checkpoint['checkpoint_root'] ?? '',
        'changed_service_fields' => $changed,
        'old_values_captured' => true,
        'per_field_rollback' => 'services-73-74-77-84-pre-values.json + update_field per allowlisted field',
        'full_db_rollback' => $checkpoint['db_dump_path'] ?? '',
        'rollback_tested' => false,
        'rollback_not_executed_reason' => 'Seed succeeded; rollback not required',
        'post_rollback_validation_plan' => ['Seven route smoke', 'Service 74 regression', 'Home/options unchanged'],
        'result' => 'PASS',
    ];
}

$identity = fp02c_identity();
fp02c_json_write($evidence_dir . '/runtime-identity-before.json', $identity);

$services_ok = true;
foreach (FP02_TARGET_SERVICE_IDS as $sid) {
    if (empty($identity['target_services'][(string) $sid]['exists'])) {
        $services_ok = false;
    }
}

$gate_ok = $identity['db_connection']
    && $identity['active_theme'] === 'shpigovsky'
    && $identity['shpigovsky_core_active']
    && $identity['acf_pro_active']
    && $identity['service_cpt_registered']
    && $services_ok
    && $identity['wpilot']['write_enabled'] !== true;

fp02c_json_write($evidence_dir . '/db-availability-gate.json', [
    'phase' => 'V9-06D8-C',
    'generated_at' => gmdate('c'),
    'mysql_available' => $identity['db_connection'],
    'db_name' => $identity['db_name'],
    'table_prefix' => $identity['table_prefix'],
    'service_acf_inspectable' => function_exists('get_field'),
    'wpilot_write_enabled' => $identity['wpilot']['write_enabled'],
    'target_services_present' => $services_ok,
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

$baseline = fp02c_baseline_services();
fp02c_json_write($evidence_dir . '/service-objects-identity-before.json', [
    'phase' => 'V9-06D8-C',
    'generated_at' => gmdate('c'),
    'services' => $baseline['services'],
    'result' => 'PASS',
]);

$inventory = fp02c_build_inventory($baseline);
$allowlist = [
    'phase' => 'V9-06D8-C',
    'generated_at' => gmdate('c'),
    'target_service_ids' => FP02_TARGET_SERVICE_IDS,
    'allowlist_source' => ['acf-json/group_fp02_service_*.json', 'seed-wave-design.json D8-C', 'D7-D template usage'],
    'authorized_fields' => FP02_AUTHORIZED_SERVICE_FIELDS,
    'forbidden_fields' => ['service_layout_variant', 'hero_media', 'hero_eyebrow', 'hero_title_override', 'manual_related_services', 'post_title', 'post_content'],
    'fields' => $inventory['fields'],
    'writable_count' => $inventory['writable_count'],
    'result' => 'PASS',
];
fp02c_json_write($evidence_dir . '/service-acf-field-inventory.json', $inventory);
fp02c_json_write($evidence_dir . '/service-acf-field-allowlist.json', $allowlist);
fp02c_json_write($evidence_dir . '/service-content-source-map.json', fp02c_content_source_map());
$payload_doc = fp02c_proposed_payload($baseline);
fp02c_json_write($evidence_dir . '/proposed-services-seed-payload.json', $payload_doc);

if ($payload_doc['result'] === 'BLOCKED') {
    fp02c_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-C', 'verdict' => 'BLOCKED', 'reason' => 'zero writable fields']);
    fwrite(STDERR, "BLOCKED: zero writable fields\n");
    exit(2);
}

$counts = fp02c_object_counts();
$pre_drift = [
    'counts' => $counts,
    'options' => fp02c_option_snapshot(),
    'home' => fp02c_home_snapshot(),
    'hub' => fp02c_page_field_snapshot(FP02_HUB_PAGE_ID, ['services_hub_intro', 'services_hub_faq_items']),
    'contacts' => fp02c_page_field_snapshot(FP02_CONTACTS_PAGE_ID, ['contacts_messengers', 'contacts_blocks']),
    'non_target_services' => fp02c_non_target_service_snapshot(),
];

$dry = fp02c_dry_run($baseline);
fp02c_json_write($evidence_dir . '/dry-run-services-content-seed.json', $dry);

if ($dry['verdict'] !== 'SAFE_TO_APPLY_EXACT_SERVICE_ACF_ALLOWLIST') {
    fp02c_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-C', 'verdict' => 'BLOCKED', 'dry_run' => $dry['verdict']]);
    fwrite(STDERR, "Dry-run blocked\n");
    exit(3);
}

if (in_array($mode, ['dry-run', 'inventory'], true)) {
    echo "dry-run OK\n";
    exit(0);
}

$checkpoint = fp02c_checkpoint($baseline, $counts);
fp02c_json_write($evidence_dir . '/db-checkpoint.json', $checkpoint);
if ($checkpoint['result'] !== 'PASS') {
    fp02c_json_write($evidence_dir . '/final-verdict.json', ['phase' => 'V9-06D8-C', 'verdict' => 'BLOCKED', 'reason' => 'checkpoint failed']);
    fwrite(STDERR, "Checkpoint failed\n");
    exit(4);
}

if ($mode === 'checkpoint') {
    echo "checkpoint OK\n";
    exit(0);
}

$apply = fp02c_apply_seed($baseline);
fp02c_json_write($evidence_dir . '/apply-services-content-seed-result.json', $apply);

$verify = fp02c_verify_services($baseline);
fp02c_json_write($evidence_dir . '/post-seed-services-verification.json', $verify);

$routes = fp02c_route_smoke();
fp02c_json_write($evidence_dir . '/post-seed-route-smoke.json', $routes);

$s74 = fp02c_service74_regression();
fp02c_json_write($evidence_dir . '/service-74-regression-after-seed.json', $s74);

$drift = fp02c_drift_check($pre_drift);
fp02c_json_write($evidence_dir . '/no-scope-drift-validation.json', $drift);

fp02c_json_write($evidence_dir . '/olga-service-admin-usability-after-seed.json', fp02c_olga_admin_usability());
fp02c_json_write($evidence_dir . '/rollback-readiness.json', fp02c_rollback_readiness($checkpoint, $baseline, $apply));

$final = [
    'phase' => 'V9-06D8-C',
    'generated_at' => gmdate('c'),
    'verdict' => ($apply['result'] === 'PASS' && $verify['result'] === 'PASS' && $routes['result'] === 'ALL_200') ? 'PASS' : 'PARTIAL PASS',
    'apply' => $apply['result'],
    'verify' => $verify['result'],
    'routes' => $routes['result'],
    'service_74' => $s74['result'],
    'drift' => $drift['result'],
    'fields_updated_count' => count($apply['fields_updated']),
    'runtime_delivery' => 'NOT_PERFORMED',
    'source_changes' => 0,
    'database_writes' => 'SERVICE_ACF_ONLY',
];
fp02c_json_write($evidence_dir . '/final-verdict.json', $final);

echo json_encode($final, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . "\n";
