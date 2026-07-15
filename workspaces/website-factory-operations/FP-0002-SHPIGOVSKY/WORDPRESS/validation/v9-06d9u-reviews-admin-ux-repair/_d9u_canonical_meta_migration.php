<?php
/**
 * FP-0002 V9-06D9-U — canonical reviews options meta migration (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix = $wpdb->prefix;

$rows_before = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;
$row_count   = is_array( $rows_before ) ? count( $rows_before ) : 0;

$probe_before = function_exists( 'shpigovsky_get_reviews_option_items' )
	? shpigovsky_get_reviews_option_items()
	: array();

$first_before_keys = ( is_array( $rows_before ) && ! empty( $rows_before ) ) ? array_keys( $rows_before[0] ) : array();

$canonical_rows = array();
if ( is_array( $rows_before ) ) {
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
}

$reference_updates = array(
	'reviews_enabled'         => 'field_fp02_options_reviews_enabled',
	'reviews_section_heading' => 'field_fp02_options_reviews_section_heading',
	'reviews_items'           => 'field_fp02_options_reviews_items',
);

$ref_writes = array();
foreach ( $reference_updates as $name => $field_key ) {
	$option_name = '_' . $name;
	$before      = get_option( $option_name );
	update_option( $option_name, $field_key, false );
	$ref_writes[] = array(
		'option_name' => $option_name,
		'before'      => $before,
		'after'       => get_option( $option_name ),
	);
}

$migration_performed = false;
$migration_rows      = 0;
$migration_error     = null;

if ( $row_count > 0 && count( $canonical_rows ) === $row_count && function_exists( 'update_field' ) ) {
	$ok = update_field( 'reviews_items', $canonical_rows, 'option' );
	if ( $ok ) {
		$migration_performed = true;
		$migration_rows      = count( $canonical_rows );
	} else {
		$migration_error = 'update_field returned false';
	}
}

$rows_after = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;
$first_after_keys = ( is_array( $rows_after ) && ! empty( $rows_after ) ) ? array_keys( $rows_after[0] ) : array();

$probe_after = function_exists( 'shpigovsky_get_reviews_option_items' )
	? shpigovsky_get_reviews_option_items()
	: array();

$canonical_meta_keys = $wpdb->get_col(
	"SELECT option_name FROM {$prefix}options WHERE option_name LIKE 'reviews_items_%review_%' OR option_name LIKE '_reviews_items_%review_%' ORDER BY option_name LIMIT 50"
);

$legacy_meta_keys = $wpdb->get_col(
	"SELECT option_name FROM {$prefix}options WHERE option_name LIKE 'reviews_items_%author_label%' OR option_name LIKE 'reviews_items_%_text' OR option_name LIKE 'reviews_items_%metadata%' OR option_name LIKE '_reviews_items_%author_label%' ORDER BY option_name LIMIT 50"
);

$mode = function_exists( 'shpigovsky_get_reviews_source_mode' )
	? shpigovsky_get_reviews_source_mode()
	: ( ! empty( $probe_after ) ? 'OPTIONS' : 'FALLBACK' );

$admin_first_author = '';
$admin_first_text   = '';
if ( is_array( $rows_after ) && ! empty( $rows_after[0] ) ) {
	$admin_first_author = (string) ( $rows_after[0]['review_author'] ?? '' );
	$admin_first_text   = (string) ( $rows_after[0]['review_text'] ?? '' );
}

echo wp_json_encode(
	array(
		'phase'                     => 'V9-06D9-U',
		'generated_at'              => gmdate( 'c' ),
		'reference_meta_updates'    => $ref_writes,
		'rows_before_count'         => $row_count,
		'rows_after_count'          => is_array( $rows_after ) ? count( $rows_after ) : 0,
		'first_row_keys_before'     => $first_before_keys,
		'first_row_keys_after'      => $first_after_keys,
		'admin_first_author'        => $admin_first_author,
		'admin_first_text_length'   => strlen( $admin_first_text ),
		'helper_items_before'       => count( $probe_before ),
		'helper_items_after'        => count( $probe_after ),
		'migration_performed'       => $migration_performed,
		'migration_rows'            => $migration_rows,
		'migration_error'           => $migration_error,
		'canonical_meta_keys_sample'=> $canonical_meta_keys,
		'legacy_meta_keys_remaining'=> $legacy_meta_keys,
		'source_mode_after'         => $mode,
		'result'                    => (
			$migration_performed
			&& is_array( $rows_after )
			&& count( $rows_after ) === 10
			&& in_array( 'review_author', $first_after_keys, true )
			&& in_array( 'review_text', $first_after_keys, true )
			&& '' !== $admin_first_author
			&& count( $probe_after ) === 10
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
