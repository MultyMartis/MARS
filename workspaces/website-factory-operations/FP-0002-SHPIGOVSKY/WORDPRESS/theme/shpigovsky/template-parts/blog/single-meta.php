<?php
/**
 * Blog single metadata row — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id   = get_the_ID();
$show_date = shpigovsky_article_show_date( $post_id );
$reading   = shpigovsky_get_blog_card_reading_time( $post_id );
$show_auth = shpigovsky_article_show_author( $post_id );
$author    = shpigovsky_get_article_author_label( $post_id );

if ( ! $show_date && '' === $reading && ! $show_auth ) {
	return;
}
?>
<div class="blog-article-hero__meta">
	<?php if ( $show_date ) : ?>
		<time class="blog-article-hero__date" datetime="<?php echo esc_attr( get_the_date( 'Y-m-d', $post_id ) ); ?>"><?php echo esc_html( get_the_date( 'd.m.Y', $post_id ) ); ?></time>
	<?php endif; ?>
	<?php if ( '' !== $reading ) : ?>
		<?php if ( $show_date ) : ?>
			<span class="blog-article-hero__meta-separator" aria-hidden="true">·</span>
		<?php endif; ?>
		<span class="blog-article-hero__reading-time"><?php echo esc_html( $reading ); ?></span>
	<?php endif; ?>
	<?php if ( $show_auth && '' !== $author ) : ?>
		<?php if ( $show_date || '' !== $reading ) : ?>
			<span class="blog-article-hero__meta-separator" aria-hidden="true">·</span>
		<?php endif; ?>
		<span class="blog-article-hero__author"><?php echo esc_html( sprintf( 'Автор: %s', $author ) ); ?></span>
	<?php endif; ?>
</div>
