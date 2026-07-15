<?php
/**
 * Template part: services-hub/hero.php
 *
 * V9-06E43: multi-slide services-inner-hero-v2 from services_hero_slides + Swiper when count > 1.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$page_id    = shpigovsky_get_services_hub_page_id();
$raw_slides = shpigovsky_get_services_hub_repeater( 'services_hero_slides' );
$slides     = array();

if ( is_array( $raw_slides ) ) {
	foreach ( $raw_slides as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		if ( array_key_exists( 'item_enabled', $row ) && ! (bool) $row['item_enabled'] ) {
			continue;
		}

		$eyebrow = isset( $row['eyebrow'] ) ? trim( (string) $row['eyebrow'] ) : '';
		$title   = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
		$lead    = isset( $row['lead'] ) ? trim( (string) $row['lead'] ) : '';
		$cta     = isset( $row['cta_label'] ) ? trim( (string) $row['cta_label'] ) : '';
		$image   = shpigovsky_resolve_hero_image( isset( $row['image'] ) ? $row['image'] : null, 'services_hub' );

		if ( '' === $eyebrow && '' === $title && '' === $lead && '' === $image['url'] ) {
			continue;
		}

		$slides[] = array(
			'eyebrow'   => $eyebrow,
			'title'     => $title,
			'lead'      => $lead,
			'cta_label' => $cta,
			'image'     => $image,
		);
	}
}

if ( empty( $slides ) ) {
	$intro   = shpigovsky_get_services_hub_field( 'services_hub_intro' );
	$eyebrow = shpigovsky_get_services_hub_field( 'hero_eyebrow' );
	$title   = shpigovsky_get_services_hub_field( 'hero_title_override' );
	$image   = shpigovsky_get_services_hub_hero_image();

	if ( '' === $eyebrow ) {
		$eyebrow = __( 'Заболевания, которые мы лечим', 'shpigovsky' );
	}

	if ( '' === $title ) {
		$title = __( 'Лечение и профилактика', 'shpigovsky' );
	}

	$lead = '' !== $intro
		? $intro
		: __( 'Зависимость, тревога, нарушение пищевого поведения — у каждого из этих состояний есть своя биология, своя психология и своя точка, где что-то пошло не так. Нас интересует не только то, что происходит, но и почему это происходит именно с вами, именно сейчас.', 'shpigovsky' );

	$slides[] = array(
		'eyebrow'   => $eyebrow,
		'title'     => $title,
		'lead'      => $lead,
		'cta_label' => '',
		'image'     => $image,
	);
}

$default_cta = shpigovsky_get_local_hero_cta_label( $page_id );
$slide_count = count( $slides );
$is_slider   = $slide_count > 1;

$autoplay_enabled = $is_slider && shpigovsky_services_hub_list_enabled( 'services_hero_autoplay_enabled' );
$arrows_enabled   = $is_slider && shpigovsky_services_hub_list_enabled( 'services_hero_arrows_enabled' );
$dots_enabled     = $is_slider && shpigovsky_services_hub_list_enabled( 'services_hero_dots_enabled' );
$autoplay_delay   = (int) shpigovsky_get_services_hub_field( 'services_hero_autoplay_delay' );
if ( $autoplay_delay < 1000 ) {
	$autoplay_delay = 5000;
}

get_template_part(
	'template-parts/shared/services-inner-hero-v2',
	null,
	array(
		'title_id'          => 'services-inner-hero-v2-title',
		'cta_source'        => 'services-hero-v2',
		'default_cta_label' => $default_cta,
		'slides'            => $slides,
		'is_slider'         => $is_slider,
		'autoplay_enabled'  => $autoplay_enabled,
		'autoplay_delay'    => $autoplay_delay,
		'arrows_enabled'    => $arrows_enabled,
		'dots_enabled'      => $dots_enabled,
	)
);
