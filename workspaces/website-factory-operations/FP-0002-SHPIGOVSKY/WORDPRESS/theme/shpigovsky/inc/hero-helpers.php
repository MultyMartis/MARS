<?php
/**
 * Hero system — V9 context registry, ACF resolution, theme asset fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Canonical hero layout variants used across FP-0002 V9 routes.
 *
 * @return array<string, array<string, mixed>>
 */
function shpigovsky_get_hero_context_registry() {
	return array(
		'home' => array(
			'label'           => 'Home',
			'layout'          => 'home',
			'acf_field'       => 'hero_media',
			'fallback_key'    => 'home',
			'fallback_asset'  => 'img/hero/hero-main.png',
			'fallback_width'  => 2230,
			'fallback_height' => 1246,
			'fallback_alt'    => '',
		),
		'services_hub' => array(
			'label'           => 'Services Hub',
			'layout'          => 'services_inner_v2',
			'acf_field'       => 'hero_media',
			'fallback_key'    => 'services_hub',
			'fallback_asset'  => 'img/content/services/services-hero.webp',
			'fallback_width'  => 1400,
			'fallback_height' => 628,
			'fallback_alt'    => '',
		),
		'service_subdivision' => array(
			'label'           => 'Service Subdivision',
			'layout'          => 'services_inner_v2',
			'acf_field'       => 'hero_media',
			'fallback_key'    => 'service_subdivision',
			'fallback_asset'  => 'img/content/services/service-subdivision-hero.webp',
			'fallback_width'  => 1134,
			'fallback_height' => 613,
			'fallback_alt'    => '',
		),
		'service_leaf_alcohol' => array(
			'label'           => 'Service Leaf — Alcohol',
			'layout'          => 'services_inner_v2',
			'acf_field'       => 'hero_media',
			'fallback_key'    => 'service_leaf_alcohol',
			'fallback_asset'  => 'img/content/services/service-leaf-alcohol-hero.webp',
			'fallback_width'  => 850,
			'fallback_height' => 567,
			'fallback_alt'    => '',
		),
		'service_leaf_genotyping' => array(
			'label'           => 'Service Leaf — Genotyping',
			'layout'          => 'services_inner_v2',
			'acf_field'       => 'hero_media',
			'fallback_key'    => 'service_leaf_genotyping',
			'fallback_asset'  => 'img/content/rehabilitation-program/program-genotyping.webp',
			'fallback_width'  => 850,
			'fallback_height' => 567,
			'fallback_alt'    => 'Генотипирование',
		),
		'institutional' => array(
			'label'           => 'Institutional',
			'layout'          => 'services_inner_v2',
			'acf_field'       => 'hero_media',
			'fallback_key'    => 'institutional',
			'fallback_asset'  => 'img/content/o-centre/o-centre-hero.webp',
			'fallback_width'  => 1890,
			'fallback_height' => 1260,
			'fallback_alt'    => '',
		),
	);
}

/**
 * Read an ACF image field for a post/page.
 *
 * @param int    $post_id    Object ID.
 * @param string $field_name Field name.
 * @return array<string, mixed>|null
 */
function shpigovsky_get_hero_acf_image( $post_id, $field_name = 'hero_media' ) {
	if ( ! function_exists( 'get_field' ) || $post_id <= 0 ) {
		return null;
	}

	$image = get_field( $field_name, $post_id );

	return is_array( $image ) ? $image : null;
}

/**
 * Resolve theme asset fallback descriptor for a hero context key.
 *
 * @param string $context_key Registry key.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_hero_theme_fallback( $context_key ) {
	$registry = shpigovsky_get_hero_context_registry();

	if ( ! isset( $registry[ $context_key ] ) ) {
		return array(
			'url'    => '',
			'alt'    => '',
			'width'  => 0,
			'height' => 0,
		);
	}

	$context = $registry[ $context_key ];
	$path    = SHPIGOVSKY_THEME_DIR . '/assets/' . ltrim( $context['fallback_asset'], '/' );

	if ( ! is_readable( $path ) ) {
		return array(
			'url'    => '',
			'alt'    => (string) $context['fallback_alt'],
			'width'  => (int) $context['fallback_width'],
			'height' => (int) $context['fallback_height'],
		);
	}

	return array(
		'url'    => shpigovsky_asset_uri( $context['fallback_asset'] ),
		'alt'    => (string) $context['fallback_alt'],
		'width'  => (int) $context['fallback_width'],
		'height' => (int) $context['fallback_height'],
	);
}

/**
 * Resolve hero image URL/alt/dimensions from ACF with theme fallback.
 *
 * @param array<string, mixed>|null $acf_image  ACF image array.
 * @param string                    $context_key Hero context registry key.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_resolve_hero_image( $acf_image, $context_key ) {
	$url = shpigovsky_acf_image_url( $acf_image );
	$alt = shpigovsky_acf_image_alt( $acf_image );

	if ( '' !== $url ) {
		$width  = 0;
		$height = 0;

		if ( is_array( $acf_image ) ) {
			$width  = ! empty( $acf_image['width'] ) ? (int) $acf_image['width'] : 0;
			$height = ! empty( $acf_image['height'] ) ? (int) $acf_image['height'] : 0;
		}

		if ( $width <= 0 || $height <= 0 ) {
			$fallback = shpigovsky_get_hero_theme_fallback( $context_key );
			$width    = $fallback['width'];
			$height   = $fallback['height'];
		}

		return array(
			'url'    => $url,
			'alt'    => $alt,
			'width'  => $width,
			'height' => $height,
		);
	}

	return shpigovsky_get_hero_theme_fallback( $context_key );
}

/**
 * Resolve service hero context key from layout variant and post slug.
 *
 * @param int    $post_id Service post ID.
 * @param string $variant Layout variant slug.
 * @return string
 */
