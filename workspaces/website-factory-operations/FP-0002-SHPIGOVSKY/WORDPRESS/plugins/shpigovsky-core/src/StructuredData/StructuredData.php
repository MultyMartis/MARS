<?php
/**
 * Structured data module — single JSON-LD graph owner for FP-0002.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\StructuredData;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Registers wp_head JSON-LD output.
 */
final class StructuredData implements ModuleInterface {

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'structured-data.schema-org';
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
		add_action( 'wp_head', array( __CLASS__, 'render_json_ld' ), 6 );
	}

	/**
	 * Output one server-rendered JSON-LD script block.
	 */
	public static function render_json_ld() {
		$graph = GraphBuilder::build();
		if ( null === $graph ) {
			return;
		}

		$json = wp_json_encode( $graph, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT );
		if ( ! is_string( $json ) || '' === $json ) {
			return;
		}

		echo '<script type="application/ld+json">' . $json . '</script>' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- JSON encoded.
	}
}
