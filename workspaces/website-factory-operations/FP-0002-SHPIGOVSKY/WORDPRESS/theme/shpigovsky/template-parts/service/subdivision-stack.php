<?php
/**
 * Service subdivision stack orchestrator.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = function_exists( 'shpigovsky_get_current_service_id' ) ? shpigovsky_get_current_service_id() : get_the_ID();

get_template_part( 'template-parts/service/inner-hero' );

if ( shpigovsky_section_block_enabled( $post_id, 'section_nav_visible' ) ) {
	get_template_part( 'template-parts/service/subnav' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_dependencies_visible' ) ) {
	get_template_part( 'template-parts/service/children' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_nature_visible' ) ) {
	get_template_part( 'template-parts/service/nature' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_mid_cta_visible' ) ) {
	get_template_part( 'template-parts/service/mid-cta' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_program_visible' ) ) {
	get_template_part( 'template-parts/service/program' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_stages_visible' ) ) {
	get_template_part( 'template-parts/service/stages' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_approach_visible' ) ) {
	get_template_part( 'template-parts/service/team-stats' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_clinic_landscape_visible' ) ) {
	get_template_part( 'template-parts/home/clinic-landscape' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_specialists_visible' ) ) {
	get_template_part(
		'template-parts/home/specialists',
		null,
		array(
			'section_id' => 'service-subdivision-specialists',
			'heading_id' => 'service-subdivision-specialists-heading',
		)
	);
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_founder_quote_visible' ) ) {
	get_template_part( 'template-parts/home/founder-quote' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_comfort_visible' ) ) {
	get_template_part(
		'template-parts/home/comfort',
		null,
		array(
			'section_id' => 'service-subdivision-comfort',
			'heading_id' => 'service-subdivision-comfort-heading',
		)
	);
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_reviews_visible' ) ) {
	get_template_part( 'template-parts/home/reviews' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_faq_visible' ) ) {
	get_template_part( 'template-parts/service/faq' );
}

if ( shpigovsky_section_block_enabled( $post_id, 'section_final_form_visible' ) ) {
	get_template_part( 'template-parts/components/final-form' );
}
