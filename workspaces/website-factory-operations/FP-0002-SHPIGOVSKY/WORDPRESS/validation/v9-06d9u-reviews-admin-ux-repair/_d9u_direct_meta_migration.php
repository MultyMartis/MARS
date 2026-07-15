<?php
/**
 * FP-0002 V9-06D9-U — direct options_* canonical meta migration (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$field_refs = array(
	'review_author'   => 'field_fp02_options_review_author',
	'review_text'     => 'field_fp02_options_review_text',
	'review_context'  => 'field_fp02_options_review_context',
	'review_source'   => 'field_fp02_options_review_source',
	'review_date'     => 'field_fp02_options_review_date',
	'review_rating'   => 'field_fp02_options_review_rating',
	'review_visible'  => 'field_fp02_options_review_visible',
	'review_featured' => 'field_fp02_options_review_featured',
);

$legacy_map = array(
	'review_author'  => 'author_label',
	'review_text'    => 'text',
	'review_context' => 'metadata',
	'review_source'  => 'source',
);

$count = (int) get_option( 'options_reviews_items', 0 );
if ( $count <= 0 ) {
	$count = (int) get_option( 'reviews_items', 0 );
}

$writes  = array();
$deleted = array();

for ( $i = 0; $i < $count; $i++ ) {
	foreach ( $legacy_map as $canonical => $legacy ) {
		$value = get_option( "options_reviews_items_{$i}_{$legacy}", null );
		if ( null === $value ) {
			$value = get_option( "reviews_items_{$i}_{$legacy}", '' );
		}

		update_option( "options_reviews_items_{$i}_{$canonical}", (string) $value, false );
		update_option( "_options_reviews_items_{$i}_{$canonical}", $field_refs[ $canonical ], false );
		$writes[] = array( 'row' => $i, 'field' => $canonical, 'len' => strlen( (string) $value ) );

		if ( get_option( "options_reviews_items_{$i}_{$legacy}", null ) !== null ) {
			delete_option( "options_reviews_items_{$i}_{$legacy}" );
			delete_option( "_options_reviews_items_{$i}_{$legacy}" );
			$deleted[] = "options_reviews_items_{$i}_{$legacy}";
		}
	}

	$defaults = array(
		'review_date'     => '',
		'review_rating'   => '5',
		'review_visible'  => '1',
		'review_featured' => '1',
	);
	foreach ( $defaults as $canonical => $default ) {
		update_option( "options_reviews_items_{$i}_{$canonical}", $default, false );
		update_option( "_options_reviews_items_{$i}_{$canonical}", $field_refs[ $canonical ], false );
	}
}

update_option( 'options_reviews_items', (string) $count, false );
update_option( '_options_reviews_items', 'field_fp02_options_reviews_items', false );
update_option( '_options_reviews_enabled', 'field_fp02_options_reviews_enabled', false );
update_option( '_options_reviews_section_heading', 'field_fp02_options_reviews_section_heading', false );
update_option( '_reviews_items', 'field_fp02_options_reviews_items', false );
update_option( '_reviews_enabled', 'field_fp02_options_reviews_enabled', false );
update_option( '_reviews_section_heading', 'field_fp02_options_reviews_section_heading', false );

if ( function_exists( 'acf_get_store' ) ) {
	acf_get_store( 'values' )->reset();
}

$rows_after = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;
$first_keys = ( is_array( $rows_after ) && ! empty( $rows_after ) ) ? array_keys( $rows_after[0] ) : array();
$admin_first_author = is_array( $rows_after ) && ! empty( $rows_after[0] ) ? (string) ( $rows_after[0]['review_author'] ?? '' ) : '';
$admin_first_text   = is_array( $rows_after ) && ! empty( $rows_after[0] ) ? (string) ( $rows_after[0]['review_text'] ?? '' ) : '';
$probe_after        = function_exists( 'shpigovsky_get_reviews_option_items' ) ? shpigovsky_get_reviews_option_items() : array();

echo wp_json_encode(
	array(
		'phase'                   => 'V9-06D9-U',
		'generated_at'            => gmdate( 'c' ),
		'rows_migrated'           => $count,
		'writes_count'            => count( $writes ),
		'legacy_keys_deleted'     => count( $deleted ),
		'first_row_keys_after'    => $first_keys,
		'admin_first_author'      => $admin_first_author,
		'admin_first_text_length' => strlen( $admin_first_text ),
		'helper_items_after'      => count( $probe_after ),
		'source_mode_after'       => function_exists( 'shpigovsky_get_reviews_source_mode' ) ? shpigovsky_get_reviews_source_mode() : 'UNKNOWN',
		'result'                  => (
			$count === 10
			&& in_array( 'review_author', $first_keys, true )
			&& in_array( 'review_text', $first_keys, true )
			&& '' !== $admin_first_author
			&& count( $probe_after ) === 10
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
