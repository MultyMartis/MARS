<?php
/**
 * Frontend site search — V9-06E62E.
 *
 * Native WordPress search for the main frontend query only.
 * Included: post, page, service. Excludes attachments, private/password,
 * and known legal/system pages.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Post types included in frontend site search.
 *
 * @return string[]
 */
function shpigovsky_search_post_types() {
	$types = array( 'post', 'page' );

	if ( post_type_exists( 'service' ) ) {
		$types[] = 'service';
	}

	/**
	 * Filter searchable post types (frontend main search only).
	 *
	 * @param string[] $types Post types.
	 */
	return apply_filters( 'shpigovsky_search_post_types', $types );
}

/**
 * Results per page for frontend search.
 *
 * @return int
 */
function shpigovsky_search_posts_per_page() {
	return 12;
}

/**
 * Page IDs excluded from frontend search (legal / system utility pages).
 *
 * @return int[]
 */
function shpigovsky_search_excluded_page_ids() {
	$slugs = array(
		'user-agreement',
		'consent-personal-data',
		'cookie-files-policy',
		'privacy-policy',
	);

	$ids = array();

	foreach ( $slugs as $slug ) {
		$page = get_page_by_path( $slug );

		if ( $page instanceof WP_Post ) {
			$ids[] = (int) $page->ID;
		}
	}

	/**
	 * Filter excluded page IDs from frontend search.
	 *
	 * @param int[] $ids Page IDs.
	 */
	return array_values( array_unique( array_map( 'intval', apply_filters( 'shpigovsky_search_excluded_page_ids', $ids ) ) ) );
}

/**
 * Configure the main frontend search query.
 *
 * @param WP_Query $query Query.
 * @return void
 */
