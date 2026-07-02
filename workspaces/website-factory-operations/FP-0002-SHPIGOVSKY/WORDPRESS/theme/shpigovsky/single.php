<?php
/**
 * Single blog post.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--single-post" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php
	while ( have_posts() ) :
		the_post();
		?>
		<article <?php post_class( 'shpigovsky-skeleton__article' ); ?>>
			<header class="shpigovsky-skeleton__entry-header">
				<h1><?php the_title(); ?></h1>
				<p class="shpigovsky-skeleton__entry-date">
					<time datetime="<?php echo esc_attr( get_the_date( DATE_W3C ) ); ?>"><?php echo esc_html( get_the_date() ); ?></time>
				</p>
			</header>
			<?php get_template_part( 'template-parts/blog/article-content' ); ?>
			<?php get_template_part( 'template-parts/blog/article-lower-stack' ); ?>
		</article>
		<?php
	endwhile;
	?>
</main>
<?php
get_footer();
