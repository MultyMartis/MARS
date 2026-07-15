<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
foreach ( array( 'depressiya', 'ptsr' ) as $slug ) {
	$url = home_url( "/uslugi/psihicheskoe-zdorovie/{$slug}/" );
	$resp = wp_remote_get( $url, array( 'timeout' => 20 ) );
	echo $slug . ': ' . wp_remote_retrieve_response_code( $resp ) . "\n";
}
