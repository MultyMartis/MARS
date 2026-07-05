<?php
/**
 * Admin options and deprecated field guards — V9-06D9-U.
 *
 * Registers top-level Reviews options page and suppresses deprecated Home
 * `home_reviews_teaser` local PHP field from shpigovsky-core without plugin edits.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register dedicated Reviews ACF options page.
 */
function shpigovsky_register_reviews_options_page() {
	if ( ! function_exists( 'acf_add_options_page' ) ) {
		return;
	}

	acf_add_options_page(
		array(
			'page_title'      => 'Отзывы',
			'menu_title'      => 'Отзывы',
			'menu_slug'       => 'fp02-reviews',
			'capability'      => 'manage_options',
			'position'        => 60,
			'redirect'        => false,
			'icon_url'        => 'dashicons-star-filled',
			'updated_message' => 'Отзывы обновлены.',
		)
	);
}
add_action( 'acf/init', 'shpigovsky_register_reviews_options_page', 15 );

/**
 * Hide deprecated Home reviews teaser field in admin.
 *
 * Field remains registered in shpigovsky-core PHP for compatibility; theme suppresses UI.
 *
 * @param array<string, mixed>|false $field Prepared field.
 * @return array<string, mixed>|false
 */
function shpigovsky_hide_deprecated_home_reviews_teaser_field( $field ) {
	if ( is_array( $field ) && ( $field['key'] ?? '' ) === 'field_fp02_home_reviews_teaser' ) {
		return false;
	}

	return $field;
}
add_filter( 'acf/prepare_field', 'shpigovsky_hide_deprecated_home_reviews_teaser_field' );

/**
 * Strip deprecated Home reviews teaser from save payload before core validation runs.
 */
function shpigovsky_strip_deprecated_home_reviews_teaser_on_save() {
	if ( empty( $_POST['acf'] ) || ! is_array( $_POST['acf'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Missing
		return;
	}

	if ( isset( $_POST['acf']['field_fp02_home_reviews_teaser'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Missing
		unset( $_POST['acf']['field_fp02_home_reviews_teaser'] ); // phpcs:ignore WordPress.Security.NonceVerification.Missing
	}
}
add_action( 'acf/validate_save_post', 'shpigovsky_strip_deprecated_home_reviews_teaser_on_save', 1 );
