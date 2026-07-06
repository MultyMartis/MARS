<?php
/**
 * Service subdivision stack orchestrator.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<article <?php post_class( 'shpigovsky-service shpigovsky-service--subdivision' ); ?>>
	<?php
	get_template_part( 'template-parts/service/inner-hero' );
	get_template_part( 'template-parts/service/subnav' );
	get_template_part( 'template-parts/service/children' );
	get_template_part( 'template-parts/service/nature' );
	get_template_part( 'template-parts/service/mid-cta' );
	get_template_part( 'template-parts/service/program' );
	get_template_part( 'template-parts/service/stages' );
	get_template_part( 'template-parts/service/team-stats' );
	get_template_part( 'template-parts/home/clinic-landscape' );
	get_template_part(
		'template-parts/home/specialists',
		null,
		array(
			'section_id' => 'service-subdivision-specialists',
			'heading_id' => 'service-subdivision-specialists-heading',
		)
	);
	get_template_part( 'template-parts/home/founder-quote' );
	get_template_part(
		'template-parts/home/comfort',
		null,
		array(
			'section_id' => 'service-subdivision-comfort',
			'heading_id' => 'service-subdivision-comfort-heading',
		)
	);
	get_template_part( 'template-parts/home/reviews' );
	get_template_part( 'template-parts/service/faq' );
	get_template_part( 'template-parts/components/final-form' );
	?>
</article>
