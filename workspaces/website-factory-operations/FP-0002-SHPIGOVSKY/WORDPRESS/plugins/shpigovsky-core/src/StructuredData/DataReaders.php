<?php
/**
 * Read-only accessors for schema data owned by theme / ACF options.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\StructuredData;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Normalized reads from existing WordPress data owners.
 */
final class DataReaders {

	/**
	 * @param string $field Option field name.
	 * @return string
	 */
	public static function site_option( $field ) {
		if ( function_exists( 'shpigovsky_get_site_option' ) ) {
			return trim( (string) shpigovsky_get_site_option( $field ) );
		}

		if ( function_exists( 'get_field' ) ) {
			$value = get_field( $field, 'option' );
			if ( is_string( $value ) ) {
				return trim( $value );
			}
		}

		return '';
	}

	/**
	 * @return string
	 */
	public static function organization_name() {
		$name = self::site_option( 'organisation_name' );
		if ( '' !== $name ) {
			return $name;
		}

		if ( function_exists( 'shpigovsky_brand_label' ) ) {
			return trim( (string) shpigovsky_brand_label() );
		}

		return trim( (string) get_bloginfo( 'name', 'display' ) );
	}

	/**
	 * @return string
	 */
	public static function primary_phone() {
		$phone = self::site_option( 'phone_primary' );
		if ( '' !== $phone ) {
			return $phone;
		}

		return self::site_option( 'phone_secondary' );
	}

	/**
	 * @return string
	 */
	public static function site_email() {
		$email = sanitize_email( self::site_option( 'site_email' ) );

		return is_email( $email ) ? $email : '';
	}

	/**
	 * @return string
	 */
	public static function site_logo_url() {
		if ( function_exists( 'get_custom_logo' ) ) {
			$logo_id = (int) get_theme_mod( 'custom_logo' );
			if ( $logo_id > 0 ) {
				$url = wp_get_attachment_image_url( $logo_id, 'full' );
				if ( is_string( $url ) && '' !== $url ) {
					return $url;
				}
			}
		}

		return '';
	}

	/**
	 * Contacts page ID by slug.
	 *
	 * @return int
	 */
	public static function contacts_page_id() {
		$page = get_page_by_path( 'kontakty' );

		return ( $page instanceof \WP_Post ) ? (int) $page->ID : 0;
	}

	/**
	 * Normalized location rows for schema (same owner as contacts page).
	 *
	 * @return array<int, array<string, string>>
	 */
	public static function contact_locations() {
		$page_id = self::contacts_page_id();
		if ( $page_id <= 0 || ! function_exists( 'get_field' ) ) {
			return array();
		}

		$rows = get_field( 'contacts_locations', $page_id );
		if ( is_array( $rows ) && ! empty( $rows ) && function_exists( 'shpigovsky_normalize_contacts_location_rows' ) ) {
			return shpigovsky_normalize_contacts_location_rows( $rows );
		}

		if ( function_exists( 'shpigovsky_get_contacts_static_locations' ) ) {
			return shpigovsky_get_contacts_static_locations();
		}

		return array();
	}

	/**
	 * @param int $post_id Post ID.
	 * @return string
	 */
	public static function entity_seo_title( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id <= 0 ) {
			return '';
		}

		if ( function_exists( 'shpigovsky_get_entity_seo_field' ) ) {
			return trim( (string) shpigovsky_get_entity_seo_field( $post_id, 'fp02_seo_title' ) );
		}

		return '';
	}

	/**
	 * @param int $post_id Post ID.
	 * @return string
	 */
	public static function entity_seo_description( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id <= 0 ) {
			return '';
		}

		if ( function_exists( 'shpigovsky_get_entity_seo_field' ) ) {
			return trim( (string) shpigovsky_get_entity_seo_field( $post_id, 'fp02_seo_description' ) );
		}

		return '';
	}

	/**
	 * Plain description fallback from excerpt/content.
	 *
	 * @param int $post_id Post ID.
	 * @return string
	 */
	public static function post_description( $post_id ) {
		$post_id = (int) $post_id;
		$desc    = self::entity_seo_description( $post_id );
		if ( '' !== $desc ) {
			return wp_strip_all_tags( $desc );
		}

		$post = get_post( $post_id );
		if ( ! $post instanceof \WP_Post ) {
			return '';
		}

		$excerpt = trim( (string) $post->post_excerpt );
		if ( '' !== $excerpt ) {
			return wp_strip_all_tags( $excerpt );
		}

		$content = trim( wp_strip_all_tags( (string) $post->post_content ) );
		if ( '' === $content ) {
			return '';
		}

		return wp_html_excerpt( $content, 300, '…' );
	}

	/**
	 * Featured image URL when present.
	 *
	 * @param int $post_id Post ID.
	 * @return string
	 */
	public static function post_image_url( $post_id ) {
		$url = get_the_post_thumbnail_url( (int) $post_id, 'full' );

		return is_string( $url ) ? $url : '';
	}

	/**
	 * Canonical absolute URL for current or given post.
	 *
	 * @param int $post_id Post ID.
	 * @return string
	 */
	public static function canonical_url( $post_id = 0 ) {
		if ( $post_id > 0 ) {
			$url = get_permalink( (int) $post_id );
			return is_string( $url ) ? untrailingslashit( $url ) : '';
		}

		if ( is_singular() ) {
			$url = get_permalink( get_queried_object_id() );
			return is_string( $url ) ? untrailingslashit( $url ) : '';
		}

		if ( is_front_page() ) {
			return untrailingslashit( home_url( '/' ) );
		}

		if ( is_home() ) {
			$page_for_posts = (int) get_option( 'page_for_posts' );
			if ( $page_for_posts > 0 ) {
				$url = get_permalink( $page_for_posts );
				return is_string( $url ) ? untrailingslashit( $url ) : untrailingslashit( home_url( '/' ) );
			}
		}

		return untrailingslashit( home_url( add_query_arg( array(), $GLOBALS['wp']->request ?? '' ) ) );
	}

	/**
	 * Specialist role / job title from ACF.
	 *
	 * @param int $post_id Specialist post ID.
	 * @return string
	 */
	public static function specialist_job_title( $post_id ) {
		$post_id = (int) $post_id;
		if ( $post_id <= 0 || ! function_exists( 'get_field' ) ) {
			return '';
		}

		$role = get_field( 'specialist_role', $post_id );
		if ( is_string( $role ) && '' !== trim( $role ) ) {
			return trim( $role );
		}

		$post = get_post( $post_id );
		if ( $post instanceof \WP_Post ) {
			$excerpt = trim( (string) $post->post_excerpt );
			if ( '' !== $excerpt ) {
				return $excerpt;
			}
		}

		return '';
	}
}
