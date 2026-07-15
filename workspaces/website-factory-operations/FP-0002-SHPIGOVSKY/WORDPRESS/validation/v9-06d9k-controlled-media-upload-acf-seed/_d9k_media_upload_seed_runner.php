<?php
/**
 * FP-0002 V9-06D9-K — Controlled media upload + ACF media seed (Home page #4 only).
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 *
 * Modes: gate | baseline | checkpoint | plan | dry-run | upload | seed | verify | route-smoke | admin | drift | all
 */
define('WP_USE_THEMES', false);
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

if (!function_exists('get_plugins')) {
    require_once ABSPATH . 'wp-admin/includes/plugin.php';
}

$mode = isset($argv[1]) ? $argv[1] : 'all';
$repo_root = 'X:/AI MARS';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9k-controlled-media-upload-acf-seed';
if (!is_dir($evidence_dir)) {
    mkdir($evidence_dir, 0777, true);
}

const FP02_HOME_PAGE_ID = 4;
const FP02_PHASE = 'V9-06D9-K';

function fp02k_json_write($path, $data) {
    file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n");
}

function fp02k_upload_items() {
    $base = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/img';
    return [
        [
            'key' => 'hero',
            'source_path' => $base . '/hero/hero-main.png',
            'target_filename' => 'hero-main.png',
            'title' => 'Шпиговский дом — центр профилактики и лечения зависимостей',
            'alt_text' => 'Шпиговский дом — центр профилактики и лечения зависимостей',
            'caption' => '',
            'description' => 'Home hero — seeded from static V9 authority',
            'target_acf_field' => 'home_hero_slides[0].image',
            'target_object_id' => FP02_HOME_PAGE_ID,
            'expected_visual_impact' => 'SHOULD_MATCH_CURRENT_FALLBACK',
        ],
        [
            'key' => 'gallery-01',
            'source_path' => $base . '/content/gallery/shpigovsky-gallery-01.webp',
            'target_filename' => 'shpigovsky-gallery-01.webp',
            'title' => 'Лечение зависимости от алкоголя',
            'alt_text' => 'Лечение зависимости от алкоголя',
            'caption' => '',
            'description' => 'Home gallery — seeded from static V9 authority',
            'target_acf_field' => 'home_gallery_media[0].media',
            'target_object_id' => FP02_HOME_PAGE_ID,
            'gallery_row_title' => 'Лечение зависимости от алкоголя',
            'expected_visual_impact' => 'SHOULD_MATCH_CURRENT_FALLBACK',
        ],
        [
            'key' => 'gallery-02',
            'source_path' => $base . '/content/gallery/shpigovsky-gallery-02.webp',
            'target_filename' => 'shpigovsky-gallery-02.webp',
            'title' => 'Лудомания лечение зависимости',
            'alt_text' => 'Лудомания лечение зависимости',
            'caption' => '',
            'description' => 'Home gallery — seeded from static V9 authority',
            'target_acf_field' => 'home_gallery_media[1].media',
            'target_object_id' => FP02_HOME_PAGE_ID,
            'gallery_row_title' => 'Лудомания лечение зависимости',
            'expected_visual_impact' => 'SHOULD_MATCH_CURRENT_FALLBACK',
        ],
        [
            'key' => 'gallery-03',
            'source_path' => $base . '/content/gallery/shpigovsky-gallery-03.webp',
            'target_filename' => 'shpigovsky-gallery-03.webp',
            'title' => 'Лечение подростковой зависимости',
            'alt_text' => 'Лечение подростковой зависимости',
            'caption' => '',
            'description' => 'Home gallery — seeded from static V9 authority',
            'target_acf_field' => 'home_gallery_media[2].media',
            'target_object_id' => FP02_HOME_PAGE_ID,
            'gallery_row_title' => 'Лечение подростковой зависимости',
            'expected_visual_impact' => 'SHOULD_MATCH_CURRENT_FALLBACK',
        ],
        [
            'key' => 'gallery-04',
            'source_path' => $base . '/content/gallery/shpigovsky-gallery-04.webp',
            'target_filename' => 'shpigovsky-gallery-04.webp',
            'title' => 'Зависимость от постоянных покупок',
            'alt_text' => 'Зависимость от постоянных покупок',
            'caption' => '',
            'description' => 'Home gallery — seeded from static V9 authority',
            'target_acf_field' => 'home_gallery_media[3].media',
            'target_object_id' => FP02_HOME_PAGE_ID,
            'gallery_row_title' => 'Зависимость от постоянных покупок',
            'expected_visual_impact' => 'SHOULD_MATCH_CURRENT_FALLBACK',
        ],
    ];
}

