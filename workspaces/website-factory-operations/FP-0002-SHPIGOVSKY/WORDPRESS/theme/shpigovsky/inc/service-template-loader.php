<?php
/**
 * Service template loader — layout meta routing boundary (skeleton).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Allowed service layout variants (architecture contract).
 *
 * @return string[]
 */
function shpigovsky_service_layout_variants() {
	return array( 'subdivision', 'leaf', 'alcohol-special' );
}

/**
 * Resolve service layout variant for the current post.
 *
 * V9-06B: returns skeleton default only — no ACF/meta reads yet.
 *
 * @return string
 */
function shpigovsky_get_service_layout_variant() {
	/**
	 * Filter service layout variant once field integration exists (V9-06C+).
	 *
	 * @param string $variant Layout variant slug.
	 */
	return apply_filters( 'shpigovsky_service_layout_variant', 'leaf' );
}

/**
 * Map layout variant to stack template slug.
 *
 * @param string $variant Layout variant.
 * @return string
 */
function shpigovsky_service_stack_slug( $variant ) {
	$map = array(
		'subdivision'     => 'subdivision-stack',
		'leaf'            => 'leaf-stack',
		'alcohol-special' => 'alcohol-stack',
	);

	return isset( $map[ $variant ] ) ? $map[ $variant ] : 'leaf-stack';
}

/**
 * Load the service stack template part for the current service.
 */
function shpigovsky_load_service_template() {
	$variant = shpigovsky_get_service_layout_variant();
	$slug    = shpigovsky_service_stack_slug( $variant );

	get_template_part( 'template-parts/service/' . $slug );
}
