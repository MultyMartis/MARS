<?php
/**
 * Operation ID generation for WPilot runtime runs.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Operation_Id {
	/**
	 * Generate a new operation ID in the op_<uuid> format.
	 *
	 * @return string
	 */
	public static function generate() {
		if ( function_exists( 'wp_generate_uuid4' ) ) {
			return 'op_' . wp_generate_uuid4();
		}

		return 'op_' . wp_hash( microtime( true ) . wp_rand() );
	}
}
