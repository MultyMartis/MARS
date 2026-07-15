<?php
/**
 * E24A probe — structured sections field audit (NOT FOR GIT).
 */

ini_set( 'display_errors', '1' );
error_reporting( E_ALL );

define( 'WP_USE_THEMES', false );
require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$service_ids = array( 73, 74 );
$field_keys  = array(
	'field_fp02_programme_items_service',
	'field_fp02_programme_item_title_service',
	'field_fp02_programme_item_text_service',
	'field_fp02_signs_items_service',
	'field_fp02_stages_service',
);

$fields = array();
foreach ( $field_keys as $key ) {
	$f = function_exists( 'acf_get_field' ) ? acf_get_field( $key ) : null;
	if ( ! is_array( $f ) ) {
		$fields[ $key ] = null;
		continue;
	}
	$entry = array(
		'key'      => $f['key'] ?? '',
		'label'    => $f['label'] ?? '',
		'name'     => $f['name'] ?? '',
		'type'     => $f['type'] ?? '',
		'required' => (int) ( $f['required'] ?? 0 ),
		'min'      => $f['min'] ?? null,
		'max'      => $f['max'] ?? null,
	);
	if ( ! empty( $f['sub_fields'] ) && is_array( $f['sub_fields'] ) ) {
		$entry['sub_fields'] = array();
		foreach ( $f['sub_fields'] as $sub ) {
			$entry['sub_fields'][] = array(
				'key'      => $sub['key'] ?? '',
				'label'    => $sub['label'] ?? '',
				'name'     => $sub['name'] ?? '',
				'type'     => $sub['type'] ?? '',
				'required' => (int) ( $sub['required'] ?? 0 ),
			);
		}
	}
	$fields[ $key ] = $entry;
}

$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_service_structured_sections' ) : null;

$meta = array();
foreach ( $service_ids as $post_id ) {
	$post = get_post( $post_id );
	$meta[ $post_id ] = array(
		'title'           => $post ? $post->post_title : '',
		'slug'            => $post ? $post->post_name : '',
		'programme_items' => get_field( 'programme_items', $post_id ),
		'hero_cta_label'  => get_field( 'hero_cta_label', $post_id ),
	);
}

// Simulate ACF validation for empty programme row (title only, empty text).
$validation = array();
if ( function_exists( 'acf_validate_value' ) ) {
	$test_row = array( array( 'title' => 'Test', 'text' => '' ) );
	$field    = acf_get_field( 'field_fp02_programme_items_service' );
	if ( is_array( $field ) ) {
		$valid = acf_validate_value( $test_row, $field, "acf[{$field['key']}]" );
		$validation['programme_items_title_only'] = ( true === $valid ) ? 'PASS' : $valid;
	}
	$valid_empty = acf_validate_value( array(), $field, "acf[{$field['key']}]" );
	$validation['programme_items_empty'] = ( true === $valid_empty ) ? 'PASS' : $valid_empty;
}

echo wp_json_encode(
	array(
		'group_title' => is_array( $group ) ? ( $group['title'] ?? '' ) : null,
		'fields'      => $fields,
		'service_meta'=> $meta,
		'validation'  => $validation,
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
