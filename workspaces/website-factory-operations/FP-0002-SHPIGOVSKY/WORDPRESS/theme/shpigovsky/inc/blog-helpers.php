<?php
/**
 * Blog archive helpers — V9-06E26B.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Posts page ID for the blog archive.
 *
 * @return int
 */
function shpigovsky_get_blog_posts_page_id() {
	$page_id = (int) get_option( 'page_for_posts' );

	return $page_id > 0 ? $page_id : 0;
}

/**
 * Read a scalar blog archive setting from the posts page.
 *
 * @param string $field_name ACF field name.
 * @return string
 */
function shpigovsky_get_blog_archive_field( $field_name ) {
	$page_id = shpigovsky_get_blog_posts_page_id();

	if ( $page_id <= 0 || ! function_exists( 'get_field' ) ) {
		return '';
	}

	$value = get_field( $field_name, $page_id );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Blog archive H1 with static V9 fallback.
 *
 * @return string
 */
function shpigovsky_get_blog_archive_title() {
	$title = shpigovsky_get_blog_archive_field( 'blog_archive_title' );

	if ( '' !== $title ) {
		return $title;
	}

	return 'Статьи о зависимостях, диагностике и методах лечения';
}

/**
 * Blog archive intro with static V9 fallback.
 *
 * @return string
 */
function shpigovsky_get_blog_archive_intro() {
	$intro = shpigovsky_get_blog_archive_field( 'blog_archive_intro' );

	if ( '' !== $intro ) {
		return $intro;
	}

	return 'Специалисты центра реабилитации Шпиговский Дом рассказывают о видах зависимостей, что говорит о их наличии, какие подходы в лечении существуют, какие методы дают действительно хороший результат';
}

/**
 * Empty state title.
 *
 * @return string
 */
function shpigovsky_get_blog_archive_empty_title() {
	$title = shpigovsky_get_blog_archive_field( 'blog_archive_empty_title' );

	if ( '' !== $title ) {
		return $title;
	}

	return 'Статей пока нет';
}

/**
 * Empty state text.
 *
 * @return string
 */
function shpigovsky_get_blog_archive_empty_text() {
	$text = shpigovsky_get_blog_archive_field( 'blog_archive_empty_text' );

	if ( '' !== $text ) {
		return $text;
	}

	return 'Мы готовим материалы для этого раздела. Загляните позже или запишитесь на консультацию — первый разговор ни к чему не обязывает.';
}

/**
 * Card link label.
 *
 * @return string
 */
function shpigovsky_get_blog_archive_card_link_label() {
	$label = shpigovsky_get_blog_archive_field( 'blog_archive_card_link_label' );

	if ( '' !== $label ) {
		return $label;
	}

	return 'Читать';
}

/**
 * Fallback card image data for archive cards.
 *
 * @return array{url:string,width:int,height:int,alt:string}
 */
function shpigovsky_get_blog_archive_card_fallback_image() {
	$page_id = shpigovsky_get_blog_posts_page_id();
	$image   = array();

	if ( $page_id > 0 && function_exists( 'get_field' ) ) {
		$acf_image = get_field( 'blog_archive_card_fallback_image', $page_id );

		if ( is_array( $acf_image ) && ! empty( $acf_image['url'] ) ) {
			$image = $acf_image;
		}
	}

	if ( empty( $image['url'] ) ) {
		return array(
			'url'    => shpigovsky_asset_uri( 'img/content/home-articles/article-alcohol-dependence.webp' ),
			'width'  => 1216,
			'height' => 1632,
			'alt'    => '',
		);
	}

	return array(
		'url'    => (string) $image['url'],
		'width'  => ! empty( $image['width'] ) ? (int) $image['width'] : 1216,
		'height' => ! empty( $image['height'] ) ? (int) $image['height'] : 1632,
		'alt'    => ! empty( $image['alt'] ) ? (string) $image['alt'] : '',
	);
}

/**
 * Format reading time for archive cards.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_get_blog_card_reading_time( $post_id ) {
	$minutes = 0;

	if ( function_exists( 'get_field' ) ) {
		$minutes = (int) get_field( 'article_reading_time', $post_id );
	}

	if ( $minutes <= 0 ) {
		return '';
	}

	$mod10  = $minutes % 10;
	$mod100 = $minutes % 100;

	if ( $mod10 === 1 && $mod100 !== 11 ) {
		$suffix = 'минута';
	} elseif ( $mod10 >= 2 && $mod10 <= 4 && ( $mod100 < 10 || $mod100 >= 20 ) ) {
		$suffix = 'минуты';
	} else {
		$suffix = 'минут';
	}

	return sprintf( '%d %s на чтение', $minutes, $suffix );
}

/**
 * Whether a post should show its publish date on archive cards.
 *
 * @param int $post_id Post ID.
 * @return bool
 */
function shpigovsky_blog_card_show_date( $post_id ) {
	if ( ! function_exists( 'get_field' ) ) {
		return true;
	}

	$value = get_field( 'article_show_date_public', $post_id );

	if ( null === $value || '' === $value ) {
		return true;
	}

	return (bool) $value;
}

/**
 * Build archive card args for a post.
 *
 * @param int $post_id Post ID.
 * @return array<string, mixed>
 */
function shpigovsky_build_blog_archive_card_args( $post_id ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return array();
	}

	$fallback = shpigovsky_get_blog_archive_card_fallback_image();
	$image_id = (int) get_post_thumbnail_id( $post_id );
	$image    = $fallback;

	if ( $image_id > 0 ) {
		$src = wp_get_attachment_image_src( $image_id, 'large' );

		if ( is_array( $src ) && ! empty( $src[0] ) ) {
			$image = array(
				'url'    => (string) $src[0],
				'width'  => ! empty( $src[1] ) ? (int) $src[1] : 1216,
				'height' => ! empty( $src[2] ) ? (int) $src[2] : 1632,
				'alt'    => trim( (string) get_post_meta( $image_id, '_wp_attachment_image_alt', true ) ),
			);
		}
	}

	if ( '' === $image['alt'] ) {
		$image['alt'] = get_the_title( $post_id );
	}

	$show_date = shpigovsky_blog_card_show_date( $post_id );
	$timestamp = get_post_time( 'U', true, $post_id );

	return array(
		'title'        => get_the_title( $post_id ),
		'url'          => get_permalink( $post_id ),
		'excerpt'      => get_the_excerpt( $post_id ),
		'image_url'    => $image['url'],
		'image_width'  => $image['width'],
		'image_height' => $image['height'],
		'image_alt'    => $image['alt'],
		'iso_date'     => $show_date ? get_post_time( 'Y-m-d', true, $post_id ) : '',
		'formatted_date' => $show_date ? wp_date( 'd.m.Y', $timestamp ) : '',
		'reading_time' => shpigovsky_get_blog_card_reading_time( $post_id ),
		'link_label'   => shpigovsky_get_blog_archive_card_link_label(),
	);
}

