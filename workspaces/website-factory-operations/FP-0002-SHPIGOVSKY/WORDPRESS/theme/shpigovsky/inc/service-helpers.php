<?php
/**
 * Service single template ACF read helpers and CPT queries — V9-06D7-D.
 *
 * Read-only; no meta writes.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Current service post ID in the loop.
 *
 * @return int
 */
function shpigovsky_get_current_service_id() {
	return (int) get_the_ID();
}

/**
 * Read a bounded service repeater safely.
 *
 * @param int    $post_id    Service post ID.
 * @param string $field_name Repeater field name.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_get_service_repeater( $post_id, $field_name ) {
	if ( ! function_exists( 'get_field' ) || $post_id <= 0 ) {
		return array();
	}

	$rows = get_field( $field_name, $post_id );

	if ( ! is_array( $rows ) ) {
		return array();
	}

	$normalized = array();

	foreach ( $rows as $row ) {
		if ( is_array( $row ) ) {
			$normalized[] = $row;
		}
	}

	return $normalized;
}

/**
 * Read service hero image attachment array.
 *
 * @param int $post_id Service post ID.
 * @return array<string, mixed>|null
 */
function shpigovsky_get_service_hero_image( $post_id ) {
	if ( ! function_exists( 'get_field' ) || $post_id <= 0 ) {
		return null;
	}

	$image = get_field( 'hero_media', $post_id );

	return is_array( $image ) ? $image : null;
}

/**
 * Theme asset fallback for service hero images when ACF hero_media is empty.
 *
 * @param string $variant Layout variant slug.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_service_default_hero_image( $variant ) {
	if ( 'subdivision' === $variant ) {
		return array(
			'url'    => shpigovsky_asset_uri( 'img/content/services/service-subdivision-hero.webp' ),
			'alt'    => '',
			'width'  => 1134,
			'height' => 613,
		);
	}

	return array(
		'url'    => '',
		'alt'    => '',
		'width'  => 0,
		'height' => 0,
	);
}

/**
 * Resolve service H1 title with optional ACF override.
 *
 * @param int $post_id Service post ID.
 * @return string
 */
function shpigovsky_get_service_hero_title( $post_id ) {
	$override = shpigovsky_get_service_field( $post_id, 'hero_title_override' );

	if ( '' !== $override ) {
		return $override;
	}

	$title = get_the_title( $post_id );

	return is_string( $title ) ? trim( $title ) : '';
}

/**
 * Whether a service post has published child services.
 *
 * @param int $post_id Service post ID.
 * @return bool
 */
function shpigovsky_service_has_children( $post_id ) {
	if ( ! post_type_exists( 'service' ) || $post_id <= 0 ) {
		return false;
	}

	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => $post_id,
			'posts_per_page' => 1,
			'fields'         => 'ids',
			'no_found_rows'  => true,
		)
	);

	return ! empty( $children );
}

/**
 * Get published child services for a parent service.
 *
 * @param int $post_id Parent service post ID.
 * @return WP_Post[]
 */
function shpigovsky_get_service_children( $post_id ) {
	if ( ! post_type_exists( 'service' ) || $post_id <= 0 ) {
		return array();
	}

	$children = get_posts(
		array(
			'post_type'      => 'service',
			'post_status'    => 'publish',
			'post_parent'    => $post_id,
			'posts_per_page' => 30,
			'orderby'        => 'menu_order',
			'order'          => 'ASC',
			'no_found_rows'  => true,
		)
	);

	return is_array( $children ) ? $children : array();
}

/**
 * Map ACF layout value to theme stack variant slug.
 *
 * @param string $acf_value Raw ACF select value.
 * @return string
 */
function shpigovsky_map_acf_layout_to_variant( $acf_value ) {
	$map = array(
		'subdivision'     => 'subdivision',
		'standard'        => 'leaf',
		'extended'        => 'leaf',
		'alcohol_special' => 'alcohol-special',
		'placeholder'     => 'leaf',
	);

	return isset( $map[ $acf_value ] ) ? $map[ $acf_value ] : '';
}

/**
 * Infer layout variant from hierarchy when ACF is empty.
 *
 * @param int $post_id Service post ID.
 * @return string
 */
function shpigovsky_infer_service_layout_variant( $post_id ) {
	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return 'leaf';
	}

	if ( 'lechenie-alkogolnoy-zavisimosti' === $post->post_name ) {
		return 'alcohol-special';
	}

	if ( shpigovsky_service_has_children( $post_id ) ) {
		return 'subdivision';
	}

	return 'leaf';
}

