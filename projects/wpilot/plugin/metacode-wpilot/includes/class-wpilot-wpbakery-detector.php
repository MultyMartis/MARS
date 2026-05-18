<?php
/**
 * Minimal WPBakery shortcode detection for read-only inspection.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_WPBakery_Detector {
	const MAX_SCAN_BYTES      = 1048576;
	const MAX_SHORTCODE_COUNT = 10000;

	/**
	 * Shortcodes commonly emitted by WPBakery.
	 *
	 * @var array
	 */
	private static $known_shortcodes = array(
		'vc_row',
		'vc_column',
		'vc_column_text',
		'vc_section',
		'vc_empty_space',
		'vc_single_image',
		'vc_btn',
		'vc_raw_html',
		'vc_raw_js',
	);

	/**
	 * Check whether content appears to contain WPBakery shortcodes.
	 *
	 * @param string $content Post content.
	 * @return bool
	 */
	public static function has_wpbakery( $content ) {
		return ! empty( self::shortcode_counts( $content ) );
	}

	/**
	 * Count known WPBakery shortcode appearances.
	 *
	 * @param string $content Post content.
	 * @return array
	 */
	public static function shortcode_counts( $content ) {
		$content = self::normalize_content( $content );
		$counts = array();

		foreach ( self::$known_shortcodes as $shortcode ) {
			$pattern = '/\[' . preg_quote( $shortcode, '/' ) . '(\s|\]|\])/';
			$count   = self::safe_match_count( $pattern, $content );

			if ( $count > 0 ) {
				$counts[ $shortcode ] = $count;
			}
		}

		ksort( $counts );

		return $counts;
	}

	/**
	 * Return basic structural signals without attempting unsafe mutation logic.
	 *
	 * @param string $content Post content.
	 * @return array
	 */
	public static function basic_integrity( $content ) {
		$content     = self::normalize_content( $content );
		$open_rows   = self::safe_match_count( '/\[vc_row(\s|\])/', $content );
		$closed_rows = self::safe_match_count( '/\[\/vc_row\]/', $content );

		return array(
			'vc_row_open_count'  => $open_rows,
			'vc_row_close_count' => $closed_rows,
			'vc_row_balanced'    => $open_rows === $closed_rows,
		);
	}

	/**
	 * Deterministic read-only warnings about structure signals.
	 *
	 * @param string $content Post content.
	 * @return array
	 */
	public static function warnings( $content ) {
		$content   = self::normalize_content( $content );
		$warnings  = array();
		$integrity = self::basic_integrity( $content );

		if ( ! $integrity['vc_row_balanced'] ) {
			$warnings[] = 'vc_row_shortcode_count_mismatch';
		}

		if ( 1 === self::safe_match( '/\[vc_raw_(html|js)(\s|\])/', $content ) ) {
			$warnings[] = 'raw_shortcode_present';
		}

		return $warnings;
	}

	/**
	 * Normalize content before regex inspection without exposing or mutating storage.
	 *
	 * @param mixed $content Potential post content.
	 * @return string
	 */
	private static function normalize_content( $content ) {
		if ( is_object( $content ) && method_exists( $content, '__toString' ) ) {
			$content = (string) $content;
		}

		if ( ! is_scalar( $content ) ) {
			return '';
		}

		$content = (string) $content;

		if ( function_exists( 'wp_check_invalid_utf8' ) ) {
			$content = wp_check_invalid_utf8( $content, true );
		}

		if ( strlen( $content ) > self::MAX_SCAN_BYTES ) {
			return substr( $content, 0, self::MAX_SCAN_BYTES );
		}

		return $content;
	}

	/**
	 * Guarded preg_match wrapper.
	 *
	 * @param string $pattern Regex pattern.
	 * @param string $content Normalized content.
	 * @return int
	 */
	private static function safe_match( $pattern, $content ) {
		$result = @preg_match( $pattern, $content );

		return 1 === $result ? 1 : 0;
	}

	/**
	 * Count regex matches without retaining all match payloads in memory.
	 *
	 * @param string $pattern Regex pattern.
	 * @param string $content Normalized content.
	 * @return int
	 */
	private static function safe_match_count( $pattern, $content ) {
		$count  = 0;
		$offset = 0;
		$length = strlen( $content );

		while ( $offset < $length && $count < self::MAX_SHORTCODE_COUNT ) {
			$matches = array();
			$result  = @preg_match( $pattern, $content, $matches, PREG_OFFSET_CAPTURE, $offset );

			if ( 1 !== $result || empty( $matches[0][0] ) || ! isset( $matches[0][1] ) ) {
				break;
			}

			$count++;
			$offset = (int) $matches[0][1] + max( 1, strlen( $matches[0][0] ) );
		}

		return $count;
	}
}