/**
 * Blog archive breadcrumb trail.
 *
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_blog_breadcrumb_trail() {
	return array(
		array(
			'label' => __( 'Главная', 'shpigovsky' ),
			'url'   => home_url( '/' ),
		),
		array(
			'label' => __( 'Статьи', 'shpigovsky' ),
			'url'   => '',
		),
	);
}

/**
 * CTA band payload for blog lower stack.
 *
 * @return array<string, mixed>
 */
function shpigovsky_get_blog_archive_cta_band() {
	$title = shpigovsky_get_blog_archive_field( 'blog_archive_final_cta_title' );
	$text  = shpigovsky_get_blog_archive_field( 'blog_archive_final_cta_text' );
	$phone = shpigovsky_get_blog_archive_field( 'blog_archive_final_cta_phone' );
	$hint  = shpigovsky_get_blog_archive_field( 'blog_archive_final_cta_phone_hint' );
	$label = shpigovsky_get_blog_archive_field( 'blog_archive_final_cta_button_label' );

	if ( '' === $phone ) {
		$phone = shpigovsky_get_site_option( 'phone_primary' );
	}

	if ( '' === $phone ) {
		$phone = '8 (925) 183-64-64';
	}

	return array(
		'title'          => '' !== $title ? $title : 'Запишитесь на встречу',
		'subtitle'       => '' !== $text ? $text : 'Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.',
		'phone'          => $phone,
		'phone_hint'     => '' !== $hint ? $hint : 'Или позвоните нам',
		'button_label'   => '' !== $label ? $label : 'Записаться',
		'source'         => 'blog-cta-01',
		'section_id'     => 'blog-cta-01',
		'heading_id'     => 'blog-cta-01-heading',
		'heading_text'   => '' !== $title ? $title : 'Запишитесь на встречу',
		'wrap_section'   => true,
		'button_first'   => true,
		'margin_flush'   => true,
	);
}

