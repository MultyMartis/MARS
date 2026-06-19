<?php
/**
 * Content checksum helpers for WPilot integrity checks.
 *
 * @package MetaCode_WPilot
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class WPilot_Checksum {
	/**
	 * Normalize content to JSON-safe UTF-8 before checksumming.
	 *
	 * @param string $content Raw content.
	 * @return string
	 */
	public static function normalize_content( $content ) {
		$content = is_string( $content ) ? $content : '';

		if ( function_exists( 'wp_check_invalid_utf8' ) ) {
			$content = wp_check_invalid_utf8( $content, true );
		}

		return is_string( $content ) ? $content : '';
	}

	/**
	 * Generate a sha256 checksum with the documented prefix.
	 *
	 * @param string $content Content to hash.
	 * @return string
	 */
	public static function hash( $content ) {
		return 'sha256:' . hash( 'sha256', self::normalize_content( $content ) );
	}

	/**
	 * Verify content against an expected checksum.
	 *
	 * @param string $content Content to verify.
	 * @param string $expected_checksum Expected checksum value.
	 * @return bool
	 */
	public static function verify( $content, $expected_checksum ) {
		if ( ! is_string( $expected_checksum ) || '' === $expected_checksum ) {
			return false;
		}

		return hash_equals( $expected_checksum, self::hash( $content ) );
	}
}
