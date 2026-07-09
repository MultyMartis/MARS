<?php
/**
 * Single blog post — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-blog-article__main" id="main-content">
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class( 'blog-article' ); ?>>
			<div class="blog-article__container container">
				<?php
				get_template_part( 'template-parts/blog/single-hero' );
				get_template_part( 'template-parts/blog/single-content' );
				?>
			</div>
			<?php
			get_template_part( 'template-parts/blog/single-conclusion' );
			get_template_part( 'template-parts/blog/single-sources' );
			get_template_part( 'template-parts/blog/faq' );
			get_template_part( 'template-parts/blog/related' );
			?>
		</article>
		<?php
		get_template_part( 'template-parts/blog/single-lower-stack' );
	endwhile;
	?>
</main>
<?php
get_footer();
