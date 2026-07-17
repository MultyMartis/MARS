<?php
/**
 * Template Name: Institutional
 * Route family: /o-centre/ + children
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

$page_id  = (int) get_queried_object_id();
$is_about = shpigovsky_is_about_hub_page( $page_id );
?>
<main class="site-main site-main--institutional<?php echo $is_about ? ' page-o-centre__main' : ''; ?>" id="main-content">
	<?php
	get_template_part( 'template-parts/institutional/hero' );

	if ( $is_about ) {
		set_query_var( 'shpigovsky_breadcrumb_trail', shpigovsky_get_about_hub_breadcrumb_trail() );
		set_query_var( 'shpigovsky_subnav_items', shpigovsky_get_v9_about_hub_subnav_items() );
		shpigovsky_render_internal_page_nav();

		get_template_part( 'template-parts/institutional/institutional-narrative' );
		get_template_part( 'template-parts/institutional/founder-quote' );
		get_template_part( 'template-parts/institutional/who-we-treat' );
		get_template_part( 'template-parts/institutional/approach-band' );
		get_template_part( 'template-parts/home/staff-photo' );
		get_template_part( 'template-parts/home/feature-grid' );
		get_template_part( 'template-parts/home/clinic-landscape' );
		get_template_part( 'template-parts/institutional/about-program' );
		get_template_part( 'template-parts/institutional/infrastructure-narrative' );

		set_query_var( 'shpigovsky_program_cta_band', shpigovsky_get_about_guest_cta_band( 'o-centre-guest-cta' ) );
		get_template_part( 'template-parts/components/program-cta-band' );

		get_template_part(
			'template-parts/home/specialists',
			null,
			array(
				'section_id' => 'specialists',
				'heading_id' => 'o-centre-specialists-heading',
			)
		);
		get_template_part(
			'template-parts/home/reviews',
			null,
			array(
				'section_id' => 'reviews',
			)
		);
		get_template_part(
			'template-parts/components/final-form',
			null,
			array(
				'heading_id'             => 'o-centre-final-form-heading',
				'heading_text'           => __( 'Остались вопросы?', 'shpigovsky' ),
				'lead_text'              => __( 'Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь', 'shpigovsky' ),
				'lead_source'            => 'o-centre-final-section',
				'section_modifier_class' => '',
			)
		);
	} else {
		// Non-hub institutional pages: single internal-page-nav shell (no duplicate wrappers).
		shpigovsky_render_breadcrumbs(
			array(
				'wrap' => 'internal',
			)
		);
		while ( have_posts() ) :
			the_post();
			?>
			<article <?php post_class(); ?>>
				<h1 class="screen-reader-text"><?php the_title(); ?></h1>
			</article>
			<?php
		endwhile;
	}
	?>
</main>
<?php
get_footer();
