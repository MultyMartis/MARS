<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$q = new WP_Query(
	array(
		'post_type'      => 'service',
		'posts_per_page' => 5,
		'post_status'    => 'publish',
		'orderby'        => 'ID',
		'order'          => 'ASC',
	)
);
foreach ( $q->posts as $post ) {
	echo get_permalink( $post ) . PHP_EOL;
}
