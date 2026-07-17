<?php
/**
 * Shared reviews helpers — V9-06D9-X admin-to-frontend binding repair.
 *
 * V9-06E62C: stable review_uid anchors (not repeater indices).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Generate a unique review UID in format review-xxxxxxxx.
 *
 * @param array<int, string> $existing Existing UIDs to avoid.
 * @return string
 */
function shpigovsky_generate_review_uid( array $existing = array() ) {
	$existing_map = array_fill_keys( array_map( 'strval', $existing ), true );

	for ( $i = 0; $i < 32; $i++ ) {
		$candidate = 'review-' . strtolower( substr( bin2hex( random_bytes( 4 ) ), 0, 8 ) );
		if ( ! isset( $existing_map[ $candidate ] ) ) {
			return $candidate;
		}
	}

	return 'review-' . strtolower( substr( md5( uniqid( (string) wp_rand(), true ) ), 0, 8 ) );
}

/**
 * Normalize / validate a stored review UID.
 *
 * @param string $uid Raw UID.
 * @return string Empty when invalid.
 */
function shpigovsky_sanitize_review_uid( $uid ) {
	$uid = strtolower( trim( (string) $uid ) );
	if ( preg_match( '/^review-[a-z0-9]{6,32}$/', $uid ) ) {
		return $uid;
	}
	return '';
}

/**
 * Static V9 fallback review items (same content as pre-D9-R home/reviews.php).
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_reviews_fallback_items() {
	return array(
		array(
			'author'  => 'Александр, Москва',
			'text'    => 'Обратились в&nbsp;центр в&nbsp;непростой период. С&nbsp;первого контакта чувствовалось уважительное отношение и&nbsp;спокойный тон общения. Персонал отвечал на&nbsp;вопросы без спешки и&nbsp;давления.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Мария, Московская область',
			'text'    => 'Для нас было важно, что в&nbsp;центре поддерживают спокойную обстановку. Пространство организовано аккуратно, без ощущения формального учреждения. Это помогло легче адаптироваться.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Елена, Москва',
			'text'    => 'Понравилось, что этапы сопровождения объясняли простым языком. Мы понимали, что происходит на&nbsp;каждом шаге, и&nbsp;могли спокойно планировать визиты и&nbsp;общение с&nbsp;специалистами.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Игорь, Московская область',
			'text'    => 'Семье было важно получать понятную обратную связь. Сотрудники центра поддерживали контакт, отвечали на&nbsp;звонки и&nbsp;помогали сохранять спокойствие в&nbsp;сложной ситуации.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Наталья, Москва',
			'text'    => 'Отметила внимательное отношение персонала к&nbsp;мелочам быта и&nbsp;режима. В&nbsp;центре создают условия, в&nbsp;которых проще сосредоточиться на&nbsp;восстановлении и&nbsp;ежедневных задачах.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Сергей, Московская область',
			'text'    => 'Комфортные условия проживания и&nbsp;чёткий распорядок помогли быстрее войти в&nbsp;рабочий ритм. Атмосфера в&nbsp;центре дружелюбная, без излишней официальности.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Анна, Москва',
			'text'    => 'Ценим деликатный подход к&nbsp;личной информации. Вопросы конфиденциальности обсуждали заранее, и&nbsp;это создало дополнительное чувство безопасности для всей семьи.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Дмитрий, Московская область',
			'text'    => 'Понравилась последовательность в&nbsp;организации помощи: от&nbsp;первичной консультации до&nbsp;ежедневного сопровождения. Команда работает согласованно и&nbsp;внимательно относится к&nbsp;запросам.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Ольга, Москва',
			'text'    => 'Сотрудники центра оперативно отвечали на&nbsp;вопросы и&nbsp;поддерживали контакт с&nbsp;родственниками. Такая обратная связь помогала чувствовать, что процесс под контролем.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
		array(
			'author'  => 'Михаил, Московская область',
			'text'    => 'В&nbsp;центре чувствуется человеческое отношение: специалисты говорят спокойно, слушают и&nbsp;не&nbsp;обесценивают переживания. Именно это для нас стало решающим при выборе.',
			'rating'  => 5,
			'context' => '',
			'source'  => '',
			'date'    => '',
		),
	);
}

/**
 * Canonical ACF options context for top-level Reviews admin.
 *
 * @return string
 */
function shpigovsky_get_reviews_options_context() {
	return 'fp02-reviews';
}

/**
 * Last resolved ACF options context used by reviews helpers (request-scoped).
 *
 * @return string Empty when unresolved.
 */
