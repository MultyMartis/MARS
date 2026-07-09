<?php
/**
 * Template part: components/blog-related-card.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$item = wp_parse_args(
	$args ?? array(),
	array(
		'title'        => '',
		'url'          => '',
		'image_url'    => '',
		'image_width'  => 1216,
		'image_height' => 1632,
		'image_alt'    => '',
		'link_label'   => 'Читать',
	)
);

$title = trim( (string) $item['title'] );
$url   = trim( (string) $item['url'] );

if ( '' === $title || '' === $url ) {
	return;
}
?>
<article class="blog-related-card">
	<a class="blog-related-card__image-link" href="<?php echo esc_url( $url ); ?>">
		<img
			class="blog-related-card__image"
			src="<?php echo esc_url( (string) $item['image_url'] ); ?>"
			width="<?php echo esc_attr( (string) $item['image_width'] ); ?>"
			height="<?php echo esc_attr( (string) $item['image_height'] ); ?>"
			alt="<?php echo esc_attr( (string) $item['image_alt'] ); ?>"
			loading="lazy"
			decoding="async"
		>
	</a>
	<div class="blog-related-card__body">
		<h3 class="blog-related-card__title">
			<a class="blog-related-card__title-link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
		</h3>
		<p class="blog-related-card__read-more">
			<a class="blog-related-card__read-more-link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( (string) $item['link_label'] ); ?></a>
		</p>
	</div>
</article>
