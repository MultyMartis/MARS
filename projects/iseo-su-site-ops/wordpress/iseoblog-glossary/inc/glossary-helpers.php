<?php
/**
 * Glossary helper functions (archive query, letter grouping, sorting).
 *
 * @package iseoblog
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Post statuses visible on the glossary archive for the current viewer.
 *
 * Anonymous / public gate closed → publish only (archive still 404 via template_redirect).
 * Authorized editors → include drafts for preview without publishing.
 *
 * @return string[]
 */
function iseo_glossary_archive_post_statuses() {
	if ( current_user_can( 'edit_posts' ) ) {
		return array( 'publish', 'draft', 'pending', 'future', 'private' );
	}
	return array( 'publish' );
}

/**
 * Raw term title for grouping/display (avoids front-end title filters).
 *
 * @param WP_Post|int $post Post.
 * @return string
 */
function iseo_glossary_term_title( $post ) {
	$post = get_post( $post );
	if ( ! $post ) {
		return '';
	}
	return trim( wp_strip_all_tags( (string) $post->post_title ) );
}

/**
 * Safe list URL for a glossary term.
 *
 * Published + public exposure → permalink.
 * Draft/pending/etc. → preview link only when the viewer can edit that post.
 * Otherwise empty (title rendered without a public link).
 *
 * @param WP_Post|int $post Post.
 * @return string
 */
function iseo_glossary_term_list_url( $post ) {
	$post = get_post( $post );
	if ( ! $post ) {
		return '';
	}

	if ( 'publish' === $post->post_status && iseo_glossary_is_publicly_exposed() ) {
		$url = get_permalink( $post );
		return $url ? (string) $url : '';
	}

	if ( current_user_can( 'edit_post', $post->ID ) ) {
		$preview = get_preview_post_link( $post );
		return $preview ? (string) $preview : '';
	}

	return '';
}

/**
 * Load glossary archive posts via a dedicated query.
 *
 * The main WordPress archive query can report found_posts without hydrating
 * $wp_query->posts for mixed draft statuses on the front end. Do not rely on it.
 *
 * @return WP_Post[]
 */
