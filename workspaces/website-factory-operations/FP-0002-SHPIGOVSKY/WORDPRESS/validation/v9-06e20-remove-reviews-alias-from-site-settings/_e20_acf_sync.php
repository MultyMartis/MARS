<?php
$json_path = dirname( __DIR__, 4 ) . '/acf-json/group_fp02_site_options_reviews.json';
if ( ! is_readable( $json_path ) ) {
	$json_path = ABSPATH . 'acf-json/group_fp02_site_options_reviews.json';
}

$before = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$before_locs = array();
if ( is_array( $before['location'] ?? null ) ) {
	foreach ( $before['location'] as $rule_group ) {
		foreach ( (array) $rule_group as $rule ) {
			if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
				$before_locs[] = (string) ( $rule['value'] ?? '' );
			}
		}
	}
}

$db_write = false;
$import_result = 'SKIPPED';
if ( function_exists( 'acf_import_field_group' ) && is_readable( $json_path ) ) {
	$json = json_decode( file_get_contents( $json_path ), true );
	if ( is_array( $json ) ) {
		acf_import_field_group( $json );
		$db_write = true;
		$import_result = 'PASS';
	}
}

$after = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( 'group_fp02_site_options_reviews' ) : null;
$after_locs = array();
if ( is_array( $after['location'] ?? null ) ) {
	foreach ( $after['location'] as $rule_group ) {
		foreach ( (array) $rule_group as $rule ) {
			if ( ( $rule['param'] ?? '' ) === 'options_page' ) {
				$after_locs[] = (string) ( $rule['value'] ?? '' );
			}
		}
	}
}

echo json_encode(
	array(
		'json_path'            => $json_path,
		'before_locations'     => $before_locs,
		'after_locations'      => $after_locs,
		'db_write'             => $db_write,
		'import_result'        => $import_result,
		'alias_removed'        => ! in_array( 'fp02-block-reviews', $after_locs, true ),
		'canonical_preserved'  => in_array( 'fp02-reviews', $after_locs, true ),
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
);
