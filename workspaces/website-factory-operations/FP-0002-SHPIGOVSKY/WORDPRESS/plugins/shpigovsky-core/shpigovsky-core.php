<?php
/**
 * Plugin Name: Shpigovsky Core
 * Plugin URI: https://example.invalid/shpigovsky-core
 * Description: FP-0002 functionality plugin — FOUNDATION ONLY. No project content model yet.
 * Version: 0.1.0
 * Requires at least: 6.0
 * Requires PHP: 8.0
 * Author: Forge WordPress / FP-0002
 * Text Domain: shpigovsky-core
 * License: GPL-2.0-or-later
 *
 * @package Shpigovsky_Core
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'SHPIGOVSKY_CORE_VERSION', '0.1.0' );
define( 'SHPIGOVSKY_CORE_FILE', __FILE__ );
define( 'SHPIGOVSKY_CORE_DIR', plugin_dir_path( __FILE__ ) );
define( 'SHPIGOVSKY_CORE_URI', plugin_dir_url( __FILE__ ) );

require_once SHPIGOVSKY_CORE_DIR . 'includes/class-bootstrap.php';

/**
 * Initialize plugin.
 */
function shpigovsky_core_init() {
	Shpigovsky_Core_Bootstrap::init();
}
add_action( 'plugins_loaded', 'shpigovsky_core_init' );

/**
 * ACF JSON load path — project source directory.
 *
 * @param array<int, string> $paths Existing paths.
 * @return array<int, string>
 */
function shpigovsky_core_acf_json_load( $paths ) {
	$paths[] = trailingslashit( dirname( dirname( SHPIGOVSKY_CORE_DIR ) ) ) . 'acf-json';
	return $paths;
}
add_filter( 'acf/settings/load_json', 'shpigovsky_core_acf_json_load' );

/**
 * ACF JSON save path.
 *
 * @param string $path Default save path.
 * @return string
 */
function shpigovsky_core_acf_json_save( $path ) {
	return trailingslashit( dirname( dirname( SHPIGOVSKY_CORE_DIR ) ) ) . 'acf-json';
}
add_filter( 'acf/settings/save_json', 'shpigovsky_core_acf_json_save' );
