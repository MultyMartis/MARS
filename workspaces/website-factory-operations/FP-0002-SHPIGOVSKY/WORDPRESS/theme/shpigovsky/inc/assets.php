<?php
/**
 * Asset registration — V9 global shell (V9-06D7-A).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Resolve asset version from filemtime when available.
 *
 * @param string $relative_path Path under theme assets/.
 * @return string
 */
function shpigovsky_asset_version( $relative_path ) {
	$absolute = SHPIGOVSKY_THEME_DIR . '/assets/' . ltrim( $relative_path, '/' );

	if ( is_readable( $absolute ) ) {
		return (string) filemtime( $absolute );
	}

	return SHPIGOVSKY_THEME_VERSION;
}

/**
 * Register V9 global shell assets.
 */
function shpigovsky_enqueue_assets() {
	$v9_css_path = SHPIGOVSKY_THEME_DIR . '/assets/css/v9-style.css';

	if ( is_readable( $v9_css_path ) ) {
		wp_enqueue_style(
			'shpigovsky-v9',
			SHPIGOVSKY_THEME_URI . '/assets/css/v9-style.css',
			array(),
			shpigovsky_asset_version( 'css/v9-style.css' )
		);
	} else {
		wp_enqueue_style(
			'shpigovsky-foundation',
			SHPIGOVSKY_THEME_URI . '/assets/css/foundation.css',
			array(),
			SHPIGOVSKY_THEME_VERSION
		);
	}

	$child_css = SHPIGOVSKY_THEME_DIR . '/assets/css/service-child-services.css';
	$is_placeholder_service = is_singular( 'service' )
		&& function_exists( 'shpigovsky_resolve_service_layout_variant' )
		&& 'placeholder' === shpigovsky_resolve_service_layout_variant();
	if ( is_readable( $child_css ) && is_singular( 'service' ) && ! $is_placeholder_service ) {
		$child_deps = array();
		if ( wp_style_is( 'shpigovsky-v9', 'enqueued' ) || wp_style_is( 'shpigovsky-v9', 'registered' ) ) {
			$child_deps[] = 'shpigovsky-v9';
		} elseif ( wp_style_is( 'shpigovsky-foundation', 'enqueued' ) || wp_style_is( 'shpigovsky-foundation', 'registered' ) ) {
			$child_deps[] = 'shpigovsky-foundation';
		}
		wp_enqueue_style(
			'shpigovsky-service-child-services',
			SHPIGOVSKY_THEME_URI . '/assets/css/service-child-services.css',
			$child_deps,
			shpigovsky_asset_version( 'css/service-child-services.css' )
		);
	}

	$shell_js_path = SHPIGOVSKY_THEME_DIR . '/assets/js/v9-shell.js';

	if ( is_readable( $shell_js_path ) ) {
		wp_enqueue_script(
			'shpigovsky-v9-shell',
			SHPIGOVSKY_THEME_URI . '/assets/js/v9-shell.js',
			array(),
			shpigovsky_asset_version( 'js/v9-shell.js' ),
			true
		);
	}

	/**
	 * Extension hook for later waves (Swiper, Fancybox, Inputmask, page modules).
	 */
	do_action( 'shpigovsky_enqueue_theme_assets' );
}
add_action( 'wp_enqueue_scripts', 'shpigovsky_enqueue_assets' );

/**
 * Inline js-enabled flag for progressive enhancement parity with V9 static.
 */
function shpigovsky_js_enabled_flag() {
	echo "<script>(function(){document.documentElement.classList.add('js-enabled');})();</script>\n"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
}
add_action( 'wp_head', 'shpigovsky_js_enabled_flag', 0 );
