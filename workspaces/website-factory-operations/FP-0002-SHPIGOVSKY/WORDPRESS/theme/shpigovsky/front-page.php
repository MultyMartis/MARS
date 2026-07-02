<?php
/**
 * Front page — home section orchestration boundary.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--front" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php
	get_template_part( 'template-parts/home/hero' );
	get_template_part( 'template-parts/home/feature-grid' );
	get_template_part( 'template-parts/home/treatment-prevention' );
	get_template_part( 'template-parts/home/rehabilitation-program' );
	get_template_part( 'template-parts/home/gallery' );
	get_template_part( 'template-parts/home/articles-teaser' );
	get_template_part( 'template-parts/home/faq' );
	get_template_part( 'template-parts/components/final-form' );
	?>
</main>
<?php
get_footer();
