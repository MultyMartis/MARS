<?php
/**
 * Template part: home/specialists.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * Future ACF wiring: D9-E wave.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$section_id = isset( $args['section_id'] ) ? (string) $args['section_id'] : '';
$heading_id = isset( $args['heading_id'] ) ? (string) $args['heading_id'] : 'specialists-heading';
$specialists_heading = shpigovsky_home_text_or_fallback( 'home_specialists_heading', 'Специалисты центра' );

?>
<section data-reveal class="specialists"<?php echo '' !== $section_id ? ' id="' . esc_attr( $section_id ) . '"' : ''; ?> aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
  <div class="container">
    <div class="specialists__head">
      <h2 class="specialists__heading" id="<?php echo esc_attr( $heading_id ); ?>"><?php echo esc_html( $specialists_heading ); ?></h2>
      <a class="specialists__all-link" href="<?php echo esc_url( home_url( '/o-centre/' ) ); ?>">
        <span class="specialists__all-text">все специалисты</span>
        <span class="specialists__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <div class="specialists__slider swiper" data-specialists-slider>
      <div class="specialists__wrapper swiper-wrapper">
        <article class="specialists__card swiper-slide">
          <img class="specialists__photo" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-specialists/sergey-shpigovsky.webp' ) ); ?>" width="615" height="605" alt="Сергей Юрьевич Шпиговский" loading="lazy" decoding="async">
          <h3 class="specialists__name">Сергей Юрьевич Шпиговский</h3>
          <p class="specialists__role">Аддиктолог, интервенционист</p>
        </article>
        <article class="specialists__card swiper-slide">
          <img class="specialists__photo" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-specialists/maxim-kazakov.webp' ) ); ?>" width="657" height="605" alt="Максим Михайлович Казаков" loading="lazy" decoding="async">
          <h3 class="specialists__name">Максим Михайлович Казаков</h3>
          <p class="specialists__role">Психолог, преподаватель психологии, гештальт-терапевт</p>
        </article>
        <article class="specialists__card swiper-slide">
          <img class="specialists__photo" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-specialists/darya-kostyuk.webp' ) ); ?>" width="643" height="610" alt="Дарья Владимировна Костюк" loading="lazy" decoding="async">
          <h3 class="specialists__name">Дарья Владимировна Костюк</h3>
          <p class="specialists__role">Психолог, EMDR терапевт, телесно-ориентированный терапевт</p>
        </article>
        <article class="specialists__card swiper-slide">
          <img class="specialists__photo" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-specialists/sergey-shpigovsky.webp' ) ); ?>" width="615" height="605" alt="Сергей Юрьевич Шпиговский" loading="lazy" decoding="async">
          <h3 class="specialists__name">Сергей Юрьевич Шпиговский</h3>
          <p class="specialists__role">Аддиктолог, интервенционист</p>
        </article>
        <article class="specialists__card swiper-slide">
          <img class="specialists__photo" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-specialists/tatyana-shapiguzova.webp' ) ); ?>" width="643" height="610" alt="Шапигузова Татьяна Андреевна" loading="lazy" decoding="async">
          <h3 class="specialists__name">Шапигузова Татьяна Андреевна</h3>
          <p class="specialists__role">Сертифицированный гонг-мастер, звукотерапевт и&nbsp;преподаватель Кундалини йоги.</p>
        </article>
      </div>
      <div class="specialists__pagination swiper-pagination" data-specialists-pagination></div>
    </div>
  </div>
</section>
