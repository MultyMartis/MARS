<?php
/**
 * Glossary helper functions (letter grouping, sorting).
 *
 * @package iseoblog
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Derive alphabet group key from a term title.
 *
 * @param string $title Term title.
 * @return string Group key such as "А", "B", or "0-9".
 */
function iseo_glossary_letter_from_title( $title ) {
	$title = trim( wp_strip_all_tags( (string) $title ) );
	if ( '' === $title ) {
		return '#';
	}

	$char = mb_substr( $title, 0, 1, 'UTF-8' );
	$char = mb_strtoupper( $char, 'UTF-8' );

	if ( 'Ё' === $char ) {
		return 'Ё';
	}

	if ( preg_match( '/^[А-Я]$/u', $char ) ) {
		return $char;
	}

	if ( preg_match( '/^[A-Z]$/', $char ) ) {
		return $char;
	}

	if ( preg_match( '/^[0-9]$/', $char ) ) {
		return '0-9';
	}

	return '#';
}

/**
 * Stable sort key for alphabet groups.
 *
 * @param string $letter Group key.
 * @return string
 */
function iseo_glossary_letter_sort_key( $letter ) {
	$cyr = array( 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я' );
	$lat = range( 'A', 'Z' );

	$pos = array_search( $letter, $cyr, true );
	if ( false !== $pos ) {
		return sprintf( '1-%02d', $pos );
	}

	$pos = array_search( $letter, $lat, true );
	if ( false !== $pos ) {
		return sprintf( '2-%02d', $pos );
	}

	if ( '0-9' === $letter ) {
		return '3-00';
	}

	return '4-00';
}

/**
 * Display label for a letter group.
 *
 * @param string $letter Group key.
 * @return string
 */
function iseo_glossary_letter_label( $letter ) {
	if ( '0-9' === $letter ) {
		return '0–9';
	}
	if ( '#' === $letter ) {
		return '#';
	}
	return $letter;
}

/**
 * Anchor id for a letter group.
 *
 * @param string $letter Group key.
 * @return string
 */
function iseo_glossary_letter_anchor( $letter ) {
	$map = array(
		'0-9' => '0-9',
		'#'   => 'other',
		'Ё'   => 'yo',
	);
	if ( isset( $map[ $letter ] ) ) {
		return 'glossary-letter-' . $map[ $letter ];
	}
	if ( preg_match( '/^[A-Z]$/', $letter ) ) {
		return 'glossary-letter-lat-' . strtolower( $letter );
	}
	// Cyrillic: use unicode codepoint for predictable ASCII-safe anchors.
	if ( function_exists( 'mb_ord' ) ) {
		return 'glossary-letter-u' . dechex( mb_ord( $letter, 'UTF-8' ) );
	}
	return 'glossary-letter-' . rawurlencode( $letter );
}

/**
 * Group posts by derived letter.
 *
 * @param WP_Post[] $posts Posts.
 * @return array<string, WP_Post[]>
 */
function iseo_glossary_group_posts_by_letter( $posts ) {
	$groups = array();
	foreach ( $posts as $post ) {
		$letter = iseo_glossary_letter_from_title( get_the_title( $post ) );
		if ( ! isset( $groups[ $letter ] ) ) {
			$groups[ $letter ] = array();
		}
		$groups[ $letter ][] = $post;
	}

	uksort(
		$groups,
		static function ( $a, $b ) {
			return strcmp( iseo_glossary_letter_sort_key( $a ), iseo_glossary_letter_sort_key( $b ) );
		}
	);

	foreach ( $groups as $letter => $items ) {
		usort(
			$items,
			static function ( $left, $right ) {
				return strnatcasecmp( get_the_title( $left ), get_the_title( $right ) );
			}
		);
		$groups[ $letter ] = $items;
	}

	return $groups;
}

/**
 * Optional archive search query string.
 *
 * @return string
 */
function iseo_glossary_search_query() {
	if ( empty( $_GET['glossary_q'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		return '';
	}
	return sanitize_text_field( wp_unslash( $_GET['glossary_q'] ) ); // phpcs:ignore WordPress.Security.NonceVerification.Recommended
}

/**
 * Filter posts by title/excerpt/search haystack.
 *
 * @param WP_Post[] $posts Posts.
 * @param string    $q     Query.
 * @return WP_Post[]
 */
function iseo_glossary_filter_posts( $posts, $q ) {
	$q = trim( (string) $q );
	if ( '' === $q ) {
		return $posts;
	}
	$needle = mb_strtolower( $q, 'UTF-8' );
	$out    = array();
	foreach ( $posts as $post ) {
		$hay = mb_strtolower( get_the_title( $post ) . ' ' . $post->post_excerpt, 'UTF-8' );
		if ( false !== mb_strpos( $hay, $needle, 0, 'UTF-8' ) ) {
			$out[] = $post;
		}
	}
	return $out;
}
