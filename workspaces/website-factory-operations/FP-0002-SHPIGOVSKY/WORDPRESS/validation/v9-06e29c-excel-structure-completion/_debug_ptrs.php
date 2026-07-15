<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$rows = $wpdb->get_results( "SELECT ID, post_type, post_name, post_status, post_parent FROM {$wpdb->posts} WHERE post_name='ptsr'" );
print_r( $rows );

// Parse request manually
$wp = new WP();
$wp->parse_request();
echo "\nQuery vars:\n";
print_r( $wp->query_vars );

// Direct rewrite test
$rules = get_option( 'rewrite_rules' );
foreach ( $rules as $pattern => $rewrite ) {
	if ( str_contains( $pattern, 'uslugi' ) ) {
		echo "$pattern => $rewrite\n";
	}
}
