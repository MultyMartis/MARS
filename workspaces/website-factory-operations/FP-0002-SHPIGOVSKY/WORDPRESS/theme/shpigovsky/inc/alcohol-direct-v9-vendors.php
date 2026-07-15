<?php
/**
 * Alcohol direct V9 vendor enqueue — Swiper for specialists/reviews sliders (V9-06E13).
 *
 * Static V9 usluga-konechnaya-v1.html requires Swiper on service leaf; home-vendors.php
 * limits Swiper to is_front_page() only.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether the current request is the general service stack (legacy alcohol-special name).
 *
 * @return bool
 */
function shpigovsky_is_alcohol_direct_v9_page() {
	if ( ! is_singular( 'service' ) ) {
		return false;
	}

	return function_exists( 'shpigovsky_is_service_general_variant' )
		? shpigovsky_is_service_general_variant( shpigovsky_resolve_service_layout_variant() )
		: ( 'service-general' === shpigovsky_resolve_service_layout_variant() );
}

/**
 * Enqueue Swiper vendor on alcohol leaf for specialists slider parity.
 */
function shpigovsky_enqueue_alcohol_direct_v9_vendors() {
	if ( ! shpigovsky_is_alcohol_direct_v9_page() ) {
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
add_action( 'shpigovsky_enqueue_theme_assets', 'shpigovsky_enqueue_alcohol_direct_v9_vendors' );
