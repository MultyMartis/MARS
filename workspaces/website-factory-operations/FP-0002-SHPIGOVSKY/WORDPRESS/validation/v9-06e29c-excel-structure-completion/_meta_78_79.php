<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
foreach ( array( 78, 79 ) as $id ) {
	echo "=== ID $id ===\n";
	$meta = $wpdb->get_results( $wpdb->prepare( "SELECT meta_key, meta_value FROM {$wpdb->postmeta} WHERE post_id=%d ORDER BY meta_key", $id ) );
	foreach ( $meta as $m ) {
		$val = strlen( $m->meta_value ) > 80 ? substr( $m->meta_value, 0, 80 ) . '...' : $m->meta_value;
		echo "{$m->meta_key} = {$val}\n";
	}
	echo "\n";
}
