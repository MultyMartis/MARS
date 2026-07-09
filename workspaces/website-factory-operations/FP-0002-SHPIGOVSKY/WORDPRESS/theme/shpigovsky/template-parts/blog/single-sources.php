<?php
/**
 * Blog single sources — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$sources = shpigovsky_get_article_sources( get_the_ID() );

if ( empty( $sources ) ) {
	return;
}
?>
<section class="blog-article-sources" aria-labelledby="blog-article-sources-label">
	<div class="blog-article-sources__container container">
		<div class="blog-article-sources__content">
			<h2 class="blog-article-sources__label" id="blog-article-sources-label"><?php esc_html_e( 'Источники:', 'shpigovsky' ); ?></h2>
			<div class="blog-article-sources__list">
				<?php foreach ( $sources as $source_text ) : ?>
					<p><?php echo wp_kses_post( $source_text ); ?></p>
				<?php endforeach; ?>
			</div>
		</div>
	</div>
</section>
