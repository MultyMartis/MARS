<?php
/**
 * Theme template helpers — skeleton stubs for V9 integration.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether the current request is the designated blog posts page.
 *
 * @return bool
 */
function shpigovsky_is_blog_posts_page() {
	return is_home() && ! is_front_page();
}

/**
 * Whether breadcrumbs are enabled for the current template context.
 *
 * Pages include the blog posts page, contacts, reviews, and institutional pages.
 * Service CPT screens are controlled separately.
 *
 * @return bool
 */
function shpigovsky_breadcrumbs_enabled_for_context() {
	if ( is_front_page() ) {
		return false;
	}

	$field_name = is_singular( 'service' ) ? 'show_breadcrumbs_services' : 'show_breadcrumbs_pages';

	if ( ! function_exists( 'get_field' ) ) {
		return true;
	}

	$value = get_field( $field_name, 'option' );

	if ( null === $value || '' === $value ) {
		return true;
	}

	return (bool) $value;
}

/**
 * Build a small default breadcrumb trail for page-like screens.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_default_breadcrumb_trail() {
	$title = '';

	if ( shpigovsky_is_blog_posts_page() && function_exists( 'shpigovsky_get_blog_breadcrumb_trail' ) ) {
		return shpigovsky_get_blog_breadcrumb_trail();
	}

	if ( is_singular() ) {
		$title = get_the_title( get_queried_object_id() );
	} elseif ( is_archive() ) {
		$title = get_the_archive_title();
	}

	$title = trim( wp_strip_all_tags( (string) $title ) );

	if ( '' === $title ) {
		return array();
	}

	return array(
		array(
			'label' => __( 'Главная', 'shpigovsky' ),
			'url'   => home_url( '/' ),
		),
		array(
			'label' => $title,
			'url'   => '',
		),
	);
}

/**
 * Whether the current screen should keep an empty breadcrumb shell (no invented crumbs).
 *
 * Contacts / Reviews keep the HTML block for operator layout parity even when the trail is empty.
 *
 * @return bool
 */
function shpigovsky_breadcrumbs_allow_empty_shell() {
	if ( is_page_template( 'page-templates/contacts.php' ) || is_page_template( 'page-templates/reviews.php' ) ) {
		return true;
	}

	$slug = is_singular() ? (string) get_post_field( 'post_name', get_queried_object_id() ) : '';

	return in_array( $slug, array( 'kontakty', 'otzyvy' ), true );
}

/**
 * Whether breadcrumbs should use the shared `.internal-page-nav > .container` shell.
 *
 * Contacts / Reviews / Blog archive / Blog single / Service stacks already provide
 * their own wrappers — do not nest another container there.
 *
 * @return bool
 */
function shpigovsky_breadcrumbs_should_use_internal_wrap() {
	if ( is_page_template( 'page-templates/contacts.php' ) || is_page_template( 'page-templates/reviews.php' ) ) {
		return false;
	}

	if ( shpigovsky_is_blog_posts_page() || is_singular( 'post' ) ) {
		return false;
	}

	if ( is_singular( 'service' ) ) {
		return false;
	}

	return true;
}

/**
 * Render breadcrumb region when not on the front page.
 *
 * V9-06E61: no wrapper is emitted when disabled.
 * Contacts/Reviews may render an empty structural shell without inventing labels.
 * V9-06E62A: Generic / Specialist / Legal / default page family wrap crumbs in
 * `.internal-page-nav > .container` without changing breadcrumb markup/CSS.
 *
 * @param array $args {
 *     Optional. @type string $wrap auto|internal|none
 * }
 */
function shpigovsky_render_breadcrumbs( $args = array() ) {
	$args = wp_parse_args(
		$args,
		array(
			'wrap' => 'auto',
		)
	);

	if ( ! shpigovsky_breadcrumbs_enabled_for_context() ) {
		return;
	}

	$trail = get_query_var( 'shpigovsky_breadcrumb_trail', array() );

	if ( empty( $trail ) && ! shpigovsky_breadcrumbs_allow_empty_shell() ) {
		$trail = shpigovsky_get_default_breadcrumb_trail();
	}

	if ( empty( $trail ) && ! shpigovsky_breadcrumbs_allow_empty_shell() ) {
		return;
	}

	set_query_var( 'shpigovsky_breadcrumb_trail', is_array( $trail ) ? $trail : array() );
	set_query_var( 'shpigovsky_breadcrumbs_allow_empty', shpigovsky_breadcrumbs_allow_empty_shell() );

	$wrap = (string) $args['wrap'];
	if ( 'auto' === $wrap ) {
		$wrap = shpigovsky_breadcrumbs_should_use_internal_wrap() ? 'internal' : 'none';
	}

	if ( 'internal' === $wrap ) {
		echo '<div class="internal-page-nav"><div class="container">';
	}

	get_template_part( 'template-parts/navigation/breadcrumbs' );

	if ( 'internal' === $wrap ) {
		echo '</div></div>';
	}
}

/**
 * Render internal page navigation band when applicable.
 *
 * V9-06B: hook point only — no dynamic menu graph yet.
 */
function shpigovsky_render_internal_page_nav() {
	get_template_part( 'template-parts/components/internal-page-nav' );
}

/**
 * Render placeholder notice for unpublished or stub content.
 *
 * @param string $context Optional context slug for future styling.
 */
function shpigovsky_render_placeholder_notice( $context = 'default' ) {
	set_query_var( 'shpigovsky_placeholder_context', $context );
	get_template_part( 'template-parts/page/placeholder-notice' );
}
