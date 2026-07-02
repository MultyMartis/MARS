<?php
/**
 * Asset loader placeholder — no frontend assets until approved handoff.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enqueue foundation-only stylesheet.
 */
function shpigovsky_enqueue_assets() {
	wp_enqueue_style(
		'shpigovsky-foundation',
		SHPIGOVSKY_THEME_URI . '/assets/css/foundation.css',
		array(),
		SHPIGOVSKY_THEME_VERSION
	);
}
add_action( 'wp_enqueue_scripts', 'shpigovsky_enqueue_assets' );
