<?php
/**
 * Plugin Name: MetaCODE WPilot
 * Plugin URI: https://example.invalid/metacode-wpilot
 * Description: DEV/test WPilot bridge with read-only inspection and backup/rollback recovery path.
 * Version: 0.3.0
 * Author: MetaCODE
 * License: GPL-2.0-or-later
 * Text Domain: metacode-wpilot
 * Domain Path: /languages
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'WPILOT_PLUGIN_FILE', __FILE__ );
define( 'WPILOT_PLUGIN_DIR', plugin_dir_path( __FILE__ ) );

require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-constants.php';

define( 'WPILOT_VERSION', WPilot_Constants::VERSION );
define( 'WPILOT_SCHEMA_VERSION', WPilot_Constants::SCHEMA_VERSION );
define( 'WPILOT_REST_NAMESPACE', WPilot_Constants::REST_NAMESPACE );

require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-response.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-errors.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-settings.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-connection-tracker.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-environment.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-request-context.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-auth.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-wpbakery-detector.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-site-reader.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-dry-run.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-checksum.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-operation-id.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-schema.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-audit-service.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-backup-service.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-rollback-service.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-scoped-replace-service.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-rest-controller.php';
require_once WPILOT_PLUGIN_DIR . 'admin/class-wpilot-admin-ui-model.php';
require_once WPILOT_PLUGIN_DIR . 'admin/class-wpilot-admin-page.php';
require_once WPILOT_PLUGIN_DIR . 'includes/class-wpilot-plugin.php';

register_activation_hook( __FILE__, array( 'WPilot_Settings', 'activate' ) );
register_deactivation_hook( __FILE__, array( 'WPilot_Settings', 'deactivate' ) );

add_action(
	'plugins_loaded',
	static function () {
		WPilot_Plugin::instance()->init();
	}
);
