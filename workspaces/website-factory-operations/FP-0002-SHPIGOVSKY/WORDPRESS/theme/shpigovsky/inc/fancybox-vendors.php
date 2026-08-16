<?php
/**
 * Shared Fancybox vendor enqueue helper (V9-07A01).
 *
 * Comfort galleries reuse home/comfort.php on Home, /uslugi/, subdivision and
 * general service stacks. Fancybox must be present wherever that partial renders.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register/enqueue local Fancybox CSS+JS and attach as shell dependency.
 *
 * Idempotent: safe to call from multiple page-scoped vendor loaders.
 *
 * @param bool $require_swiper_css_dep When true, Fancybox CSS depends on Swiper CSS if registered.
 * @return void
 */
function shpigovsky_enqueue_fancybox_vendor( $require_swiper_css_dep = false ) {
	$vendor_base = SHPIGOVSKY_THEME_URI . '/assets/vendor';
	$vendor_dir  = SHPIGOVSKY_THEME_DIR . '/assets/vendor';

	$fancybox_style_deps = array();
	if ( $require_swiper_css_dep && ( wp_style_is( 'shpigovsky-swiper', 'registered' ) || wp_style_is( 'shpigovsky-swiper', 'enqueued' ) ) ) {
		$fancybox_style_deps[] = 'shpigovsky-swiper';
	}

	if ( is_readable( $vendor_dir . '/fancybox/fancybox.css' ) && ! wp_style_is( 'shpigovsky-fancybox', 'enqueued' ) ) {
		if ( ! wp_style_is( 'shpigovsky-fancybox', 'registered' ) ) {
			wp_register_style(
				'shpigovsky-fancybox',
				$vendor_base . '/fancybox/fancybox.css',
				$fancybox_style_deps,
				shpigovsky_asset_version( 'vendor/fancybox/fancybox.css' )
			);
		}
		wp_enqueue_style( 'shpigovsky-fancybox' );
	}

	if ( is_readable( $vendor_dir . '/fancybox/fancybox.umd.js' ) && ! wp_script_is( 'shpigovsky-fancybox', 'enqueued' ) ) {
		if ( ! wp_script_is( 'shpigovsky-fancybox', 'registered' ) ) {
			wp_register_script(
				'shpigovsky-fancybox',
				$vendor_base . '/fancybox/fancybox.umd.js',
				array(),
				shpigovsky_asset_version( 'vendor/fancybox/fancybox.umd.js' ),
				true
			);
		}
		wp_enqueue_script( 'shpigovsky-fancybox' );
	}

	global $wp_styles;
	if ( isset( $wp_styles->registered['shpigovsky-v9'] ) && ( wp_style_is( 'shpigovsky-fancybox', 'registered' ) || wp_style_is( 'shpigovsky-fancybox', 'enqueued' ) ) ) {
		$deps = (array) $wp_styles->registered['shpigovsky-v9']->deps;
		if ( ! in_array( 'shpigovsky-fancybox', $deps, true ) ) {
			$wp_styles->registered['shpigovsky-v9']->deps = array_merge( $deps, array( 'shpigovsky-fancybox' ) );
		}
	}

	if ( isset( $GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell'] ) && ( wp_script_is( 'shpigovsky-fancybox', 'registered' ) || wp_script_is( 'shpigovsky-fancybox', 'enqueued' ) ) ) {
		$shell_deps = (array) $GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell']->deps;
		if ( ! in_array( 'shpigovsky-fancybox', $shell_deps, true ) ) {
			$GLOBALS['wp_scripts']->registered['shpigovsky-v9-shell']->deps = array_merge( $shell_deps, array( 'shpigovsky-fancybox' ) );
		}
	}
}

/**
 * PROD-P07: Fancybox on Generic Content pages that enable shared Comfort («О доме»).
 *
 * @return void
 */
function shpigovsky_enqueue_generic_reusable_vendors() {
	if ( ! is_page_template( 'page-templates/generic.php' ) ) {
		return;
	}

	$page_id = (int) get_queried_object_id();
	if ( $page_id <= 0 || ! function_exists( 'get_field' ) ) {
		return;
	}

	$blocks = get_field( 'generic_page_reusable_blocks', $page_id );
	if ( ! is_array( $blocks ) || ! in_array( 'about_home', $blocks, true ) ) {
		return;
	}

	shpigovsky_enqueue_fancybox_vendor( true );
}
add_action( 'wp_enqueue_scripts', 'shpigovsky_enqueue_generic_reusable_vendors', 30 );
