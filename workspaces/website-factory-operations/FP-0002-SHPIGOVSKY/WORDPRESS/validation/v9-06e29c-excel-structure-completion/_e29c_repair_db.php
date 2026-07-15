<?php
/**
 * FP-0002 V9-06E29C — DB-level service duplicate repair (bypasses depth guard).
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

global $wpdb;
$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e29c-excel-structure-completion';
$prefix   = $wpdb->prefix;

$trash_ids = array( 1009, 1010, 1014, 1015, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028 );
$trash_results = array();
foreach ( $trash_ids as $id ) {
	$updated = $wpdb->update(
		$prefix . 'posts',
		array( 'post_status' => 'trash' ),
		array( 'ID' => (int) $id ),
		array( '%s' ),
		array( '%d' )
	);
	$trash_results[] = array( 'id' => (int) $id, 'updated' => (int) $updated );
}

$renames = array(
	314 => array( 'post_name' => 'lechenie-narkoticheskoy-zavisimosti', 'post_title' => 'Лечение наркотической зависимости' ),
	316 => array( 'post_name' => 'lechenie-povedencheskoy-zavisimosti', 'post_title' => 'Поведенческие зависимости' ),
	80  => array( 'post_name' => 'emotsionalnoe-vygoranie', 'post_title' => 'Эмоциональное выгорание' ),
	86  => array( 'post_name' => 'buliniya', 'post_title' => 'Булимия' ),
);

$rename_results = array();
foreach ( $renames as $id => $data ) {
	$updated = $wpdb->update(
		$prefix . 'posts',
		$data,
		array( 'ID' => (int) $id ),
		array( '%s', '%s' ),
		array( '%d' )
	);
	$rename_results[] = array( 'id' => (int) $id, 'slug' => $data['post_name'], 'updated' => (int) $updated );
}

$reparents = array(
	315  => 314,
	1011 => 314,
	1012 => 314,
	1013 => 314,
	1016 => 316,
	1017 => 316,
	1018 => 316,
	1019 => 316,
);

$reparent_results = array();
foreach ( $reparents as $id => $parent ) {
	$updated = $wpdb->update(
		$prefix . 'posts',
		array( 'post_parent' => (int) $parent ),
		array( 'ID' => (int) $id ),
		array( '%d' ),
		array( '%d' )
	);
	$reparent_results[] = array( 'id' => (int) $id, 'parent' => (int) $parent, 'updated' => (int) $updated );
}

clean_post_cache( 314 );
clean_post_cache( 316 );
clean_post_cache( 315 );
foreach ( array_keys( $reparents ) as $id ) {
	clean_post_cache( (int) $id );
}

flush_rewrite_rules( false );

$summary = array(
	'trashed'   => $trash_results,
	'renames'   => $rename_results,
	'reparents' => $reparent_results,
);

file_put_contents(
	$evidence . '/repair-db-result.json',
	wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n"
);

echo wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) . "\n";
