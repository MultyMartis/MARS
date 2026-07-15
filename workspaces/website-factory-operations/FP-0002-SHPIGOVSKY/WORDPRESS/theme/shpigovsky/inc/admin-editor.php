<?php
/**
 * Admin editor UX — hide native content editor on template-managed pages (V9-06D9-N)
 * and on service CPT screens (V9-06E46-FIX04).
 *
 * Editing for these pages is via ACF metaboxes and theme templates; the Classic Editor
 * content box is empty after D9-M cleanup and confuses operators.
 *
 * Service CPT: post_content is not the admin content model (optional leftover fallback
 * for leaf intro only). Values are preserved; editor UI is hidden for all service screens.
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
		11, // О центре hub.
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
 * Resolve post ID on post edit admin screens.
 *
 * @return int
 */
function shpigovsky_admin_edit_page_id() {
	if ( isset( $_GET['post'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		return (int) $_GET['post']; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
	}

	global $post;

	if ( $post && isset( $post->ID ) ) {
		return (int) $post->ID;
	}

	return 0;
}

/**
 * Whether current admin edit screen is the service CPT.
 *
 * @return bool
 */
function shpigovsky_admin_is_service_edit_screen() {
	if ( ! is_admin() ) {
		return false;
	}

	$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;

	if ( $screen && isset( $screen->post_type ) && 'service' === $screen->post_type ) {
		return true;
	}

	$post_id = shpigovsky_admin_edit_page_id();

	if ( $post_id > 0 ) {
		$post = get_post( $post_id );
		return $post && 'service' === $post->post_type;
	}

	if ( isset( $_GET['post_type'] ) && 'service' === $_GET['post_type'] ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		return true;
	}

	return false;
}

/**
 * Remove editor support early on allowlisted page edit screens and all service CPT screens.
 */
function shpigovsky_maybe_remove_page_editor_support() {
	if ( ! is_admin() ) {
		return;
	}

	if ( shpigovsky_admin_is_service_edit_screen() ) {
		remove_post_type_support( 'service', 'editor' );
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
 * Remove native content editor metabox on allowlisted pages and service CPT.
 */
function shpigovsky_hide_native_editor_metabox() {
	if ( ! is_admin() ) {
		return;
	}

	$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;

	if ( ! $screen || 'post' !== $screen->base ) {
		return;
	}

	if ( 'service' === $screen->post_type ) {
		remove_meta_box( 'postdivrich', 'service', 'normal' );
		return;
	}

	if ( 'page' !== $screen->post_type ) {
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

	$hide = shpigovsky_admin_is_service_edit_screen()
		|| shpigovsky_should_hide_native_editor( shpigovsky_admin_edit_page_id() );

	if ( ! $hide ) {
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
add_action( 'admin_head-post-new.php', 'shpigovsky_hide_native_editor_admin_css' );

/**
 * Whether the current admin screen should load FP-0002 ACF admin CSS.
 *
 * V9-06E41 — front page; V9-06E43 — Services hub; V9-06E44 — service CPT;
 * V9-06E53 — all page + service edit screens + FP02 Site Settings options pages
 * so thematic blocks and generic-page ACF share the same visual layer.
 *
 * @param string $hook_suffix Current admin hook suffix.
 * @return bool
 */
function shpigovsky_admin_should_enqueue_fp02_acf_css( $hook_suffix ) {
	if ( in_array( $hook_suffix, array( 'post.php', 'post-new.php' ), true ) ) {
		$screen = function_exists( 'get_current_screen' ) ? get_current_screen() : null;
		$post_type = ( $screen && isset( $screen->post_type ) ) ? (string) $screen->post_type : '';

		if ( in_array( $post_type, array( 'page', 'service' ), true ) ) {
			return true;
		}
	}

	// ACF options pages under FP02 Site Settings (slug contains fp02-site-settings).
	if ( is_string( $hook_suffix ) && false !== strpos( $hook_suffix, 'fp02-site-settings' ) ) {
		return true;
	}

	return false;
}

/**
 * Body class for scoped FP-0002 ACF admin visual rules (V9-06E53).
 *
 * @param string $classes Space-separated body classes.
 * @return string
 */
function shpigovsky_fp02_acf_admin_body_class( $classes ) {
	$hook = isset( $GLOBALS['hook_suffix'] ) ? (string) $GLOBALS['hook_suffix'] : '';

	if ( ! shpigovsky_admin_should_enqueue_fp02_acf_css( $hook ) ) {
		return $classes;
	}

	$classes .= ' fp02-acf-admin';

	return $classes;
}
add_filter( 'admin_body_class', 'shpigovsky_fp02_acf_admin_body_class' );

/**
 * Enqueue unified FP02 ACF admin CSS.
 * V9-06E41–E45 — section titles, notices, layout help/hide.
 * V9-06E53 — thematic block separation; no noisy internal field dividers.
 */
function shpigovsky_enqueue_home_acf_admin_css( $hook_suffix ) {
	if ( ! shpigovsky_admin_should_enqueue_fp02_acf_css( $hook_suffix ) ) {
		return;
	}

	$rel = 'assets/css/admin-fp02-acf.css';

	if ( ! is_readable( SHPIGOVSKY_THEME_DIR . '/' . $rel ) ) {
		// Fallback for older runtime copies that only have the alias file.
		$rel = 'assets/css/admin-home-acf.css';
		if ( ! is_readable( SHPIGOVSKY_THEME_DIR . '/' . $rel ) ) {
			return;
		}
	}

	wp_enqueue_style(
		'shpigovsky-fp02-acf-admin',
		SHPIGOVSKY_THEME_URI . '/' . $rel,
		array(),
		shpigovsky_asset_version( $rel )
	);

	// Legacy handle alias (E41–E45): same stylesheet URL, no second network fetch.
	wp_register_style(
		'shpigovsky-home-acf-admin',
		false,
		array( 'shpigovsky-fp02-acf-admin' ),
		shpigovsky_asset_version( $rel )
	);
	wp_enqueue_style( 'shpigovsky-home-acf-admin' );
}
add_action( 'admin_enqueue_scripts', 'shpigovsky_enqueue_home_acf_admin_css' );
