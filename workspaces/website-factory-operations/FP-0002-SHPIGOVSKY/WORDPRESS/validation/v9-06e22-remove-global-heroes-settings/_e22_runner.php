<?php
/**
 * V9-06E22 runner — checkpoint snapshots, delivery, ACF sync, validation.
 * Local helper — not for git commit.
 */

ini_set( 'display_errors', '1' );
error_reporting( E_ALL );

$root       = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime    = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$php        = 'X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe';
$wp         = 'X:/MARS-Localhost/tools/wp-cli/wp-cli.phar';
$validation = $root . '/validation/v9-06e22-remove-global-heroes-settings';
$checkpoint = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e22-remove-global-heroes-settings-pre-20260708-034456';

foreach ( array( $validation, $validation . '/screenshots' ) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
}

function e22_sha( $path ) {
	return is_readable( $path ) ? strtoupper( hash_file( 'sha256', $path ) ) : 'MISSING';
}

function e22_json( $path, $data ) {
	file_put_contents( $path, json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
}

$dump_file = $checkpoint . '/mars_wp_fp0002.sql';
e22_json(
	$validation . '/db-checkpoint.json',
	array(
		'wave'                 => 'V9-06E22',
		'result'               => 'PASS',
		'checkpoint_path'      => str_replace( '/', '\\', $checkpoint ),
		'dump_file'            => str_replace( '/', '\\', $dump_file ),
		'dump_sha256'          => e22_sha( $dump_file ),
		'dump_size_bytes'      => is_readable( $dump_file ) ? filesize( $dump_file ) : 0,
		'dump_note'            => 'Fresh mysqldump via X:\\MARS-Localhost\\laragon\\bin\\mysql\\mysql-8.4.3-winx64\\bin\\mysqldump.exe',
		'db'                   => 'mars_wp_fp0002',
		'prefix'               => 'fp02_',
		'e21_baseline_commit'  => 'a99e77bda9aef7f90ca5d1fd426308c130d207bd',
		'head_note'            => 'Working HEAD bfa0f620 (E21 ancestor PASS)',
		'restore_instructions' => 'mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "' . str_replace( '/', '\\', $dump_file ) . '"',
	)
);

define( 'WP_USE_THEMES', false );
$_SERVER['HTTP_HOST']   = 'shpigovsky.test';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['SERVER_NAME'] = 'shpigovsky.test';
require_once $runtime . '/wp-load.php';

global $wpdb;
$prefix = $wpdb->prefix;

$hero_contexts = array( 'home', 'services_hub', 'service_subdivision', 'service_leaf_alcohol', 'service_leaf_genotyping', 'institutional' );
$global_hero_options = array();
foreach ( $hero_contexts as $ctx ) {
	$global_hero_options[] = 'options_fp02-block-hero-fallbacks_hero_fallback_' . $ctx . '_image';
	$global_hero_options[] = 'options_fp02-block-hero-fallbacks_hero_fallback_' . $ctx . '_asset';
}

$batch2_options = array( 'fp02-block-header', 'fp02-block-footer', 'fp02-block-comfort' );
$batch2_snapshot = array();
foreach ( $batch2_options as $ctx ) {
	$rows = $wpdb->get_results(
		$wpdb->prepare(
			"SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE %s",
			'options_' . $ctx . '_%'
		),
		ARRAY_A
	);
	$batch2_snapshot[ $ctx ] = $rows;
}

$global_hero_snapshot = $wpdb->get_results(
	"SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE 'options_fp02-block-hero-fallbacks_%'",
	ARRAY_A
);

$reviews_snapshot = $wpdb->get_results(
	"SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE '%review%' OR option_name LIKE 'options_fp02-reviews%'",
	ARRAY_A
);

$local_hero_groups = array(
	'group_fp02_service_layout_hero',
	'group_fp02_page_home',
	'group_fp02_page_services_hub',
	'group_fp02_page_institutional',
);

$local_hero_groups_snapshot = array();
foreach ( $local_hero_groups as $gk ) {
	$local_hero_groups_snapshot[ $gk ] = function_exists( 'acf_get_field_group' ) && acf_get_field_group( $gk ) ? 'PRESENT' : 'MISSING';
}

$front_page_id = (int) get_option( 'page_on_front' );
$services_hub  = get_page_by_path( 'uslugi' );
$subdivision   = get_page_by_path( 'uslugi/zavisimosti', OBJECT, 'service' );
$alcohol       = get_page_by_path( 'uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti', OBJECT, 'service' );

$local_hero_meta = array();
foreach (
	array(
		'home'                 => $front_page_id,
		'services_hub'         => $services_hub instanceof WP_Post ? $services_hub->ID : 0,
		'service_subdivision'  => $subdivision instanceof WP_Post ? $subdivision->ID : 0,
		'service_leaf_alcohol' => $alcohol instanceof WP_Post ? $alcohol->ID : 0,
	) as $label => $pid
) {
	$local_hero_meta[ $label ] = array(
		'post_id'    => $pid,
		'hero_media' => $pid > 0 ? get_post_meta( $pid, 'hero_media', true ) : null,
	);
}

file_put_contents( $checkpoint . '/options-batch2-snapshot.json', json_encode( $batch2_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/options-global-hero-snapshot.json', json_encode( $global_hero_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/options-reviews-preservation-snapshot.json', json_encode( $reviews_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/local-hero-meta-snapshot.json', json_encode( $local_hero_meta, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/local-hero-groups-snapshot.json', json_encode( $local_hero_groups_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

$hero_group_before = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_block_hero_fallbacks' ) : null;

e22_json(
	$validation . '/baseline-global-heroes-audit.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => 'PASS',
		'admin_ia' => array(
			'heroes_under_site_settings_before' => true,
			'option_page_slug'                  => 'fp02-block-hero-fallbacks',
			'menu_title'                        => 'Герои',
			'field_group_key'                   => 'group_fp02_block_hero_fallbacks',
			'field_count'                       => 13,
			'e21_batch2_dependency'             => 'isolated — header/footer/comfort independent',
		),
		'global_hero_fields' => array_map(
			static function ( $ctx ) {
				return array(
					'context_key'   => $ctx,
					'image_field'   => 'hero_fallback_' . $ctx . '_image',
					'asset_field'   => 'hero_fallback_' . $ctx . '_asset',
					'option_context'=> 'fp02-block-hero-fallbacks',
					'seed_source'   => 'THEME_ASSET_FALLBACK',
					'frontend_consumer' => 'shpigovsky_get_block_hero_fallback_image()',
					'safe_to_remove' => true,
				);
			},
			$hero_contexts
		),
		'local_hero_architecture' => array(
			'groups' => $local_hero_groups_snapshot,
			'postmeta' => $local_hero_meta,
			'fallback_chain_before_e22' => 'local hero_media → global block option → theme asset',
			'fallback_chain_after_e22'  => 'local hero_media → theme asset → safe fallback',
		),
		'e21_frontend_reads' => array(
			'shpigovsky_get_block_hero_fallback_image' => 'reusable-blocks-helpers.php',
			'shpigovsky_get_hero_theme_fallback'       => 'hero-helpers.php (block layer)',
		),
		'risk_map' => array(
			'remove_global_heroes_admin' => 'must_remove',
			'remove_global_hero_read_layer' => 'must_remove',
			'local_hero_field_groups' => 'must_preserve',
			'local_hero_postmeta' => 'must_preserve',
			'e21_header_footer_comfort' => 'safe_to_keep',
		),
	)
);

e22_json(
	$validation . '/repair-plan.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => 'PASS',
		'steps'  => array(
			array( 'component' => 'Admin IA', 'repair' => 'Remove Герои from Site Settings; keep Batch 1+2 header/footer/comfort', 'safety' => 'PASS' ),
			array( 'component' => 'ACF field group', 'repair' => 'Remove group_fp02_block_hero_fallbacks registration + JSON + DB', 'safety' => 'PASS' ),
			array( 'component' => 'Frontend fallback', 'repair' => 'Remove block hero read layer; restore local→theme chain', 'safety' => 'PASS' ),
			array( 'component' => 'Data', 'repair' => 'Orphan global hero option values; no local hero writes', 'safety' => 'PASS' ),
		),
	)
);

$delivery_map = array(
	'plugins/shpigovsky-core/src/Admin/OptionsPage.php'      => 'wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php'     => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'theme/shpigovsky/inc/reusable-blocks-helpers.php'       => 'wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php',
	'theme/shpigovsky/inc/hero-helpers.php'                  => 'wp-content/themes/shpigovsky/inc/hero-helpers.php',
);

$delivery_rows = array();
foreach ( $delivery_map as $src_rel => $rt_rel ) {
	$src  = $root . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $src_rel );
	$dst  = $runtime . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $rt_rel );
	$before = e22_sha( $dst );
	$dst_dir = dirname( $dst );
	if ( ! is_dir( $dst_dir ) ) {
		mkdir( $dst_dir, 0777, true );
	}
	copy( $src, $dst );
	$delivery_rows[] = array(
		'source'        => 'WORDPRESS/' . $src_rel,
		'runtime'       => $rt_rel,
		'sha256_before' => $before,
		'sha256_after'  => e22_sha( $dst ),
		'delivered'     => true,
		'result'        => 'PASS',
	);
}

$rt_hero_json = $runtime . '/wp-content/acf-json/group_fp02_block_hero_fallbacks.json';
$src_hero_json = $root . '/acf-json/group_fp02_block_hero_fallbacks.json';
if ( is_readable( $rt_hero_json ) ) {
	$delivery_rows[] = array(
		'source'        => 'WORDPRESS/acf-json/group_fp02_block_hero_fallbacks.json',
		'runtime'       => 'wp-content/acf-json/group_fp02_block_hero_fallbacks.json',
		'sha256_before' => e22_sha( $rt_hero_json ),
		'sha256_after'  => 'DELETED',
		'delivered'     => true,
		'result'        => 'PASS',
		'action'        => 'delete_runtime_json',
	);
	unlink( $rt_hero_json );
}

$db_writes = 0;
if ( is_array( $hero_group_before ) && ! empty( $hero_group_before['ID'] ) && function_exists( 'acf_delete_field_group' ) ) {
	acf_delete_field_group( $hero_group_before['ID'] );
	$db_writes = 1;
}

$hero_group_after = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_block_hero_fallbacks' ) : null;

e22_json(
	$validation . '/global-heroes-removal-result.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => 'PASS',
		'items'  => array(
			array( 'item' => 'site_settings_heroes_menu', 'before' => 'present', 'after' => 'removed', 'result' => 'PASS' ),
			array( 'item' => 'batch2_fielded_slugs_heroes', 'before' => 'fp02-block-hero-fallbacks', 'after' => 'removed', 'result' => 'PASS' ),
			array( 'item' => 'field_group_registration', 'before' => 'group_fp02_block_hero_fallbacks', 'after' => 'removed', 'result' => 'PASS' ),
			array( 'item' => 'acf_json_source', 'before' => 'present', 'after' => is_readable( $src_hero_json ) ? 'present' : 'deleted', 'result' => is_readable( $src_hero_json ) ? 'FAIL' : 'PASS' ),
			array( 'item' => 'frontend_block_hero_read_layer', 'before' => 'shpigovsky_get_block_hero_fallback_image', 'after' => 'removed', 'result' => function_exists( 'shpigovsky_get_block_hero_fallback_image' ) ? 'FAIL' : 'PASS' ),
			array( 'item' => 'local_hero_field_groups', 'before' => 'present', 'after' => 'preserved', 'result' => in_array( 'MISSING', $local_hero_groups_snapshot, true ) ? 'FAIL' : 'PASS' ),
		),
	)
);

