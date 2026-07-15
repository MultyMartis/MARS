<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$keep = 1244;
$trash = array( 1153, 639 );

foreach ( $trash as $id ) {
	$p = get_post( $id );
	if ( ! $p ) {
		echo "MISSING={$id}\n";
		continue;
	}
	wp_trash_post( $id );
	echo "TRASHED={$id} was={$p->post_status}\n";
}

wp_update_post(
	array(
		'ID'          => $keep,
		'post_status' => 'publish',
		'post_title'  => 'Страница — Главная',
	)
);

$publish = get_posts(
	array(
		'post_type'      => 'acf-field-group',
		'post_status'    => 'publish',
		'posts_per_page' => 50,
		's'              => 'Главная',
	)
);

$home_groups = array();
foreach ( get_posts( array( 'post_type' => 'acf-field-group', 'post_status' => 'publish', 'posts_per_page' => 100 ) ) as $p ) {
	$children = get_posts(
		array(
			'post_type'      => 'acf-field',
			'post_parent'    => $p->ID,
			'posts_per_page' => -1,
			'post_status'    => 'any',
		)
	);
	// Detect by child field names.
	$names = array();
	foreach ( $children as $c ) {
		$names[] = $c->post_excerpt; // ACF stores field name in post_excerpt
	}
	if ( in_array( 'home_gallery_display_mode', $names, true ) || in_array( 'home_recovery_intro_heading', $names, true ) ) {
		$home_groups[] = array(
			'ID'       => $p->ID,
			'title'    => $p->post_title,
			'children' => count( $children ),
		);
	}
}

echo 'KEEP_CHILDREN=' . count(
	get_posts(
		array(
			'post_type'      => 'acf-field',
			'post_parent'    => $keep,
			'posts_per_page' => -1,
			'post_status'    => 'any',
		)
	)
) . "\n";
echo 'HOME_PUBLISH_GROUPS=' . wp_json_encode( $home_groups, JSON_UNESCAPED_UNICODE ) . "\n";

$fields = acf_get_fields( 'group_fp02_page_home' );
echo 'acf_get_fields=' . count( (array) $fields ) . "\n";
echo "DEDUP_OK\n";
