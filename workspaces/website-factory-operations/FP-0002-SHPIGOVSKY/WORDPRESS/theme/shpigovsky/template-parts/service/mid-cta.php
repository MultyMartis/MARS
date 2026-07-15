<?php
/**
 * Template part: service/mid-cta.php
 *
 * Mid-page CTA band wrapper for service stacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id  = shpigovsky_get_current_service_id();
$variant  = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );

if ( shpigovsky_is_service_general_variant( $variant ) ) {
	$phone = shpigovsky_get_site_option( 'phone_primary' );
	$phone = '' !== $phone ? $phone : '8 (925) 183-64-64';
	$cta   = array(
		'title'        => 'Запишитесь на встречу',
		'subtitle'     => 'Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.',
		'phone'        => $phone,
		'phone_hint'   => 'Или позвоните нам',
		'button_label' => 'Записаться',
		'source'       => 'service-leaf-cta-01',
	);
} else {
	$cta = shpigovsky_get_service_cta_band( $post_id );
}
$section_id = 'subdivision' === $variant ? 'service-subdivision-start' : 'service-leaf-cta-01';

if ( 'subdivision' === $variant ) {
	$cta['source'] = 'service-subdivision-cta-01';
}

set_query_var(
	'shpigovsky_program_cta_band',
	array_merge(
		$cta,
		array(
			'section_id'   => $section_id,
			'heading_id'   => $section_id . '-heading',
			'heading_text' => $cta['title'],
			'wrap_section' => true,
			'button_first' => true,
			'margin_flush' => true,
		)
	)
);

get_template_part( 'template-parts/components/program-cta-band' );
