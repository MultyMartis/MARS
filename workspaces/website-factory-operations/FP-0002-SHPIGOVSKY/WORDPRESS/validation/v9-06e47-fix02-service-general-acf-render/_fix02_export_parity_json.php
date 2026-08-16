<?php
/**
 * V9-06E47-FIX02 — export ServiceGeneralParity group JSON (no field conditionals).
 *
 * @package Shpigovsky
 */

require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$group = \Shpigovsky\Core\Fields\ServiceGeneralParity::group();

// Normalize conditional_logic to 0 for JSON clarity.
$normalize = function ( &$fields ) use ( &$normalize ) {
	if ( ! is_array( $fields ) ) {
		return;
	}
	foreach ( $fields as &$f ) {
		if ( ! is_array( $f ) ) {
			continue;
		}
		if ( array_key_exists( 'conditional_logic', $f ) ) {
			$f['conditional_logic'] = 0;
		}
		if ( ! empty( $f['sub_fields'] ) && is_array( $f['sub_fields'] ) ) {
			$normalize( $f['sub_fields'] );
		}
	}
	unset( $f );
};
$normalize( $group['fields'] );
$group['modified'] = 1784454900;

$json = wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE );
$json = str_replace( "\n", "\r\n", $json ) . "\r\n";

$paths = array(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/acf-json/group_fp02_service_general_parity.json',
	'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json/group_fp02_service_general_parity.json',
);

foreach ( $paths as $path ) {
	$dir = dirname( $path );
	if ( ! is_dir( $dir ) ) {
		wp_mkdir_p( $dir );
	}
	file_put_contents( $path, $json );
	echo 'WROTE ' . $path . ' bytes=' . strlen( $json ) . PHP_EOL;
}

$with = 0;
foreach ( $group['fields'] as $f ) {
	if ( ! empty( $f['conditional_logic'] ) ) {
		++$with;
	}
}
echo 'fields=' . count( $group['fields'] ) . ' with_nonempty_cond=' . $with . PHP_EOL;
