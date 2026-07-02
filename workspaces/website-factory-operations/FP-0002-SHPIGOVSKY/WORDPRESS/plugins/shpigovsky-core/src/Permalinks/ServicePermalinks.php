<?php
/**
 * Nested service permalink module — rewrite rules deferred to V9-06C.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Permalinks;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Service permalink and rewrite boundary.
 */
final class ServicePermalinks implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'permalinks.service';
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
		add_action( 'init', array( __CLASS__, 'register_rewrite_rules' ), 20 );
	}

	/**
	 * Register nested service rewrite rules per FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.
	 *
	 * V9-06B: not executed while skeleton mode is active.
	 */
	public static function register_rewrite_rules() {
		// V9-06C implementation.
	}
}