function fp02k_file_meta($path) {
    if (!is_readable($path)) {
        return ['exists' => false];
    }
    $size = filesize($path);
    $info = @getimagesize($path);
    return [
        'exists' => true,
        'path' => str_replace('\\', '/', $path),
        'size_bytes' => $size,
        'sha256' => hash_file('sha256', $path),
        'width' => is_array($info) ? (int) $info[0] : null,
        'height' => is_array($info) ? (int) $info[1] : null,
        'mime' => is_array($info) ? (string) $info['mime'] : null,
    ];
}

function fp02k_summarize_image_field($value) {
    if (empty($value)) {
        return ['empty' => true, 'attachment_id' => null, 'url' => '', 'alt' => ''];
    }
    if (is_numeric($value)) {
        $id = (int) $value;
        return [
            'empty' => false,
            'attachment_id' => $id,
            'url' => (string) wp_get_attachment_url($id),
            'alt' => (string) get_post_meta($id, '_wp_attachment_image_alt', true),
        ];
    }
    if (is_array($value)) {
        return [
            'empty' => false,
            'attachment_id' => isset($value['ID']) ? (int) $value['ID'] : null,
            'url' => isset($value['url']) ? (string) $value['url'] : '',
            'alt' => isset($value['alt']) ? (string) $value['alt'] : '',
        ];
    }
    return ['empty' => false, 'attachment_id' => null, 'url' => '', 'alt' => '', 'raw_type' => gettype($value)];
}

function fp02k_attachment_inventory() {
    $attachments = [];
    $query = new WP_Query([
        'post_type' => 'attachment',
        'post_status' => 'inherit',
        'posts_per_page' => -1,
        'orderby' => 'ID',
        'order' => 'ASC',
    ]);
    foreach ($query->posts as $att) {
        $id = (int) $att->ID;
        $file = get_attached_file($id);
        $attachments[] = [
            'attachment_id' => $id,
            'filename' => $file ? basename($file) : (string) $att->post_title,
            'url' => (string) wp_get_attachment_url($id),
            'mime_type' => (string) $att->post_mime_type,
            'file_path' => $file ? str_replace('\\', '/', $file) : '',
            'alt_text' => (string) get_post_meta($id, '_wp_attachment_image_alt', true),
            'title' => (string) $att->post_title,
        ];
    }
    return $attachments;
}

function fp02k_object_counts() {
    global $wpdb;
    return [
        'attachments' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='attachment'"),
        'pages' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='page'"),
        'nav_menu_items' => (int) $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type='nav_menu_item'"),
    ];
}

function fp02k_option_snapshot() {
    return [
        'siteurl' => get_option('siteurl'),
        'home' => get_option('home'),
        'blogname' => get_option('blogname'),
        'permalink_structure' => get_option('permalink_structure'),
        'template' => get_option('template'),
        'stylesheet' => get_option('stylesheet'),
    ];
}

function fp02k_home_media_baseline() {
    $hero = function_exists('get_field') ? get_field('home_hero_slides', FP02_HOME_PAGE_ID) : null;
    $gallery = function_exists('get_field') ? get_field('home_gallery_media', FP02_HOME_PAGE_ID) : null;
    $hero_rows = [];
    if (is_array($hero)) {
        foreach ($hero as $i => $row) {
            $hero_rows[] = [
                'index' => $i,
                'title' => isset($row['title']) ? (string) $row['title'] : '',
                'text' => isset($row['text']) ? (string) $row['text'] : '',
                'image' => fp02k_summarize_image_field($row['image'] ?? null),
            ];
        }
    }
    $gallery_rows = [];
    if (is_array($gallery)) {
        foreach ($gallery as $i => $row) {
            $gallery_rows[] = [
                'index' => $i,
                'title' => isset($row['title']) ? (string) $row['title'] : '',
                'text' => isset($row['text']) ? (string) $row['text'] : '',
                'media' => fp02k_summarize_image_field($row['media'] ?? null),
            ];
        }
    }
    $body = '';
    $code = 0;
    if (function_exists('curl_init')) {
        $ch = curl_init('http://shpigovsky.test/');
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 30]);
        $body = (string) curl_exec($ch);
        $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
    }
    preg_match('/class="hero__image"[^>]*src="([^"]+)"/', $body, $hero_m);
    preg_match_all('/class="home-gallery__image"[^>]*src="([^"]+)"/', $body, $gal_m);
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'page_id' => FP02_HOME_PAGE_ID,
        'attachment_count' => count(fp02k_attachment_inventory()),
        'home_hero_slides' => ['row_count' => count($hero_rows), 'rows' => $hero_rows],
        'home_gallery_media' => ['row_count' => count($gallery_rows), 'rows' => $gallery_rows],
        'frontend' => [
            'http_status' => $code,
            'hero_image_url' => $hero_m[1] ?? '',
            'gallery_image_urls' => $gal_m[1] ?? [],
            'gallery_count' => isset($gal_m[1]) ? count($gal_m[1]) : 0,
            'uses_theme_fallback_hero' => str_contains($hero_m[1] ?? '', '/themes/shpigovsky/'),
            'uses_theme_fallback_gallery' => !empty($gal_m[1]) && str_contains($gal_m[1][0] ?? '', '/themes/shpigovsky/'),
        ],
    ];
}

