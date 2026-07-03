<?php
/**
 * ACF integration — JSON paths and Pro dependency guard.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Fields;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

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
		return ModuleRegistry::is_enabled( self::id() ) && shpigovsky_core_acf_is_available();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_filter( 'acf/settings/load_json', array( __CLASS__, 'add_load_path' ) );
		add_filter( 'acf/settings/save_json', array( __CLASS__, 'set_save_path' ) );

		if ( is_admin() ) {
			add_action( 'admin_notices', array( __CLASS__, 'render_dependency_notices' ) );
		}
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

	/**
	 * Render bounded dependency notices.
	 */
	public static function render_dependency_notices() {
		if ( ! current_user_can( 'manage_options' ) ) {
			return;
		}

		if ( ! shpigovsky_core_acf_pro_is_active() ) {
			printf(
				'<div class="notice notice-error"><p><strong>Shpigovsky Core</strong> — %s</p></div>',
				esc_html__( 'ACF Pro is required for FP-0002 field groups. Source is safe, but runtime field registration is unavailable.', 'shpigovsky-core' )
			);
			return;
		}

		if ( shpigovsky_core_acf_extended_is_active() ) {
			printf(
				'<div class="notice notice-info"><p><strong>Shpigovsky Core</strong> — %s</p></div>',
				esc_html__( 'ACF Extended PRO is present but FP-0002 does not use ACFE APIs or ACFE-only field types.', 'shpigovsky-core' )
			);
		}
	}
}