function shpigovsky_get_reviews_resolved_options_context() {
	return shpigovsky_reviews_options_context_state( 'get' );
}

/**
 * Remember which options context supplied review rows for this request.
 *
 * @param string $context ACF options context slug.
 * @return void
 */
function shpigovsky_set_reviews_resolved_options_context( $context ) {
	shpigovsky_reviews_options_context_state( 'set', $context );
}

/**
 * Request-scoped storage for resolved reviews options context.
 *
 * @param string      $action One of get|set.
 * @param string|null $value  Context slug when setting.
 * @return string
 */
function shpigovsky_reviews_options_context_state( $action, $value = null ) {
	static $resolved = '';

	if ( 'set' === $action && is_string( $value ) && '' !== $value ) {
		$resolved = $value;
	}

	return is_string( $resolved ) ? $resolved : '';
}

/**
 * Legacy generic options context retained for empty-canonical fallback only.
 *
 * @return string
 */
function shpigovsky_get_reviews_legacy_options_context() {
	return 'option';
}

/**
 * Ordered ACF options contexts for reviews reads.
 *
 * Canonical top-level Reviews admin (`fp02-reviews`) first; legacy `option`
 * second only when canonical has no usable rows.
 *
 * @return array<int, string>
 */
function shpigovsky_get_reviews_options_read_contexts() {
	return array(
		shpigovsky_get_reviews_options_context(),
		shpigovsky_get_reviews_legacy_options_context(),
	);
}

/**
 * Read a reviews options field from canonical context with generic fallback.
 *
 * @param string $field_name ACF field name.
 * @return mixed
 */
function shpigovsky_get_reviews_option_field( $field_name ) {
	if ( ! function_exists( 'get_field' ) ) {
		return null;
	}

	$contexts = shpigovsky_get_reviews_options_read_contexts();

	foreach ( $contexts as $context ) {
		$value = get_field( $field_name, $context );

		if ( null !== $value && '' !== $value ) {
			return $value;
		}
	}

	return null;
}

/**
 * Whether the shared reviews section should render.
 *
 * @return bool
 */
function shpigovsky_reviews_enabled() {
	if ( ! function_exists( 'get_field' ) ) {
		return true;
	}

	$value = shpigovsky_get_reviews_option_field( 'reviews_enabled' );

	if ( null === $value || '' === $value ) {
		return true;
	}

	return (bool) $value;
}

/**
 * Normalize a rating value to integer 1–5.
 *
 * @param mixed $rating Raw rating.
 * @return int
 */
function shpigovsky_normalize_review_rating( $rating ) {
	$rating = (int) $rating;

	if ( $rating < 1 ) {
		return 5;
	}

	if ( $rating > 5 ) {
		return 5;
	}

	return $rating;
}

/**
 * Pick the first non-empty string value from a row using candidate field names.
 *
 * @param array<string, mixed> $row        Raw ACF row.
 * @param array<int, string>   $candidates Candidate field names in priority order.
 * @return string
 */
function shpigovsky_pick_review_string_field( $row, $candidates ) {
	foreach ( $candidates as $key ) {
		if ( ! array_key_exists( $key, $row ) ) {
			continue;
		}

		$value = trim( (string) $row[ $key ] );

		if ( '' !== $value ) {
			return $value;
		}
	}

	return '';
}

/**
 * Pick a boolean review flag with canonical and legacy field fallbacks.
 *
 * @param array<string, mixed> $row        Raw ACF row.
 * @param array<int, string>   $candidates Candidate field names in priority order.
 * @param bool                 $default    Default when unset or empty.
 * @return bool
 */
function shpigovsky_pick_review_bool_field( $row, $candidates, $default = true ) {
	foreach ( $candidates as $key ) {
		if ( ! array_key_exists( $key, $row ) ) {
			continue;
		}

		$value = $row[ $key ];

		if ( '' === $value || null === $value ) {
			continue;
		}

		return (bool) $value;
	}

	return $default;
}

/**
 * Normalize one ACF options repeater row into render-ready review data.
 *
 * Supports canonical D9-R options subfields and legacy D9-S/page-reviews names.
 *
 * @param array<string, mixed> $row Raw ACF row.
 * @return array<string, mixed>|null
 */