/**
 * Expert quote payload for blog lower stack.
 *
 * @return array<string, string>
 */
function shpigovsky_get_blog_archive_expert_quote() {
	$page_id = shpigovsky_get_blog_posts_page_id();
	$photo   = array();

	if ( $page_id > 0 && function_exists( 'get_field' ) ) {
		$acf_photo = get_field( 'blog_archive_expert_photo', $page_id );

		if ( is_array( $acf_photo ) && ! empty( $acf_photo['url'] ) ) {
			$photo = $acf_photo;
		}
	}

	$photo_url = ! empty( $photo['url'] ) ? (string) $photo['url'] : shpigovsky_asset_uri( 'img/content/founder-sergey-shpigovsky.png' );

	return array(
		'quote_text' => shpigovsky_get_blog_archive_field( 'blog_archive_expert_quote_text' ) ?: 'Мы делимся здесь практическими материалами о зависимостях и восстановлении — простым языком, без запугивания и без обещаний мгновенного результата.',
		'name'       => shpigovsky_get_blog_archive_field( 'blog_archive_expert_name' ) ?: 'Сергей Юрьевич Шпиговский',
		'role'       => shpigovsky_get_blog_archive_field( 'blog_archive_expert_role' ) ?: 'Основатель центра. Аддиктолог, интервенционист',
		'photo_url'  => $photo_url,
		'photo_width' => ! empty( $photo['width'] ) ? (string) (int) $photo['width'] : '1281',
		'photo_height' => ! empty( $photo['height'] ) ? (string) (int) $photo['height'] : '1278',
		'photo_alt'  => shpigovsky_get_blog_archive_field( 'blog_archive_expert_name' ) ?: 'Сергей Юрьевич Шпиговский',
		'cta_label'  => shpigovsky_get_blog_archive_field( 'blog_archive_expert_cta_label' ) ?: 'Записаться на консультацию',
	);
}

/**
 * Archive posts per page — matches V9 desktop grid density.
 *
 * @param WP_Query $query Main query.
 */
function shpigovsky_blog_archive_posts_per_page( $query ) {
	if ( is_admin() || ! $query->is_main_query() || ! $query->is_home() ) {
		return;
	}

	$query->set( 'posts_per_page', 12 );
}
add_action( 'pre_get_posts', 'shpigovsky_blog_archive_posts_per_page' );

/**
 * Add V9 body classes on blog archive.
 *
 * @param string[] $classes Body classes.
 * @return string[]
 */