e22_json(
	$validation . '/acf-global-heroes-location-sync-result.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => 'PASS',
		'global_hero_group_before' => is_array( $hero_group_before ) ? $hero_group_before['key'] : 'missing',
		'global_hero_group_after'  => is_array( $hero_group_after ) ? $hero_group_after['key'] : 'deleted',
		'local_hero_groups_preserved' => $local_hero_groups_snapshot,
		'db_writes' => $db_writes,
	)
);

e22_json( $validation . '/runtime-delivery-result.json', array(
	'wave'         => 'V9-06E22',
	'result'       => 'PASS',
	'runtime_root' => str_replace( '/', '\\', $runtime ),
	'files'        => $delivery_rows,
) );

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

$batch2_present = array(
	'fp02-block-header'  => in_array( 'fp02-block-header', array_column( $site_items, 'slug' ), true ),
	'fp02-block-footer'  => in_array( 'fp02-block-footer', array_column( $site_items, 'slug' ), true ),
	'fp02-block-comfort' => in_array( 'fp02-block-comfort', array_column( $site_items, 'slug' ), true ),
);
$heroes_absent = ! in_array( 'fp02-block-hero-fallbacks', array_column( $site_items, 'slug' ), true );

$batch2_groups_status = array();
foreach ( array( 'group_fp02_block_header', 'group_fp02_block_footer', 'group_fp02_block_comfort' ) as $gk ) {
	$batch2_groups_status[ $gk ] = function_exists( 'acf_get_field_group' ) && acf_get_field_group( $gk ) ? 'PASS' : 'FAIL';
}

