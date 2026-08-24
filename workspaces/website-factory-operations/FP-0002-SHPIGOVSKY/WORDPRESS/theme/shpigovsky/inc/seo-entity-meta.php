<?php
/**
 * Per-entity SEO title + meta description output — PROD-P13.
 *
 * Owner: FP-0002 theme. No Yoast/Rank Math present.
 *
 * Context resolution covers singular entities, static front page, and posts page.
 *
 * Fallbacks:
 * - Empty SEO Title → WordPress title-tag (object title + site name).
 * - Empty Meta Description → omit the tag (do not invent marketing copy).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Public singles that own SEO fields.
 *
 * @return array<int, string>
 */
function shpigovsky_seo_entity_post_types() {
	return array( 'page', 'post', 'service', 'specialist' );
}

/**
 * Resolve the post ID that owns SEO fields for the current request.
 *
 * @return int
 */
function shpigovsky_seo_get_context_post_id() {
	if ( is_singular( shpigovsky_seo_entity_post_types() ) ) {
		return (int) get_queried_object_id();
	}

	if ( is_front_page() ) {
		$page_on_front = (int) get_option( 'page_on_front' );

		return $page_on_front > 0 ? $page_on_front : 0;
	}

	if ( is_home() ) {
		$page_for_posts = (int) get_option( 'page_for_posts' );

		return $page_for_posts > 0 ? $page_for_posts : 0;
	}

	return 0;
}

/**
 * Whether entity SEO title/description should emit for this request.
 *
 * @return bool
 */
function shpigovsky_seo_should_emit_entity_meta() {
	if ( is_search() || is_404() ) {
		return false;
	}

	if ( function_exists( 'shpigovsky_seo_owns_pagination_meta' ) && shpigovsky_seo_owns_pagination_meta() ) {
		return false;
	}

	if ( function_exists( 'shpigovsky_seo_is_search_results' ) && shpigovsky_seo_is_search_results() ) {
		return false;
	}

	return shpigovsky_seo_get_context_post_id() > 0;
}

/**
 * Read entity SEO field.
 *
 * @param int    $post_id Post ID.
 * @param string $name    Field name.
 * @return string
 */
function shpigovsky_get_entity_seo_field( $post_id, $name ) {
	$post_id = (int) $post_id;
	if ( $post_id <= 0 ) {
		return '';
	}

	if ( function_exists( 'get_field' ) ) {
		$value = get_field( $name, $post_id );
		if ( is_string( $value ) && '' !== trim( $value ) ) {
			return trim( $value );
		}
	}

	$meta = get_post_meta( $post_id, $name, true );

	return is_string( $meta ) ? trim( $meta ) : '';
}

/**
 * Replace document title when a custom SEO title is set.
 *
 * @param array<string, string> $parts Title parts.
 * @return array<string, string>
 */
function shpigovsky_entity_seo_title_parts( $parts ) {
	if ( ! shpigovsky_seo_should_emit_entity_meta() ) {
		return $parts;
	}

	$post_id = shpigovsky_seo_get_context_post_id();
	$title   = shpigovsky_get_entity_seo_field( $post_id, 'fp02_seo_title' );

	if ( '' === $title ) {
		return $parts;
	}

	$parts['title'] = $title;
	unset( $parts['site'], $parts['tagline'] );

	return $parts;
}
add_filter( 'document_title_parts', 'shpigovsky_entity_seo_title_parts', 15 );

/**
 * Output meta description when explicitly filled.
 */
function shpigovsky_entity_seo_meta_description() {
	if ( ! shpigovsky_seo_should_emit_entity_meta() ) {
		return;
	}

	$post_id     = shpigovsky_seo_get_context_post_id();
	$description = shpigovsky_get_entity_seo_field( $post_id, 'fp02_seo_description' );

	if ( '' === $description ) {
		return;
	}

	printf(
		'<meta name="description" content="%s" />' . "\n",
		esc_attr( wp_strip_all_tags( $description ) )
	);
}
add_action( 'wp_head', 'shpigovsky_entity_seo_meta_description', 3 );
