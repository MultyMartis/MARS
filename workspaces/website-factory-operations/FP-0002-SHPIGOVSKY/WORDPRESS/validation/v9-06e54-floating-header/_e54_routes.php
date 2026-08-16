<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$pages = get_posts(
	array(
		'post_type'   => 'page',
		'post_status' => 'publish',
		'numberposts' => 20,
		'orderby'     => 'ID',
		'order'       => 'ASC',
	)
);

foreach ( $pages as $p ) {
	echo 'PAGE ' . $p->ID . ' ' . $p->post_name . ' ' . get_permalink( $p->ID ) . PHP_EOL;
}

$posts = get_posts(
	array(
		'post_type'   => 'post',
		'post_status' => 'publish',
		'numberposts' => 5,
	)
);

foreach ( $posts as $p ) {
	echo 'POST ' . $p->ID . ' ' . $p->post_name . ' ' . get_permalink( $p->ID ) . PHP_EOL;
}
