<?php
/**
 * Module contract — register only when enabled.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Contracts;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Core module interface.
 */
interface ModuleInterface {

	/**
	 * Unique module identifier.
	 *
	 * @return string
	 */
	public static function id();

	/**
	 * Whether module hooks should register in the current phase.
	 *
	 * @return bool
	 */
	public static function is_enabled();

	/**
	 * Register WordPress hooks for this module.
	 */
	public static function register();
}
