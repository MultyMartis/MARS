<?php
/**
 * Favicon output — V9 static assets for frontend, admin, and login.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether theme-packaged favicon assets are available.
 *
 * @return bool
 */
function shpigovsky_has_theme_favicon_assets() {
	return is_readable( SHPIGOVSKY_THEME_DIR . '/assets/favicon/favicon.svg' );
}

/**
 * Output favicon link tags when Site Icon is not configured.
 */
function shpigovsky_output_favicon_tags() {
	if ( function_exists( 'has_site_icon' ) && has_site_icon() ) {
		return;
	}

	if ( ! shpigovsky_has_theme_favicon_assets() ) {
		return;
	}

	$base = trailingslashit( shpigovsky_asset_uri( 'favicon' ) );

	$tags = array(
		'<link rel="icon" type="image/svg+xml" href="' . esc_url( $base . 'favicon.svg' ) . '">',
	);

	if ( is_readable( SHPIGOVSKY_THEME_DIR . '/assets/favicon/favicon-32x32.png' ) ) {
		$tags[] = '<link rel="icon" type="image/png" sizes="32x32" href="' . esc_url( $base . 'favicon-32x32.png' ) . '">';
	}

	if ( is_readable( SHPIGOVSKY_THEME_DIR . '/assets/favicon/favicon.ico' ) ) {
		$tags[] = '<link rel="icon" href="' . esc_url( $base . 'favicon.ico' ) . '" sizes="any">';
	}

	if ( is_readable( SHPIGOVSKY_THEME_DIR . '/assets/favicon/apple-touch-icon.png' ) ) {
		$tags[] = '<link rel="apple-touch-icon" sizes="180x180" href="' . esc_url( $base . 'apple-touch-icon.png' ) . '">';
	}

	echo implode( "\n", $tags ) . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
}
add_action( 'wp_head', 'shpigovsky_output_favicon_tags', 5 );
add_action( 'admin_head', 'shpigovsky_output_favicon_tags', 5 );
add_action( 'login_head', 'shpigovsky_output_favicon_tags', 5 );
