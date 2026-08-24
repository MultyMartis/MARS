<?php
/**
 * Stable Schema.org @id helpers for FP-0002 graph nodes.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\StructuredData;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Deterministic entity identifiers rooted at the canonical site URL.
 */
final class EntityIds {

	/**
	 * Site origin without trailing slash.
	 *
	 * @return string
	 */
	public static function base_url() {
		return untrailingslashit( home_url( '/' ) );
	}

	/**
	 * @return string
	 */
	public static function website() {
		return self::base_url() . '/#website';
	}

	/**
	 * Primary medical organization node.
	 *
	 * @return string
	 */
	public static function organization() {
		return self::base_url() . '/#organization';
	}

	/**
	 * Branch / clinic location node.
	 *
	 * @param string $key Stable slug key.
	 * @return string
	 */
	public static function location( $key ) {
		$key = sanitize_title( (string) $key );
		if ( '' === $key ) {
			$key = 'location';
		}

		return self::base_url() . '/#location-' . $key;
	}

	/**
	 * Current page WebPage node.
	 *
	 * @param string $url Canonical page URL.
	 * @return string
	 */
	public static function webpage( $url ) {
		$url = untrailingslashit( (string) $url );
		if ( '' === $url ) {
			$url = self::base_url();
		}

		return $url . '#webpage';
	}

	/**
	 * BreadcrumbList node for a page.
	 *
	 * @param string $url Canonical page URL.
	 * @return string
	 */
	public static function breadcrumbs( $url ) {
		return self::webpage( $url ) . '-breadcrumb';
	}

	/**
	 * ItemList node scoped to a page.
	 *
	 * @param string $url Canonical page URL.
	 * @param string $scope Scope slug.
	 * @return string
	 */
	public static function item_list( $url, $scope ) {
		$scope = sanitize_title( (string) $scope );
		if ( '' === $scope ) {
			$scope = 'items';
		}

		return self::webpage( $url ) . '-' . $scope . '-list';
	}

	/**
	 * Entity node for a post object.
	 *
	 * @param int $post_id Post ID.
	 * @return string
	 */
	public static function post_entity( $post_id ) {
		$url = get_permalink( (int) $post_id );

		return is_string( $url ) && '' !== $url ? untrailingslashit( $url ) . '#entity' : self::base_url() . '/#entity-' . (int) $post_id;
	}
}
