<?php
/**
 * Page-aware Schema.org graph builder for FP-0002.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\StructuredData;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Builds a deduplicated @graph for the current request.
 */
final class GraphBuilder {

	/**
	 * @return array<string, mixed>|null
	 */
	public static function build() {
		if ( is_admin() || is_feed() || is_robots() || is_trackback() ) {
			return null;
		}

		if ( is_search() || is_404() ) {
			return null;
		}

		$graph = array();
		self::merge_nodes( $graph, OrganizationBuilder::build_nodes() );
		self::merge_nodes( $graph, array( self::website_node() ) );
		self::merge_nodes( $graph, self::page_nodes() );

		if ( empty( $graph ) ) {
			return null;
		}

		return array(
			'@context' => 'https://schema.org',
			'@graph'   => array_values( $graph ),
		);
	}

	/**
	 * @return array<string, mixed>
	 */
	private static function website_node() {
		$node = array(
			'@type'     => 'WebSite',
			'@id'       => EntityIds::website(),
			'url'       => EntityIds::base_url(),
			'name'      => DataReaders::organization_name(),
			'publisher' => array(
				'@id' => EntityIds::organization(),
			),
		);

		$desc = trim( (string) get_bloginfo( 'description', 'display' ) );
		if ( '' !== $desc ) {
			$node['description'] = wp_strip_all_tags( $desc );
		}

		return $node;
	}

	/**
	 * @return array<int, array<string, mixed>>
	 */
	private static function page_nodes() {
		$page_url = self::current_page_url();
		$nodes    = array();

		$webpage = self::base_webpage_node( $page_url );
		$nodes[] = $webpage;

		if ( is_front_page() ) {
			return $nodes;
		}

		if ( is_page_template( 'page-templates/contacts.php' ) || is_page( 'kontakty' ) ) {
			$nodes[0]['@type'] = 'ContactPage';
			$nodes[0]['about'] = array(
				'@id' => EntityIds::organization(),
			);
			return $nodes;
		}

		if ( self::is_specialists_hub() ) {
			$nodes[0]['@type'] = 'CollectionPage';
			$list = self::specialists_item_list( $page_url );
			if ( null !== $list ) {
				$nodes[] = $list;
				$nodes[0]['mainEntity'] = array( '@id' => $list['@id'] );
			}
			return $nodes;
		}

		if ( is_page_template( 'page-templates/services-hub.php' ) || is_page( 'uslugi' ) ) {
			$nodes[0]['@type'] = 'CollectionPage';
			$list = self::services_item_list( $page_url );
			if ( null !== $list ) {
				$nodes[] = $list;
				$nodes[0]['mainEntity'] = array( '@id' => $list['@id'] );
			}
			return $nodes;
		}

		if ( is_singular( 'service' ) ) {
			$entity = self::service_entity_node( get_queried_object_id(), $page_url );
			if ( null !== $entity ) {
				$nodes[] = $entity;
				$nodes[0]['mainEntity'] = array( '@id' => $entity['@id'] );
			}
			return $nodes;
		}

		if ( is_singular( 'specialist' ) ) {
			$entity = self::person_entity_node( get_queried_object_id(), $page_url );
			if ( null !== $entity ) {
				$nodes[] = $entity;
				$nodes[0]['mainEntity'] = array( '@id' => $entity['@id'] );
			}
			return $nodes;
		}

		if ( is_singular( 'post' ) ) {
			$entity = self::article_entity_node( get_queried_object_id(), $page_url );
			if ( null !== $entity ) {
				$nodes[] = $entity;
				$nodes[0]['mainEntity'] = array( '@id' => $entity['@id'] );
			}
			return $nodes;
		}

		if ( is_page_template( 'page-templates/institutional.php' ) && function_exists( 'shpigovsky_is_about_hub_page' ) && shpigovsky_is_about_hub_page() ) {
			$nodes[0]['@type'] = 'AboutPage';
			$nodes[0]['about'] = array(
				'@id' => EntityIds::organization(),
			);
			return $nodes;
		}

		if ( is_page_template( 'page-templates/reviews.php' ) || is_page( 'otzyvy' ) ) {
			$nodes[0]['@type'] = 'CollectionPage';
			return $nodes;
		}

		return $nodes;
	}

