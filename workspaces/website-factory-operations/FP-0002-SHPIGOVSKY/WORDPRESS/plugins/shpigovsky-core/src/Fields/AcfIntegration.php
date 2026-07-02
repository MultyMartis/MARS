<?php
/**
 * ACF integration — JSON paths and Pro dependency guard.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * ACF JSON load/save and field integration boundary.
 */
final class AcfIntegration implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'fields.acf';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ! shpigovsky_core_is_skeleton_mode() && shpigovsky_core_acf_pro_is_active();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_filter( 'acf/settings/load_json', array( __CLASS__, 'add_load_path' ) );
		add_filter( 'acf/settings/save_json', array( __CLASS__, 'set_save_path' ) );
	}

	/**
	 * Resolve canonical ACF JSON directory.
	 *
	 * @return string
	 */
	public static function get_json_directory() {
		return trailingslashit( dirname( dirname( SHPIGOVSKY_CORE_DIR ) ) ) . 'acf-json';
	}

	/**
	 * Append project ACF JSON load path.
	 *
	 * @param array<int, string> $paths Existing paths.
	 * @return array<int, string>
	 */
	public static function add_load_path( $paths ) {
		$paths[] = self::get_json_directory();
		return $paths;
	}

	/**
	 * Set project ACF JSON save path.
	 *
	 * @param string $path Default save path.
	 * @return string
	 */
	public static function set_save_path( $path ) {
		return self::get_json_directory();
	}
}
