<?php
/**
 * Template part: home/gallery.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$media_rows = shpigovsky_get_home_repeater( 'home_gallery_media' );

$slides = array();

foreach ( $media_rows as $row ) {
	$caption = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
	$text    = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
	$image   = isset( $row['media'] ) ? $row['media'] : null;
	$url     = shpigovsky_acf_image_url( $image );
	$alt     = shpigovsky_acf_image_alt( $image );

	if ( '' === $url ) {
		continue;
	}

	if ( '' === $caption && '' !== $text ) {
		$caption = $text;
	}

	$slides[] = array(
		'url'     => $url,
		'alt'     => $alt,
		'caption' => $caption,
	);
}

if ( empty( $slides ) ) {
	return;
}
?>
<section data-reveal class="home-gallery" aria-label="<?php echo esc_attr__( 'Фотогалерея центра', 'shpigovsky' ); ?>">
	<div class="container">
		<div class="home-gallery__slider swiper" data-gallery-slider>
			<div class="home-gallery__wrapper swiper-wrapper">
				<?php foreach ( $slides as $index => $slide ) : ?>
					<figure class="home-gallery__slide swiper-slide">
						<img
							class="home-gallery__image"
							src="<?php echo esc_url( $slide['url'] ); ?>"
							alt="<?php echo esc_attr( $slide['alt'] ); ?>"
							<?php echo 0 === $index ? 'decoding="async"' : 'loading="lazy" decoding="async"'; ?>
						>
						<?php if ( '' !== $slide['caption'] ) : ?>
							<figcaption class="home-gallery__caption"><?php echo esc_html( $slide['caption'] ); ?></figcaption>
						<?php endif; ?>
					</figure>
				<?php endforeach; ?>
			</div>
			<div class="home-gallery__pagination swiper-pagination" data-gallery-pagination></div>
		</div>
	</div>
</section>