function shpigovsky_blog_body_class( $classes ) {
	if ( shpigovsky_is_blog_posts_page() ) {
		$classes[] = 'page-blog';
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_blog_body_class' );

/**
 * Add data-page attribute hook for blog archive.
 */
function shpigovsky_blog_body_attributes() {
	if ( ! shpigovsky_is_blog_posts_page() ) {
		return;
	}

	echo ' data-page="blog"';
}
add_action( 'shpigovsky_body_attributes', 'shpigovsky_blog_body_attributes' );

/**
 * Whether the current request is a single blog post.
 *
 * @return bool
 */
function shpigovsky_is_blog_single() {
	return is_singular( 'post' );
}

/**
 * Blog single breadcrumb trail.
 *
 * @param int $post_id Post ID.
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_blog_single_breadcrumb_trail( $post_id ) {
	$post_id = (int) $post_id;
	$blog_id = shpigovsky_get_blog_posts_page_id();
	$blog_url = $blog_id > 0 ? get_permalink( $blog_id ) : home_url( '/blog/' );

	return array(
		array(
			'label' => __( 'Главная', 'shpigovsky' ),
			'url'   => home_url( '/' ),
		),
		array(
			'label' => __( 'Статьи', 'shpigovsky' ),
			'url'   => is_string( $blog_url ) ? $blog_url : home_url( '/blog/' ),
		),
		array(
			'label' => get_the_title( $post_id ),
			'url'   => '',
		),
	);
}

/**
 * Read scalar article ACF field.
 *
 * @param string $field_name Field name.
 * @param int    $post_id Post ID.
 * @return string
 */
function shpigovsky_get_article_field( $field_name, $post_id ) {
	$post_id = (int) $post_id;

	if ( $post_id <= 0 || ! function_exists( 'get_field' ) ) {
		return '';
	}

	$value = get_field( $field_name, $post_id );

	if ( is_array( $value ) || is_object( $value ) ) {
		return '';
	}

	return is_string( $value ) ? trim( $value ) : ( is_numeric( $value ) ? (string) $value : '' );
}

/**
 * Article eyebrow.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_get_article_eyebrow( $post_id ) {
	return shpigovsky_get_article_field( 'article_eyebrow', $post_id );
}

/**
 * Article lead with excerpt fallback.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_get_article_lead( $post_id ) {
	$post_id = (int) $post_id;
	$lead    = shpigovsky_get_article_field( 'article_lead', $post_id );

	if ( '' !== $lead ) {
		return $lead;
	}

	$excerpt = get_post_field( 'post_excerpt', $post_id );

	return is_string( $excerpt ) ? trim( $excerpt ) : '';
}

/**
 * Whether article date is public.
 *
 * @param int $post_id Post ID.
 * @return bool
 */
function shpigovsky_article_show_date( $post_id ) {
	return shpigovsky_blog_card_show_date( $post_id );
}

/**
 * Whether article author is public.
 *
 * @param int $post_id Post ID.
 * @return bool
 */
function shpigovsky_article_show_author( $post_id ) {
	if ( ! function_exists( 'get_field' ) ) {
		return false;
	}

	$hide = get_field( 'article_hide_author_public', $post_id );

	if ( null === $hide || '' === $hide ) {
		return false;
	}

	return ! (bool) $hide;
}

/**
 * Article author label.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_get_article_author_label( $post_id ) {
	$label = shpigovsky_get_article_field( 'article_author_label', $post_id );

	if ( '' !== $label ) {
		return $label;
	}

	return 'Шпиговский С.Ю.';
}

/**
 * Featured image payload for article hero.
 *
 * @param int $post_id Post ID.
 * @return array{url:string,width:int,height:int,alt:string}
 */
function shpigovsky_get_article_hero_image( $post_id ) {
	$post_id  = (int) $post_id;
	$fallback = shpigovsky_get_blog_archive_card_fallback_image();
	$image_id = (int) get_post_thumbnail_id( $post_id );
	$image    = $fallback;

	if ( $image_id > 0 ) {
		$src = wp_get_attachment_image_src( $image_id, 'large' );

		if ( is_array( $src ) && ! empty( $src[0] ) ) {
			$image = array(
				'url'    => (string) $src[0],
				'width'  => ! empty( $src[1] ) ? (int) $src[1] : 570,
				'height' => ! empty( $src[2] ) ? (int) $src[2] : 600,
				'alt'    => trim( (string) get_post_meta( $image_id, '_wp_attachment_image_alt', true ) ),
			);
		}
	}

	if ( '' === $image['alt'] ) {
		$image['alt'] = get_the_title( $post_id );
	}

	return $image;
}

/**
 * Whether TOC should render.
 *
 * @param int $post_id Post ID.
 * @return bool
 */
function shpigovsky_article_show_toc( $post_id ) {
	if ( ! function_exists( 'get_field' ) ) {
		return true;
	}

	$value = get_field( 'article_show_toc', $post_id );

	if ( null === $value || '' === $value ) {
		return true;
	}

	return (bool) $value;
}

/**
 * TOC title with V9 fallback.
 *
 * @param int $post_id Post ID.
 * @return string
 */
function shpigovsky_get_article_toc_title( $post_id ) {
	$title = shpigovsky_get_article_field( 'article_toc_title', $post_id );

	return '' !== $title ? $title : 'Оглавление:';
}

/**
 * Sanitize heading text into a stable anchor id.
 *
 * @param string $text Heading text.
 * @return string
 */
function shpigovsky_article_anchor_id( $text ) {
	$text = remove_accents( wp_strip_all_tags( (string) $text ) );
	$text = strtolower( $text );
	$text = preg_replace( '/[^a-z0-9\-]+/u', '-', $text );
	$text = trim( (string) $text, '-' );

	if ( '' === $text ) {
		return 'section';
	}

	return $text;
}

/**
 * Ensure h2/h3 in article content have stable anchor ids.
 *
 * @param string $content Post content.
 * @return string
 */
function shpigovsky_article_content_heading_ids( $content ) {
	if ( ! shpigovsky_is_blog_single() || ! in_the_loop() || ! is_main_query() ) {
		return $content;
	}

	if ( ! is_string( $content ) || '' === $content ) {
		return $content;
	}

	$used = array();

	return (string) preg_replace_callback(
		'/<h([23])([^>]*)>(.*?)<\/h\1>/is',
		static function ( $matches ) use ( &$used ) {
			$level = $matches[1];
			$attrs = $matches[2];
			$inner = $matches[3];

			if ( preg_match( '/\sid=(["\'])([^"\']+)\1/i', $attrs, $id_match ) ) {
				$used[ $id_match[2] ] = true;
				return $matches[0];
			}

			$base = shpigovsky_article_anchor_id( $inner );
			$id   = $base;
			$idx  = 2;

			while ( isset( $used[ $id ] ) ) {
				$id = $base . '-' . $idx;
				++$idx;
			}

			$used[ $id ] = true;

			return sprintf( '<h%s id="%s"%s>%s</h%s>', $level, esc_attr( $id ), $attrs, $inner, $level );
		},
		$content
	);
}
add_filter( 'the_content', 'shpigovsky_article_content_heading_ids', 5 );

/**
 * Build TOC items from rendered article headings.
 *
 * @param int $post_id Post ID.
 * @return array<int, array{id:string,label:string,level:int}>
 */
function shpigovsky_get_article_toc_items( $post_id ) {
	$post_id = (int) $post_id;
	$post    = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return array();
	}

	$content = apply_filters( 'the_content', $post->post_content );

	if ( ! preg_match_all( '/<h([23])[^>]*id=(["\'])([^"\']+)\2[^>]*>(.*?)<\/h\1>/is', $content, $matches, PREG_SET_ORDER ) ) {
		return array();
	}

	$items = array();

	foreach ( $matches as $match ) {
		$label = trim( wp_strip_all_tags( $match[4] ) );

		if ( '' === $label ) {
			continue;
		}

		$items[] = array(
			'id'    => (string) $match[3],
			'label' => $label,
			'level' => (int) $match[1],
		);
	}

	return $items;
}

/**
 * Conclusion block payload.
 *
 * @param int $post_id Post ID.
 * @return array<string, mixed>
 */
function shpigovsky_get_article_conclusion( $post_id ) {
	$quote = shpigovsky_get_article_field( 'article_conclusion_quote', $post_id );
	$expert = shpigovsky_get_blog_archive_expert_quote();

	return array(
		'heading' => shpigovsky_get_article_field( 'article_conclusion_heading', $post_id ) ?: 'Заключение',
		'quote'   => $quote,
		'name'    => $expert['name'],
		'role'    => $expert['role'],
		'photo'   => array(
			'url'    => $expert['photo_url'],
			'width'  => (int) $expert['photo_width'],
			'height' => (int) $expert['photo_height'],
			'alt'    => $expert['photo_alt'],
		),
	);
}

/**
 * Source list items.
 *
 * @param int $post_id Post ID.
 * @return string[]
 */
function shpigovsky_get_article_sources( $post_id ) {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$rows = get_field( 'article_source_items', $post_id );

	if ( ! is_array( $rows ) || empty( $rows ) ) {
		return array();
	}

	$sources = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$text = isset( $row['source_text'] ) ? trim( (string) $row['source_text'] ) : '';

		if ( '' !== $text ) {
			$sources[] = $text;
		}
	}

	return $sources;
}

