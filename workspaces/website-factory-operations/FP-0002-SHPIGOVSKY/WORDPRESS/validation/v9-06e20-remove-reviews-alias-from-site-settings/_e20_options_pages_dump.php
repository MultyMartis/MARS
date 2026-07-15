<?php
do_action( 'acf/init' );
$all = function_exists( 'acf_get_options_pages' ) ? acf_get_options_pages() : array();
$rows = array();
foreach ( (array) $all as $slug => $page ) {
	$rows[] = array(
		'slug'        => is_string( $slug ) ? $slug : ( $page['menu_slug'] ?? '' ),
		'menu_title'  => $page['menu_title'] ?? '',
		'parent_slug' => $page['parent_slug'] ?? '',
		'post_id'     => $page['post_id'] ?? '',
	);
}
echo json_encode( array( 'count' => count( $rows ), 'pages' => $rows ), JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
