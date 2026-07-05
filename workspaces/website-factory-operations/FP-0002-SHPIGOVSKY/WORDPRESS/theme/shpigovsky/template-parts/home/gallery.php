<?php
/**
 * Template part: home/gallery.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * Future ACF wiring: D9-E wave.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

?>
<section data-reveal class="home-gallery" aria-label="Фотогалерея центра">
  <div class="container">
    <div class="home-gallery__slider swiper" data-gallery-slider>
      <div class="home-gallery__wrapper swiper-wrapper">
        <figure class="home-gallery__slide swiper-slide">
          <img
            class="home-gallery__image"
            src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/gallery/shpigovsky-gallery-01.webp' ) ); ?>"
            width="621"
            height="938"
            alt=""
            decoding="async"
          >
          <figcaption class="home-gallery__caption">Лечение зависимости от&nbsp;алкоголя</figcaption>
        </figure>
        <figure class="home-gallery__slide swiper-slide">
          <img
            class="home-gallery__image"
            src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/gallery/shpigovsky-gallery-02.webp' ) ); ?>"
            width="1113"
            height="738"
            alt=""
            loading="lazy"
            decoding="async"
          >
          <figcaption class="home-gallery__caption">Лудомания лечение зависимости</figcaption>
        </figure>
        <figure class="home-gallery__slide swiper-slide">
          <img
            class="home-gallery__image"
            src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/gallery/shpigovsky-gallery-03.webp' ) ); ?>"
            width="1171"
            height="864"
            alt=""
            loading="lazy"
            decoding="async"
          >
          <figcaption class="home-gallery__caption">Лечение подростковой зависимости</figcaption>
        </figure>
        <figure class="home-gallery__slide swiper-slide">
          <img
            class="home-gallery__image"
            src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/gallery/shpigovsky-gallery-04.webp' ) ); ?>"
            width="1296"
            height="921"
            alt=""
            loading="lazy"
            decoding="async"
          >
          <figcaption class="home-gallery__caption">Зависимость от&nbsp;постоянных покупок</figcaption>
        </figure>
      </div>
      <div class="home-gallery__pagination swiper-pagination" data-gallery-pagination></div>
    </div>
  </div>
</section>
