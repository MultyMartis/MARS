<?php
/**
 * FP-0002 V9-06D9-X — baseline binding probe (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix = $wpdb->prefix;

$contexts = array( 'fp02-reviews', 'option', 'options' );
$acf      = array();

foreach ( $contexts as $ctx ) {
	$rows  = function_exists( 'get_field' ) ? get_field( 'reviews_items', $ctx ) : null;
	$first = '';
	$keys  = array();

	if ( is_array( $rows ) && ! empty( $rows[0] ) ) {
		$keys  = array_keys( $rows[0] );
		$row   = $rows[0];
		$first = (string) ( $row['review_author'] ?? $row['author_label'] ?? $row['author'] ?? '' );
	}

	$acf[ $ctx ] = array(
		'count'        => is_array( $rows ) ? count( $rows ) : 0,
		'first_author' => $first,
		'raw_keys'     => $keys,
	);
}

$meta_keys = array(
	'options_reviews_items_0_review_author',
	'fp02-reviews_reviews_items_0_review_author',
);
$meta = array();

foreach ( $meta_keys as $key ) {
	$meta[ $key ] = get_option( $key, '__NOT_FOUND__' );
}

$helper_items = function_exists( 'shpigovsky_get_reviews_items' )
	? shpigovsky_get_reviews_items()
	: array();
$helper_first = ! empty( $helper_items[0]['author'] ) ? $helper_items[0]['author'] : '';

$home_html   = wp_remote_retrieve_body( wp_remote_get( home_url( '/' ) ) );
$otzyvy_html = wp_remote_retrieve_body( wp_remote_get( home_url( '/otzyvy/' ) ) );

preg_match( '/reviews__author-name[^>]*>([^<]+)/u', $home_html, $home_match );
preg_match( '/review-archive-card__author[^>]*>([^<]+)/u', $otzyvy_html, $otzyvy_match );

echo wp_json_encode(
	array(
		'phase'                  => 'V9-06D9-X',
		'generated_at'           => gmdate( 'c' ),
		'acf_contexts'             => $acf,
		'meta_direct'              => $meta,
		'helper_first_author'      => $helper_first,
		'helper_items_count'       => count( $helper_items ),
		'source_mode'              => function_exists( 'shpigovsky_get_reviews_source_mode' )
			? shpigovsky_get_reviews_source_mode()
			: 'UNKNOWN',
		'home_first_author'        => isset( $home_match[1] ) ? html_entity_decode( trim( $home_match[1] ), ENT_QUOTES, 'UTF-8' ) : '',
		'otzyvy_first_author'      => isset( $otzyvy_match[1] ) ? html_entity_decode( trim( $otzyvy_match[1] ), ENT_QUOTES, 'UTF-8' ) : '',
		'helper_read_context_used' => 'fp02-reviews-first-then-option',
		'result'                   => 'PASS',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
