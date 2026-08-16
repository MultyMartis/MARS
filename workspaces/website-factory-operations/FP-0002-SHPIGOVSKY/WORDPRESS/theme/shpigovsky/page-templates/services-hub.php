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

	if ( shpigovsky_services_hub_list_enabled( 'services_hub_nav_visible' ) ) {
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
	}

	get_template_part( 'template-parts/services-hub/service-groups' );
	get_template_part( 'template-parts/services-hub/rehabilitation-program' );
	get_template_part( 'template-parts/home/founder-quote' );
	get_template_part(
		'template-parts/home/comfort',
		null,
		array(
			'section_id' => 'services-comfort',
			'heading_id' => 'comfort-heading',
		)
	);

	if ( shpigovsky_services_hub_list_enabled( 'services_hub_secondary_cta_visible' ) ) {
		$cta_phone = shpigovsky_get_site_option( 'phone_primary' );
		$cta_phone = '' !== $cta_phone ? $cta_phone : '8 (925) 183-64-64';
		$v9_cta    = shpigovsky_get_v9_services_hub_program_copy()['secondary_cta'];

		$sec_title  = shpigovsky_get_services_hub_field( 'services_hub_secondary_cta_title' );
		$sec_sub    = shpigovsky_get_services_hub_field( 'services_hub_secondary_cta_subtitle' );
		$sec_button = shpigovsky_get_services_hub_field( 'services_hub_secondary_cta_button' );

		set_query_var(
			'shpigovsky_program_cta_band',
			array(
				'title'          => '' !== $sec_title ? $sec_title : $v9_cta['title'],
				'subtitle'       => '' !== $sec_sub ? $sec_sub : $v9_cta['subtitle'],
				'phone'          => $cta_phone,
				'phone_hint'     => function_exists( 'shpigovsky_get_cta_band_phone_hint' )
					? shpigovsky_get_cta_band_phone_hint( __( 'Или позвоните нам', 'shpigovsky' ) )
					: __( 'Или позвоните нам', 'shpigovsky' ),
				'button_label'   => '' !== $sec_button ? $sec_button : $v9_cta['button_label'],
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
	}

	get_template_part(
		'template-parts/services-hub/faq',
		null,
		array(
			'section_id' => 'services-faq',
		)
	);

	if ( shpigovsky_services_hub_list_enabled( 'services_hub_final_form_visible' ) ) {
		get_template_part( 'template-parts/components/final-form' );
	}
	?>
</main>
<?php
get_footer();
