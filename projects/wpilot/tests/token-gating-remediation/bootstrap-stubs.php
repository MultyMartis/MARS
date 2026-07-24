<?php
/**
 * Minimal WordPress-function stubs for bounded WPilot token-gating tests.
 *
 * Not a WordPress runtime. No network. No Localhost site boot.
 *
 * @package MetaCode_WPilot_Tests
 */

if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/stub-abspath/' );
}

// Loaded after class-wpilot-constants.php in the runner; placeholders if needed early.
if ( ! defined( 'WPILOT_VERSION' ) ) {
	define( 'WPILOT_VERSION', '0.3.0' );
}
if ( ! defined( 'WPILOT_SCHEMA_VERSION' ) ) {
	define( 'WPILOT_SCHEMA_VERSION', '0.2.0' );
}

if ( ! class_exists( 'WP_REST_Response' ) ) {
	/**
	 * Minimal stand-in for WordPress REST response object.
	 */
	class WP_REST_Response {
		/**
		 * @var mixed
		 */
		public $data;

		/**
		 * @var int
		 */
		public $status;

		/**
		 * @var array
		 */
		public $headers = array();

		/**
		 * @param mixed $data   Response data.
		 * @param int   $status HTTP status.
		 */
		public function __construct( $data = null, $status = 200 ) {
			$this->data   = $data;
			$this->status = (int) $status;
		}

		/**
		 * @param string $key   Header name.
		 * @param string $value Header value.
		 * @return void
		 */
		public function header( $key, $value ) {
			$this->headers[ $key ] = $value;
		}
	}
}

if ( ! class_exists( 'WPilot_Schema' ) ) {
	/**
	 * No-op schema stub for activation tests.
	 */
	class WPilot_Schema {
		/**
		 * @return void
		 */
		public static function install_or_upgrade() {}

		/**
		 * @return bool
		 */
		public static function is_valid() {
			return true;
		}
	}
}

$GLOBALS['wpilot_test_options'] = array();
$GLOBALS['wpilot_test_current_user_can'] = true;
$GLOBALS['wpilot_test_update_log'] = array();
$GLOBALS['wpilot_test_password_calls'] = array();
$GLOBALS['wpilot_test_external_calls'] = array();

if ( ! function_exists( 'wp_parse_args' ) ) {
	function wp_parse_args( $args, $defaults = array() ) {
		if ( is_object( $args ) ) {
			$args = get_object_vars( $args );
		}
		if ( ! is_array( $args ) ) {
			$args = array();
		}
		if ( ! is_array( $defaults ) ) {
			$defaults = array();
		}
		return array_merge( $defaults, $args );
	}
}

if ( ! function_exists( 'get_option' ) ) {
	function get_option( $name, $default = false ) {
		if ( isset( $GLOBALS['wpilot_test_options'][ $name ] ) ) {
			return $GLOBALS['wpilot_test_options'][ $name ];
		}
		return $default;
	}
}

if ( ! function_exists( 'update_option' ) ) {
	function update_option( $name, $value, $autoload = null ) {
		$GLOBALS['wpilot_test_options'][ $name ] = $value;
		$GLOBALS['wpilot_test_update_log'][] = array(
			'name'  => $name,
			'value' => $value,
		);
		return true;
	}
}

if ( ! function_exists( 'current_user_can' ) ) {
	function current_user_can( $capability ) {
		return ! empty( $GLOBALS['wpilot_test_current_user_can'] );
	}
}

if ( ! function_exists( 'current_time' ) ) {
	function current_time( $type, $gmt = 0 ) {
		return '2026-07-24 03:00:00';
	}
}

if ( ! function_exists( 'wp_generate_password' ) ) {
	function wp_generate_password( $length = 12, $special_chars = true, $extra_special_chars = false ) {
		$GLOBALS['wpilot_test_password_calls'][] = $length;
		return str_repeat( 'a', (int) $length );
	}
}

if ( ! function_exists( 'wp_hash_password' ) ) {
	function wp_hash_password( $password ) {
		return 'hash:' . substr( hash( 'sha256', (string) $password ), 0, 16 );
	}
}

if ( ! function_exists( 'sanitize_text_field' ) ) {
	function sanitize_text_field( $str ) {
		return is_string( $str ) ? trim( strip_tags( $str ) ) : '';
	}
}

if ( ! function_exists( 'absint' ) ) {
	function absint( $value ) {
		return abs( (int) $value );
	}
}

/**
 * Reset in-memory option store between cases.
 *
 * @param array $options Option snapshot.
 * @return void
 */
function wpilot_test_reset_options( array $options = array() ) {
	$GLOBALS['wpilot_test_options'] = array(
		'wpilot_options' => $options,
	);
	$GLOBALS['wpilot_test_update_log'] = array();
	$GLOBALS['wpilot_test_password_calls'] = array();
	$GLOBALS['wpilot_test_external_calls'] = array();
	$GLOBALS['wpilot_test_current_user_can'] = true;
}
