<?php
/**
 * Template part: services-hub/hero.php
 *
 * V9 services hub hero — services-inner-hero-v2 with ACF + theme asset fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

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

get_template_part(
	'template-parts/shared/services-inner-hero-v2',
	null,
	array(
		'title_id'     => 'services-inner-hero-v2-title',
		'eyebrow'      => $eyebrow,
		'title'        => $title,
		'lead'         => $lead,
		'cta_label'    => shpigovsky_get_hero_default_cta_label(),
		'cta_source'   => 'services-hero-v2',
		'image_url'    => $image['url'],
		'image_alt'    => $image['alt'],
		'image_width'  => $image['width'],
		'image_height' => $image['height'],
	)
);
