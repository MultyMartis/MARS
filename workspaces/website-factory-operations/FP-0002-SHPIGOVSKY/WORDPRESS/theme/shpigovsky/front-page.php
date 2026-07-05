<?php
/**
 * Front page — V9 Home main orchestration (D9-D static transplant).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

get_template_part( 'template-parts/home/hero' );

if ( is_front_page() ) {
	echo '</div>' . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
}
?>
<main class="site-main site-main--front" id="main-content">
	<?php
	get_template_part( 'template-parts/home/recovery-intro' );
	get_template_part( 'template-parts/home/founder-quote' );
	get_template_part( 'template-parts/home/treatment-prevention' );
	get_template_part( 'template-parts/home/gallery' );
	get_template_part( 'template-parts/home/why-us' );
	get_template_part( 'template-parts/home/staff-photo' );
	get_template_part( 'template-parts/home/feature-grid' );
	get_template_part( 'template-parts/home/clinic-landscape' );
	get_template_part( 'template-parts/home/recovery-life' );
	get_template_part( 'template-parts/home/reviews' );
	get_template_part( 'template-parts/home/rehabilitation-requirements' );
	get_template_part( 'template-parts/home/rehabilitation-program' );
	get_template_part( 'template-parts/home/genotyping' );
	get_template_part( 'template-parts/home/comfort' );
	get_template_part( 'template-parts/home/videos' );
	get_template_part( 'template-parts/home/specialists' );
	get_template_part( 'template-parts/home/articles-teaser' );
	get_template_part( 'template-parts/home/faq' );
	get_template_part( 'template-parts/components/final-form' );
	?>
</main>
<?php
get_footer();
