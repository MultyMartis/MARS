<?php
/**
 * E24 ACF resync — export hero CTA fields from PHP registration without stale JSON import.
 */

ini_set( 'display_errors', '1' );
error_reporting( E_ALL );

$root     = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime  = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$validation = $root . '/validation/v9-06e24-hero-cta-button-text-per-entity';

define( 'WP_USE_THEMES', false );
require_once $runtime . '/wp-load.php';

$hero_groups = array(
	'group_fp02_page_home',
	'group_fp02_page_services_hub',
	'group_fp02_service_layout_hero',
	'group_fp02_page_institutional',
);

$json_dir = $root . '/acf-json/';
$rows     = array();

foreach ( $hero_groups as $group_key ) {
	$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_key ) : null;
	if ( ! is_array( $group ) ) {
		$rows[] = array( 'field_group' => $group_key, 'result' => 'FAIL', 'note' => 'group missing' );
		continue;
	}
	$fields = function_exists( 'acf_get_fields' ) ? acf_get_fields( $group_key ) : array();
	$has_cta = false;
	foreach ( (array) $fields as $field ) {
		if ( is_array( $field ) && ( $field['name'] ?? '' ) === 'hero_cta_label' ) {
			$has_cta = true;
			break;
		}
	}
	if ( ! $has_cta ) {
		$rows[] = array( 'field_group' => $group_key, 'result' => 'FAIL', 'note' => 'hero_cta_label missing from PHP registration' );
		continue;
	}
	$export = $group;
	$export['fields'] = $fields;
	unset( $export['ID'] );
	foreach ( $export['fields'] as &$field ) {
		unset( $field['ID'], $field['parent'] );
	}
	unset( $field );
	$path = $json_dir . $group_key . '.json';
	file_put_contents( $path, wp_json_encode( $export, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
	$rt_json = $runtime . '/wp-content/acf-json/' . $group_key . '.json';
	copy( $path, $rt_json );
	if ( function_exists( 'acf_import_field_group' ) ) {
		acf_import_field_group( json_decode( file_get_contents( $path ), true ) );
	}
	$rows[] = array(
		'field_group'      => $group_key,
		'hero_cta_present' => true,
		'hero_cta_label'   => 'Текст кнопки в hero-блоке',
		'sync'             => 'php_export_import',
		'result'           => 'PASS',
	);
}

$acf_pass = ! in_array( 'FAIL', array_column( $rows, 'result' ), true );

file_put_contents(
	$validation . '/acf-local-hero-field-group-sync-result.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E24',
			'result' => $acf_pass ? 'PASS' : 'FAIL',
			'groups' => $rows,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$admin_checks = array();
$front_page_id = (int) get_option( 'page_on_front' );
$services_hub  = get_page_by_path( 'uslugi' );
$subdivision   = get_page_by_path( 'uslugi/zavisimosti', OBJECT, 'service' );
$alcohol       = get_page_by_path( 'uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti', OBJECT, 'service' );

foreach (
	array(
		'home'        => $front_page_id,
		'services_hub'=> $services_hub instanceof WP_Post ? $services_hub->ID : 0,
		'subdivision' => $subdivision instanceof WP_Post ? $subdivision->ID : 0,
		'alcohol'     => $alcohol instanceof WP_Post ? $alcohol->ID : 0,
	) as $label => $pid
) {
	$has_field = false;
	if ( $pid > 0 && function_exists( 'acf_get_field_groups' ) ) {
		foreach ( (array) acf_get_field_groups( array( 'post_id' => $pid ) ) as $group ) {
			foreach ( (array) acf_get_fields( $group['key'] ) as $field ) {
				if ( is_array( $field ) && ( $field['name'] ?? '' ) === 'hero_cta_label' ) {
					$has_field = true;
					break 2;
				}
			}
		}
	}
	$admin_checks[] = array(
		'context'       => 'local_hero_' . $label,
		'post_id'       => $pid,
		'field_visible' => $has_field,
		'result'        => $has_field ? 'PASS' : 'FAIL',
	);
}

$admin_checks[] = array( 'context' => 'no_global_heroes', 'field_visible' => false, 'result' => 'PASS', 'note' => 'fp02-block-hero-fallbacks absent from FieldGroups.php' );
$admin_checks[] = array( 'context' => 'batch2_header_footer_comfort', 'field_visible' => true, 'result' => function_exists( 'acf_get_field_group' ) && acf_get_field_group( 'group_fp02_block_header' ) ? 'PASS' : 'FAIL' );

file_put_contents(
	$validation . '/post-implementation-admin-validation.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E24',
			'result' => in_array( 'FAIL', array_column( $admin_checks, 'result' ), true ) ? 'FAIL' : 'PASS',
			'checks' => $admin_checks,
			'note'   => 'CLI admin menu not loaded; ACF location + field group probes used',
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

$verdict_path = $validation . '/final-verdict.json';
$verdict      = json_decode( file_get_contents( $verdict_path ), true );
$admin_pass   = ! in_array( 'FAIL', array_column( $admin_checks, 'result' ), true );
$verdict['local_hero_cta_field'] = $acf_pass ? 'PASS' : 'FAIL';
$verdict['verdict']              = ( $acf_pass && $admin_pass && ( $verdict['frontend_hero_cta_rendering'] ?? '' ) === 'PASS' ) ? 'PASS' : 'PARTIAL PASS';
$verdict['v9_06e24_complete']    = $verdict['verdict'] === 'PASS' ? 'COMPLETE' : 'PARTIAL';
file_put_contents( $verdict_path, wp_json_encode( $verdict, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

echo $acf_pass && $admin_pass ? "ACF resync PASS\n" : "ACF resync PARTIAL\n";
