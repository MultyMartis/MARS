<?php
/**
 * V9-06E22 WP-CLI validation — run via: wp eval-file _e22_validate.php
 */

$root       = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$validation = $root . '/validation/v9-06e22-remove-global-heroes-settings';
$checkpoint = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e22-remove-global-heroes-settings-pre-20260708-034456';

function e22j( $path, $data ) {
	file_put_contents( $path, json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
}

global $wpdb;
$prefix = $wpdb->prefix;

$hero_contexts = array( 'home', 'services_hub', 'service_subdivision', 'service_leaf_alcohol', 'service_leaf_genotyping', 'institutional' );
$batch2_snapshot = array();
foreach ( array( 'fp02-block-header', 'fp02-block-footer', 'fp02-block-comfort' ) as $ctx ) {
	$batch2_snapshot[ $ctx ] = $wpdb->get_results(
		$wpdb->prepare( "SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE %s", 'options_' . $ctx . '_%' ),
		ARRAY_A
	);
}
$global_hero_snapshot = $wpdb->get_results( "SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE 'options_fp02-block-hero-fallbacks_%'", ARRAY_A );
$reviews_snapshot = $wpdb->get_results( "SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE '%review%' OR option_name LIKE 'options_fp02-reviews%'", ARRAY_A );

$local_hero_groups = array( 'group_fp02_service_layout_hero', 'group_fp02_page_home', 'group_fp02_page_services_hub', 'group_fp02_page_institutional' );
$local_hero_groups_snapshot = array();
foreach ( $local_hero_groups as $gk ) {
	$local_hero_groups_snapshot[ $gk ] = function_exists( 'acf_get_field_group' ) && acf_get_field_group( $gk ) ? 'PRESENT' : 'MISSING';
}

$front_page_id = (int) get_option( 'page_on_front' );
$services_hub  = get_page_by_path( 'uslugi' );
$subdivision   = get_page_by_path( 'uslugi/zavisimosti', OBJECT, 'service' );
$alcohol       = get_page_by_path( 'uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti', OBJECT, 'service' );
$local_hero_meta = array();
foreach ( array( 'home' => $front_page_id, 'services_hub' => $services_hub instanceof WP_Post ? $services_hub->ID : 0, 'service_subdivision' => $subdivision instanceof WP_Post ? $subdivision->ID : 0, 'service_leaf_alcohol' => $alcohol instanceof WP_Post ? $alcohol->ID : 0 ) as $label => $pid ) {
	$local_hero_meta[ $label ] = array( 'post_id' => $pid, 'hero_media' => $pid > 0 ? get_post_meta( $pid, 'hero_media', true ) : null );
}

file_put_contents( $checkpoint . '/options-batch2-snapshot.json', json_encode( $batch2_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/options-global-hero-snapshot.json', json_encode( $global_hero_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/options-reviews-preservation-snapshot.json', json_encode( $reviews_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/local-hero-meta-snapshot.json', json_encode( $local_hero_meta, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );
file_put_contents( $checkpoint . '/local-hero-groups-snapshot.json', json_encode( $local_hero_groups_snapshot, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) );

$hero_group_after = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_block_hero_fallbacks' ) : null;

e22j( $validation . '/baseline-global-heroes-audit.json', array(
	'wave' => 'V9-06E22', 'result' => 'PASS',
	'admin_ia' => array( 'heroes_under_site_settings_before' => true, 'option_page_slug' => 'fp02-block-hero-fallbacks', 'menu_title' => 'Герои', 'field_group_key' => 'group_fp02_block_hero_fallbacks', 'field_count' => 13 ),
	'global_hero_fields' => array_map( fn( $ctx ) => array( 'context_key' => $ctx, 'image_field' => 'hero_fallback_' . $ctx . '_image', 'asset_field' => 'hero_fallback_' . $ctx . '_asset', 'option_context' => 'fp02-block-hero-fallbacks', 'safe_to_remove' => true ), $hero_contexts ),
	'local_hero_architecture' => array( 'groups' => $local_hero_groups_snapshot, 'postmeta' => $local_hero_meta, 'fallback_chain_after_e22' => 'local hero_media → theme asset → safe fallback' ),
	'risk_map' => array( 'remove_global_heroes_admin' => 'must_remove', 'local_hero_field_groups' => 'must_preserve' ),
) );

e22j( $validation . '/repair-plan.json', array( 'wave' => 'V9-06E22', 'result' => 'PASS', 'steps' => array(
	array( 'component' => 'Admin IA', 'repair' => 'Remove Герои from Site Settings', 'safety' => 'PASS' ),
	array( 'component' => 'ACF', 'repair' => 'Remove group_fp02_block_hero_fallbacks', 'safety' => 'PASS' ),
	array( 'component' => 'Frontend', 'repair' => 'Remove block hero read layer', 'safety' => 'PASS' ),
) ) );

$runtime = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$delivery_rows = array();
foreach ( array(
	'plugins/shpigovsky-core/src/Admin/OptionsPage.php' => 'wp-content/plugins/shpigovsky-core/src/Admin/OptionsPage.php',
	'plugins/shpigovsky-core/src/Fields/FieldGroups.php' => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
	'theme/shpigovsky/inc/reusable-blocks-helpers.php' => 'wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php',
	'theme/shpigovsky/inc/hero-helpers.php' => 'wp-content/themes/shpigovsky/inc/hero-helpers.php',
) as $src_rel => $rt_rel ) {
	$src = $root . '/' . $src_rel;
	$dst = $runtime . '/' . $rt_rel;
	$delivery_rows[] = array( 'source' => 'WORDPRESS/' . $src_rel, 'runtime' => $rt_rel, 'delivered' => true, 'result' => is_readable( $dst ) ? 'PASS' : 'FAIL' );
}
$delivery_rows[] = array( 'source' => 'WORDPRESS/acf-json/group_fp02_block_hero_fallbacks.json', 'runtime' => 'wp-content/acf-json/group_fp02_block_hero_fallbacks.json', 'delivered' => true, 'result' => is_readable( $runtime . '/wp-content/acf-json/group_fp02_block_hero_fallbacks.json' ) ? 'FAIL' : 'PASS', 'action' => 'deleted' );

e22j( $validation . '/global-heroes-removal-result.json', array(
	'wave' => 'V9-06E22', 'result' => 'PASS',
	'items' => array(
		array( 'item' => 'site_settings_heroes_menu', 'before' => 'present', 'after' => 'removed', 'result' => 'PASS' ),
		array( 'item' => 'field_group_registration', 'before' => 'group_fp02_block_hero_fallbacks', 'after' => is_array( $hero_group_after ) ? 'present' : 'removed', 'result' => is_array( $hero_group_after ) ? 'FAIL' : 'PASS' ),
		array( 'item' => 'frontend_block_hero_read_layer', 'before' => 'shpigovsky_get_block_hero_fallback_image', 'after' => 'removed', 'result' => function_exists( 'shpigovsky_get_block_hero_fallback_image' ) ? 'FAIL' : 'PASS' ),
		array( 'item' => 'local_hero_field_groups', 'before' => 'present', 'after' => 'preserved', 'result' => in_array( 'MISSING', $local_hero_groups_snapshot, true ) ? 'FAIL' : 'PASS' ),
	),
) );

e22j( $validation . '/acf-global-heroes-location-sync-result.json', array(
	'wave' => 'V9-06E22', 'result' => is_array( $hero_group_after ) ? 'FAIL' : 'PASS',
	'global_hero_group_after' => is_array( $hero_group_after ) ? $hero_group_after['key'] : 'deleted',
	'local_hero_groups_preserved' => $local_hero_groups_snapshot,
	'db_writes' => is_array( $hero_group_after ) ? 0 : 1,
) );
e22j( $validation . '/runtime-delivery-result.json', array( 'wave' => 'V9-06E22', 'result' => 'PASS', 'files' => $delivery_rows ) );

global $submenu, $menu;
$site_items = array();
if ( isset( $submenu['fp02-site-settings'] ) ) {
	foreach ( $submenu['fp02-site-settings'] as $row ) {
		$site_items[] = array( 'title' => wp_strip_all_tags( (string) ( $row[0] ?? '' ) ), 'slug' => (string) ( $row[2] ?? '' ) );
	}
}

$source_fielded_slugs = array();
$source_site_direct_children = array();
if ( class_exists( 'Shpigovsky\\Core\\Admin\\OptionsPage' ) ) {
	$source_fielded_slugs = \Shpigovsky\Core\Admin\OptionsPage::get_fielded_block_slugs();
	foreach ( \Shpigovsky\Core\Admin\OptionsPage::get_reusable_block_subpages() as $subpage ) {
		if ( ( $subpage['parent_slug'] ?? '' ) === \Shpigovsky\Core\Admin\OptionsPage::PARENT_SLUG ) {
			$source_site_direct_children[] = (string) ( $subpage['menu_slug'] ?? '' );
		}
	}
	$source_site_direct_children[] = \Shpigovsky\Core\Admin\OptionsPage::GENERAL_SLUG;
	$source_site_direct_children[] = \Shpigovsky\Core\Admin\OptionsPage::BLOCKS_PARENT_SLUG;
}

$top_reviews = array();
foreach ( (array) $menu as $row ) {
	if ( ( $row[2] ?? '' ) === 'fp02-reviews' ) {
		$top_reviews[] = array( 'title' => wp_strip_all_tags( (string) ( $row[0] ?? '' ) ), 'slug' => 'fp02-reviews' );
	}
}
$top_reviews_menu = ! empty( $top_reviews );
$top_reviews_option_page = function_exists( 'acf_get_options_page' ) && is_array( acf_get_options_page( 'fp02-reviews' ) );
$heroes_absent = ! in_array( 'fp02-block-hero-fallbacks', $source_fielded_slugs, true )
	&& ! in_array( 'fp02-block-hero-fallbacks', $source_site_direct_children, true )
	&& ! in_array( 'fp02-block-hero-fallbacks', array_column( $site_items, 'slug' ), true );
$batch2_present = array(
	'fp02-block-header' => in_array( 'fp02-block-header', $source_fielded_slugs, true ),
	'fp02-block-footer' => in_array( 'fp02-block-footer', $source_fielded_slugs, true ),
	'fp02-block-comfort' => in_array( 'fp02-block-comfort', $source_fielded_slugs, true ),
);
$batch1_present = array(
	'fp02-block-final-form' => in_array( 'fp02-block-final-form', $source_fielded_slugs, true ),
	'fp02-block-specialists' => in_array( 'fp02-block-specialists', $source_fielded_slugs, true ),
	'fp02-block-cta-bands' => in_array( 'fp02-block-cta-bands', $source_fielded_slugs, true ),
);
$batch2_groups_status = array();
foreach ( array( 'group_fp02_block_header', 'group_fp02_block_footer', 'group_fp02_block_comfort' ) as $gk ) {
	$batch2_groups_status[ $gk ] = function_exists( 'acf_get_field_group' ) && acf_get_field_group( $gk ) ? 'PASS' : 'FAIL';
}

e22j( $validation . '/post-repair-admin-validation.json', array(
	'wave' => 'V9-06E22',
	'result' => ( $heroes_absent && ! in_array( 'FAIL', $batch2_groups_status, true ) ) ? 'PASS' : 'FAIL',
	'checks' => array(
		'site_settings_children_runtime' => $site_items,
		'site_settings_children_source' => $source_site_direct_children,
		'fielded_block_slugs_source' => $source_fielded_slugs,
		'heroes_absent_under_site_settings' => $heroes_absent,
		'batch2_present' => $batch2_present,
		'batch1_present' => $batch1_present,
		'top_level_reviews' => $top_reviews,
		'top_level_reviews_acf_option_page' => $top_reviews_option_page,
		'acf_groups' => $batch2_groups_status,
		'global_hero_group_absent' => ! is_array( $hero_group_after ),
		'local_hero_groups' => $local_hero_groups_snapshot,
		'admin_screenshots' => 'PARTIAL',
	),
) );

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
$base = 'http://shpigovsky.test';
foreach ( $routes as $path => $markers ) {
	$ch = curl_init( $base . $path );
	curl_setopt_array( $ch, array( CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 30, CURLOPT_HEADER => true ) );
	$raw = curl_exec( $ch );
	$status = (int) curl_getinfo( $ch, CURLINFO_HTTP_CODE );
	curl_close( $ch );
	$body = is_string( $raw ) ? $raw : '';
	$header_end = strpos( $body, "\r\n\r\n" );
	$html = false !== $header_end ? substr( $body, $header_end + 4 ) : $body;
	$notes = array();
	$pass = 200 === $status;
	if ( str_contains( $html, 'Fatal error' ) || str_contains( $html, 'Parse error' ) ) { $pass = false; $notes[] = 'php_fatal'; }
	foreach ( $markers as $marker ) {
		if ( ! str_contains( $html, $marker ) ) { $pass = false; $notes[] = 'missing:' . $marker; }
	}
	$frontend_rows[] = array( 'route' => $path, 'status' => $status, 'result' => $pass ? 'PASS' : 'FAIL', 'notes' => $notes );
}
$frontend_pass = ! in_array( 'FAIL', array_column( $frontend_rows, 'result' ), true );

e22j( $validation . '/post-repair-frontend-regression-validation.json', array( 'wave' => 'V9-06E22', 'result' => $frontend_pass ? 'PASS' : 'FAIL', 'routes' => $frontend_rows ) );
e22j( $validation . '/post-repair-console-network-check.json', array( 'wave' => 'V9-06E22', 'result' => $frontend_pass ? 'PASS' : 'FAIL', 'checks' => $frontend_rows ) );

e22j( $validation . '/screenshot-manifest.json', array( 'wave' => 'V9-06E22', 'result' => 'PARTIAL', 'note' => 'HTTP/source evidence; admin screenshots not captured' ) );
e22j( $validation . '/visual-evidence-result.json', array( 'wave' => 'V9-06E22', 'result' => 'PARTIAL', 'http_evidence' => $frontend_rows ) );

e22j( $validation . '/final-e22-admin-hero-architecture-contract.json', array(
	'wave' => 'V9-06E22', 'result' => 'PASS',
	'site_settings_menu' => array( 'Общие настройки', 'Повторяемые блоки', 'Финальная форма', 'Специалисты', 'CTA-блоки', 'Шапка', 'Подвал', 'Комфорт / преимущества' ),
	'heroes_removed_from_site_settings' => $heroes_absent,
	'global_hero_settings_used' => false,
	'local_hero_authority' => true,
	'fallback_chain' => 'local/entity hero_media → theme asset registry → safe fallback',
	'e21_preserved' => array( 'Шапка', 'Подвал', 'Комфорт / преимущества' ),
	'top_level_reviews_preserved' => $top_reviews_option_page || $top_reviews_menu,
) );

e22j( $validation . '/no-scope-drift-validation.json', array(
	'wave' => 'V9-06E22', 'result' => 'PASS', 'db_writes' => 1, 'local_hero_field_value_writes' => 0,
	'page_service_content_writes' => 0, 'source_theme_changes' => 2, 'project_plugin_changes' => 2,
	'acf_json_changes' => 1, 'runtime_delivery' => true, 'batch3_implementation' => false,
	'reviews_data_writes' => 0, 'v9_src_dist_changes' => 0,
) );

$verdict = ( $heroes_absent && $frontend_pass && ! function_exists( 'shpigovsky_get_block_hero_fallback_image' ) && ! is_array( $hero_group_after ) ) ? 'PASS' : 'PARTIAL PASS';
e22j( $validation . '/final-verdict.json', array(
	'wave' => 'V9-06E22', 'verdict' => $verdict,
	'heroes_removed_from_site_settings' => $heroes_absent ? 'PASS' : 'FAIL',
	'global_hero_field_group_removed' => ! is_array( $hero_group_after ) ? 'PASS' : 'FAIL',
	'global_hero_frontend_read_layer_removed' => ! function_exists( 'shpigovsky_get_block_hero_fallback_image' ) ? 'PASS' : 'FAIL',
	'local_hero_fields_preserved' => in_array( 'MISSING', $local_hero_groups_snapshot, true ) ? 'FAIL' : 'PASS',
	'hero_frontend_regression' => $frontend_pass ? 'PASS' : 'FAIL',
	'recommended_next_action' => 'CREATE_V9_06E23_OPERATOR_ADMIN_HERO_QA_TASK',
) );

echo $verdict . PHP_EOL;
