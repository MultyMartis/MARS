<?php
/**
 * Blog archive list — V9-06E26B.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$archive_title = shpigovsky_get_blog_archive_title();
$archive_intro = shpigovsky_get_blog_archive_intro();
?>
<section class="blog-archive" aria-labelledby="blog-archive-heading">
	<div class="container blog-archive__container">
		<h1 class="blog-archive__heading" id="blog-archive-heading"><?php echo esc_html( $archive_title ); ?></h1>

		<?php if ( '' !== $archive_intro ) : ?>
			<p class="blog-archive__intro block-whith-red-line"><?php echo esc_html( $archive_intro ); ?></p>
		<?php endif; ?>

		<?php if ( have_posts() ) : ?>
			<div class="blog-archive__grid" data-reveal-group>
				<?php
				while ( have_posts() ) :
					the_post();
					get_template_part(
						'template-parts/components/blog-archive-card',
						null,
						shpigovsky_build_blog_archive_card_args( get_the_ID() )
					);
				endwhile;
				?>
			</div>
			<?php get_template_part( 'template-parts/blog/pagination' ); ?>
		<?php else : ?>
			<?php get_template_part( 'template-parts/blog/empty-state' ); ?>
		<?php endif; ?>
	</div>
</section>
