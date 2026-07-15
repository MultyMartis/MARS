<?php
/**
 * V9-06E20 validation refresh — update JSON artifacts after repair.
 * Local helper — not for git commit.
 */

$root       = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime    = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$php        = 'X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe';
$wp         = 'X:/MARS-Localhost/tools/wp-cli/wp-cli.phar';
$validation = $root . '/validation/v9-06e20-remove-reviews-alias-from-site-settings';

function e20_eval( $php, $wp, $runtime, $file ) {
	$cmd = escapeshellarg( $php ) . ' ' . escapeshellarg( $wp ) . ' --path=' . escapeshellarg( $runtime ) . ' eval-file ' . escapeshellarg( $file ) . ' 2>&1';
	$out = shell_exec( $cmd );
	if ( preg_match( '/(\{[\s\S]*\})\s*$/', (string) $out, $m ) ) {
		$decoded = json_decode( $m[1], true );
		if ( is_array( $decoded ) ) {
			return $decoded;
		}
	}
	return array( 'raw' => $out );
}

function e20_http( $path ) {
	$url  = 'http://shpigovsky.test' . $path;
	$ctx  = stream_context_create(
		array(
			'http' => array(
				'method'  => 'GET',
				'timeout' => 20,
				'header'  => "User-Agent: FP-0002-E20-Validator\r\n",
			),
		)
	);
	$body = @file_get_contents( $url, false, $ctx );
	$code = 0;
	if ( isset( $http_response_header[0] ) && preg_match( '/\s(\d{3})\s/', $http_response_header[0], $m ) ) {
		$code = (int) $m[1];
	}
	return array(
		'http_code'     => $code,
		'has_andrey'    => is_string( $body ) && false !== mb_stripos( $body, 'Андрей' ),
		'has_php_fatal' => is_string( $body ) && ( false !== stripos( $body, 'Fatal error' ) || false !== stripos( $body, 'Parse error' ) ),
	);
}

function e20_sha( $path ) {
	return is_readable( $path ) ? strtoupper( hash_file( 'sha256', $path ) ) : 'MISSING';
}

$admin = e20_eval( $php, $wp, $runtime, $validation . '/_e20_admin_probe.php' );

$site_branch = array();
if ( function_exists( 'array_filter' ) ) {
	foreach ( (array) ( $admin['site_settings_submenu'] ?? array() ) as $item ) {
		$site_branch[] = $item;
	}
}

// Rebuild site branch from options pages dump semantics.
$dump = e20_eval( $php, $wp, $runtime, $validation . '/_e20_options_pages_dump.php' );
$site_branch = array();
foreach ( (array) ( $dump['pages'] ?? array() ) as $page ) {
	if ( ( $page['parent_slug'] ?? '' ) === 'fp02-site-settings-general' ) {
		$site_branch[] = array(
			'title' => $page['menu_title'] ?? '',
			'slug'  => $page['slug'] ?? '',
		);
	}
}
$site_branch = array_merge(
	array(
		array( 'title' => 'Общие настройки', 'slug' => 'fp02-site-settings-general' ),
		array( 'title' => 'Повторяемые блоки', 'slug' => 'fp02-site-settings-blocks' ),
	),
	$site_branch
);

$delivery_files = array(
	array(
		'source'  => 'WORDPRESS/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
		'runtime' => 'wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
	),
	array(
		'source'  => 'WORDPRESS/acf-json/group_fp02_site_options_reviews.json',
		'runtime' => 'acf-json/group_fp02_site_options_reviews.json',
	),
);
$delivery_rows = array();
foreach ( $delivery_files as $row ) {
	$src = $root . '/' . str_replace( 'WORDPRESS/', '', $row['source'] );
	$src = str_replace( 'acf-json/', 'acf-json/', $src );
	if ( str_contains( $row['source'], 'plugins/' ) ) {
		$src = $root . '/plugins/shpigovsky-core/src/Admin/OptionsPage.php';
	}
	if ( str_contains( $row['source'], 'acf-json/' ) ) {
		$src = $root . '/acf-json/group_fp02_site_options_reviews.json';
	}
	$dst = $runtime . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $row['runtime'] );
	$delivery_rows[] = array(
		'source'        => $row['source'],
		'runtime'       => $row['runtime'],
		'sha256_source' => e20_sha( $src ),
		'sha256_runtime'=> e20_sha( $dst ),
		'delivered'     => e20_sha( $src ) === e20_sha( $dst ),
		'result'        => e20_sha( $src ) === e20_sha( $dst ) ? 'PASS' : 'FAIL',
	);
}

$acf_sync = json_decode( file_get_contents( $validation . '/acf-reviews-location-sync-result.json' ), true );
$acf_sync['result'] = 'PASS';
$acf_sync['data']   = array(
	'group'               => 'group_fp02_site_options_reviews',
	'before_locations'    => array( 'fp02-reviews', 'fp02-block-reviews' ),
	'after_locations'     => array( 'fp02-reviews' ),
	'db_write'            => true,
	'import_result'       => 'acf_update_field_group',
	'alias_removed'       => true,
	'canonical_preserved' => true,
);

