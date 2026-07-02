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
<main class="shpigovsky-skeleton shpigovsky-skeleton--legal" id="main-content">
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
	get_template_part( 'template-parts/legal/document-page' );
	?>
</main>
<?php
get_footer();
