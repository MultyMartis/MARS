<?php
/**
 * BreadcrumbList builder aligned with theme breadcrumb helpers.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\StructuredData;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Emits BreadcrumbList only when a real trail exists.
 */
final class BreadcrumbBuilder {

	/**
	 * @param string $page_url Canonical page URL.
	 * @return array<string, mixed>|null
	 */
	public static function build_for_request( $page_url ) {
		if ( is_front_page() ) {
			return null;
		}

		if ( self::is_specialists_hub() ) {
			return null;
		}

		if ( function_exists( 'shpigovsky_breadcrumbs_enabled_for_context' ) && ! shpigovsky_breadcrumbs_enabled_for_context() ) {
			return null;
		}

		$trail = self::resolve_trail();
		if ( empty( $trail ) ) {
			return null;
		}

		$items = array();
		$pos   = 1;

		foreach ( $trail as $crumb ) {
			$label = isset( $crumb['label'] ) ? trim( wp_strip_all_tags( (string) $crumb['label'] ) ) : '';
			$url   = isset( $crumb['url'] ) ? trim( (string) $crumb['url'] ) : '';

			if ( '' === $label ) {
				continue;
			}

			$item = array(
				'@type'    => 'ListItem',
				'position' => $pos,
				'name'     => $label,
			);

			if ( '' !== $url ) {
				$item['item'] = untrailingslashit( $url );
			} else {
				$item['item'] = untrailingslashit( (string) $page_url );
			}

			$items[] = $item;
			++$pos;
		}

		if ( empty( $items ) ) {
			return null;
		}

		return array(
			'@type'           => 'BreadcrumbList',
			'@id'             => EntityIds::breadcrumbs( $page_url ),
			'itemListElement' => $items,
		);
	}

	/**
	 * @return array<int, array{label:string,url:string}>
	 */
	private static function resolve_trail() {
		if ( is_singular( 'service' ) && function_exists( 'shpigovsky_get_service_breadcrumb_trail' ) ) {
			return shpigovsky_get_service_breadcrumb_trail( get_queried_object_id() );
		}

		if ( is_singular( 'post' ) && function_exists( 'shpigovsky_get_blog_single_breadcrumb_trail' ) ) {
			return shpigovsky_get_blog_single_breadcrumb_trail( get_queried_object_id() );
		}

		if ( function_exists( 'shpigovsky_is_blog_posts_page' ) && shpigovsky_is_blog_posts_page() && function_exists( 'shpigovsky_get_blog_breadcrumb_trail' ) ) {
			return shpigovsky_get_blog_breadcrumb_trail();
		}

		if ( is_page_template( 'page-templates/institutional.php' ) && function_exists( 'shpigovsky_is_about_hub_page' ) && shpigovsky_is_about_hub_page() && function_exists( 'shpigovsky_get_about_hub_breadcrumb_trail' ) ) {
			return shpigovsky_get_about_hub_breadcrumb_trail();
		}

		if ( is_search() && function_exists( 'shpigovsky_get_search_breadcrumb_trail' ) ) {
			return shpigovsky_get_search_breadcrumb_trail();
		}

		if ( is_page_template( 'page-templates/services-hub.php' ) ) {
			if ( function_exists( 'shpigovsky_services_hub_list_enabled' ) && shpigovsky_services_hub_list_enabled( 'services_hub_nav_visible' ) ) {
				return array(
					array(
						'label' => __( 'Главная', 'shpigovsky' ),
						'url'   => home_url( '/' ),
					),
					array(
						'label' => __( 'Услуги лечения и профилактики', 'shpigovsky' ),
						'url'   => '',
					),
				);
			}

			return array();
		}

		if ( function_exists( 'shpigovsky_breadcrumbs_allow_empty_shell' ) && shpigovsky_breadcrumbs_allow_empty_shell() ) {
			return array();
		}

		if ( function_exists( 'shpigovsky_get_default_breadcrumb_trail' ) ) {
			return shpigovsky_get_default_breadcrumb_trail();
		}

		return array();
	}

	/**
	 * @return bool
	 */
	private static function is_specialists_hub() {
		if ( is_page_template( 'page-templates/specialists-hub.php' ) ) {
			return true;
		}

		if ( is_page( 'specialisty' ) ) {
			return true;
		}

		return false;
	}
}
