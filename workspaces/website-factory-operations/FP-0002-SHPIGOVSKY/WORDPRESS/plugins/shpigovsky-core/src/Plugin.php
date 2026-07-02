<?php
/**
 * Plugin orchestrator — loads bounded modules when enabled.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core;

use Shpigovsky\Core\Admin\EditorRestrictions;
use Shpigovsky\Core\Admin\OptionsPage;
use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\Fields\AcfIntegration;
use Shpigovsky\Core\Fields\RepeaterValidation;
use Shpigovsky\Core\Forms\ConsultationHandler;
use Shpigovsky\Core\Migrations\MigrationRunner;
use Shpigovsky\Core\Permalinks\ServicePermalinks;
use Shpigovsky\Core\Settings\SiteSettings;

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
	private static $modules = array(
		Service::class,
		ServicePermalinks::class,
		AcfIntegration::class,
		RepeaterValidation::class,
		SiteSettings::class,
		MigrationRunner::class,
		ConsultationHandler::class,
		OptionsPage::class,
		EditorRestrictions::class,
	);

	/**
	 * Initialize plugin modules.
	 */
	public static function init() {
		foreach ( self::$modules as $module_class ) {
			if ( is_subclass_of( $module_class, ModuleInterface::class ) && $module_class::is_enabled() ) {
				$module_class::register();
			}
		}

		if ( shpigovsky_core_is_skeleton_mode() && is_admin() && current_user_can( 'manage_options' ) ) {
			add_action( 'admin_notices', array( __CLASS__, 'render_skeleton_notice' ) );
		}
	}

	/**
	 * Activation boundary — no rewrite flush or object mutations in skeleton phase.
	 */
	public static function activate() {
		// V9-06C+: versioned activation tasks only when model registration is authorized.
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
			esc_html__( 'V9-06B skeleton — modules present but disabled; no content model registered.', 'shpigovsky-core' )
		);
	}
}