function shpigovsky_get_service_hero_context_key( $post_id, $variant ) {
	if ( 'subdivision' === $variant ) {
		return 'service_subdivision';
	}

	$post = get_post( $post_id );

	if ( $post instanceof WP_Post ) {
		if ( 'alcohol-special' === $variant || 'lechenie-alkogolnoy-zavisimosti' === $post->post_name ) {
			return 'service_leaf_alcohol';
		}

		if ( 'genotipirovanie' === $post->post_name ) {
			return 'service_leaf_genotyping';
		}
	}

	return 'service_leaf_alcohol';
}

/**
 * Resolve home hero image: hero_media > slide image > theme fallback.
 *
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_home_hero_image() {
	$page_id = shpigovsky_get_front_page_id();

	if ( $page_id <= 0 ) {
		return shpigovsky_get_hero_theme_fallback( 'home' );
	}

	$direct_image = shpigovsky_get_hero_acf_image( $page_id, 'hero_media' );

	if ( '' !== shpigovsky_acf_image_url( $direct_image ) ) {
		return shpigovsky_resolve_hero_image( $direct_image, 'home' );
	}

	$slides      = shpigovsky_get_home_repeater( 'home_hero_slides' );
	$slide       = ! empty( $slides[0] ) && is_array( $slides[0] ) ? $slides[0] : array();
	$slide_image = isset( $slide['image'] ) ? $slide['image'] : null;

	return shpigovsky_resolve_hero_image( $slide_image, 'home' );
}

/**
 * Resolve services hub hero image from ACF with theme fallback.
 *
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_services_hub_hero_image() {
	$page_id = shpigovsky_get_services_hub_page_id();

	if ( $page_id <= 0 ) {
		return shpigovsky_get_hero_theme_fallback( 'services_hub' );
	}

	$image = shpigovsky_get_hero_acf_image( $page_id, 'hero_media' );

	return shpigovsky_resolve_hero_image( $image, 'services_hub' );
}

/**
 * Resolve service hero image from ACF with variant-aware theme fallback.
 *
 * @param int    $post_id Service post ID.
 * @param string $variant Layout variant slug.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_service_hero_image_resolved( $post_id, $variant = '' ) {
	if ( '' === $variant ) {
		$variant = shpigovsky_get_service_layout_variant();
	}

	$context_key = shpigovsky_get_service_hero_context_key( $post_id, $variant );
	$image       = shpigovsky_get_service_hero_image( $post_id );

	return shpigovsky_resolve_hero_image( $image, $context_key );
}

/**
 * Resolve institutional page hero image from ACF with theme fallback.
 *
 * @param int $page_id Page ID.
 * @return array{url:string,alt:string,width:int,height:int}
 */
function shpigovsky_get_institutional_hero_image( $page_id ) {
	$image = shpigovsky_get_hero_acf_image( $page_id, 'hero_media' );

	return shpigovsky_resolve_hero_image( $image, 'institutional' );
}

/**
 * Default hero CTA label from site options with static fallback.
 *
 * @return string
 */
function shpigovsky_get_hero_default_cta_label() {
	$label = shpigovsky_get_site_option( 'default_button_label' );

	return '' !== $label ? $label : __( 'Записаться на консультацию', 'shpigovsky' );
}

/**
 * Resolve local/entity hero CTA button label with route and global fallbacks.
 *
 * Fallback chain: local hero_cta_label → route-specific fallback → site default → static V9.
 *
 * @param int    $post_id        Page or service post ID.
 * @param string $route_fallback Optional route-specific label when local field is empty.
 * @return string
 */
function shpigovsky_get_local_hero_cta_label( $post_id, $route_fallback = '' ) {
	$local = '';

	if ( $post_id > 0 && function_exists( 'get_field' ) ) {
		$value = get_field( 'hero_cta_label', $post_id );

		if ( is_string( $value ) ) {
			$local = trim( $value );
		}
	}

	if ( '' !== $local ) {
		return $local;
	}

	if ( '' !== $route_fallback ) {
		return $route_fallback;
	}

	return shpigovsky_get_hero_default_cta_label();
}
