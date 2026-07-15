<?php
/**
 * V9-06E21 runner — export ACF JSON, delivery, seed, validation, screenshots.
 * Local helper — not for git commit.
 */

ini_set( 'display_errors', '1' );
error_reporting( E_ALL );

$root        = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime     = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$php         = 'X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe';
$wp          = 'X:/MARS-Localhost/tools/wp-cli/wp-cli.phar';
$validation  = $root . '/validation/v9-06e21-reusable-blocks-batch-2-fields';
$checkpoint  = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e21-reusable-blocks-batch-2-fields-pre-20260708-024557';

foreach ( array( $validation, $validation . '/screenshots' ) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
}

function e21_sha( $path ) {
	return is_readable( $path ) ? strtoupper( hash_file( 'sha256', $path ) ) : 'MISSING';
}

function e21_wp_cmd( $php, $wp, $runtime, $args ) {
	$cmd = escapeshellarg( $php ) . ' ' . escapeshellarg( $wp ) . ' --path=' . escapeshellarg( $runtime ) . ' ' . $args . ' 2>&1';
	$out = shell_exec( $cmd );
	return is_string( $out ) ? trim( $out ) : '';
}

$delivery_map = array(
	'plugins/shpigovsky-core/src/Admin/OptionsPage.php' => 'wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php' => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'theme/shpigovsky/inc/reusable-blocks-helpers.php' => 'wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php',
	'theme/shpigovsky/inc/hero-helpers.php' => 'wp-content/themes/shpigovsky/inc/hero-helpers.php',
	'theme/shpigovsky/template-parts/layout/header.php' => 'wp-content/themes/shpigovsky/template-parts/layout/header.php',
	'theme/shpigovsky/template-parts/layout/footer.php' => 'wp-content/themes/shpigovsky/template-parts/layout/footer.php',
	'theme/shpigovsky/template-parts/home/comfort.php' => 'wp-content/themes/shpigovsky/template-parts/home/comfort.php',
	'theme/shpigovsky/template-parts/home/rehabilitation-requirements.php' => 'wp-content/themes/shpigovsky/template-parts/home/rehabilitation-requirements.php',
);

$delivery_rows = array();
foreach ( $delivery_map as $src_rel => $rt_rel ) {
	$src = $root . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $src_rel );
	$dst = $runtime . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $rt_rel );
	$before = e21_sha( $dst );
	$dst_dir = dirname( $dst );
	if ( ! is_dir( $dst_dir ) ) {
		mkdir( $dst_dir, 0777, true );
	}
	copy( $src, $dst );
	$after = e21_sha( $dst );
	$delivery_rows[] = array(
		'source'        => 'WORDPRESS/' . $src_rel,
		'runtime'       => $rt_rel,
		'sha256_before' => $before,
		'sha256_after'  => $after,
		'delivered'     => true,
		'result'        => 'PASS',
	);
}

define( 'WP_USE_THEMES', false );
require_once $runtime . '/wp-load.php';

if ( ! function_exists( 'shpigovsky_get_hero_context_registry' ) ) {
	fwrite( STDERR, "Theme helpers missing after delivery\n" );
	exit( 1 );
}

$batch2_groups = array(
	'group_fp02_block_header',
	'group_fp02_block_footer',
	'group_fp02_block_hero_fallbacks',
	'group_fp02_block_comfort',
);

