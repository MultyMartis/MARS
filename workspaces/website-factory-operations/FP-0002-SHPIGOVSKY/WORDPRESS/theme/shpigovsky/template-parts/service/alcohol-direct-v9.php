<?php
/**
 * Direct static V9 section stack — usluga-konechnaya-v1.html authority.
 *
 * Replaces semantic ACF/home-partial orchestration for alcohol-special route only.
 * Hero admin image system preserved via inner-hero partial.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

// 1. services-inner-hero-v2 — KEEP_FOR_HERO (admin hero_media).
get_template_part( 'template-parts/service/inner-hero' );

// 2. internal-page-nav — static V9 alcohol anchor list via subnav helper.
get_template_part( 'template-parts/service/subnav' );

// 3–6. Direct V9 leaf sections (intro/bordered-info use alcohol-special branches in shared partials).
get_template_part( 'template-parts/service/intro' );
get_template_part( 'template-parts/service/bordered-info' );
get_template_part( 'template-parts/service/mid-cta' );
get_template_part( 'template-parts/service/signs' );

// 7. service-leaf-approach-v1 — direct V9 (not ACF programme_items).
get_template_part( 'template-parts/service/alcohol-direct-v9/approach' );

// 8. clinic-landscape — static V9 markup proven in home/clinic-landscape.php.
get_template_part(
	'template-parts/home/clinic-landscape',
	null,
	array(
		'modifier_class' => 'service-leaf-landscape-v1',
	)
);

// 9. services-program-v2 — alcohol-special branch in program.php.
get_template_part( 'template-parts/service/program' );

// 10. service-leaf-stages-v1 — direct V9 (not ACF stages).
get_template_part( 'template-parts/service/alcohol-direct-v9/stages' );

// 11. service-leaf-corridor-v1.
get_template_part( 'template-parts/service/corridor' );

// 12. specialists — direct V9 (not home/specialists.php; requires Swiper on alcohol leaf).
get_template_part( 'template-parts/service/alcohol-direct-v9/specialists' );

// 13–15. Shared V9 sections with service-leaf IDs.

get_template_part(
	'template-parts/home/founder-quote',
	null,
	array(
		'modal_source'   => 'service-leaf-founder',
		'modifier_class' => ' founder-quote--variant-b',
	)
);

get_template_part(
	'template-parts/home/comfort',
	null,
	array(
		'section_id' => 'service-leaf-comfort',
		'heading_id' => 'service-leaf-comfort-heading',
	)
);

get_template_part(
	'template-parts/home/reviews',
	null,
	array(
		'section_id' => 'service-leaf-reviews',
	)
);

// 16. faq — direct V9 static items (not ACF faq_items).
get_template_part( 'template-parts/service/alcohol-direct-v9/faq' );

// 17. final-form — static V9 placement.
get_template_part(
	'template-parts/components/final-form',
	null,
	array(
		'lead_source' => 'service-leaf-final-section',
		'heading_id'  => 'service-leaf-final-form-heading',
	)
);
