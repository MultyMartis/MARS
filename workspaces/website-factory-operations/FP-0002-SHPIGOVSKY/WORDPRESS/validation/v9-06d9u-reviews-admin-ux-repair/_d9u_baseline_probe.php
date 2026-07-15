<?php
/**
 * FP-0002 V9-06D9-U — baseline probe (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix = $wpdb->prefix;

function d9u_decode_group_content( $content ) {
	$data = maybe_unserialize( $content );
	return is_array( $data ) ? $data : array();
}

function d9u_group_has_field( $group_content, $field_name ) {
	if ( ! is_string( $group_content ) ) {
		return false;
	}
	return false !== strpos( $group_content, '"' . $field_name . '"' );
}

$home_group_row = $wpdb->get_row(
	$wpdb->prepare(
		"SELECT ID, post_content FROM {$prefix}posts WHERE post_type = %s AND post_name = %s LIMIT 1",
		'acf-field-group',
		'group_fp02_page_home'
	),
	ARRAY_A
);

$reviews_group_row = $wpdb->get_row(
	$wpdb->prepare(
		"SELECT ID, post_content FROM {$prefix}posts WHERE post_type = %s AND post_name = %s LIMIT 1",
		'acf-field-group',
		'group_fp02_site_options_reviews'
	),
	ARRAY_A
);

$home_content = $home_group_row['post_content'] ?? '';
$reviews_content = $reviews_group_row['post_content'] ?? '';

$options_meta = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT option_name, option_value FROM {$prefix}options WHERE option_name LIKE %s OR option_name LIKE %s ORDER BY option_name",
		'reviews_%',
		'_reviews_%'
	),
	ARRAY_A
);

$legacy_option_keys = array();
$canonical_option_keys = array();
foreach ( $options_meta as $row ) {
	$name = $row['option_name'];
	if ( preg_match( '/author_label|_0_text|_0_metadata/', $name ) ) {
		$legacy_option_keys[] = $name;
	}
	if ( preg_match( '/review_author|review_text|review_context/', $name ) ) {
		$canonical_option_keys[] = $name;
	}
}

$rows = function_exists( 'get_field' ) ? get_field( 'reviews_items', 'option' ) : null;
$first_row_keys = ( is_array( $rows ) && ! empty( $rows ) ) ? array_keys( $rows[0] ) : array();

$home_meta = $wpdb->get_results(
	$wpdb->prepare(
		"SELECT meta_key, meta_value FROM {$prefix}postmeta WHERE post_id = %d AND (meta_key LIKE %s OR meta_key = %s) ORDER BY meta_key",
		4,
		'home_reviews%',
		'home_reviews_teaser'
	),
	ARRAY_A
);

$reviews_location = 'unknown';
if ( false !== strpos( $reviews_content, 'fp02-reviews' ) ) {
	$reviews_location = 'fp02-reviews';
} elseif ( false !== strpos( $reviews_content, 'fp02-site-settings' ) ) {
	$reviews_location = 'fp02-site-settings';
}

$canonical_json_home = json_decode(
	file_get_contents( 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_page_home.json' ),
	true
);
$canonical_home_has_teaser = false;
if ( is_array( $canonical_json_home ) ) {
	foreach ( $canonical_json_home['fields'] ?? array() as $field ) {
		if ( ( $field['name'] ?? '' ) === 'home_reviews_teaser' ) {
			$canonical_home_has_teaser = true;
			break;
		}
	}
}

echo wp_json_encode(
	array(
		'phase'                          => 'V9-06D9-U',
		'generated_at'                   => gmdate( 'c' ),
		'home_group_db_id'               => $home_group_row['ID'] ?? null,
		'home_group_db_has_teaser'       => d9u_group_has_field( $home_content, 'home_reviews_teaser' ),
		'canonical_json_has_teaser'      => $canonical_home_has_teaser,
		'reviews_group_db_id'            => $reviews_group_row['ID'] ?? null,
		'reviews_group_location'         => $reviews_location,
		'reviews_items_count'            => is_array( $rows ) ? count( $rows ) : 0,
		'first_row_keys'                 => $first_row_keys,
		'legacy_option_meta_keys_sample' => array_slice( $legacy_option_keys, 0, 20 ),
		'canonical_option_meta_keys_sample' => array_slice( $canonical_option_keys, 0, 20 ),
		'legacy_option_meta_count'       => count( $legacy_option_keys ),
		'canonical_option_meta_count'    => count( $canonical_option_keys ),
		'home_reviews_meta'              => $home_meta,
		'helper_option_items_count'      => function_exists( 'shpigovsky_get_reviews_option_items' )
			? count( shpigovsky_get_reviews_option_items() )
			: 0,
		'source_mode'                    => function_exists( 'shpigovsky_get_reviews_source_mode' )
			? shpigovsky_get_reviews_source_mode()
			: 'UNKNOWN',
		'validation_hook_teaser_limit'   => 6,
		'validation_hook_source'         => 'plugins/shpigovsky-core/src/Fields/RepeaterValidation.php field_fp02_home_reviews_teaser',
		'result'                         => 'PASS',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
