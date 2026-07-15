<?php
/**
 * FP-0002 V9-06D9-U — sync reviews options ACF group (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$json_root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/';
$groups    = array(
	'group_fp02_site_options_reviews' => $json_root . 'group_fp02_site_options_reviews.json',
);

if ( ! function_exists( 'acf_import_field_group' ) ) {
	echo wp_json_encode( array( 'result' => 'FAIL', 'error' => 'acf_import_field_group unavailable' ) );
	exit( 1 );
}

$synced = array();
$results = array();

foreach ( $groups as $key => $path ) {
	$raw = json_decode( file_get_contents( $path ), true );
	if ( ! is_array( $raw ) ) {
		$results[] = array( 'group' => $key, 'result' => 'FAIL', 'error' => 'invalid json' );
		continue;
	}
	$import = acf_import_field_group( $raw );
	$results[] = array(
		'group'      => $key,
		'import_id'  => is_array( $import ) ? ( $import['ID'] ?? null ) : $import,
		'location'   => $raw['location'][0][0]['value'] ?? null,
		'result'     => 'PASS',
	);
	$synced[] = $key;
}

$options_field = acf_get_field( 'field_fp02_options_reviews_items' );
$options_subs  = array();
if ( ! empty( $options_field['sub_fields'] ) ) {
	foreach ( $options_field['sub_fields'] as $sf ) {
		$options_subs[] = array(
			'key'  => $sf['key'] ?? '',
			'name' => $sf['name'] ?? '',
		);
	}
}

$group_row = get_posts(
	array(
		'post_type'      => 'acf-field-group',
		'name'           => 'group_fp02_site_options_reviews',
		'posts_per_page' => 1,
		'post_status'    => 'any',
	)
);
$location_value = null;
if ( ! empty( $group_row[0]->post_content ) ) {
	$location_value = false !== strpos( $group_row[0]->post_content, 'fp02-reviews' )
		? 'fp02-reviews'
		: ( false !== strpos( $group_row[0]->post_content, 'fp02-site-settings' ) ? 'fp02-site-settings' : 'other' );
}

echo wp_json_encode(
	array(
		'phase'                          => 'V9-06D9-U',
		'generated_at'                   => gmdate( 'c' ),
		'synced_groups'                  => $synced,
		'import_results'                 => $results,
		'options_reviews_items_subfields'=> $options_subs,
		'reviews_group_location_after'   => $location_value,
		'result'                         => (
			in_array( 'review_author', wp_list_pluck( $options_subs, 'name' ), true )
			&& 'fp02-reviews' === $location_value
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
