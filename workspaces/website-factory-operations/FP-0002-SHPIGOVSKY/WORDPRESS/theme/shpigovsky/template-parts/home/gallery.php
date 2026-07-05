<?php
/**
 * Template part: home/gallery.php
 *
 * D9-H: ACF wiring with static V9 fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$fallback_slides = shpigovsky_home_gallery_fallback_items();
$acf_rows        = shpigovsky_get_home_repeater( 'home_gallery_media' );
$slide_count     = ! empty( $acf_rows ) ? count( $acf_rows ) : count( $fallback_slides );

?>
<section data-reveal class="home-gallery" aria-label="Фотогалерея центра">
  <div class="container">
    <div class="home-gallery__slider swiper" data-gallery-slider>
      <div class="home-gallery__wrapper swiper-wrapper">
        <?php for ( $index = 0; $index < $slide_count; $index++ ) : ?>
          <?php
			$acf_row       = ! empty( $acf_rows[ $index ] ) && is_array( $acf_rows[ $index ] ) ? $acf_rows[ $index ] : array();
			$fallback_row  = isset( $fallback_slides[ $index ] ) ? $fallback_slides[ $index ] : end( $fallback_slides );
			$caption       = isset( $acf_row['title'] ) && '' !== trim( (string) $acf_row['title'] )
				? trim( (string) $acf_row['title'] )
				: (string) $fallback_row['title'];
			$image         = shpigovsky_home_gallery_slide_image( $acf_row, $fallback_row );
			$is_lazy       = ! empty( $fallback_row['lazy'] );
			?>
        <figure class="home-gallery__slide swiper-slide">
          <?php if ( '' !== $image['url'] ) : ?>
          <img
            class="home-gallery__image"
            src="<?php echo esc_url( $image['url'] ); ?>"
            width="<?php echo esc_attr( (string) $image['width'] ); ?>"
            height="<?php echo esc_attr( (string) $image['height'] ); ?>"
            alt=""
            <?php echo $is_lazy ? 'loading="lazy"' : ''; ?>
            decoding="async"
          >
          <?php endif; ?>
          <figcaption class="home-gallery__caption"><?php echo wp_kses_post( $caption ); ?></figcaption>
        </figure>
        <?php endfor; ?>
      </div>
      <div class="home-gallery__pagination swiper-pagination" data-gallery-pagination></div>
    </div>
  </div>
</section>
