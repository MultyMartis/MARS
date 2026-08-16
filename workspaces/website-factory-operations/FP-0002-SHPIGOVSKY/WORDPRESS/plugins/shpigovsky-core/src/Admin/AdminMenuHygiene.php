<?php
/**
 * Hide raw Options admin screens from normal production UX — PROD-P13.
 *
 * Owner of the "Options" menu: ACF Extended PRO (`acf-extended-pro`).
 * Does not uninstall ACFE and does not delete wp_options rows.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Targeted admin-menu hygiene.
 */
final class AdminMenuHygiene implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.menu-hygiene';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'acf/init', array( __CLASS__, 'disable_acfe_options_module' ), 5 );
		add_filter( 'acfe/modules/options/admin', '__return_false' );
		add_action( 'admin_menu', array( __CLASS__, 'remove_raw_options_screens' ), 9999 );
	}

	/**
	 * Turn off ACFE Options UI when the setting API exists.
	 */
	public static function disable_acfe_options_module() {
		if ( function_exists( 'acf_update_setting' ) ) {
			acf_update_setting( 'acfe/modules/options', false );
		}
	}

	/**
	 * Remove leftover Options menu entries without touching data.
	 */
	public static function remove_raw_options_screens() {
		$top_slugs = array(
			'options',
			'acf-options',
			'acfe-options',
			'acfe-manage-options',
			'wp-options',
			'all-options',
		);

		foreach ( $top_slugs as $slug ) {
			remove_menu_page( $slug );
		}

		$parents = array( 'tools.php', 'options-general.php', 'acf', 'acf-options', 'edit.php?post_type=acf-field-group' );
		$subs    = array( 'options', 'acf-options', 'acfe-options', 'acfe-manage-options', 'acfe-tools' );

		foreach ( $parents as $parent ) {
			foreach ( $subs as $sub ) {
				remove_submenu_page( $parent, $sub );
			}
		}

		global $menu, $submenu;
		if ( is_array( $menu ) ) {
			foreach ( $menu as $key => $item ) {
				$title = isset( $item[0] ) ? wp_strip_all_tags( (string) $item[0] ) : '';
				$slug  = isset( $item[2] ) ? (string) $item[2] : '';
				if ( self::is_raw_options_entry( $title, $slug ) ) {
					unset( $menu[ $key ] );
				}
			}
		}
		if ( is_array( $submenu ) ) {
			foreach ( $submenu as $parent => $items ) {
				foreach ( $items as $key => $item ) {
					$title = isset( $item[0] ) ? wp_strip_all_tags( (string) $item[0] ) : '';
					$slug  = isset( $item[2] ) ? (string) $item[2] : '';
					if ( self::is_raw_options_entry( $title, $slug ) ) {
						unset( $submenu[ $parent ][ $key ] );
					}
				}
			}
		}
	}

	/**
	 * Match the raw wp_options browser, not Site Settings.
	 *
	 * @param string $title Menu title.
	 * @param string $slug  Menu slug.
	 * @return bool
	 */
	private static function is_raw_options_entry( $title, $slug ) {
		$title_plain = trim( wp_strip_all_tags( (string) $title ) );
		$slug        = (string) $slug;

		if ( 0 === strpos( $slug, 'fp02-site-settings' ) ) {
			return false;
		}

		if ( preg_match( '/^options$/i', $title_plain ) ) {
			return true;
		}

		if ( preg_match( '/acfe[-_]?(manage[-_])?options/i', $slug ) ) {
			return true;
		}

		return false;
	}
}
