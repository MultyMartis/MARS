<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$posts = get_posts( array( 'post_type' => 'service', 'posts_per_page' => 50, 'post_status' => 'any' ) );
foreach ( $posts as $p ) {
	echo $p->ID . ' ' . $p->post_name . ' parent=' . $p->post_parent . PHP_EOL;
}
