<?php
/**
 * Normalized search result card — V9-06E62E.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = get_the_ID();
$title   = get_the_title( $post_id );
$url     = get_permalink( $post_id );

if ( ! is_string( $title ) || '' === trim( $title ) || ! is_string( $url ) || '' === $url ) {
	return;
}

$type_label = shpigovsky_search_result_type_label( $post_id );
$excerpt    = shpigovsky_search_result_excerpt( $post_id );
$image      = shpigovsky_search_result_image( $post_id );
?>
<li class="search-result-card">
	<article class="search-result-card__article">
		<?php if ( is_array( $image ) && ! empty( $image['url'] ) ) : ?>
			<a class="search-result-card__media" href="<?php echo esc_url( $url ); ?>" tabindex="-1" aria-hidden="true">
				<img
					class="search-result-card__image"
					src="<?php echo esc_url( $image['url'] ); ?>"
					<?php if ( ! empty( $image['width'] ) ) : ?>
						width="<?php echo esc_attr( (string) $image['width'] ); ?>"
					<?php endif; ?>
					<?php if ( ! empty( $image['height'] ) ) : ?>
						height="<?php echo esc_attr( (string) $image['height'] ); ?>"
					<?php endif; ?>
					alt=""
					loading="lazy"
					decoding="async"
				>
			</a>
		<?php endif; ?>

		<div class="search-result-card__body">
			<p class="search-result-card__type"><?php echo esc_html( $type_label ); ?></p>
			<h2 class="search-result-card__title">
				<a class="search-result-card__title-link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
			</h2>
			<?php if ( '' !== $excerpt ) : ?>
				<p class="search-result-card__excerpt"><?php echo esc_html( $excerpt ); ?></p>
			<?php endif; ?>
		</div>
	</article>
</li>