/**
 * FAQ items for article single.
 *
 * @param int $post_id Post ID.
 * @return array<int, array{question:string,answer:string}>
 */
function shpigovsky_get_article_faq_items( $post_id ) {
	if ( ! function_exists( 'get_field' ) ) {
		return array();
	}

	$rows = get_field( 'article_faq_items', $post_id );

	if ( ! is_array( $rows ) || empty( $rows ) ) {
		return array();
	}

	$items = array();

	foreach ( $rows as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$question = isset( $row['question'] ) ? trim( (string) $row['question'] ) : '';
		$answer   = isset( $row['answer'] ) ? trim( (string) $row['answer'] ) : '';

		if ( '' === $question || '' === $answer ) {
			continue;
		}

		$items[] = array(
			'question' => $question,
			'answer'   => $answer,
		);
	}

	return $items;
}

/**
 * Related posts for article single.
 *
 * @param int $post_id Post ID.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_article_related_posts( $post_id ) {
	$post_id = (int) $post_id;
	$cards   = array();
	$related = array();

	if ( function_exists( 'get_field' ) ) {
		$acf_related = get_field( 'related_posts', $post_id );

		if ( is_array( $acf_related ) ) {
			foreach ( $acf_related as $item ) {
				if ( $item instanceof WP_Post ) {
					$related[] = (int) $item->ID;
				} elseif ( is_numeric( $item ) ) {
					$related[] = (int) $item;
				}
			}
		}
	}

	$related = array_values( array_unique( array_filter( $related ) ) );

	if ( empty( $related ) ) {
		$categories = wp_get_post_categories( $post_id );

		if ( ! empty( $categories ) ) {
			$query = new WP_Query(
				array(
					'post_type'           => 'post',
					'post_status'         => 'publish',
					'posts_per_page'      => 3,
					'post__not_in'        => array( $post_id ),
					'ignore_sticky_posts' => true,
					'category__in'        => $categories,
					'orderby'             => 'date',
					'order'               => 'DESC',
					'no_found_rows'       => true,
				)
			);

			if ( $query->have_posts() ) {
				while ( $query->have_posts() ) {
					$query->the_post();
					$related[] = get_the_ID();
				}
				wp_reset_postdata();
			}
		}
	}

	foreach ( $related as $related_id ) {
		$related_id = (int) $related_id;

		if ( $related_id <= 0 || $related_id === $post_id ) {
			continue;
		}

		if ( 'publish' !== get_post_status( $related_id ) ) {
			continue;
		}

		$archive_card = shpigovsky_build_blog_archive_card_args( $related_id );

		if ( empty( $archive_card ) ) {
			continue;
		}

		$cards[] = array(
			'title'        => $archive_card['title'],
			'url'          => $archive_card['url'],
			'image_url'    => $archive_card['image_url'],
			'image_width'  => $archive_card['image_width'],
			'image_height' => $archive_card['image_height'],
			'image_alt'    => $archive_card['image_alt'],
			'link_label'   => $archive_card['link_label'],
		);

		if ( count( $cards ) >= 3 ) {
			break;
		}
	}

	return $cards;
}

/**
 * Final CTA band for article single.
 *
 * @param int $post_id Post ID.
 * @return array<string, mixed>
 */
