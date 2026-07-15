<?php
/**
 * FP-0002 V9-06D9-W — ACF sync verification (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;

echo wp_json_encode(
	array(
		'phase'          => 'V9-06D9-W',
		'generated_at'   => gmdate( 'c' ),
		'group_id'       => $group['ID'] ?? null,
		'group_location' => $group['location'] ?? null,
		'group_active'   => $group['active'] ?? null,
		'json_location'  => 'fp02-reviews',
		'result'         => (
			is_array( $group )
			&& ( $group['location'][0][0]['value'] ?? '' ) === 'fp02-reviews'
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
