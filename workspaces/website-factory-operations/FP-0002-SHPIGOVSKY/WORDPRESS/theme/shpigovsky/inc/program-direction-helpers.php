<?php
/**
 * Program direction map — shared Home / services / about program blocks.
 *
 * V9-06E62D: Home direction card text owned by child-page ACF
 * `treatment_program_short_description` («Мини-описание»).
 *
 * V9-07A01: Title, permalink and mini-description always resolve from live
 * Treatment Program child pages under parent #13. Helper maps may hold only
 * non-content visual metadata (marker / image assets) keyed by page ID.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Canonical Treatment Program parent page ID.
 *
 * @return int
 */
function shpigovsky_get_treatment_program_parent_id() {
	$parent = get_page_by_path( 'o-centre/programma-lecheniya' );

	if ( $parent instanceof WP_Post ) {
		return (int) $parent->ID;
	}

	return 13;
}

/**
 * Non-content visual metadata for known Treatment Program children.
 *
 * Keys are stable page IDs. Do not store title, slug, URL or description here.
 *
 * @return array<int, array{marker:string,image:string,width:int,height:int}>
 */
function shpigovsky_get_program_direction_visual_meta() {
	return array(
		1053 => array(
			'marker' => '01',
			'image'  => 'img/content/rehabilitation-program/program-genotyping.webp',
			'width'  => 1216,
			'height' => 1632,
		),
		1054 => array(
			'marker' => '02',
			'image'  => 'img/content/rehabilitation-program/program-neuropsychology.webp',
			'width'  => 1632,
			'height' => 1216,
		),
		1055 => array(
			'marker' => '03',
			'image'  => 'img/content/rehabilitation-program/program-psychocorrection.webp',
			'width'  => 880,
			'height' => 1184,
		),
		1056 => array(
			'marker' => '04',
			'image'  => 'img/content/rehabilitation-program/program-kinesiotherapy.webp',
			'width'  => 880,
			'height' => 1184,
		),
	);
}

/**
 * Published Treatment Program child pages in display order.
 *
 * Order: menu_order ASC, then ID ASC (established seed order when menu_order ties).
 *
 * @return array<int, WP_Post>
 */
function shpigovsky_get_treatment_program_child_pages() {
	$parent_id = shpigovsky_get_treatment_program_parent_id();
	if ( $parent_id <= 0 ) {
		return array();
	}

	$children = get_posts(
		array(
			'post_type'        => 'page',
			'post_parent'      => $parent_id,
			'post_status'      => 'publish',
			'orderby'          => array(
				'menu_order' => 'ASC',
				'ID'         => 'ASC',
			),
			'posts_per_page'   => 50,
			'suppress_filters' => true,
		)
	);

	return is_array( $children ) ? $children : array();
}

/**
 * Resolve program direction child page under programma-lecheniya by slug.
 *
 * Kept for path/legacy callers. Card rendering uses live child queries instead.
 *
 * @param string $slug Child page slug.
 * @return WP_Post|null
 */
function shpigovsky_get_program_direction_page( $slug ) {
	$slug = sanitize_title( (string) $slug );
	$path = 'o-centre/programma-lecheniya/' . $slug;
	$page = get_page_by_path( $path );

	return ( $page instanceof WP_Post ) ? $page : null;
}

/**
 * Resolve permalink for a program direction page under programma-lecheniya.
 *
 * @param string $slug Child page slug.
 * @return string Absolute URL (falls back to expected path when page missing).
 */
function shpigovsky_get_program_direction_url( $slug ) {
	$page = shpigovsky_get_program_direction_page( $slug );

	if ( $page instanceof WP_Post ) {
		$url = get_permalink( $page );
		if ( is_string( $url ) && '' !== $url ) {
			return $url;
		}
	}

	$slug = sanitize_title( (string) $slug );
	$path = 'o-centre/programma-lecheniya/' . $slug;

	return home_url( '/' . $path . '/' );
}

/**
 * Mini-description for a Treatment Program child page.
 *
 * @param int $page_id Child page ID.
 * @return string Raw HTML-safe fragment (may contain &nbsp;); empty when unset.
 */
function shpigovsky_get_treatment_program_short_description( $page_id ) {
	$page_id = (int) $page_id;
	if ( $page_id <= 0 ) {
		return '';
	}

	$value = '';
	if ( function_exists( 'get_field' ) ) {
		$raw = get_field( 'treatment_program_short_description', $page_id );
		if ( is_string( $raw ) ) {
			$value = $raw;
		}
	}

	if ( '' === $value ) {
		$meta = get_post_meta( $page_id, 'treatment_program_short_description', true );
		if ( is_string( $meta ) ) {
			$value = $meta;
		}
	}

	return is_string( $value ) ? trim( $value ) : '';
}

/**
 * Program direction items with live titles, permalinks and mini-descriptions.
 *
 * @param string $variant home|service|about — retained for callers; content source is identical.
 * @return array<int, array{slug:string,title:string,marker:string,title_display:string,url:string,image:string,width:int,height:int,alt:string,text:string,page_id:int}>
 */
function shpigovsky_get_program_direction_items( $variant = 'service' ) {
	unset( $variant );

	$items   = array();
	$visuals = shpigovsky_get_program_direction_visual_meta();
	$index   = 0;

	foreach ( shpigovsky_get_treatment_program_child_pages() as $child ) {
		if ( ! ( $child instanceof WP_Post ) ) {
			continue;
		}

		++$index;
		$page_id = (int) $child->ID;
		$title   = get_the_title( $child );
		$title   = is_string( $title ) ? trim( $title ) : '';
		$meta    = isset( $visuals[ $page_id ] ) && is_array( $visuals[ $page_id ] ) ? $visuals[ $page_id ] : array();
		$marker  = isset( $meta['marker'] ) && '' !== (string) $meta['marker']
			? (string) $meta['marker']
			: sprintf( '%02d', $index );
		$image   = isset( $meta['image'] ) ? (string) $meta['image'] : '';
		$width   = isset( $meta['width'] ) ? (int) $meta['width'] : 0;
		$height  = isset( $meta['height'] ) ? (int) $meta['height'] : 0;
		$url     = get_permalink( $child );
		$url     = ( is_string( $url ) && '' !== $url ) ? $url : '';

		$items[] = array(
			'slug'          => (string) $child->post_name,
			'title'         => $title,
			'marker'        => $marker,
			'title_display' => $marker . ' — ' . $title,
			'url'           => $url,
			'image'         => '' !== $image ? shpigovsky_asset_uri( $image ) : '',
			'width'         => $width,
			'height'        => $height,
			'alt'           => $title,
			'text'          => shpigovsky_get_treatment_program_short_description( $page_id ),
			'page_id'       => $page_id,
		);
	}

	return $items;
}
