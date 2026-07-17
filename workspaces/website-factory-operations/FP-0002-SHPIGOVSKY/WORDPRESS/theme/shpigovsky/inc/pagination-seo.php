<?php
/**
 * Blog + Reviews pagination SEO — V9-06E62B.
 *
 * Theme owns self-canonicals when no dedicated SEO plugin is active.
 * Does not emit obsolete rel=prev/rel=next.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Whether current request is a Blog posts archive (including paged).
 *
 * @return bool
 */
function shpigovsky_seo_is_blog_archive() {
	return is_home() && ! is_front_page();
}

/**
 * Whether current request is the Reviews page template archive.
 *
 * @return bool
 */
function shpigovsky_seo_is_reviews_archive() {
	return is_page_template( 'page-templates/reviews.php' );
}

/**
 * Whether theme should own pagination SEO for this request.
 *
 * @return bool
 */
function shpigovsky_seo_owns_pagination_meta() {
	if ( defined( 'WPSEO_VERSION' ) || defined( 'RANK_MATH_VERSION' ) || defined( 'AIOSEO_VERSION' ) ) {
		return false;
	}

	return shpigovsky_seo_is_blog_archive() || shpigovsky_seo_is_reviews_archive();
}

/**
 * Current paged number (1-based).
 *
 * @return int
 */
function shpigovsky_seo_current_paged() {
	$paged = (int) get_query_var( 'paged' );

	if ( $paged < 1 ) {
		$paged = (int) get_query_var( 'page' );
	}

	return max( 1, $paged );
}

/**
 * Absolute self-canonical URL for Blog or Reviews archive pages.
 *
 * @return string Empty when not applicable.
 */
function shpigovsky_seo_self_canonical_url() {
	$paged = shpigovsky_seo_current_paged();

	if ( shpigovsky_seo_is_blog_archive() ) {
		$page_id = (int) get_option( 'page_for_posts' );
		$base    = $page_id > 0 ? get_permalink( $page_id ) : home_url( '/blog/' );

		if ( ! is_string( $base ) || '' === $base ) {
			$base = home_url( '/blog/' );
		}

		$base = trailingslashit( $base );

		if ( $paged > 1 ) {
			return $base . user_trailingslashit( 'page/' . $paged, 'single' );
		}

		return $base;
	}

	if ( shpigovsky_seo_is_reviews_archive() ) {
		$page_id = function_exists( 'shpigovsky_get_reviews_archive_page_id' )
			? shpigovsky_get_reviews_archive_page_id()
			: 0;
		$base    = $page_id > 0 ? get_permalink( $page_id ) : home_url( '/otzyvy/' );

		if ( ! is_string( $base ) || '' === $base ) {
			$base = home_url( '/otzyvy/' );
		}

		$base = trailingslashit( $base );

		if ( $paged > 1 ) {
			return $base . user_trailingslashit( 'page/' . $paged, 'single' );
		}

		return $base;
	}

	return '';
}

/**
 * Remove core rel_canonical on Blog/Reviews so theme emits a single tag.
 *
 * @return void
 */
function shpigovsky_seo_remove_core_canonical() {
	if ( ! shpigovsky_seo_owns_pagination_meta() ) {
		return;
	}

	remove_action( 'wp_head', 'rel_canonical' );
}
add_action( 'wp', 'shpigovsky_seo_remove_core_canonical', 20 );

/**
 * Output one self-referencing canonical link.
 *
 * @return void
 */
function shpigovsky_seo_output_canonical() {
	if ( ! shpigovsky_seo_owns_pagination_meta() ) {
		return;
	}

	$url = shpigovsky_seo_self_canonical_url();

	if ( '' === $url ) {
		return;
	}

	echo '<link rel="canonical" href="' . esc_url( $url ) . '" />' . "\n";
}
add_action( 'wp_head', 'shpigovsky_seo_output_canonical', 1 );

/**
 * Distinguish paginated archive document titles (page 2+).
 *
 * Blog posts page: WordPress core already injects a page marker — do not duplicate.
 * Reviews page template: core does not — add «Страница N».
 *
 * @param array<string, string> $parts Title parts.
 * @return array<string, string>
 */
function shpigovsky_seo_document_title_parts( $parts ) {
	if ( ! shpigovsky_seo_owns_pagination_meta() ) {
		return $parts;
	}

	$paged = shpigovsky_seo_current_paged();

	if ( $paged < 2 ) {
		return $parts;
	}

	if ( shpigovsky_seo_is_blog_archive() ) {
		return $parts;
	}

	if ( ! shpigovsky_seo_is_reviews_archive() ) {
		return $parts;
	}

	$parts['page'] = sprintf(
		/* translators: %d: page number */
		__( 'Страница %d', 'shpigovsky' ),
		$paged
	);

	return $parts;
}
add_filter( 'document_title_parts', 'shpigovsky_seo_document_title_parts', 20 );