function shpigovsky_normalize_review_row( $row ) {
	if ( ! is_array( $row ) ) {
		return null;
	}

	$author = shpigovsky_pick_review_string_field(
		$row,
		array( 'review_author', 'author_label', 'author' )
	);
	$text   = shpigovsky_pick_review_string_field(
		$row,
		array( 'review_text', 'text' )
	);

	if ( '' === $author && '' === $text ) {
		return null;
	}

	$visible = shpigovsky_pick_review_bool_field(
		$row,
		array( 'review_visible', 'visible' ),
		true
	);

	if ( ! $visible ) {
		return null;
	}

	$featured = shpigovsky_pick_review_bool_field(
		$row,
		array( 'review_featured', 'featured' ),
		true
	);

	$rating_raw = null;
	foreach ( array( 'review_rating', 'rating' ) as $rating_key ) {
		if ( array_key_exists( $rating_key, $row ) && '' !== $row[ $rating_key ] && null !== $row[ $rating_key ] ) {
			$rating_raw = $row[ $rating_key ];
			break;
		}
	}

	$service_data = shpigovsky_resolve_review_service_data( $row['review_service'] ?? null );
	$service_id   = 0;

	if ( isset( $row['review_service'] ) ) {
		if ( $row['review_service'] instanceof WP_Post ) {
			$service_id = (int) $row['review_service']->ID;
		} elseif ( is_numeric( $row['review_service'] ) ) {
			$service_id = (int) $row['review_service'];
		} elseif ( is_array( $row['review_service'] ) && isset( $row['review_service']['ID'] ) ) {
			$service_id = (int) $row['review_service']['ID'];
		}
	}

	$uid = shpigovsky_pick_review_string_field(
		$row,
		array( 'review_uid', 'review_key' )
	);

	return array(
		'author'       => $author,
		'text'         => $text,
		'context'      => '' !== $service_data['title'] ? $service_data['title'] : shpigovsky_pick_review_string_field(
			$row,
			array( 'review_context', 'metadata' )
		),
		'source'       => shpigovsky_pick_review_string_field(
			$row,
			array( 'review_source', 'source' )
		),
		'date'         => shpigovsky_pick_review_string_field(
			$row,
			array( 'review_date', 'date' )
		),
		'rating'       => shpigovsky_normalize_review_rating( null !== $rating_raw ? $rating_raw : 5 ),
		'service_href' => $service_data['url'],
		'service_id'   => $service_id,
		'featured'     => $featured,
		'visible'      => true,
		'is_demo'      => false,
		'review_uid'   => $uid,
		'review_id'    => 0,
	);
}

/**
 * Resolve service relationship data from an ACF post_object value.
 *
 * @param mixed $service Raw ACF value.
 * @return array{title:string,url:string}
 */
function shpigovsky_resolve_review_service_data( $service ) {
	$post_id = 0;

	if ( $service instanceof WP_Post ) {
		$post_id = (int) $service->ID;
	} elseif ( is_numeric( $service ) ) {
		$post_id = (int) $service;
	} elseif ( is_array( $service ) && isset( $service['ID'] ) ) {
		$post_id = (int) $service['ID'];
	}

	if ( $post_id <= 0 || 'service' !== get_post_type( $post_id ) ) {
		return array(
			'title' => '',
			'url'   => '',
		);
	}

	$url = get_permalink( $post_id );

	return array(
		'title' => get_the_title( $post_id ),
		'url'   => is_string( $url ) ? $url : '',
	);
}

/**
 * Read visible review rows from ACF Options.
 *
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_reviews_option_items() {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	shpigovsky_set_reviews_resolved_options_context( '' );

	foreach ( shpigovsky_get_reviews_options_read_contexts() as $context ) {
		$candidate = get_field( 'reviews_items', $context );

		if ( ! is_array( $candidate ) || empty( $candidate ) ) {
			continue;
		}

		$normalized = array();

		foreach ( $candidate as $raw_index => $row ) {
			$item = shpigovsky_normalize_review_row( $row );

			if ( null === $item ) {
				continue;
			}

			// Legacy 1-based index retained for diagnostics only (not used as public anchor).
			$item['review_id'] = (int) $raw_index + 1;
			$normalized[]      = $item;
		}

		if ( ! empty( $normalized ) ) {
			shpigovsky_set_reviews_resolved_options_context( $context );

			return $normalized;
		}
	}

	return array();
}

/**
 * Resolve shared reviews items with options precedence and static fallback.
 *
 * @param array<string, mixed> $args {
 *     Optional query args.
 *
 *     @type bool $featured_only Limit to featured rows when options exist.
 *     @type int  $limit         Max items; 0 = no limit.
 * }
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_reviews_items( $args = array() ) {
	$args = wp_parse_args(
		$args,
		array(
			'featured_only' => false,
			'limit'         => 0,
		)
	);

	$option_items = shpigovsky_get_reviews_option_items();

	if ( ! empty( $option_items ) ) {
		$items = $option_items;

		if ( ! empty( $args['featured_only'] ) ) {
			$items = array_values(
				array_filter(
					$items,
					static function ( $item ) {
						return ! empty( $item['featured'] );
					}
				)
			);
		}
	} else {
		$items = shpigovsky_get_reviews_fallback_items();

		foreach ( $items as $index => $item ) {
			$items[ $index ]['featured'] = true;
			$items[ $index ]['visible']  = true;
			$items[ $index ]['is_demo']  = true;
		}
	}

	$limit = (int) $args['limit'];

	if ( $limit > 0 ) {
		$items = array_slice( $items, 0, $limit );
	}

	return $items;
}

/**
 * Reviews archive posts-per-page setting.
 *
 * @return int
 */
