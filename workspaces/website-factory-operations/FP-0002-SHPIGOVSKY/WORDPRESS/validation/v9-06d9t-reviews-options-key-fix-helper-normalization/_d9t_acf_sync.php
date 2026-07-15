<?php
/**
 * FP-0002 V9-06D9-T — sync repaired options reviews ACF group (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$json_path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_site_options_reviews.json';
$raw       = json_decode( file_get_contents( $json_path ), true );

if ( ! is_array( $raw ) || ! function_exists( 'acf_import_field_group' ) ) {
	echo wp_json_encode(
		array(
			'result' => 'FAIL',
			'error'  => 'acf_import_field_group unavailable',
		)
	);
	exit( 1 );
}

$before_field = acf_get_field( 'field_fp02_reviews_items' );
$before_subs  = array();
if ( ! empty( $before_field['sub_fields'] ) ) {
	foreach ( $before_field['sub_fields'] as $sf ) {
		$before_subs[] = array(
			'key'  => $sf['key'] ?? '',
			'name' => $sf['name'] ?? '',
		);
	}
}

$import_result = acf_import_field_group( $raw );

$options_field = acf_get_field( 'field_fp02_options_reviews_items' );
$page_field    = acf_get_field( 'field_fp02_reviews_items' );

$options_subs = array();
if ( ! empty( $options_field['sub_fields'] ) ) {
	foreach ( $options_field['sub_fields'] as $sf ) {
		$options_subs[] = array(
			'key'  => $sf['key'] ?? '',
			'name' => $sf['name'] ?? '',
		);
	}
}

$page_subs = array();
if ( ! empty( $page_field['sub_fields'] ) ) {
	foreach ( $page_field['sub_fields'] as $sf ) {
		$page_subs[] = array(
			'key'  => $sf['key'] ?? '',
			'name' => $sf['name'] ?? '',
		);
	}
}

$synced_groups = array( 'group_fp02_site_options_reviews' );

echo wp_json_encode(
	array(
		'phase'                         => 'V9-06D9-T',
		'generated_at'                  => gmdate( 'c' ),
		'synced_groups'                 => $synced_groups,
		'before_reviews_items_subfields'=> $before_subs,
		'options_reviews_items_subfields'=> $options_subs,
		'page_reviews_items_subfields'  => $page_subs,
		'options_field_key'             => $options_field['key'] ?? null,
		'page_field_key'                => $page_field['key'] ?? null,
		'keys_distinct'                 => ( $options_field['key'] ?? '' ) !== ( $page_field['key'] ?? '' ),
		'import_result_id'              => is_array( $import_result ) ? ( $import_result['ID'] ?? null ) : $import_result,
		'result'                        => (
			! empty( $options_field )
			&& 'field_fp02_options_reviews_items' === ( $options_field['key'] ?? '' )
			&& in_array( 'review_author', wp_list_pluck( $options_subs, 'name' ), true )
		) ? 'PASS' : 'FAIL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
