<?php
/**
 * Template part: service/inner-hero.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id    = shpigovsky_get_current_service_id();
$variant    = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$title_id   = 'subdivision' === $variant ? 'service-subdivision-hero-title' : 'service-leaf-hero-title';
$hero_title = shpigovsky_get_service_hero_title( $post_id );
$hero_lead  = shpigovsky_get_service_field( $post_id, 'hero_lead' );
$eyebrow    = shpigovsky_get_service_field( $post_id, 'hero_eyebrow' );
$image      = shpigovsky_get_service_hero_image_resolved( $post_id, $variant );
$cta_route  = '';

if ( '' === $eyebrow ) {
	$eyebrow = __( 'Заболевания, которые мы лечим', 'shpigovsky' );
}

if ( shpigovsky_is_service_general_variant( $variant ) && shpigovsky_service_uses_alcohol_v9_static_copy( $post_id ) ) {
	if ( '' === $hero_title || 'Лечение алкогольной зависимости' === $hero_title ) {
		$hero_title = 'Центр лечения алкогольной зависимости';
	}

	if ( '' === $hero_lead ) {
		$hero_lead = 'В центре реабилитации Шпиговский Дом мы понимаем, что каждый человек уникален, поэтому мы не предложим вам универсальный подход к лечению. Путь в борьбе с алкогольной зависимостью может быть только индивидуальным.';
	}

	$cta_route = 'Записаться на консультацию';
}

if ( '' === $hero_title ) {
	$hero_title = get_the_title( $post_id );
}

$cta_label = shpigovsky_get_local_hero_cta_label( $post_id, $cta_route );

if ( shpigovsky_is_service_general_variant( $variant ) && shpigovsky_service_uses_alcohol_v9_static_copy( $post_id ) && 'Записаться' === $cta_label ) {
	$cta_label = 'Записаться на консультацию';
}

$cta_source = 'subdivision' === $variant ? 'service-subdivision-hero-v1' : 'service-leaf-hero-v1';

get_template_part(
	'template-parts/shared/services-inner-hero-v2',
	null,
	array(
		'title_id'     => $title_id,
		'eyebrow'      => $eyebrow,
		'title'        => $hero_title,
		'lead'         => $hero_lead,
		'cta_label'    => $cta_label,
		'cta_source'   => $cta_source,
		'image_url'    => $image['url'],
		'image_alt'    => $image['alt'],
		'image_width'  => $image['width'],
		'image_height' => $image['height'],
	)
);