/**
 * Resolve canonical service layout variant for routing.
 *
 * @param int|null $post_id Optional post ID; defaults to current post.
 * @return string
 */
function shpigovsky_resolve_service_layout_variant( $post_id = null ) {
	if ( null === $post_id ) {
		$post_id = shpigovsky_get_current_service_id();
	}

	$post_id = (int) $post_id;

	if ( $post_id <= 0 ) {
		return 'leaf';
	}

	$acf_value = shpigovsky_get_service_field( $post_id, 'service_layout_variant' );
	$variant   = shpigovsky_map_acf_layout_to_variant( $acf_value );

	if ( '' !== $variant ) {
		return $variant;
	}

	return shpigovsky_infer_service_layout_variant( $post_id );
}

/**
 * Main element class for the current service layout variant.
 *
 * @param string $variant Layout variant slug.
 * @return string
 */
function shpigovsky_get_service_main_class( $variant ) {
	if ( 'subdivision' === $variant ) {
		return 'page-service-subdivision-v1__main site-main site-main--service site-main--service-subdivision';
	}

	return 'page-service-leaf-v1__main site-main site-main--service site-main--service-leaf';
}

/**
 * Build breadcrumb trail items for a service post.
 *
 * @param int $post_id Service post ID.
 * @return array<int, array{label:string,url:string}>
 */
function shpigovsky_get_service_breadcrumb_trail( $post_id ) {
	$trail = array(
		array(
			'label' => __( 'Главная', 'shpigovsky' ),
			'url'   => home_url( '/' ),
		),
		array(
			'label' => __( 'Услуги', 'shpigovsky' ),
			'url'   => home_url( '/uslugi/' ),
		),
	);

	$post = get_post( $post_id );

	if ( ! $post instanceof WP_Post ) {
		return $trail;
	}

	$ancestors = array_reverse( get_post_ancestors( $post ) );

	foreach ( $ancestors as $ancestor_id ) {
		$ancestor = get_post( $ancestor_id );

		if ( ! $ancestor instanceof WP_Post || 'service' !== $ancestor->post_type ) {
			continue;
		}

		$url = get_permalink( $ancestor );

		$trail[] = array(
			'label' => get_the_title( $ancestor ),
			'url'   => is_string( $url ) ? $url : '',
		);
	}

	$trail[] = array(
		'label' => get_the_title( $post ),
		'url'   => '',
	);

	return $trail;
}

/**
 * Build in-page subnav anchor items for a service layout variant.
 *
 * @param string $variant Layout variant slug.
 * @return array<int, array{id:string,label:string}>
 */
