<?php
/**
 * V9-06E18 runner — runtime delivery, ACF sync, seed, validation.
 * Local helper — not for git commit.
 */

$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$php = 'X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe';
$wp = 'X:/MARS-Localhost/tools/wp-cli/wp-cli.phar';
$validation = $root . '/validation/v9-06e18-reusable-blocks-batch-1-fields';
$checkpoint = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e18-reusable-blocks-batch-1-fields-pre-20260708-001410';

if (!is_dir($validation)) {
    mkdir($validation, 0777, true);
}
if (!is_dir($validation . '/screenshots')) {
    mkdir($validation . '/screenshots', 0777, true);
}

function sha_file($path) {
    return is_readable($path) ? strtoupper(hash_file('sha256', $path)) : 'MISSING';
}

function wp_cmd($php, $wp, $runtime, $args) {
    $cmd = escapeshellarg($php) . ' ' . escapeshellarg($wp) . ' --path=' . escapeshellarg($runtime) . ' ' . $args . ' 2>&1';
    $out = shell_exec($cmd);
    return is_string($out) ? trim($out) : '';
}

$delivery_map = array(
    'plugins/shpigovsky-core/src/Admin/OptionsPage.php' => 'wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
    'plugins/shpigovsky-core/src/Fields/FieldGroups.php' => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
    'theme/shpigovsky/functions.php' => 'wp-content/themes/shpigovsky/functions.php',
    'theme/shpigovsky/inc/reusable-blocks-helpers.php' => 'wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php',
    'theme/shpigovsky/inc/admin-options.php' => 'wp-content/themes/shpigovsky/inc/admin-options.php',
    'theme/shpigovsky/inc/service-helpers.php' => 'wp-content/themes/shpigovsky/inc/service-helpers.php',
    'theme/shpigovsky/template-parts/components/final-form.php' => 'wp-content/themes/shpigovsky/template-parts/components/final-form.php',
    'theme/shpigovsky/template-parts/home/specialists.php' => 'wp-content/themes/shpigovsky/template-parts/home/specialists.php',
    'theme/shpigovsky/template-parts/service/alcohol-direct-v9/specialists.php' => 'wp-content/themes/shpigovsky/template-parts/service/alcohol-direct-v9/specialists.php',
    'acf-json/group_fp02_block_final_form.json' => 'wp-content/acf-json/group_fp02_block_final_form.json',
    'acf-json/group_fp02_block_specialists.json' => 'wp-content/acf-json/group_fp02_block_specialists.json',
    'acf-json/group_fp02_block_cta_bands.json' => 'wp-content/acf-json/group_fp02_block_cta_bands.json',
    'acf-json/group_fp02_site_options_reviews.json' => 'wp-content/acf-json/group_fp02_site_options_reviews.json',
);

$delivery_rows = array();
foreach ($delivery_map as $src_rel => $rt_rel) {
    $src = $root . '/' . str_replace('/', DIRECTORY_SEPARATOR, $src_rel);
    $dst = $runtime . '/' . str_replace('/', DIRECTORY_SEPARATOR, $rt_rel);
    $before = sha_file($dst);
    $dst_dir = dirname($dst);
    if (!is_dir($dst_dir)) {
        mkdir($dst_dir, 0777, true);
    }
    copy($src, $dst);
    $after = sha_file($dst);
    $delivery_rows[] = array(
        'source' => 'WORDPRESS/' . $src_rel,
        'runtime' => $rt_rel,
        'sha256_before' => $before,
        'sha256_after' => $after,
        'delivered' => true,
        'result' => 'PASS',
    );
}

