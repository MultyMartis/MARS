<?php
define( 'WP_USE_THEMES', false );
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$p = get_post( 79 );
print_r( $p ? array( 'ID' => $p->ID, 'name' => $p->post_name, 'status' => $p->post_status, 'parent' => $p->post_parent ) : 'missing' );
