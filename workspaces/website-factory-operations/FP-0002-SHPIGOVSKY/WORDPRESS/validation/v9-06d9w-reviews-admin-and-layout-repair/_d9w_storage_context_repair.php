<?php
/**
 * FP-0002 V9-06D9-W — reviews storage context repair (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix       = $wpdb->prefix;
$source_prefix = 'options_reviews_';
$target_prefix = 'fp02-reviews_reviews_';
$ref_map       = array(
	'_' . $target_prefix . 'enabled'         => 'field_fp02_options_reviews_enabled',
	'_' . $target_prefix . 'section_heading' => 'field_fp02_options_reviews_section_heading',
	'_' . $target_prefix . 'items'           => 'field_fp02_options_reviews_items',
	'_' . $target_prefix . 'items_%_review_author'   => 'field_fp02_options_review_author',
	'_' . $target_prefix . 'items_%_review_text'     => 'field_fp02_options_review_text',
	'_' . $target_prefix . 'items_%_review_context'  => 'field_fp02_options_review_context',
	'_' . $target_prefix . 'items_%_review_source'   => 'field_fp02_options_review_source',
	'_' . $target_prefix . 'items_%_review_date'     => 'field_fp02_options_review_date',
	'_' . $target_prefix . 'items_%_review_rating'   => 'field_fp02_options_review_rating',
	'_' . $target_prefix . 'items_%_review_visible'  => 'field_fp02_options_review_visible',
	'_' . $target_prefix . 'items_%_review_featured' => 'field_fp02_options_review_featured',
);

$seed_path = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9s-controlled-reviews-options-seed/_seed_payload.json';
$seed      = json_decode( file_get_contents( $seed_path ), true );

if ( ! is_array( $seed ) || empty( $seed['reviews_items'] ) ) {
	echo wp_json_encode( array( 'result' => 'FAIL', 'error' => 'seed payload unavailable' ) );
	exit( 1 );
}

$canonical_rows = array();
foreach ( $seed['reviews_items'] as $row ) {
	if ( ! is_array( $row ) ) {
		continue;
	}
	$canonical_rows[] = array(
		'review_author'   => $row['review_author'] ?? $row['author_label'] ?? $row['author'] ?? '',
		'review_text'     => $row['review_text'] ?? $row['text'] ?? '',
		'review_context'  => $row['review_context'] ?? $row['metadata'] ?? '',
		'review_source'   => $row['review_source'] ?? $row['source'] ?? '',
		'review_date'     => $row['review_date'] ?? $row['date'] ?? '',
		'review_rating'   => isset( $row['review_rating'] ) ? (int) $row['review_rating'] : ( isset( $row['rating'] ) ? (int) $row['rating'] : 5 ),
		'review_visible'  => array_key_exists( 'review_visible', $row ) ? (bool) $row['review_visible'] : ( array_key_exists( 'visible', $row ) ? (bool) $row['visible'] : true ),
		'review_featured' => array_key_exists( 'review_featured', $row ) ? (bool) $row['review_featured'] : ( array_key_exists( 'featured', $row ) ? (bool) $row['featured'] : true ),
	);
}

$option_writes = 0;
if ( function_exists( 'update_field' ) ) {
	update_field( 'reviews_enabled', (bool) ( $seed['reviews_enabled'] ?? true ), 'option' );
	update_field( 'reviews_section_heading', (string) ( $seed['reviews_section_heading'] ?? 'Отзывы' ), 'option' );
	update_field( 'reviews_items', $canonical_rows, 'option' );
	$option_writes = 3;
}

$source_rows = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE %s OR option_name LIKE %s ORDER BY option_name",
		$source_prefix . '%',
		'_' . $source_prefix . '%'
	),
	ARRAY_A
);

$copied = array();
foreach ( $source_rows as $row ) {
	$source_name = $row['option_name'];
	$target_name = str_replace( 'options_reviews_', $target_prefix, $source_name );
	$target_name = str_replace( '_options_reviews_', '_fp02-reviews_reviews_', $target_name );

	$value = $row['option_value'];

	if ( 0 === strpos( $source_name, '_' ) ) {
		if ( '_options_reviews_enabled' === $source_name ) {
			$value = 'field_fp02_options_reviews_enabled';
		} elseif ( '_options_reviews_section_heading' === $source_name ) {
			$value = 'field_fp02_options_reviews_section_heading';
		} elseif ( '_options_reviews_items' === $source_name ) {
			$value = 'field_fp02_options_reviews_items';
		} elseif ( preg_match( '/_options_reviews_items_\d+_review_([a-z_]+)$/', $source_name, $matches ) ) {
			$value = 'field_fp02_options_review_' . $matches[1];
		}
	}

	update_option( $target_name, $value, false );
	$copied[] = array(
		'source' => $source_name,
		'target' => $target_name,
	);
}

$fp02_rows = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'fp02-reviews' ) : null;
$option_rows = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;

$fp02_first = '';
$option_first = '';
if ( is_array( $fp02_rows ) && ! empty( $fp02_rows[0] ) ) {
	$fp02_first = (string) ( $fp02_rows[0]['review_author'] ?? '' );
}
if ( is_array( $option_rows ) && ! empty( $option_rows[0] ) ) {
	$option_first = (string) ( $option_rows[0]['review_author'] ?? '' );
}

$helper_count = function_exists( 'shpigovsky_get_reviews_option_items' )
	? count( shpigovsky_get_reviews_option_items() )
	: 0;
$source_mode = function_exists( 'shpigovsky_get_reviews_source_mode' )
	? shpigovsky_get_reviews_source_mode()
	: 'UNKNOWN';

echo wp_json_encode(
	array(
		'phase'                   => 'V9-06D9-W',
		'generated_at'            => gmdate( 'c' ),
		'seed_rows'               => count( $canonical_rows ),
		'option_update_field_writes' => $option_writes,
		'meta_copied_count'       => count( $copied ),
		'meta_copied_sample'      => array_slice( $copied, 0, 8 ),
		'fp02_rows_after'         => is_array( $fp02_rows ) ? count( $fp02_rows ) : 0,
		'option_rows_after'       => is_array( $option_rows ) ? count( $option_rows ) : 0,
		'fp02_admin_first_author' => $fp02_first,
		'option_admin_first_author' => $option_first,
		'helper_items_count'      => $helper_count,
		'source_mode'             => $source_mode,
		'result'                  => (
			is_array( $fp02_rows )
			&& count( $fp02_rows ) === 10
			&& '' !== $fp02_first
			&& 10 === $helper_count
			&& 'OPTIONS' === $source_mode
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
