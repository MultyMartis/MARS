<?php
/**
 * Template Name: Legal
 * Route family: legal pages (4 routes)
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-plain-content__main" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php
	while ( have_posts() ) :
		the_post();
		get_template_part( 'template-parts/legal/document-page' );
	endwhile;
	?>
</main>
<?php
get_footer();
