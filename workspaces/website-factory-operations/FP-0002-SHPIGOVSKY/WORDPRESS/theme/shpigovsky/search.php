<?php
/**
 * Search results — V9-06E62E / FIX01.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

global $wp_query;

$query_raw   = get_search_query( false );
$query_raw   = is_string( $query_raw ) ? trim( $query_raw ) : '';
$found_count = (int) $wp_query->found_posts;
$has_query   = '' !== $query_raw;
$has_results = $has_query && have_posts();
?>
<main class="page-search" id="main-content">
	<?php if ( function_exists( 'shpigovsky_breadcrumbs_enabled_for_context' ) && shpigovsky_breadcrumbs_enabled_for_context() ) : ?>
		<div class="internal-page-nav">
			<div class="container">
				<?php
				set_query_var( 'shpigovsky_breadcrumb_trail', shpigovsky_get_search_breadcrumb_trail() );
				shpigovsky_render_breadcrumbs( array( 'wrap' => 'none' ) );
				?>
			</div>
		</div>
	<?php endif; ?>

	<section class="page-search__content" aria-labelledby="page-search-title">
		<div class="container page-search__container">
			<h1 class="page-search__title" id="page-search-title"><?php esc_html_e( 'Результаты поиска', 'shpigovsky' ); ?></h1>
			<?php if ( $has_query ) : ?>
				<p class="page-search__summary"><?php echo esc_html( shpigovsky_search_found_summary( $found_count, $query_raw ) ); ?></p>
			<?php else : ?>
				<p class="page-search__summary"><?php esc_html_e( 'Введите поисковый запрос', 'shpigovsky' ); ?></p>
			<?php endif; ?>

			<?php if ( $has_results ) : ?>
				<ul class="page-search__list">
					<?php
					while ( have_posts() ) :
						the_post();
						get_template_part( 'template-parts/search/result-card' );
					endwhile;
					?>
				</ul>
				<?php get_template_part( 'template-parts/search/pagination' ); ?>
			<?php else : ?>
				<div class="page-search__empty">
					<?php if ( $has_query ) : ?>
						<p class="page-search__empty-text">
							<?php
							printf(
								/* translators: %s: search query */
								esc_html__( 'По запросу «%s» ничего не найдено. Попробуйте изменить формулировку.', 'shpigovsky' ),
								esc_html( $query_raw )
							);
							?>
						</p>
					<?php endif; ?>

					<div class="page-search__empty-form">
						<?php
						get_template_part(
							'searchform',
							null,
							array(
								'input_id'   => 'page-search-empty-field',
								'form_class' => 'site-search-form site-search-form--page',
								'show_intro' => false,
								'value'      => $query_raw,
							)
						);
						?>
					</div>

					<p class="page-search__empty-links">
						<a class="page-search__empty-link" href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'На главную', 'shpigovsky' ); ?></a>
						<span class="page-search__empty-sep" aria-hidden="true">·</span>
						<a class="page-search__empty-link" href="<?php echo esc_url( home_url( '/uslugi/' ) ); ?>"><?php esc_html_e( 'Услуги', 'shpigovsky' ); ?></a>
					</p>
				</div>
			<?php endif; ?>
		</div>
	</section>
</main>
<?php
get_footer();
