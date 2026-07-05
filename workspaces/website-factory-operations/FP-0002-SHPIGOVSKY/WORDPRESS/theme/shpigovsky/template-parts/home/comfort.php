<?php
/**
 * Template part: home/comfort.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * Future ACF wiring: D9-E wave.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$comfort_heading = shpigovsky_home_text_or_fallback( 'home_comfort_heading', 'Комфорт, приватность, забота' );
$comfort_lead    = shpigovsky_home_text_or_fallback(
	'home_comfort_lead',
	'Разговор&nbsp;— это уже первый шаг. Мы расскажем, что можем предложить именно вам или вашему близкому&nbsp;— без давления и&nbsp;без шаблонных ответов.'
);

?>
<section data-reveal class="comfort"  aria-labelledby="comfort-heading">
  <div class="container">
    <div class="comfort__head">
      <h2 class="comfort__heading" id="comfort-heading"><?php echo esc_html( $comfort_heading ); ?></h2>
      <a class="comfort__all-link" href="<?php echo esc_url( home_url( '/o-centre/galereya-o-dome/' ) ); ?>">
        <span class="comfort__all-text">подробнее о&nbsp;доме</span>
        <span class="comfort__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <p class="comfort__lead"><?php echo wp_kses_post( $comfort_lead ); ?></p>

    
      <div class="comfort__gallery">
      <div class="comfort__gallery-item comfort__gallery-item_decor">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/branding/logo.svg' ) ); ?>" width="auto" height="auto" alt="" loading="lazy" decoding="async">
      </div>
      <a class="comfort__gallery-item comfort__gallery-item--wide" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-01.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-01.webp' ) ); ?>" width="1957" height="1113" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-02.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-02.webp' ) ); ?>" width="1881" height="1246" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-03.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-03.webp' ) ); ?>" width="1623" height="1155" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-04.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-04.webp' ) ); ?>" width="1610" height="1146" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-05.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-05.webp' ) ); ?>" width="1276" height="1136" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item comfort__gallery-item--wide" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-06.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-06.webp' ) ); ?>" width="2201" height="1227" alt="" loading="lazy" decoding="async">
      </a>
    </div>
  </div>
</section>
