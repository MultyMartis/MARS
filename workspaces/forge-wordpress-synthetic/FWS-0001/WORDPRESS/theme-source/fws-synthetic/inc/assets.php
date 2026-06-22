<?php
/**
 * Enqueue theme styles and scripts.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enqueue front-end assets.
 */
function fws_synthetic_enqueue_assets() {
	wp_enqueue_style(
		'fws-synthetic-style',
		FWS_SYNTHETIC_URI . '/assets/css/style.css',
		array(),
		FWS_SYNTHETIC_VERSION
	);

	wp_enqueue_script(
		'fws-synthetic-main',
		FWS_SYNTHETIC_URI . '/assets/js/main.js',
		array(),
		FWS_SYNTHETIC_VERSION,
		true
	);
}
add_action( 'wp_enqueue_scripts', 'fws_synthetic_enqueue_assets' );
