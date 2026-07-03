<?php
/**
 * Nested service permalink module — source implementation for V9-06C.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Permalinks;

use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\Contracts\ModuleInterface;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Service permalink and rewrite boundary.
 */
final class ServicePermalinks implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'permalinks.service';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ! shpigovsky_core_is_skeleton_mode();
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'init', array( __CLASS__, 'register_rewrite_rules' ), 20 );
		add_filter( 'post_type_link', array( __CLASS__, 'filter_service_permalink' ), 10, 2 );
		add_filter( 'redirect_canonical', array( __CLASS__, 'filter_canonical_redirect' ), 10, 2 );
	}

	/**
	 * Register nested service rewrite rules per FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.
	 *
	 * The exact /uslugi/ hub remains a native Page. These rules only claim child paths.
	 * Do not flush rewrite rules here; activation/migration flush is a later delivery boundary.
	 */
	public static function register_rewrite_rules() {
		add_rewrite_rule(
			'^uslugi/([^/]+)/([^/]+)/?$',
			'index.php?post_type=' . Service::POST_TYPE . '&' . Service::POST_TYPE . '=$matches[2]',
			'top'
		);

		add_rewrite_rule(
			'^uslugi/([^/]+)/?$',
			'index.php?post_type=' . Service::POST_TYPE . '&' . Service::POST_TYPE . '=$matches[1]',
			'top'
		);
	}

	/**
	 * Generate canonical service permalinks from ancestor chain.
	 *
	 * @param string   $permalink Generated permalink.
	 * @param \WP_Post $post Post object.
	 * @return string
	 */
	public static function filter_service_permalink( $permalink, $post ) {
		if ( ! $post instanceof \WP_Post || Service::POST_TYPE !== $post->post_type ) {
			return $permalink;
		}

		$path = self::build_path_from_post( $post );

		if ( '' === $path || 'uslugi' === $path ) {
			return home_url( '/uslugi/' );
		}

		return home_url( user_trailingslashit( 'uslugi/' . $path ) );
	}

	/**
	 * Avoid canonical redirects that collapse nested service paths to leaf-only paths.
	 *
	 * @param string|false $redirect_url Proposed redirect URL.
	 * @param string       $requested_url Requested URL.
	 * @return string|false
	 */
	public static function filter_canonical_redirect( $redirect_url, $requested_url ) {
		if ( ! is_singular( Service::POST_TYPE ) ) {
			return $redirect_url;
		}

		$canonical = get_permalink();

		if ( $canonical && untrailingslashit( $canonical ) === untrailingslashit( $requested_url ) ) {
			return false;
		}

		return $redirect_url;
	}

	/**
	 * Build a relative service path from a post object.
	 *
	 * @param \WP_Post|object $post Service-like post object.
	 * @return string
	 */
	public static function build_path_from_post( $post ) {
		$slugs   = array();
		$current = $post;
		$depth   = 0;

		while ( $current && $depth < 3 ) {
			$slug = isset( $current->post_name ) ? sanitize_title( $current->post_name ) : '';

			if ( '' === $slug || 'uslugi' === $slug ) {
				break;
			}

			array_unshift( $slugs, $slug );

			$parent_id = isset( $current->post_parent ) ? (int) $current->post_parent : 0;

			if ( $parent_id <= 0 ) {
				break;
			}

			$current = get_post( $parent_id );
			$depth++;
		}

		return implode( '/', array_slice( $slugs, 0, 2 ) );
	}

	/**
	 * Pure source-test helper for simulated services.
	 *
	 * @param array<string, array{slug:string,parent:?string}> $services Service fixture map.
	 * @param string                                           $service_id Service ID.
	 * @return string
	 */
	public static function build_path_from_fixture( array $services, $service_id ) {
		if ( ! isset( $services[ $service_id ] ) ) {
			return '';
		}

		$slugs   = array();
		$current = $service_id;
		$guard   = 0;

		while ( isset( $services[ $current ] ) && $guard < 3 ) {
			array_unshift( $slugs, sanitize_title( $services[ $current ]['slug'] ) );
			$current = $services[ $current ]['parent'];
			$guard++;
		}

		return 'uslugi/' . implode( '/', array_slice( $slugs, 0, 2 ) ) . '/';
	}
}
