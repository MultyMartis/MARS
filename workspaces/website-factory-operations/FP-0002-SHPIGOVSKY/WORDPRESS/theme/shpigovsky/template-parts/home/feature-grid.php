<?php
/**
 * Template part: home/feature-grid.php
 *
 * D9-H: ACF wiring with static V9 fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$advantage_items = shpigovsky_home_repeater_or_fallback(
	'home_advantages',
	shpigovsky_home_advantages_fallback_items()
);

?>
<section data-reveal class="home-feature-grid @@class" aria-label="Преимущества центра">
  <div class="container">
    <ul class="home-feature-grid__card-grid">
      <?php foreach ( $advantage_items as $item ) : ?>
        <?php
		$title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
		$text  = isset( $item['text'] ) ? trim( (string) $item['text'] ) : '';

		if ( '' === $title && '' === $text ) {
			continue;
		}
		?>
      <li class="home-feature-grid__card">
        <h3 class="home-feature-grid__card-title"><?php echo wp_kses_post( $title ); ?></h3>
        <p class="home-feature-grid__card-text"><?php echo wp_kses_post( $text ); ?></p>
      </li>
      <?php endforeach; ?>
    </ul>
  </div>
</section>
