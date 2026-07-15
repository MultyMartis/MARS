<?php
/**
 * Nested service permalink module — source implementation for V9-06C.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Permalinks;

use Shpigovsky\Core\ContentTypes\Service;
use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

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
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'init', array( __CLASS__, 'register_rewrite_rules' ), 20 );
		add_filter( 'request', array( __CLASS__, 'filter_service_request' ), 10, 1 );
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
		// Depth-3 Excel interim routes (V9-06E29C): zavisimosti/subdivision/leaf.
		add_rewrite_rule(
			'^uslugi/([^/]+)/([^/]+)/([^/]+)/?$',
			'index.php?post_type=' . Service::POST_TYPE . '&' . Service::POST_TYPE . '=$matches[1]/$matches[2]/$matches[3]',
			'top'
		);

		// Depth-2 must pass parent/child path: hierarchical CPT lookup uses get_page_by_path.
		// Leaf-only $matches[2] fails for children (e.g. Service 74 under Service 73).
		add_rewrite_rule(
			'^uslugi/([^/]+)/([^/]+)/?$',
			'index.php?post_type=' . Service::POST_TYPE . '&' . Service::POST_TYPE . '=$matches[1]/$matches[2]',
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
	 * Resolve nested service path query vars to a concrete post ID.
	 *
	 * @param array<string, mixed> $query_vars Request query vars.
	 * @return array<string, mixed>
	 */
	public static function filter_service_request( $query_vars ) {
		if ( empty( $query_vars['post_type'] ) || Service::POST_TYPE !== $query_vars['post_type'] ) {
			return $query_vars;
		}

		$path = '';

		if ( ! empty( $query_vars[ Service::POST_TYPE ] ) ) {
			$path = (string) $query_vars[ Service::POST_TYPE ];
		} elseif ( ! empty( $query_vars['name'] ) && str_contains( (string) $query_vars['name'], '/' ) ) {
			$path = (string) $query_vars['name'];
		}

		if ( '' === $path || ! str_contains( $path, '/' ) ) {
			return $query_vars;
		}

		$post = get_page_by_path( $path, OBJECT, Service::POST_TYPE );

		if ( ! $post instanceof \WP_Post || 'publish' !== $post->post_status ) {
			return $query_vars;
		}

		$query_vars['p']         = (int) $post->ID;
		$query_vars['post_type'] = Service::POST_TYPE;
		unset( $query_vars[ Service::POST_TYPE ], $query_vars['name'] );

		return $query_vars;
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

		return implode( '/', array_slice( $slugs, 0, 3 ) );
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
