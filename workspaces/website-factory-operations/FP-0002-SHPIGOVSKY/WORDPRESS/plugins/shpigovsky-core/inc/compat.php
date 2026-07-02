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
 * V9-06B: guard only — ACF Pro not required until V9-06C.
 *
 * @return bool
 */
function shpigovsky_core_acf_pro_is_active() {
	return function_exists( 'acf' ) && defined( 'ACF_PRO' ) && ACF_PRO;
}

/**
 * Whether the plugin is in skeleton mode (no model registration).
 *
 * @return bool
 */
function shpigovsky_core_is_skeleton_mode() {
	return defined( 'SHPIGOVSKY_CORE_SKELETON' ) && SHPIGOVSKY_CORE_SKELETON;
}