function shpigovsky_get_reviews_per_page() {
	if ( ! function_exists( 'get_field' ) ) {
		return 10;
	}

	$value = (int) get_field( 'reviews_per_page', shpigovsky_get_reviews_options_context() );

	return $value > 0 ? $value : 10;
}

/**
 * Slice reviews for current archive page.
 *
 * @param array<int, array<string, mixed>> $items Review rows.
 * @return array{items:array<int,array<string,mixed>>,current:int,total:int,per_page:int,out_of_range:bool}
 */
function shpigovsky_paginate_reviews_items( $items ) {
	$per_page     = shpigovsky_get_reviews_per_page();
	$count        = count( $items );
	$total        = max( 1, (int) ceil( $count / $per_page ) );
	$requested    = max( 1, (int) get_query_var( 'paged', 1 ) );
	$out_of_range = $requested > $total;
	$current      = $out_of_range ? $total : $requested;
	$offset       = ( $current - 1 ) * $per_page;

	return array(
		'items'        => $out_of_range ? array() : array_slice( $items, $offset, $per_page ),
		'current'      => $current,
		'total'        => $total,
		'per_page'     => $per_page,
		'out_of_range' => $out_of_range,
	);
}

/**
 * Reviews archive page ID (`/otzyvy/`).
 *
 * @return int
 */
function shpigovsky_get_reviews_archive_page_id() {
	static $cached = null;

	if ( null !== $cached ) {
		return $cached;
	}

	$page = get_page_by_path( 'otzyvy' );

	if ( $page instanceof WP_Post ) {
		$cached = (int) $page->ID;
		return $cached;
	}

	$pages = get_posts(
		array(
			'post_type'              => 'page',
			'post_status'            => 'publish',
			'posts_per_page'         => 20,
			'meta_key'               => '_wp_page_template',
			'meta_value'             => 'page-templates/reviews.php',
			'no_found_rows'          => true,
			'update_post_meta_cache' => false,
			'update_post_term_cache' => false,
			'fields'                 => 'ids',
		)
	);

	$cached = ! empty( $pages ) ? (int) $pages[0] : 0;

	return $cached;
}

/**
 * Build archive URL for a review UID (stable across repeater reorder).
 *
 * Page number is computed from current row position + reviews_per_page.
 * Cached per request — no per-card DB queries.
 *
 * @param string $review_uid Stable review UID (review-xxxxxxxx).
 * @return string Absolute URL with #{review_uid}, or archive root when unknown.
 */
function shpigovsky_get_review_archive_url( $review_uid ) {
	static $map = null;

	$review_uid = shpigovsky_sanitize_review_uid( $review_uid );
	$page_id    = shpigovsky_get_reviews_archive_page_id();
	$base       = $page_id > 0 ? get_permalink( $page_id ) : home_url( '/otzyvy/' );

	if ( ! is_string( $base ) || '' === $base ) {
		$base = home_url( '/otzyvy/' );
	}

	$base = trailingslashit( $base );

	if ( null === $map ) {
		$map      = array();
		$items    = shpigovsky_get_reviews_items(
			array(
				'featured_only' => false,
				'limit'         => 0,
			)
		);
		$per_page = shpigovsky_get_reviews_per_page();

		foreach ( $items as $index => $item ) {
			$uid = shpigovsky_sanitize_review_uid( $item['review_uid'] ?? '' );
			if ( '' === $uid ) {
				continue;
			}
			$page_num     = (int) floor( $index / $per_page ) + 1;
			$map[ $uid ]  = $page_num;
		}
	}

	if ( '' === $review_uid || ! isset( $map[ $review_uid ] ) ) {
		return $base;
	}

	$page_num = (int) $map[ $review_uid ];
	$url      = $base;

	if ( $page_num > 1 ) {
		$url = $base . user_trailingslashit( 'page/' . $page_num, 'single' );
	}

	return $url . '#' . $review_uid;
}

