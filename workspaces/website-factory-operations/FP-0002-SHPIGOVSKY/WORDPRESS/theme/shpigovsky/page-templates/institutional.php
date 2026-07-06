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
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--institutional site-main site-main--institutional" id="main-content">
	<?php
	get_template_part( 'template-parts/institutional/hero' );
	shpigovsky_render_breadcrumbs();
	shpigovsky_render_internal_page_nav();
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class(); ?>>
			<h1 class="screen-reader-text"><?php the_title(); ?></h1>
		</article>
		<?php
	endwhile;
	get_template_part( 'template-parts/institutional/institutional-narrative' );
	?>
</main>
<?php
get_footer();
