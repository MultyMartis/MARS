<?php
/**
 * Request-scoped metadata extraction for WPilot.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Request_Context {
	/**
	 * Build request-scoped operational metadata.
	 *
	 * @param WP_REST_Request|null $request Optional REST request.
	 * @param string               $endpoint_name Endpoint name.
	 * @param string               $auth_state Auth state label.
	 * @return array
	 */
	public static function build( $request = null, $endpoint_name = '', $auth_state = 'not-required' ) {
		return array(
			'request_id'            => self::request_id(),
			'timestamp_utc'         => current_time( 'mysql', true ),
			'endpoint'              => sanitize_key( $endpoint_name ),
			'auth_state'            => sanitize_key( $auth_state ),
			'bridge_state_snapshot' => WPilot_Environment::snapshot(),
			'client_ip'             => self::client_ip(),
			'user_agent'            => self::user_agent( $request ),
		);
	}

	/**
	 * Build response metadata without echoing full client fingerprint fields.
	 *
	 * @param WP_REST_Request|null $request Optional REST request.
	 * @param string               $endpoint_name Endpoint name.
	 * @param string               $auth_state Auth state label.
	 * @return array
	 */
	public static function response_meta( $request = null, $endpoint_name = '', $auth_state = 'not-required' ) {
		$context = self::build( $request, $endpoint_name, $auth_state );

		return array(
			'request_id'            => $context['request_id'],
			'timestamp_utc'         => $context['timestamp_utc'],
			'endpoint'              => $context['endpoint'],
			'auth_state'            => $context['auth_state'],
			'bridge_state_snapshot' => $context['bridge_state_snapshot'],
		);
	}

	/**
	 * Generate a request ID without persistence.
	 *
	 * @return string
	 */
	private static function request_id() {
		if ( function_exists( 'wp_generate_uuid4' ) ) {
			return 'wpilot-' . wp_generate_uuid4();
		}

		return 'wpilot-' . wp_hash( microtime( true ) . wp_rand() );
	}

	/**
	 * Capture a conservative client IP when supplied by the web server.
	 *
	 * @return string
	 */
	private static function client_ip() {
		$remote_addr = isset( $_SERVER['REMOTE_ADDR'] ) ? wp_unslash( $_SERVER['REMOTE_ADDR'] ) : '';
		$remote_addr = is_string( $remote_addr ) ? trim( $remote_addr ) : '';

		return filter_var( $remote_addr, FILTER_VALIDATE_IP ) ? $remote_addr : '';
	}

	/**
	 * Capture a capped, sanitized user-agent string.
	 *
	 * @param WP_REST_Request|null $request Optional REST request.
	 * @return string
	 */
	private static function user_agent( $request ) {
		$user_agent = '';

		if ( $request instanceof WP_REST_Request ) {
			$user_agent = $request->get_header( 'user_agent' );
		}

		if ( '' === $user_agent && isset( $_SERVER['HTTP_USER_AGENT'] ) ) {
			$user_agent = wp_unslash( $_SERVER['HTTP_USER_AGENT'] );
		}

		if ( ! is_string( $user_agent ) ) {
			return '';
		}

		return substr( sanitize_text_field( $user_agent ), 0, 200 );
	}
}