/**
 * Ensure every reviews_items row has a unique persistent review_uid.
 *
 * Idempotent: existing valid UIDs are preserved; empty/invalid/duplicate get new IDs.
 *
 * @param string $context ACF options context.
 * @return array{updated:bool,assigned:int,preserved:int,rows:int}
 */
function shpigovsky_ensure_review_uids( $context = '' ) {
	if ( ! function_exists( 'get_field' ) || ! function_exists( 'update_field' ) ) {
		return array(
			'updated'    => false,
			'assigned'   => 0,
			'preserved'  => 0,
			'rows'       => 0,
		);
	}

	if ( '' === $context ) {
		$context = shpigovsky_get_reviews_options_context();
	}

	$rows = get_field( 'reviews_items', $context );
	if ( ! is_array( $rows ) ) {
		return array(
			'updated'    => false,
			'assigned'   => 0,
			'preserved'  => 0,
			'rows'       => 0,
		);
	}

	$seen      = array();
	$assigned  = 0;
	$preserved = 0;
	$changed   = false;

	foreach ( $rows as $index => $row ) {
		if ( ! is_array( $row ) ) {
			$row = array();
		}
		$uid = shpigovsky_sanitize_review_uid( $row['review_uid'] ?? '' );
		if ( '' === $uid || isset( $seen[ $uid ] ) ) {
			$uid      = shpigovsky_generate_review_uid( array_keys( $seen ) );
			$assigned++;
			$changed  = true;
		} else {
			$preserved++;
		}
		$seen[ $uid ]              = true;
		$rows[ $index ]            = $row;
		$rows[ $index ]['review_uid'] = $uid;
	}

	if ( $changed ) {
		update_field( 'reviews_items', $rows, $context );
	}

	return array(
		'updated'   => $changed,
		'assigned'  => $assigned,
		'preserved' => $preserved,
		'rows'      => count( $rows ),
	);
}

/**
 * Persist review_uid values when Reviews options are saved in admin.
 *
 * @param int|string $post_id ACF post/options id.
 * @return void
 */
function shpigovsky_reviews_save_ensure_uids( $post_id ) {
	if ( ! is_string( $post_id ) && ! is_numeric( $post_id ) ) {
		return;
	}

	$post_id = (string) $post_id;
	$contexts = array(
		shpigovsky_get_reviews_options_context(),
		'fp02-reviews',
		'option',
		'options',
	);

	$matched = false;
	foreach ( $contexts as $ctx ) {
		if ( $post_id === (string) $ctx || false !== strpos( $post_id, 'fp02-reviews' ) ) {
			$matched = true;
			break;
		}
	}

	if ( ! $matched && function_exists( 'acf_get_options_page' ) ) {
		// Options screen save for Reviews.
		if ( isset( $_POST['acf'] ) && is_array( $_POST['acf'] ) ) { // phpcs:ignore WordPress.Security.NonceVerification.Missing
			foreach ( array_keys( $_POST['acf'] ) as $key ) { // phpcs:ignore WordPress.Security.NonceVerification.Missing
				if ( false !== strpos( (string) $key, 'reviews_items' ) || 'field_fp02_options_reviews_items' === $key ) {
					$matched = true;
					break;
				}
			}
		}
	}

	if ( ! $matched ) {
		return;
	}

	shpigovsky_ensure_review_uids( shpigovsky_get_reviews_options_context() );
}
add_action( 'acf/save_post', 'shpigovsky_reviews_save_ensure_uids', 20 );

/**
 * Mark review_uid as read-only in admin UI.
 *
 * @param array<string,mixed>|false $field Field.
 * @return array<string,mixed>|false
 */
function shpigovsky_reviews_readonly_uid_field( $field ) {
	if ( ! is_array( $field ) ) {
		return $field;
	}
	$field['readonly'] = 1;
	$field['disabled'] = 0;
	return $field;
}
add_filter( 'acf/prepare_field/key=field_fp02_options_review_uid', 'shpigovsky_reviews_readonly_uid_field' );

/**
 * Force HTTP 404 when Reviews archive page is out of range.
 *
 * @return void
 */
