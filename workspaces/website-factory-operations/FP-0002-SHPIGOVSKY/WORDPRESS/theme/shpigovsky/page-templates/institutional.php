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
<main class="shpigovsky-skeleton shpigovsky-skeleton--institutional" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php shpigovsky_render_internal_page_nav(); ?>
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class(); ?>>
			<h1><?php the_title(); ?></h1>
		</article>
		<?php
	endwhile;
	get_template_part( 'template-parts/institutional/institutional-narrative' );
	?>
</main>
<?php
get_footer();
