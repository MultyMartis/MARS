<?php
/**
 * Theme setup: supports, menus.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register theme features and menus.
 */
function shpigovsky_setup() {
	load_theme_textdomain( 'shpigovsky', SHPIGOVSKY_THEME_DIR . '/languages' );

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
			'primary' => __( 'Главное меню', 'shpigovsky' ),
			'footer'  => __( 'Нижнее меню', 'shpigovsky' ),
			'legal'   => __( 'Правовое меню', 'shpigovsky' ),
		)
	);
}
add_action( 'after_setup_theme', 'shpigovsky_setup' );
