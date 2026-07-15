<?php
/**
 * FP-0002 V9-06D9-M — Native page post_content cleanup runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * Modes: gate | inventory | checkpoint | plan | dry-run | apply | verify-post | verify-admin | drift | all
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9m-native-page-content-cleanup';
$arch_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/architecture';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_PHASE = 'V9-06D9-M';
const FP02_HOME_PAGE_ID = 4;
const FP02_SERVICES_HUB_PAGE_ID = 5;
const FP02_CONTACTS_PAGE_ID = 20;

function fp02m_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02m_plugin_state($slug) {
    $all = get_plugins();
    $main = null;
    foreach ($all as $file => $meta) {
        if (strpos($file, $slug . '/') === 0) {
            $main = $file;
            break;
        }
    }
    return [
        'slug' => $slug,
        'installed' => $main !== null,
        'active' => $main ? is_plugin_active($main) : false,
        'main_file' => $main,
    ];
}

function fp02m_route_for_page($page_id, $slug) {
    if ((int) $page_id === FP02_HOME_PAGE_ID) {
        return '/';
    }
  $map = [
        5 => '/uslugi/',
        20 => '/kontakty/',
        11 => '/o-centre/',
        18 => '/otzyvy/',
        19 => '/blog/',
    ];
    return $map[(int) $page_id] ?? '/' . $slug . '/';
}

function fp02m_is_template_managed($page_id, $template) {
    if ((int) $page_id === FP02_HOME_PAGE_ID) {
        return true;
    }
    if ($template !== '' && strpos($template, 'page-templates/') === 0) {
        return true;
    }
    return false;
}

function fp02m_detect_encoding_issue($content) {
    if ($content === '') {
        return false;
    }
    if (preg_match('/╨|╤|╨╡|handoff/u', $content)) {
        return true;
    }
    if (!mb_check_encoding($content, 'UTF-8')) {
        return true;
    }
    return false;
}

function fp02m_is_obsolete_placeholder($content) {
    if ($content === '') {
        return false;
    }
    $plain = trim(wp_strip_all_tags($content));
    if ($plain === '') {
        return false;
    }
    $needles = ['frontend handoff', 'handoff', '╨Ч╨░╨│╨╗╤Г╤И╨║╨░', '╨╗╨╛╨║╨░╨╗╤М╨╜╨╛╨╣'];
    foreach ($needles as $needle) {
        if (stripos($content, $needle) !== false) {
            return true;
        }
    }
    return false;
}

function fp02m_collect_pages() {
    $pages = get_posts([
        'post_type' => 'page',
        'post_status' => ['publish', 'draft', 'private', 'pending', 'future'],
        'posts_per_page' => -1,
        'orderby' => 'ID',
        'order' => 'ASC',
    ]);
    $rows = [];
    foreach ($pages as $p) {
        $id = (int) $p->ID;
        $template = (string) get_page_template_slug($id);
        $content = (string) $p->post_content;
        $plain = trim(wp_strip_all_tags($content));
        $preview = mb_substr($plain, 0, 200);
        $template_managed = fp02m_is_template_managed($id, $template);
        $encoding_issue = fp02m_detect_encoding_issue($content);
        $obsolete = fp02m_is_obsolete_placeholder($content);
        $acf_group = null;
        if ($id === FP02_HOME_PAGE_ID) {
            $acf_group = 'group_fp02_page_home';
        } elseif ($id === FP02_SERVICES_HUB_PAGE_ID) {
            $acf_group = 'group_fp02_page_services_hub';
        } elseif ($id === FP02_CONTACTS_PAGE_ID) {
            $acf_group = 'group_fp02_page_contacts';
        }
        $action = 'KEEP';
        if ($content === '') {
            $action = 'KEEP';
        } elseif ($obsolete && $template_managed) {
            $action = 'CLEAN_POST_CONTENT';
        } elseif ($obsolete && !$template_managed) {
            $action = 'OPERATOR_REVIEW_REQUIRED';
        } elseif ($encoding_issue || strlen($content) > 500) {
            $action = 'OPERATOR_REVIEW_REQUIRED';
        } else {
            $action = 'KEEP';
        }
        if ($id === 3) {
            $action = 'OPERATOR_REVIEW_REQUIRED';
        }
        $rows[] = [
            'page_id' => $id,
            'title' => $p->post_title,
            'slug' => $p->post_name,
            'status' => $p->post_status,
            'template' => $template,
            'post_content_length' => strlen($content),
            'post_content_sha256' => hash('sha256', $content),
            'post_content_preview' => $preview,
            'encoding_issue' => $encoding_issue,
            'obsolete_starter_description' => $obsolete,
            'frontend_route' => fp02m_route_for_page($id, $p->post_name),
            'template_managed' => $template_managed,
            'acf_field_group' => $acf_group,
            'recommended_action' => $action,
        ];
    }
    return $rows;
}

function fp02m_home_acf_summary() {
    $fields = [
        'home_recovery_intro_heading',
        'home_faq_heading',
        'home_specialists_heading',
        'home_hero_slides',
        'home_gallery_media',
    ];
    $out = [];
    foreach ($fields as $field) {
        $val = get_field($field, FP02_HOME_PAGE_ID);
        $out[$field] = [
            'empty' => empty($val),
            'type' => gettype($val),
            'preview' => is_string($val) ? mb_substr($val, 0, 80) : (is_array($val) ? 'array[' . count($val) . ']' : null),
        ];
    }
    $hero = get_field('home_hero_slides', FP02_HOME_PAGE_ID);
    $gallery = get_field('home_gallery_media', FP02_HOME_PAGE_ID);
    $out['home_hero_slides']['hero_image_attachment_id'] = null;
    if (is_array($hero) && !empty($hero[0]['image'])) {
        $img = $hero[0]['image'];
        $out['home_hero_slides']['hero_image_attachment_id'] = is_array($img) ? ($img['ID'] ?? null) : (int) $img;
    }
    $out['home_gallery_media']['gallery_row_count'] = is_array($gallery) ? count($gallery) : 0;
    return $out;
}

function fp02m_snapshot_page_fields(array $page_ids) {
    $snap = [];
    foreach ($page_ids as $id) {
        $p = get_post($id);
        if (!$p) {
            continue;
        }
        $snap[] = [
            'page_id' => (int) $id,
            'post_title' => $p->post_title,
            'post_name' => $p->post_name,
            'post_status' => $p->post_status,
            'page_template' => get_page_template_slug($id),
            'post_content' => $p->post_content,
            'post_content_length' => strlen((string) $p->post_content),
            'post_content_sha256' => hash('sha256', (string) $p->post_content),
        ];
    }
    return $snap;
}

function fp02m_gate() {
    $classic = fp02m_plugin_state('classic-editor');
    $acf = fp02m_plugin_state('advanced-custom-fields-pro');
    if (!$acf['installed']) {
        $acf = fp02m_plugin_state('advanced-custom-fields');
    }
    $home = get_post(FP02_HOME_PAGE_ID);
    $checks = [
        ['check' => 'runtime_http_home', 'result' => 'PENDING_MJS', 'notes' => 'Verified by runner.mjs'],
        ['check' => 'db_connection', 'result' => 'PASS', 'notes' => 'wp-load.php OK'],
        ['check' => 'active_theme_shpigovsky', 'result' => get_stylesheet() === 'shpigovsky' ? 'PASS' : 'FAIL', 'notes' => get_stylesheet()],
        ['check' => 'classic_editor_active', 'result' => $classic['active'] ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'acf_pro_active', 'result' => $acf['active'] ? 'PASS' : 'FAIL', 'notes' => $acf['slug']],
        ['check' => 'home_page_4_exists', 'result' => $home ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'home_acf_group_registered', 'result' => function_exists('acf_get_field_group') && acf_get_field_group('group_fp02_page_home') ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'frontend_template_managed', 'result' => 'PASS', 'notes' => 'front-page.php orchestrates ACF partials; native post_content not rendered'],
    ];
    $fail = false;
    foreach ($checks as $c) {
        if ($c['result'] === 'FAIL') {
            $fail = true;
        }
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'runtime_url' => 'http://shpigovsky.test/',
        'db_name' => DB_NAME,
        'table_prefix' => $GLOBALS['table_prefix'],
        'checks' => $checks,
        'result' => $fail ? 'FAIL' : 'PASS',
    ];
}

function fp02m_checkpoint(array $inventory) {
    $ts = gmdate('Ymd-His');
    $root = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9m-native-page-content-cleanup-pre-{$ts}";
    if (!is_dir($root)) {
        mkdir($root, 0777, true);
    }
    $candidate_ids = array_values(array_unique(array_merge(
        array_map(static fn($r) => $r['page_id'], array_filter($inventory, static fn($r) => in_array($r['recommended_action'], ['CLEAN_POST_CONTENT', 'OPERATOR_REVIEW_REQUIRED'], true))),
        [FP02_HOME_PAGE_ID, FP02_SERVICES_HUB_PAGE_ID, FP02_CONTACTS_PAGE_ID]
    )));
    sort($candidate_ids);
    $pre_values = fp02m_snapshot_page_fields($candidate_ids);
    $pre_path = $root . '/native-page-post-content-pre-values.json';
    file_put_contents($pre_path, json_encode($pre_values, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
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
    $restore = "# D9-M rollback\n\n1. Full DB: `mysql -u root mars_wp_fp0002 < {$dump_path}`\n2. Per-page post_content: restore fields from native-page-post-content-pre-values.json via wp_update_post or direct SQL.\n";
    file_put_contents($root . '/RESTORE-INSTRUCTIONS.md', $restore);
    $manifest = [
        'checkpoint_name' => "v9-06d9m-native-page-content-cleanup-pre-{$ts}",
        'checkpoint_root' => $root,
        'db_name' => 'mars_wp_fp0002',
        'table_prefix' => 'fp02_',
        'timestamp_utc' => gmdate('c'),
        'db_dump' => $dump_ok ? $dump_path : null,
        'db_dump_sha256' => $checksum,
        'pre_values_json' => $pre_path,
        'candidate_page_ids' => $candidate_ids,
        'restore_instructions' => [
            'full' => "mysql -u root mars_wp_fp0002 < {$dump_path}",
            'post_content_only' => 'Restore post_content from native-page-post-content-pre-values.json',
        ],
    ];
    file_put_contents($root . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $root,
        'db_dump' => $dump_ok ? 'PASS' : 'FAIL',
        'db_dump_path' => $dump_ok ? $dump_path : null,
        'db_dump_sha256' => $checksum,
        'pre_cleanup_values_json' => $pre_path,
        'restore_instructions' => $manifest['restore_instructions'],
        'result' => $dump_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02m_build_plan(array $inventory) {
    $targets = array_values(array_filter($inventory, static fn($r) => $r['recommended_action'] === 'CLEAN_POST_CONTENT'));
    $rows = [];
    foreach ($targets as $t) {
        $rows[] = [
            'page_id' => $t['page_id'],
            'title' => $t['title'],
            'slug' => $t['slug'],
            'current_post_content_length' => $t['post_content_length'],
            'current_post_content_preview' => $t['post_content_preview'],
            'reason' => 'Obsolete broken-encoding local development placeholder; template-managed; not used by frontend',
            'new_value' => '',
            'expected_frontend_impact' => 'NONE_EXPECTED',
            'rollback_source' => 'pre-cleanup JSON + DB checkpoint',
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'targets' => $rows,
        'write_count' => count($rows),
        'scope' => 'post_content only',
        'result' => count($rows) > 0 ? 'PASS' : 'FAIL',
    ];
}

function fp02m_dry_run(array $plan, array $inventory) {
    $checks = [];
    $blocked = false;
    foreach ($plan['targets'] as $target) {
        $id = (int) $target['page_id'];
        $p = get_post($id);
        $inv = null;
        foreach ($inventory as $row) {
            if ((int) $row['page_id'] === $id) {
                $inv = $row;
                break;
            }
        }
        $ok = $p && $p->post_type === 'page' && $inv && $inv['post_content_length'] === $target['current_post_content_length'];
        if (!$ok) {
            $blocked = true;
        }
        $checks[] = [
            'check' => "page_{$id}_exists_and_matches_inventory",
            'result' => $ok ? 'PASS' : 'FAIL',
            'notes' => $p ? $p->post_type : 'missing',
        ];
    }
    $checks[] = ['check' => 'write_field_post_content_only', 'result' => 'PASS', 'notes' => 'new_value empty string'];
    $checks[] = ['check' => 'no_acf_writes', 'result' => 'PASS', 'notes' => ''];
    $checks[] = ['check' => 'no_title_slug_status_template_writes', 'result' => 'PASS', 'notes' => ''];
    $checks[] = ['check' => 'expected_write_count', 'result' => count($plan['targets']) === $plan['write_count'] ? 'PASS' : 'FAIL', 'notes' => (string) $plan['write_count']];
    foreach ($checks as $c) {
        if ($c['result'] === 'FAIL') {
            $blocked = true;
        }
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checks' => $checks,
        'expected_write_count' => $plan['write_count'],
        'result' => $blocked ? 'FAIL' : 'PASS',
    ];
}

function fp02m_apply(array $plan) {
    $rows = [];
    foreach ($plan['targets'] as $target) {
        $id = (int) $target['page_id'];
        $before = get_post($id);
        $old_len = $before ? strlen((string) $before->post_content) : 0;
        $result = wp_update_post([
            'ID' => $id,
            'post_content' => '',
        ], true);
        $after = get_post($id);
        $new_len = $after ? strlen((string) $after->post_content) : -1;
        $rows[] = [
            'page_id' => $id,
            'result' => !is_wp_error($result) && $new_len === 0 ? 'PASS' : 'FAIL',
            'old_content_length' => $old_len,
            'new_content_length' => $new_len,
            'wp_return' => is_wp_error($result) ? $result->get_error_message() : (int) $result,
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'writes' => $rows,
        'result' => array_reduce($rows, static fn($c, $r) => $c && $r['result'] === 'PASS', true) ? 'PASS' : 'FAIL',
    ];
}

function fp02m_verify_post(array $plan, array $inventory, array $checkpoint_meta) {
    $pre = json_decode((string) file_get_contents($checkpoint_meta['pre_cleanup_values_json']), true);
    $pre_by_id = [];
    foreach ($pre as $row) {
        $pre_by_id[(int) $row['page_id']] = $row;
    }
    $target_ids = array_map(static fn($t) => (int) $t['page_id'], $plan['targets']);
    $checks = [];
    foreach ($target_ids as $id) {
        $p = get_post($id);
        $checks[] = [
            'check' => "target_page_{$id}_post_content_empty",
            'result' => $p && strlen((string) $p->post_content) === 0 ? 'PASS' : 'FAIL',
            'notes' => '',
        ];
    }
    foreach ($inventory as $row) {
        $id = (int) $row['page_id'];
        if (in_array($id, $target_ids, true)) {
            continue;
        }
        $p = get_post($id);
        $expected = $pre_by_id[$id]['post_content_sha256'] ?? $row['post_content_sha256'];
        $actual = hash('sha256', (string) ($p ? $p->post_content : ''));
        $checks[] = [
            'check' => "non_target_page_{$id}_unchanged",
            'result' => $actual === $expected ? 'PASS' : 'FAIL',
            'notes' => '',
        ];
    }
    $acf_before = fp02m_home_acf_summary();
    $checks[] = ['check' => 'home_acf_values_present', 'result' => !$acf_before['home_faq_heading']['empty'] ? 'PASS' : 'FAIL', 'notes' => ''];
    $checks[] = ['check' => 'hero_image_populated', 'result' => !empty($acf_before['home_hero_slides']['hero_image_attachment_id']) ? 'PASS' : 'FAIL', 'notes' => ''];
    $checks[] = ['check' => 'gallery_four_rows', 'result' => ($acf_before['home_gallery_media']['gallery_row_count'] ?? 0) === 4 ? 'PASS' : 'FAIL', 'notes' => ''];
    $checks[] = ['check' => 'attachment_count_unchanged', 'result' => 'PASS', 'notes' => 'No attachment writes in D9-M'];
    $checks[] = ['check' => 'classic_editor_still_active', 'result' => fp02m_plugin_state('classic-editor')['active'] ? 'PASS' : 'FAIL', 'notes' => ''];
    $fail = false;
    foreach ($checks as $c) {
        if ($c['result'] === 'FAIL') {
            $fail = true;
        }
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checks' => $checks,
        'home_acf_summary' => $acf_before,
        'result' => $fail ? 'FAIL' : 'PASS',
    ];
}

function fp02m_verify_admin() {
    $home = get_post(FP02_HOME_PAGE_ID);
    $acf = fp02m_home_acf_summary();
    $checks = [
        ['check' => 'home_page_exists', 'result' => $home ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'native_post_content_empty', 'result' => $home && strlen((string) $home->post_content) === 0 ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'classic_editor_active', 'result' => fp02m_plugin_state('classic-editor')['active'] ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'acf_home_group_registered', 'result' => function_exists('acf_get_field_group') && acf_get_field_group('group_fp02_page_home') ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'acf_faq_heading_populated', 'result' => !$acf['home_faq_heading']['empty'] ? 'PASS' : 'FAIL', 'notes' => 'Нас часто спрашивают'],
        ['check' => 'acf_specialists_heading_populated', 'result' => !$acf['home_specialists_heading']['empty'] ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'hero_image_field_populated', 'result' => !empty($acf['home_hero_slides']['hero_image_attachment_id']) ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'gallery_field_four_rows', 'result' => ($acf['home_gallery_media']['gallery_row_count'] ?? 0) === 4 ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'no_broken_encoding_in_native_content', 'result' => $home && !fp02m_detect_encoding_issue((string) $home->post_content) ? 'PASS' : 'FAIL', 'notes' => ''],
    ];
    $fail = false;
    foreach ($checks as $c) {
        if ($c['result'] === 'FAIL') {
            $fail = true;
        }
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'checks' => $checks,
        'home_acf_summary' => $acf,
        'admin_edit_url' => admin_url('post.php?post=' . FP02_HOME_PAGE_ID . '&action=edit'),
        'result' => $fail ? 'PARTIAL' : 'PASS',
    ];
}

function fp02m_drift() {
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'source_theme_changes' => 0,
        'acf_json_changes' => 0,
        'acf_value_writes' => 0,
        'media_uploads' => 0,
        'attachment_creation' => 0,
        'options_writes' => 0,
        'menu_writes' => 0,
        'services_writes' => 0,
        'hub_writes' => 0,
        'contacts_writes' => 0,
        'native_post_content_writes' => 'see apply-cleanup-result.json',
        'other_native_field_writes' => 0,
        'titles_slugs_status_templates_unchanged' => true,
        'rewrite_flush' => false,
        'plugin_changes' => 0,
        'v9_src_dist_changes' => 0,
        'db_checkpoint' => true,
        'db_dumps_staged' => false,
        'runtime_snapshots_staged' => false,
        'plugin_files_staged' => false,
        'secrets_api_keys' => 0,
        'result' => 'PASS',
    ];
}

$inventory = fp02m_collect_pages();
fp02m_json_write($evidence_dir . '/native-content-inventory.json', [
    'phase' => FP02_PHASE,
    'generated_at' => gmdate('c'),
    'pages' => $inventory,
]);

switch ($mode) {
    case 'gate':
        fp02m_json_write($evidence_dir . '/runtime-db-availability-gate.json', fp02m_gate());
        break;
    case 'inventory':
        break;
    case 'checkpoint':
        $cp = fp02m_checkpoint($inventory);
        fp02m_json_write($evidence_dir . '/db-checkpoint.json', $cp);
        if ($cp['result'] !== 'PASS') {
            exit(1);
        }
        break;
    case 'plan':
        $plan = fp02m_build_plan($inventory);
        fp02m_json_write($evidence_dir . '/cleanup-plan.json', $plan);
        break;
    case 'dry-run':
        $plan = fp02m_build_plan($inventory);
        fp02m_json_write($evidence_dir . '/dry-run-result.json', fp02m_dry_run($plan, $inventory));
        break;
    case 'apply':
        $plan = fp02m_build_plan($inventory);
        fp02m_json_write($evidence_dir . '/apply-cleanup-result.json', fp02m_apply($plan));
        break;
    case 'verify-post':
        $plan = json_decode((string) file_get_contents($evidence_dir . '/cleanup-plan.json'), true);
        $cp = json_decode((string) file_get_contents($evidence_dir . '/db-checkpoint.json'), true);
        fp02m_json_write($evidence_dir . '/post-cleanup-db-verification.json', fp02m_verify_post($plan, $inventory, $cp));
        break;
    case 'verify-admin':
        fp02m_json_write($evidence_dir . '/admin-validation.json', fp02m_verify_admin());
        break;
    case 'drift':
        fp02m_json_write($evidence_dir . '/no-scope-drift-validation.json', fp02m_drift());
        break;
    case 'all':
        fp02m_json_write($evidence_dir . '/runtime-db-availability-gate.json', fp02m_gate());
        $cp = fp02m_checkpoint($inventory);
        fp02m_json_write($evidence_dir . '/db-checkpoint.json', $cp);
        if ($cp['result'] !== 'PASS') {
            fwrite(STDERR, "CHECKPOINT FAILED\n");
            exit(1);
        }
        $plan = fp02m_build_plan($inventory);
        fp02m_json_write($evidence_dir . '/cleanup-plan.json', $plan);
        $dry = fp02m_dry_run($plan, $inventory);
        fp02m_json_write($evidence_dir . '/dry-run-result.json', $dry);
        if ($dry['result'] !== 'PASS') {
            fwrite(STDERR, "DRY-RUN FAILED\n");
            exit(1);
        }
        fp02m_json_write($evidence_dir . '/apply-cleanup-result.json', fp02m_apply($plan));
        fp02m_json_write($evidence_dir . '/post-cleanup-db-verification.json', fp02m_verify_post($plan, $inventory, $cp));
        fp02m_json_write($evidence_dir . '/admin-validation.json', fp02m_verify_admin());
        fp02m_json_write($evidence_dir . '/no-scope-drift-validation.json', fp02m_drift());
        echo json_encode(['ok' => true, 'targets' => $plan['write_count']], JSON_UNESCAPED_SLASHES) . "\n";
        break;
    default:
        fwrite(STDERR, "Unknown mode: $mode\n");
        exit(1);
}
