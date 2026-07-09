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
