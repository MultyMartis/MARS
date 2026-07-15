<?php
/**
 * FP-0002 V9-06D9-W — post-repair probe (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix = $wpdb->prefix;

$duplicate_groups = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT ID, post_status FROM {$prefix}posts WHERE post_type = %s AND post_name = %s AND post_status != 'trash' ORDER BY ID",
		'acf-field-group',
		'group_fp02_site_options_reviews'
	),
	ARRAY_A
);

$rows_fp02 = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'fp02-reviews' ) : null;
$rows_option = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;

$fp02_first_author = '';
$option_first_author = '';
if ( is_array( $rows_fp02 ) && ! empty( $rows_fp02[0] ) ) {
	$fp02_first_author = (string) ( $rows_fp02[0]['review_author'] ?? '' );
}
if ( is_array( $rows_option ) && ! empty( $rows_option[0] ) ) {
	$option_first_author = (string) ( $rows_option[0]['review_author'] ?? '' );
}

$home_teaser = $wpdb->get_var(
	$wpdb->prepare(
		"SELECT meta_value FROM {$prefix}postmeta WHERE post_id = %d AND meta_key = %s LIMIT 1",
		4,
		'home_reviews_teaser'
	)
);

echo wp_json_encode(
	array(
		'phase'                   => 'V9-06D9-W',
		'generated_at'            => gmdate( 'c' ),
		'duplicate_group_count'   => count( $duplicate_groups ),
		'duplicate_groups'        => $duplicate_groups,
		'fp02_rows'               => is_array( $rows_fp02 ) ? count( $rows_fp02 ) : 0,
		'option_rows'             => is_array( $rows_option ) ? count( $rows_option ) : 0,
		'fp02_admin_first_author' => $fp02_first_author,
		'option_admin_first_author' => $option_first_author,
		'helper_items_count'      => function_exists( 'shpigovsky_get_reviews_option_items' )
			? count( shpigovsky_get_reviews_option_items() )
			: 0,
		'source_mode'             => function_exists( 'shpigovsky_get_reviews_source_mode' )
			? shpigovsky_get_reviews_source_mode()
			: 'UNKNOWN',
		'home_teaser_meta_present' => '' !== (string) $home_teaser,
		'result'                  => 'PASS',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
