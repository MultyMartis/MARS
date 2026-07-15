<?php
/**
 * FP-0002 V9-06D9-T — baseline probe (TEMPORARY — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$options_field = acf_get_field( 'field_fp02_reviews_items' );
$page_field      = acf_get_field( 'field_fp02_reviews_items' );

$options_group = acf_get_field_group( 'group_fp02_site_options_reviews' );
$page_group    = acf_get_field_group( 'group_fp02_page_reviews' );

$options_fields = acf_get_fields( 'group_fp02_site_options_reviews' );
$page_fields    = acf_get_fields( 'group_fp02_page_reviews' );

function fp02_collect_keys( $fields ) {
	$keys = array();
	if ( ! is_array( $fields ) ) {
		return $keys;
	}
	foreach ( $fields as $f ) {
		$keys[] = array(
			'key'  => $f['key'] ?? '',
			'name' => $f['name'] ?? '',
		);
		if ( ! empty( $f['sub_fields'] ) ) {
			foreach ( $f['sub_fields'] as $sf ) {
				$keys[] = array(
					'key'  => $sf['key'] ?? '',
					'name' => $sf['name'] ?? '',
				);
			}
		}
	}
	return $keys;
}

$items = get_field( 'reviews_items', 'option' );
$opt   = function_exists( 'shpigovsky_get_reviews_option_items' )
	? shpigovsky_get_reviews_option_items()
	: array();
$resolved = function_exists( 'shpigovsky_get_reviews_items' )
	? shpigovsky_get_reviews_items( array( 'limit' => 10 ) )
	: array();

$first = $resolved[0] ?? array();
$mode  = empty( $opt ) ? 'FALLBACK' : ( ! empty( $first['is_demo'] ) ? 'FALLBACK' : 'OPTIONS' );

global $wpdb;
$meta_rows = $wpdb->get_results(
	"SELECT option_name, option_value FROM {$wpdb->options} WHERE option_name LIKE '%reviews%' ORDER BY option_name",
	ARRAY_A
);
$meta = array();
foreach ( $meta_rows as $row ) {
	$val = $row['option_value'];
	if ( strlen( $val ) > 300 ) {
		$val = substr( $val, 0, 300 ) . '...';
	}
	$meta[ $row['option_name'] ] = $val;
}

$home_meta = get_post_meta( 4 );
$home_reviews = array();
foreach ( $home_meta as $k => $v ) {
	if ( str_starts_with( $k, 'home_reviews' ) ) {
		$home_reviews[ $k ] = is_array( $v ) ? $v[0] : $v;
	}
}

$out = array(
	'generated_at'                  => gmdate( 'c' ),
	'options_group_keys'            => fp02_collect_keys( $options_fields ),
	'page_group_keys'               => fp02_collect_keys( $page_fields ),
	'duplicate_keys'                => array(),
	'reviews_items_count'           => is_array( $items ) ? count( $items ) : 0,
	'first_option_row'              => is_array( $items ) && ! empty( $items ) ? $items[0] : null,
	'first_option_row_keys'         => is_array( $items ) && ! empty( $items ) ? array_keys( $items[0] ) : array(),
	'helper_option_items_count'     => count( $opt ),
	'resolved_items_count'          => count( $resolved ),
	'frontend_source_mode_before'   => $mode,
	'options_meta_sample'           => $meta,
	'home_page_4_reviews_meta'      => $home_reviews,
);

$opt_keys = array_column( fp02_collect_keys( $options_fields ), 'key' );
$page_keys = array_column( fp02_collect_keys( $page_fields ), 'key' );
$out['duplicate_keys'] = array_values( array_intersect( $opt_keys, $page_keys ) );

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06d9t-reviews-options-key-fix-helper-normalization/baseline-collision-data-audit-probe.json';
file_put_contents( $evidence, wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo wp_json_encode( $out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT );
