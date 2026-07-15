<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

// Force refresh post 79
delete_post_meta( 79, '_edit_lock' );
clean_post_cache( 79 );

$url = home_url( '/uslugi/psihicheskoe-zdorovie/ptrs/' );
$resp = wp_remote_get( $url, array( 'timeout' => 20, 'headers' => array( 'Cache-Control' => 'no-cache' ) ) );
echo 'status: ' . wp_remote_retrieve_response_code( $resp ) . "\n";

// Direct WP_Query like core
$q = new WP_Query(
	array(
		'post_type'      => 'service',
		'name'           => 'ptrs',
		'post_parent'    => 77,
		'posts_per_page' => 1,
	)
);
echo 'direct query count: ' . $q->post_count . "\n";

// Hierarchical name query
$q2 = new WP_Query(
	array(
		'post_type' => 'service',
		'name'      => 'psihicheskoe-zdorovie/ptrs',
	)
);
echo 'path name query count: ' . $q2->post_count . "\n";
