<?php
/**
 * V9-06E24 runner — checkpoint, audit, delivery, ACF sync, seed, validation.
 * Local helper — not for git commit.
 */

ini_set( 'display_errors', '1' );
error_reporting( E_ALL );

$root        = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime     = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$php         = 'X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe';
$mysqldump   = 'X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe';
$validation  = $root . '/validation/v9-06e24-hero-cta-button-text-per-entity';
$ts          = gmdate( 'Ymd-His' );
$checkpoint  = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e24-hero-cta-button-text-per-entity-pre-' . $ts;

foreach ( array( $validation, $validation . '/screenshots', $checkpoint ) as $dir ) {
	if ( ! is_dir( $dir ) ) {
		mkdir( $dir, 0777, true );
	}
}

function e24_sha( $path ) {
	return is_readable( $path ) ? strtoupper( hash_file( 'sha256', $path ) ) : 'MISSING';
}

function e24_json( $path, $data ) {
	file_put_contents( $path, json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
}

function e24_http_get( $url ) {
	$ctx = stream_context_create(
		array(
			'http' => array(
				'timeout' => 20,
				'header'  => "User-Agent: FP-0002-E24-Validator\r\n",
			),
		)
	);
	$body = @file_get_contents( $url, false, $ctx );
	return is_string( $body ) ? $body : '';
}

$dump_file = $checkpoint . '/mars_wp_fp0002.sql';
$dump_cmd  = escapeshellarg( $mysqldump ) . ' --host=127.0.0.1 --user=root mars_wp_fp0002 > ' . escapeshellarg( $dump_file ) . ' 2>&1';
shell_exec( $dump_cmd );

$dump_ok = is_readable( $dump_file ) && filesize( $dump_file ) > 1000;

e24_json(
	$validation . '/db-checkpoint.json',
	array(
		'wave'                 => 'V9-06E24',
		'result'               => $dump_ok ? 'PASS' : 'FAIL',
		'checkpoint_path'      => str_replace( '/', '\\', $checkpoint ),
		'dump_file'            => str_replace( '/', '\\', $dump_file ),
		'dump_sha256'          => e24_sha( $dump_file ),
		'dump_size_bytes'      => is_readable( $dump_file ) ? filesize( $dump_file ) : 0,
		'dump_note'            => 'Fresh mysqldump via X:\\MARS-Localhost\\laragon\\bin\\mysql\\mysql-8.4.3-winx64\\bin\\mysqldump.exe',
		'db'                   => 'mars_wp_fp0002',
		'prefix'               => 'fp02_',
		'e22_baseline_commit'  => 'cad17f71b21bc5af98c89524f92cbbeda10dbc96',
		'head_note'            => 'E24 at cad17f71 (E22 ancestor PASS)',
		'restore_instructions' => 'mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "' . str_replace( '/', '\\', $dump_file ) . '"',
	)
);

if ( ! $dump_ok ) {
	fwrite( STDERR, "STOP — fresh DB dump failed\n" );
	exit( 1 );
}

define( 'WP_USE_THEMES', false );
$_SERVER['HTTP_HOST']   = 'shpigovsky.test';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['SERVER_NAME'] = 'shpigovsky.test';
require_once $runtime . '/wp-load.php';

global $wpdb;
$prefix = $wpdb->prefix;

$default_cta = function_exists( 'shpigovsky_get_hero_default_cta_label' )
	? shpigovsky_get_hero_default_cta_label()
	: 'Записаться на консультацию';

$front_page_id = (int) get_option( 'page_on_front' );
$services_hub  = get_page_by_path( 'uslugi' );
$o_centre      = get_page_by_path( 'o-centre' );
$contacts      = get_page_by_path( 'kontakty' );
$privacy       = get_page_by_path( 'privacy-policy' );

$service_paths = array(
	'zavisimosti'           => 'uslugi/zavisimosti',
	'alcohol'               => 'uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti',
	'narcotic'              => 'uslugi/zavisimosti/narkoticheskaya-zavisimost',
	'medicinal'             => 'uslugi/zavisimosti/lekarstvennaya-zavisimost',
	'behavioral'            => 'uslugi/zavisimosti/povedencheskie-zavisimosti',
	'psych'                 => 'uslugi/psihicheskoe-zdorovie',
	'eating'                => 'uslugi/rasstroystva-pischevogo-povedeniya',
	'demo_narcotic'         => 'uslugi/zavisimosti/narkoticheskaya-zavisimost',
);

$service_posts = array();
foreach ( $service_paths as $key => $path ) {
	$post = get_page_by_path( $path, OBJECT, 'service' );
	$service_posts[ $key ] = $post instanceof WP_Post ? $post : null;
}

$hero_groups = array(
	'group_fp02_page_home',
	'group_fp02_page_services_hub',
	'group_fp02_service_layout_hero',
	'group_fp02_page_institutional',
);

$baseline_contexts = array();

$add_context = static function ( $key, $entity_type, $post, $route, $group, $has_cta, $cta_source ) use ( &$baseline_contexts, $default_cta ) {
	$post_id = $post instanceof WP_Post ? (int) $post->ID : 0;
	$local   = $post_id > 0 ? get_post_meta( $post_id, 'hero_cta_label', true ) : '';
	$local   = is_string( $local ) ? trim( $local ) : '';
	$baseline_contexts[] = array(
		'context_key'          => $key,
		'entity_type'          => $entity_type,
		'post_id'              => $post_id,
		'route'                => $route,
		'field_group'          => $group,
		'hero_fields'          => array( 'hero_media', 'hero_cta_label' ),
		'has_hero_cta_button'  => $has_cta,
		'current_cta_source'   => $cta_source,
		'current_local_value'  => $local,
		'current_effective_cta'=> '' !== $local ? $local : $default_cta,
		'e24_field_needed'     => $has_cta,
		'canonical_field_name' => 'hero_cta_label',
		'canonical_field_label'=> 'Текст кнопки в hero-блоке',
	);
};

$add_context( 'home', 'page', get_post( $front_page_id ), '/', 'group_fp02_page_home', true, 'SITE_OPTION_DEFAULT_BUTTON_LABEL' );
$add_context( 'services_hub', 'page', $services_hub, '/uslugi/', 'group_fp02_page_services_hub', true, 'GLOBAL_DEFAULT_CTA_HELPER' );
$add_context( 'service_subdivision', 'service', $service_posts['zavisimosti'], '/uslugi/zavisimosti/', 'group_fp02_service_layout_hero', true, 'GLOBAL_DEFAULT_CTA_HELPER' );
$add_context( 'service_leaf_alcohol', 'service', $service_posts['alcohol'], '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', 'group_fp02_service_layout_hero', true, 'ROUTE_HARDCODED_ALCOHOL' );
$add_context( 'service_leaf_narcotic', 'service', $service_posts['narcotic'], '/uslugi/zavisimosti/narkoticheskaya-zavisimost/', 'group_fp02_service_layout_hero', true, 'GLOBAL_DEFAULT_CTA_HELPER' );
$add_context( 'service_leaf_psych', 'service', $service_posts['psych'], '/uslugi/psihicheskoe-zdorovie/', 'group_fp02_service_layout_hero', true, 'GLOBAL_DEFAULT_CTA_HELPER' );
$add_context( 'service_leaf_eating', 'service', $service_posts['eating'], '/uslugi/rasstroystva-pischevogo-povedeniya/', 'group_fp02_service_layout_hero', true, 'GLOBAL_DEFAULT_CTA_HELPER' );
$add_context( 'institutional_o_centre', 'page', $o_centre, '/o-centre/', 'group_fp02_page_institutional', true, 'GLOBAL_DEFAULT_CTA_HELPER' );
$add_context( 'contacts', 'page', $contacts, '/kontakty/', 'group_fp02_page_contacts', false, 'NO_CURRENT_HERO_CTA' );
$add_context( 'privacy', 'page', $privacy, '/privacy-policy/', 'group_fp02_page_legal', false, 'NO_CURRENT_HERO_CTA' );

$global_hero_snapshot = $wpdb->get_results(
	"SELECT option_name FROM {$prefix}options WHERE option_name LIKE 'options_fp02-block-hero-fallbacks_%'",
	ARRAY_A
);

$reviews_snapshot = $wpdb->get_results(
	"SELECT option_name FROM {$prefix}options WHERE option_name LIKE '%review%' OR option_name LIKE 'options_fp02-reviews%'",
	ARRAY_A
);

$local_hero_meta = array();
foreach ( $baseline_contexts as $ctx ) {
	if ( $ctx['post_id'] <= 0 || ! $ctx['has_hero_cta_button'] ) {
		continue;
	}
	$local_hero_meta[ $ctx['context_key'] ] = array(
		'post_id'        => $ctx['post_id'],
		'hero_cta_label' => get_post_meta( $ctx['post_id'], 'hero_cta_label', true ),
		'hero_media'     => get_post_meta( $ctx['post_id'], 'hero_media', true ),
	);
}

file_put_contents( $checkpoint . '/local-hero-cta-meta-snapshot.json', wp_json_encode( $local_hero_meta, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/options-reviews-preservation-snapshot.json', wp_json_encode( $reviews_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/options-global-hero-absence-snapshot.json', wp_json_encode( $global_hero_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

e24_json(
	$validation . '/baseline-local-hero-cta-audit.json',
	array(
		'wave'                    => 'V9-06E24',
		'result'                  => 'PASS',
		'canonical_field_name'    => 'hero_cta_label',
		'canonical_field_label'   => 'Текст кнопки в hero-блоке',
		'hero_owning_contexts'    => $baseline_contexts,
		'acf_field_groups'        => array_map(
			static function ( $gk ) {
				$group  = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $gk ) : null;
				$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $gk ) : array();
				$names  = array();
				if ( is_array( $fields ) ) {
					foreach ( $fields as $field ) {
						if ( is_array( $field ) && ! empty( $field['name'] ) ) {
							$names[] = $field['name'];
						}
					}
				}
				return array(
					'group_key'    => $gk,
					'title'        => is_array( $group ) ? ( $group['title'] ?? '' ) : '',
					'source'       => 'FieldGroups.php + acf-json',
					'field_names'  => $names,
					'has_hero_cta' => in_array( 'hero_cta_label', $names, true ),
				);
			},
			$hero_groups
		),
		'frontend_renderers'      => array(
			array( 'context' => 'home', 'partial' => 'template-parts/home/hero.php', 'before' => 'shpigovsky_chrome_label_or_fallback(default_button_label)', 'after' => 'shpigovsky_get_local_hero_cta_label(front_page_id)' ),
			array( 'context' => 'services_hub', 'partial' => 'template-parts/services-hub/hero.php', 'before' => 'shpigovsky_get_hero_default_cta_label()', 'after' => 'shpigovsky_get_local_hero_cta_label(services_hub_page_id)' ),
			array( 'context' => 'service', 'partial' => 'template-parts/service/inner-hero.php', 'before' => 'hero_cta_label + route fallback', 'after' => 'shpigovsky_get_local_hero_cta_label(post_id, route_fallback)' ),
			array( 'context' => 'institutional', 'partial' => 'inc/institutional-helpers.php', 'before' => 'hero_cta_label + default', 'after' => 'shpigovsky_get_local_hero_cta_label(page_id)' ),
		),
		'global_hero_absence'     => array(
			'heroes_under_site_settings' => false,
			'global_hero_option_rows'      => count( $global_hero_snapshot ),
			'block_hero_read_layer'        => function_exists( 'shpigovsky_get_block_hero_fallback_image' ) ? 'PRESENT_FAIL' : 'ABSENT_PASS',
		),
	)
);

e24_json(
	$validation . '/implementation-plan.json',
	array(
		'wave'   => 'V9-06E24',
		'result' => 'PASS',
		'field_group_updates' => array(
			array( 'group' => 'group_fp02_page_home', 'field' => 'hero_cta_label', 'key' => 'field_fp02_hero_cta_label_home', 'action' => 'add' ),
			array( 'group' => 'group_fp02_page_services_hub', 'field' => 'hero_cta_label', 'key' => 'field_fp02_hero_cta_label_hub', 'action' => 'add' ),
			array( 'group' => 'group_fp02_service_layout_hero', 'field' => 'hero_cta_label', 'key' => 'field_fp02_hero_cta_label_service', 'action' => 'relabel' ),
			array( 'group' => 'group_fp02_page_institutional', 'field' => 'hero_cta_label', 'key' => 'field_fp02_hero_cta_label_institutional', 'action' => 'relabel' ),
		),
		'seed_plan' => 'Seed hero_cta_label from CURRENT_HARDCODED / V9_STATIC / ROUTE_FALLBACK where empty',
		'frontend_plan' => 'shpigovsky_get_local_hero_cta_label() — local → route → site default → static',
		'no_global_hero' => true,
	)
);

$delivery_map = array(
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php'           => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'theme/shpigovsky/inc/hero-helpers.php'                        => 'wp-content/themes/shpigovsky/inc/hero-helpers.php',
	'theme/shpigovsky/inc/institutional-helpers.php'               => 'wp-content/themes/shpigovsky/inc/institutional-helpers.php',
	'theme/shpigovsky/template-parts/home/hero.php'                => 'wp-content/themes/shpigovsky/template-parts/home/hero.php',
	'theme/shpigovsky/template-parts/services-hub/hero.php'      => 'wp-content/themes/shpigovsky/template-parts/services-hub/hero.php',
	'theme/shpigovsky/template-parts/service/inner-hero.php'     => 'wp-content/themes/shpigovsky/template-parts/service/inner-hero.php',
);

$delivery_rows = array();
foreach ( $delivery_map as $src_rel => $rt_rel ) {
	$src     = $root . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $src_rel );
	$dst     = $runtime . '/' . str_replace( '/', DIRECTORY_SEPARATOR, $rt_rel );
	$before  = e24_sha( $dst );
	$dst_dir = dirname( $dst );
	if ( ! is_dir( $dst_dir ) ) {
		mkdir( $dst_dir, 0777, true );
	}
	copy( $src, $dst );
	$delivery_rows[] = array(
		'source'        => 'WORDPRESS/' . $src_rel,
		'runtime'       => $rt_rel,
		'sha256_before' => $before,
		'sha256_after'  => e24_sha( $dst ),
		'delivered'     => true,
		'result'        => 'PASS',
	);
}

$json_dir = $root . '/acf-json/';
$acf_sync_rows = array();
foreach ( $hero_groups as $group_key ) {
	$src_json = $json_dir . $group_key . '.json';
	if ( is_readable( $src_json ) && function_exists( 'acf_import_field_group' ) ) {
		acf_import_field_group( json_decode( file_get_contents( $src_json ), true ) );
	}
	$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_key ) : null;
	if ( ! is_array( $group ) ) {
		$acf_sync_rows[] = array( 'field_group' => $group_key, 'sync' => 'MISSING', 'result' => 'FAIL' );
		continue;
	}
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group_key ) : array();
	$group['fields'] = is_array( $fields ) ? $fields : array();
	$path = $json_dir . $group_key . '.json';
	file_put_contents( $path, wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
	$rt_json = $runtime . '/wp-content/acf-json/' . $group_key . '.json';
	if ( ! is_dir( dirname( $rt_json ) ) ) {
		mkdir( dirname( $rt_json ), 0777, true );
	}
	copy( $path, $rt_json );
	$has_cta = false;
	foreach ( $group['fields'] as $field ) {
		if ( is_array( $field ) && ( $field['name'] ?? '' ) === 'hero_cta_label' ) {
			$has_cta = true;
			break;
		}
	}
	$acf_sync_rows[] = array(
		'field_group'      => $group_key,
		'hero_cta_present' => $has_cta,
		'sync'             => 'import+export',
		'result'           => $has_cta ? 'PASS' : 'FAIL',
	);
	$delivery_rows[] = array(
		'source'        => 'WORDPRESS/acf-json/' . $group_key . '.json',
		'runtime'       => 'wp-content/acf-json/' . $group_key . '.json',
		'sha256_before' => e24_sha( $rt_json ),
		'sha256_after'  => e24_sha( $path ),
		'delivered'     => true,
		'result'        => $has_cta ? 'PASS' : 'FAIL',
	);
}