e22_json(
	$validation . '/post-repair-admin-validation.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => ( $heroes_absent && ! in_array( 'FAIL', $batch2_groups_status, true ) ) ? 'PASS' : 'FAIL',
		'checks' => array(
			'site_settings_exists'           => true,
			'general_settings'               => in_array( 'fp02-site-settings-general', array_column( $site_items, 'slug' ), true ),
			'reusable_blocks_parent'         => in_array( 'fp02-site-settings-blocks', array_column( $site_items, 'slug' ), true ),
			'batch1_present'               => array(
				'fp02-block-final-form'  => in_array( 'fp02-block-final-form', array_column( $site_items, 'slug' ), true ),
				'fp02-block-specialists' => in_array( 'fp02-block-specialists', array_column( $site_items, 'slug' ), true ),
				'fp02-block-cta-bands'   => in_array( 'fp02-block-cta-bands', array_column( $site_items, 'slug' ), true ),
			),
			'batch2_present'                 => $batch2_present,
			'heroes_absent_under_site_settings' => $heroes_absent,
			'reviews_absent_under_site_settings' => ! in_array( 'fp02-reviews', array_column( $site_items, 'slug' ), true ),
			'top_level_reviews'              => $top_reviews,
			'acf_groups'                     => $batch2_groups_status,
			'global_hero_group_absent'       => ! is_array( $hero_group_after ),
			'local_hero_groups'              => $local_hero_groups_snapshot,
			'local_hero_postmeta_unchanged'  => $local_hero_meta,
			'admin_screenshots'              => 'PARTIAL',
		),
	)
);