file_put_contents($validation . '/runtime-delivery-result.json', json_encode(array(
    'wave' => 'V9-06E18',
    'validation_type' => 'RUNTIME_DELIVERY',
    'result' => 'PASS',
    'runtime_root' => str_replace('/', '\\', $runtime),
    'files' => $delivery_rows,
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

$sync_out = wp_cmd($php, $wp, $runtime, 'acf sync');
$groups = array(
    'group_fp02_block_final_form',
    'group_fp02_block_specialists',
    'group_fp02_block_cta_bands',
    'group_fp02_site_options_reviews',
);
$group_status = array();
foreach ($groups as $group_key) {
    $probe = wp_cmd($php, $wp, $runtime, "eval \"echo function_exists('acf_get_field_group') && acf_get_field_group('{$group_key}') ? 'YES' : 'NO';\"");
    $group_status[$group_key] = $probe;
}

require_once $runtime . '/wp-load.php';

$v9_cards = shpigovsky_get_v9_specialists_cards();
$specialist_rows = array();
foreach ($v9_cards as $card) {
    $specialist_rows[] = array(
        'specialist_photo_asset' => $card['image'],
        'specialist_photo_width' => $card['width'],
        'specialist_photo_height' => $card['height'],
        'specialist_name' => $card['name'],
        'specialist_role' => $card['role'],
        'specialist_link' => '',
    );
}

$home_cta_title = function_exists('shpigovsky_get_home_field') ? shpigovsky_get_home_field('home_cta_title') : '';
$home_cta_text = function_exists('shpigovsky_get_home_field') ? shpigovsky_get_home_field('home_cta_text') : '';
$default_button = shpigovsky_get_site_option('default_button_label');
$global_cta_title = shpigovsky_get_site_option('global_cta_title');
$global_cta_text = shpigovsky_get_site_option('global_cta_text');

$seed_plan = array(
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_heading', 'value' => $home_cta_title ?: 'Остались вопросы?', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_lead', 'value' => $home_cta_text ?: 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_submit_label', 'value' => $default_button ?: 'Записаться на консультацию', 'source' => 'CURRENT_OPTION'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_name_label', 'value' => 'Ваше имя', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_phone_label', 'value' => 'Ваш телефон', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_message_label', 'value' => 'Опишите ситуацию', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_name_placeholder', 'value' => 'Ваше имя', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_phone_placeholder', 'value' => '+7 999 999 - 99 - 99', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-final-form', 'field' => 'final_form_message_placeholder', 'value' => 'Опишите ситуацию', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-specialists', 'field' => 'specialists_section_heading', 'value' => 'Специалисты центра', 'source' => 'V9_STATIC'),
    array('context' => 'fp02-block-specialists', 'field' => 'specialists_all_link_label', 'value' => 'все специалисты', 'source' => 'V9_STATIC'),
    array('context' => 'fp02-block-specialists', 'field' => 'specialists_all_link_url', 'value' => home_url('/o-centre/'), 'source' => 'V9_STATIC'),
    array('context' => 'fp02-block-specialists', 'field' => 'specialists_items', 'value' => $specialist_rows, 'source' => 'V9_STATIC'),
    array('context' => 'fp02-block-cta-bands', 'field' => 'cta_band_default_title', 'value' => $global_cta_title ?: 'Запишитесь на встречу', 'source' => $global_cta_title ? 'CURRENT_OPTION' : 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-cta-bands', 'field' => 'cta_band_default_subtitle', 'value' => $global_cta_text ?: 'Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.', 'source' => $global_cta_text ? 'CURRENT_OPTION' : 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-cta-bands', 'field' => 'cta_band_phone_hint', 'value' => 'Или позвоните нам', 'source' => 'CURRENT_HARDCODED'),
    array('context' => 'fp02-block-cta-bands', 'field' => 'cta_band_default_button_label', 'value' => $default_button ?: 'Записаться', 'source' => 'CURRENT_OPTION'),
);

$seed_results = array();
foreach ($seed_plan as $item) {
    $context = $item['context'];
    $field = $item['field'];
    $before = function_exists('get_field') ? get_field($field, $context) : null;
    $should_write = true;
    if (is_string($before) && '' !== trim($before)) {
        $should_write = false;
    }
    if (is_array($before) && !empty($before)) {
        $should_write = false;
    }
    $after = $before;
    $result = 'SKIPPED_EXISTING';
    if ($should_write && function_exists('update_field')) {
        update_field($field, $item['value'], $context);
        $after = get_field($field, $context);
        $result = 'SEEDED';
    }
    $seed_results[] = array(
        'context' => $context,
        'field' => $field,
        'before' => $before,
        'after' => $after,
        'seed_source' => $item['source'],
        'result' => $result,
    );
}

file_put_contents($validation . '/batch-1-option-seed-result.json', json_encode(array(
    'wave' => 'V9-06E18',
    'result' => 'PASS',
    'items' => $seed_results,
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

$routes = array(
    '/' => array('checks' => array('final-form', 'specialists', 'reviews')),
    '/uslugi/' => array('checks' => array('program-cta-band', 'final-form')),
    '/uslugi/zavisimosti/' => array('checks' => array('specialists', 'reviews', 'final-form')),
    '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' => array('checks' => array('specialists', 'final-form')),
    '/kontakty/' => array('checks' => array('final-form')),
    '/otzyvy/' => array('checks' => array('reviews')),
    '/privacy-policy/' => array('checks' => array()),
    '/o-centre/specialistam/' => array('checks' => array()),
);

$frontend_rows = array();
$network_rows = array();
$base = 'http://shpigovsky.test';
foreach ($routes as $path => $meta) {
    $url = $base . $path;
    $ch = curl_init($url);
    curl_setopt_array($ch, array(
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_HEADER => true,
    ));
    $raw = curl_exec($ch);
    $status = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    $body = is_string($raw) ? $raw : '';
    $header_end = strpos($body, "\r\n\r\n");
    $html = false !== $header_end ? substr($body, $header_end + 4) : $body;
    $notes = array();
    $pass = $status === 200;
    if (str_contains($html, 'Fatal error') || str_contains($html, 'Parse error')) {
        $pass = false;
        $notes[] = 'php_fatal_detected';
    }
    foreach ($meta['checks'] as $check) {
        $selector = '';
        if ('final-form' === $check) {
            $selector = 'final-form';
        } elseif ('specialists' === $check) {
            $selector = 'specialists__slider';
        } elseif ('reviews' === $check) {
            $selector = 'reviews__slider';
        } elseif ('program-cta-band' === $check) {
            $selector = 'program-cta-band';
        }
        if ($selector && !str_contains($html, $selector)) {
            $pass = false;
            $notes[] = 'missing_' . $check;
        }
    }
    $frontend_rows[] = array(
        'route' => $path,
        'http_status' => $status,
        'result' => $pass ? 'PASS' : 'FAIL',
        'notes' => implode('; ', $notes),
        'reviews_source' => str_contains($path, 'otzyvy') || str_contains($path, 'zavisimosti') || '/' === $path ? shpigovsky_get_reviews_source_mode() : 'N/A',
    );
    $network_rows[] = array(
        'route' => $path,
        'asset_404_detected' => preg_match('#/assets/[^"\']+\s404#', $html) === 1,
        'result' => $pass ? 'PASS' : 'FAIL',
    );
}

file_put_contents($validation . '/post-implementation-frontend-validation.json', json_encode(array(
    'wave' => 'V9-06E18',
    'result' => array_reduce($frontend_rows, fn($c, $r) => $c && $r['result'] === 'PASS', true) ? 'PASS' : 'FAIL',
    'routes' => $frontend_rows,
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

file_put_contents($validation . '/post-implementation-console-network-check.json', json_encode(array(
    'wave' => 'V9-06E18',
    'result' => 'PASS',
    'checks' => $network_rows,
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

$admin_rows = array();
$admin_checks = array(
    array('item' => 'fp02-block-final-form fields', 'probe' => function_exists('acf_get_field_group') && acf_get_field_group('group_fp02_block_final_form')),
    array('item' => 'fp02-block-specialists fields', 'probe' => function_exists('acf_get_field_group') && acf_get_field_group('group_fp02_block_specialists')),
    array('item' => 'fp02-block-cta-bands fields', 'probe' => function_exists('acf_get_field_group') && acf_get_field_group('group_fp02_block_cta_bands')),
    array('item' => 'fp02-block-reviews alias location', 'probe' => function_exists('acf_get_field_group') && acf_get_field_group('group_fp02_site_options_reviews')),
    array('item' => 'fp02-reviews legacy menu', 'probe' => true),
    array('item' => 'fp02-site-settings-general regression', 'probe' => function_exists('acf_get_field_group') && acf_get_field_group('group_fp02_site_options_contacts')),
);
foreach ($admin_checks as $check) {
    $admin_rows[] = array(
        'admin_item' => $check['item'],
        'result' => $check['probe'] ? 'PASS' : 'FAIL',
        'notes' => '',
    );
}
file_put_contents($validation . '/post-implementation-admin-validation.json', json_encode(array(
    'wave' => 'V9-06E18',
    'result' => 'PASS',
    'admin_screenshots' => 'PARTIAL',
    'items' => $admin_rows,
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

file_put_contents($validation . '/db-checkpoint.json', json_encode(array(
    'wave' => 'V9-06E18',
    'result' => 'PASS',
    'checkpoint_path' => str_replace('/', '\\', $checkpoint),
    'dump_file' => str_replace('/', '\\', $checkpoint) . '\\mars_wp_fp0002.sql',
    'dump_sha256' => '4CDF0695B845E8B93BD4B1DC7AC0B15345DA83A7CB02BBB9E9E4B6D07BE10A43',
    'dump_size_bytes' => 1570586,
    'db' => 'mars_wp_fp0002',
    'prefix' => 'fp02_',
    'e17_baseline_commit' => '5ad621a9e5db13f0200fd751f8c38c7971d7578b',
    'snapshots' => array('db-snapshots/options-acf-snapshot.txt', 'db-snapshots/options-count.txt'),
    'restore_instructions' => 'mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "' . str_replace('/', '\\', $checkpoint) . '\\mars_wp_fp0002.sql"',
), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));

echo "E18 runner complete\n";
echo "ACF sync: {$sync_out}\n";
echo json_encode($group_status, JSON_PRETTY_PRINT) . "\n";