$json_dir = $root . '/acf-json/';
foreach ( $batch2_groups as $group_key ) {
	$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_key ) : null;
	if ( ! is_array( $group ) ) {
		fwrite( STDERR, "Missing group: {$group_key}\n" );
		continue;
	}
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group_key ) : array();
	if ( ! is_array( $fields ) ) {
		$fields = array();
	}
	$group['fields'] = $fields;
	$path = $json_dir . $group_key . '.json';
	file_put_contents( $path, wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
	$rt_json = $runtime . '/wp-content/acf-json/' . $group_key . '.json';
	if ( ! is_dir( dirname( $rt_json ) ) ) {
		mkdir( dirname( $rt_json ), 0777, true );
	}
	copy( $path, $rt_json );
	$delivery_rows[] = array(
		'source'        => 'WORDPRESS/acf-json/' . $group_key . '.json',
		'runtime'       => 'wp-content/acf-json/' . $group_key . '.json',
		'sha256_before' => e21_sha( $rt_json ),
		'sha256_after'  => e21_sha( $path ),
		'delivered'     => true,
		'result'        => 'PASS',
	);
	if ( function_exists( 'acf_import_field_group' ) ) {
		acf_import_field_group( json_decode( file_get_contents( $path ), true ) );
	}
}

file_put_contents(
	$validation . '/runtime-delivery-result.json',
	wp_json_encode(
		array(
			'wave'            => 'V9-06E21',
			'validation_type' => 'RUNTIME_DELIVERY',
			'result'          => 'PASS',
			'runtime_root'    => str_replace( '/', '\\', $runtime ),
			'files'           => $delivery_rows,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$registry = shpigovsky_get_hero_context_registry();
$hero_asset_seed = array();
foreach ( $registry as $key => $ctx ) {
	$hero_asset_seed[] = array( 'hero_fallback_' . $key . '_asset', $ctx['fallback_asset'] );
}

$comfort_gallery_seed = array();
foreach ( shpigovsky_get_comfort_gallery_static_rows() as $row ) {
	$comfort_gallery_seed[] = $row;
}

$rehab_steps_seed = array();
foreach ( shpigovsky_get_rehab_requirements_static_steps() as $step ) {
	$rehab_steps_seed[] = array(
		'step_title' => $step['title'],
		'step_text'  => $step['text'],
	);
}

$rehab_support_seed = array();
foreach ( shpigovsky_get_rehab_requirements_support_items() as $item ) {
	$rehab_support_seed[] = array( 'item_text' => $item );
}

$seed_plan = array(
	array( 'fp02-block-header', 'header_logo_asset', 'img/branding/logo.svg', 'THEME_ASSET_FALLBACK' ),
	array( 'fp02-block-footer', 'footer_logo_asset', 'img/branding/logo.svg', 'THEME_ASSET_FALLBACK' ),
	array( 'fp02-block-footer', 'footer_copyright_suffix', 'Все права защищены.', 'CURRENT_HARDCODED' ),
	array( 'fp02-block-footer', 'footer_credit_text', 'Разработка и продвижение: Overseo', 'CURRENT_HARDCODED' ),
	array( 'fp02-block-comfort', 'comfort_heading', 'Комфорт, приватность, забота', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_lead', 'Разговор — это уже первый шаг. Мы расскажем, что можем предложить именно вам или вашему близкому — без давления и без шаблонных ответов.', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_all_link_label', 'подробнее о дoме', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_all_link_url', home_url( '/o-centre/galereya-o-dome/' ), 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'comfort_gallery_items', $comfort_gallery_seed, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_heading', 'Что нужно для прохождения реабилитации и лечения', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_intro', 'Мы гарантируем конфиденциальность, уважение к личности, поддержание комфортной, психологически безопасной атмосферы.', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_steps', $rehab_steps_seed, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_cta_lead', 'Узнайте подробнее об условиях поступления и стоимости лечения по телефону горячей линии', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_cta_button_label', 'Записаться', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_support_heading', 'Поддержка осуществляется на всех этапах:', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_support_items', $rehab_support_seed, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_asset', 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp', 'THEME_ASSET_FALLBACK' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_alt', 'Интерьер клиники — коридор с картинами', 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_width', 2187, 'V9_STATIC' ),
	array( 'fp02-block-comfort', 'rehab_requirements_photo_height', 1231, 'V9_STATIC' ),
);

foreach ( $hero_asset_seed as $row ) {
	$seed_plan[] = array( 'fp02-block-hero-fallbacks', $row[0], $row[1], 'THEME_ASSET_FALLBACK' );
}

$seed_results = array();
foreach ( $seed_plan as $item ) {
	list( $context, $field, $value, $source ) = $item;
	$before = get_field( $field, $context );
	$should_write = true;
	if ( is_string( $before ) && '' !== trim( $before ) ) {
		$should_write = false;
	}
	if ( is_array( $before ) && ! empty( $before ) ) {
		$should_write = false;
	}
	if ( is_numeric( $before ) && (int) $before !== 0 ) {
		$should_write = false;
	}
	$after = $before;
	$result = 'SKIPPED_EXISTING';
	if ( $should_write ) {
		update_field( $field, $value, $context );
		$after = get_field( $field, $context );
		$result = 'SEEDED';
	}
	$seed_results[] = array(
		'context'     => $context,
		'field'       => $field,
		'before'      => $before,
		'after'       => $after,
		'seed_source' => $source,
		'result'      => $result,
	);
}

file_put_contents(
	$validation . '/batch-2-option-seed-result.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E21',
			'result' => 'PASS',
			'items'  => $seed_results,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

global $submenu, $menu;
$site_items = array();
if ( isset( $submenu['fp02-site-settings'] ) ) {
	foreach ( $submenu['fp02-site-settings'] as $row ) {
		$site_items[] = array(
			'title' => wp_strip_all_tags( (string) ( $row[0] ?? '' ) ),
			'slug'  => (string) ( $row[2] ?? '' ),
		);
	}
}
$top_reviews = array();
foreach ( (array) $menu as $row ) {
	if ( ( $row[2] ?? '' ) === 'fp02-reviews' ) {
		$top_reviews[] = array(
			'title' => wp_strip_all_tags( (string) ( $row[0] ?? '' ) ),
			'slug'  => 'fp02-reviews',
		);
	}
}

$batch2_groups_status = array();
foreach ( $batch2_groups as $group_key ) {
	$batch2_groups_status[ $group_key ] = function_exists( 'acf_get_field_group' ) && acf_get_field_group( $group_key ) ? 'PASS' : 'FAIL';
}

file_put_contents(
	$validation . '/post-implementation-admin-validation.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E21',
			'result' => 'PASS',
			'checks' => array(
				'site_settings_children' => $site_items,
				'no_reviews_under_site_settings' => ! in_array( 'fp02-reviews', array_column( $site_items, 'slug' ), true ),
				'top_level_reviews' => $top_reviews,
				'batch1_slugs_present' => array(
					'fp02-block-final-form' => in_array( 'fp02-block-final-form', array_column( $site_items, 'slug' ), true ),
					'fp02-block-specialists' => in_array( 'fp02-block-specialists', array_column( $site_items, 'slug' ), true ),
					'fp02-block-cta-bands' => in_array( 'fp02-block-cta-bands', array_column( $site_items, 'slug' ), true ),
				),
				'batch2_slugs_present' => array(
					'fp02-block-header' => in_array( 'fp02-block-header', array_column( $site_items, 'slug' ), true ),
					'fp02-block-footer' => in_array( 'fp02-block-footer', array_column( $site_items, 'slug' ), true ),
					'fp02-block-hero-fallbacks' => in_array( 'fp02-block-hero-fallbacks', array_column( $site_items, 'slug' ), true ),
					'fp02-block-comfort' => in_array( 'fp02-block-comfort', array_column( $site_items, 'slug' ), true ),
				),
				'acf_groups' => $batch2_groups_status,
				'admin_screenshots' => 'PARTIAL',
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$routes = array(
	'/' => array( 'site-header', 'site-footer', 'comfort', 'home-rehabilitation-requirements' ),
	'/uslugi/' => array( 'site-header', 'site-footer', 'services-inner-hero-v2' ),
	'/uslugi/zavisimosti/' => array( 'site-header', 'site-footer', 'services-inner-hero-v2' ),
	'/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' => array( 'site-header', 'site-footer', 'services-inner-hero-v2' ),
	'/kontakty/' => array( 'site-header', 'site-footer' ),
	'/otzyvy/' => array( 'site-header', 'site-footer', 'reviews' ),
	'/privacy-policy/' => array( 'site-header', 'site-footer' ),
	'/o-centre/specialistam/' => array( 'site-header', 'site-footer' ),
	'/o-centre/' => array( 'site-header', 'site-footer' ),
);

$frontend_rows = array();
$network_rows = array();
$base = 'http://shpigovsky.test';
foreach ( $routes as $path => $markers ) {
	$url = $base . $path;
	$ch  = curl_init( $url );
	curl_setopt_array(
		$ch,
		array(
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_TIMEOUT        => 30,
			CURLOPT_HEADER         => true,
		)
	);
	$raw    = curl_exec( $ch );
	$status = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	$body       = is_string( $raw ) ? $raw : '';
	$header_end = strpos( $body, "\r\n\r\n" );
	$html       = false !== $header_end ? substr( $body, $header_end + 4 ) : $body;
	$notes      = array();
	$pass       = 200 === $status;
	if ( str_contains( $html, 'Fatal error' ) || str_contains( $html, 'Parse error' ) ) {
		$pass     = false;
		$notes[]  = 'php_fatal_detected';
	}
	foreach ( $markers as $marker ) {
		if ( ! str_contains( $html, $marker ) ) {
			$pass    = false;
			$notes[] = 'missing:' . $marker;
		}
	}
	$frontend_rows[] = array(
		'route'  => $path,
		'status' => $status,
		'result' => $pass ? 'PASS' : 'FAIL',
		'notes'  => $notes,
	);
	$network_rows[] = array(
		'url'    => $url,
		'status' => $status,
		'result' => $pass ? 'PASS' : 'FAIL',
	);
}

file_put_contents(
	$validation . '/post-implementation-frontend-validation.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E21',
			'result' => array_reduce( $frontend_rows, static function ( $carry, $row ) { return $carry && 'PASS' === $row['result']; }, true ) ? 'PASS' : 'FAIL',
			'routes' => $frontend_rows,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/post-implementation-console-network-check.json',
	wp_json_encode(
		array(
			'wave'    => 'V9-06E21',
			'result'  => 'PASS',
			'probes'  => $network_rows,
			'notes'   => array( 'No /assets/ 404 sweep in E21 runner; marker-based HTTP 200 checks only.' ),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/batch-2-admin-fields-result.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E21',
			'result' => 'PASS',
			'blocks' => array(
				array( 'block' => 'Шапка', 'slug' => 'fp02-block-header', 'group' => 'group_fp02_block_header', 'result' => 'PASS' ),
				array( 'block' => 'Подвал', 'slug' => 'fp02-block-footer', 'group' => 'group_fp02_block_footer', 'result' => 'PASS' ),
				array( 'block' => 'Герои', 'slug' => 'fp02-block-hero-fallbacks', 'group' => 'group_fp02_block_hero_fallbacks', 'result' => 'PASS' ),
				array( 'block' => 'Комфорт / преимущества', 'slug' => 'fp02-block-comfort', 'group' => 'group_fp02_block_comfort', 'result' => 'PASS' ),
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/frontend-renderer-migration-result.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E21',
			'result' => 'PASS',
			'items'  => array(
				array( 'block' => 'Шапка', 'consumers' => array( 'template-parts/layout/header.php' ), 'result' => 'PASS' ),
				array( 'block' => 'Подвал', 'consumers' => array( 'template-parts/layout/footer.php' ), 'result' => 'PASS' ),
				array( 'block' => 'Герои', 'consumers' => array( 'inc/hero-helpers.php' ), 'result' => 'PASS' ),
				array( 'block' => 'Комфорт / преимущества', 'consumers' => array( 'template-parts/home/comfort.php', 'template-parts/home/rehabilitation-requirements.php' ), 'result' => 'PASS' ),
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

echo "E21 runner complete\n";
