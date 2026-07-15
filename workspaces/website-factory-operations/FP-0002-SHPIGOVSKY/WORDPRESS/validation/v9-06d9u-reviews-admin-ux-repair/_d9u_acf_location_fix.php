<?php
/**
 * FP-0002 V9-06D9-U — update active reviews group location in-place (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$json_path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_site_options_reviews.json';
$raw       = json_decode( file_get_contents( $json_path ), true );

$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;

if ( ! is_array( $group ) || ! function_exists( 'acf_update_field_group' ) ) {
	echo wp_json_encode( array( 'result' => 'FAIL', 'error' => 'acf group unavailable' ) );
	exit( 1 );
}

$before_id       = $group['ID'] ?? null;
$before_location = $group['location'] ?? null;

$group['location'] = $raw['location'] ?? $group['location'];
$updated           = acf_update_field_group( $group );
$after             = acf_get_field_group( 'group_fp02_site_options_reviews' );

echo wp_json_encode(
	array(
		'phase'            => 'V9-06D9-U',
		'generated_at'     => gmdate( 'c' ),
		'group_id'         => $before_id,
		'location_before'  => $before_location,
		'location_after'   => $after['location'] ?? null,
		'update_ok'        => (bool) $updated,
		'result'           => (
			is_array( $after['location'][0][0] ?? null )
			&& ( $after['location'][0][0]['value'] ?? '' ) === 'fp02-reviews'
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
