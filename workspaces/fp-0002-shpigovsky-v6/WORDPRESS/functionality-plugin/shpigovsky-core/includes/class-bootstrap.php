<?php
/**
 * Plugin bootstrap — foundation modules disabled by default.
 *
 * @package Shpigovsky_Core
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Core bootstrap.
 */
class Shpigovsky_Core_Bootstrap {

	/**
	 * Initialize safe foundation hooks only.
	 */
	public static function init() {
		add_action( 'admin_notices', array( __CLASS__, 'admin_foundation_notice' ) );
	}

	/**
	 * Admin notice for foundation state.
	 */
	public static function admin_foundation_notice() {
		if ( ! current_user_can( 'manage_options' ) ) {
			return;
		}
		printf(
			'<div class="notice notice-info"><p><strong>Shpigovsky Core</strong> — %s</p></div>',
			esc_html__( 'FOUNDATION ONLY — no project content model registered.', 'shpigovsky-core' )
		);
	}
}
