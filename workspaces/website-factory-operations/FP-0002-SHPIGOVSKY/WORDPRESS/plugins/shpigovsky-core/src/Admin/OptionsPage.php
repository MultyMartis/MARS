<?php
/**
 * ACF options page registration — deferred to V9-06C.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Admin options pages boundary.
 */
final class OptionsPage implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.options-page';
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
		add_action( 'acf/init', array( __CLASS__, 'register_options_pages' ) );
	}

	/**
	 * Register ACF options pages.
	 */
	public static function register_options_pages() {
		if ( ! function_exists( 'acf_add_options_page' ) ) {
			return;
		}

		acf_add_options_page(
			array(
				'page_title'      => __( 'Настройки сайта', 'shpigovsky-core' ),
				'menu_title'      => __( 'Настройки сайта', 'shpigovsky-core' ),
				'menu_slug'       => 'fp02-site-settings',
				'capability'      => 'manage_options',
				'position'        => 59,
				'redirect'        => false,
				'icon_url'        => 'dashicons-admin-generic',
				'updated_message' => __( 'Настройки сайта обновлены.', 'shpigovsky-core' ),
			)
		);
	}
}
