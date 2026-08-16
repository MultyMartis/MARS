<?php
/**
 * WordPress-native sitemap configuration — PROD-P10.
 *
 * Extends core /wp-sitemap.xml; does not invent a second competing sitemap system.
 * Generation can be enabled even when blog_public=0 (temporary-domain noindex).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enable/disable core sitemaps from Admin setting (independent of blog_public).
 *
 * @param bool $enabled Core decision.
 * @return bool
 */
function shpigovsky_sitemaps_enabled( $enabled ) {
	unset( $enabled );
	return shpigovsky_sitemap_is_enabled();
}
add_filter( 'wp_sitemaps_enabled', 'shpigovsky_sitemaps_enabled', 20 );

/**
 * Disable users provider.
 *
 * @param WP_Sitemaps_Provider|false $provider Provider.
 * @param string                     $name Name.
 * @return WP_Sitemaps_Provider|false
 */
function shpigovsky_sitemaps_filter_providers( $provider, $name ) {
	if ( 'users' === $name ) {
		return false;
	}

	return $provider;
}
add_filter( 'wp_sitemaps_add_provider', 'shpigovsky_sitemaps_filter_providers', 10, 2 );

/**
 * Limit public post types in sitemap.
 *
 * @param array<string, WP_Post_Type> $post_types Post types.
 * @return array<string, WP_Post_Type>
 */
function shpigovsky_sitemaps_post_types( $post_types ) {
	if ( ! is_array( $post_types ) ) {
		return array();
	}

	if ( ! shpigovsky_seo_get_bool( 'sitemap_include_pages', true ) ) {
		unset( $post_types['page'] );
	}

	if ( ! shpigovsky_seo_get_bool( 'sitemap_include_articles', true ) ) {
		unset( $post_types['post'] );
	}

	if ( ! shpigovsky_seo_get_bool( 'sitemap_include_services', true ) ) {
		unset( $post_types['service'] );
	} elseif ( isset( $post_types['service'] ) === false && post_type_exists( 'service' ) ) {
		$obj = get_post_type_object( 'service' );
		if ( $obj instanceof WP_Post_Type && $obj->public ) {
			$post_types['service'] = $obj;
		}
	}

	// Specialists use dedicated provider (wp-sitemap-specialists-1.xml); never duplicate under posts.
	unset( $post_types['specialist'] );

	unset( $post_types['attachment'] );

	return $post_types;
}
add_filter( 'wp_sitemaps_post_types', 'shpigovsky_sitemaps_post_types', 20 );

/**
 * Hide unused taxonomies from sitemap.
 *
 * @param array<string, WP_Taxonomy> $taxonomies Taxonomies.
 * @return array<string, WP_Taxonomy>
 */
function shpigovsky_sitemaps_taxonomies( $taxonomies ) {
	return array();
}
add_filter( 'wp_sitemaps_taxonomies', 'shpigovsky_sitemaps_taxonomies', 20 );

/**
 * Specialist IDs for sitemap (PROD-P11 CPT; legacy hub children only if CPT empty).
 *
 * @return array<int, int>
 */
function shpigovsky_sitemap_specialist_page_ids() {
	$ids = array();

	if ( post_type_exists( 'specialist' ) ) {
		$cpt_ids = get_posts(
			array(
				'post_type'              => 'specialist',
				'post_status'            => 'publish',
				'posts_per_page'         => 200,
				'orderby'                => 'menu_order title',
				'order'                  => 'ASC',
				'has_password'           => false,
				'no_found_rows'          => true,
				'update_post_meta_cache' => false,
				'update_post_term_cache' => false,
				'fields'                 => 'ids',
			)
		);
		$ids = array_map( 'intval', (array) $cpt_ids );
	}

	if ( ! empty( $ids ) ) {
		return array_values( array_unique( array_filter( $ids ) ) );
	}

	// Legacy / rollback: child pages of hub.
	$hub = get_page_by_path( 'specyalisty' );

	if ( ! $hub instanceof WP_Post ) {
		return array();
	}

	$children = get_posts(
		array(
			'post_type'              => 'page',
			'post_status'            => 'publish',
			'post_parent'            => (int) $hub->ID,
			'posts_per_page'         => 200,
			'orderby'                => 'menu_order title',
			'order'                  => 'ASC',
			'has_password'           => false,
			'no_found_rows'          => true,
			'update_post_meta_cache' => false,
			'update_post_term_cache' => false,
			'fields'                 => 'ids',
		)
	);

	return array_values( array_unique( array_filter( array_map( 'intval', (array) $children ) ) ) );
}

