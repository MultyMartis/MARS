<?php
/**
 * Template part: home/specialists.php
 *
 * V9-06E18: reusable block options with V9 static fallback.
 * V9-06E34: cards from `/specyalisty/` child pages; card links to specialist pages.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( is_front_page() && ! shpigovsky_home_list_enabled( 'home_specialists_visible' ) ) {
	return;
}

$section_id          = isset( $args['section_id'] ) ? (string) $args['section_id'] : '';
$heading_id          = isset( $args['heading_id'] ) ? (string) $args['heading_id'] : 'specialists-heading';
$specialists_heading = shpigovsky_get_specialists_section_heading();
$all_link_label      = shpigovsky_get_specialists_all_link_label();
$all_link_url        = shpigovsky_get_specialists_all_link_url();
$cards               = shpigovsky_get_specialists_cards();

?>
<section data-reveal class="specialists"<?php echo '' !== $section_id ? ' id="' . esc_attr( $section_id ) . '"' : ''; ?> aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
  <div class="container">
    <div class="specialists__head">
      <h2 class="specialists__heading" id="<?php echo esc_attr( $heading_id ); ?>"><?php echo esc_html( $specialists_heading ); ?></h2>
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
    </div>
  </div>
</section>
