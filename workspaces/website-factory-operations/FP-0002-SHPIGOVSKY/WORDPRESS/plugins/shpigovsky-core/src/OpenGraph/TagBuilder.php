<?php
/**
 * Normalized Open Graph model for FP-0002 public routes.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\OpenGraph;

use Shpigovsky\Core\StructuredData\DataReaders;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Builds deterministic OG tag payloads from existing editorial owners.
 */
final class TagBuilder {

	/**
	 * @return array<string, mixed>|null
	 */
	public static function build() {
		if ( ! RequestContext::should_emit() ) {
			return null;
		}

		$title = self::resolve_title();
		$url   = RequestContext::current_page_url();

		if ( '' === $title || '' === $url ) {
			return null;
		}

		$model = array(
			'title'     => $title,
			'url'       => $url,
			'type'      => RequestContext::og_type(),
			'site_name' => DataReaders::organization_name(),
		);

		$description = self::resolve_description();
		if ( '' !== $description ) {
			$model['description'] = $description;
		}

		$locale = RequestContext::og_locale();
		if ( '' !== $locale ) {
			$model['locale'] = $locale;
		}

		$image = ImageResolver::resolve_for_request();
		if ( is_array( $image ) && ! empty( $image['url'] ) ) {
			$model['image'] = $image;
		}

		if ( 'article' === $model['type'] && is_singular( 'post' ) ) {
			$article = self::article_meta( (int) get_queried_object_id() );
			if ( ! empty( $article ) ) {
				$model['article'] = $article;
			}
		}

		return $model;
	}

	/**
	 * @return string
	 */
	private static function resolve_title() {
		$post_id = RequestContext::context_post_id();
		if ( $post_id > 0 ) {
			$seo = DataReaders::entity_seo_title( $post_id );
			if ( '' !== $seo ) {
				return wp_strip_all_tags( $seo );
			}

			$title = get_the_title( $post_id );
			if ( is_string( $title ) && '' !== trim( $title ) ) {
				return wp_strip_all_tags( trim( $title ) );
			}
		}

		if ( is_front_page() ) {
			$name = DataReaders::organization_name();
			if ( '' !== $name ) {
				return wp_strip_all_tags( $name );
			}
		}

		return wp_strip_all_tags( wp_get_document_title() );
	}

	/**
	 * SEO meta description only — omit when empty (no invented copy).
	 *
	 * @return string
	 */
	private static function resolve_description() {
		$post_id = RequestContext::context_post_id();
		if ( $post_id <= 0 ) {
			return '';
		}

		$desc = DataReaders::entity_seo_description( $post_id );
		if ( '' === $desc ) {
			return '';
		}

		return wp_strip_all_tags( $desc );
	}

	/**
	 * @param int $post_id Post ID.
	 * @return array<string, string>
	 */
	private static function article_meta( $post_id ) {
		$post = get_post( (int) $post_id );
		if ( ! $post instanceof \WP_Post ) {
			return array();
		}

		$meta = array();

		$published = get_post_time( 'c', true, $post, false );
		if ( is_string( $published ) && '' !== $published ) {
			$meta['published_time'] = $published;
		}

		$modified = get_post_modified_time( 'c', true, $post, false );
		if ( is_string( $modified ) && '' !== $modified ) {
			$meta['modified_time'] = $modified;
		}

		return $meta;
	}
}
