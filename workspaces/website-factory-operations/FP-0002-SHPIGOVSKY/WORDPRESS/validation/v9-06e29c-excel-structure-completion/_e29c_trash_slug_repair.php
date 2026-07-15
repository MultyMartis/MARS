<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
global $wpdb;
$prefix = $wpdb->prefix;
$trashed = $wpdb->get_results( "SELECT ID, post_name FROM {$prefix}posts WHERE post_status='trash' AND post_type IN ('service','page')" );
$results = array();
foreach ( $trashed as $row ) {
	$new_slug = $row->post_name . '-trashed-' . $row->ID;
	$wpdb->update(
		$prefix . 'posts',
		array( 'post_name' => $new_slug ),
		array( 'ID' => (int) $row->ID ),
		array( '%s' ),
		array( '%d' )
	);
	$results[] = array( 'id' => (int) $row->ID, 'from' => $row->post_name, 'to' => $new_slug );
}
flush_rewrite_rules( false );
file_put_contents(
	'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e29c-excel-structure-completion/trash-slug-repair.json',
	wp_json_encode( $results, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) . "\n"
);
echo wp_json_encode( array( 'count' => count( $results ) ), JSON_UNESCAPED_UNICODE ) . "\n";
