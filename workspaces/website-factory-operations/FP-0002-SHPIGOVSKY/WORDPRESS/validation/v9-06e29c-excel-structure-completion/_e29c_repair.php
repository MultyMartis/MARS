<?php
/**
 * FP-0002 V9-06E29C — repair duplicate services from first mutation pass.
 */
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e29c-excel-structure-completion';

function fp02e29c_repair_get_service_by_slug( $slug ) {
	$posts = get_posts(
		array(
			'name'           => $slug,
			'post_type'      => 'service',
			'post_status'    => 'any',
			'posts_per_page' => 1,
			'fields'         => 'all',
		)
	);
	return ! empty( $posts ) ? $posts[0] : null;
}

function fp02e29c_repair_trash_ids( array $ids ) {
	$rows = array();
	foreach ( $ids as $id ) {
		$id = (int) $id;
		$post = get_post( $id );
		if ( ! $post ) {
			$rows[] = array( 'id' => $id, 'action' => 'MISSING' );
			continue;
		}
		wp_trash_post( $id );
		$rows[] = array( 'id' => $id, 'slug' => $post->post_name, 'action' => 'TRASHED' );
	}
	return $rows;
}

$renames = array(
	314 => array( 'post_name' => 'lechenie-narkoticheskoy-zavisimosti', 'post_title' => 'Лечение наркотической зависимости' ),
	316 => array( 'post_name' => 'lechenie-povedencheskoy-zavisimosti', 'post_title' => 'Поведенческие зависимости' ),
	315 => array( 'post_name' => 'lekarstva', 'post_title' => 'Лечение лекарственной зависимости', 'post_parent' => 314 ),
	80  => array( 'post_name' => 'emotsionalnoe-vygoranie', 'post_title' => 'Эмоциональное выгорание' ),
	86  => array( 'post_name' => 'buliniya', 'post_title' => 'Булимия' ),
);

$rename_results = array();
foreach ( $renames as $id => $data ) {
	$data['ID'] = (int) $id;
	$result     = wp_update_post( $data, true );
	$rename_results[] = array(
		'id'     => (int) $id,
		'slug'   => $data['post_name'],
		'result' => is_wp_error( $result ) ? $result->get_error_message() : 'OK',
	);
}

$narc_parent = 314;
$beh_parent  = 316;

$reparent = array(
	1011 => $narc_parent,
	1012 => $narc_parent,
	1013 => $narc_parent,
	1016 => $beh_parent,
	1017 => $beh_parent,
	1018 => $beh_parent,
	1019 => $beh_parent,
);

$reparent_results = array();
foreach ( $reparent as $id => $parent ) {
	$result = wp_update_post(
		array(
			'ID'          => (int) $id,
			'post_parent' => (int) $parent,
		),
		true
	);
	$reparent_results[] = array(
		'id'     => (int) $id,
		'parent' => (int) $parent,
		'result' => is_wp_error( $result ) ? $result->get_error_message() : 'OK',
	);
}

$trash_ids = array( 1009, 1010, 1014, 1015, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028 );
$trash_results = fp02e29c_repair_trash_ids( $trash_ids );

flush_rewrite_rules( false );

$summary = array(
	'renames'   => $rename_results,
	'reparents' => $reparent_results,
	'trashed'   => $trash_results,
);

file_put_contents(
	$evidence . '/repair-result.json',
	wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n"
);

echo wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) . "\n";
