<?php
/**
 * Blog single hero — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id   = get_the_ID();
$trail     = shpigovsky_get_blog_single_breadcrumb_trail( $post_id );
$eyebrow   = shpigovsky_get_article_eyebrow( $post_id );
$lead      = shpigovsky_get_article_lead( $post_id );
$image     = shpigovsky_get_article_hero_image( $post_id );
$show_date = shpigovsky_article_show_date( $post_id );
$reading   = shpigovsky_get_blog_card_reading_time( $post_id );
$show_auth = shpigovsky_article_show_author( $post_id );
$author    = shpigovsky_get_article_author_label( $post_id );
$show_toc  = shpigovsky_article_show_toc( $post_id );
$toc_items = $show_toc ? shpigovsky_get_article_toc_items( $post_id ) : array();
$toc_title = shpigovsky_get_article_toc_title( $post_id );
?>
<header class="blog-article-hero">
	<div class="blog-article-hero__breadcrumbs">
		<nav class="breadcrumbs" aria-label="<?php esc_attr_e( 'Хлебные крошки', 'shpigovsky' ); ?>">
			<ol class="breadcrumbs__list">
				<?php foreach ( $trail as $index => $crumb ) : ?>
					<?php
					$label = isset( $crumb['label'] ) ? trim( (string) $crumb['label'] ) : '';
					$url   = isset( $crumb['url'] ) ? trim( (string) $crumb['url'] ) : '';
					$last  = $index === count( $trail ) - 1;

					if ( '' === $label ) {
						continue;
					}
					?>
					<li class="breadcrumbs__item<?php echo $last ? ' breadcrumbs__item--current' : ''; ?>"<?php echo $last ? ' aria-current="page"' : ''; ?>>
						<?php if ( ! $last && '' !== $url ) : ?>
							<a class="breadcrumbs__link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $label ); ?></a>
						<?php else : ?>
							<span class="breadcrumbs__current"><?php echo esc_html( $label ); ?></span>
						<?php endif; ?>
					</li>
				<?php endforeach; ?>
			</ol>
		</nav>
	</div>

	<div class="blog-article-hero__layout">
		<div class="blog-article-hero__editorial">
			<?php if ( '' !== $eyebrow ) : ?>
				<p class="blog-article-hero__eyebrow"><?php echo esc_html( $eyebrow ); ?></p>
			<?php endif; ?>
			<h1 class="blog-article-hero__title"><?php the_title(); ?></h1>
			<?php get_template_part( 'template-parts/blog/single-meta' ); ?>
			<?php if ( $show_toc && ! empty( $toc_items ) ) : ?>
				<?php
				set_query_var( 'shpigovsky_article_toc_title', $toc_title );
				set_query_var( 'shpigovsky_article_toc_items', $toc_items );
				get_template_part( 'template-parts/blog/toc' );
				?>
			<?php endif; ?>
		</div>

		<?php if ( ! empty( $image['url'] ) ) : ?>
			<figure class="blog-article-hero__media">
				<img
					src="<?php echo esc_url( $image['url'] ); ?>"
					width="<?php echo esc_attr( (string) $image['width'] ); ?>"
					height="<?php echo esc_attr( (string) $image['height'] ); ?>"
					alt="<?php echo esc_attr( $image['alt'] ); ?>"
					decoding="async"
					<?php echo has_post_thumbnail( $post_id ) ? '' : 'loading="lazy"'; ?>
				>
			</figure>
		<?php endif; ?>
	</div>

	<?php if ( '' !== $lead ) : ?>
		<div class="blog-article-hero__excerpt block-whith-red-line">
			<?php echo wp_kses_post( wpautop( $lead ) ); ?>
		</div>
	<?php endif; ?>
</header>
