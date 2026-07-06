<?php
/**
 * Service alcohol-special stack orchestrator — V9 usluga-konechnaya-v1 authority.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<article <?php post_class( 'shpigovsky-service shpigovsky-service--alcohol' ); ?>>
	<?php
	get_template_part( 'template-parts/service/inner-hero' );
	get_template_part( 'template-parts/service/subnav' );
	get_template_part( 'template-parts/service/intro' );
	get_template_part( 'template-parts/service/bordered-info' );
	get_template_part( 'template-parts/service/mid-cta' );
	get_template_part( 'template-parts/service/signs' );
	get_template_part( 'template-parts/service/approach' );
	get_template_part(
		'template-parts/home/clinic-landscape',
		null,
		array(
			'modifier_class' => 'service-leaf-landscape-v1',
		)
	);
	get_template_part( 'template-parts/service/program' );
	get_template_part( 'template-parts/service/stages' );
	get_template_part( 'template-parts/service/corridor' );
	get_template_part(
		'template-parts/home/specialists',
		null,
		array(
			'section_id' => 'service-leaf-specialists',
			'heading_id' => 'service-leaf-specialists-heading',
		)
	);
	get_template_part(
		'template-parts/home/founder-quote',
		null,
		array(
			'modal_source' => 'service-leaf-founder',
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
	get_template_part( 'template-parts/service/faq' );
	get_template_part(
		'template-parts/components/final-form',
		null,
		array(
			'lead_source' => 'service-leaf-final-section',
			'heading_id'  => 'service-leaf-final-form-heading',
		)
	);
	?>
</article>
