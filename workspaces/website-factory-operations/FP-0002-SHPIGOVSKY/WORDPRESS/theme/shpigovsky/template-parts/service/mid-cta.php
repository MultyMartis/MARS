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
$cta      = shpigovsky_get_service_cta_band( $post_id );
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
