<?php
/**
 * Services Hub page ACF read helpers and Service CPT queries — V9-06D7-C.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Services Hub page post ID for ACF context.
 *
 * @return int
 */
function shpigovsky_get_services_hub_page_id() {
	if ( is_page_template( 'page-templates/services-hub.php' ) ) {
		return (int) get_queried_object_id();
	}

	$pages = get_posts(
		array(
			'post_type'      => 'page',
			'post_status'    => 'publish',
			'meta_key'       => '_wp_page_template',
			'meta_value'     => 'page-templates/services-hub.php',
			'posts_per_page' => 1,
			'no_found_rows'  => true,
			'fields'         => 'ids',
		)
	);

	if ( ! empty( $pages[0] ) ) {
		return (int) $pages[0];
	}

	return 0;
}

/**
 * Read a scalar Services Hub ACF field safely.
 *
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_services_hub_field( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$page_id = shpigovsky_get_services_hub_page_id();

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
 * Read a boolean Services Hub ACF field safely.
 *
 * @param string $field_name Field name.
 * @return bool
 */
function shpigovsky_get_services_hub_bool( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return false;
	}

	$page_id = shpigovsky_get_services_hub_page_id();

	if ( $page_id <= 0 ) {
		return false;
	}

	return (bool) get_field( $field_name, $page_id );
}

/**
 * Read a bounded Services Hub repeater safely.
 *
 * @param string $field_name Repeater field name.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_services_hub_repeater( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$page_id = shpigovsky_get_services_hub_page_id();

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
 * Read a scalar service ACF field safely.
 *
 * @param int    $post_id    Service post ID.
 * @param string $field_name Field name.
 * @return string
 */
function shpigovsky_get_service_field( $post_id, $field_name ) {
	if ( ! function_exists( 'get_field' ) || $post_id <= 0 ) {
		return '';
	}

	$value = get_field( $field_name, $post_id );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Resolve V9 modifier classes for a parent service slug.
 *
 * @param string $slug Parent service slug.
 * @return string
 */
function shpigovsky_get_services_hub_group_modifier( $slug ) {
	$map = array(
		'zavisimosti'                         => 'services-category-hub--addictions services-category-hub--no-gallery',
		'psihicheskoe-zdorovie'               => 'services-category-hub--mental-health services-category-hub--no-gallery',
		'rasstroystva-pischevogo-povedeniya'  => 'services-category-hub--eating-disorders services-category-hub--no-gallery services-category-hub--compact',
		'genotipirovanie'                     => 'services-category-hub--genotyping services-category-hub--no-gallery services-category-hub--compact',
	);

	if ( isset( $map[ $slug ] ) ) {
		return $map[ $slug ];
	}

	return 'services-category-hub--no-gallery';
}

/**
 * Build child service card data from a service post.
 *
 * @param WP_Post $child Child service post.
 * @return array{title:string,url:string,text:string}|null
 */
function shpigovsky_build_services_hub_child_card( $child ) {
	if ( ! $child instanceof WP_Post ) {
		return null;
	}

	$title = get_the_title( $child );
	$url   = get_permalink( $child );

	if ( '' === $title ) {
		return null;
	}

	$text = shpigovsky_get_service_field( $child->ID, 'intro_text' );

	if ( '' === $text ) {
		$text = shpigovsky_get_service_field( $child->ID, 'hero_lead' );
	}

	if ( '' === $text ) {
		$text = trim( (string) get_the_excerpt( $child ) );
	}

	return array(
		'title' => $title,
		'url'   => is_string( $url ) ? $url : '',
		'text'  => $text,
	);
}

/**
 * Build grouped Services Hub sections from hierarchical Service CPT.
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_services_hub_groups() {
	if ( ! post_type_exists( 'service' ) ) {
		return array();
	}

	$query_mode = shpigovsky_get_services_hub_field( 'services_hub_query_mode' );

	if ( '' === $query_mode ) {
		$query_mode = 'grouped_by_parent';
	}

	if ( 'flat' === $query_mode ) {
		return shpigovsky_get_services_hub_flat_group();
	}

	$parents = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => 0,
			'posts_per_page' => 12,
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
				'posts_per_page' => 30,
				'orderby'        => 'menu_order',
				'order'          => 'ASC',
				'no_found_rows'  => true,
			)
		);

		$cards = array();

		foreach ( $children as $child ) {
			$card = shpigovsky_build_services_hub_child_card( $child );

			if ( null !== $card ) {
				$cards[] = $card;
			}
		}

		if ( empty( $cards ) ) {
			$parent_card = shpigovsky_build_services_hub_child_card( $parent );

			if ( null !== $parent_card ) {
				$cards[] = $parent_card;
			}
		}

		if ( empty( $cards ) ) {
			continue;
		}

		$slug = $parent->post_name;

		$lead_primary   = shpigovsky_get_service_field( $parent->ID, 'hero_lead' );
		$lead_secondary = shpigovsky_get_service_field( $parent->ID, 'intro_text' );

		if ( '' === $lead_secondary ) {
			$lead_secondary = shpigovsky_get_service_field( $parent->ID, 'intro_note' );
		}

		$groups[] = array(
			'parent_id'      => $parent->ID,
			'title'          => get_the_title( $parent ),
			'slug'           => $slug,
			'lead_primary'   => $lead_primary,
			'lead_secondary' => $lead_secondary,
			'modifier_class' => shpigovsky_get_services_hub_group_modifier( $slug ),
			'section_id'     => 'services-category-' . sanitize_html_class( $slug ) . '-heading',
			'cta_source'     => 'services-' . sanitize_html_class( $slug ),
			'children'       => $cards,
			'gallery'        => array(),
		);
	}

	return $groups;
}

/**
 * Build a single flat group when query mode is flat.
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_services_hub_flat_group() {
	$services = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'posts_per_page' => 50,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
			'no_found_rows'  => true,
		)
	);

	if ( empty( $services ) ) {
		return array();
	}

	$cards = array();

	foreach ( $services as $service ) {
		$card = shpigovsky_build_services_hub_child_card( $service );

		if ( null !== $card ) {
			$cards[] = $card;
		}
	}

	if ( empty( $cards ) ) {
		return array();
	}

	return array(
		array(
			'parent_id'      => 0,
			'title'          => __( 'Услуги центра', 'shpigovsky' ),
			'slug'           => 'all-services',
			'lead_primary'   => shpigovsky_get_services_hub_field( 'services_hub_intro' ),
			'lead_secondary' => '',
			'modifier_class' => 'services-category-hub--no-gallery',
			'section_id'     => 'services-category-all-heading',
			'cta_source'     => 'services-flat',
			'children'       => $cards,
			'gallery'        => array(),
		),
	);
}

/**
 * Whether Services Hub has renderable service groups.
 *
 * @return bool
 */
function shpigovsky_services_hub_has_groups() {
	return ! empty( shpigovsky_get_services_hub_groups() );
}
