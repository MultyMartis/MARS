<?php
/**
 * Plugin Name: FWS Synthetic Core
 * Plugin URI: https://example.invalid/fws-synthetic-core
 * Description: Functionality plugin for FWS-0001 — CPT service, post meta, ACF Free fallback.
 * Version: 1.0.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: Forge WordPress Synthetic
 * Text Domain: fws-synthetic
 * License: GPL-2.0-or-later
 *
 * @package FWS_Synthetic_Core
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'FWS_SYNTHETIC_CORE_VERSION', '1.0.0' );
define( 'FWS_SYNTHETIC_CORE_FILE', __FILE__ );
define( 'FWS_SYNTHETIC_CORE_DIR', plugin_dir_path( __FILE__ ) );
define( 'FWS_SYNTHETIC_CORE_URI', plugin_dir_url( __FILE__ ) );

require_once FWS_SYNTHETIC_CORE_DIR . 'includes/class-cpt-service.php';
require_once FWS_SYNTHETIC_CORE_DIR . 'includes/class-meta.php';
require_once FWS_SYNTHETIC_CORE_DIR . 'includes/class-acf-fallback.php';

/**
 * Bootstrap plugin components.
 */
function fws_synthetic_core_init() {
	FWS_Synthetic_CPT_Service::init();
	FWS_Synthetic_Meta::init();
	FWS_Synthetic_ACF_Fallback::init();
}
add_action( 'plugins_loaded', 'fws_synthetic_core_init' );

/**
 * Load ACF JSON field groups from WORDPRESS/acf-json.
 *
 * @param array<int, string> $paths Existing paths.
 * @return array<int, string>
 */
function fws_synthetic_core_acf_json_load( $paths ) {
	$paths[] = trailingslashit( dirname( dirname( FWS_SYNTHETIC_CORE_DIR ) ) ) . 'acf-json';
	return $paths;
}
add_filter( 'acf/settings/load_json', 'fws_synthetic_core_acf_json_load' );

/**
 * Save ACF JSON to shared folder (when ACF sync is used).
 *
 * @param string $path Default save path.
 * @return string
 */
function fws_synthetic_core_acf_json_save( $path ) {
	return trailingslashit( dirname( dirname( FWS_SYNTHETIC_CORE_DIR ) ) ) . 'acf-json';
}
add_filter( 'acf/settings/save_json', 'fws_synthetic_core_acf_json_save' );
