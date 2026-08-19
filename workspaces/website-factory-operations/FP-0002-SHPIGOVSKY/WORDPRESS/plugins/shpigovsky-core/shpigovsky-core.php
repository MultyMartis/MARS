<?php
/**
 * Plugin Name: Shpigovsky Core
 * Plugin URI: https://example.invalid/shpigovsky-core
 * Description: FP-0002 functionality plugin — cookie consent foundation, truthful Admin status, and preserved production editorial reality.
 * Version: 0.3.17-p18e-ab
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

define( 'SHPIGOVSKY_CORE_VERSION', '0.3.17-p18e-ab' );
define( 'SHPIGOVSKY_CORE_FILE', __FILE__ );
define( 'SHPIGOVSKY_CORE_DIR', plugin_dir_path( __FILE__ ) );
define( 'SHPIGOVSKY_CORE_URI', plugin_dir_url( __FILE__ ) );
define( 'SHPIGOVSKY_CORE_MODE', 'content_model' );
define( 'SHPIGOVSKY_CORE_SKELETON', 'skeleton' === SHPIGOVSKY_CORE_MODE );
define( 'SHPIGOVSKY_CORE_V9_06C_SOURCE_IMPLEMENTED', true );
define( 'SHPIGOVSKY_CORE_V9_06C1_SOURCE_GATE_RESOLVED', true );

require_once SHPIGOVSKY_CORE_DIR . 'inc/compat.php';
require_once SHPIGOVSKY_CORE_DIR . 'src/Loader/Autoloader.php';

Shpigovsky\Core\Loader\Autoloader::register( SHPIGOVSKY_CORE_DIR . 'src' );

register_activation_hook( SHPIGOVSKY_CORE_FILE, array( 'Shpigovsky\Core\Plugin', 'activate' ) );
register_deactivation_hook( SHPIGOVSKY_CORE_FILE, array( 'Shpigovsky\Core\Plugin', 'deactivate' ) );

/**
 * Load plugin text domain for admin/runtime strings (V9-06E39 localization foundation).
 */
add_action(
	'init',
	static function () {
		load_plugin_textdomain(
			'shpigovsky-core',
			false,
			dirname( plugin_basename( SHPIGOVSKY_CORE_FILE ) ) . '/languages'
		);
	},
	0
);

add_action(
	'plugins_loaded',
	static function () {
		Shpigovsky\Core\Plugin::init();
	},
	5
);
