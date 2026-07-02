<?php
/**
 * PSR-4 autoloader for Shpigovsky\Core namespace.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Loader;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Minimal class autoloader.
 */
final class Autoloader {

	/**
	 * Base directory for src/ classes.
	 *
	 * @var string
	 */
	private static $base_dir = '';

	/**
	 * Register autoloader.
	 *
	 * @param string $base_dir Absolute path to src directory.
	 */
	public static function register( $base_dir ) {
		self::$base_dir = rtrim( $base_dir, '/\\' ) . DIRECTORY_SEPARATOR;
		spl_autoload_register( array( __CLASS__, 'autoload' ) );
	}

	/**
	 * Autoload callback.
	 *
	 * @param string $class Fully qualified class name.
	 */
	private static function autoload( $class ) {
		$prefix = 'Shpigovsky\\Core\\';

		if ( 0 !== strpos( $class, $prefix ) ) {
			return;
		}

		$relative = substr( $class, strlen( $prefix ) );
		$file     = self::$base_dir . str_replace( '\\', DIRECTORY_SEPARATOR, $relative ) . '.php';

		if ( is_readable( $file ) ) {
			require_once $file;
		}
	}
}
