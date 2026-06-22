<?php
/**
 * Register service custom post type.
 *
 * @package FWS_Synthetic_Core
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Service CPT registration.
 */
class FWS_Synthetic_CPT_Service {

	/**
	 * Hook registration.
	 */
	public static function init() {
		add_action( 'init', array( __CLASS__, 'register' ) );
	}

	/**
	 * Register CPT.
	 */
	public static function register() {
		$labels = array(
			'name'               => __( 'Услуги', 'fws-synthetic' ),
			'singular_name'      => __( 'Услуга', 'fws-synthetic' ),
			'menu_name'          => __( 'Услуги', 'fws-synthetic' ),
			'add_new'            => __( 'Добавить услугу', 'fws-synthetic' ),
			'add_new_item'       => __( 'Добавить услугу', 'fws-synthetic' ),
			'edit_item'          => __( 'Редактировать услугу', 'fws-synthetic' ),
			'new_item'           => __( 'Новая услуга', 'fws-synthetic' ),
			'view_item'          => __( 'Просмотр услуги', 'fws-synthetic' ),
			'search_items'       => __( 'Искать услуги', 'fws-synthetic' ),
			'not_found'          => __( 'Услуги не найдены', 'fws-synthetic' ),
			'not_found_in_trash' => __( 'В корзине услуг нет', 'fws-synthetic' ),
			'all_items'          => __( 'Все услуги', 'fws-synthetic' ),
		);

		register_post_type(
			'service',
			array(
				'labels'       => $labels,
				'public'       => true,
				'has_archive'  => true,
				'rewrite'      => array( 'slug' => 'services' ),
				'menu_icon'    => 'dashicons-hammer',
				'show_in_rest' => true,
				'supports'     => array( 'title', 'editor', 'excerpt', 'thumbnail' ),
			)
		);
	}
}
