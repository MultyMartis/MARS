<?php
/**
 * Template part: home/clinic-landscape.php
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
<section data-reveal class="clinic-landscape @@class" aria-label="Территория клиники">
  <div class="container">
    <div class="clinic-landscape__bleed">
      <img
        class="clinic-landscape__image"
        src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/pre-reviews/shpigovsky-clinic-landscape.webp' ) ); ?>"
        width="1139"
        height="584"
        alt="Здание и территория реабилитационного центра"
        loading="lazy"
        decoding="async"
      >
    </div>
  </div>
</section>
