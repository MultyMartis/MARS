<?php
/**
 * Plugin Name: Shpigovsky Core
 * Plugin URI: https://example.invalid/shpigovsky-core
 * Description: FP-0002 functionality plugin — V9-06B skeleton. Module boundaries only; no content model registration yet.
 * Version: 0.2.0-skeleton
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

define( 'SHPIGOVSKY_CORE_VERSION', '0.2.0-skeleton' );
define( 'SHPIGOVSKY_CORE_FILE', __FILE__ );
define( 'SHPIGOVSKY_CORE_DIR', plugin_dir_path( __FILE__ ) );
define( 'SHPIGOVSKY_CORE_URI', plugin_dir_url( __FILE__ ) );
define( 'SHPIGOVSKY_CORE_SKELETON', true );

require_once SHPIGOVSKY_CORE_DIR . 'inc/compat.php';
require_once SHPIGOVSKY_CORE_DIR . 'src/Loader/Autoloader.php';

Shpigovsky\Core\Loader\Autoloader::register( SHPIGOVSKY_CORE_DIR . 'src' );

register_activation_hook( SHPIGOVSKY_CORE_FILE, array( 'Shpigovsky\Core\Plugin', 'activate' ) );
register_deactivation_hook( SHPIGOVSKY_CORE_FILE, array( 'Shpigovsky\Core\Plugin', 'deactivate' ) );

add_action(
	'plugins_loaded',
	static function () {
		Shpigovsky\Core\Plugin::init();
	},
	5
);
