<?php
do_action( 'acf/init' );

$site_items = array();
if ( function_exists( 'acf_get_options_pages' ) ) {
	foreach ( (array) acf_get_options_pages() as $page ) {
		if ( ( $page['parent_slug'] ?? '' ) === 'fp02-site-settings' ) {
			$site_items[] = array(
				'title'   => (string) ( $page['menu_title'] ?? $page['page_title'] ?? '' ),
				'slug'    => (string) ( $page['menu_slug'] ?? '' ),
				'post_id' => (string) ( $page['post_id'] ?? '' ),
			);
		}
	}
}

$top_reviews = function_exists( 'acf_get_options_page' ) ? acf_get_options_page( 'fp02-reviews' ) : null;
$alias_page  = function_exists( 'acf_get_options_page' ) ? acf_get_options_page( 'fp02-block-reviews' ) : null;

$group = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$locations = array();
if ( is_array( $group['location'] ?? null ) ) {
	foreach ( $group['location'] as $rule_group ) {
		foreach ( (array) $rule_group as $rule ) {
			if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
				$locations[] = (string) ( $rule['value'] ?? '' );
			}
		}
	}
}

$review_rows   = 0;
$sample_author = '';
if ( function_exists( 'have_rows' ) ) {
	if ( have_rows( 'reviews_items', 'fp02-reviews' ) ) {
		while ( have_rows( 'reviews_items', 'fp02-reviews' ) ) {
			the_row();
			++$review_rows;
			if ( '' === $sample_author ) {
				$sample_author = (string) get_sub_field( 'review_author' );
			}
		}
	}
}

echo json_encode(
	array(
		'site_settings_submenu'  => $site_items,
		'reviews_alias_present'  => in_array( 'fp02-block-reviews', array_column( $site_items, 'slug' ), true ) || is_array( $alias_page ),
		'alias_page_registered'  => is_array( $alias_page ),
		'top_level_reviews'      => is_array( $top_reviews ) && empty( $top_reviews['parent_slug'] ?? '' ),
		'field_group_locations'  => $locations,
		'reviews_data'           => array(
			'context'       => 'fp02-reviews',
			'review_rows'   => $review_rows,
			'sample_author' => $sample_author,
		),
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
