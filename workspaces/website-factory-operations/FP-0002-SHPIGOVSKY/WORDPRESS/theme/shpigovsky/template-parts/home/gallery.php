<?php
/**
 * Template part: home/gallery.php
 *
 * V9-06E32: Home gallery slides are clickable service cards from the service CPT
 * (depth-1 eligible services with service_show_on_home_gallery).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_home_list_enabled( 'home_gallery_visible' ) ) {
	return;
}

$slides = shpigovsky_get_home_gallery_service_slides();

if ( empty( $slides ) ) {
	return;
}

?>
<section data-reveal class="home-gallery" aria-label="Услуги центра">
  <div class="container">
    <div class="home-gallery__slider swiper" data-gallery-slider>
      <div class="home-gallery__wrapper swiper-wrapper">
        <?php foreach ( $slides as $index => $slide ) : ?>
          <?php
			$title        = isset( $slide['title'] ) ? (string) $slide['title'] : '';
			$url          = isset( $slide['url'] ) ? (string) $slide['url'] : '';
			$image_url    = isset( $slide['image_url'] ) ? (string) $slide['image_url'] : '';
			$width        = isset( $slide['width'] ) ? (int) $slide['width'] : 800;
			$height       = isset( $slide['height'] ) ? (int) $slide['height'] : 600;
			$alt          = isset( $slide['alt'] ) && '' !== trim( (string) $slide['alt'] ) ? (string) $slide['alt'] : $title;
			$is_lazy      = $index > 0;
			?>
        <figure class="home-gallery__slide swiper-slide">
          <a class="home-gallery__link" href="<?php echo esc_url( $url ); ?>">
            <?php if ( '' !== $image_url ) : ?>
            <img
              class="home-gallery__image"
              src="<?php echo esc_url( $image_url ); ?>"
              width="<?php echo esc_attr( (string) $width ); ?>"
              height="<?php echo esc_attr( (string) $height ); ?>"
              alt="<?php echo esc_attr( $alt ); ?>"
              <?php echo $is_lazy ? 'loading="lazy"' : ''; ?>
              decoding="async"
            >
            <?php endif; ?>
            <figcaption class="home-gallery__caption"><?php echo esc_html( $title ); ?></figcaption>
          </a>
        </figure>
        <?php endforeach; ?>
      </div>
      <div class="home-gallery__pagination swiper-pagination" data-gallery-pagination></div>
      <?php get_template_part( 'template-parts/components/fp02-slider-mobile-nav' ); ?>
    </div>
  </div>
</section>