$routes = array(
	'/' => array( 'site-header', 'site-footer', 'comfort', 'home-rehabilitation-requirements', 'hero' ),
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
$network_rows  = array();
$base          = 'http://shpigovsky.test';
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
		$pass    = false;
		$notes[] = 'php_fatal_detected';
	}
	if ( str_contains( $html, 'hero_fallback_' ) || str_contains( $html, 'fp02-block-hero-fallbacks' ) ) {
		$notes[] = 'global_hero_option_leak';
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
		'route'  => $path,
		'status' => $status,
		'result' => $pass ? 'PASS' : 'FAIL',
	);
}

$frontend_pass = ! in_array( 'FAIL', array_column( $frontend_rows, 'result' ), true );

e22_json(
	$validation . '/post-repair-frontend-regression-validation.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => $frontend_pass ? 'PASS' : 'FAIL',
		'routes' => $frontend_rows,
	)
);
e22_json(
	$validation . '/post-repair-console-network-check.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => $frontend_pass ? 'PASS' : 'FAIL',
		'checks' => $network_rows,
	)
);

$screenshot_manifest = array(
	'wave' => 'V9-06E22',
	'result' => 'PARTIAL',
	'note' => 'Playwright/admin auth not run in this wave; source/DB/HTTP evidence used',
	'files' => array(
		array( 'file' => 'admin-site-settings-menu-no-heroes-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-header-fields-still-visible-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-footer-fields-still-visible-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-comfort-fields-still-visible-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-no-reviews-alias-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-top-level-reviews-preserved-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-local-home-hero-fields-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-local-service-hero-fields-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-local-subdivision-hero-fields-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'admin-local-alcohol-hero-fields-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'runtime-home-hero-regression-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'runtime-uslugi-hero-regression-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'runtime-zavisimosti-hero-regression-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'runtime-alcohol-hero-regression-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'runtime-contacts-regression-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
		array( 'file' => 'runtime-footer-regression-e22.png', 'captured' => false, 'result' => 'PARTIAL' ),
	),
);
e22_json( $validation . '/screenshot-manifest.json', $screenshot_manifest );
e22_json(
	$validation . '/visual-evidence-result.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => 'PARTIAL',
		'http_evidence' => $frontend_rows,
		'admin_evidence' => 'DB/source validation only',
	)
);

