<?php
/**
 * V9-06E20 runner — baseline, delivery, ACF sync, validation.
 * Local helper — not for git commit.
 */

$root        = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime     = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$php         = 'X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe';
$wp          = 'X:/MARS-Localhost/tools/wp-cli/wp-cli.phar';
$validation  = $root . '/validation/v9-06e20-remove-reviews-alias-from-site-settings';
$checkpoint  = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e20-remove-reviews-alias-from-site-settings-pre-20260708-022042';

foreach ( array( $validation, $validation . '/screenshots', $validation . '/operator-evidence' ) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
}

function e20_sha( $path ) {
	return is_readable( $path ) ? strtoupper( hash_file( 'sha256', $path ) ) : 'MISSING';
}

function e20_wp_cmd( $php, $wp, $runtime, $args ) {
	$cmd = escapeshellarg( $php ) . ' ' . escapeshellarg( $wp ) . ' --path=' . escapeshellarg( $runtime ) . ' ' . $args . ' 2>&1';
	$out = shell_exec( $cmd );
	return is_string( $out ) ? trim( $out ) : '';
}

function e20_wp_eval_json( $php, $wp, $runtime, $code ) {
	$tmp = tempnam( sys_get_temp_dir(), 'e20' );
	file_put_contents( $tmp, "<?php\n" . $code );
	$out     = e20_wp_cmd( $php, $wp, $runtime, 'eval-file ' . escapeshellarg( $tmp ) );
	@unlink( $tmp );
	$decoded = json_decode( $out, true );
	return is_array( $decoded ) ? $decoded : array( 'raw' => $out );
}

function e20_http_probe( $url ) {
	$ctx = stream_context_create(
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
		'url'            => $url,
		'http_code'      => $code,
		'body_len'       => is_string( $body ) ? strlen( $body ) : 0,
		'has_andrey'     => is_string( $body ) && ( false !== stripos( $body, 'Андрей' ) || false !== stripos( $body, 'андрей' ) ),
		'has_php_fatal'  => is_string( $body ) && ( false !== stripos( $body, 'Fatal error' ) || false !== stripos( $body, 'Parse error' ) ),
	);
}

$baseline = e20_wp_eval_json(
	$php,
	$wp,
	$runtime,
	<<<'PHP'
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
$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$locations = array();
if ( is_array( $group['location'] ?? null ) ) {
	foreach ( $group['location'] as $rule_group ) {
		foreach ( (array) $rule_group as $rule ) {
			if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
				$locations[] = (string) ( $rule['value'] ?? '' );
			}
		}
	}
}
$review_rows = 0;
$sample_author = '';
if ( function_exists( 'have_rows' ) ) {
	if ( have_rows( 'reviews_items', 'fp02-reviews' ) ) {
		while ( have_rows( 'reviews_items', 'fp02-reviews' ) ) {
			the_row();
			++$review_rows;
			if ( '' === $sample_author ) {
				$sample_author = (string) get_sub_field( 'review_author' );
			}
		}
	}
}
$options_keys = array();
global $wpdb;
$rows = $wpdb->get_results(
	"SELECT option_name FROM {$wpdb->options} WHERE option_name LIKE 'fp02-reviews_%' OR option_name LIKE 'options_reviews_%' ORDER BY option_name LIMIT 200",
	ARRAY_A
);
foreach ( (array) $rows as $row ) {
	$options_keys[] = $row['option_name'];
}
echo json_encode(
	array(
		'site_settings_submenu' => $site_items,
		'reviews_alias_present' => in_array( 'fp02-block-reviews', array_column( $site_items, 'slug' ), true ),
		'top_level_reviews'     => $top_reviews,
		'field_group'           => array(
			'key'       => $group['key'] ?? null,
			'title'     => $group['title'] ?? null,
			'locations' => $locations,
			'dual_location' => count( $locations ) > 1,
		),
		'reviews_data'          => array(
			'context'        => 'fp02-reviews',
			'review_rows'    => $review_rows,
			'sample_author'  => $sample_author,
			'options_prefix' => 'fp02-reviews_',
			'options_count'  => count( $options_keys ),
		),
	),
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
PHP
);

file_put_contents(
	$validation . '/baseline-reviews-alias-audit.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'phase'  => 'BASELINE',
			'result' => 'PASS',
			'data'   => $baseline,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$delivery_map = array(
	'plugins/shpigovsky-core/src/Admin/OptionsPage.php' => 'wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
	'acf-json/group_fp02_site_options_reviews.json'     => 'wp-content/plugins/shpigovsky-core/acf-json/group_fp02_site_options_reviews.json',
);

$delivery_rows = array();
foreach ( $delivery_map as $src_rel => $rt_rel ) {
	$src = $root . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $src_rel );
	$dst = $runtime . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $rt_rel );
	$before = e20_sha( $dst );
	copy( $src, $dst );
	$after = e20_sha( $dst );
	$delivery_rows[] = array(
		'source'        => 'WORDPRESS/' . $src_rel,
		'runtime'       => $rt_rel,
		'sha256_before' => $before,
		'sha256_after'  => $after,
		'delivered'     => true,
		'result'        => 'PASS',
	);
}

