<?php
/**
 * Home page vendor enqueue — Swiper, Fancybox, Inputmask (D9-D / D9-E).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enqueue V9 home interaction vendors on front page only.
 *
 * CSS order matches static V9: vendor bundles first, theme overrides last.
 */
function shpigovsky_enqueue_home_vendors() {
	if ( ! is_front_page() ) {
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

	if ( is_readable( $vendor_dir . '/fancybox/fancybox.css' ) ) {
		wp_enqueue_style(
			'shpigovsky-fancybox',
			$vendor_base . '/fancybox/fancybox.css',
			array( 'shpigovsky-swiper' ),
			shpigovsky_asset_version( 'vendor/fancybox/fancybox.css' )
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

	if ( is_readable( $vendor_dir . '/fancybox/fancybox.umd.js' ) ) {
		wp_enqueue_script(
			'shpigovsky-fancybox',
			$vendor_base . '/fancybox/fancybox.umd.js',
			array(),
			shpigovsky_asset_version( 'vendor/fancybox/fancybox.umd.js' ),
			true
		);
	}

	if ( is_readable( $vendor_dir . '/inputmask/inputmask.min.js' ) ) {
		wp_enqueue_script(
			'shpigovsky-inputmask',
			$vendor_base . '/inputmask/inputmask.min.js',
			array(),
			shpigovsky_asset_version( 'vendor/inputmask/inputmask.min.js' ),
			true
		);
	}

	global $wp_styles;
	$theme_style_deps = array();

	if ( wp_style_is( 'shpigovsky-swiper', 'registered' ) || wp_style_is( 'shpigovsky-swiper', 'enqueued' ) ) {
		$theme_style_deps[] = 'shpigovsky-swiper';
	}

	if ( wp_style_is( 'shpigovsky-fancybox', 'registered' ) || wp_style_is( 'shpigovsky-fancybox', 'enqueued' ) ) {
		$theme_style_deps[] = 'shpigovsky-fancybox';
	}

	if ( ! empty( $theme_style_deps ) && isset( $wp_styles->registered['shpigovsky-v9'] ) ) {
		$wp_styles->registered['shpigovsky-v9']->deps = $theme_style_deps;
	}

	$shell_deps = array();

	if ( wp_script_is( 'shpigovsky-swiper', 'registered' ) || wp_script_is( 'shpigovsky-swiper', 'enqueued' ) ) {
		$shell_deps[] = 'shpigovsky-swiper';
	}

	if ( wp_script_is( 'shpigovsky-fancybox', 'registered' ) || wp_script_is( 'shpigovsky-fancybox', 'enqueued' ) ) {
		$shell_deps[] = 'shpigovsky-fancybox';
	}

	if ( wp_script_is( 'shpigovsky-inputmask', 'registered' ) || wp_script_is( 'shpigovsky-inputmask', 'enqueued' ) ) {
		$shell_deps[] = 'shpigovsky-inputmask';
	}

	if ( ! empty( $shell_deps ) && isset( $GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell'] ) ) {
		$GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell']->deps = $shell_deps;
	}
}
add_action( 'shpigovsky_enqueue_theme_assets', 'shpigovsky_enqueue_home_vendors' );