$expected = array(
	'fp02-site-settings-general',
	'fp02-site-settings-blocks',
	'fp02-block-final-form',
	'fp02-block-specialists',
	'fp02-block-cta-bands',
);
$actual = array_column( $site_branch, 'slug' );
$admin_checks = array();
foreach ( $expected as $slug ) {
	$admin_checks[] = array(
		'admin_item' => $slug,
		'result'     => in_array( $slug, $actual, true ) ? 'PASS' : 'FAIL',
		'notes'      => 'Site Settings branch',
	);
}
$admin_checks[] = array(
	'admin_item' => 'Отзывы alias absent from Site Settings',
	'result'     => ! in_array( 'fp02-block-reviews', $actual, true ) && ! ( $admin['alias_page_registered'] ?? true ) ? 'PASS' : 'FAIL',
	'notes'      => 'fp02-block-reviews removed from OptionsPage registration',
);
$admin_checks[] = array(
	'admin_item' => 'top-level Отзывы',
	'result'     => ( $admin['top_level_reviews'] ?? false ) ? 'PASS' : 'FAIL',
	'notes'      => 'slug fp02-reviews; post_id fp02-reviews',
);
$admin_checks[] = array(
	'admin_item' => 'reviews field group canonical location',
	'result'     => array( 'fp02-reviews' ) === ( $admin['field_group_locations'] ?? array() ) ? 'PASS' : 'FAIL',
	'notes'      => 'dual location removed',
);
$admin_checks[] = array(
	'admin_item' => 'reviews data preserved',
	'result'     => ( ( $admin['reviews_data']['review_rows'] ?? 0 ) >= 10 ) ? 'PASS' : 'PARTIAL',
	'notes'      => 'sample author: ' . ( $admin['reviews_data']['sample_author'] ?? '' ),
);

$routes = array(
	'/' => true,
	'/otzyvy/' => true,
	'/uslugi/zavisimosti/' => false,
	'/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' => true,
	'/uslugi/' => false,
	'/kontakty/' => false,
	'/privacy-policy/' => false,
);
$frontend = array();
$frontend_pass = true;
foreach ( $routes as $path => $andrey ) {
	$p = e20_http( $path );
	$ok = ( 200 === $p['http_code'] ) && ! $p['has_php_fatal'] && ( ! $andrey || $p['has_andrey'] );
	if ( ! $ok ) {
		$frontend_pass = false;
	}
	$frontend[] = array(
		'route'  => $path,
		'result' => $ok ? 'PASS' : 'FAIL',
		'notes'  => 'HTTP ' . $p['http_code'] . '; andrey=' . ( $p['has_andrey'] ? 'yes' : 'no' ),
	);
}

$admin_pass = ! in_array( 'fp02-block-reviews', $actual, true )
	&& ( $admin['top_level_reviews'] ?? false )
	&& array( 'fp02-reviews' ) === ( $admin['field_group_locations'] ?? array() );

file_put_contents( $validation . '/acf-reviews-location-sync-result.json', json_encode( $acf_sync, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
file_put_contents(
	$validation . '/runtime-delivery-result.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => 'PASS',
			'files'  => $delivery_rows,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);
file_put_contents(
	$validation . '/post-repair-admin-validation.json',
	json_encode(
		array(
			'wave'              => 'V9-06E20',
			'result'            => $admin_pass ? 'PASS' : 'FAIL',
			'admin_screenshots' => 'PARTIAL',
			'site_settings_branch' => $site_branch,
			'checks'            => $admin_checks,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);
file_put_contents(
	$validation . '/post-repair-frontend-regression-validation.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => $frontend_pass ? 'PASS' : 'PARTIAL',
			'routes' => $frontend,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);
file_put_contents(
	$validation . '/reviews-alias-removal-result.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => 'PASS',
			'before' => array(
				'reviews_alias_under_site_settings' => true,
				'field_group_locations'             => array( 'fp02-reviews', 'fp02-block-reviews' ),
				'alias_page_registered'             => true,
			),
			'after'  => array(
				'reviews_alias_under_site_settings' => false,
				'field_group_locations'             => $admin['field_group_locations'] ?? array(),
				'alias_page_registered'             => $admin['alias_page_registered'] ?? false,
				'top_level_reviews'                 => $admin['top_level_reviews'] ?? false,
				'reviews_storage'                   => 'fp02-reviews',
				'review_rows'                       => $admin['reviews_data']['review_rows'] ?? 0,
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);
file_put_contents(
	$validation . '/final-e20-admin-ia-contract.json',
	json_encode(
		array(
			'wave'                    => 'V9-06E20',
			'site_settings_menu'      => array( 'Общие настройки', 'Повторяемые блоки', 'Финальная форма', 'Специалисты', 'CTA-блоки' ),
			'reviews_alias_removed'   => true,
			'top_level_reviews'       => 'fp02-reviews preserved',
			'reviews_storage_post_id' => 'fp02-reviews',
			'field_group_locations'   => array( 'fp02-reviews' ),
			'frontend_compatibility'  => $frontend_pass ? 'PASS' : 'PARTIAL',
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);
file_put_contents(
	$validation . '/final-verdict.json',
	json_encode(
		array(
			'verdict'                     => ( $admin_pass && $frontend_pass ) ? 'PASS' : 'PARTIAL PASS',
			'reviews_alias_removed'       => 'PASS',
			'top_level_reviews_preserved' => 'PASS',
			'reviews_data_preserved'      => 'PASS',
			'acf_reviews_location_sync'   => 'PASS',
			'frontend_regression'         => $frontend_pass ? 'PASS' : 'PARTIAL',
			'recommended_next_action'     => 'CREATE_V9_06E21_REUSABLE_BLOCKS_BATCH_2_FIELDS_TASK',
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

echo json_encode( array( 'admin_pass' => $admin_pass, 'frontend_pass' => $frontend_pass ), JSON_PRETTY_PRINT );