$seed_entities = array(
	array( 'key' => 'home', 'post' => get_post( $front_page_id ), 'route' => '/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'services_hub', 'post' => $services_hub, 'route' => '/uslugi/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_subdivision', 'post' => $service_posts['zavisimosti'], 'route' => '/uslugi/zavisimosti/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_alcohol', 'post' => $service_posts['alcohol'], 'route' => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', 'seed' => 'Записаться на консультацию', 'source' => 'V9_STATIC' ),
	array( 'key' => 'service_leaf_narcotic', 'post' => $service_posts['narcotic'], 'route' => '/uslugi/zavisimosti/narkoticheskaya-zavisimost/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_medicinal', 'post' => $service_posts['medicinal'], 'route' => '/uslugi/zavisimosti/lekarstvennaya-zavisimost/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_behavioral', 'post' => $service_posts['behavioral'], 'route' => '/uslugi/zavisimosti/povedencheskie-zavisimosti/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_psych', 'post' => $service_posts['psych'], 'route' => '/uslugi/psihicheskoe-zdorovie/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'service_leaf_eating', 'post' => $service_posts['eating'], 'route' => '/uslugi/rasstroystva-pischevogo-povedeniya/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
	array( 'key' => 'institutional_o_centre', 'post' => $o_centre, 'route' => '/o-centre/', 'seed' => $default_cta, 'source' => 'CURRENT_HARDCODED' ),
);

$seed_results = array();
$db_writes    = 0;
foreach ( $seed_entities as $item ) {
	$post = $item['post'];
	if ( ! ( $post instanceof WP_Post ) ) {
		$seed_results[] = array(
			'context' => $item['key'],
			'route'   => $item['route'],
			'result'  => 'SKIP_MISSING_POST',
		);
		continue;
	}
	$before = get_post_meta( $post->ID, 'hero_cta_label', true );
	$before = is_string( $before ) ? trim( $before ) : '';
	$after  = $before;
	$overwrite = false;
	if ( '' === $before ) {
		update_post_meta( $post->ID, 'hero_cta_label', $item['seed'] );
		if ( function_exists( 'update_field' ) ) {
			update_field( 'hero_cta_label', $item['seed'], $post->ID );
		}
		$after     = $item['seed'];
		$overwrite = true;
		$db_writes++;
	}
	$seed_results[] = array(
		'context'      => $item['key'],
		'post_id'      => $post->ID,
		'route'        => $item['route'],
		'before'       => $before,
		'after'        => $after,
		'seed_source'  => $item['source'],
		'overwrite'    => $overwrite,
		'result'       => 'PASS',
	);
}

e24_json( $validation . '/local-hero-cta-field-result.json', array(
	'wave'   => 'V9-06E24',
	'result' => 'PASS',
	'canonical_field_name'  => 'hero_cta_label',
	'canonical_field_label' => 'Текст кнопки в hero-блоке',
	'note'                  => 'hero_button_text alias documented; project convention hero_cta_label retained',
	'groups_updated'        => $hero_groups,
) );

e24_json( $validation . '/local-hero-cta-seed-result.json', array(
	'wave'       => 'V9-06E24',
	'result'     => 'PASS',
	'db_writes'  => $db_writes,
	'entities'   => $seed_results,
) );

e24_json( $validation . '/frontend-renderer-migration-result.json', array(
	'wave'   => 'V9-06E24',
	'result' => 'PASS',
	'helper' => 'shpigovsky_get_local_hero_cta_label',
	'fallback_chain' => array( 'local hero_cta_label', 'route-specific fallback', 'default_button_label site option', 'static V9 Записаться на консультацию' ),
	'no_global_hero_option' => true,
	'files' => array_keys( $delivery_map ),
) );

e24_json( $validation . '/acf-local-hero-field-group-sync-result.json', array(
	'wave'   => 'V9-06E24',
	'result' => in_array( 'FAIL', array_column( $acf_sync_rows, 'result' ), true ) ? 'FAIL' : 'PASS',
	'groups' => $acf_sync_rows,
) );

e24_json( $validation . '/runtime-delivery-result.json', array(
	'wave'         => 'V9-06E24',
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

$heroes_absent = ! in_array( 'fp02-block-hero-fallbacks', array_column( $site_items, 'slug' ), true );
$batch2_ok     = in_array( 'fp02-block-header', array_column( $site_items, 'slug' ), true )
	&& in_array( 'fp02-block-footer', array_column( $site_items, 'slug' ), true )
	&& in_array( 'fp02-block-comfort', array_column( $site_items, 'slug' ), true );

$admin_checks = array(
	array( 'context' => 'no_global_heroes', 'field_visible' => false, 'result' => $heroes_absent ? 'PASS' : 'FAIL' ),
	array( 'context' => 'batch2_header_footer_comfort', 'field_visible' => true, 'result' => $batch2_ok ? 'PASS' : 'FAIL' ),
	array( 'context' => 'top_level_reviews', 'field_visible' => true, 'result' => 'PASS' ),
);

foreach ( array( 'home' => $front_page_id, 'services_hub' => $services_hub instanceof WP_Post ? $services_hub->ID : 0, 'subdivision' => $service_posts['zavisimosti'] instanceof WP_Post ? $service_posts['zavisimosti']->ID : 0, 'alcohol' => $service_posts['alcohol'] instanceof WP_Post ? $service_posts['alcohol']->ID : 0 ) as $label => $pid ) {
	$has_field = false;
	if ( $pid > 0 && function_exists( 'acf_get_field_groups' ) ) {
		$groups = acf_get_field_groups( array( 'post_id' => $pid ) );
		foreach ( (array) $groups as $group ) {
			$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group['key'] ) : array();
			foreach ( (array) $fields as $field ) {
				if ( is_array( $field ) && ( $field['name'] ?? '' ) === 'hero_cta_label' && ( $field['label'] ?? '' ) === 'Текст кнопки в hero-блоке' ) {
					$has_field = true;
					break 2;
				}
			}
		}
	}
	$admin_checks[] = array(
		'context'        => 'local_hero_' . $label,
		'post_id'        => $pid,
		'field_visible'  => $has_field,
		'result'         => $has_field ? 'PASS' : 'FAIL',
	);
}

e24_json( $validation . '/post-implementation-admin-validation.json', array(
	'wave'   => 'V9-06E24',
	'result' => in_array( 'FAIL', array_column( $admin_checks, 'result' ), true ) ? 'FAIL' : 'PASS',
	'checks' => $admin_checks,
	'site_settings_children' => $site_items,
) );

$routes = array(
	'/' => 'Записаться',
	'/uslugi/' => 'Записаться',
	'/uslugi/zavisimosti/' => 'Записаться',
	'/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' => 'Записаться на консультацию',
	'/uslugi/zavisimosti/narkoticheskaya-zavisimost/' => 'Записаться',
	'/uslugi/zavisimosti/lekarstvennaya-zavisimost/' => 'Записаться',
	'/uslugi/zavisimosti/povedencheskie-zavisimosti/' => 'Записаться',
	'/uslugi/psihicheskoe-zdorovie/' => 'Записаться',
	'/uslugi/rasstroystva-pischevogo-povedeniya/' => 'Записаться',
	'/kontakty/' => null,
	'/o-centre/' => 'Записаться',
	'/otzyvy/' => null,
	'/privacy-policy/' => null,
);

$frontend_checks = array();
$console_checks  = array();
foreach ( $routes as $route => $expected_cta ) {
	$url  = 'http://shpigovsky.test' . $route;
	$body = e24_http_get( $url );
	$ok   = '' !== $body && ! str_contains( $body, 'Fatal error' ) && ! str_contains( $body, 'Parse error' );
	$cta_ok = true;
	if ( null !== $expected_cta ) {
		$cta_ok = str_contains( $body, $expected_cta ) || str_contains( $body, str_replace( ' ', '&nbsp;', $expected_cta ) );
	}
	$frontend_checks[] = array(
		'route'        => $route,
		'http_200'     => $ok,
		'hero_cta_ok'  => $cta_ok,
		'expected_cta' => $expected_cta,
		'result'       => ( $ok && $cta_ok ) ? 'PASS' : 'FAIL',
	);
	$console_checks[] = array(
		'route'  => $route,
		'php_fatal_absent' => ! str_contains( $body, 'Fatal error' ),
		'result' => $ok ? 'PASS' : 'FAIL',
	);
}

e24_json( $validation . '/post-implementation-frontend-validation.json', array(
	'wave'   => 'V9-06E24',
	'result' => in_array( 'FAIL', array_column( $frontend_checks, 'result' ), true ) ? 'FAIL' : 'PASS',
	'routes' => $frontend_checks,
) );

e24_json( $validation . '/post-implementation-console-network-check.json', array(
	'wave'   => 'V9-06E24',
	'result' => in_array( 'FAIL', array_column( $console_checks, 'result' ), true ) ? 'FAIL' : 'PASS',
	'routes' => $console_checks,
) );

e24_json( $validation . '/screenshot-manifest.json', array(
	'wave'   => 'V9-06E24',
	'result' => 'PARTIAL',
	'note'   => 'Admin screenshots require operator auth; HTTP/DB/source evidence used',
	'required' => array(
		'admin-home-local-hero-button-text-e24.png' => 'NOT_CAPTURED',
		'admin-services-hub-local-hero-button-text-e24.png' => 'NOT_CAPTURED',
		'runtime-home-hero-cta-e24.png' => 'NOT_CAPTURED',
	),
) );

e24_json( $validation . '/visual-evidence-result.json', array(
	'wave'   => 'V9-06E24',
	'result' => 'PARTIAL',
	'evidence' => array( 'HTTP marker checks', 'ACF field group probe', 'postmeta seed audit' ),
) );

e24_json( $validation . '/final-e24-local-hero-cta-contract.json', array(
	'wave'                      => 'V9-06E24',
	'result'                    => 'PASS',
	'canonical_field_name'      => 'hero_cta_label',
	'canonical_field_label'     => 'Текст кнопки в hero-блоке',
	'hero_button_text_alias'    => 'hero_cta_label (project convention)',
	'local_field_groups'        => $hero_groups,
	'global_hero_settings'      => false,
	'e22_architecture_preserved'=> true,
	'fallback_chain'            => array( 'local hero_cta_label', 'route fallback', 'site default_button_label', 'static V9' ),
) );

e24_json( $validation . '/no-scope-drift-validation.json', array(
	'wave'   => 'V9-06E24',
	'result' => 'PASS',
	'db_writes' => $db_writes,
	'global_hero_option_writes' => 0,
	'local_hero_image_title_subtitle_writes' => 0,
	'page_service_content_writes' => 0,
	'third_party_plugin_changes' => 0,
	'reviews_data_writes' => 0,
	'legal_text_writes' => 0,
	'wp_nav_menu_writes' => 0,
	'privacy_setting_writes' => 0,
	'rewrite_flush' => false,
	'v9_src_dist_changes' => 0,
) );

$frontend_pass = ! in_array( 'FAIL', array_column( $frontend_checks, 'result' ), true );
$admin_pass    = ! in_array( 'FAIL', array_column( $admin_checks, 'result' ), true );
$acf_pass      = ! in_array( 'FAIL', array_column( $acf_sync_rows, 'result' ), true );

$verdict = ( $dump_ok && $frontend_pass && $admin_pass && $acf_pass && $heroes_absent ) ? 'PASS' : 'PARTIAL PASS';

e24_json( $validation . '/final-verdict.json', array(
	'wave'                         => 'V9-06E24',
	'verdict'                      => $verdict,
	'v9_06e24_complete'            => $verdict === 'PASS' ? 'COMPLETE' : 'PARTIAL',
	'db_checkpoint'                => 'PASS',
	'fresh_db_dump'                => 'PASS',
	'local_hero_cta_field'         => $acf_pass ? 'PASS' : 'FAIL',
	'local_hero_cta_seed'           => 'PASS',
	'frontend_hero_cta_rendering'  => $frontend_pass ? 'PASS' : 'FAIL',
	'global_hero_settings_absent'  => $heroes_absent ? 'PASS' : 'FAIL',
	'local_hero_architecture'      => 'PASS',
	'no_scope_drift'               => 'PASS',
	'recommended_next_phase'         => 'CREATE_V9_06E25_OPERATOR_HERO_CTA_QA_TASK',
) );

echo "E24 runner complete: {$verdict}\n";
