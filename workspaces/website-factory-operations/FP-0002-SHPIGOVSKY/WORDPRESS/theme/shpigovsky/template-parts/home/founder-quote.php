<?php
/**
 * Template part: home/founder-quote.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * V9-06E41: Home-level visibility toggle (content source remains external/static).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( is_front_page() && ! shpigovsky_home_list_enabled( 'home_founder_quote_visible' ) ) {
	return;
}

if ( function_exists( 'shpigovsky_is_services_hub_page' ) && shpigovsky_is_services_hub_page() && ! shpigovsky_services_hub_list_enabled( 'services_hub_founder_quote_visible' ) ) {
	return;
}

$quote = function_exists( 'shpigovsky_get_founder_quote_block_context_data' )
	? shpigovsky_get_founder_quote_block_context_data()
	: array();
$paragraphs = isset( $quote['paragraphs'] ) && is_array( $quote['paragraphs'] ) ? $quote['paragraphs'] : array();
$name       = isset( $quote['name'] ) ? trim( (string) $quote['name'] ) : 'Сергей Юрьевич Шпиговский';
$role       = isset( $quote['role'] ) ? trim( (string) $quote['role'] ) : 'Основатель центра. Аддиктолог, интервенционист';
$photo_url  = isset( $quote['photo_url'] ) ? trim( (string) $quote['photo_url'] ) : shpigovsky_asset_uri( 'img/content/founder-sergey-shpigovsky.png' );
$photo_alt  = isset( $quote['photo_alt'] ) ? trim( (string) $quote['photo_alt'] ) : $name;
$photo_w    = isset( $quote['photo_width'] ) ? (int) $quote['photo_width'] : 1281;
$photo_h    = isset( $quote['photo_height'] ) ? (int) $quote['photo_height'] : 1278;
$cta_label  = isset( $quote['cta_label'] ) ? trim( (string) $quote['cta_label'] ) : 'Записаться на консультацию';
?>
<section data-reveal class="founder-quote founder-quote--variant-b" aria-labelledby="founder-quote-label">
  <div class="container">
    <div class="founder-quote__layout">
      <blockquote class="founder-quote__quote">
        <svg class="founder-quote__mark" width="70" height="55" viewBox="0 0 70 55" aria-hidden="true" focusable="false">
          <path fill="currentColor" d="M17.1856 55.0000 C13.9721 55.0000 11.3174 54.3678 9.2216 53.1034 C7.1257 51.8391 5.3792 50.1533 3.9820 48.0460 C2.5848 45.7982 1.5369 43.2695 0.8383 40.4598 C0.2794 37.6501 0.0000 35.1213 0.0000 32.8736 C0.0000 25.9898 1.7465 19.6679 5.2395 13.9080 C8.8723 8.1481 14.3912 3.5121 21.7964 0.0000 L23.6826 3.7931 C19.4910 5.6194 15.8583 8.4291 12.7844 12.2222 C9.7106 16.0153 8.0339 19.8787 7.7545 23.8123 C7.4750 25.9195 7.6148 27.8863 8.1737 29.7126 C10.6886 27.3244 13.7625 26.1303 17.3952 26.1303 C21.4471 26.1303 24.8703 27.4649 27.6647 30.1341 C30.4591 32.6628 31.8563 36.1750 31.8563 40.6705 C31.8563 44.8851 30.3892 48.3269 27.4551 50.9962 C24.6607 53.6654 21.2375 55.0000 17.1856 55.0000 Z M55.3293 55.0000 C52.1158 55.0000 49.4611 54.3678 47.3653 53.1034 C45.2695 51.8391 43.5230 50.1533 42.1257 48.0460 C40.7285 45.7982 39.6806 43.2695 38.9820 40.4598 C38.4232 37.6501 38.1437 35.1213 38.1437 32.8736 C38.1437 25.9898 39.8902 19.6679 43.3832 13.9080 C47.0160 8.1481 52.5349 3.5121 59.9401 0.0000 L61.8263 3.7931 C57.6347 5.6194 54.0020 8.4291 50.9281 12.2222 C47.8543 16.0153 46.1776 19.8787 45.8982 23.8123 C45.6188 25.9195 45.7585 27.8863 46.3174 29.7126 C48.8323 27.3244 51.9062 26.1303 55.5389 26.1303 C59.5908 26.1303 63.0140 27.4649 65.8084 30.1341 C68.6028 32.6628 70.0000 36.1750 70.0000 40.6705 C70.0000 44.8851 68.5329 48.3269 65.5988 50.9962 C62.8044 53.6654 59.3812 55.0000 55.3293 55.0000 Z"/>
        </svg>
        <?php foreach ( $paragraphs as $paragraph ) : ?>
          <p class="founder-quote__text"><span><?php echo wp_kses_post( $paragraph ); ?></span></p>
        <?php endforeach; ?>
      </blockquote>
      <figure class="founder-quote__figure">
        <span class="visually-hidden" id="founder-quote-label">Слово основателя</span>
        <img
          class="founder-quote__photo"
          src="<?php echo esc_url( $photo_url ); ?>"
          width="<?php echo esc_attr( (string) $photo_w ); ?>"
          height="<?php echo esc_attr( (string) $photo_h ); ?>"
          alt="<?php echo esc_attr( $photo_alt ); ?>"
        >
        <figcaption class="founder-quote__author">
          <p class="founder-quote__name"><?php echo esc_html( $name ); ?></p>
          <p class="founder-quote__role"><?php echo esc_html( $role ); ?></p>
          <button
            type="button"
            class="btn founder-quote__cta"
            data-modal-open="consultation"
            data-modal-source="founder-quote"
            data-modal-title="<?php echo esc_attr( $cta_label ); ?>"
            data-modal-submit-text="<?php echo esc_attr( $cta_label ); ?>"
          ><?php echo esc_html( $cta_label ); ?></button>
        </figcaption>
      </figure>
    </div>
  </div>
</section>
