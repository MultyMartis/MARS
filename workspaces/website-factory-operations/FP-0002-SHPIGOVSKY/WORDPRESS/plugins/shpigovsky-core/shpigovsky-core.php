<?php
/**
 * Plugin Name: Shpigovsky Core
 * Plugin URI: https://example.invalid/shpigovsky-core
 * Description: FP-0002 functionality plugin — V9-06C.1 content model source activation gate resolved. Runtime delivery remains separate.
 * Version: 0.3.1-v9-06c1-source
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

define( 'SHPIGOVSKY_CORE_VERSION', '0.3.1-v9-06c1-source' );
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

add_action(
	'plugins_loaded',
	static function () {
		Shpigovsky\Core\Plugin::init();
	},
	5
);
