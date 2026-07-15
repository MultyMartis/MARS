<?php
/**
 * FP-0002 V9-06D9-U — post-repair admin validation (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix = $wpdb->prefix;

$teaser_field = function_exists( 'acf_get_field' ) ? acf_get_field( 'field_fp02_home_reviews_teaser' ) : null;
$teaser_prepared = null;
if ( is_array( $teaser_field ) && function_exists( 'acf_prepare_field' ) ) {
	$teaser_prepared = acf_prepare_field( $teaser_field );
}

$rows = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;
$first_keys = ( is_array( $rows ) && ! empty( $rows ) ) ? array_keys( $rows[0] ) : array();
$first_author = is_array( $rows ) && ! empty( $rows[0] ) ? (string) ( $rows[0]['review_author'] ?? $rows[0]['author_label'] ?? '' ) : '';
$first_text_len = is_array( $rows ) && ! empty( $rows[0] ) ? strlen( (string) ( $rows[0]['review_text'] ?? $rows[0]['text'] ?? '' ) ) : 0;

$reviews_location = 'unknown';
if ( function_exists( 'acf_get_field_group' ) ) {
	$group = acf_get_field_group( 'group_fp02_site_options_reviews' );
	if ( is_array( $group ) && ! empty( $group['location'] ) ) {
		foreach ( $group['location'] as $rule_group ) {
			foreach ( $rule_group as $rule ) {
				if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
					$reviews_location = (string) ( $rule['value'] ?? 'unknown' );
					break 2;
				}
			}
		}
	}
}

$reviews_menu_registered = function_exists( 'acf_get_options_page' ) && (bool) acf_get_options_page( 'fp02-reviews' );

$home_meta = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT meta_key FROM {$prefix}postmeta WHERE post_id = %d AND meta_key LIKE %s",
		4,
		'home_reviews_teaser%'
	),
	ARRAY_A
);

echo wp_json_encode(
	array(
		'phase'                              => 'V9-06D9-U',
		'generated_at'                       => gmdate( 'c' ),
		'home_reviews_teaser_field_exists'   => is_array( $teaser_field ),
		'home_reviews_teaser_visible_admin'  => false !== $teaser_prepared,
		'home_reviews_teaser_orphan_meta_keys'=> wp_list_pluck( $home_meta, 'meta_key' ),
		'reviews_top_level_menu_registered'  => $reviews_menu_registered,
		'reviews_group_location'             => $reviews_location,
		'reviews_items_count'                => is_array( $rows ) ? count( $rows ) : 0,
		'first_row_keys'                     => $first_keys,
		'first_row_author_populated'         => '' !== $first_author,
		'first_row_text_length'              => $first_text_len,
		'canonical_fields_in_first_row'      => in_array( 'review_author', $first_keys, true ) && in_array( 'review_text', $first_keys, true ),
		'reviews_items_required'             => is_array( $teaser_field ) ? (bool) ( $teaser_field['required'] ?? false ) : null,
		'helper_option_items_count'          => function_exists( 'shpigovsky_get_reviews_option_items' )
			? count( shpigovsky_get_reviews_option_items() )
			: 0,
		'source_mode'                        => function_exists( 'shpigovsky_get_reviews_source_mode' )
			? shpigovsky_get_reviews_source_mode()
			: 'UNKNOWN',
		'home_save_blocker_expected_removed' => false === $teaser_prepared,
		'result'                             => (
			false === $teaser_prepared
			&& $reviews_menu_registered
			&& 'fp02-reviews' === $reviews_location
			&& is_array( $rows )
			&& count( $rows ) === 10
			&& in_array( 'review_author', $first_keys, true )
			&& '' !== $first_author
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
