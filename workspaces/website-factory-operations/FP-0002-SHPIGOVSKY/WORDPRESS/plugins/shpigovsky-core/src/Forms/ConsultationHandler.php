<?php
/**
 * Consultation form handler — server POST boundary.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Forms;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Consultation form submission handler.
 */
final class ConsultationHandler implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'forms.consultation';
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
		add_action( 'admin_post_nopriv_shpigovsky_consultation', array( __CLASS__, 'handle_submission' ) );
		add_action( 'admin_post_shpigovsky_consultation', array( __CLASS__, 'handle_submission' ) );
	}

	/**
	 * Handle consultation form POST.
	 *
	 * V9-06B: not registered while skeleton mode is active.
	 */
	public static function handle_submission() {
		// V9-08+ implementation per FP-0002-LOCAL-MAIL-AND-FORM-POLICY-v1.md.
		wp_safe_redirect( wp_get_referer() ? wp_get_referer() : home_url( '/' ) );
		exit;
	}
}
