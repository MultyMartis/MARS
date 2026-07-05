<?php
/**
 * Template part: home/staff-photo.php
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
<section data-reveal class="home-staff-photo @@class" aria-label="Команда центра">
  <div class="container">
    <div class="home-staff-photo__bleed">
      <img
        class="home-staff-photo__image"
        src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/pre-reviews/shpigovsky-staff-group.webp' ) ); ?>"
        width="1139"
        height="443"
        alt="Команда специалистов реабилитационного центра"
        loading="lazy"
        decoding="async"
      >
    </div>
  </div>
</section>
