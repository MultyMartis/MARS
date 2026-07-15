<?php
/**
 * FP-0002 V9-06D9-T — options reference meta + optional canonical row migration (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$reference_updates = array(
	'reviews_enabled'          => 'field_fp02_options_reviews_enabled',
	'reviews_section_heading'  => 'field_fp02_options_reviews_section_heading',
	'reviews_items'            => 'field_fp02_options_reviews_items',
);

$ref_writes = array();
foreach ( $reference_updates as $name => $field_key ) {
	$option_name = '_' . $name;
	$before      = get_option( $option_name );
	$updated     = update_option( $option_name, $field_key, false );
	$ref_writes[] = array(
		'option_name' => $option_name,
		'before'      => $before,
		'after'       => get_option( $option_name ),
		'ok'          => (bool) $updated || get_option( $option_name ) === $field_key,
	);
}

$rows_before = get_field( 'reviews_items', 'option' );
$row_count   = is_array( $rows_before ) ? count( $rows_before ) : 0;

$probe_before = function_exists( 'shpigovsky_get_reviews_option_items' )
	? shpigovsky_get_reviews_option_items()
	: array();

$migration_performed = false;
$migration_rows      = 0;

if ( is_array( $rows_before ) && ! empty( $rows_before ) ) {
	$first_keys = array_keys( $rows_before[0] );
	$needs_row_migration = in_array( 'author_label', $first_keys, true )
		|| in_array( 'text', $first_keys, true );

	if ( $needs_row_migration ) {
		$canonical_rows = array();
		foreach ( $rows_before as $row ) {
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

		if ( count( $canonical_rows ) === $row_count && function_exists( 'update_field' ) ) {
			$ok = update_field( 'reviews_items', $canonical_rows, 'option' );
			if ( $ok ) {
				$migration_performed = true;
				$migration_rows      = count( $canonical_rows );
			}
		}
	}
}

$rows_after = get_field( 'reviews_items', 'option' );
$probe_after = function_exists( 'shpigovsky_get_reviews_option_items' )
	? shpigovsky_get_reviews_option_items()
	: array();

$mode = function_exists( 'shpigovsky_get_reviews_source_mode' )
	? shpigovsky_get_reviews_source_mode()
	: ( ! empty( $probe_after ) ? 'OPTIONS' : 'FALLBACK' );

$first_after_keys = ( is_array( $rows_after ) && ! empty( $rows_after ) ) ? array_keys( $rows_after[0] ) : array();

echo wp_json_encode(
	array(
		'phase'                      => 'V9-06D9-T',
		'generated_at'               => gmdate( 'c' ),
		'reference_meta_updates'     => $ref_writes,
		'rows_before_count'          => $row_count,
		'rows_after_count'           => is_array( $rows_after ) ? count( $rows_after ) : 0,
		'helper_items_before'        => count( $probe_before ),
		'helper_items_after'         => count( $probe_after ),
		'first_row_keys_after'       => $first_after_keys,
		'migration_performed'        => $migration_performed,
		'migration_rows'             => $migration_rows,
		'mode'                       => empty( $probe_after ) && ! $migration_performed && count( $probe_before ) > 0
			? 'compatibility_helper_only'
			: ( $migration_performed ? 'canonical_meta_migrated' : 'compatibility_helper_only' ),
		'source_mode_after'          => $mode,
		'result'                     => ( is_array( $rows_after ) && count( $rows_after ) === 10 && count( $probe_after ) >= 1 )
			? 'PASS'
			: 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
