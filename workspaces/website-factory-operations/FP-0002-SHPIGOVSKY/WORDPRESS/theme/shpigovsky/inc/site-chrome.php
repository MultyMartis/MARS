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
 * Static V9 visual fallback messenger rows — retired in P13.
 * Empty configuration must not invent placeholder URLs.
 *
 * @param string $context Context.
 * @return array<int, array{label:string,url:string,icon:string,type:string}>
 */
function shpigovsky_get_messenger_visual_fallback_rows( $context = 'header' ) {
	unset( $context );
	return array();
}

/**
 * Resolve messenger rows for chrome from the canonical social_platforms settings.
 *
 * @param string $context header|mobile-header|offcanvas|footer|contacts.
 * @return array<int, array{label:string,url:string,icon:string,type:string}>
 */
function shpigovsky_get_messenger_link_rows( $context = 'header' ) {
	$surface = 'header';
	if ( 'footer' === $context ) {
		$surface = 'footer';
	} elseif ( 'contacts' === $context ) {
		$surface = 'contacts';
	}

	return shpigovsky_get_social_platform_rows( $surface );
}

/**
 * Canonical social/messenger rows.
 *
 * Contacts: every configured platform with a URL.
 * Header (incl. floating + offcanvas): show_header.
 * Footer: show_footer.
 *
 * @param string $surface header|footer|contacts.
 * @return array<int, array{label:string,url:string,icon:string,type:string,show_header:bool,show_footer:bool}>
 */
function shpigovsky_get_social_platform_rows( $surface = 'header' ) {
	$rows = array();

	if ( function_exists( 'get_field' ) ) {
		$raw = get_field( 'social_platforms', 'option' );
		if ( is_array( $raw ) ) {
			foreach ( $raw as $row ) {
				$normalized = shpigovsky_normalize_social_platform_row( $row );
				if ( null === $normalized ) {
					continue;
				}
				$rows[] = $normalized;
			}
		}
	}

	if ( empty( $rows ) ) {
		foreach ( shpigovsky_get_legacy_social_link_rows() as $legacy ) {
			$normalized = shpigovsky_normalize_social_platform_row(
				array(
					'type'        => shpigovsky_infer_social_platform_type( $legacy['label'], $legacy['url'] ),
					'url'         => $legacy['url'],
					'show_header' => 1,
					'show_footer' => 1,
				)
			);
			if ( null !== $normalized ) {
				$rows[] = $normalized;
			}
		}
	}

	$out = array();
	foreach ( $rows as $row ) {
		if ( 'contacts' === $surface ) {
			$out[] = $row;
			continue;
		}
		if ( 'footer' === $surface && ! empty( $row['show_footer'] ) ) {
			$out[] = $row;
			continue;
		}
		if ( 'header' === $surface && ! empty( $row['show_header'] ) ) {
			$out[] = $row;
		}
	}

	return $out;
}

/**
 * Legacy social_links repeater (pre-P13). Used only as fallback if new field empty.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_legacy_social_link_rows() {
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
		if ( '' === $url || '#' === $url ) {
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
 * Read configured social/messenger rows from site options (canonical).
 *
 * @return array<int, array{label:string,url:string,icon?:string,type?:string}>
 */
function shpigovsky_get_social_link_rows() {
	return shpigovsky_get_social_platform_rows( 'footer' );
}

/**
 * Normalize one platform row.
 *
 * @param mixed $row Raw row.
 * @return array{label:string,url:string,icon:string,type:string,show_header:bool,show_footer:bool}|null
 */
function shpigovsky_normalize_social_platform_row( $row ) {
	if ( ! is_array( $row ) ) {
		return null;
	}

	$url  = isset( $row['url'] ) ? trim( (string) $row['url'] ) : '';
	$type = isset( $row['type'] ) ? sanitize_key( (string) $row['type'] ) : '';
	if ( '' === $type ) {
		$type = shpigovsky_infer_social_platform_type( isset( $row['label'] ) ? (string) $row['label'] : '', $url );
	}

	$catalog = shpigovsky_social_platform_catalog();
	if ( '' === $url || '#' === $url || ! isset( $catalog[ $type ] ) ) {
		return null;
	}

	$meta = $catalog[ $type ];

	return array(
		'type'        => $type,
		'label'       => $meta['label'],
		'url'         => $url,
		'icon'        => $meta['icon'],
		'show_header' => ! empty( $row['show_header'] ),
		'show_footer' => ! empty( $row['show_footer'] ),
	);
}

/**
 * Known platforms that already have theme icons.
 *
 * @return array<string, array{label:string,icon:string}>
 */
function shpigovsky_social_platform_catalog() {
	return array(
		'telegram' => array(
			'label' => 'Telegram',
			'icon'  => 'telegram.svg',
		),
		'whatsapp' => array(
			'label' => 'WhatsApp',
			'icon'  => 'whatsapp.svg',
		),
		'max'      => array(
			'label' => 'MAX',
			'icon'  => 'max.svg',
		),
		'youtube'  => array(
			'label' => 'YouTube',
			'icon'  => '',
		),
	);
}

/**
 * Infer platform type from label/URL.
 *
 * @param string $label Label.
 * @param string $url   URL.
 * @return string
 */
function shpigovsky_infer_social_platform_type( $label, $url ) {
	$hay = mb_strtolower( trim( $label . ' ' . $url ) );
	if ( str_contains( $hay, 't.me' ) || str_contains( $hay, 'telegram' ) ) {
		return 'telegram';
	}
	if ( str_contains( $hay, 'wa.me' ) || str_contains( $hay, 'whatsapp' ) || str_contains( $hay, 'what\'s up' ) || str_contains( $hay, 'whats up' ) ) {
		return 'whatsapp';
	}
	if ( str_contains( $hay, 'youtu' ) ) {
		return 'youtube';
	}
	if ( str_contains( $hay, 'max.ru' ) || preg_match( '/(^|[^a-zа-я])max([^a-zа-я]|$)/u', $hay ) ) {
		return 'max';
	}
	return '';
}

/**
 * Map a social label to a packaged icon filename when known.
 *
 * @param string $label Social label.
 * @return string Icon filename or empty for Font Awesome fallback.
 */
function shpigovsky_social_icon_for_label( $label ) {
	$type = shpigovsky_infer_social_platform_type( (string) $label, '' );
	$catalog = shpigovsky_social_platform_catalog();
	if ( isset( $catalog[ $type ] ) ) {
		return $catalog[ $type ]['icon'];
	}
	return '';
}