function shpigovsky_get_article_cta_band( $post_id ) {
	$archive = shpigovsky_get_blog_archive_cta_band();
	$title   = shpigovsky_get_article_field( 'article_final_cta_title', $post_id );
	$text    = shpigovsky_get_article_field( 'article_final_cta_text', $post_id );
	$label   = shpigovsky_get_article_field( 'article_final_cta_button_label', $post_id );
	$url     = shpigovsky_get_article_field( 'article_final_cta_button_url', $post_id );

	return array(
		'title'        => '' !== $title ? $title : $archive['title'],
		'subtitle'     => '' !== $text ? $text : $archive['subtitle'],
		'phone'        => $archive['phone'],
		'phone_hint'   => $archive['phone_hint'],
		'button_label' => '' !== $label ? $label : $archive['button_label'],
		'button_url'   => $url,
		'source'       => 'blog-article-cta-01',
		'section_id'   => 'blog-article-cta-01',
		'heading_id'   => 'blog-article-cta-01-heading',
		'heading_text' => '' !== $title ? $title : $archive['heading_text'],
		'wrap_section' => true,
		'button_first' => true,
		'margin_flush' => true,
	);
}

/**
 * Add V9 body classes on blog single.
 *
 * @param string[] $classes Body classes.
 * @return string[]
 */
function shpigovsky_blog_single_body_class( $classes ) {
	if ( shpigovsky_is_blog_single() ) {
		$classes[] = 'page-blog-article';
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_blog_single_body_class' );

/**
 * Add data-page attribute hook for blog single.
 */
function shpigovsky_blog_single_body_attributes() {
	if ( ! shpigovsky_is_blog_single() ) {
		return;
	}

	echo ' data-page="blog-article"';
}
add_action( 'shpigovsky_body_attributes', 'shpigovsky_blog_single_body_attributes' );
