<?php
/**
 * V9-06E34 read-only audit: specialists parent/children + slider source.
 */
require_once 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';

$evidence = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e34-specialists-child-pages-auto-slider';
$backup  = 'X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e34-specialists-pages-slider-before-20260713-020509';

$parent = get_page_by_path( 'specyalisty' );
$out    = array(
	'parent'            => null,
	'children'          => array(),
	'duplicates'        => array(),
	'static_slider'     => function_exists( 'shpigovsky_get_v9_specialists_cards' ) ? shpigovsky_get_v9_specialists_cards() : array(),
	'acf_slider'        => null,
	'resolved_cards'    => function_exists( 'shpigovsky_get_specialists_cards' ) ? shpigovsky_get_specialists_cards() : array(),
	'all_link_url'      => function_exists( 'shpigovsky_get_specialists_all_link_url' ) ? shpigovsky_get_specialists_all_link_url() : null,
	'all_link_label'    => function_exists( 'shpigovsky_get_specialists_all_link_label' ) ? shpigovsky_get_specialists_all_link_label() : null,
	'section_heading'   => function_exists( 'shpigovsky_get_specialists_section_heading' ) ? shpigovsky_get_specialists_section_heading() : null,
);

if ( $parent instanceof WP_Post ) {
	$out['parent'] = array(
		'ID'            => (int) $parent->ID,
		'title'         => $parent->post_title,
		'slug'          => $parent->post_name,
		'status'        => $parent->post_status,
		'template'      => (string) get_page_template_slug( $parent->ID ),
		'url'           => get_permalink( $parent->ID ),
		'menu_order'    => (int) $parent->menu_order,
		'content_len'   => strlen( (string) $parent->post_content ),
		'excerpt'       => $parent->post_excerpt,
		'thumb'         => (int) get_post_thumbnail_id( $parent->ID ),
	);

	$children = get_posts(
		array(
			'post_type'      => 'page',
			'post_parent'    => $parent->ID,
			'post_status'    => array( 'publish', 'draft', 'private', 'pending', 'future' ),
			'numberposts'    => 100,
			'orderby'        => array( 'menu_order' => 'ASC', 'title' => 'ASC' ),
		)
	);

	$title_map = array();
	$slug_map  = array();
	foreach ( $children as $child ) {
		$row = array(
			'ID'          => (int) $child->ID,
			'title'       => $child->post_title,
			'slug'        => $child->post_name,
			'status'      => $child->post_status,
			'template'    => (string) get_page_template_slug( $child->ID ),
			'url'         => get_permalink( $child->ID ),
			'menu_order'  => (int) $child->menu_order,
			'content_len' => strlen( (string) $child->post_content ),
			'excerpt'     => $child->post_excerpt,
			'thumb'       => (int) get_post_thumbnail_id( $child->ID ),
			'content'     => $child->post_content,
		);
		$out['children'][] = $row;
		$key_t = mb_strtolower( trim( $child->post_title ) );
		$key_s = mb_strtolower( trim( $child->post_name ) );
		$title_map[ $key_t ][] = (int) $child->ID;
		$slug_map[ $key_s ][]  = (int) $child->ID;
	}
	foreach ( $title_map as $k => $ids ) {
		if ( count( $ids ) > 1 ) {
			$out['duplicates'][] = array( 'by' => 'title', 'key' => $k, 'ids' => $ids );
		}
	}
	foreach ( $slug_map as $k => $ids ) {
		if ( count( $ids ) > 1 ) {
			$out['duplicates'][] = array( 'by' => 'slug', 'key' => $k, 'ids' => $ids );
		}
	}
}

if ( function_exists( 'get_field' ) && function_exists( 'shpigovsky_get_specialists_block_context' ) ) {
	$out['acf_slider'] = get_field( 'specialists_items', shpigovsky_get_specialists_block_context() );
}

@mkdir( $evidence, 0777, true );
file_put_contents( $evidence . '/e34-audit-before.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );
file_put_contents( $backup . '/specialists-inventory-before.json', wp_json_encode( $out, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) );

echo "AUDIT_OK parent=" . ( $out['parent'] ? $out['parent']['ID'] : 'none' ) . " children=" . count( $out['children'] ) . " static=" . count( $out['static_slider'] ) . " resolved=" . count( $out['resolved_cards'] ) . PHP_EOL;
