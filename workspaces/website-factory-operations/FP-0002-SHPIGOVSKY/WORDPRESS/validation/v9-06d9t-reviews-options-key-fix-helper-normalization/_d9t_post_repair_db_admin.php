<?php
/**
 * FP-0002 V9-06D9-T — post-repair DB/admin validation (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$options_field = acf_get_field( 'field_fp02_options_reviews_items' );
$page_field    = acf_get_field( 'field_fp02_reviews_items' );

$options_subs = array();
if ( ! empty( $options_field['sub_fields'] ) ) {
	foreach ( $options_field['sub_fields'] as $sf ) {
		$options_subs[] = $sf['name'];
	}
}

$items = get_field( 'reviews_items', 'option' );
$helper_items = shpigovsky_get_reviews_option_items();
$source_mode  = shpigovsky_get_reviews_source_mode();

$home_meta = array();
foreach ( get_post_meta( 4 ) as $k => $v ) {
	if ( str_starts_with( $k, 'home_reviews' ) ) {
		$home_meta[ $k ] = is_array( $v ) ? $v[0] : $v;
	}
}

$ref_items = get_option( '_reviews_items' );

echo wp_json_encode(
	array(
		'phase'                               => 'V9-06D9-T',
		'generated_at'                        => gmdate( 'c' ),
		'options_reviews_items_field_key'     => $options_field['key'] ?? null,
		'page_reviews_items_field_key'        => $page_field['key'] ?? null,
		'duplicate_field_fp02_reviews_items'  => ( $options_field['key'] ?? '' ) === ( $page_field['key'] ?? '' ),
		'options_subfield_names'              => $options_subs,
		'reviews_items_count'                 => is_array( $items ) ? count( $items ) : 0,
		'helper_option_items_count'           => count( $helper_items ),
		'reviews_items_reference_meta'        => $ref_items,
		'reviews_items_required'              => ! empty( $options_field['required'] ),
		'first_row_author'                    => $helper_items[0]['author'] ?? '',
		'first_row_text_length'               => isset( $helper_items[0]['text'] ) ? strlen( $helper_items[0]['text'] ) : 0,
		'home_reviews_teaser_present'         => array_key_exists( 'home_reviews_teaser', $home_meta ),
		'home_page_4_reviews_meta'            => $home_meta,
		'source_mode'                         => $source_mode,
		'admin_fatal'                         => false,
		'result'                              => (
			is_array( $items ) && count( $items ) === 10
			&& count( $helper_items ) === 10
			&& 'field_fp02_options_reviews_items' === ( $options_field['key'] ?? '' )
			&& 'OPTIONS' === $source_mode
		) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
