<?php
/**
 * Option-backed plugin state for WPilot.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Settings {
	const OPTION_NAME = WPilot_Constants::OPTION_NAME;

	/**
	 * Default option state. Bridge and writes are disabled by default.
	 *
	 * @return array
	 */
	public static function defaults() {
		return array(
			'bridge_enabled'       => false,
			'write_enabled'        => false,
			'emergency_disabled'   => false,
			'token_hash'           => '',
			'token_created_at'     => '',
			'dev_confirmed'        => false,
			'plugin_version'       => WPILOT_VERSION,
			'schema_version'       => WPILOT_SCHEMA_VERSION,
			'token_revoked_at'     => '',
			'last_token_used_at'   => '',
			'last_safety_error'    => '',
			'allowed_post_types'   => array( 'page' ),
			'retention_days'       => 30,
			'backup_retention_max' => 10,
		);
	}

	/**
	 * Activation keeps the bridge disabled and preserves existing token state.
	 *
	 * @return void
	 */
	public static function activate() {
		$options = wp_parse_args( get_option( self::OPTION_NAME, array() ), self::defaults() );

		$options['bridge_enabled']     = false;
		$options['write_enabled']      = false;
		$options['emergency_disabled'] = false;
		$options['dev_confirmed']      = false;
		$options['plugin_version']     = WPILOT_VERSION;
		$options['schema_version']     = WPILOT_SCHEMA_VERSION;

		update_option( self::OPTION_NAME, self::sanitize_options( $options ), false );
	}

	/**
	 * Deactivation disables bridge operations while preserving plugin state.
	 *
	 * @return void
	 */
	public static function deactivate() {
		$options                   = self::get_options();
		$options['bridge_enabled'] = false;
		$options['write_enabled']  = false;

		update_option( self::OPTION_NAME, self::sanitize_options( $options ), false );
	}

	/**
	 * Get merged plugin options.
	 *
	 * @return array
	 */
	public static function get_options() {
		return wp_parse_args( get_option( self::OPTION_NAME, array() ), self::defaults() );
	}

	/**
	 * Persist selected plugin options.
	 *
	 * @param array $options Options to save.
	 * @param bool  $allow_write_enable Whether this call may enable dry-run write readiness.
	 * @return void
	 */
	public static function update_options( array $options, $allow_write_enable = false ) {
		$current = self::get_options();
		$merged  = wp_parse_args( $options, $current );

		update_option( self::OPTION_NAME, self::sanitize_options( $merged, $allow_write_enable, $current ), false );
	}

	/**
	 * Store a generated token hash and return the plaintext token once.
	 *
	 * @param array|null $options Optional state snapshot.
	 * @return string
	 */
	public static function generate_token() {
		$token   = WPilot_Constants::TOKEN_PREFIX . wp_generate_password( WPilot_Constants::TOKEN_LENGTH, false, false );
		$options = self::get_options();

		$options['token_hash']         = wp_hash_password( $token );
		$options['token_created_at']   = current_time( 'mysql', true );
		$options['token_revoked_at']   = '';
		$options['last_token_used_at'] = '';

		self::update_options( $options );

		return $token;
	}

	/**
	 * Revoke the active token without storing plaintext.
	 *
	 * @return void
	 */
	public static function revoke_token() {
		$options = self::get_options();

		$options['token_hash']       = '';
		$options['token_created_at'] = '';
		$options['token_revoked_at'] = current_time( 'mysql', true );

		self::update_options( $options );
	}

	/**
	 * Compute the current operator-facing plugin state.
	 *
	 * @return string
	 */
	public static function get_state( $options = null ) {
		$options = is_array( $options ) ? wp_parse_args( $options, self::defaults() ) : self::get_options();

		if ( ! empty( $options['emergency_disabled'] ) ) {
			return WPilot_Constants::STATE_EMERGENCY_DISABLED;
		}

		if ( empty( $options['bridge_enabled'] ) ) {
			return WPilot_Constants::STATE_DISABLED;
		}

		if ( empty( $options['dev_confirmed'] ) ) {
			return WPilot_Constants::STATE_ENABLED_WITHOUT_DEV_CONFIRMATION;
		}

		if ( ! empty( $options['token_hash'] ) ) {
			return WPilot_Constants::STATE_TOKEN_GENERATED;
		}

		return WPilot_Constants::STATE_ENABLED_DEV;
	}

	/**
	 * Normalize option values before persistence.
	 *
	 * @param array      $options Raw options.
	 * @param bool       $allow_write_enable Whether this call may enable dry-run write readiness.
	 * @param array|null $current_options Current persisted options before this update.
	 * @return array
	 */
	private static function sanitize_options( array $options, $allow_write_enable = false, $current_options = null ) {
		$defaults        = self::defaults();
		$options         = wp_parse_args( $options, $defaults );
		$current_options = is_array( $current_options ) ? wp_parse_args( $current_options, $defaults ) : $defaults;

		$bridge_enabled     = (bool) $options['bridge_enabled'];
		$dev_confirmed      = (bool) $options['dev_confirmed'];
		$emergency_disabled = (bool) $options['emergency_disabled'];
		$write_enabled      = ! empty( $options['write_enabled'] )
			&& $bridge_enabled
			&& $dev_confirmed
			&& ! $emergency_disabled;

		if ( ! $allow_write_enable && empty( $current_options['write_enabled'] ) && $write_enabled ) {
			$write_enabled = false;
		}

		return array(
			'bridge_enabled'       => $bridge_enabled,
			'write_enabled'        => $write_enabled,
			'emergency_disabled'   => $emergency_disabled,
			'token_hash'           => is_string( $options['token_hash'] ) ? $options['token_hash'] : '',
			'token_created_at'     => sanitize_text_field( $options['token_created_at'] ),
			'dev_confirmed'        => $dev_confirmed,
			'plugin_version'       => sanitize_text_field( $options['plugin_version'] ),
			'schema_version'       => sanitize_text_field( $options['schema_version'] ),
			'token_revoked_at'     => sanitize_text_field( $options['token_revoked_at'] ),
			'last_token_used_at'   => sanitize_text_field( $options['last_token_used_at'] ),
			'last_safety_error'    => sanitize_text_field( $options['last_safety_error'] ),
			'allowed_post_types'   => array( 'page' ),
			'retention_days'       => absint( $options['retention_days'] ),
			'backup_retention_max' => absint( $options['backup_retention_max'] ),
		);
	}
}