function shpigovsky_get_service_subnav_items( $variant ) {
	if ( 'subdivision' === $variant ) {
		return array(
			array(
				'id'    => 'service-subdivision-dependencies',
				'label' => __( 'Зависимости', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-nature',
				'label' => __( 'Природа зависимости', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-program',
				'label' => __( 'Программа лечения', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-start',
				'label' => __( 'С чего начать', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-approach',
				'label' => __( 'Наш подход к лечению', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-specialists',
				'label' => __( 'Специалисты', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-comfort',
				'label' => __( 'Условия центра', 'shpigovsky' ),
			),
			array(
				'id'    => 'service-subdivision-faq',
				'label' => __( 'Вопросы и ответы', 'shpigovsky' ),
			),
		);
	}

	$items = array(
		array(
			'id'    => 'service-leaf-intro',
			'label' => __( 'О программе', 'shpigovsky' ),
		),
		array(
			'id'    => 'service-leaf-program',
			'label' => __( 'Программа лечения', 'shpigovsky' ),
		),
		array(
			'id'    => 'service-leaf-start',
			'label' => __( 'С чего начать', 'shpigovsky' ),
		),
		array(
			'id'    => 'service-leaf-faq',
			'label' => __( 'Вопросы и ответы', 'shpigovsky' ),
		),
	);

	if ( 'alcohol-special' === $variant ) {
		array_splice(
			$items,
			1,
			0,
			array(
				array(
					'id'    => 'service-leaf-signs',
					'label' => __( 'Признаки зависимости', 'shpigovsky' ),
				),
			)
		);
	}

	return $items;
}

/**
 * Default programme direction labels when ACF repeater is empty.
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_get_service_programme_fallback_items() {
	return array(
		array(
			'title' => '01 — Генотипирование',
			'text'  => '',
		),
		array(
			'title' => '02 — Нейропсихологическая коррекция',
			'text'  => '',
		),
		array(
			'title' => '03 — Психокоррекция',
			'text'  => '',
		),
		array(
			'title' => '04 — Кинезиотерапия',
			'text'  => '',
		),
	);
}

/**
 * Static V9 programme items for service subdivision layout parity.
 *
 * @return array<int, array{title:string,image:string,width:int,height:int,alt:string}>
 */
function shpigovsky_get_service_subdivision_programme_fallback_items() {
	return array(
		array(
			'title'  => '01 — Генотипирование',
			'image'  => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-genotyping.webp' ),
			'width'  => 1216,
			'height' => 1632,
			'alt'    => 'Генотипирование',
		),
		array(
			'title'  => '02 — Нейропсихологическая коррекция',
			'image'  => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-neuropsychology.webp' ),
			'width'  => 1632,
			'height' => 1216,
			'alt'    => 'Нейропсихологическая коррекция',
		),
		array(
			'title'  => '03 — Психокоррекция',
			'image'  => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-psychocorrection.webp' ),
			'width'  => 880,
			'height' => 1184,
			'alt'    => 'Психокоррекция',
		),
		array(
			'title'  => '04 — Кинезиотерапия',
			'image'  => shpigovsky_asset_uri( 'img/content/rehabilitation-program/program-kinesiotherapy.webp' ),
			'width'  => 880,
			'height' => 1184,
			'alt'    => 'Кинезиотерапия',
		),
	);
}

/**
 * Static V9 dependencies section heading for subdivision pages.
 *
 * @return string
 */
function shpigovsky_get_service_subdivision_dependencies_heading() {
	return __( 'Зависимости, которые мы лечим', 'shpigovsky' );
}

/**
 * Static V9 dependencies section lead fallback.
 *
 * @return string
 */
function shpigovsky_get_service_subdivision_dependencies_lead_fallback() {
	return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
}

/**
 * Static V9 dependencies section footer text fallback.
 *
 * @return string
 */
function shpigovsky_get_service_subdivision_dependencies_footer_fallback() {
	return 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
}

/**
 * Add V9 body class for service single routes.
 *
 * @param string[] $classes Body classes.
 * @return string[]
 */
function shpigovsky_service_body_class( $classes ) {
	if ( ! is_singular( 'service' ) ) {
		return $classes;
	}

	$variant = shpigovsky_get_service_layout_variant();

	if ( 'subdivision' === $variant ) {
		$classes[] = 'page-service-subdivision-v1';
	} elseif ( 'leaf' === $variant || 'alcohol-special' === $variant ) {
		$classes[] = 'page-service-leaf-v1';
	}

	return $classes;
}
add_filter( 'body_class', 'shpigovsky_service_body_class' );

/**
 * Resolve CTA band copy for service mid-page CTAs.
 *
 * @param int $post_id Service post ID.
 * @return array{title:string,subtitle:string,phone:string,phone_hint:string,button_label:string,source:string}
 */
function shpigovsky_get_service_cta_band( $post_id ) {
	$title        = shpigovsky_get_service_field( $post_id, 'cta_title' );
	$subtitle     = shpigovsky_get_service_field( $post_id, 'cta_text' );
	$button_label = shpigovsky_get_service_field( $post_id, 'cta_button_label' );
	$phone        = shpigovsky_get_site_option( 'phone_primary' );
	$phone        = '' !== $phone ? shpigovsky_format_phone_display( $phone ) : '';
	$default_cta  = shpigovsky_get_site_option( 'default_button_label' );
	$default_cta  = '' !== $default_cta ? $default_cta : __( 'Записаться', 'shpigovsky' );

	if ( '' === $title ) {
		$title = __( 'Запишитесь на встречу', 'shpigovsky' );
	}

	if ( '' === $subtitle ) {
		$subtitle = __( 'Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.', 'shpigovsky' );
	}

	if ( '' === $button_label ) {
		$button_label = $default_cta;
	}

	return array(
		'title'        => $title,
		'subtitle'     => $subtitle,
		'phone'        => $phone,
		'phone_hint'   => __( 'Или позвоните нам', 'shpigovsky' ),
		'button_label' => $button_label,
		'source'       => 'service-cta-' . $post_id,
	);
}
