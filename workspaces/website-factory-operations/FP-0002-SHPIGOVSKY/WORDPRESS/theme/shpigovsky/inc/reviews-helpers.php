<?php
/**
 * Shared reviews helpers — V9-06D9-R ACF Options + static V9 fallback.
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
 * Whether the shared reviews section should render.
 *
 * @return bool
 */
function shpigovsky_reviews_enabled() {
	if ( ! function_exists( 'get_field' ) ) {
		return true;
	}

	$value = get_field( 'reviews_enabled', 'option' );

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
 * Normalize one ACF options repeater row into render-ready review data.
 *
 * @param array<string, mixed> $row Raw ACF row.
 * @return array<string, mixed>|null
 */
function shpigovsky_normalize_review_row( $row ) {
	if ( ! is_array( $row ) ) {
		return null;
	}

	$author = isset( $row['review_author'] ) ? trim( (string) $row['review_author'] ) : '';
	$text   = isset( $row['review_text'] ) ? trim( (string) $row['review_text'] ) : '';

	if ( '' === $author && '' === $text ) {
		return null;
	}

	$visible = true;
	if ( array_key_exists( 'review_visible', $row ) && '' !== $row['review_visible'] && null !== $row['review_visible'] ) {
		$visible = (bool) $row['review_visible'];
	}

	if ( ! $visible ) {
		return null;
	}

	$featured = true;
	if ( array_key_exists( 'review_featured', $row ) && '' !== $row['review_featured'] && null !== $row['review_featured'] ) {
		$featured = (bool) $row['review_featured'];
	}

	return array(
		'author'   => $author,
		'text'     => $text,
		'context'  => isset( $row['review_context'] ) ? trim( (string) $row['review_context'] ) : '',
		'source'   => isset( $row['review_source'] ) ? trim( (string) $row['review_source'] ) : '',
		'date'     => isset( $row['review_date'] ) ? trim( (string) $row['review_date'] ) : '',
		'rating'   => shpigovsky_normalize_review_rating( $row['review_rating'] ?? 5 ),
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

	$rows = get_field( 'reviews_items', 'option' );

	if ( ! is_array( $rows ) || empty( $rows ) ) {
		return array();
	}

	$items = array();

	foreach ( $rows as $row ) {
		$normalized = shpigovsky_normalize_review_row( $row );

		if ( null !== $normalized ) {
			$items[] = $normalized;
		}
	}

	return $items;
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
 * Resolve shared reviews section heading.
 *
 * @param string $fallback Default heading when options and Home field are empty.
 * @return string
 */
function shpigovsky_get_reviews_heading( $fallback = 'Отзывы' ) {
	$option_heading = shpigovsky_get_site_option( 'reviews_section_heading' );

	if ( '' !== $option_heading ) {
		return $option_heading;
	}

	return shpigovsky_home_text_or_fallback( 'home_reviews_heading', $fallback );
}
