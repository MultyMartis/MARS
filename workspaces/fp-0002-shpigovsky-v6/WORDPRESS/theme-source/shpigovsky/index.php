<?php
/**
 * Main template — foundation placeholder.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-foundation" id="main-content">
	<div class="shpigovsky-foundation__inner">
		<h1><?php esc_html_e( 'FP-0002 LOCAL WORDPRESS FOUNDATION', 'shpigovsky' ); ?></h1>
		<p><?php esc_html_e( 'Frontend integration has not started.', 'shpigovsky' ); ?></p>
		<?php if ( have_posts() ) : ?>
			<?php
			while ( have_posts() ) :
				the_post();
				?>
				<article <?php post_class( 'shpigovsky-foundation__content' ); ?>>
					<?php the_title( '<h2>', '</h2>' ); ?>
					<?php the_content(); ?>
				</article>
				<?php
			endwhile;
			?>
		<?php endif; ?>
	</div>
</main>
<?php
get_footer();
