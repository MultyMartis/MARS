<?php
/**
 * Direct V9 port: specialists section (usluga-konechnaya-v1.html).
 *
 * Exact static V9 markup from partials/sections/specialists.html — not home/specialists.php.
 * Swiper vendor required: inc/alcohol-direct-v9-vendors.php.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$cards = shpigovsky_get_v9_specialists_cards();

?>
<section data-reveal class="specialists" id="service-leaf-specialists" aria-labelledby="service-leaf-specialists-heading">
  <div class="container">
    <div class="specialists__head">
      <h2 class="specialists__heading" id="service-leaf-specialists-heading">Специалисты центра</h2>
      <a class="specialists__all-link" href="<?php echo esc_url( home_url( '/o-centre/' ) ); ?>">
        <span class="specialists__all-text">все специалисты</span>
        <span class="specialists__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <div class="specialists__slider swiper" data-specialists-slider>
      <div class="specialists__wrapper swiper-wrapper">
        <?php foreach ( $cards as $card ) : ?>
        <article class="specialists__card swiper-slide">
          <img class="specialists__photo" src="<?php echo esc_url( shpigovsky_asset_uri( $card['image'] ) ); ?>" width="<?php echo (int) $card['width']; ?>" height="<?php echo (int) $card['height']; ?>" alt="<?php echo esc_attr( $card['name'] ); ?>" loading="lazy" decoding="async">
          <h3 class="specialists__name"><?php echo esc_html( $card['name'] ); ?></h3>
          <p class="specialists__role"><?php echo wp_kses_post( $card['role'] ); ?></p>
        </article>
        <?php endforeach; ?>
      </div>
      <div class="specialists__pagination swiper-pagination" data-specialists-pagination></div>
    </div>
  </div>
</section>
