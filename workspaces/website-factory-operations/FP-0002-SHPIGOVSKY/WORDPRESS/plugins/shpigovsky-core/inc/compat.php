<?php
/**
 * Dependency guards and environment checks.
 *
 * @package Shpigovsky_Core
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether ACF Pro is available for field integration.
 *
 * V9-06C source uses only public ACF Pro APIs and must not depend on ACF Extended PRO.
 *
 * @return bool
 */
function shpigovsky_core_acf_pro_is_active() {
	return function_exists( 'acf' ) && defined( 'ACF_PRO' ) && ACF_PRO;
}

/**
 * Whether ACF runtime APIs exist without proving Pro capability.
 *
 * @return bool
 */
function shpigovsky_core_acf_is_available() {
	return function_exists( 'acf' );
}

/**
 * Whether ACF Extended PRO appears to be active.
 *
 * FP-0002 V9-06C records this only for non-invasive notices; it never calls ACFE APIs.
 *
 * @return bool
 */
function shpigovsky_core_acf_extended_is_active() {
	return defined( 'ACFE_VERSION' ) || class_exists( 'ACFE' );
}

/**
 * Whether the plugin is in skeleton mode (no model registration).
 *
 * @return bool
 */
function shpigovsky_core_is_skeleton_mode() {
	return defined( 'SHPIGOVSKY_CORE_SKELETON' ) && SHPIGOVSKY_CORE_SKELETON;
}
