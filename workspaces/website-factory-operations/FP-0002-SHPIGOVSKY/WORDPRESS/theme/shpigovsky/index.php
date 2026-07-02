<?php
/**
 * Main template — last-resort fallback loop.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php if ( have_posts() ) : ?>
		<?php
		while ( have_posts() ) :
			the_post();
			?>
			<article <?php post_class( 'shpigovsky-skeleton__article' ); ?>>
				<h1><?php the_title(); ?></h1>
				<?php the_content(); ?>
			</article>
			<?php
		endwhile;
		?>
	<?php else : ?>
		<p><?php esc_html_e( 'Контент не найден.', 'shpigovsky' ); ?></p>
	<?php endif; ?>
</main>
<?php
get_footer();
