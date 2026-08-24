<?php
/**
 * Page-aware Open Graph image selection via existing theme media owners.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\OpenGraph;

use Shpigovsky\Core\StructuredData\DataReaders;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Resolves share image payload without scraping arbitrary body media.
 */
final class ImageResolver {

	/**
	 * @return array{url:string,width:int,height:int,alt:string}|null
	 */
	public static function resolve_for_request() {
		if ( is_front_page() ) {
			return self::from_hero_payload(
				function_exists( 'shpigovsky_get_home_hero_image' ) ? shpigovsky_get_home_hero_image() : null
			);
		}

		if ( self::is_services_hub() ) {
			return self::from_hero_payload(
				function_exists( 'shpigovsky_get_services_hub_hero_image' ) ? shpigovsky_get_services_hub_hero_image() : null
			);
		}

		if ( is_singular( 'service' ) ) {
			$post_id = (int) get_queried_object_id();
			if ( $post_id <= 0 ) {
				return null;
			}

			if ( function_exists( 'shpigovsky_get_service_hero_image_resolved' ) ) {
				return self::from_hero_payload( shpigovsky_get_service_hero_image_resolved( $post_id ) );
			}

			return self::from_attachment_url( DataReaders::post_image_url( $post_id ), $post_id );
		}

		if ( is_singular( 'specialist' ) ) {
			return self::specialist_portrait( (int) get_queried_object_id() );
		}

		if ( is_singular( 'post' ) ) {
			return self::article_featured_image( (int) get_queried_object_id() );
		}

		if ( is_singular() ) {
			$post_id = (int) get_queried_object_id();

			if ( self::is_specialists_hub_page( $post_id ) ) {
				return self::from_hero_payload(
					function_exists( 'shpigovsky_get_institutional_hero_image' )
						? shpigovsky_get_institutional_hero_image( $post_id )
						: null
				);
			}

			if ( has_post_thumbnail( $post_id ) ) {
				return self::from_attachment_id( (int) get_post_thumbnail_id( $post_id ), $post_id );
			}

			if ( function_exists( 'shpigovsky_get_institutional_hero_image' ) ) {
				return self::from_hero_payload( shpigovsky_get_institutional_hero_image( $post_id ) );
			}

			return self::from_attachment_url( DataReaders::post_image_url( $post_id ), $post_id );
		}

		if ( function_exists( 'shpigovsky_is_blog_posts_page' ) && shpigovsky_is_blog_posts_page() ) {
			$page_for_posts = (int) get_option( 'page_for_posts' );
			if ( $page_for_posts > 0 && function_exists( 'shpigovsky_get_institutional_hero_image' ) ) {
				return self::from_hero_payload( shpigovsky_get_institutional_hero_image( $page_for_posts ) );
			}
		}

		return null;
	}

	/**
	 * @param int $post_id Specialist post ID.
	 * @return array{url:string,width:int,height:int,alt:string}|null
	 */
	private static function specialist_portrait( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id <= 0 ) {
			return null;
		}

		$thumb_id = (int) get_post_thumbnail_id( $post_id );
		if ( $thumb_id <= 0 ) {
			return null;
		}

		return self::from_attachment_id( $thumb_id, $post_id );
	}

	/**
	 * Featured image only — no blog archive card fallback for social previews.
	 *
	 * @param int $post_id Post ID.
	 * @return array{url:string,width:int,height:int,alt:string}|null
	 */
	private static function article_featured_image( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id <= 0 || ! has_post_thumbnail( $post_id ) ) {
			return null;
		}

		return self::from_attachment_id( (int) get_post_thumbnail_id( $post_id ), $post_id );
	}

	/**
	 * @param mixed $payload Hero helper payload.
	 * @return array{url:string,width:int,height:int,alt:string}|null
	 */
	private static function from_hero_payload( $payload ) {
		if ( ! is_array( $payload ) ) {
			return null;
		}

		$url = isset( $payload['url'] ) ? trim( (string) $payload['url'] ) : '';
		if ( '' === $url ) {
			return null;
		}

		$width  = isset( $payload['width'] ) ? (int) $payload['width'] : 0;
		$height = isset( $payload['height'] ) ? (int) $payload['height'] : 0;
		$alt    = isset( $payload['alt'] ) ? trim( (string) $payload['alt'] ) : '';

		return self::normalize_payload( $url, $width, $height, $alt );
	}

	/**
	 * @param int $attachment_id Attachment ID.
	 * @param int $post_id       Context post for alt fallback.
	 * @return array{url:string,width:int,height:int,alt:string}|null
	 */
	private static function from_attachment_id( $attachment_id, $post_id ) {
		$attachment_id = (int) $attachment_id;
		if ( $attachment_id <= 0 ) {
			return null;
		}

		$src = wp_get_attachment_image_src( $attachment_id, 'full' );
		if ( ! is_array( $src ) || empty( $src[0] ) ) {
			return null;
		}

		$alt = trim( (string) get_post_meta( $attachment_id, '_wp_attachment_image_alt', true ) );
		if ( '' === $alt && $post_id > 0 ) {
			$alt = trim( (string) get_the_title( $post_id ) );
		}

		return self::normalize_payload(
			(string) $src[0],
			! empty( $src[1] ) ? (int) $src[1] : 0,
			! empty( $src[2] ) ? (int) $src[2] : 0,
			$alt
		);
	}

	/**
	 * @param string $url     Image URL.
	 * @param int    $post_id Context post for alt fallback.
	 * @return array{url:string,width:int,height:int,alt:string}|null
	 */
	private static function from_attachment_url( $url, $post_id ) {
		$url = trim( (string) $url );
		if ( '' === $url ) {
			return null;
		}

		$alt = $post_id > 0 ? trim( (string) get_the_title( $post_id ) ) : '';

		return self::normalize_payload( $url, 0, 0, $alt );
	}

	/**
	 * @param string $url    Image URL.
	 * @param int    $width  Width when known.
	 * @param int    $height Height when known.
	 * @param string $alt    Alt text when known.
	 * @return array{url:string,width:int,height:int,alt:string}|null
	 */
	private static function normalize_payload( $url, $width, $height, $alt ) {
		$url = RequestContext::absolute_https_url( $url );
		if ( '' === $url || 0 === stripos( $url, 'data:' ) ) {
			return null;
		}

		return array(
			'url'    => $url,
			'width'  => max( 0, (int) $width ),
			'height' => max( 0, (int) $height ),
			'alt'    => trim( (string) $alt ),
		);
	}

	/**
	 * @return bool
	 */
	private static function is_services_hub() {
		return is_page_template( 'page-templates/services-hub.php' ) || is_page( 'uslugi' );
	}

	/**
	 * @param int $post_id Page ID.
	 * @return bool
	 */
	private static function is_specialists_hub_page( $post_id ) {
		if ( is_page_template( 'page-templates/specialists-hub.php' ) || is_page( 'specialisty' ) ) {
			return true;
		}

		return $post_id > 0 && 'page-templates/specialists-hub.php' === get_page_template_slug( $post_id );
	}
}
