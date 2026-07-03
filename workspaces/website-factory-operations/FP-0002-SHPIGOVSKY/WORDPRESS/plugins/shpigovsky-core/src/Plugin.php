<?php
/**
 * Plugin orchestrator — loads bounded modules when enabled.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Main plugin bootstrap.
 */
final class Plugin {

	/**
	 * Registered module classes.
	 *
	 * @var class-string<ModuleInterface>[]
	 */
	private static $modules = null;

	/**
	 * Initialize plugin modules.
	 */
	public static function init() {
		foreach ( self::get_modules() as $module_class ) {
			if ( is_subclass_of( $module_class, ModuleInterface::class ) && $module_class::is_enabled() ) {
				$module_class::register();
			}
		}

		if ( shpigovsky_core_is_skeleton_mode() && is_admin() && current_user_can( 'manage_options' ) ) {
			add_action( 'admin_notices', array( __CLASS__, 'render_skeleton_notice' ) );
		}
	}

	/**
	 * Activation boundary — no rewrite flush or object mutations in source-only phase.
	 */
	public static function activate() {
		// V9-06D+ delivery may flush rewrites once after explicit operator authorization.
	}

	/**
	 * Deactivation boundary — no destructive cleanup in skeleton phase.
	 */
	public static function deactivate() {
		// V9-06C+: bounded deactivation tasks when authorized.
	}

	/**
	 * Admin notice for skeleton state.
	 */
	public static function render_skeleton_notice() {
		printf(
			'<div class="notice notice-info"><p><strong>Shpigovsky Core</strong> — %s</p></div>',
			esc_html__( 'Skeleton mode is active — content-model modules are disabled until source mode is changed.', 'shpigovsky-core' )
		);
	}

	/**
	 * Return phase-aware module classes.
	 *
	 * @return array<int, class-string<ModuleInterface>>
	 */
	private static function get_modules() {
		if ( null === self::$modules ) {
			self::$modules = ModuleRegistry::get_module_classes();
		}

		return self::$modules;
	}
}
