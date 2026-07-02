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
 * Render breadcrumb region when not on the front page.
 *
 * V9-06B: inert placeholder partial only.
 */
function shpigovsky_render_breadcrumbs() {
	if ( is_front_page() ) {
		return;
	}

	get_template_part( 'template-parts/navigation/breadcrumbs' );
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
