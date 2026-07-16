<?php
/**
 * Site chrome helpers — safe ACF option reads and asset URLs.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Read an ACF options field without fatal when ACF or value is missing.
 *
 * @param string $field_name Option field name.
 * @return string Sanitized scalar string or empty.
 */
function shpigovsky_get_site_option( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$value = get_field( $field_name, 'option' );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Theme asset URI helper.
 *
 * @param string $relative_path Path relative to theme assets root.
 * @return string Escaped-ready URI.
 */
function shpigovsky_asset_uri( $relative_path ) {
	return trailingslashit( SHPIGOVSKY_THEME_URI ) . 'assets/' . ltrim( $relative_path, '/' );
}

/**
 * Format a display phone from stored option text.
 *
 * @param string $phone Raw phone string.
 * @return string Display phone or empty.
 */
function shpigovsky_format_phone_display( $phone ) {
	$phone = trim( (string) $phone );

	return $phone;
}

/**
 * Build tel: href from phone option text.
 *
 * @param string $phone Raw phone string.
 * @return string tel URI or empty.
 */
function shpigovsky_phone_href( $phone ) {
	$digits = preg_replace( '/\D+/', '', (string) $phone );

	if ( '' === $digits ) {
		return '';
	}

	if ( 11 === strlen( $digits ) && '8' === $digits[0] ) {
		$digits = '7' . substr( $digits, 1 );
	}

	return 'tel:+' . $digits;
}

/**
 * Split multiline option text into non-empty lines.
 *
 * @param string $text Multiline text.
 * @return string[]
 */
function shpigovsky_split_option_lines( $text ) {
	$lines = preg_split( '/\r\n|\r|\n/', (string) $text );

	if ( ! is_array( $lines ) ) {
		return array();
	}

	return array_values(
		array_filter(
			array_map(
				static function ( $line ) {
					return trim( (string) $line );
				},
				$lines
			)
		)
	);
}

/**
 * Organisation / brand label for chrome.
 *
 * @return string
 */
function shpigovsky_brand_label() {
	$org = shpigovsky_get_site_option( 'organisation_name' );

	if ( '' !== $org ) {
		return $org;
	}

	return get_bloginfo( 'name', 'display' );
}

/**
 * Static V9 visual fallback messenger rows when social_links option is empty.
 *
 * D9-B: placeholder href="#" only — no operator URLs invented.
 *
 * @param string $context header|mobile-header|offcanvas.
 * @return array<int, array{label:string,url:string,icon:string}>
 */
function shpigovsky_get_messenger_visual_fallback_rows( $context = 'header' ) {
	$desktop = array(
		array(
			'label' => 'Telegram',
			'url'   => '#',
			'icon'  => 'telegram.svg',
		),
		array(
			'label' => 'WhatsApp',
			'url'   => '#',
			'icon'  => 'whatsapp.svg',
		),
		array(
			'label' => 'Max',
			'url'   => '#',
			'icon'  => 'max.svg',
		),
	);

	$mobile = array(
		array(
			'label' => 'Telegram',
			'url'   => '#',
			'icon'  => 'telegram.svg',
		),
		array(
			'label' => 'WhatsApp',
			'url'   => '#',
			'icon'  => 'whatsapp.svg',
		),
		array(
			'label' => 'Max',
			'url'   => '#',
			'icon'  => 'max.svg',
		),
	);

	if ( 'header' === $context ) {
		return $desktop;
	}

	return $mobile;
}

/**
 * Resolve messenger rows for chrome: configured options or static visual fallback.
 *
 * @param string $context header|mobile-header|offcanvas.
 * @return array<int, array{label:string,url:string,icon?:string,fallback?:bool}>
 */
function shpigovsky_get_messenger_link_rows( $context = 'header' ) {
	$rows = shpigovsky_get_social_link_rows();

	if ( ! empty( $rows ) ) {
		return $rows;
	}

	$fallback = shpigovsky_get_messenger_visual_fallback_rows( $context );

	foreach ( $fallback as $index => $row ) {
		$fallback[ $index ]['fallback'] = true;
	}

	return $fallback;
}

/**
 * Read configured social/messenger rows from site options.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_social_link_rows() {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$rows = get_field( 'social_links', 'option' );

	if ( ! is_array( $rows ) ) {
		return array();
	}

	$normalized = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$url   = isset( $row['url'] ) ? trim( (string) $row['url'] ) : '';
		$label = isset( $row['label'] ) ? trim( (string) $row['label'] ) : '';

		if ( '' === $url ) {
			continue;
		}

		$normalized[] = array(
			'label' => $label,
			'url'   => $url,
		);
	}

	return $normalized;
}

/**
 * Map a social label to a packaged icon filename when known.
 *
 * @param string $label Social label.
 * @return string Icon filename or empty for Font Awesome fallback.
 */
function shpigovsky_social_icon_for_label( $label ) {
	$key = mb_strtolower( trim( (string) $label ) );

	if ( str_contains( $key, 'telegram' ) ) {
		return 'telegram.svg';
	}

	if ( str_contains( $key, 'whatsapp' ) ) {
		return 'whatsapp.svg';
	}

	if ( 'max' === $key || str_contains( $key, 'max' ) ) {
		return 'max.svg';
	}

	if ( str_contains( $key, 'youtube' ) ) {
		return '';
	}

	return '';
}
