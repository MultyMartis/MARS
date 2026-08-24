<?php
/**
 * Template Name: Specialists Hub
 * Route family: /specialisty/
 *
 * Page #1030 owns URL / H1 / SEO / optional intro / reusable-block selection.
 * Specialist cards come from shpigovsky_get_specialists_cards() (CPT, menu_order).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-plain-content__main site-main site-main--specialists-hub" id="main-content">
	<?php
	while ( have_posts() ) :
		the_post();
		get_template_part( 'template-parts/specialist/hub-content' );
	endwhile;
	?>
</main>
<?php
get_footer();
