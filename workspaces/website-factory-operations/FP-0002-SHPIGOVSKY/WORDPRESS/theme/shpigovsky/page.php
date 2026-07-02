<?php
/**
 * Generic page fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--page" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class( 'shpigovsky-skeleton__article' ); ?>>
			<h1><?php the_title(); ?></h1>
			<?php get_template_part( 'template-parts/page/plain-content' ); ?>
		</article>
		<?php
	endwhile;
	?>
</main>
<?php
get_footer();