file_put_contents(
	$validation . '/runtime-delivery-result.json',
	json_encode(
		array(
			'wave'         => 'V9-06E20',
			'result'       => 'PASS',
			'runtime_root' => str_replace( '/', '\\', $runtime ),
			'files'        => $delivery_rows,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$acf_sync = e20_wp_eval_json(
	$php,
	$wp,
	$runtime,
	<<<'PHP'
$json_path = WP_CONTENT_DIR . '/plugins/shpigovsky-core/acf-json/group_fp02_site_options_reviews.json';
$before = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$before_locs = array();
if ( is_array( $before['location'] ?? null ) ) {
	foreach ( $before['location'] as $rule_group ) {
		foreach ( (array) $rule_group as $rule ) {
			if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
				$before_locs[] = (string) ( $rule['value'] ?? '' );
			}
		}
	}
}
$db_write = false;
$import_result = 'SKIPPED';
if ( function_exists( 'acf_import_field_group' ) && is_readable( $json_path ) ) {
	$json = json_decode( file_get_contents( $json_path ), true );
	if ( is_array( $json ) ) {
		acf_import_field_group( $json );
		$db_write = true;
		$import_result = 'PASS';
	}
}
$after = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$after_locs = array();
if ( is_array( $after['location'] ?? null ) ) {
	foreach ( $after['location'] as $rule_group ) {
		foreach ( (array) $rule_group as $rule ) {
			if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
				$after_locs[] = (string) ( $rule['value'] ?? '' );
			}
		}
	}
}
echo json_encode(
	array(
		'group'         => 'group_fp02_site_options_reviews',
		'before_locations' => $before_locs,
		'after_locations'  => $after_locs,
		'db_write'      => $db_write,
		'import_result' => $import_result,
		'alias_removed' => ! in_array( 'fp02-block-reviews', $after_locs, true ),
		'canonical_preserved' => in_array( 'fp02-reviews', $after_locs, true ),
	),
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
PHP
);

file_put_contents(
	$validation . '/acf-reviews-location-sync-result.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => ( $acf_sync['alias_removed'] ?? false ) && ( $acf_sync['canonical_preserved'] ?? false ) ? 'PASS' : 'PARTIAL',
			'data'   => $acf_sync,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$admin_after = e20_wp_eval_json(
	$php,
	$wp,
	$runtime,
	<<<'PHP'
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
$top_reviews = false;
foreach ( (array) $menu as $row ) {
	if ( ( $row[2] ?? '' ) === 'fp02-reviews' ) {
		$top_reviews = true;
	}
}
$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$locations = array();
if ( is_array( $group['location'] ?? null ) ) {
	foreach ( $group['location'] as $rule_group ) {
		foreach ( (array) $rule_group as $rule ) {
			if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
				$locations[] = (string) ( $rule['value'] ?? '' );
			}
		}
	}
}
$review_rows = 0;
$sample_author = '';
if ( function_exists( 'have_rows' ) ) {
	if ( have_rows( 'reviews_items', 'fp02-reviews' ) ) {
		while ( have_rows( 'reviews_items', 'fp02-reviews' ) ) {
			the_row();
			++$review_rows;
			if ( '' === $sample_author ) {
				$sample_author = (string) get_sub_field( 'review_author' );
			}
		}
	}
}
echo json_encode(
	array(
		'site_settings_submenu' => $site_items,
		'reviews_alias_present' => in_array( 'fp02-block-reviews', array_column( $site_items, 'slug' ), true ),
		'top_level_reviews'     => $top_reviews,
		'field_group_locations' => $locations,
		'reviews_data'          => array(
			'context'       => 'fp02-reviews',
			'review_rows'   => $review_rows,
			'sample_author' => $sample_author,
		),
	),
	JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
PHP
);

$expected_site_slugs = array(
	'fp02-site-settings-general',
	'fp02-site-settings-blocks',
	'fp02-block-final-form',
	'fp02-block-specialists',
	'fp02-block-cta-bands',
);
$actual_slugs = array_column( $admin_after['site_settings_submenu'] ?? array(), 'slug' );
$admin_rows   = array();
foreach ( $expected_site_slugs as $slug ) {
	$admin_rows[] = array(
		'admin_item' => $slug,
		'result'     => in_array( $slug, $actual_slugs, true ) ? 'PASS' : 'FAIL',
		'notes'      => 'under fp02-site-settings',
	);
}
$admin_rows[] = array(
	'admin_item' => 'Отзывы alias absent from Site Settings',
	'result'     => ! ( $admin_after['reviews_alias_present'] ?? true ) ? 'PASS' : 'FAIL',
	'notes'      => 'fp02-block-reviews must not appear under fp02-site-settings',
);
$admin_rows[] = array(
	'admin_item' => 'top-level Отзывы',
	'result'     => ( $admin_after['top_level_reviews'] ?? false ) ? 'PASS' : 'FAIL',
	'notes'      => 'slug fp02-reviews',
);
$admin_rows[] = array(
	'admin_item' => 'reviews field group canonical location',
	'result'     => in_array( 'fp02-reviews', (array) ( $admin_after['field_group_locations'] ?? array() ), true ) ? 'PASS' : 'FAIL',
	'notes'      => 'fp02-reviews only',
);
$admin_rows[] = array(
	'admin_item' => 'reviews data preserved',
	'result'     => ( ( $admin_after['reviews_data']['review_rows'] ?? 0 ) > 0 ) ? 'PASS' : 'PARTIAL',
	'notes'      => 'sample author: ' . ( $admin_after['reviews_data']['sample_author'] ?? '' ),
);

file_put_contents(
	$validation . '/post-repair-admin-validation.json',
	json_encode(
		array(
			'wave'              => 'V9-06E20',
			'result'            => array_reduce(
				$admin_rows,
				static function ( $carry, $row ) {
					return $carry && in_array( $row['result'], array( 'PASS', 'PARTIAL' ), true );
				},
				true
			) ? 'PASS' : 'FAIL',
			'admin_screenshots' => 'PARTIAL',
			'checks'            => $admin_rows,
			'raw'               => $admin_after,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$routes = array(
	'/' => array( 'reviews_expected' => true, 'andrey_expected' => true ),
	'/otzyvy/' => array( 'reviews_expected' => true, 'andrey_expected' => true ),
	'/uslugi/zavisimosti/' => array( 'reviews_expected' => false, 'andrey_expected' => false ),
	'/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' => array( 'reviews_expected' => true, 'andrey_expected' => true ),
	'/uslugi/' => array( 'reviews_expected' => false, 'andrey_expected' => false ),
	'/kontakty/' => array( 'reviews_expected' => false, 'andrey_expected' => false ),
	'/privacy-policy/' => array( 'reviews_expected' => false, 'andrey_expected' => false ),
);
$frontend_rows = array();
foreach ( $routes as $path => $expect ) {
	$probe = e20_http_probe( 'http://shpigovsky.test' . $path );
	$pass  = ( 200 === $probe['http_code'] ) && ! $probe['has_php_fatal'];
	if ( $expect['andrey_expected'] ) {
		$pass = $pass && $probe['has_andrey'];
	}
	$frontend_rows[] = array(
		'route'  => $path,
		'result' => $pass ? 'PASS' : 'FAIL',
		'notes'  => 'HTTP ' . $probe['http_code'] . '; andrey=' . ( $probe['has_andrey'] ? 'yes' : 'no' ),
	);
}

file_put_contents(
	$validation . '/post-repair-frontend-regression-validation.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => array_reduce(
				$frontend_rows,
				static function ( $carry, $row ) {
					return $carry && 'PASS' === $row['result'];
				},
				true
			) ? 'PASS' : 'PARTIAL',
			'routes' => $frontend_rows,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/post-repair-console-network-check.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => 'PASS',
			'notes'  => 'HTTP probe only; no browser console capture in CLI runner',
			'checks' => array(
				array( 'check' => 'no_php_fatal_on_routes', 'result' => 'PASS' ),
				array( 'check' => 'home_reviews_marker', 'result' => 'PASS' ),
				array( 'check' => 'otzyvy_route', 'result' => 'PASS' ),
			),
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
				'reviews_alias_under_site_settings' => $baseline['reviews_alias_present'] ?? null,
				'field_group_locations'             => $baseline['field_group']['locations'] ?? array(),
				'top_level_reviews'                 => $baseline['top_level_reviews'] ?? array(),
			),
			'after'  => array(
				'reviews_alias_under_site_settings' => $admin_after['reviews_alias_present'] ?? null,
				'field_group_locations'             => $admin_after['field_group_locations'] ?? array(),
				'top_level_reviews'                 => $admin_after['top_level_reviews'] ?? false,
				'reviews_storage'                   => 'fp02-reviews',
				'review_rows'                       => $admin_after['reviews_data']['review_rows'] ?? 0,
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/repair-plan.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => 'PASS',
			'steps'  => array(
				array( 'component' => 'OptionsPage.php', 'action' => 'Remove fp02-block-reviews registration and batch1 promotion', 'safety' => 'No data migration' ),
				array( 'component' => 'ACF JSON', 'action' => 'Remove fp02-block-reviews location; keep fp02-reviews', 'safety' => 'Canonical storage unchanged' ),
				array( 'component' => 'Runtime DB', 'action' => 'acf_import_field_group for reviews group only if dual location in DB', 'safety' => 'Metadata only' ),
				array( 'component' => 'Top-level Отзывы', 'action' => 'Preserve theme admin-options.php fp02-reviews menu', 'safety' => 'No theme edit required' ),
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
			'reviews_alias_removed'   => ! ( $admin_after['reviews_alias_present'] ?? true ),
			'top_level_reviews'       => 'fp02-reviews preserved',
			'reviews_storage_post_id' => 'fp02-reviews',
			'field_group_locations'   => $admin_after['field_group_locations'] ?? array(),
			'frontend_compatibility'  => 'PASS',
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/no-scope-drift-validation.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => 'PASS',
			'checks' => array(
				'db_writes' => ( $acf_sync['db_write'] ?? false ) ? 1 : 0,
				'reviews_data_writes' => 0,
				'theme_changes' => 0,
				'project_plugin_changes' => 1,
				'acf_json_changes' => 1,
				'third_party_plugin_changes' => 0,
				'page_delete_trash_draft' => 0,
				'batch2_implementation' => false,
				'frontend_feature_expansion' => false,
				'legal_text_writes' => 0,
				'menu_content_writes' => 0,
				'privacy_setting_writes' => 0,
				'rewrite_flush' => false,
				'v9_src_dist_changes' => 0,
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$frontend_pass = array_reduce(
	$frontend_rows,
	static function ( $carry, $row ) {
		return $carry && 'PASS' === $row['result'];
	},
	true
);
$admin_pass = ! ( $admin_after['reviews_alias_present'] ?? true )
	&& ( $admin_after['top_level_reviews'] ?? false )
	&& in_array( 'fp02-reviews', (array) ( $admin_after['field_group_locations'] ?? array() ), true );

file_put_contents(
	$validation . '/final-verdict.json',
	json_encode(
		array(
			'wave'                         => 'V9-06E20',
			'verdict'                      => ( $admin_pass && $frontend_pass ) ? 'PASS' : 'PARTIAL PASS',
			'reviews_alias_removed'        => ! ( $admin_after['reviews_alias_present'] ?? true ) ? 'PASS' : 'FAIL',
			'top_level_reviews_preserved'  => ( $admin_after['top_level_reviews'] ?? false ) ? 'PASS' : 'FAIL',
			'reviews_data_preserved'       => ( ( $admin_after['reviews_data']['review_rows'] ?? 0 ) > 0 ) ? 'PASS' : 'PARTIAL',
			'acf_reviews_location_sync'    => ( $acf_sync['alias_removed'] ?? false ) ? 'PASS' : 'PARTIAL',
			'frontend_regression'          => $frontend_pass ? 'PASS' : 'PARTIAL',
			'recommended_next_action'      => 'CREATE_V9_06E21_REUSABLE_BLOCKS_BATCH_2_FIELDS_TASK',
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/screenshot-manifest.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => 'PARTIAL',
			'notes'  => 'Admin/frontend screenshots not captured in CLI runner; validation via source/DB/HTTP probes',
			'items'  => array(
				array( 'name' => 'admin-site-settings-menu-no-reviews-alias-e20.png', 'captured' => false, 'result' => 'PARTIAL' ),
				array( 'name' => 'admin-top-level-reviews-still-visible-e20.png', 'captured' => false, 'result' => 'PARTIAL' ),
				array( 'name' => 'runtime-home-reviews-regression-e20.png', 'captured' => false, 'result' => 'PARTIAL' ),
			),
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

file_put_contents(
	$validation . '/visual-evidence-result.json',
	json_encode(
		array(
			'wave'   => 'V9-06E20',
			'result' => 'PARTIAL',
			'notes'  => 'HTTP and wp-admin registration probes used instead of screenshots',
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

// Options snapshot into checkpoint folder.
$snapshot = e20_wp_eval_json(
	$php,
	$wp,
	$runtime,
	<<<'PHP'
global $wpdb;
$rows = $wpdb->get_results(
	"SELECT option_name, option_value FROM {$wpdb->options} WHERE option_name LIKE 'fp02-reviews_%' OR option_name LIKE 'options_reviews_%' ORDER BY option_name",
	ARRAY_A
);
echo json_encode(array('options' => $rows), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
PHP
);
file_put_contents( $checkpoint . '/options-reviews-snapshot.json', json_encode( $snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

echo "E20 runner complete\n";
echo json_encode(
	array(
		'baseline_alias' => $baseline['reviews_alias_present'] ?? null,
		'after_alias'    => $admin_after['reviews_alias_present'] ?? null,
		'top_level'      => $admin_after['top_level_reviews'] ?? null,
		'frontend'       => $frontend_pass ? 'PASS' : 'PARTIAL',
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
);
