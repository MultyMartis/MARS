<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$rows = $wpdb->get_results( "SELECT ID, post_name, post_status, post_parent FROM {$wpdb->posts} WHERE post_name LIKE '%ptsr%'" );
print_r( $rows );
$path = 'psihicheskoe-zdorovie/ptrs';
$post = get_page_by_path( $path, OBJECT, 'service' );
echo "get_page_by_path: " . ( $post ? $post->ID : 'null' ) . "\n";

$_SERVER['REQUEST_URI'] = '/uslugi/psihicheskoe-zdorovie/ptrs/';
$_SERVER['REQUEST_METHOD'] = 'GET';
global $wp;
$wp->init();
$wp->parse_request();
echo "after parse:\n";
print_r( $wp->query_vars );
$filtered = \Shpigovsky\Core\Permalinks\ServicePermalinks::filter_service_request( $wp->query_vars );
echo "after filter:\n";
print_r( $filtered );
