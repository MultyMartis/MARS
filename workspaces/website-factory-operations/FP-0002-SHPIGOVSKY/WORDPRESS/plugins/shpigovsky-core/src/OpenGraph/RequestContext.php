<?php
/**
 * Request-scoped context for Open Graph (mirrors schema URL / post resolution).
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\OpenGraph;

use Shpigovsky\Core\StructuredData\EntityIds;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Normalized current-request reads for OG output.
 */
final class RequestContext {

	/**
	 * Whether OG should emit for the current request.
	 *
	 * @return bool
	 */
	public static function should_emit() {
		if ( is_admin() || is_feed() || is_robots() || is_trackback() ) {
			return false;
		}

		if ( is_search() || is_404() ) {
			return false;
		}

		return true;
	}

	/**
	 * Post ID that owns SEO fields for this request (theme helper when available).
	 *
	 * @return int
	 */
	public static function context_post_id() {
		if ( function_exists( 'shpigovsky_seo_get_context_post_id' ) ) {
			return (int) shpigovsky_seo_get_context_post_id();
		}

		if ( is_singular() ) {
			return (int) get_queried_object_id();
		}

		if ( is_front_page() ) {
			return (int) get_option( 'page_on_front' );
		}

		if ( function_exists( 'shpigovsky_is_blog_posts_page' ) && shpigovsky_is_blog_posts_page() ) {
			return (int) get_option( 'page_for_posts' );
		}

		return 0;
	}

	/**
	 * Canonical absolute page URL (same rules as Schema.org GraphBuilder).
	 *
	 * @return string
	 */
	public static function current_page_url() {
		if ( is_front_page() ) {
			return self::absolute_https_url( EntityIds::base_url() );
		}

		if ( is_singular() ) {
			$url = get_permalink( get_queried_object_id() );
			if ( is_string( $url ) && '' !== $url ) {
				return self::absolute_https_url( untrailingslashit( $url ) );
			}
		}

		if ( function_exists( 'shpigovsky_is_blog_posts_page' ) && shpigovsky_is_blog_posts_page() ) {
			$page_for_posts = (int) get_option( 'page_for_posts' );
			if ( $page_for_posts > 0 ) {
				$url = get_permalink( $page_for_posts );
				if ( is_string( $url ) && '' !== $url ) {
					return self::absolute_https_url( untrailingslashit( $url ) );
				}
			}
		}

		global $wp;
		$request = is_object( $wp ) && isset( $wp->request ) ? (string) $wp->request : '';

		return self::absolute_https_url(
			untrailingslashit( home_url( $request ? '/' . ltrim( $request, '/' ) : '/' ) )
		);
	}

	/**
	 * Open Graph object type for the current request.
	 *
	 * @return string
	 */
	public static function og_type() {
		if ( is_singular( 'post' ) ) {
			return 'article';
		}

		return 'website';
	}

	/**
	 * Open Graph locale tag value when site locale is known.
	 *
	 * @return string
	 */
	public static function og_locale() {
		$locale = trim( (string) get_locale() );
		if ( '' === $locale ) {
			return '';
		}

		if ( false !== strpos( $locale, '_' ) ) {
			return str_replace( '-', '_', $locale );
		}

		$language = strtolower( $locale );
		if ( 'ru' === $language ) {
			return 'ru_RU';
		}

		return $locale;
	}

	/**
	 * Force HTTPS absolute URL when the site is served over TLS.
	 *
	 * @param string $url Raw URL.
	 * @return string
	 */
	public static function absolute_https_url( $url ) {
		$url = trim( (string) $url );
		if ( '' === $url ) {
			return '';
		}

		if ( is_ssl() || 0 === stripos( (string) home_url( '/' ), 'https://' ) ) {
			return set_url_scheme( $url, 'https' );
		}

		return $url;
	}
}