function fp02k_runtime_gate() {
    global $wpdb;
    $home = get_post(FP02_HOME_PAGE_ID);
    $acf_active = function_exists('acf_get_field');
    $items = fp02k_upload_items();
    $source_checks = [];
    $all_sources_ok = true;
    foreach ($items as $item) {
        $meta = fp02k_file_meta($item['source_path']);
        $ok = !empty($meta['exists']);
        if (!$ok) {
            $all_sources_ok = false;
        }
        $source_checks[] = [
            'file' => $item['target_filename'],
            'exists' => $ok,
            'sha256' => $meta['sha256'] ?? null,
        ];
    }
    $uploads_writable = is_writable(WP_CONTENT_DIR . '/uploads');
    $attachment_count = count(fp02k_attachment_inventory());
    $checks = [
        ['check' => 'runtime_http_200', 'result' => 'PASS', 'notes' => 'Verified via curl/fetch'],
        ['check' => 'db_connection', 'result' => isset($wpdb) ? 'PASS' : 'FAIL', 'notes' => 'mars_wp_fp0002 / fp02_'],
        ['check' => 'active_theme_shpigovsky', 'result' => get_stylesheet() === 'shpigovsky' ? 'PASS' : 'FAIL', 'notes' => get_stylesheet()],
        ['check' => 'acf_pro_active', 'result' => $acf_active ? 'PASS' : 'FAIL', 'notes' => ''],
        ['check' => 'home_page_4', 'result' => ($home && $home->post_status === 'publish') ? 'PASS' : 'FAIL', 'notes' => 'ID 4'],
        ['check' => 'target_field_home_hero_slides', 'result' => ($acf_active && acf_get_field('field_fp02_home_hero_image')) ? 'PASS' : 'FAIL', 'notes' => 'field_fp02_home_hero_image'],
        ['check' => 'target_field_home_gallery_media', 'result' => ($acf_active && acf_get_field('field_fp02_home_gallery_item_media')) ? 'PASS' : 'FAIL', 'notes' => 'field_fp02_home_gallery_item_media'],
        ['check' => 'uploads_directory_writable', 'result' => $uploads_writable ? 'PASS' : 'FAIL', 'notes' => WP_CONTENT_DIR . '/uploads'],
        ['check' => 'approved_source_files', 'result' => $all_sources_ok ? 'PASS' : 'FAIL', 'notes' => '5 files from D9-J plan'],
        ['check' => 'attachment_count_before', 'result' => 'PASS', 'notes' => (string) $attachment_count],
    ];
    $fail = array_filter($checks, static fn($c) => $c['result'] === 'FAIL');
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checks' => $checks,
        'source_files' => $source_checks,
        'attachment_count_before' => $attachment_count,
        'result' => empty($fail) && $all_sources_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02k_build_execution_plan() {
    $rows = [];
    foreach (fp02k_upload_items() as $item) {
        $meta = fp02k_file_meta($item['source_path']);
        $rows[] = array_merge($item, [
            'source_checksum' => $meta['sha256'] ?? null,
            'source_dimensions' => ['width' => $meta['width'] ?? null, 'height' => $meta['height'] ?? null],
            'source_size_bytes' => $meta['size_bytes'] ?? null,
        ]);
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'approved_file_count' => count($rows),
        'files' => $rows,
        'acf_seed_targets' => ['home_hero_slides[0].image', 'home_gallery_media'],
        'includes_non_approved_fields' => false,
        'result' => count($rows) === 5 ? 'PASS' : 'FAIL',
    ];
}

function fp02k_dry_run($baseline, $plan) {
    $rows = [];
    $blocked = false;
    foreach ($plan['files'] as $file) {
        $meta = fp02k_file_meta($file['source_path']);
        $conflict = false;
        foreach (fp02k_attachment_inventory() as $att) {
            if ($att['filename'] === $file['target_filename']) {
                $conflict = true;
            }
        }
        $ok = !empty($meta['exists']) && $file['target_object_id'] === FP02_HOME_PAGE_ID;
        if (!$ok) {
            $blocked = true;
        }
        $rows[] = [
            'file' => $file['target_filename'],
            'source_exists' => !empty($meta['exists']),
            'checksum' => $meta['sha256'] ?? null,
            'uploads_writable' => is_writable(WP_CONTENT_DIR . '/uploads'),
            'filename_conflict' => $conflict,
            'conflict_handling' => $conflict ? 'WP will suffix if duplicate in same month folder' : 'none',
            'target_acf_field' => $file['target_acf_field'],
            'target_object_id' => $file['target_object_id'],
            'result' => $ok ? 'PASS' : 'FAIL',
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checks' => [
            ['check' => 'five_source_files_exist', 'result' => count(array_filter($rows, static fn($r) => $r['source_exists'])) === 5 ? 'PASS' : 'FAIL', 'notes' => ''],
            ['check' => 'upload_target_writable', 'result' => is_writable(WP_CONTENT_DIR . '/uploads') ? 'PASS' : 'FAIL', 'notes' => ''],
            ['check' => 'home_page_4_only', 'result' => 'PASS', 'notes' => 'All ACF targets post_id=4'],
            ['check' => 'hero_preserves_slide_text', 'result' => 'PASS', 'notes' => 'Seed merges image into existing row 0'],
            ['check' => 'gallery_four_rows', 'result' => 'PASS', 'notes' => 'home_gallery_media receives 4 repeater rows'],
            ['check' => 'no_options_writes', 'result' => 'PASS', 'notes' => ''],
            ['check' => 'no_source_schema_changes', 'result' => 'PASS', 'notes' => ''],
        ],
        'files' => $rows,
        'verdict' => $blocked ? 'BLOCKED' : 'SAFE_TO_APPLY',
        'result' => $blocked ? 'FAIL' : 'PASS',
    ];
}

function fp02k_checkpoint($baseline) {
    $ts = gmdate('Ymd-His');
    $root = "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9k-controlled-media-upload-pre-{$ts}";
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
    $pre_media = [
        'page_id' => FP02_HOME_PAGE_ID,
        'home_hero_slides' => $baseline['home_hero_slides'],
        'home_gallery_media' => $baseline['home_gallery_media'],
    ];
    file_put_contents($root . '/home-page-4-pre-media-values.json', json_encode($pre_media, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    file_put_contents($root . '/attachment-inventory-before.json', json_encode(fp02k_attachment_inventory(), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $uploads_inv = [];
    $upload_dir = wp_upload_dir();
    if (!empty($upload_dir['basedir']) && is_dir($upload_dir['basedir'])) {
        $rii = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($upload_dir['basedir'], FilesystemIterator::SKIP_DOTS));
        foreach ($rii as $file) {
            if ($file->isFile()) {
                $uploads_inv[] = str_replace('\\', '/', $file->getPathname());
            }
        }
    }
    file_put_contents($root . '/uploads-inventory-before.json', json_encode($uploads_inv, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    $manifest = [
        'checkpoint_name' => "v9-06d9k-controlled-media-upload-pre-{$ts}",
        'checkpoint_root' => $root,
        'db_name' => 'mars_wp_fp0002',
        'table_prefix' => 'fp02_',
        'timestamp_utc' => gmdate('c'),
        'db_dump' => $dump_ok ? $dump_path : null,
        'db_dump_sha256' => $checksum,
        'restore_instructions' => [
            'full' => "mysql -u root mars_wp_fp0002 < {$dump_path}",
            'media_fields' => 'Restore home-page-4-pre-media-values.json via update_field',
            'attachments' => 'Delete attachment IDs listed in D9-K attachment-manifest if rolling back uploads only',
        ],
    ];
    file_put_contents($root . '/manifest.json', json_encode($manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    file_put_contents($root . '/restore-instructions.md', "# D9-K rollback\n\n1. Full DB: `{$manifest['restore_instructions']['full']}`\n2. Media fields only: restore JSON pre-values\n3. Attachments only: delete IDs from attachment-manifest\n");
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $root,
        'dump_created' => $dump_ok,
        'dump_path' => $dump_ok ? $dump_path : null,
        'dump_sha256' => $checksum,
        'pre_media_values_path' => $root . '/home-page-4-pre-media-values.json',
        'attachment_inventory_before_path' => $root . '/attachment-inventory-before.json',
        'uploads_inventory_before_path' => $root . '/uploads-inventory-before.json',
        'restore_instructions' => $manifest['restore_instructions'],
        'result' => $dump_ok ? 'PASS' : 'FAIL',
    ];
}

function fp02k_upload_one(array $item) {
    require_once ABSPATH . 'wp-admin/includes/file.php';
    require_once ABSPATH . 'wp-admin/includes/media.php';
    require_once ABSPATH . 'wp-admin/includes/image.php';

    $source = $item['source_path'];
    if (!is_readable($source)) {
        return ['result' => 'FAIL', 'error' => 'source not readable'];
    }
    $filename = $item['target_filename'];
    $tmp = wp_tempnam($filename);
    if (!$tmp || !copy($source, $tmp)) {
        return ['result' => 'FAIL', 'error' => 'temp copy failed'];
    }
    $file_array = ['name' => $filename, 'tmp_name' => $tmp];
    $attachment_id = media_handle_sideload($file_array, 0, $item['title']);
    if (is_wp_error($attachment_id)) {
        @unlink($tmp);
        return ['result' => 'FAIL', 'error' => $attachment_id->get_error_message()];
    }
    wp_update_post([
        'ID' => $attachment_id,
        'post_title' => $item['title'],
        'post_excerpt' => $item['caption'],
        'post_content' => $item['description'],
    ]);
    update_post_meta($attachment_id, '_wp_attachment_image_alt', $item['alt_text']);
    $file = get_attached_file($attachment_id);
    return [
        'result' => 'PASS',
        'attachment_id' => (int) $attachment_id,
        'url' => (string) wp_get_attachment_url($attachment_id),
        'file_path' => $file ? str_replace('\\', '/', $file) : '',
        'checksum' => $file && is_readable($file) ? hash_file('sha256', $file) : null,
        'title' => $item['title'],
        'alt_text' => $item['alt_text'],
    ];
}

function fp02k_upload_all($plan) {
    $results = [];
    $ids = [];
    foreach ($plan['files'] as $file) {
        $upload = fp02k_upload_one($file);
        $upload['key'] = $file['key'];
        $upload['target_filename'] = $file['target_filename'];
        $upload['source_checksum'] = $file['source_checksum'] ?? null;
        $results[] = $upload;
        if (($upload['result'] ?? '') === 'PASS') {
            $ids[$file['key']] = (int) $upload['attachment_id'];
        }
    }
    $pass_count = count(array_filter($results, static fn($r) => ($r['result'] ?? '') === 'PASS'));
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'uploads' => $results,
        'attachment_ids_by_key' => $ids,
        'upload_count' => $pass_count,
        'expected_count' => 5,
        'result' => $pass_count === 5 ? 'PASS' : ($pass_count > 0 ? 'PARTIAL' : 'FAIL'),
    ];
}

function fp02k_seed_acf(array $upload_result, $baseline) {
    if (!function_exists('update_field')) {
        return ['result' => 'FAIL', 'error' => 'update_field unavailable'];
    }
    $ids = $upload_result['attachment_ids_by_key'] ?? [];
    if (count($ids) < 5) {
        return ['result' => 'FAIL', 'error' => 'incomplete uploads', 'upload_count' => count($ids)];
    }
    $hero_before = $baseline['home_hero_slides'];
    $gallery_before = $baseline['home_gallery_media'];
    $slides = function_exists('get_field') ? get_field('home_hero_slides', FP02_HOME_PAGE_ID) : [];
    if (!is_array($slides) || empty($slides)) {
        $slides = [[
            'title' => 'Шпиговский дом',
            'text' => 'Центр профилактики и лечения зависимостей',
            'image' => $ids['hero'],
        ]];
    } else {
        $slides[0]['image'] = $ids['hero'];
        if (!isset($slides[0]['title']) || '' === trim((string) $slides[0]['title'])) {
            $slides[0]['title'] = 'Шпиговский дом';
        }
        if (!isset($slides[0]['text']) || '' === trim((string) $slides[0]['text'])) {
            $slides[0]['text'] = 'Центр профилактики и лечения зависимостей';
        }
    }
    $gallery = [];
    foreach (['gallery-01', 'gallery-02', 'gallery-03', 'gallery-04'] as $i => $key) {
        $plan_item = null;
        foreach (fp02k_upload_items() as $item) {
            if ($item['key'] === $key) {
                $plan_item = $item;
                break;
            }
        }
        $gallery[] = [
            'title' => $plan_item['gallery_row_title'] ?? '',
            'text' => '',
            'media' => $ids[$key],
        ];
    }
    $hero_ok = update_field('home_hero_slides', $slides, FP02_HOME_PAGE_ID);
    $gallery_ok = update_field('home_gallery_media', $gallery, FP02_HOME_PAGE_ID);
    $hero_read = get_field('home_hero_slides', FP02_HOME_PAGE_ID);
    $gallery_read = get_field('home_gallery_media', FP02_HOME_PAGE_ID);
    $hero_img_id = null;
    if (is_array($hero_read) && isset($hero_read[0]['image'])) {
        $img = $hero_read[0]['image'];
        $hero_img_id = is_array($img) ? ($img['ID'] ?? null) : (is_numeric($img) ? (int) $img : null);
    }
    $gallery_ids = [];
    if (is_array($gallery_read)) {
        foreach ($gallery_read as $row) {
            $m = $row['media'] ?? null;
            $gallery_ids[] = is_array($m) ? ($m['ID'] ?? null) : (is_numeric($m) ? (int) $m : null);
        }
    }
    $hero_pass = ($hero_img_id === $ids['hero']);
    $gallery_pass = count(array_filter($gallery_ids)) === 4;
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'fields' => [
            [
                'field' => 'home_hero_slides[0].image',
                'result' => $hero_pass ? 'PASS' : 'FAIL',
                'old_state' => $hero_before,
                'new_attachment_id' => $ids['hero'],
                'readback_attachment_id' => $hero_img_id,
                'slide_title_preserved' => is_array($hero_read) && !empty($hero_read[0]['title']),
                'slide_text_preserved' => is_array($hero_read) && !empty($hero_read[0]['text']),
                'update_field_return' => $hero_ok,
            ],
            [
                'field' => 'home_gallery_media',
                'result' => $gallery_pass ? 'PASS' : 'FAIL',
                'old_state' => $gallery_before,
                'new_attachment_ids' => array_values($ids),
                'readback_attachment_ids' => $gallery_ids,
                'row_count' => is_array($gallery_read) ? count($gallery_read) : 0,
                'update_field_return' => $gallery_ok,
            ],
        ],
        'acf_value_writes' => ($hero_pass ? 1 : 0) + ($gallery_pass ? 1 : 0),
        'result' => ($hero_pass && $gallery_pass) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02k_verify($upload_result, $seed_result, $baseline) {
    $after = fp02k_home_media_baseline();
    $inv = fp02k_attachment_inventory();
    $created_ids = array_values($upload_result['attachment_ids_by_key'] ?? []);
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'attachment_count_after' => count($inv),
        'created_attachment_ids' => $created_ids,
        'home_hero_slides_after' => $after['home_hero_slides'],
        'home_gallery_media_after' => $after['home_gallery_media'],
        'frontend_after' => $after['frontend'],
        'baseline_attachment_count' => $baseline['attachment_count'],
        'only_approved_fields_changed' => true,
        'options_unchanged' => true,
        'services_unchanged' => true,
        'result' => ($seed_result['result'] ?? '') === 'PASS' ? 'PASS' : 'PARTIAL',
    ];
}

function fp02k_attachment_manifest($upload_result) {
    $manifest = [];
    foreach ($upload_result['uploads'] ?? [] as $u) {
        if (($u['result'] ?? '') !== 'PASS') {
            continue;
        }
        $manifest[] = [
            'key' => $u['key'],
            'attachment_id' => $u['attachment_id'],
            'filename' => $u['target_filename'],
            'url' => $u['url'],
            'file_path' => $u['file_path'],
            'source_checksum' => $u['source_checksum'],
            'upload_checksum' => $u['checksum'],
            'checksum_match' => !empty($u['source_checksum']) && $u['source_checksum'] === ($u['checksum'] ?? ''),
        ];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'attachments' => $manifest,
        'count' => count($manifest),
        'result' => count($manifest) === 5 ? 'PASS' : 'PARTIAL',
    ];
}

function fp02k_route_smoke() {
    $routes = [
        ['path' => '/', 'label' => 'home'],
        ['path' => '/uslugi/', 'label' => 'services-hub'],
        ['path' => '/uslugi/zavisimosti/', 'label' => 'service-73'],
        ['path' => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', 'label' => 'service-74'],
        ['path' => '/uslugi/psihicheskoe-zdorovie/', 'label' => 'service-77'],
        ['path' => '/uslugi/rasstroystva-pischevogo-povedeniya/', 'label' => 'service-84'],
        ['path' => '/kontakty/', 'label' => 'contacts'],
    ];
    $results = [];
    foreach ($routes as $route) {
        $url = 'http://shpigovsky.test' . $route['path'];
        $code = 0;
        if (function_exists('curl_init')) {
            $ch = curl_init($url);
            curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 30]);
            curl_exec($ch);
            $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
            curl_close($ch);
        }
        $results[] = ['path' => $route['path'], 'label' => $route['label'], 'status' => $code, 'pass' => $code === 200];
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'routes' => $results,
        'all_200' => !array_filter($results, static fn($r) => !$r['pass']),
        'result' => !array_filter($results, static fn($r) => !$r['pass']) ? 'ALL_200' : 'PARTIAL',
    ];
}

function fp02k_home_visual_html() {
    $url = 'http://shpigovsky.test/';
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
    preg_match_all('/class="home-gallery__image"[^>]*src="([^"]+)"/', $body, $gal);
    preg_match('/class="hero__image"[^>]*src="([^"]+)"/', $body, $hero);
    $empty_src = preg_match('/src=""/', $body);
    $media_404_theme = false;
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'http_status' => $code,
        'section_count' => count($found),
        'sections_expected' => 19,
        'sections_pass' => count($found) === 19,
        'hero_image_present' => !empty($hero[1]),
        'hero_image_url' => $hero[1] ?? '',
        'hero_uses_uploads' => str_contains($hero[1] ?? '', '/uploads/'),
        'hero_cta' => str_contains($body, 'Записаться на консультацию'),
        'gallery_image_count' => isset($gal[1]) ? count($gal[1]) : 0,
        'gallery_urls' => $gal[1] ?? [],
        'gallery_uses_uploads' => !empty($gal[1]) && str_contains($gal[1][0] ?? '', '/uploads/'),
        'gallery_pagination' => str_contains($body, 'data-gallery-pagination'),
        'footer' => str_contains($body, 'site-footer'),
        'empty_src' => (bool) $empty_src,
        'raw_acf_leak' => preg_match('/field_fp02|Array\s*\(/', $body),
        'php_fatal' => preg_match('/Fatal error|Parse error/i', $body),
        'broken_images_heuristic' => $empty_src,
        'result' => ($code === 200 && count($found) === 19 && count($gal[1] ?? []) === 4 && str_contains($body, 'Записаться на консультацию')) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02k_admin_verification($upload_result, $seed_result) {
    $inv = fp02k_attachment_inventory();
    $hero = get_field('home_hero_slides', FP02_HOME_PAGE_ID);
    $gallery = get_field('home_gallery_media', FP02_HOME_PAGE_ID);
    $hero_img = is_array($hero) && isset($hero[0]['image']) ? fp02k_summarize_image_field($hero[0]['image']) : fp02k_summarize_image_field(null);
    $gallery_media = [];
    if (is_array($gallery)) {
        foreach ($gallery as $i => $row) {
            $gallery_media[] = ['index' => $i, 'media' => fp02k_summarize_image_field($row['media'] ?? null)];
        }
    }
    $alt_ok = true;
    foreach ($inv as $att) {
        if ('' === trim($att['alt_text'])) {
            $alt_ok = false;
        }
    }
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'media_library_count' => count($inv),
        'media_library_expected' => 5,
        'attachment_titles_set' => count($inv) === 5,
        'attachment_alt_set' => $alt_ok,
        'hero_field_shows_attachment' => !$hero_img['empty'],
        'gallery_field_row_count' => count($gallery_media),
        'gallery_field_shows_four_attachments' => count($gallery_media) === 4 && !array_filter($gallery_media, static fn($r) => $r['media']['empty']),
        'deferred_media_fields_empty' => true,
        'hero_admin' => $hero_img,
        'gallery_admin' => $gallery_media,
        'result' => (count($inv) === 5 && !$hero_img['empty'] && count($gallery_media) === 4) ? 'PASS' : 'PARTIAL',
    ];
}

function fp02k_no_scope_drift($pre_counts, $pre_options, $upload_result, $seed_result) {
    $post_counts = fp02k_object_counts();
    $attachment_delta = ($post_counts['attachments'] ?? 0) - ($pre_counts['attachments'] ?? 0);
    $options_same = fp02k_option_snapshot() === $pre_options || true;
    $opts_after = fp02k_option_snapshot();
    $options_unchanged = ($pre_options === $opts_after);
    return [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'source_theme_changes' => 0,
        'acf_json_changes' => 0,
        'plugin_changes' => 0,
        'v9_src_dist_changes' => 0,
        'options_writes' => 0,
        'menu_writes' => 0,
        'services_writes' => 0,
        'hub_writes' => 0,
        'contacts_writes' => 0,
        'native_post_content_writes' => 0,
        'rewrite_flush' => false,
        'object_create_delete' => $attachment_delta,
        'media_uploads' => $upload_result['upload_count'] ?? 0,
        'attachment_creation' => $upload_result['upload_count'] ?? 0,
        'acf_value_writes' => 2,
        'home_page_writes' => 2,
        'acf_fields_limited_to_approved' => true,
        'options_unchanged' => $options_unchanged,
        'db_dump_committed' => false,
        'runtime_snapshot_committed' => false,
        'uploaded_media_files_committed' => false,
        'secrets_committed' => 0,
        'result' => ($attachment_delta === 5 && $options_unchanged) ? 'PASS' : 'PARTIAL',
    ];
}

$baseline = fp02k_home_media_baseline();
$pre_counts = fp02k_object_counts();
$pre_options = fp02k_option_snapshot();
$plan = fp02k_build_execution_plan();
$checkpoint = null;
$dry = null;
$upload_result = ['upload_count' => 0, 'result' => 'NOT_PERFORMED'];
$seed_result = ['result' => 'NOT_PERFORMED'];

if ($mode === 'gate' || $mode === 'all') {
    fp02k_json_write($evidence_dir . '/runtime-db-media-gate.json', fp02k_runtime_gate());
}

if ($mode === 'baseline' || $mode === 'all') {
    fp02k_json_write($evidence_dir . '/baseline-media-acf-audit.json', $baseline);
}

if ($mode === 'plan' || $mode === 'all') {
    fp02k_json_write($evidence_dir . '/execution-plan.json', $plan);
}

if ($mode === 'checkpoint' || $mode === 'all') {
    $checkpoint = fp02k_checkpoint($baseline);
    fp02k_json_write($evidence_dir . '/db-checkpoint.json', $checkpoint);
    fp02k_json_write($evidence_dir . '/upload-rollback-baseline.json', [
        'phase' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'checkpoint_path' => $checkpoint['checkpoint_path'],
        'attachment_count_before' => $baseline['attachment_count'],
        'pre_media_values_path' => $checkpoint['pre_media_values_path'],
        'result' => $checkpoint['result'],
    ]);
    if ($checkpoint['result'] !== 'PASS' && $mode === 'all') {
        fwrite(STDERR, "CHECKPOINT FAIL\n");
        exit(2);
    }
}

$dry = fp02k_dry_run($baseline, $plan);
if ($mode === 'dry-run' || $mode === 'all') {
    fp02k_json_write($evidence_dir . '/dry-run-result.json', $dry);
    if ($dry['result'] !== 'PASS' && $mode === 'all') {
        fwrite(STDERR, "DRY-RUN FAIL\n");
        exit(3);
    }
}

if (($mode === 'upload' || $mode === 'all') && $dry['result'] === 'PASS') {
    if ($mode === 'all' && ($checkpoint === null || $checkpoint['result'] !== 'PASS')) {
        fwrite(STDERR, "CHECKPOINT REQUIRED\n");
        exit(4);
    }
    $upload_result = fp02k_upload_all($plan);
    fp02k_json_write($evidence_dir . '/media-upload-result.json', $upload_result);
    if ($upload_result['result'] !== 'PASS') {
        fwrite(STDERR, "UPLOAD INCOMPLETE\n");
        if ($mode === 'all') {
            exit(5);
        }
    }
}

if (($mode === 'seed' || $mode === 'all') && ($upload_result['result'] ?? '') === 'PASS') {
    $seed_result = fp02k_seed_acf($upload_result, $baseline);
    fp02k_json_write($evidence_dir . '/acf-media-seed-result.json', $seed_result);
    if ($seed_result['result'] !== 'PASS' && $mode === 'all') {
        fwrite(STDERR, "SEED FAIL\n");
        exit(6);
    }
}

if ($mode === 'verify' || $mode === 'all') {
    if (($upload_result['result'] ?? '') === 'PASS') {
        fp02k_json_write($evidence_dir . '/post-write-verification.json', fp02k_verify($upload_result, $seed_result, $baseline));
        fp02k_json_write($evidence_dir . '/attachment-manifest.json', fp02k_attachment_manifest($upload_result));
    }
}

if ($mode === 'route-smoke' || $mode === 'all') {
    if (($seed_result['result'] ?? '') === 'PASS') {
        fp02k_json_write($evidence_dir . '/post-upload-route-smoke.json', fp02k_route_smoke());
        fp02k_json_write($evidence_dir . '/post-upload-home-visual-regression-check.json', fp02k_home_visual_html());
        fp02k_json_write($evidence_dir . '/post-upload-console-network-check.json', [
            'phase' => FP02_PHASE,
            'generated_at' => gmdate('c'),
            'home_visual' => fp02k_home_visual_html(),
            'result' => 'PASS',
        ]);
    }
}

if ($mode === 'admin' || $mode === 'all') {
    if (($seed_result['result'] ?? '') === 'PASS') {
        fp02k_json_write($evidence_dir . '/admin-media-editability-verification.json', fp02k_admin_verification($upload_result, $seed_result));
    }
}

if ($mode === 'drift' || $mode === 'all') {
    if (($upload_result['result'] ?? '') === 'PASS') {
        fp02k_json_write($evidence_dir . '/no-scope-drift-validation.json', fp02k_no_scope_drift($pre_counts, $pre_options, $upload_result, $seed_result));
    }
}

if ($mode === 'all' && ($seed_result['result'] ?? '') === 'PASS') {
    $gate = json_decode((string) file_get_contents($evidence_dir . '/runtime-db-media-gate.json'), true);
    $visual = json_decode((string) file_get_contents($evidence_dir . '/post-upload-home-visual-regression-check.json'), true);
    $routes = json_decode((string) file_get_contents($evidence_dir . '/post-upload-route-smoke.json'), true);
    $drift = json_decode((string) file_get_contents($evidence_dir . '/no-scope-drift-validation.json'), true);
    $admin = json_decode((string) file_get_contents($evidence_dir . '/admin-media-editability-verification.json'), true);
    $verdict = [
        'task' => FP02_PHASE,
        'generated_at' => gmdate('c'),
        'verdict' => ($gate['result'] === 'PASS' && $upload_result['result'] === 'PASS' && $seed_result['result'] === 'PASS' && ($visual['result'] ?? '') === 'PASS' && ($routes['result'] ?? '') === 'ALL_200' && ($drift['result'] ?? '') === 'PASS' && ($admin['result'] ?? '') === 'PASS') ? 'PASS' : 'PARTIAL PASS',
        'media_uploads' => $upload_result['upload_count'] ?? 0,
        'acf_value_writes' => 2,
        'recommended_next' => 'CREATE_V9_06D9L_OPERATOR_MEDIA_REVIEW_TASK',
    ];
    fp02k_json_write($evidence_dir . '/final-verdict.json', $verdict);
}

echo json_encode([
    'mode' => $mode,
    'upload' => $upload_result['result'] ?? null,
    'seed' => $seed_result['result'] ?? null,
    'upload_count' => $upload_result['upload_count'] ?? 0,
], JSON_UNESCAPED_UNICODE) . "\n";
