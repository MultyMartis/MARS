<?php
/**
 * Template Name: Services Hub
 * Route family: /uslugi/
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-uslugi-v2__main site-main site-main--services-hub" id="main-content">
	<?php
	get_template_part( 'template-parts/services-hub/hero' );

	set_query_var(
		'shpigovsky_breadcrumb_trail',
		array(
			array(
				'label' => __( 'Главная', 'shpigovsky' ),
				'url'   => home_url( '/' ),
			),
			array(
				'label' => __( 'Услуги лечения и профилактики', 'shpigovsky' ),
				'url'   => '',
			),
		)
	);
	set_query_var( 'shpigovsky_subnav_items', shpigovsky_get_services_hub_subnav_items() );
	get_template_part( 'template-parts/components/internal-page-nav' );

	get_template_part( 'template-parts/services-hub/service-groups' );
	get_template_part( 'template-parts/services-hub/rehabilitation-program' );
	get_template_part( 'template-parts/home/founder-quote' );
	get_template_part(
		'template-parts/home/comfort',
		null,
		array(
			'section_id'  => 'services-comfort',
			'heading_id'  => 'comfort-heading',
		)
	);

	$cta_phone = shpigovsky_get_site_option( 'phone_primary' );
	$cta_phone = '' !== $cta_phone ? $cta_phone : '8 (925) 183-64-64';
	$v9_cta    = shpigovsky_get_v9_services_hub_program_copy()['secondary_cta'];
	set_query_var(
		'shpigovsky_program_cta_band',
		array(
			'title'          => $v9_cta['title'],
			'subtitle'       => $v9_cta['subtitle'],
			'phone'          => $cta_phone,
			'phone_hint'     => '',
			'button_label'   => $v9_cta['button_label'],
			'modal_source'   => $v9_cta['source'],
			'section_id'     => '',
			'heading_id'     => '',
			'heading_text'   => '',
			'wrap_section'   => false,
			'wrap_container' => true,
			'button_first'   => false,
			'margin_flush'   => false,
		)
	);
	get_template_part( 'template-parts/components/program-cta-band' );

	get_template_part(
		'template-parts/services-hub/faq',
		null,
		array(
			'section_id' => 'services-faq',
		)
	);
	get_template_part( 'template-parts/components/final-form' );
	?>
</main>
<?php
get_footer();
