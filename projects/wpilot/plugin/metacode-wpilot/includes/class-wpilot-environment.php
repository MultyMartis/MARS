<?php
/**
 * Deterministic environment gates for WPilot.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Environment {
	/**
	 * Check whether the read-only bridge is enabled.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return bool
	 */
	public static function bridge_enabled( $options = null ) {
		$options = self::options( $options );

		return ! empty( $options['bridge_enabled'] );
	}

	/**
	 * Check whether the operator confirmed DEV/test use.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return bool
	 */
	public static function dev_confirmed( $options = null ) {
		$options = self::options( $options );

		return ! empty( $options['dev_confirmed'] );
	}

	/**
	 * Check whether the emergency stop is active.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return bool
	 */
	public static function emergency_disabled( $options = null ) {
		$options = self::options( $options );

		return ! empty( $options['emergency_disabled'] );
	}

	/**
	 * Check whether write readiness is disabled.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return bool
	 */
	public static function write_disabled( $options = null ) {
		$options = self::options( $options );

		return empty( $options['write_enabled'] );
	}

	/**
	 * Validate option state for operational routes.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return bool
	 */
	public static function environment_valid( $options = null ) {
		$options = self::options( $options );

		return is_array( $options )
			&& array_key_exists( 'bridge_enabled', $options )
			&& array_key_exists( 'dev_confirmed', $options )
			&& array_key_exists( 'emergency_disabled', $options )
			&& array_key_exists( 'write_enabled', $options );
	}

	/**
	 * Boolean readiness check for non-REST admin flows.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return bool
	 */
	public static function is_operationally_ready( $options = null ) {
		$options = self::options( $options );

		return self::environment_valid( $options )
			&& ! self::emergency_disabled( $options )
			&& self::bridge_enabled( $options )
			&& self::dev_confirmed( $options );
	}

	/**
	 * Check deterministic readiness for authenticated read-only endpoints.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @param array      $meta Response metadata.
	 * @return true|WP_REST_Response
	 */
	public static function operational_readiness( $options = null, array $meta = array() ) {
		$options = self::options( $options );

		if ( ! self::environment_valid( $options ) ) {
			return WPilot_Errors::safe_unknown( $meta );
		}

		if ( self::emergency_disabled( $options ) ) {
			return WPilot_Errors::emergency_disabled( $meta );
		}

		if ( ! self::bridge_enabled( $options ) ) {
			return WPilot_Errors::bridge_disabled( $meta );
		}

		if ( ! self::dev_confirmed( $options ) ) {
			return WPilot_Errors::dev_not_confirmed( $meta );
		}

		return true;
	}

	/**
	 * Build a request-scoped bridge state snapshot.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return array
	 */
	public static function snapshot( $options = null ) {
		$options = self::options( $options );

		return array(
			'state'              => WPilot_Settings::get_state( $options ),
			'bridge_enabled'     => self::bridge_enabled( $options ),
			'dev_confirmed'      => self::dev_confirmed( $options ),
			'emergency_disabled' => self::emergency_disabled( $options ),
			'write_enabled'      => ! self::write_disabled( $options ),
		);
	}

	/**
	 * Resolve an options snapshot.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return array
	 */
	private static function options( $options ) {
		return is_array( $options ) ? $options : WPilot_Settings::get_options();
	}
}
