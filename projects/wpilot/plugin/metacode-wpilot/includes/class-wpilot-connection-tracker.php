<?php
/**
 * Persistent MARS connection status for operator diagnostics.
 *
 * Stores only safe metadata — no tokens, headers, payloads, or secrets.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Connection_Tracker {
	const STATUS_NEVER   = 'never';
	const STATUS_SUCCESS = 'success';
	const STATUS_FAILED  = 'failed';

	const KEY_STATUS              = 'last_connection_status';
	const KEY_SUCCESS_AT          = 'last_connection_success_at';
	const KEY_AUTHORIZED_AT       = 'last_authorized_connection_at';
	const KEY_AUTHORIZED_ENDPOINT = 'last_authorized_endpoint';
	const KEY_FAILURE_AT          = 'last_connection_failure_at';
	const KEY_FAILURE_REASON      = 'last_connection_failure_reason';

	/**
	 * Safe auth failure codes allowed in persisted diagnostics.
	 *
	 * @var array<int, string>
	 */
	private static $allowed_failure_reasons = array(
		WPilot_Errors::AUTH_MISSING,
		WPilot_Errors::AUTH_INVALID,
		WPilot_Errors::TOKEN_REVOKED,
	);

	/**
	 * Record a successful authenticated REST request.
	 *
	 * Success metadata is independent from failure metadata — a later auth
	 * refusal must not erase the last authorized connection snapshot.
	 *
	 * @param string $endpoint Compact REST path label (e.g. site-info, plugins).
	 * @return void
	 */
	public static function record_success( $endpoint = '' ) {
		$options = WPilot_Settings::get_options();
		$now     = current_time( 'mysql', true );

		$options[ self::KEY_STATUS ]        = self::STATUS_SUCCESS;
		$options[ self::KEY_SUCCESS_AT ]     = $now;
		$options[ self::KEY_AUTHORIZED_AT ]  = $now;
		$options[ self::KEY_AUTHORIZED_ENDPOINT ] = self::sanitize_endpoint_label( $endpoint );

		WPilot_Settings::update_options( $options );
	}

	/**
	 * Record an authentication failure with a safe error code.
	 *
	 * @param string $reason_code Stable auth error code.
	 * @return void
	 */
	public static function record_auth_failure( $reason_code ) {
		if ( ! self::is_allowed_failure_reason( $reason_code ) ) {
			return;
		}

		$options = WPilot_Settings::get_options();

		$options[ self::KEY_FAILURE_AT ]     = current_time( 'mysql', true );
		$options[ self::KEY_FAILURE_REASON ] = sanitize_key( $reason_code );

		WPilot_Settings::update_options( $options );
	}

	/**
	 * Operator-facing connection snapshot for admin UI.
	 *
	 * @return array<string, string>
	 */
	public static function get_snapshot() {
		$options = WPilot_Settings::get_options();

		$authorized_at = isset( $options[ self::KEY_AUTHORIZED_AT ] ) ? (string) $options[ self::KEY_AUTHORIZED_AT ] : '';
		$success_at    = isset( $options[ self::KEY_SUCCESS_AT ] ) ? (string) $options[ self::KEY_SUCCESS_AT ] : '';

		if ( '' === $authorized_at && '' !== $success_at ) {
			$authorized_at = $success_at;
		}

		$failure_at     = isset( $options[ self::KEY_FAILURE_AT ] ) ? (string) $options[ self::KEY_FAILURE_AT ] : '';
		$failure_reason = isset( $options[ self::KEY_FAILURE_REASON ] ) ? (string) $options[ self::KEY_FAILURE_REASON ] : '';
		$status         = self::derive_status( $authorized_at, $failure_at );

		return array(
			'status'              => $status,
			'success_at'          => $success_at,
			'authorized_at'       => $authorized_at,
			'authorized_endpoint' => isset( $options[ self::KEY_AUTHORIZED_ENDPOINT ] ) ? (string) $options[ self::KEY_AUTHORIZED_ENDPOINT ] : '',
			'failure_at'          => $failure_at,
			'failure_reason'      => $failure_reason,
		);
	}

	/**
	 * Derive operator-facing status without letting a later failure erase success.
	 *
	 * @param string $authorized_at Last authorized connection timestamp (UTC).
	 * @param string $failure_at Last auth failure timestamp (UTC).
	 * @return string
	 */
	private static function derive_status( $authorized_at, $failure_at ) {
		if ( '' !== $authorized_at ) {
			return self::STATUS_SUCCESS;
		}

		if ( '' !== $failure_at ) {
			return self::STATUS_FAILED;
		}

		return self::STATUS_NEVER;
	}

	/**
	 * Sanitize a compact endpoint label for persistence.
	 *
	 * @param string $endpoint Raw endpoint label.
	 * @return string
	 */
	public static function sanitize_endpoint_label( $endpoint ) {
		$endpoint = strtolower( trim( (string) $endpoint ) );
		$endpoint = preg_replace( '/[^a-z0-9\/\-]/', '', $endpoint );

		return substr( $endpoint, 0, 64 );
	}

	/**
	 * Whether a failure reason may be persisted.
	 *
	 * @param string $reason_code Candidate error code.
	 * @return bool
	 */
	public static function is_allowed_failure_reason( $reason_code ) {
		return in_array( $reason_code, self::$allowed_failure_reasons, true );
	}
}
