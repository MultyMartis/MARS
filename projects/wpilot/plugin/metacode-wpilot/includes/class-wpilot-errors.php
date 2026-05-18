<?php
/**
 * Central refusal and error helpers for WPilot.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Errors {
	const AUTH_MISSING          = 'AUTH_MISSING';
	const AUTH_INVALID          = 'AUTH_INVALID';
	const TOKEN_REVOKED         = 'TOKEN_REVOKED';
	const BRIDGE_DISABLED       = 'BRIDGE_DISABLED';
	const EMERGENCY_DISABLED    = 'EMERGENCY_DISABLED';
	const DEV_NOT_CONFIRMED     = 'DEV_NOT_CONFIRMED';
	const SAFE_UNKNOWN          = 'SAFE_UNKNOWN';
	const INVALID_REQUEST       = 'INVALID_REQUEST';
	const UNSUPPORTED_OPERATION = 'UNSUPPORTED_OPERATION';
	const TARGET_NOT_FOUND      = 'TARGET_NOT_FOUND';

	/**
	 * Authentication token is absent from the documented header.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function auth_missing( array $meta = array() ) {
		return self::build( self::AUTH_MISSING, 'Authentication token is required.', $meta, 401 );
	}

	/**
	 * Authentication token did not validate.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function auth_invalid( array $meta = array() ) {
		return self::build( self::AUTH_INVALID, 'Authentication token is invalid.', $meta, 401 );
	}

	/**
	 * Token is absent or has been revoked.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function token_revoked( array $meta = array() ) {
		return self::build( self::TOKEN_REVOKED, 'Authentication token has been revoked or has not been generated.', $meta, 401 );
	}

	/**
	 * Bridge is disabled by operator state.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function bridge_disabled( array $meta = array() ) {
		return self::build( self::BRIDGE_DISABLED, 'Bridge is disabled. Enable it in plugin settings before using this endpoint.', $meta, 403 );
	}

	/**
	 * Emergency stop is active.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function emergency_disabled( array $meta = array() ) {
		return self::build( self::EMERGENCY_DISABLED, 'Bridge is emergency-disabled and requires administrator intervention.', $meta, 403 );
	}

	/**
	 * DEV/test confirmation is missing.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function dev_not_confirmed( array $meta = array() ) {
		return self::build( self::DEV_NOT_CONFIRMED, 'DEV/test use has not been explicitly confirmed.', $meta, 403 );
	}

	/**
	 * Environment state cannot be safely treated as ready.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function safe_unknown( array $meta = array() ) {
		return self::build( self::SAFE_UNKNOWN, 'Environment state is not safe to interpret for this operation.', $meta, 403 );
	}

	/**
	 * Request data is invalid.
	 *
	 * @param string $message Operator-readable message.
	 * @param array  $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function invalid_request( $message = 'Request is invalid.', array $meta = array() ) {
		return self::build( self::INVALID_REQUEST, $message, $meta, 400 );
	}

	/**
	 * Operation is not implemented in this read-only phase.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function unsupported_operation( array $meta = array() ) {
		return self::build( self::UNSUPPORTED_OPERATION, 'Operation is unsupported in this read-only MVP.', $meta, 405 );
	}

	/**
	 * Requested target was not found or is outside the read-only allowlist.
	 *
	 * @param array $meta Response metadata.
	 * @return WP_REST_Response
	 */
	public static function target_not_found( array $meta = array() ) {
		return self::build( self::TARGET_NOT_FOUND, 'Target page or post was not found.', $meta, 404 );
	}

	/**
	 * Build the deterministic error envelope.
	 *
	 * @param string $code Stable error code.
	 * @param string $message Operator-readable message.
	 * @param array  $meta Response metadata.
	 * @param int    $status HTTP status.
	 * @return WP_REST_Response
	 */
	private static function build( $code, $message, array $meta, $status ) {
		return WPilot_Response::error( $code, $message, $meta, $status );
	}
}
