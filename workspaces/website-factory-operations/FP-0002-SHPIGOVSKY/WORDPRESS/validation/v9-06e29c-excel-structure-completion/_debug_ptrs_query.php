<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$_SERVER['REQUEST_URI'] = '/uslugi/psihicheskoe-zdorovie/ptsr/';
$_SERVER['REQUEST_METHOD'] = 'GET';

global $wp, $wp_query;
$wp->init();
$wp->parse_request();
echo "query_vars:\n";
print_r( $wp->query_vars );

$wp->query_posts();
echo "is_404: " . ( $wp_query->is_404() ? 'yes' : 'no' ) . "\n";
echo "queried_id: " . (int) get_queried_object_id() . "\n";
if ( $wp_query->post ) {
	echo "post: {$wp_query->post->ID} {$wp_query->post->post_name}\n";
}

// compare depressiya
$_SERVER['REQUEST_URI'] = '/uslugi/psihicheskoe-zdorovie/depressiya/';
$wp->init();
$wp->parse_request();
$wp->query_posts();
echo "\ndepressiya is_404: " . ( $wp_query->is_404() ? 'yes' : 'no' ) . " id=" . get_queried_object_id() . "\n";
