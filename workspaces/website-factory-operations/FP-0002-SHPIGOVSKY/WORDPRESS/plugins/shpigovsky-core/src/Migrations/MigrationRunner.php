<?php
/**
 * Versioned data migrations module.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Migrations;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Migration runner boundary.
 */
final class MigrationRunner implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'migrations.runner';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ! shpigovsky_core_is_skeleton_mode();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'admin_init', array( __CLASS__, 'maybe_run_migrations' ) );
	}

	/**
	 * Run pending migrations when authorized.
	 */
	public static function maybe_run_migrations() {
		// V9-06D+ implementation.
	}
}
