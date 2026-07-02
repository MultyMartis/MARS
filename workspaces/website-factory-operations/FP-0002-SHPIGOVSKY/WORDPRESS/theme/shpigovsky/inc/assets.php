<?php
/**
 * Asset registration boundary — V9 build handoff deferred to V9-07+.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register skeleton stylesheet only until V9 assets are authorized.
 */
function shpigovsky_enqueue_assets() {
	wp_enqueue_style(
		'shpigovsky-foundation',
		SHPIGOVSKY_THEME_URI . '/assets/css/foundation.css',
		array(),
		SHPIGOVSKY_THEME_VERSION
	);

	/**
	 * V9 compiled assets (style.css, main.js, vendor bundles) enqueue here in V9-07A+.
	 * Source authority: workspaces/fp-0002-shpigovsky-v9/dist/
	 */
	do_action( 'shpigovsky_enqueue_theme_assets' );
}
add_action( 'wp_enqueue_scripts', 'shpigovsky_enqueue_assets' );