function shpigovsky_search_pre_get_posts( $query ) {
	if ( is_admin() || ! $query instanceof WP_Query || ! $query->is_main_query() || ! $query->is_search() ) {
		return;
	}

	$query->set( 'post_type', shpigovsky_search_post_types() );
	$query->set( 'posts_per_page', shpigovsky_search_posts_per_page() );
	$query->set( 'post_status', 'publish' );
	$query->set( 'ignore_sticky_posts', true );
	$query->set( 'has_password', false );

	$excluded = shpigovsky_search_excluded_page_ids();

	if ( ! empty( $excluded ) ) {
		$existing = $query->get( 'post__not_in' );
		$existing = is_array( $existing ) ? array_map( 'intval', $existing ) : array();
		$query->set( 'post__not_in', array_values( array_unique( array_merge( $existing, $excluded ) ) ) );
	}

	$raw = isset( $_GET['s'] ) ? wp_unslash( (string) $_GET['s'] ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
	$raw = is_string( $raw ) ? trim( $raw ) : '';

	if ( '' === $raw ) {
		// Empty query: keep is_search() but force zero results (no broken dump of all content).
		$query->set( 's', '' );
		$query->set( 'post__in', array( 0 ) );
	}
}
add_action( 'pre_get_posts', 'shpigovsky_search_pre_get_posts' );

/**
 * Russian content-type label for a search result.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_search_result_type_label( $post_id ) {
	$post_id = (int) $post_id;
	$type    = get_post_type( $post_id );

	if ( 'service' === $type ) {
		return __( 'Услуга', 'shpigovsky' );
	}

	if ( 'post' === $type ) {
		return __( 'Статья', 'shpigovsky' );
	}

	if ( 'page' === $type ) {
		$ancestors = get_post_ancestors( $post_id );
		$hub       = get_page_by_path( 'specyalisty' );

		if ( $hub instanceof WP_Post ) {
			$hub_id = (int) $hub->ID;

			if ( $post_id === $hub_id ) {
				return __( 'Страница', 'shpigovsky' );
			}

			if ( in_array( $hub_id, array_map( 'intval', $ancestors ), true ) || (int) get_post_field( 'post_parent', $post_id ) === $hub_id ) {
				return __( 'Специалист', 'shpigovsky' );
			}
		}

		return __( 'Страница', 'shpigovsky' );
	}

	return __( 'Страница', 'shpigovsky' );
}

/**
 * Build a clean excerpt for a search result (read-only; does not mutate stored content).
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_search_result_excerpt( $post_id ) {
	$post_id = (int) $post_id;
	$post    = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return '';
	}

	$text = '';

	if ( has_excerpt( $post_id ) ) {
		$text = (string) $post->post_excerpt;
	}

	if ( '' === trim( wp_strip_all_tags( $text ) ) ) {
		$short = '';

		if ( function_exists( 'get_field' ) ) {
			foreach ( array( 'treatment_program_short_description', 'generic_page_lead', 'service_intro_note', 'intro_note' ) as $field ) {
				$value = get_field( $field, $post_id );

				if ( is_string( $value ) && '' !== trim( wp_strip_all_tags( $value ) ) ) {
					$short = $value;
					break;
				}
			}
		}

		$text = '' !== $short ? $short : (string) $post->post_content;
	}

	$text = strip_shortcodes( $text );
	$text = preg_replace( '@<(script|style)[^>]*>.*?</\1>@si', '', $text );
	$text = preg_replace( '/<!--.*?-->/s', '', $text );
	$text = wp_strip_all_tags( (string) $text );
	$text = preg_replace( '/\s+/u', ' ', $text );
	$text = trim( (string) $text );

	if ( '' === $text ) {
		return '';
	}

	return wp_trim_words( $text, 36, '…' );
}

/**
 * Featured image URL for a search card, or empty string.
 *
 * @param int $post_id Post ID.
 * @return array{url:string,width:int,height:int,alt:string}|null
 */
function shpigovsky_search_result_image( $post_id ) {
	$post_id = (int) $post_id;

	if ( ! has_post_thumbnail( $post_id ) ) {
		return null;
	}

	$thumb_id = (int) get_post_thumbnail_id( $post_id );
	$src      = wp_get_attachment_image_src( $thumb_id, 'medium_large' );

	if ( ! is_array( $src ) || empty( $src[0] ) ) {
		return null;
	}

	$alt = get_post_meta( $thumb_id, '_wp_attachment_image_alt', true );
	$alt = is_string( $alt ) ? trim( $alt ) : '';

	if ( '' === $alt ) {
		$alt = get_the_title( $post_id );
	}

	return array(
		'url'    => (string) $src[0],
		'width'  => isset( $src[1] ) ? (int) $src[1] : 0,
		'height' => isset( $src[2] ) ? (int) $src[2] : 0,
		'alt'    => (string) $alt,
	);
}

/**
 * Human-readable found count line (Russian).
 *
 * @param int    $count Found posts.
 * @param string $query Search query.
 * @return string
 */
function shpigovsky_search_found_summary( $count, $query ) {
	$count = max( 0, (int) $count );
	$query = trim( (string) $query );

	if ( '' === $query ) {
		return __( 'Введите поисковый запрос', 'shpigovsky' );
	}

	$mod10  = $count % 10;
	$mod100 = $count % 100;

	if ( 1 === $mod10 && 11 !== $mod100 ) {
		$word = __( 'результат', 'shpigovsky' );
	} elseif ( $mod10 >= 2 && $mod10 <= 4 && ( $mod100 < 12 || $mod100 > 14 ) ) {
		$word = __( 'результата', 'shpigovsky' );
	} else {
		$word = __( 'результатов', 'shpigovsky' );
	}

	return sprintf(
		/* translators: 1: search query, 2: count, 3: result word */
		__( 'По запросу «%1$s» найдено: %2$d %3$s', 'shpigovsky' ),
		$query,
		$count,
		$word
	);
}

/**
 * Breadcrumb trail for search results.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_search_breadcrumb_trail() {
	return array(
		array(
			'label' => __( 'Главная', 'shpigovsky' ),
			'url'   => home_url( '/' ),
		),
		array(
			'label' => __( 'Результаты поиска', 'shpigovsky' ),
			'url'   => '',
		),
	);
}

/**
 * Whether theme should own search SEO meta (no dedicated SEO plugin).
 *
 * @return bool
 */
function shpigovsky_seo_is_search_results() {
	return is_search() && ! is_admin();
}

/**
 * Prefer noindex,follow on search result pages.
 *
 * @param array<string, string|bool> $robots Robots directives.
 * @return array<string, string|bool>
 */
function shpigovsky_search_wp_robots( $robots ) {
	if ( ! shpigovsky_seo_is_search_results() ) {
		return $robots;
	}

	if ( defined( 'WPSEO_VERSION' ) || defined( 'RANK_MATH_VERSION' ) || defined( 'AIOSEO_VERSION' ) ) {
		return $robots;
	}

	$robots['noindex'] = true;
	$robots['follow']  = true;
	unset( $robots['nofollow'] );

	return $robots;
}
add_filter( 'wp_robots', 'shpigovsky_search_wp_robots', 20 );

/**
 * Document title for search: include query and page number.
 *
 * @param array<string, string> $parts Title parts.
 * @return array<string, string>
 */
function shpigovsky_search_document_title_parts( $parts ) {
	if ( ! shpigovsky_seo_is_search_results() ) {
		return $parts;
	}

	$query = trim( (string) get_search_query( false ) );

	if ( '' !== $query ) {
		$parts['title'] = sprintf(
			/* translators: %s: search query */
			__( 'Результаты поиска: %s', 'shpigovsky' ),
			$query
		);
	} else {
		$parts['title'] = __( 'Результаты поиска', 'shpigovsky' );
	}

	$paged = (int) get_query_var( 'paged' );

	if ( $paged < 1 ) {
		$paged = (int) get_query_var( 'page' );
	}

	if ( $paged > 1 ) {
		$parts['page'] = sprintf(
			/* translators: %d: page number */
			__( 'Страница %d', 'shpigovsky' ),
			$paged
		);
	}

	return $parts;
}
add_filter( 'document_title_parts', 'shpigovsky_search_document_title_parts', 25 );

/**
 * Remove core canonical on search to avoid pointing at Home / unrelated URLs.
 *
 * @return void
 */
function shpigovsky_search_remove_core_canonical() {
	if ( ! shpigovsky_seo_is_search_results() ) {
		return;
	}

	if ( defined( 'WPSEO_VERSION' ) || defined( 'RANK_MATH_VERSION' ) || defined( 'AIOSEO_VERSION' ) ) {
		return;
	}

	remove_action( 'wp_head', 'rel_canonical' );
}
add_action( 'wp', 'shpigovsky_search_remove_core_canonical', 20 );
