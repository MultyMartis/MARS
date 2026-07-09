<?php
/**
 * Blog single related posts — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$related = shpigovsky_get_article_related_posts( get_the_ID() );

if ( empty( $related ) ) {
	return;
}

$blog_url = get_permalink( shpigovsky_get_blog_posts_page_id() );
if ( ! is_string( $blog_url ) || '' === $blog_url ) {
	$blog_url = home_url( '/blog/' );
}
?>
<section data-reveal class="blog-article-related" aria-labelledby="blog-article-related-label">
	<div class="blog-article-related__container container">
		<div class="blog-article-related__head">
			<h2 class="blog-article-related__heading" id="blog-article-related-label"><?php esc_html_e( 'Рекомендуем к прочтению', 'shpigovsky' ); ?></h2>
			<a class="blog-article-related__all-link" href="<?php echo esc_url( $blog_url ); ?>">
				<span class="blog-article-related__all-text"><?php esc_html_e( 'все статьи', 'shpigovsky' ); ?></span>
				<span class="blog-article-related__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>
		<div class="blog-article-related__grid">
			<?php foreach ( $related as $card_args ) : ?>
				<?php get_template_part( 'template-parts/components/blog-related-card', null, $card_args ); ?>
			<?php endforeach; ?>
		</div>
	</div>
</section>
