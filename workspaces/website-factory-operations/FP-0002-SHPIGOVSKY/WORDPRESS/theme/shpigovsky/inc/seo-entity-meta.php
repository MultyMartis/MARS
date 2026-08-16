<?php
/**
 * Per-entity SEO title + meta description output — PROD-P13.
 *
 * Owner: FP-0002 theme. No Yoast/Rank Math present.
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
	if ( is_front_page() || is_home() || is_search() || is_404() || is_archive() ) {
		return $parts;
	}

	if ( ! is_singular( shpigovsky_seo_entity_post_types() ) ) {
		return $parts;
	}

	$title = shpigovsky_get_entity_seo_field( get_queried_object_id(), 'fp02_seo_title' );
	if ( '' === $title ) {
		return $parts;
	}

	$parts['title'] = $title;
	return $parts;
}
add_filter( 'document_title_parts', 'shpigovsky_entity_seo_title_parts', 15 );

/**
 * Output meta description when explicitly filled.
 */
function shpigovsky_entity_seo_meta_description() {
	if ( is_front_page() || is_home() || is_search() || is_404() || is_archive() ) {
		return;
	}

	if ( ! is_singular( shpigovsky_seo_entity_post_types() ) ) {
		return;
	}

	$description = shpigovsky_get_entity_seo_field( get_queried_object_id(), 'fp02_seo_description' );
	if ( '' === $description ) {
		return;
	}

	printf(
		'<meta name="description" content="%s" />' . "\n",
		esc_attr( wp_strip_all_tags( $description ) )
	);
}
add_action( 'wp_head', 'shpigovsky_entity_seo_meta_description', 3 );
