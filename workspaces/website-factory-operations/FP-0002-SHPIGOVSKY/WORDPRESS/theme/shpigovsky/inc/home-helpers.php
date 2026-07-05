<?php
/**
 * Home page ACF read helpers — V9-06D7-B source integration.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Front page post ID for ACF context.
 *
 * @return int
 */
function shpigovsky_get_front_page_id() {
	$page_id = (int) get_option( 'page_on_front' );

	if ( $page_id > 0 ) {
		return $page_id;
	}

	if ( is_singular( 'page' ) ) {
		return (int) get_queried_object_id();
	}

	return 0;
}

/**
 * Read a scalar home ACF field safely.
 *
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_home_field( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$page_id = shpigovsky_get_front_page_id();

	if ( $page_id <= 0 ) {
		return '';
	}

	$value = get_field( $field_name, $page_id );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Read a boolean home ACF field safely.
 *
 * @param string $field_name Field name.
 * @return bool
 */
function shpigovsky_get_home_bool( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return false;
	}

	$page_id = shpigovsky_get_front_page_id();

	if ( $page_id <= 0 ) {
		return false;
	}

	return (bool) get_field( $field_name, $page_id );
}

/**
 * Read a bounded home repeater safely.
 *
 * @param string $field_name Repeater field name.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_home_repeater( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$page_id = shpigovsky_get_front_page_id();

	if ( $page_id <= 0 ) {
		return array();
	}

	$rows = get_field( $field_name, $page_id );

	if ( ! is_array( $rows ) ) {
		return array();
	}

	$normalized = array();

	foreach ( $rows as $row ) {
		if ( is_array( $row ) ) {
			$normalized[] = $row;
		}
	}

	return $normalized;
}

/**
 * Static V9 home hero image fallback when ACF image is not seeded.
 *
 * D9-C: theme asset only — no DB/media upload required.
 *
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_home_hero_image_fallback() {
	$relative = 'assets/img/hero/hero-main.png';
	$path     = SHPIGOVSKY_THEME_DIR . '/' . $relative;

	if ( ! is_readable( $path ) ) {
		return array(
			'url'    => '',
			'alt'    => '',
			'width'  => 0,
			'height' => 0,
		);
	}

	return array(
		'url'    => SHPIGOVSKY_THEME_URI . '/' . $relative,
		'alt'    => '',
		'width'  => 2230,
		'height' => 1246,
	);
}

/**
 * Resolve ACF image array to URL.
 *
 * @param mixed $image Image field value.
 * @param string $size Image size slug.
 * @return string
 */
function shpigovsky_acf_image_url( $image, $size = 'full' ) {
	if ( ! is_array( $image ) ) {
		return '';
	}

	if ( ! empty( $image['sizes'][ $size ] ) ) {
		return (string) $image['sizes'][ $size ];
	}

	if ( ! empty( $image['url'] ) ) {
		return (string) $image['url'];
	}

	return '';
}

/**
 * Resolve ACF image alt text.
 *
 * @param mixed $image Image field value.
 * @return string
 */
function shpigovsky_acf_image_alt( $image ) {
	if ( ! is_array( $image ) ) {
		return '';
	}

	if ( ! empty( $image['alt'] ) ) {
		return trim( (string) $image['alt'] );
	}

	return '';
}

/**
 * Build service accordion groups from the service CPT (read-only query).
 *
 * @return array<int, array{title:string,items:array<int, array{title:string,url:string}>}>
 */
function shpigovsky_get_home_service_accordion_groups() {
	if ( ! post_type_exists( 'service' ) ) {
		return array();
	}

	$parents = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => 0,
			'posts_per_page' => 6,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
			'no_found_rows'  => true,
		)
	);

	if ( empty( $parents ) ) {
		return array();
	}

	$groups = array();

	foreach ( $parents as $parent ) {
		if ( ! $parent instanceof WP_Post ) {
			continue;
		}

		$children = get_posts(
			array(
				'post_type'      => 'service',
				'post_status'    => 'publish',
				'post_parent'    => $parent->ID,
				'posts_per_page' => 20,
				'orderby'        => 'menu_order',
				'order'          => 'ASC',
				'no_found_rows'  => true,
			)
		);

		$items = array();

		foreach ( $children as $child ) {
			if ( ! $child instanceof WP_Post ) {
				continue;
			}

			$items[] = array(
				'title' => get_the_title( $child ),
				'url'   => get_permalink( $child ),
			);
		}

		if ( empty( $items ) ) {
			continue;
		}

		$groups[] = array(
			'title' => get_the_title( $parent ),
			'items' => $items,
		);
	}

	return $groups;
}

/**
 * Fallback accordion groups from home_service_nav_items when CPT query is empty.
 *
 * @return array<int, array{title:string,items:array<int, array{title:string,url:string,text:string}>}>
 */
function shpigovsky_get_home_nav_accordion_fallback() {
	$rows = shpigovsky_get_home_repeater( 'home_service_nav_items' );

	if ( empty( $rows ) ) {
		return array();
	}

	$groups = array();

	foreach ( $rows as $row ) {
		$title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$text  = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';

		if ( '' === $title && '' === $text ) {
			continue;
		}

		$groups[] = array(
			'title' => $title,
			'items' => array(
				array(
					'title' => $title,
					'url'   => '',
					'text'  => $text,
				),
			),
		);
	}

	return $groups;
}
