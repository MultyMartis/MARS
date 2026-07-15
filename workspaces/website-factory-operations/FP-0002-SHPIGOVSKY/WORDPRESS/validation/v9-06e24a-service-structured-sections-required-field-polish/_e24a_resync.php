<?php
/**
 * E24A ACF resync — structured sections optional programme fields.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */

ini_set( 'display_errors', '1' );
error_reporting( E_ALL );

$root       = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime    = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$validation = $root . '/validation/v9-06e24a-service-structured-sections-required-field-polish';

define( 'WP_USE_THEMES', false );
require_once $runtime . '/wp-load.php';

$group_key = 'group_fp02_service_structured_sections';
$json_dir  = $root . '/acf-json/';
$rows      = array();

$export_group = null;
if ( class_exists( '\\Shpigovsky\\Core\\Fields\\FieldGroups' ) ) {
	foreach ( \Shpigovsky\Core\Fields\FieldGroups::get_field_groups() as $candidate ) {
		if ( is_array( $candidate ) && ( $candidate['key'] ?? '' ) === $group_key ) {
			$export_group = $candidate;
			break;
		}
	}
}

$group = is_array( $export_group ) ? $export_group : ( function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $group_key ) : null );
if ( ! is_array( $group ) ) {
	$rows[] = array( 'field_group' => $group_key, 'result' => 'FAIL', 'note' => 'group missing' );
} else {
	$fields = is_array( $export_group ) ? ( $export_group['fields'] ?? array() ) : ( function_exists( 'acf_get_fields' ) ? acf_get_fields( $group_key ) : array() );
	$programme = null;
	foreach ( (array) $fields as $field ) {
		if ( is_array( $field ) && ( $field['name'] ?? '' ) === 'programme_items' ) {
			$programme = $field;
			break;
		}
	}
	if ( ! is_array( $programme ) ) {
		$rows[] = array( 'field_group' => $group_key, 'result' => 'FAIL', 'note' => 'programme_items missing' );
	} else {
		$export = $group;
		$export['fields'] = $fields;
		unset( $export['ID'] );
		$path = $json_dir . $group_key . '.json';
		file_put_contents( $path, wp_json_encode( $export, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
		$rt_json = $runtime . '/wp-content/acf-json/' . $group_key . '.json';
		if ( ! is_dir( dirname( $rt_json ) ) ) {
			wp_mkdir_p( dirname( $rt_json ) );
		}
		copy( $path, $rt_json );
		if ( function_exists( 'acf_import_field_group' ) ) {
			acf_import_field_group( json_decode( file_get_contents( $path ), true ) );
		}
		$sub_required = array();
		foreach ( (array) ( $programme['sub_fields'] ?? array() ) as $sub ) {
			$sub_required[] = array(
				'name'     => $sub['name'] ?? '',
				'label'    => $sub['label'] ?? '',
				'required' => (int) ( $sub['required'] ?? 0 ),
			);
		}
		$rows[] = array(
			'field_group'              => $group_key,
			'programme_items_label'    => $programme['label'] ?? '',
			'programme_items_required' => (int) ( $programme['required'] ?? 0 ),
			'sub_fields'               => $sub_required,
			'sync'                     => 'php_export_import',
			'result'                   => 'PASS',
		);
	}
}

$acf_pass = ! in_array( 'FAIL', array_column( $rows, 'result' ), true );

file_put_contents(
	$validation . '/acf-sync-result.json',
	wp_json_encode(
		array(
			'wave'   => 'V9-06E24A',
			'result' => $acf_pass ? 'PASS' : 'FAIL',
			'groups' => $rows,
		),
		JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
	)
);

echo wp_json_encode( array( 'result' => $acf_pass ? 'PASS' : 'FAIL', 'groups' => $rows ), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );
