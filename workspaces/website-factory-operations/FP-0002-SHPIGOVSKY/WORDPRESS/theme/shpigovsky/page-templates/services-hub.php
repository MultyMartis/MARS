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
<main class="shpigovsky-skeleton shpigovsky-skeleton--services-hub" id="main-content">
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
	shpigovsky_render_placeholder_notice( 'services-hub' );
	?>
</main>
<?php
get_footer();
