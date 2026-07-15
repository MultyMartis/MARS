<?php
/**
 * Services hub (/uslugi/) vendor enqueue — Swiper for category galleries (V9-06E33-FIX01).
 *
 * home-vendors.php limits Swiper to is_front_page(); category card sliders on the
 * services hub need the same local Swiper vendor (no CDN).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enqueue Swiper on the services hub page template only.
 */
function shpigovsky_enqueue_services_hub_vendors() {
	if ( ! is_page_template( 'page-templates/services-hub.php' ) ) {
		return;
	}

	$vendor_base = SHPIGOVSKY_THEME_URI . '/assets/vendor';
	$vendor_dir  = SHPIGOVSKY_THEME_DIR . '/assets/vendor';

	if ( is_readable( $vendor_dir . '/swiper/swiper-bundle.min.css' ) ) {
		wp_enqueue_style(
			'shpigovsky-swiper',
			$vendor_base . '/swiper/swiper-bundle.min.css',
			array(),
			shpigovsky_asset_version( 'vendor/swiper/swiper-bundle.min.css' )
		);
	}

	if ( is_readable( $vendor_dir . '/swiper/swiper-bundle.min.js' ) ) {
		wp_enqueue_script(
			'shpigovsky-swiper',
			$vendor_base . '/swiper/swiper-bundle.min.js',
			array(),
			shpigovsky_asset_version( 'vendor/swiper/swiper-bundle.min.js' ),
			true
		);
	}

	global $wp_styles;

	if ( wp_style_is( 'shpigovsky-swiper', 'registered' ) || wp_style_is( 'shpigovsky-swiper', 'enqueued' ) ) {
		if ( isset( $wp_styles->registered['shpigovsky-v9'] ) ) {
			$deps = (array) $wp_styles->registered['shpigovsky-v9']->deps;
			if ( ! in_array( 'shpigovsky-swiper', $deps, true ) ) {
				$wp_styles->registered['shpigovsky-v9']->deps = array_merge( $deps, array( 'shpigovsky-swiper' ) );
			}
		}
	}

	if ( wp_script_is( 'shpigovsky-swiper', 'registered' ) || wp_script_is( 'shpigovsky-swiper', 'enqueued' ) ) {
		if ( isset( $GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell'] ) ) {
			$shell_deps = (array) $GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell']->deps;
			if ( ! in_array( 'shpigovsky-swiper', $shell_deps, true ) ) {
				$GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell']->deps = array_merge( $shell_deps, array( 'shpigovsky-swiper' ) );
			}
		}
	}
}
add_action( 'shpigovsky_enqueue_theme_assets', 'shpigovsky_enqueue_services_hub_vendors' );
