<?php
/**
 * Deterministic REST response envelopes for WPilot.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Response {
	/**
	 * Build a standard success response.
	 *
	 * @param array $data Response data.
	 * @param array $meta Response metadata.
	 * @param int   $status HTTP status.
	 * @return WP_REST_Response
	 */
	public static function success( array $data = array(), array $meta = array(), $status = 200 ) {
		$response = new WP_REST_Response(
			array(
				'ok'   => true,
				'data' => $data,
				'meta' => $meta,
			),
			$status
		);

		return self::with_safe_headers( $response );
	}

	/**
	 * Build a standard error response.
	 *
	 * @param string $code Stable error code.
	 * @param string $message Operator-readable message.
	 * @param array  $meta Response metadata.
	 * @param int    $status HTTP status.
	 * @param array  $details Optional deterministic error details.
	 * @return WP_REST_Response
	 */
	public static function error( $code, $message, array $meta = array(), $status = 403, array $details = array() ) {
		$error = array_merge(
			array(
				'code'    => (string) $code,
				'message' => (string) $message,
			),
			$details
		);

		$response = new WP_REST_Response(
			array(
				'ok'    => false,
				'error' => $error,
				'meta'  => $meta,
			),
			$status
		);

		return self::with_safe_headers( $response );
	}

	/**
	 * Add deterministic no-cache JSON headers to plugin-owned responses.
	 *
	 * @param WP_REST_Response $response REST response.
	 * @return WP_REST_Response
	 */
	private static function with_safe_headers( WP_REST_Response $response ) {
		$response->header( 'Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0' );
		$response->header( 'Pragma', 'no-cache' );
		$response->header( 'Expires', '0' );
		$response->header( 'Content-Type', WPilot_Constants::CONTENT_TYPE_JSON );

		return $response;
	}
}
