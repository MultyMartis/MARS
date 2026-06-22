<?php
/**
 * Theme setup: supports, menus, image sizes.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register theme features and menus.
 */
function fws_synthetic_setup() {
	load_theme_textdomain( 'fws-synthetic', FWS_SYNTHETIC_DIR . '/languages' );

	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support(
		'html5',
		array(
			'search-form',
			'comment-form',
			'comment-list',
			'gallery',
			'caption',
			'style',
			'script',
		)
	);

	register_nav_menus(
		array(
			'primary' => __( 'Главное меню', 'fws-synthetic' ),
			'footer'  => __( 'Нижнее меню', 'fws-synthetic' ),
		)
	);

	add_image_size( 'fws-service-card', 400, 300, true );
}
add_action( 'after_setup_theme', 'fws_synthetic_setup' );
