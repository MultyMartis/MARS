<?php
/**
 * Direct V9 port: specialists section (usluga-konechnaya-v1.html).
 *
 * V9-06E18: shared specialists block data source with home/subdivision renderers.
 * V9-06E34: cards from `/specyalisty/` child pages; card links to specialist pages.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$cards          = shpigovsky_get_specialists_cards();
$heading        = shpigovsky_get_specialists_section_heading();
$all_link_label = shpigovsky_get_specialists_all_link_label();
$all_link_url   = shpigovsky_get_specialists_all_link_url();

?>
<section data-reveal class="specialists" id="service-leaf-specialists" aria-labelledby="service-leaf-specialists-heading">
  <div class="container">
    <div class="specialists__head">
      <h2 class="specialists__heading" id="service-leaf-specialists-heading"><?php echo esc_html( $heading ); ?></h2>
      <a class="specialists__all-link" href="<?php echo esc_url( $all_link_url ); ?>">
        <span class="specialists__all-text"><?php echo esc_html( $all_link_label ); ?></span>
        <span class="specialists__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <div class="specialists__slider swiper" data-specialists-slider>
      <div class="specialists__wrapper swiper-wrapper">
        <?php foreach ( $cards as $card ) : ?>
        <article class="specialists__card swiper-slide">
          <?php if ( ! empty( $card['link'] ) ) : ?>
          <a class="specialists__card-link" href="<?php echo esc_url( $card['link'] ); ?>">
          <?php endif; ?>
            <img class="specialists__photo" src="<?php echo esc_url( $card['image'] ); ?>" width="<?php echo (int) $card['width']; ?>" height="<?php echo (int) $card['height']; ?>" alt="<?php echo esc_attr( $card['name'] ); ?>" loading="lazy" decoding="async">
            <h3 class="specialists__name"><?php echo esc_html( $card['name'] ); ?></h3>
            <p class="specialists__role"><?php echo wp_kses_post( $card['role'] ); ?></p>
          <?php if ( ! empty( $card['link'] ) ) : ?>
          </a>
          <?php endif; ?>
        </article>
        <?php endforeach; ?>
      </div>
      <div class="specialists__pagination swiper-pagination" data-specialists-pagination></div>
      <?php get_template_part( 'template-parts/components/fp02-slider-mobile-nav' ); ?>
    </div>
  </div>
</section>
