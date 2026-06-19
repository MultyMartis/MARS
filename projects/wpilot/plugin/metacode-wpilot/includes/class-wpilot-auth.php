<?php
/**
 * Header token authentication for WPilot REST endpoints.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Auth {
	const HEADER_NAME = WPilot_Constants::TOKEN_HEADER_NAME;

	/**
	 * Validate current bridge state and token for read-only endpoints.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return true|WP_REST_Response
	 */
	public static function require_read_access( WP_REST_Request $request ) {
		$options = WPilot_Settings::get_options();
		$meta    = WPilot_Request_Context::response_meta( $request, self::endpoint_name( $request ), 'checking' );

		$readiness = WPilot_Environment::operational_readiness( $options, $meta );
		if ( true !== $readiness ) {
			return $readiness;
		}

		if ( empty( $options['token_hash'] ) ) {
			return WPilot_Errors::token_revoked( $meta );
		}

		$token = self::get_request_token( $request );

		if ( '' === $token ) {
			return WPilot_Errors::auth_missing( $meta );
		}

		if ( ! wp_check_password( $token, $options['token_hash'] ) ) {
			return WPilot_Errors::auth_invalid( $meta );
		}

		$options['last_token_used_at'] = current_time( 'mysql', true );
		WPilot_Settings::update_options( $options );

		return true;
	}

	/**
	 * Validate dry-run access without updating token metadata or other options.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return true|WP_REST_Response
	 */
	public static function require_dry_run_access( WP_REST_Request $request ) {
		$options = WPilot_Settings::get_options();
		$meta    = WPilot_Request_Context::response_meta( $request, self::endpoint_name( $request ), 'checking' );

		$readiness = WPilot_Environment::operational_readiness( $options, $meta );
		if ( true !== $readiness ) {
			return $readiness;
		}

		if ( empty( $options['token_hash'] ) ) {
			return WPilot_Errors::token_revoked( $meta );
		}

		$token = self::get_request_token( $request );

		if ( '' === $token ) {
			return WPilot_Errors::auth_missing( $meta );
		}

		if ( ! wp_check_password( $token, $options['token_hash'] ) ) {
			return WPilot_Errors::auth_invalid( $meta );
		}

		if ( empty( $options['write_enabled'] ) ) {
			return WPilot_Response::error(
				'WRITE_DISABLED',
				'Dry-run replacement is gated by write readiness. Enable write mode in DEV before using this endpoint.',
				$meta,
				403,
				array(
					'stage'              => 'state',
					'mutation_performed' => false,
					'rollback_available' => false,
				)
			);
		}

		return true;
	}

	/**
	 * Validate backup-create access: bridge, DEV, token, and schema.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return true|WP_REST_Response
	 */
	public static function require_backup_access( WP_REST_Request $request ) {
		$options = WPilot_Settings::get_options();
		$meta    = WPilot_Request_Context::response_meta( $request, self::endpoint_name( $request ), 'checking' );

		$readiness = WPilot_Environment::operational_readiness( $options, $meta );
		if ( true !== $readiness ) {
			return $readiness;
		}

		if ( ! WPilot_Schema::is_valid() ) {
			return WPilot_Response::error(
				'INVALID_CONFIG',
				'Plugin storage schema is not ready.',
				$meta,
				503,
				array(
					'stage'              => 'storage',
					'mutation_performed' => false,
					'rollback_available' => false,
				)
			);
		}

		if ( empty( $options['token_hash'] ) ) {
			return WPilot_Errors::token_revoked( $meta );
		}

		$token = self::get_request_token( $request );

		if ( '' === $token ) {
			return WPilot_Errors::auth_missing( $meta );
		}

		if ( ! wp_check_password( $token, $options['token_hash'] ) ) {
			return WPilot_Errors::auth_invalid( $meta );
		}

		$options['last_token_used_at'] = current_time( 'mysql', true );
		WPilot_Settings::update_options( $options );

		return true;
	}

	/**
	 * Validate rollback access: backup access plus write readiness.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return true|WP_REST_Response
	 */
	public static function require_rollback_access( WP_REST_Request $request ) {
		$guard = self::require_backup_access( $request );
		if ( true !== $guard ) {
			return $guard;
		}

		$options = WPilot_Settings::get_options();
		$meta    = WPilot_Request_Context::response_meta( $request, self::endpoint_name( $request ), 'checking' );

		if ( empty( $options['write_enabled'] ) ) {
			return WPilot_Response::error(
				'WRITE_DISABLED',
				'Rollback is gated by write readiness. Enable write mode in DEV before using this endpoint.',
				$meta,
				403,
				array(
					'stage'              => 'state',
					'mutation_performed' => false,
					'rollback_available' => true,
				)
			);
		}

		return true;
	}

	/**
	 * Validate scoped-replace access: rollback access plus approval gate in handler.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return true|WP_REST_Response
	 */
	public static function require_scoped_replace_access( WP_REST_Request $request ) {
		return self::require_rollback_access( $request );
	}

	/**
	 * Extract token from the documented header.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return string
	 */
	public static function get_request_token( WP_REST_Request $request ) {
		$token = $request->get_header( self::HEADER_NAME );

		if ( empty( $token ) ) {
			$token = $request->get_header( WPilot_Constants::TOKEN_HEADER_FALLBACK );
		}

		return is_string( $token ) ? trim( $token ) : '';
	}

	/**
	 * Derive a compact endpoint name for request metadata.
	 *
	 * @param WP_REST_Request $request REST request.
	 * @return string
	 */
	private static function endpoint_name( WP_REST_Request $request ) {
		$route = trim( (string) $request->get_route(), '/' );
		$route = str_replace( '/', '-', $route );

		return $route;
	}
}
