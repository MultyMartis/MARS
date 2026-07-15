<?php
/**
 * Direct static V9 section stack — general service stack (V9-06E45-FIX01 / V9-06E47).
 *
 * Layout order matches usluga-konechnaya-v1 / service_general stack (legacy alcohol_special).
 * Content SoT: ACF «Услуга — блоки страницы» (seeded). Alcohol PHP demos are emergency only.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();

// 1. services-inner-hero-v2 — KEEP_FOR_HERO (admin hero_media).
get_template_part( 'template-parts/service/inner-hero' );

// 2. internal-page-nav.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_nav_visible' ) ) {
	get_template_part( 'template-parts/service/subnav' );
}

// 3. Intro.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_intro_visible' ) ) {
	get_template_part( 'template-parts/service/intro' );
}

// 4. Bordered info.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_bordered_info_visible' ) ) {
	get_template_part( 'template-parts/service/bordered-info' );
}

// 5. Mid CTA.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_mid_cta_visible' ) ) {
	get_template_part( 'template-parts/service/mid-cta' );
}

// 6. Signs.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_signs_visible' ) ) {
	get_template_part( 'template-parts/service/signs' );
}

// 7. Approach — ACF-driven leaf approach when available; else programme_items partial.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_approach_visible' ) ) {
	$approach = function_exists( 'shpigovsky_get_general_approach_copy' )
		? shpigovsky_get_general_approach_copy( $post_id )
		: null;
	if ( is_array( $approach ) && ! empty( $approach['cards'] ) ) {
		get_template_part( 'template-parts/service/alcohol-direct-v9/approach' );
	} else {
		get_template_part( 'template-parts/service/approach' );
	}
}

// 8. clinic-landscape.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_clinic_landscape_visible' ) ) {
	get_template_part(
		'template-parts/home/clinic-landscape',
		null,
		array(
			'modifier_class' => 'service-leaf-landscape-v1',
		)
	);
}

// 9. services-program-v2.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_program_visible' ) ) {
	get_template_part( 'template-parts/service/program' );
}

// 10. stages — ACF-driven leaf stages when available; else shared stages partial.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_stages_visible' ) ) {
	$stages = function_exists( 'shpigovsky_get_general_stages_copy' )
		? shpigovsky_get_general_stages_copy( $post_id )
		: null;
	if ( is_array( $stages ) && ! empty( $stages['steps'] ) ) {
		get_template_part( 'template-parts/service/alcohol-direct-v9/stages' );
	} else {
		get_template_part( 'template-parts/service/stages' );
	}
}

// 11. corridor.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_corridor_visible' ) ) {
	get_template_part( 'template-parts/service/corridor' );
}

// 12. specialists — shared CPT cards (preserve historic alcohol visibility when unset).
$show_specialists = shpigovsky_general_block_enabled( $post_id, 'service_general_specialists_visible' );
if ( $show_specialists ) {
	$specialists_meta_set = metadata_exists( 'post', $post_id, 'service_general_specialists_visible' );
	if ( $specialists_meta_set || ( function_exists( 'shpigovsky_is_known_alcohol_service_page' ) && shpigovsky_is_known_alcohol_service_page( $post_id ) ) ) {
		get_template_part( 'template-parts/service/alcohol-direct-v9/specialists' );
	}
}

// 13–15. Shared V9 sections.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_founder_quote_visible' ) ) {
	get_template_part(
		'template-parts/home/founder-quote',
		null,
		array(
			'modal_source'   => 'service-leaf-founder',
			'modifier_class' => ' founder-quote--variant-b',
		)
	);
}

if ( shpigovsky_general_block_enabled( $post_id, 'service_general_comfort_visible' ) ) {
	get_template_part(
		'template-parts/home/comfort',
		null,
		array(
			'section_id' => 'service-leaf-comfort',
			'heading_id' => 'service-leaf-comfort-heading',
		)
	);
}

if ( shpigovsky_general_block_enabled( $post_id, 'service_general_reviews_visible' ) ) {
	get_template_part(
		'template-parts/home/reviews',
		null,
		array(
			'section_id' => 'service-leaf-reviews',
		)
	);
}

// 15b. Child services tile menu — before FAQ.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_children_visible' ) ) {
	get_template_part( 'template-parts/service/child-services' );
}

// 16. FAQ.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_faq_visible' ) ) {
	$faq_items = function_exists( 'shpigovsky_get_general_faq_items' )
		? shpigovsky_get_general_faq_items( $post_id )
		: array();
	if ( ! empty( $faq_items ) ) {
		get_template_part( 'template-parts/service/alcohol-direct-v9/faq' );
	} else {
		get_template_part( 'template-parts/service/faq' );
	}
}

// 17. final-form.
if ( shpigovsky_general_block_enabled( $post_id, 'service_general_final_form_visible' ) ) {
	get_template_part(
		'template-parts/components/final-form',
		null,
		array(
			'lead_source' => 'service-leaf-final-section',
			'heading_id'  => 'service-leaf-final-form-heading',
		)
	);
}
