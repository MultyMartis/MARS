<?php
/**
 * Site settings module — options page fields deferred.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Settings;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Global site settings boundary.
 */
final class SiteSettings implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'settings.site';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() ) && shpigovsky_core_acf_pro_is_active();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_filter( 'pre_update_option', array( __CLASS__, 'prevent_secret_like_options' ), 10, 3 );
	}

	/**
	 * Secret-like field name fragments forbidden in FP-0002 options source.
	 *
	 * @return array<int, string>
	 */
	public static function get_forbidden_option_patterns() {
		return array( 'password', 'passwd', 'secret', 'token', 'api_key', 'apikey', 'license', 'smtp' );
	}

	/**
	 * Guard against accidental secret-like option mutations after delivery activation.
	 *
	 * @param mixed  $value New value.
	 * @param string $option Option name.
	 * @param mixed  $old_value Old value.
	 * @return mixed
	 */
	public static function prevent_secret_like_options( $value, $option, $old_value ) {
		if ( in_array( (string) $option, \Shpigovsky\Core\Mail\MailOps::allowlisted_option_names(), true ) ) {
			return $value;
		}

		foreach ( self::get_forbidden_option_patterns() as $pattern ) {
			if ( false !== stripos( (string) $option, $pattern ) ) {
				return $old_value;
			}
		}

		return $value;
	}
}
