<?php
/**
 * Blog single table of contents — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$toc_title = get_query_var( 'shpigovsky_article_toc_title', shpigovsky_get_article_toc_title( get_the_ID() ) );
$toc_items = get_query_var( 'shpigovsky_article_toc_items', shpigovsky_get_article_toc_items( get_the_ID() ) );

if ( empty( $toc_items ) || ! is_array( $toc_items ) ) {
	return;
}
?>
<nav class="blog-article-hero__toc" aria-label="<?php esc_attr_e( 'Оглавление статьи', 'shpigovsky' ); ?>">
	<div class="blog-article-hero__toc-title"><?php echo esc_html( $toc_title ); ?></div>
	<ul>
		<?php foreach ( $toc_items as $item ) : ?>
			<?php
			$label = isset( $item['label'] ) ? trim( (string) $item['label'] ) : '';
			$anchor = isset( $item['id'] ) ? trim( (string) $item['id'] ) : '';

			if ( '' === $label || '' === $anchor ) {
				continue;
			}
			?>
			<li><a href="<?php echo esc_url( '#' . $anchor ); ?>"><?php echo esc_html( $label ); ?></a></li>
		<?php endforeach; ?>
	</ul>
</nav>
