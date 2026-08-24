<?php
/**
 * Open Graph module — single og:* meta owner for FP-0002.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\OpenGraph;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Registers wp_head Open Graph meta output (separate from SEO + JSON-LD).
 */
final class OpenGraph implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'open-graph.meta';
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
		add_action( 'wp_head', array( __CLASS__, 'render_meta_tags' ), 4 );
	}

	/**
	 * Output server-rendered Open Graph protocol tags.
	 */
	public static function render_meta_tags() {
		$model = TagBuilder::build();
		if ( ! is_array( $model ) ) {
			return;
		}

		self::emit_property( 'og:title', (string) $model['title'] );

		if ( ! empty( $model['description'] ) ) {
			self::emit_property( 'og:description', (string) $model['description'] );
		}

		self::emit_property( 'og:url', (string) $model['url'] );
		self::emit_property( 'og:type', (string) $model['type'] );
		self::emit_property( 'og:site_name', (string) $model['site_name'] );

		if ( ! empty( $model['locale'] ) ) {
			self::emit_property( 'og:locale', (string) $model['locale'] );
		}

		if ( ! empty( $model['image'] ) && is_array( $model['image'] ) ) {
			$image = $model['image'];
			if ( ! empty( $image['url'] ) ) {
				self::emit_property( 'og:image', (string) $image['url'] );
				if ( ! empty( $image['width'] ) ) {
					self::emit_property( 'og:image:width', (string) (int) $image['width'] );
				}
				if ( ! empty( $image['height'] ) ) {
					self::emit_property( 'og:image:height', (string) (int) $image['height'] );
				}
				if ( ! empty( $image['alt'] ) ) {
					self::emit_property( 'og:image:alt', (string) $image['alt'] );
				}
			}
		}

		if ( ! empty( $model['article'] ) && is_array( $model['article'] ) ) {
			if ( ! empty( $model['article']['published_time'] ) ) {
				self::emit_property( 'article:published_time', (string) $model['article']['published_time'] );
			}
			if ( ! empty( $model['article']['modified_time'] ) ) {
				self::emit_property( 'article:modified_time', (string) $model['article']['modified_time'] );
			}
		}
	}

	/**
	 * @param string $property Meta property name.
	 * @param string $content  Attribute value.
	 */
	private static function emit_property( $property, $content ) {
		$content = trim( (string) $content );
		if ( '' === $content ) {
			return;
		}

		echo '<meta property="' . esc_attr( $property ) . '" content="' . esc_attr( $content ) . '" />' . "\n";
	}
}
