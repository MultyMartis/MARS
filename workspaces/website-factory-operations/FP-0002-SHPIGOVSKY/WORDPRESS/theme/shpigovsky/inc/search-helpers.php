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

	if ( 'specialist' === $type ) {
		return __( 'Специалист', 'shpigovsky' );
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

/**
 * UTF-8-safe string length for smart-search threshold.
 *
 * @param string $text Text.
 * @return int
 */
function shpigovsky_smart_search_strlen( $text ) {
	$text = (string) $text;

	if ( function_exists( 'mb_strlen' ) ) {
		return (int) mb_strlen( $text, 'UTF-8' );
	}

	if ( preg_match_all( '/./u', $text, $matches ) ) {
		return count( $matches[0] );
	}

	return strlen( $text );
}

/**
 * UTF-8-safe lowercase.
 *
 * @param string $text Text.
 * @return string
 */
function shpigovsky_smart_search_lower( $text ) {
	$text = (string) $text;
	// Normalize NBSP so render-time typography cannot break query matching.
	$text = str_replace( array( "\xC2\xA0", '&nbsp;', '&#160;', '&#xA0;', '&#xa0;' ), ' ', $text );

	if ( function_exists( 'mb_strtolower' ) ) {
		return (string) mb_strtolower( $text, 'UTF-8' );
	}

	return strtolower( $text );
}

/**
 * Whether haystack contains needle (UTF-8).
 *
 * @param string $haystack Haystack.
 * @param string $needle   Needle.
 * @return bool
 */
function shpigovsky_smart_search_contains( $haystack, $needle ) {
	$haystack = shpigovsky_smart_search_lower( $haystack );
	$needle   = shpigovsky_smart_search_lower( $needle );

	if ( '' === $needle ) {
		return false;
	}

	if ( function_exists( 'mb_strpos' ) ) {
		return false !== mb_strpos( $haystack, $needle, 0, 'UTF-8' );
	}

	return false !== strpos( $haystack, $needle );
}

/**
 * Whether haystack starts with needle (UTF-8).
 *
 * @param string $haystack Haystack.
 * @param string $needle   Needle.
 * @return bool
 */
function shpigovsky_smart_search_starts_with( $haystack, $needle ) {
	$haystack = shpigovsky_smart_search_lower( $haystack );
	$needle   = shpigovsky_smart_search_lower( $needle );

	if ( '' === $needle ) {
		return false;
	}

	if ( function_exists( 'mb_strpos' ) ) {
		return 0 === mb_strpos( $haystack, $needle, 0, 'UTF-8' );
	}

	return 0 === strpos( $haystack, $needle );
}

/**
 * Smart-search group key for a published post (mutually exclusive).
 *
 * @param int $post_id Post ID.
 * @return string One of: services|articles|specialists|pages|''
 */
function shpigovsky_smart_search_group_key( $post_id ) {
	$post_id = (int) $post_id;
	$type    = get_post_type( $post_id );

	if ( 'service' === $type ) {
		return 'services';
	}

	if ( 'post' === $type ) {
		return 'articles';
	}

	if ( 'specialist' === $type ) {
		return 'specialists';
	}

	if ( 'page' !== $type ) {
		return '';
	}

	$excluded = shpigovsky_search_excluded_page_ids();

	if ( in_array( $post_id, $excluded, true ) ) {
		return '';
	}

	$hub = get_page_by_path( 'specyalisty' );

	if ( $hub instanceof WP_Post ) {
		$hub_id = (int) $hub->ID;

		if ( $post_id === $hub_id ) {
			return 'pages';
		}

		// Legacy child-page specialists (pre-P11 / rollback only).
		$ancestors = array_map( 'intval', (array) get_post_ancestors( $post_id ) );
		$parent    = (int) get_post_field( 'post_parent', $post_id );

		if ( in_array( $hub_id, $ancestors, true ) || $parent === $hub_id ) {
			return 'specialists';
		}
	}

	return 'pages';
}

/**
 * Plain searchable text for ranking (public fields only; no private meta dump).
 *
 * @param WP_Post $post Post.
 * @return array{excerpt:string,body:string,extra:string}
 */
function shpigovsky_smart_search_rank_texts( WP_Post $post ) {
	$excerpt = '';
	$body    = '';
	$extra   = '';

	if ( has_excerpt( $post ) ) {
		$excerpt = wp_strip_all_tags( (string) $post->post_excerpt );
	}

	$body = wp_strip_all_tags( strip_shortcodes( (string) $post->post_content ) );

	if ( function_exists( 'get_field' ) ) {
		if ( 'service' === $post->post_type ) {
			foreach ( array( 'treatment_program_short_description', 'service_intro_note', 'intro_note' ) as $field ) {
				$value = get_field( $field, $post->ID );
				if ( is_string( $value ) && '' !== trim( wp_strip_all_tags( $value ) ) ) {
					$extra .= ' ' . wp_strip_all_tags( $value );
				}
			}
		}

		if ( 'specialist' === $post->post_type || ( 'page' === $post->post_type && 'specialists' === shpigovsky_smart_search_group_key( (int) $post->ID ) ) ) {
			foreach ( array( 'specialist_role', 'specialist_specialty', 'specialist_specialization' ) as $field ) {
				$value = get_field( $field, $post->ID );
				if ( is_string( $value ) && '' !== trim( wp_strip_all_tags( $value ) ) ) {
					$extra .= ' ' . wp_strip_all_tags( $value );
				}
			}
		}

		if ( 'page' === $post->post_type ) {
			$lead = get_field( 'generic_page_lead', $post->ID );
			if ( is_string( $lead ) && '' !== trim( wp_strip_all_tags( $lead ) ) ) {
				$extra .= ' ' . wp_strip_all_tags( $lead );
			}
		}
	}

	$excerpt = trim( preg_replace( '/\s+/u', ' ', $excerpt ) );
	$body    = trim( preg_replace( '/\s+/u', ' ', $body ) );
	$extra   = trim( preg_replace( '/\s+/u', ' ', $extra ) );

	return array(
		'excerpt' => $excerpt,
		'body'    => $body,
		'extra'   => $extra,
	);
}

/**
 * Deterministic relevance score (higher = better).
 *
 * Tiers: exact title 100, title starts 80, title contains 60,
 * excerpt/extra 40, body 20.
 *
 * @param WP_Post $post  Post.
 * @param string  $query Normalized query.
 * @return int
 */
function shpigovsky_smart_search_score( WP_Post $post, $query ) {
	$query = trim( (string) $query );
	$title = (string) get_the_title( $post );

	if ( '' === $query || '' === $title ) {
		return 0;
	}

	$title_l = shpigovsky_smart_search_lower( $title );
	$query_l = shpigovsky_smart_search_lower( $query );

	if ( $title_l === $query_l ) {
		return 100;
	}

	if ( shpigovsky_smart_search_starts_with( $title, $query ) ) {
		return 80;
	}

	if ( shpigovsky_smart_search_contains( $title, $query ) ) {
		return 60;
	}

	$settings = function_exists( 'shpigovsky_smart_search_settings' ) ? shpigovsky_smart_search_settings() : array(
		'match_excerpt' => true,
		'match_body'    => true,
	);
	$texts    = shpigovsky_smart_search_rank_texts( $post );

	if ( ! empty( $settings['match_excerpt'] ) ) {
		if (
			( '' !== $texts['excerpt'] && shpigovsky_smart_search_contains( $texts['excerpt'], $query ) )
			|| ( '' !== $texts['extra'] && shpigovsky_smart_search_contains( $texts['extra'], $query ) )
		) {
			return 40;
		}
	}

	if ( ! empty( $settings['match_body'] ) && '' !== $texts['body'] && shpigovsky_smart_search_contains( $texts['body'], $query ) ) {
		return 20;
	}

	return 0;
}

/**
 * Short public snippet for a suggestion card.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_smart_search_snippet( $post_id ) {
	$excerpt = shpigovsky_search_result_excerpt( (int) $post_id );

	if ( '' === $excerpt ) {
		return '';
	}

	return wp_trim_words( $excerpt, 18, '…' );
}

/**
 * Build one suggestion payload item.
 *
 * @param WP_Post $post  Post.
 * @param string  $group Group key.
 * @param int     $score Score.
 * @return array{id:int,group:string,title:string,url:string,snippet:string,score:int}
 */
function shpigovsky_smart_search_item( WP_Post $post, $group, $score ) {
	return array(
		'id'      => (int) $post->ID,
		'group'   => (string) $group,
		'title'   => wp_strip_all_tags( get_the_title( $post ) ),
		'url'     => (string) get_permalink( $post ),
		'snippet' => shpigovsky_smart_search_snippet( (int) $post->ID ),
		'score'   => (int) $score,
	);
}

/**
 * Collect and rank candidates for one post type, then filter by group key.
 *
 * @param string $query     Query.
 * @param string $post_type Post type.
 * @param string $group     Expected group key.
 * @param int    $limit     Max results for this group.
 * @return array<int, array{id:int,group:string,title:string,url:string,snippet:string,score:int}>
 */
function shpigovsky_smart_search_collect_group( $query, $post_type, $group, $limit = 5 ) {
	if ( 'service' === $post_type && ! post_type_exists( 'service' ) ) {
		return array();
	}

	if ( 'specialist' === $post_type && ! post_type_exists( 'specialist' ) ) {
		return array();
	}

	$settings = function_exists( 'shpigovsky_smart_search_settings' ) ? shpigovsky_smart_search_settings() : array(
		'per_group'   => 5,
		'exclude_ids' => array(),
	);

	$limit = isset( $settings['per_group'] ) ? (int) $settings['per_group'] : (int) $limit;
	$limit = max( 1, min( 20, $limit ) );

	$exclude = shpigovsky_search_excluded_page_ids();
	if ( ! empty( $settings['exclude_ids'] ) && is_array( $settings['exclude_ids'] ) ) {
		$exclude = array_merge( $exclude, array_map( 'intval', $settings['exclude_ids'] ) );
	}
	$exclude = array_values( array_unique( array_filter( $exclude ) ) );

	$args = array(
		'post_type'              => $post_type,
		'post_status'            => 'publish',
		's'                      => $query,
		'posts_per_page'         => 40,
		'ignore_sticky_posts'    => true,
		'has_password'           => false,
		'no_found_rows'          => true,
		'update_post_meta_cache' => false,
		'update_post_term_cache' => false,
	);

	if ( ! empty( $exclude ) ) {
		$args['post__not_in'] = $exclude;
	}

	$q      = new WP_Query( $args );
	$scored = array();

	foreach ( (array) $q->posts as $post ) {
		if ( ! $post instanceof WP_Post ) {
			continue;
		}

		$item_group = shpigovsky_smart_search_group_key( (int) $post->ID );

		if ( $item_group !== $group ) {
			continue;
		}

		$score = shpigovsky_smart_search_score( $post, $query );

		if ( $score < 1 ) {
			continue;
		}

		$scored[] = shpigovsky_smart_search_item( $post, $group, $score );
	}

	wp_reset_postdata();

	usort(
		$scored,
		static function ( $a, $b ) {
			if ( $a['score'] === $b['score'] ) {
				return $a['id'] <=> $b['id'];
			}

			return $b['score'] <=> $a['score'];
		}
	);

	return array_slice( $scored, 0, $limit );
}

/**
 * Register public read-only smart-search REST route.
 *
 * @return void
 */
function shpigovsky_smart_search_register_rest_route() {
	register_rest_route(
		'shpigovsky/v1',
		'/smart-search',
		array(
			'methods'             => WP_REST_Server::READABLE,
			'callback'            => 'shpigovsky_smart_search_rest_callback',
			'permission_callback' => '__return_true',
			'args'                => array(
				'q' => array(
					'required'          => false,
					'type'              => 'string',
					'default'           => '',
					'sanitize_callback' => static function ( $value ) {
						$value = is_string( $value ) ? $value : '';
						$value = wp_unslash( $value );
						$value = sanitize_text_field( $value );
						return trim( $value );
					},
				),
			),
		)
	);
}
add_action( 'rest_api_init', 'shpigovsky_smart_search_register_rest_route' );

/**
 * REST callback for live search suggestions.
 *
 * @param WP_REST_Request $request Request.
 * @return WP_REST_Response
 */
function shpigovsky_smart_search_rest_callback( WP_REST_Request $request ) {
	$query = (string) $request->get_param( 'q' );
	$query = trim( sanitize_text_field( $query ) );

	$settings = function_exists( 'shpigovsky_smart_search_settings' ) ? shpigovsky_smart_search_settings() : array(
		'min_chars' => 3,
		'per_group' => 5,
		'enabled'   => array(
			'services'    => true,
			'articles'    => true,
			'specialists' => true,
			'pages'       => true,
		),
		'order'     => array( 'services', 'articles', 'specialists', 'pages' ),
	);

	$min = isset( $settings['min_chars'] ) ? (int) $settings['min_chars'] : 3;
	$min = max( 2, min( 10, $min ) );

	$order = isset( $settings['order'] ) && is_array( $settings['order'] )
		? $settings['order']
		: array( 'services', 'articles', 'specialists', 'pages' );

	$enabled = isset( $settings['enabled'] ) && is_array( $settings['enabled'] )
		? $settings['enabled']
		: array();

	$groups_payload = array(
		'services'    => array(),
		'articles'    => array(),
		'specialists' => array(),
		'pages'       => array(),
	);

	$response = array(
		'q'      => $query,
		'groups' => $groups_payload,
		'empty'  => true,
		'min'    => $min,
		'order'  => array_values( $order ),
	);

	if ( shpigovsky_smart_search_strlen( $query ) < $min ) {
		return new WP_REST_Response( $response, 200 );
	}

	$map = array(
		'services'    => array( 'service', 'services' ),
		'articles'    => array( 'post', 'articles' ),
		'specialists' => array( post_type_exists( 'specialist' ) ? 'specialist' : 'page', 'specialists' ),
		'pages'       => array( 'page', 'pages' ),
	);

	$groups = $groups_payload;
	$limit  = isset( $settings['per_group'] ) ? (int) $settings['per_group'] : 5;

	foreach ( $order as $key ) {
		if ( empty( $enabled[ $key ] ) || ! isset( $map[ $key ] ) ) {
			continue;
		}

		if ( 'specialists' === $key && post_type_exists( 'specialist' ) ) {
			$cpt_items = shpigovsky_smart_search_collect_group( $query, 'specialist', 'specialists', $limit );
			if ( ! empty( $cpt_items ) ) {
				$groups[ $key ] = $cpt_items;
				continue;
			}
			// Pre-migration / rollback: fall back to legacy page children classification.
			$groups[ $key ] = shpigovsky_smart_search_collect_group( $query, 'page', 'specialists', $limit );
			continue;
		}

		$groups[ $key ] = shpigovsky_smart_search_collect_group(
			$query,
			$map[ $key ][0],
			$map[ $key ][1],
			$limit
		);
	}

	// Strip internal score from public payload; keep order.
	foreach ( $groups as $key => $items ) {
		$clean = array();
		$seen  = array();

		foreach ( $items as $item ) {
			$id = (int) $item['id'];

			if ( isset( $seen[ $id ] ) ) {
				continue;
			}

			$seen[ $id ] = true;
			unset( $item['score'] );
			$clean[] = $item;
		}

		$groups[ $key ] = $clean;
	}

	$response['groups'] = $groups;
	$response['empty']  = (
		empty( $groups['services'] )
		&& empty( $groups['articles'] )
		&& empty( $groups['specialists'] )
		&& empty( $groups['pages'] )
	);

	return new WP_REST_Response( $response, 200 );
}
