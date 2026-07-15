<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$root = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS';
$runtime = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$groups = array(
	'group_fp02_block_header',
	'group_fp02_block_footer',
	'group_fp02_block_hero_fallbacks',
	'group_fp02_block_comfort',
);
foreach ( $groups as $group_key ) {
	$group = acf_get_field_group( $group_key );
	$group['fields'] = acf_get_fields( $group_key );
	$path = $root . '/acf-json/' . $group_key . '.json';
	file_put_contents( $path, wp_json_encode( $group, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
	copy( $path, $runtime . '/wp-content/acf-json/' . $group_key . '.json' );
	acf_import_field_group( json_decode( file_get_contents( $path ), true ) );
	echo $group_key . ":ok\n";
}
