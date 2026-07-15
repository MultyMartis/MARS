<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
foreach ( array( 78, 79 ) as $id ) {
	$p = get_post( $id );
	echo "ID $id: name={$p->post_name} status={$p->post_status} parent={$p->post_parent} type={$p->post_type}\n";
	echo 'permalink: ' . get_permalink( $id ) . "\n";
	$meta = $wpdb->get_results( $wpdb->prepare( "SELECT meta_key, meta_value FROM {$wpdb->postmeta} WHERE post_id=%d LIMIT 20", $id ) );
	echo "meta count: " . count( $meta ) . "\n\n";
}
