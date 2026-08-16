<?php
/**
 * Service CPT module — source implementation for V9-06C.
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
 * Service custom post type boundary.
 */
final class Service implements ModuleInterface {

	/**
	 * Post type slug.
	 */
	public const POST_TYPE = 'service';

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'content-types.service';
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
	}

	/**
	 * Register the service post type.
	 *
	 * Source authority:
	 * - FP-0002-WORDPRESS-ARCHITECTURE-v1.md
	 * - FP-0002-WORDPRESS-ENTITY-REGISTRY-v1.json
	 * - FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.md
	 *
	 * Runtime delivery remains separate; V9-06C.1 only enables source hook registration.
	 */
	public static function register_post_type() {
		register_post_type(
			self::POST_TYPE,
			array(
				'labels'              => self::get_labels(),
				'description'         => __( 'Иерархический каталог услуг FP-0002. Хаб /uslugi/ остается отдельной страницей.', 'shpigovsky-core' ),
				'public'              => true,
				'hierarchical'        => true,
				'exclude_from_search' => false,
				'publicly_queryable'  => true,
				'show_ui'             => true,
				'show_in_menu'        => true,
				'show_in_nav_menus'   => true,
				'show_in_rest'        => true,
				'query_var'           => self::POST_TYPE,
				'has_archive'         => false,
				'rewrite'             => array(
					'slug'         => 'uslugi',
					'with_front'   => false,
					'hierarchical' => true,
					'pages'        => true,
				),
				'supports'            => array( 'title', 'editor', 'excerpt', 'thumbnail', 'page-attributes', 'revisions' ),
				'menu_position'       => 21,
				'menu_icon'           => 'dashicons-heart',
			)
		);
	}

	/**
	 * Russian labels for the service CPT.
	 *
	 * @return array<string, string>
	 */
	public static function get_labels() {
		return array(
			'name'                  => __( 'Услуги', 'shpigovsky-core' ),
			'singular_name'         => __( 'Услуга', 'shpigovsky-core' ),
			'menu_name'             => __( 'Услуги', 'shpigovsky-core' ),
			'name_admin_bar'        => __( 'Услуга', 'shpigovsky-core' ),
			'add_new'               => __( 'Добавить услугу', 'shpigovsky-core' ),
			'add_new_item'          => __( 'Добавить услугу', 'shpigovsky-core' ),
			'new_item'              => __( 'Новая услуга', 'shpigovsky-core' ),
			'edit_item'             => __( 'Редактировать услугу', 'shpigovsky-core' ),
			'view_item'             => __( 'Посмотреть услугу', 'shpigovsky-core' ),
			'all_items'             => __( 'Все услуги', 'shpigovsky-core' ),
			'search_items'          => __( 'Искать услуги', 'shpigovsky-core' ),
			'parent_item_colon'     => __( 'Родительская услуга:', 'shpigovsky-core' ),
			'not_found'             => __( 'Услуги не найдены.', 'shpigovsky-core' ),
			'not_found_in_trash'    => __( 'В корзине услуги не найдены.', 'shpigovsky-core' ),
			'featured_image'        => __( 'Изображение услуги', 'shpigovsky-core' ),
			'set_featured_image'    => __( 'Задать изображение услуги', 'shpigovsky-core' ),
			'remove_featured_image' => __( 'Удалить изображение услуги', 'shpigovsky-core' ),
			'use_featured_image'    => __( 'Использовать как изображение услуги', 'shpigovsky-core' ),
			'archives'              => __( 'Архив услуг отключен', 'shpigovsky-core' ),
		);
	}
}
