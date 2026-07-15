<?php
/**
 * FP-0002 V9-06D9-W — baseline probe (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix = $wpdb->prefix;

$duplicate_groups = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT ID, post_name, post_title, post_status, post_modified FROM {$prefix}posts WHERE post_type = %s AND post_name = %s ORDER BY ID",
		'acf-field-group',
		'group_fp02_site_options_reviews'
	),
	ARRAY_A
);

foreach ( $duplicate_groups as $index => $group_row ) {
	$content = $wpdb->get_var(
		$wpdb->prepare(
			"SELECT post_content FROM {$prefix}posts WHERE ID = %d",
			$group_row['ID']
		)
	);
	$location = 'unknown';
	if ( false !== strpos( $content, 'fp02-reviews' ) ) {
		$location = 'fp02-reviews';
	} elseif ( false !== strpos( $content, 'fp02-site-settings' ) ) {
		$location = 'fp02-site-settings';
	}
	$duplicate_groups[ $index ]['location_hint'] = $location;
}

$rows_option = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;
$rows_fp02   = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'fp02-reviews' ) : null;

$option_first_author = '';
$fp02_first_author   = '';
if ( is_array( $rows_option ) && ! empty( $rows_option[0] ) ) {
	$option_first_author = (string) ( $rows_option[0]['review_author'] ?? $rows_option[0]['author_label'] ?? '' );
}
if ( is_array( $rows_fp02 ) && ! empty( $rows_fp02[0] ) ) {
	$fp02_first_author = (string) ( $rows_fp02[0]['review_author'] ?? $rows_fp02[0]['author_label'] ?? '' );
}

$home_html   = wp_remote_retrieve_body( wp_remote_get( home_url( '/' ) ) );
$otzyvy_html = wp_remote_retrieve_body( wp_remote_get( home_url( '/otzyvy/' ) ) );

echo wp_json_encode(
	array(
		'phase'                       => 'V9-06D9-W',
		'generated_at'                => gmdate( 'c' ),
		'duplicate_group_count'       => count( $duplicate_groups ),
		'duplicate_groups'            => $duplicate_groups,
		'option_rows'                 => is_array( $rows_option ) ? count( $rows_option ) : 0,
		'fp02_rows'                   => is_array( $rows_fp02 ) ? count( $rows_fp02 ) : 0,
		'option_admin_first_author'   => $option_first_author,
		'fp02_admin_first_author'     => $fp02_first_author,
		'helper_items_count'          => function_exists( 'shpigovsky_get_reviews_option_items' )
			? count( shpigovsky_get_reviews_option_items() )
			: 0,
		'source_mode'                 => function_exists( 'shpigovsky_get_reviews_source_mode' )
			? shpigovsky_get_reviews_source_mode()
			: 'UNKNOWN',
		'home_slide_count'            => substr_count( $home_html, 'reviews__slide swiper-slide' ),
		'frontend_otzyvy_uses_slider' => false !== strpos( $otzyvy_html, 'reviews__slider swiper' ),
		'frontend_otzyvy_has_archive' => false !== strpos( $otzyvy_html, 'reviews-archive' ) && false !== strpos( $otzyvy_html, 'review-archive-card' ),
		'result'                      => 'PASS',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
