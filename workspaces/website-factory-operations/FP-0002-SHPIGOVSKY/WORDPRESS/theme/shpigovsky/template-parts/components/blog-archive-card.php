<?php
/**
 * Template part: components/blog-archive-card.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$item = wp_parse_args(
	$args ?? array(),
	array(
		'title'          => '',
		'url'            => '',
		'excerpt'        => '',
		'image_url'      => '',
		'image_width'    => 1216,
		'image_height'   => 1632,
		'image_alt'      => '',
		'iso_date'       => '',
		'formatted_date' => '',
		'reading_time'   => '',
		'link_label'     => 'Читать',
		'mobile_hidden'  => false,
	)
);

$title = trim( (string) $item['title'] );
$url   = trim( (string) $item['url'] );

if ( '' === $title || '' === $url ) {
	return;
}

$card_class = 'blog-archive-card';

if ( ! empty( $item['mobile_hidden'] ) ) {
	$card_class .= ' blog-archive-card--mobile-hidden';
}

$has_meta = '' !== trim( (string) $item['formatted_date'] ) || '' !== trim( (string) $item['reading_time'] );
?>
<article class="<?php echo esc_attr( $card_class ); ?>" data-reveal>
	<a class="blog-archive-card__image-link" href="<?php echo esc_url( $url ); ?>">
		<img
			class="blog-archive-card__image"
			src="<?php echo esc_url( (string) $item['image_url'] ); ?>"
			width="<?php echo esc_attr( (string) $item['image_width'] ); ?>"
			height="<?php echo esc_attr( (string) $item['image_height'] ); ?>"
			alt="<?php echo esc_attr( (string) $item['image_alt'] ); ?>"
			loading="lazy"
			decoding="async"
		>
	</a>
	<div class="blog-archive-card__body">
		<h2 class="blog-archive-card__title">
			<a class="blog-archive-card__title-link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
		</h2>
		<?php if ( $has_meta ) : ?>
			<p class="blog-archive-card__meta">
				<?php if ( '' !== trim( (string) $item['formatted_date'] ) ) : ?>
					<time class="blog-archive-card__date" datetime="<?php echo esc_attr( (string) $item['iso_date'] ); ?>"><?php echo esc_html( (string) $item['formatted_date'] ); ?></time>
				<?php endif; ?>
				<?php if ( '' !== trim( (string) $item['reading_time'] ) ) : ?>
					<?php if ( '' !== trim( (string) $item['formatted_date'] ) ) : ?>
						<span class="blog-archive-card__reading-time" aria-hidden="true"> · </span>
					<?php endif; ?>
					<span class="blog-archive-card__reading-time"><?php echo esc_html( (string) $item['reading_time'] ); ?></span>
				<?php endif; ?>
			</p>
		<?php endif; ?>
		<?php if ( '' !== trim( (string) $item['excerpt'] ) ) : ?>
			<p class="blog-archive-card__excerpt"><?php echo esc_html( wp_strip_all_tags( (string) $item['excerpt'] ) ); ?></p>
		<?php endif; ?>
		<p class="blog-archive-card__read-more">
			<a class="blog-archive-card__read-more-link" href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( (string) $item['link_label'] ); ?></a>
		</p>
	</div>
</article>