/**
 * Combined exclusion IDs for sitemap queries.
 *
 * @param string $post_type Post type.
 * @return array<int, int>
 */
function shpigovsky_sitemap_exclude_ids_for_type( $post_type ) {
	$exclude = shpigovsky_seo_get_id_list( 'sitemap_exclude_objects' );

	if ( function_exists( 'shpigovsky_search_excluded_page_ids' ) && 'page' === $post_type ) {
		$exclude = array_merge( $exclude, shpigovsky_search_excluded_page_ids() );
	}

	if ( 'page' === $post_type ) {
		// Specialists have their own provider when enabled; never duplicate under pages.
		$exclude = array_merge( $exclude, shpigovsky_sitemap_specialist_page_ids() );
	}

	return array_values( array_unique( array_filter( array_map( 'intval', $exclude ) ) ) );
}

/**
 * Apply exclusions to core post sitemap queries.
 *
 * @param array<string, mixed> $args Query args.
 * @param string               $post_type Post type.
 * @return array<string, mixed>
 */
function shpigovsky_sitemaps_posts_query_args( $args, $post_type ) {
	$exclude = shpigovsky_sitemap_exclude_ids_for_type( (string) $post_type );

	if ( empty( $exclude ) ) {
		return $args;
	}

	$existing = isset( $args['post__not_in'] ) ? array_map( 'intval', (array) $args['post__not_in'] ) : array();
	$args['post__not_in'] = array_values( array_unique( array_merge( $existing, $exclude ) ) );

	return $args;
}
add_filter( 'wp_sitemaps_posts_query_args', 'shpigovsky_sitemaps_posts_query_args', 20, 2 );

/**
 * Specialists sitemap provider registration (class defined after core sitemap load).
 *
 * @return void
 */
function shpigovsky_sitemaps_register_specialists_provider() {
	if ( ! shpigovsky_sitemap_is_enabled() ) {
		return;
	}

	if ( ! shpigovsky_seo_get_bool( 'sitemap_include_specialists', true ) ) {
		return;
	}

	if ( empty( shpigovsky_sitemap_specialist_page_ids() ) ) {
		return;
	}

	if ( ! class_exists( 'WP_Sitemaps_Provider' ) || ! function_exists( 'wp_register_sitemap_provider' ) ) {
		return;
	}

	if ( ! class_exists( 'Shpigovsky_Sitemaps_Specialists_Provider', false ) ) {
		/**
		 * Specialists sitemap provider (PROD-P11 Specialist CPT).
		 */
		class Shpigovsky_Sitemaps_Specialists_Provider extends WP_Sitemaps_Provider {

			/**
			 * Constructor.
			 */
			public function __construct() {
				$this->name        = 'specialists';
				$this->object_type = 'specialist';
			}

			/**
			 * @param int    $page_num       Page.
			 * @param string $object_subtype Subtype.
			 * @return array<int, array{loc:string,lastmod?:string}>
			 */
			public function get_url_list( $page_num, $object_subtype = '' ) {
				unset( $object_subtype );

				if ( 1 < (int) $page_num ) {
					return array();
				}

				$exclude  = shpigovsky_seo_get_id_list( 'sitemap_exclude_objects' );
				$ids      = shpigovsky_sitemap_specialist_page_ids();
				$url_list = array();

				foreach ( $ids as $id ) {
					if ( in_array( (int) $id, $exclude, true ) ) {
						continue;
					}

					$url = get_permalink( $id );
					if ( ! is_string( $url ) || '' === $url ) {
						continue;
					}

					$entry = array(
						'loc' => $url,
					);

					$modified = get_post_modified_time( 'c', true, $id );
					if ( is_string( $modified ) && '' !== $modified ) {
						$entry['lastmod'] = $modified;
					}

					$url_list[] = $entry;
				}

				return $url_list;
			}

			/**
			 * @param string $object_subtype Subtype.
			 * @return int
			 */
			public function get_max_num_pages( $object_subtype = '' ) {
				unset( $object_subtype );

				$ids     = shpigovsky_sitemap_specialist_page_ids();
				$exclude = shpigovsky_seo_get_id_list( 'sitemap_exclude_objects' );
				$count   = 0;

				foreach ( $ids as $id ) {
					if ( ! in_array( (int) $id, $exclude, true ) ) {
						++$count;
					}
				}

				return $count > 0 ? 1 : 0;
			}
		}
	}

	wp_register_sitemap_provider( 'specialists', new Shpigovsky_Sitemaps_Specialists_Provider() );
}
add_action( 'init', 'shpigovsky_sitemaps_register_specialists_provider', 30 );
