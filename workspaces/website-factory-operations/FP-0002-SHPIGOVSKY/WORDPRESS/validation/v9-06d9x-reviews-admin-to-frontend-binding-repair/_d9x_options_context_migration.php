<?php
/**
 * FP-0002 V9-06D9-X — sync operator-edited options context to fp02-reviews (TEMP — NOT FOR GIT).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;

$prefix        = $wpdb->prefix;
$source_prefix = 'options_reviews_';
$target_prefix = 'fp02-reviews_reviews_';

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
	$value         = $row['option_value'];

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

$fp02_first   = get_option( 'fp02-reviews_reviews_items_0_review_author', '' );
$option_first = get_option( 'options_reviews_items_0_review_author', '' );

echo wp_json_encode(
	array(
		'phase'                   => 'V9-06D9-X',
		'generated_at'            => gmdate( 'c' ),
		'migration_strategy'      => 'copy options_reviews_* to fp02-reviews_reviews_* preserving operator edit',
		'meta_copied_count'       => count( $copied ),
		'meta_copied_sample'      => array_slice( $copied, 0, 6 ),
		'option_first_author'     => $option_first,
		'fp02_first_author_after' => $fp02_first,
		'result'                  => ( 'Андрей, Москва' === $fp02_first ) ? 'PASS' : 'PARTIAL',
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
);
