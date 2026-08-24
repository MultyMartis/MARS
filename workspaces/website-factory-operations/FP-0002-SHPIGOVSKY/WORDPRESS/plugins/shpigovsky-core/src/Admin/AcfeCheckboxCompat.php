<?php
/**
 * ACFE checkbox ↔ ACF Pro private-property compatibility.
 *
 * ACFE Pro 0.9.2.3 replaces checkbox render_field and writes $instance->_values /
 * $instance->_all_checked. ACF Pro 6.5+ made those properties private, which fatals
 * Admin metaboxes that use checkbox fields (e.g. generic_page_reusable_blocks).
 *
 * Bounded fix: when the private-property incompatibility is detected, restore ACF
 * core checkbox rendering. Project checkbox fields do not rely on ACFE toggle/custom.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use ReflectionProperty;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Restore ACF core checkbox Admin rendering when ACFE Pro is incompatible.
 */
final class AcfeCheckboxCompat implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.acfe-checkbox-compat';
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
		// After ACFE field extends register (ACF/ACFE boot on acf/init).
		add_action( 'acf/init', array( __CLASS__, 'maybe_restore_core_checkbox_render' ), 100 );
	}

	/**
	 * Detect ACFE/ACF private-property clash and restore core checkbox render.
	 */
	public static function maybe_restore_core_checkbox_render() {
		if ( ! function_exists( 'acf_get_field_type' ) ) {
			return;
		}

		if ( ! class_exists( 'acfe_pro_field_checkbox', false ) && ! class_exists( 'acfe_field_checkbox', false ) ) {
			// ACFE checkbox extender not present — nothing to repair.
			if ( ! defined( 'ACFE_VERSION' ) && ! defined( 'ACFE_PRO' ) ) {
				return;
			}
		}

		$field_type = acf_get_field_type( 'checkbox' );
		if ( ! is_object( $field_type ) ) {
			return;
		}

		if ( ! self::checkbox_private_values_incompatible( $field_type ) ) {
			return;
		}

		$hook = 'acf/render_field/type=checkbox';
		remove_all_actions( $hook );
		add_action( $hook, array( $field_type, 'render_field' ), 9, 1 );
	}

	/**
	 * Whether ACF checkbox stores _values as a private property (breaks ACFE Pro 0.9.2.3).
	 *
	 * @param object $field_type ACF checkbox field type instance.
	 * @return bool
	 */
	private static function checkbox_private_values_incompatible( $field_type ) {
		try {
			$property = new ReflectionProperty( $field_type, '_values' );
		} catch ( \ReflectionException $e ) {
			return false;
		}

		return $property->isPrivate();
	}
}
