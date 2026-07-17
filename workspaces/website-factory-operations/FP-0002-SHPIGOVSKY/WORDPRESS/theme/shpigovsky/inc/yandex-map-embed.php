<?php
/**
 * Yandex Map Constructor embed validation — FP-0002 V9-06E59.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Sanitize a Yandex Constructor embed snippet to a single safe script tag.
 *
 * @param string $raw_code Raw embed code from admin.
 * @return string Safe script HTML or empty string when invalid.
 */
function shpigovsky_sanitize_yandex_constructor_embed( $raw_code ) {
	$raw_code = trim( html_entity_decode( (string) $raw_code, ENT_QUOTES | ENT_HTML5, 'UTF-8' ) );

	if ( '' === $raw_code ) {
		return '';
	}

	if ( false !== stripos( $raw_code, '<iframe' ) || false !== stripos( $raw_code, 'javascript:' ) ) {
		return '';
	}

	if ( ! preg_match( '/<script\b([^>]*)>\s*<\/script>/is', $raw_code, $matches ) ) {
		return '';
	}

	if ( preg_match( '/<script\b[^>]*>[^<\s]/is', $raw_code ) ) {
		return '';
	}

	$attr_string = $matches[1];
	$allowed     = array( 'type', 'charset', 'async', 'src' );
	$attrs       = array();

	if ( ! preg_match_all( '/([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*=\s*(["\'])(.*?)\2/i', $attr_string, $attr_matches, PREG_SET_ORDER ) ) {
		return '';
	}

	foreach ( $attr_matches as $attr_match ) {
		$name = strtolower( $attr_match[1] );

		if ( 0 === strpos( $name, 'on' ) || ! in_array( $name, $allowed, true ) ) {
			return '';
		}

		$attrs[ $name ] = $attr_match[3];
	}

	if ( empty( $attrs['src'] ) ) {
		return '';
	}

	$src     = html_entity_decode( (string) $attrs['src'], ENT_QUOTES | ENT_HTML5, 'UTF-8' );
	$parsed  = wp_parse_url( $src );
	$scheme  = is_array( $parsed ) ? strtolower( (string) ( $parsed['scheme'] ?? '' ) ) : '';
	$host    = is_array( $parsed ) ? strtolower( (string) ( $parsed['host'] ?? '' ) ) : '';
	$path    = is_array( $parsed ) ? (string) ( $parsed['path'] ?? '' ) : '';
	$query   = is_array( $parsed ) ? (string) ( $parsed['query'] ?? '' ) : '';

	if ( 'https' !== $scheme || 'api-maps.yandex.ru' !== $host ) {
		return '';
	}

	if ( 0 !== strpos( $path, '/services/constructor/1.0/js' ) ) {
		return '';
	}

	if ( '' === $query || false === stripos( $query, 'um=constructor' ) ) {
		return '';
	}

	$safe  = '<script';
	$safe .= ' type="' . esc_attr( $attrs['type'] ?? 'text/javascript' ) . '"';

	if ( ! empty( $attrs['charset'] ) ) {
		$safe .= ' charset="' . esc_attr( $attrs['charset'] ) . '"';
	}

	if ( array_key_exists( 'async', $attrs ) ) {
		$safe .= ' async';
	}

	$safe .= ' src="' . esc_url( $src ) . '"></script>';

	return $safe;
}