	/**
	 * @param string $page_url Canonical URL.
	 * @return array<string, mixed>
	 */
	private static function base_webpage_node( $page_url ) {
		$post_id = self::context_post_id();
		$name    = self::page_name( $post_id );
		$desc    = DataReaders::post_description( $post_id );

		$node = array(
			'@type'       => is_front_page() ? 'WebPage' : 'WebPage',
			'@id'         => EntityIds::webpage( $page_url ),
			'url'         => $page_url,
			'name'        => $name,
			'isPartOf'    => array(
				'@id' => EntityIds::website(),
			),
			'inLanguage'  => get_bloginfo( 'language' ),
		);

		if ( '' !== $desc ) {
			$node['description'] = $desc;
		}

		$image = DataReaders::post_image_url( $post_id );
		if ( '' !== $image ) {
			$node['primaryImageOfPage'] = $image;
		}

		$breadcrumb = BreadcrumbBuilder::build_for_request( $page_url );
		if ( null !== $breadcrumb ) {
			$node['breadcrumb'] = array(
				'@id' => $breadcrumb['@id'],
			);
		}

		return $node;
	}

	/**
	 * @param int    $post_id Post ID.
	 * @param string $page_url Canonical URL.
	 * @return array<string, mixed>|null
	 */
	private static function service_entity_node( $post_id, $page_url ) {
		$post = get_post( (int) $post_id );
		if ( ! $post instanceof \WP_Post ) {
			return null;
		}

		$node = array(
			'@type'    => 'Service',
			'@id'      => EntityIds::post_entity( $post_id ),
			'name'     => get_the_title( $post ),
			'url'      => $page_url,
			'provider' => array(
				'@id' => EntityIds::organization(),
			),
		);

		$desc = DataReaders::post_description( $post_id );
		if ( '' !== $desc ) {
			$node['description'] = $desc;
		}

		$image = DataReaders::post_image_url( $post_id );
		if ( '' !== $image ) {
			$node['image'] = $image;
		}

		return $node;
	}

	/**
	 * @param int    $post_id Post ID.
	 * @param string $page_url Canonical URL.
	 * @return array<string, mixed>|null
	 */
	private static function person_entity_node( $post_id, $page_url ) {
		$post = get_post( (int) $post_id );
		if ( ! $post instanceof \WP_Post ) {
			return null;
		}

		$node = array(
			'@type'    => 'Person',
			'@id'      => EntityIds::post_entity( $post_id ),
			'name'     => get_the_title( $post ),
			'url'      => $page_url,
			'worksFor' => array(
				'@id' => EntityIds::organization(),
			),
		);

		$job = DataReaders::specialist_job_title( $post_id );
		if ( '' !== $job ) {
			$node['jobTitle'] = $job;
		}

		$desc = DataReaders::post_description( $post_id );
		if ( '' !== $desc ) {
			$node['description'] = $desc;
		}

		$image = DataReaders::post_image_url( $post_id );
		if ( '' !== $image ) {
			$node['image'] = $image;
		}

		return $node;
	}

	/**
	 * @param int    $post_id Post ID.
	 * @param string $page_url Canonical URL.
	 * @return array<string, mixed>|null
	 */
	private static function article_entity_node( $post_id, $page_url ) {
		$post = get_post( (int) $post_id );
		if ( ! $post instanceof \WP_Post ) {
			return null;
		}

		$node = array(
			'@type'         => 'Article',
			'@id'           => EntityIds::post_entity( $post_id ),
			'headline'      => get_the_title( $post ),
			'url'           => $page_url,
			'datePublished' => get_the_date( 'c', $post ),
			'dateModified'  => get_the_modified_date( 'c', $post ),
			'publisher'     => array(
				'@id' => EntityIds::organization(),
			),
			'mainEntityOfPage' => array(
				'@id' => EntityIds::webpage( $page_url ),
			),
		);

		$desc = DataReaders::post_description( $post_id );
		if ( '' !== $desc ) {
			$node['description'] = $desc;
		}

		$image = DataReaders::post_image_url( $post_id );
		if ( '' !== $image ) {
			$node['image'] = $image;
		}

		$author = self::public_author_node( $post );
		if ( null !== $author ) {
			$node['author'] = $author;
		}

		return $node;
	}

	/**
	 * Only emit author when a public display name exists and is not a technical account.
	 *
	 * @param \WP_Post $post Post.
	 * @return array<string, string>|null
	 */
	private static function public_author_node( $post ) {
		$author_id = (int) $post->post_author;
		if ( $author_id <= 0 ) {
			return null;
		}

		$user = get_userdata( $author_id );
		if ( ! $user instanceof \WP_User ) {
			return null;
		}

		$display = trim( (string) $user->display_name );
		$login   = trim( (string) $user->user_login );

		if ( '' === $display ) {
			return null;
		}

		$blocked = array( 'admin', 'administrator', 'editor', 'operator', 'system' );
		if ( in_array( strtolower( $login ), $blocked, true ) || in_array( strtolower( $display ), $blocked, true ) ) {
			return null;
		}

		return array(
			'@type' => 'Person',
			'name'  => $display,
		);
	}

