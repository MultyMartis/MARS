<?php
/**
 * Specialist CPT single — PROD-P11.
 * Reuses P08 structured profile; independent of Generic Content page template.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-plain-content__main" id="main-content" data-layout-mode="specialist-cpt">
	<?php
	shpigovsky_render_breadcrumbs();
	while ( have_posts() ) :
		the_post();
		get_template_part( 'template-parts/specialist/profile' );
	endwhile;
	?>
</main>
<?php
get_footer();
