<?php
/**
 * Specialist CPT module — PROD-P11 dedicated entity.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\ContentTypes;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Specialist custom post type boundary.
 *
 * Public URLs remain under /specyalisty/{slug}/.
 * Hub page /specyalisty/ stays a native Page (has_archive = false).
 */
final class Specialist implements ModuleInterface {

	/**
	 * Post type slug.
	 */
	public const POST_TYPE = 'specialist';

	/**
	 * Public rewrite base (matches existing hub page slug).
	 */
	public const REWRITE_SLUG = 'specyalisty';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'content-types.specialist';
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
		add_action( 'init', array( __CLASS__, 'register_post_type' ), 10 );
		add_action( 'init', array( __CLASS__, 'maybe_flush_rewrites_once' ), 99 );
		add_filter( 'manage_' . self::POST_TYPE . '_posts_columns', array( __CLASS__, 'filter_columns' ) );
		add_action( 'manage_' . self::POST_TYPE . '_posts_custom_column', array( __CLASS__, 'render_column' ), 10, 2 );
		add_filter( 'manage_edit-' . self::POST_TYPE . '_sortable_columns', array( __CLASS__, 'sortable_columns' ) );
	}

	/**
	 * Register the specialist post type.
	 */
	public static function register_post_type() {
		register_post_type(
			self::POST_TYPE,
			array(
				'labels'              => self::get_labels(),
				'description'         => __( 'Специалисты FP-0002. Хаб /specyalisty/ остаётся отдельной страницей.', 'shpigovsky-core' ),
				'public'              => true,
				'hierarchical'        => false,
				'exclude_from_search' => false,
				'publicly_queryable'  => true,
				'show_ui'             => true,
				'show_in_menu'        => true,
				'show_in_nav_menus'   => true,
				'show_in_rest'        => false,
				'query_var'           => self::POST_TYPE,
				'has_archive'         => false,
				'rewrite'             => array(
					'slug'       => self::REWRITE_SLUG,
					'with_front' => false,
					'pages'      => true,
					'feeds'      => false,
				),
				'supports'            => array( 'title', 'thumbnail', 'page-attributes' ),
				'menu_position'       => 22,
				'menu_icon'           => 'dashicons-groups',
				'capability_type'     => 'post',
				'map_meta_cap'        => true,
			)
		);
	}

	/**
	 * One-time rewrite flush after CPT registration (PROD-P11).
	 * Does not flush on every request.
	 */
	public static function maybe_flush_rewrites_once() {
		$flag = 'fp02_specialist_cpt_rewrite_flushed_p11';
		if ( get_option( $flag ) ) {
			return;
		}
		flush_rewrite_rules( false );
		update_option( $flag, '1', false );
	}

	/**
	 * Russian admin labels.
	 *
	 * @return array<string, string>
	 */
	public static function get_labels() {
		return array(
			'name'                  => __( 'Специалисты', 'shpigovsky-core' ),
			'singular_name'         => __( 'Специалист', 'shpigovsky-core' ),
			'menu_name'             => __( 'Специалисты', 'shpigovsky-core' ),
			'name_admin_bar'        => __( 'Специалист', 'shpigovsky-core' ),
			'add_new'               => __( 'Добавить нового', 'shpigovsky-core' ),
			'add_new_item'          => __( 'Добавить специалиста', 'shpigovsky-core' ),
			'new_item'              => __( 'Новый специалист', 'shpigovsky-core' ),
			'edit_item'             => __( 'Редактировать специалиста', 'shpigovsky-core' ),
			'view_item'             => __( 'Посмотреть специалиста', 'shpigovsky-core' ),
			'all_items'             => __( 'Все специалисты', 'shpigovsky-core' ),
			'search_items'          => __( 'Искать специалистов', 'shpigovsky-core' ),
			'not_found'             => __( 'Специалисты не найдены.', 'shpigovsky-core' ),
			'not_found_in_trash'    => __( 'В корзине специалисты не найдены.', 'shpigovsky-core' ),
			'featured_image'        => __( 'Фото', 'shpigovsky-core' ),
			'set_featured_image'    => __( 'Задать фото', 'shpigovsky-core' ),
			'remove_featured_image' => __( 'Удалить фото', 'shpigovsky-core' ),
			'use_featured_image'    => __( 'Использовать как фото', 'shpigovsky-core' ),
			'archives'              => __( 'Архив специалистов отключён', 'shpigovsky-core' ),
		);
	}

	/**
	 * Admin list columns.
	 *
	 * @param array<string, string> $columns Columns.
	 * @return array<string, string>
	 */
	public static function filter_columns( $columns ) {
		$new = array();
		foreach ( (array) $columns as $key => $label ) {
			if ( 'title' === $key ) {
				$new['fp02_specialist_photo'] = __( 'Фото', 'shpigovsky-core' );
				$new['title']                 = __( 'Имя / название', 'shpigovsky-core' );
				$new['fp02_specialist_role']  = __( 'Должность / профессия', 'shpigovsky-core' );
				$new['fp02_menu_order']       = __( 'Порядок', 'shpigovsky-core' );
				continue;
			}
			$new[ $key ] = $label;
		}
		return $new;
	}

	/**
	 * Render custom columns.
	 *
	 * @param string $column Column key.
	 * @param int    $post_id Post ID.
	 */
	public static function render_column( $column, $post_id ) {
		$post_id = (int) $post_id;

		if ( 'fp02_specialist_photo' === $column ) {
			$thumb = get_the_post_thumbnail( $post_id, array( 48, 48 ), array( 'style' => 'width:48px;height:48px;object-fit:cover;border-radius:4px;' ) );
			echo $thumb ? $thumb : '&mdash;'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
			return;
		}

		if ( 'fp02_specialist_role' === $column ) {
			$role = '';
			if ( function_exists( 'get_field' ) ) {
				$raw = get_field( 'specialist_role', $post_id );
				$role = is_string( $raw ) ? trim( $raw ) : '';
			}
			if ( '' === $role ) {
				$role = trim( (string) get_post_meta( $post_id, '_shpigovsky_specialist_role', true ) );
			}
			echo esc_html( '' !== $role ? $role : '—' );
			return;
		}

		if ( 'fp02_menu_order' === $column ) {
			$post = get_post( $post_id );
			echo esc_html( $post instanceof \WP_Post ? (string) (int) $post->menu_order : '—' );
		}
	}

	/**
	 * Sortable columns.
	 *
	 * @param array<string, string> $columns Columns.
	 * @return array<string, string>
	 */
	public static function sortable_columns( $columns ) {
		$columns['fp02_menu_order'] = 'menu_order';
		return $columns;
	}
}
