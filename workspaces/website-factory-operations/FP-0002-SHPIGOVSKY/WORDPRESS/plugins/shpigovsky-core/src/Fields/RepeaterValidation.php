<?php
/**
 * Repeater validation — server-side bounded repeater enforcement.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Repeater max-item validation boundary.
 */
final class RepeaterValidation implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'fields.repeater-validation';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ! shpigovsky_core_is_skeleton_mode() && shpigovsky_core_acf_pro_is_active();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'acf/validate_save_post', array( __CLASS__, 'validate_repeaters' ) );
	}

	/**
	 * Validate repeater field bounds on save.
	 *
	 * V9-06B: contract stub — implementation in V9-06C+.
	 */
	public static function validate_repeaters() {
		// V9-06C implementation per FP-0002-FIELD-OWNERSHIP-MATRIX-v1.json.
	}
}
