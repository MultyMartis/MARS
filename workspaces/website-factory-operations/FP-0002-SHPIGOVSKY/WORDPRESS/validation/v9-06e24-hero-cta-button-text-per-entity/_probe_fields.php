<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$groups = array( 'group_fp02_page_home', 'group_fp02_page_services_hub' );
foreach ( $groups as $gk ) {
	echo $gk . ":\n";
	$fields = acf_get_fields( $gk );
	if ( ! is_array( $fields ) ) {
		echo "  NO FIELDS\n";
		continue;
	}
	foreach ( $fields as $f ) {
		if ( is_array( $f ) ) {
			echo '  - ' . ( $f['name'] ?? '?' ) . ' (' . ( $f['label'] ?? '' ) . ")\n";
		}
	}
}
