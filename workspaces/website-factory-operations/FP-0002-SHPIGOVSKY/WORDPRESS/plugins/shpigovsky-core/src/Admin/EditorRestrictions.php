<?php
/**
 * Editor restrictions — hide block editor where architecture requires classic/bounded fields.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\ContentTypes\Service;
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
		add_action( 'add_meta_boxes', array( __CLASS__, 'remove_irrelevant_metaboxes' ), 20 );
		add_filter( 'manage_' . Service::POST_TYPE . '_posts_columns', array( __CLASS__, 'filter_service_columns' ) );
		add_action( 'manage_' . Service::POST_TYPE . '_posts_custom_column', array( __CLASS__, 'render_service_column' ), 10, 2 );
		add_action( 'admin_notices', array( __CLASS__, 'render_legal_blocker_notice' ) );
	}

	/**
	 * Disable block editor for bounded post types when authorized.
	 *
	 * @param bool   $use Whether to use block editor.
	 * @param string $post_type Post type slug.
	 * @return bool
	 */
	public static function filter_block_editor( $use, $post_type ) {
		if ( Service::POST_TYPE === $post_type ) {
			return false;
		}

		return $use;
	}

	/**
	 * Remove irrelevant metaboxes for service editors after delivery activation.
	 */
	public static function remove_irrelevant_metaboxes() {
		remove_meta_box( 'commentsdiv', Service::POST_TYPE, 'normal' );
		remove_meta_box( 'commentstatusdiv', Service::POST_TYPE, 'normal' );
		remove_meta_box( 'trackbacksdiv', Service::POST_TYPE, 'normal' );
		remove_meta_box( 'postcustom', Service::POST_TYPE, 'normal' );
	}

	/**
	 * Add bounded service admin columns.
	 *
	 * @param array<string,string> $columns Columns.
	 * @return array<string,string>
	 */
	public static function filter_service_columns( $columns ) {
		$columns['fp02_service_layout'] = __( 'Макет', 'shpigovsky-core' );
		$columns['fp02_placeholder']    = __( 'Статус', 'shpigovsky-core' );

		return $columns;
	}

	/**
	 * Render service admin column values.
	 *
	 * @param string $column Column key.
	 * @param int    $post_id Post ID.
	 */
	public static function render_service_column( $column, $post_id ) {
		if ( 'fp02_service_layout' === $column ) {
			$layout = function_exists( 'get_field' ) ? get_field( 'service_layout_variant', $post_id ) : '';
			echo esc_html( $layout ? $layout : '—' );
			return;
		}

		if ( 'fp02_placeholder' === $column ) {
			$layout = function_exists( 'get_field' ) ? get_field( 'service_layout_variant', $post_id ) : '';
			echo esc_html( 'placeholder' === $layout ? __( 'Заглушка', 'shpigovsky-core' ) : __( 'Контент', 'shpigovsky-core' ) );
		}
	}

	/**
	 * Legal demo blocker notice.
	 */
	public static function render_legal_blocker_notice() {
		$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;

		if ( ! $screen || 'page' !== $screen->post_type || ! current_user_can( 'edit_pages' ) ) {
			return;
		}

		$post_id = isset( $_GET['post'] ) ? (int) $_GET['post'] : 0;

		if ( ! $post_id || ! function_exists( 'get_field' ) ) {
			return;
		}

		if ( get_field( 'legal_production_blocker', $post_id ) ) {
			printf(
				'<div class="notice notice-warning"><p><strong>FP-0002 Legal</strong> — %s</p></div>',
				esc_html__( 'Эта legal-страница помечена как DEMO / production blocker. Снять можно только после операторской проверки текста.', 'shpigovsky-core' )
			);
		}
	}
}