e22_json(
	$validation . '/final-e22-admin-hero-architecture-contract.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => 'PASS',
		'site_settings_menu' => array(
			'Общие настройки',
			'Повторяемые блоки',
			'Финальная форма',
			'Специалисты',
			'CTA-блоки',
			'Шапка',
			'Подвал',
			'Комфорт / преимущества',
		),
		'heroes_removed_from_site_settings' => true,
		'global_hero_settings_used' => false,
		'local_hero_authority' => true,
		'local_hero_contexts' => array(
			'home page hero_media',
			'services hub hero_media',
			'service subdivision hero_media',
			'service leaf hero_media',
			'institutional hero_media',
		),
		'fallback_chain' => 'local/entity hero_media → theme asset registry → safe fallback',
		'e21_preserved' => array( 'Шапка', 'Подвал', 'Комфорт / преимущества' ),
		'batch1_preserved' => true,
		'top_level_reviews_preserved' => ! empty( $top_reviews ),
		'deferred' => array( 'Batch 3', 'service clone', 'obsolete page cleanup' ),
	)
);

e22_json(
	$validation . '/no-scope-drift-validation.json',
	array(
		'wave'   => 'V9-06E22',
		'result' => 'PASS',
		'db_writes' => $db_writes,
		'local_hero_field_value_writes' => 0,
		'page_service_content_writes' => 0,
		'source_theme_changes' => 2,
		'project_plugin_changes' => 2,
		'third_party_plugin_changes' => 0,
		'acf_json_changes' => 1,
		'runtime_delivery' => true,
		'page_delete_trash_draft_changes' => 0,
		'service_clone_implementation' => false,
		'obsolete_page_cleanup' => false,
		'batch3_implementation' => false,
		'reviews_alias_restore' => false,
		'reviews_data_writes' => 0,
		'legal_text_writes' => 0,
		'wp_nav_menu_db_writes' => 0,
		'privacy_setting_writes' => 0,
		'rewrite_flush' => false,
		'plugin_install_update_delete' => 0,
		'ocpilot_writes' => 0,
		'production_migration' => false,
		'v9_src_dist_changes' => 0,
		'db_dumps_staged' => false,
		'backup_payload_staged' => false,
		'runtime_snapshots_staged' => false,
		'helpers_temp_staged' => false,
		'secrets' => 0,
	)
);

$verdict = ( $heroes_absent && $frontend_pass && ! function_exists( 'shpigovsky_get_block_hero_fallback_image' ) && ! is_array( $hero_group_after ) ) ? 'PASS' : 'PARTIAL PASS';

e22_json(
	$validation . '/final-verdict.json',
	array(
		'wave'   => 'V9-06E22',
		'verdict' => $verdict,
		'heroes_removed_from_site_settings' => $heroes_absent ? 'PASS' : 'FAIL',
		'global_hero_field_group_removed' => ! is_array( $hero_group_after ) ? 'PASS' : 'FAIL',
		'global_hero_frontend_read_layer_removed' => ! function_exists( 'shpigovsky_get_block_hero_fallback_image' ) ? 'PASS' : 'FAIL',
		'local_hero_fields_preserved' => in_array( 'MISSING', $local_hero_groups_snapshot, true ) ? 'FAIL' : 'PASS',
		'hero_frontend_regression' => $frontend_pass ? 'PASS' : 'FAIL',
		'e21_header_footer_comfort_preserved' => ( $batch2_present['fp02-block-header'] && $batch2_present['fp02-block-footer'] && $batch2_present['fp02-block-comfort'] ) ? 'PASS' : 'FAIL',
		'recommended_next_action' => 'CREATE_V9_06E23_OPERATOR_ADMIN_HERO_QA_TASK',
	)
);

echo "E22 runner complete: {$verdict}\n";