function iseo_glossary_get_archive_posts() {
	$query = new WP_Query(
		array(
			'post_type'              => 'glossary',
			'post_status'            => iseo_glossary_archive_post_statuses(),
			'posts_per_page'         => -1,
			'orderby'                => 'title',
			'order'                  => 'ASC',
			'no_found_rows'          => true,
			'ignore_sticky_posts'    => true,
			'update_post_meta_cache' => false,
			'update_post_term_cache' => false,
		)
	);

	$posts = array();
	if ( ! empty( $query->posts ) && is_array( $query->posts ) ) {
		foreach ( $query->posts as $post ) {
			$post = get_post( $post );
			if ( ! $post instanceof WP_Post ) {
				continue;
			}
			if ( 'glossary' !== $post->post_type ) {
				continue;
			}
			if ( '' === iseo_glossary_term_title( $post ) ) {
				continue;
			}
			// Private posts stay capability-gated.
			if ( 'private' === $post->post_status && ! current_user_can( 'read_post', $post->ID ) ) {
				continue;
			}
			$posts[] = $post;
		}
	}

	return $posts;
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
		return '';
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
 * Group posts by derived letter. Empty titles and empty groups are omitted.
 *
 * @param WP_Post[] $posts Posts.
 * @return array<string, WP_Post[]>
 */
function iseo_glossary_group_posts_by_letter( $posts ) {
	$groups = array();
	foreach ( $posts as $post ) {
		if ( ! $post instanceof WP_Post ) {
			continue;
		}
		$title  = iseo_glossary_term_title( $post );
		$letter = iseo_glossary_letter_from_title( $title );
		if ( '' === $letter ) {
			continue;
		}
		if ( ! isset( $groups[ $letter ] ) ) {
			$groups[ $letter ] = array();
		}
		$groups[ $letter ][] = $post;
	}

	foreach ( $groups as $letter => $items ) {
		if ( empty( $items ) ) {
			unset( $groups[ $letter ] );
		}
	}

	if ( empty( $groups ) ) {
		return array();
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
				return strnatcasecmp( iseo_glossary_term_title( $left ), iseo_glossary_term_title( $right ) );
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
		if ( ! $post instanceof WP_Post ) {
			continue;
		}
		$syn = '';
		if ( function_exists( 'get_field' ) ) {
			$syn = (string) get_field( 'glossary_synonyms', $post->ID );
		} else {
			$syn = (string) get_post_meta( $post->ID, 'glossary_synonyms', true );
		}
		$hay = mb_strtolower(
			iseo_glossary_term_title( $post ) . ' ' . $post->post_excerpt . ' ' . $syn,
			'UTF-8'
		);
		if ( false !== mb_strpos( $hay, $needle, 0, 'UTF-8' ) ) {
			$out[] = $post;
		}
	}
	return $out;
}

/**
 * Normalize a glossary term label for map lookups.
 *
 * @param string $label Label.
 * @return string
 */
function iseo_glossary_normalize_label( $label ) {
	$label = html_entity_decode( wp_strip_all_tags( (string) $label ), ENT_QUOTES | ENT_HTML5, 'UTF-8' );
	$label = preg_replace( '/\s+/u', ' ', $label );
	$label = trim( mb_strtolower( (string) $label, 'UTF-8' ) );
	return $label;
}

/**
 * Split related-term textarea into unique labels.
 *
 * @param string $raw Raw field.
 * @return string[]
 */
function iseo_glossary_parse_related_labels( $raw ) {
	$raw = trim( (string) $raw );
	if ( '' === $raw ) {
		return array();
	}
	$parts = preg_split( '/[;\n]+/u', $raw );
	$out   = array();
	$seen  = array();
	foreach ( (array) $parts as $part ) {
		$label = trim( (string) $part );
		if ( '' === $label ) {
			continue;
		}
		$key = iseo_glossary_normalize_label( $label );
		if ( '' === $key || isset( $seen[ $key ] ) ) {
			continue;
		}
		$seen[ $key ] = true;
		$out[]        = $label;
	}
	return $out;
}

/**
 * Map of normalized published glossary titles → post objects (cached per request).
 *
 * @return array<string, WP_Post>
 */
function iseo_glossary_published_title_map() {
	static $map = null;
	if ( null !== $map ) {
		return $map;
	}

	$map   = array();
	$query = new WP_Query(
		array(
			'post_type'              => 'glossary',
			'post_status'            => 'publish',
			'posts_per_page'         => -1,
			'orderby'                => 'title',
			'order'                  => 'ASC',
			'no_found_rows'          => true,
			'ignore_sticky_posts'    => true,
			'update_post_meta_cache' => false,
			'update_post_term_cache' => false,
		)
	);

	if ( empty( $query->posts ) || ! is_array( $query->posts ) ) {
		return $map;
	}

	foreach ( $query->posts as $post ) {
		$post = get_post( $post );
		if ( ! $post instanceof WP_Post ) {
			continue;
		}
		$title = iseo_glossary_term_title( $post );
		$key   = iseo_glossary_normalize_label( $title );
		if ( '' === $key || isset( $map[ $key ] ) ) {
			continue;
		}
		$map[ $key ] = $post;
	}

	return $map;
}

/**
 * Resolve related-term labels for a glossary post into public link rows.
 * Only published + publicly exposed targets are linked.
 *
 * @param WP_Post|int $post Post.
 * @return array<int, array{label:string,url:string}>
 */
function iseo_glossary_get_related_public_links( $post ) {
	$post = get_post( $post );
	if ( ! $post instanceof WP_Post ) {
		return array();
	}

	$raw = '';
	if ( function_exists( 'get_field' ) ) {
		$raw = (string) get_field( 'glossary_related_terms', $post->ID );
	}
	if ( '' === trim( $raw ) ) {
		$raw = (string) get_post_meta( $post->ID, 'glossary_related_terms', true );
	}

	$labels = iseo_glossary_parse_related_labels( $raw );
	if ( empty( $labels ) ) {
		return array();
	}

	$self_key = iseo_glossary_normalize_label( iseo_glossary_term_title( $post ) );
	$map      = iseo_glossary_published_title_map();
	$links    = array();
	$seen     = array();

	foreach ( $labels as $label ) {
		$key = iseo_glossary_normalize_label( $label );
		if ( '' === $key || $key === $self_key || isset( $seen[ $key ] ) ) {
			continue;
		}
		if ( ! isset( $map[ $key ] ) ) {
			continue;
		}
		$target = $map[ $key ];
		$url    = iseo_glossary_term_list_url( $target );
		if ( '' === $url ) {
			continue;
		}
		$seen[ $key ] = true;
		$links[]      = array(
			'label' => iseo_glossary_term_title( $target ),
			'url'   => $url,
		);
	}

	return $links;
}
