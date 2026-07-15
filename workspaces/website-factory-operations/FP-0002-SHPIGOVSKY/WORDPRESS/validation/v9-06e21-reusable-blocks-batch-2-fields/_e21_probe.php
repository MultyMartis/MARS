<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$groups = array(
	'group_fp02_block_header',
	'group_fp02_block_footer',
	'group_fp02_block_hero_fallbacks',
	'group_fp02_block_comfort',
);
foreach ( $groups as $key ) {
	$g = function_exists( 'acf_get_field_group' ) ? acf_get_field_group( $key ) : null;
	echo $key . ':' . ( is_array( $g ) ? 'yes' : 'no' ) . "\n";
	if ( is_array( $g ) ) {
		$f = acf_get_fields( $key );
		echo '  fields=' . ( is_array( $f ) ? count( $f ) : 'err' ) . "\n";
	}
}
echo "comfort items=" . count( shpigovsky_get_comfort_gallery_items() ) . "\n";
