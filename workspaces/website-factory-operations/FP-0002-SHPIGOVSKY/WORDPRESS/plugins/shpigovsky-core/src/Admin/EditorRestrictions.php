<?php
/**
 * Editor restrictions — hide block editor where architecture requires classic/bounded fields.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Editor UX restrictions boundary.
 */
final class EditorRestrictions implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.editor-restrictions';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ! shpigovsky_core_is_skeleton_mode();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_filter( 'use_block_editor_for_post_type', array( __CLASS__, 'filter_block_editor' ), 10, 2 );
	}

	/**
	 * Disable block editor for bounded post types when authorized.
	 *
	 * @param bool   $use Whether to use block editor.
	 * @param string $post_type Post type slug.
	 * @return bool
	 */
	public static function filter_block_editor( $use, $post_type ) {
		if ( 'service' === $post_type ) {
			return false;
		}

		return $use;
	}
}
