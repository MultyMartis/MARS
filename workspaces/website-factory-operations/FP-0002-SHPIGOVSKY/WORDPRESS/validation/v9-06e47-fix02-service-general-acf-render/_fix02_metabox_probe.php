<?php
define( 'WP_USE_THEMES', false );
$_SERVER['REQUEST_URI'] = '/wp-admin/post.php?post=74&action=edit';
$_SERVER['PHP_SELF']    = '/wp-admin/post.php';
$_GET['post']           = '74';
$_GET['action']         = 'edit';
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/meta-boxes.php';
require_once ABSPATH . 'wp-admin/includes/post.php';
if ( ! defined( 'WP_ADMIN' ) ) {
	define( 'WP_ADMIN', true );
}
wp_set_current_user( 1 );
$post             = get_post( 74 );
$GLOBALS['post']  = $post;
set_current_screen( 'service' );
$GLOBALS['wp_meta_boxes'] = array();

if ( post_type_supports( 'service', 'excerpt' ) ) {
	add_meta_box( 'postexcerpt', __( 'Excerpt' ), 'post_excerpt_meta_box', 'service', 'normal', 'core' );
}
if ( post_type_supports( 'service', 'revisions' ) ) {
	add_meta_box( 'revisionsdiv', __( 'Revisions' ), 'post_revisions_meta_box', 'service', 'normal', 'core' );
}
if ( post_type_supports( 'service', 'editor' ) ) {
	add_meta_box( 'postdivrich', 'Editor', '__return_empty_string', 'service', 'normal', 'core' );
}

do_action( 'add_meta_boxes', 'service', $post );
do_action( 'add_meta_boxes_service', $post );

$ids = array();
foreach ( ( $GLOBALS['wp_meta_boxes']['service'] ?? array() ) as $ctx => $pris ) {
	foreach ( (array) $pris as $prio => $boxes ) {
		foreach ( (array) $boxes as $id => $box ) {
			if ( ! empty( $box ) && is_array( $box ) ) {
				$ids[ $id ] = isset( $box['title'] ) ? $box['title'] : $id;
			}
		}
	}
}
echo 'excerpt_support=' . ( post_type_supports( 'service', 'excerpt' ) ? '1' : '0' ) . ' revisions_support=' . ( post_type_supports( 'service', 'revisions' ) ? '1' : '0' ) . PHP_EOL;
echo 'revisionsdiv=' . ( isset( $ids['revisionsdiv'] ) ? 'PRESENT' : 'hidden' ) . PHP_EOL;
echo 'postexcerpt=' . ( isset( $ids['postexcerpt'] ) ? 'PRESENT' : 'hidden' ) . PHP_EOL;
echo 'postdivrich=' . ( isset( $ids['postdivrich'] ) ? 'PRESENT' : 'hidden' ) . PHP_EOL;
echo 'ALL=' . implode( '|', array_keys( $ids ) ) . PHP_EOL;