	/**
	 * @param string $page_url Page URL.
	 * @return array<string, mixed>|null
	 */
	private static function services_item_list( $page_url ) {
		if ( ! post_type_exists( 'service' ) ) {
			return null;
		}

		$posts = get_posts(
			array(
				'post_type'      => 'service',
				'post_status'    => 'publish',
				'posts_per_page' => 100,
				'orderby'        => 'menu_order',
				'order'          => 'ASC',
				'no_found_rows'  => true,
			)
		);

		if ( empty( $posts ) ) {
			return null;
		}

		$elements = array();
		$pos      = 1;

		foreach ( $posts as $post ) {
			if ( ! $post instanceof \WP_Post ) {
				continue;
			}

			$url = get_permalink( $post );
			if ( ! is_string( $url ) || '' === $url ) {
				continue;
			}

			$elements[] = array(
				'@type'    => 'ListItem',
				'position' => $pos,
				'url'      => untrailingslashit( $url ),
				'name'     => get_the_title( $post ),
			);
			++$pos;
		}

		if ( empty( $elements ) ) {
			return null;
		}

		return array(
			'@type'           => 'ItemList',
			'@id'             => EntityIds::item_list( $page_url, 'services' ),
			'itemListElement' => $elements,
		);
	}

	/**
	 * @param string $page_url Page URL.
	 * @return array<string, mixed>|null
	 */
	private static function specialists_item_list( $page_url ) {
		$cards = function_exists( 'shpigovsky_get_specialists_cards' ) ? shpigovsky_get_specialists_cards() : array();
		if ( empty( $cards ) ) {
			return null;
		}

		$elements = array();
		$pos      = 1;

		foreach ( $cards as $card ) {
			$url = isset( $card['link'] ) ? trim( (string) $card['link'] ) : '';
			$name = isset( $card['name'] ) ? trim( (string) $card['name'] ) : '';
			if ( '' === $url || '' === $name ) {
				continue;
			}

			if ( false !== strpos( $url, '/specyalisty/' ) ) {
				$url = str_replace( '/specyalisty/', '/specialisty/', $url );
			}

			$elements[] = array(
				'@type'    => 'ListItem',
				'position' => $pos,
				'url'      => untrailingslashit( $url ),
				'name'     => $name,
			);
			++$pos;
		}

		if ( empty( $elements ) ) {
			return null;
		}

		return array(
			'@type'           => 'ItemList',
			'@id'             => EntityIds::item_list( $page_url, 'specialists' ),
			'itemListElement' => $elements,
		);
	}

	/**
	 * @return string
	 */
	private static function current_page_url() {
		if ( is_front_page() ) {
			return EntityIds::base_url();
		}

		if ( is_singular() ) {
			$url = get_permalink( get_queried_object_id() );
			if ( is_string( $url ) && '' !== $url ) {
				return untrailingslashit( $url );
			}
		}

		if ( function_exists( 'shpigovsky_is_blog_posts_page' ) && shpigovsky_is_blog_posts_page() ) {
			$page_for_posts = (int) get_option( 'page_for_posts' );
			if ( $page_for_posts > 0 ) {
				$url = get_permalink( $page_for_posts );
				if ( is_string( $url ) && '' !== $url ) {
					return untrailingslashit( $url );
				}
			}
		}

		global $wp;
		$request = is_object( $wp ) && isset( $wp->request ) ? (string) $wp->request : '';
		return untrailingslashit( home_url( $request ? '/' . ltrim( $request, '/' ) : '/' ) );
	}

	/**
	 * @return int
	 */
	private static function context_post_id() {
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
	 * @param int $post_id Post ID.
	 * @return string
	 */
	private static function page_name( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id > 0 ) {
			$seo = DataReaders::entity_seo_title( $post_id );
			if ( '' !== $seo ) {
				return $seo;
			}

			$title = get_the_title( $post_id );
			if ( is_string( $title ) && '' !== trim( $title ) ) {
				return trim( $title );
			}
		}

		if ( is_front_page() ) {
			return DataReaders::organization_name();
		}

		return wp_get_document_title();
	}

	/**
	 * @return bool
	 */
	private static function is_specialists_hub() {
		return is_page_template( 'page-templates/specialists-hub.php' ) || is_page( 'specialisty' );
	}

	/**
	 * @param array<string, array<string, mixed>> $target Target map keyed by @id.
	 * @param array<int, array<string, mixed>>     $nodes Nodes.
	 */
	private static function merge_nodes( array &$target, array $nodes ) {
		foreach ( $nodes as $node ) {
			if ( ! is_array( $node ) || empty( $node['@id'] ) ) {
				continue;
			}
			$target[ (string) $node['@id'] ] = $node;
		}

		$breadcrumb = BreadcrumbBuilder::build_for_request( self::current_page_url() );
		if ( null !== $breadcrumb && ! empty( $breadcrumb['@id'] ) ) {
			$target[ (string) $breadcrumb['@id'] ] = $breadcrumb;
		}
	}
}
