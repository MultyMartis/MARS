<?php
/**
 * Admin editor UX — hide native content editor on template-managed pages (V9-06D9-N).
 *
 * Editing for these pages is via ACF metaboxes and theme templates; the Classic Editor
 * content box is empty after D9-M cleanup and confuses operators.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Page IDs where the native post_content editor is hidden in wp-admin.
 *
 * Source: D9-M cleaned template-managed pages plus Home/Services/Contacts.
 * Excludes operator-review pages (IDs 3, 6–10, 17, 19, 21, 25).
 * Legal pages #22–24 use native post_content after V9-06E1 static copy seed.
 *
 * @return int[]
 */
function shpigovsky_get_hide_native_editor_page_ids() {
	return array(
		4,  // Home (front page).
		5,  // Services hub.
		11, // О центре.
		12, // О нас.
		13, // Программа лечения.
		14, // Галерея о доме.
		15, // Специалистам.
		16, // Родственникам.
		18, // Отзывы.
		20, // Контакты.
	);
}

/**
 * Whether the native editor should be hidden for a page ID.
 *
 * @param int $page_id Page ID.
 * @return bool
 */
function shpigovsky_should_hide_native_editor( $page_id ) {
	$page_id = (int) $page_id;

	if ( $page_id <= 0 ) {
		return false;
	}

	return in_array( $page_id, shpigovsky_get_hide_native_editor_page_ids(), true );
}

/**
 * Resolve page ID on page edit admin screens.
 *
 * @return int
 */
function shpigovsky_admin_edit_page_id() {
	if ( isset( $_GET['post'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		return (int) $_GET['post']; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
	}

	global $post;

	if ( $post && 'page' === $post->post_type ) {
		return (int) $post->ID;
	}

	return 0;
}

/**
 * Remove editor support early on allowlisted page edit screens.
 */
function shpigovsky_maybe_remove_page_editor_support() {
	if ( ! is_admin() ) {
		return;
	}

	$page_id = shpigovsky_admin_edit_page_id();

	if ( ! shpigovsky_should_hide_native_editor( $page_id ) ) {
		return;
	}

	remove_post_type_support( 'page', 'editor' );
}
add_action( 'admin_init', 'shpigovsky_maybe_remove_page_editor_support' );

/**
 * Remove native content editor metabox on allowlisted pages.
 */
function shpigovsky_hide_native_editor_metabox() {
	if ( ! is_admin() ) {
		return;
	}

	$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;

	if ( ! $screen || 'post' !== $screen->base || 'page' !== $screen->post_type ) {
		return;
	}

	global $post;

	if ( ! $post || ! shpigovsky_should_hide_native_editor( (int) $post->ID ) ) {
		return;
	}

	remove_meta_box( 'postdivrich', 'page', 'normal' );
}
add_action( 'add_meta_boxes', 'shpigovsky_hide_native_editor_metabox', 99 );

/**
 * CSS fallback if a plugin re-registers the editor metabox after removal.
 */
function shpigovsky_hide_native_editor_admin_css() {
	if ( ! is_admin() ) {
		return;
	}

	$page_id = shpigovsky_admin_edit_page_id();

	if ( ! shpigovsky_should_hide_native_editor( $page_id ) ) {
		return;
	}

	echo '<style id="shpigovsky-hide-native-editor">
		#postdivrich,
		#wp-content-editor-container,
		#wp-content-wrap,
		.edit-form-editor { display: none !important; }
	</style>';
}
add_action( 'admin_head-post.php', 'shpigovsky_hide_native_editor_admin_css' );