function shpigovsky_reviews_out_of_range_404() {
	if ( is_admin() || wp_doing_ajax() ) {
		return;
	}

	if ( ! is_page_template( 'page-templates/reviews.php' ) ) {
		return;
	}

	$requested = max( 1, (int) get_query_var( 'paged', 1 ) );

	if ( $requested <= 1 ) {
		return;
	}

	$items = shpigovsky_get_reviews_items(
		array(
			'featured_only' => false,
			'limit'         => 0,
		)
	);
	$per_page = shpigovsky_get_reviews_per_page();
	$total    = max( 1, (int) ceil( count( $items ) / $per_page ) );

	if ( $requested <= $total ) {
		return;
	}

	global $wp_query;

	$wp_query->set_404();
	status_header( 404 );
	nocache_headers();
}
add_action( 'template_redirect', 'shpigovsky_reviews_out_of_range_404', 5 );

/**
 * Prevent redirect_canonical from collapsing out-of-range Reviews pages to page 1.
 *
 * @param string|false $redirect_url Redirect target.
 * @param string       $requested_url Requested URL.
 * @return string|false
 */
function shpigovsky_reviews_disable_canonical_redirect_when_out_of_range( $redirect_url, $requested_url ) {
	if ( is_admin() || ! is_string( $requested_url ) || '' === $requested_url ) {
		return $redirect_url;
	}

	if ( ! preg_match( '~/otzyvy/page/([0-9]+)/?(?:[?#]|$)~', $requested_url, $matches ) ) {
		return $redirect_url;
	}

	$requested = max( 1, (int) $matches[1] );

	if ( $requested <= 1 ) {
		return $redirect_url;
	}

	$items = shpigovsky_get_reviews_items(
		array(
			'featured_only' => false,
			'limit'         => 0,
		)
	);
	$per_page = shpigovsky_get_reviews_per_page();
	$total    = max( 1, (int) ceil( count( $items ) / $per_page ) );

	if ( $requested > $total ) {
		return false;
	}

	return $redirect_url;
}
add_filter( 'redirect_canonical', 'shpigovsky_reviews_disable_canonical_redirect_when_out_of_range', 10, 2 );

/**
 * Resolve shared reviews data source mode for validation and diagnostics.
 *
 * @return string OPTIONS|FALLBACK|DISABLED
 */
function shpigovsky_get_reviews_source_mode() {
	if ( ! shpigovsky_reviews_enabled() ) {
		return 'DISABLED';
	}

	$option_items = shpigovsky_get_reviews_option_items();

	if ( empty( $option_items ) ) {
		return 'FALLBACK';
	}

	if ( shpigovsky_get_reviews_options_context() === shpigovsky_get_reviews_resolved_options_context() ) {
		return 'OPTIONS';
	}

	if ( shpigovsky_get_reviews_legacy_options_context() === shpigovsky_get_reviews_resolved_options_context() ) {
		return 'OPTIONS';
	}

	return 'FALLBACK';
}

/**
 * Resolve shared reviews section heading.
 *
 * @param string $fallback Default heading when options and Home field are empty.
 * @return string
 */
function shpigovsky_get_reviews_heading( $fallback = 'Отзывы' ) {
	$option_heading = shpigovsky_get_reviews_option_field( 'reviews_section_heading' );

	if ( is_string( $option_heading ) && '' !== trim( $option_heading ) ) {
		return trim( $option_heading );
	}

	return shpigovsky_home_text_or_fallback( 'home_reviews_heading', $fallback );
}

/**
 * Format review date for archive card display.
 *
 * @param string $date Raw date string from options.
 * @return array{iso: string, formatted: string}
 */
function shpigovsky_format_review_archive_date( $date ) {
	$date = trim( (string) $date );

	if ( '' === $date ) {
		return array(
			'iso'       => '',
			'formatted' => '',
		);
	}

	if ( preg_match( '/^\d{4}-\d{2}-\d{2}$/', $date ) ) {
		$timestamp = strtotime( $date . ' 00:00:00' );

		return array(
			'iso'       => $date,
			'formatted' => false !== $timestamp ? gmdate( 'd.m.Y', $timestamp ) : $date,
		);
	}

	return array(
		'iso'       => '',
		'formatted' => $date,
	);
}

/**
 * Add V9 page body class on reviews template.
 *
 * @param string[] $classes Body classes.
 * @return string[]
 */
function shpigovsky_reviews_body_class( $classes ) {
	if ( is_page_template( 'page-templates/reviews.php' ) ) {
		$classes[] = 'page-otzyvy';
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_reviews_body_class' );
