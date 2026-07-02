<?php
/**
 * Search results — minimal skeleton.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--search" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<h1><?php printf( esc_html__( 'Результаты поиска: %s', 'shpigovsky' ), esc_html( get_search_query() ) ); ?></h1>
	<?php if ( have_posts() ) : ?>
		<ul class="shpigovsky-skeleton__search-results">
			<?php
			while ( have_posts() ) :
				the_post();
				?>
				<li><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></li>
				<?php
			endwhile;
			?>
		</ul>
	<?php else : ?>
		<p><?php esc_html_e( 'Ничего не найдено.', 'shpigovsky' ); ?></p>
	<?php endif; ?>
</main>
<?php
get_footer();
