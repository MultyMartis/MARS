<?php
/**
 * Shared reviews helpers — V9-06D9-X admin-to-frontend binding repair.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
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

	return array(
		'author'   => $author,
		'text'     => $text,
		'context'  => shpigovsky_pick_review_string_field(
			$row,
			array( 'review_context', 'metadata' )
		),
		'source'   => shpigovsky_pick_review_string_field(
			$row,
			array( 'review_source', 'source' )
		),
		'date'     => shpigovsky_pick_review_string_field(
			$row,
			array( 'review_date', 'date' )
		),
		'rating'   => shpigovsky_normalize_review_rating( null !== $rating_raw ? $rating_raw : 5 ),
		'featured' => $featured,
		'visible'  => true,
		'is_demo'  => false,
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

		foreach ( $candidate as $row ) {
			$item = shpigovsky_normalize_review_row( $row );

			if ( null !== $item ) {
				$normalized[] = $item;
			}
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
