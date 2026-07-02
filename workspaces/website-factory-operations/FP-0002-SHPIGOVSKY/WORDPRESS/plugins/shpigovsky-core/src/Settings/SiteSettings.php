<?php
/**
 * Site settings module — options page fields deferred.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Settings;

use Shpigovsky\Core\Contracts\ModuleInterface;

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
		return ! shpigovsky_core_is_skeleton_mode() && shpigovsky_core_acf_pro_is_active();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		// V9-06C: register option-backed fields.
	}
}
