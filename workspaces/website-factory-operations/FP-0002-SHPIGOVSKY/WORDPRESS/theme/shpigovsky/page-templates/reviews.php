<?php
/**
 * Template Name: Reviews
 * Route family: /otzyvy/
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--reviews" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class(); ?>>
			<h1><?php the_title(); ?></h1>
		</article>
		<?php
	endwhile;
	get_template_part( 'template-parts/reviews/reviews-section' );
	get_template_part( 'template-parts/reviews/archive-list' );
	?>
</main>
<?php
get_footer();
