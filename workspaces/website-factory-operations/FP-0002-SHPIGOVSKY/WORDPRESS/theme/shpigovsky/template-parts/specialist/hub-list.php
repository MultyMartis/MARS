<?php
/**
 * Template part: specialist/hub-list.php
 *
 * Static Specialists Hub listing. Reuses production specialist card classes and
 * the existing home-feature-grid responsive grid primitive (no new visual CSS).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! function_exists( 'shpigovsky_get_specialists_cards' ) ) {
	return;
}

$cards = shpigovsky_get_specialists_cards();
if ( empty( $cards ) ) {
	return;
}

?>
<div class="specialists specialists--hub-list" data-specialists-hub-list>
	<div class="home-feature-grid__card-grid" role="list">
		<?php foreach ( $cards as $card ) : ?>
		<article class="specialists__card" role="listitem">
			<?php if ( ! empty( $card['link'] ) ) : ?>
			<a class="specialists__card-link" href="<?php echo esc_url( $card['link'] ); ?>">
			<?php endif; ?>
				<img class="specialists__photo" src="<?php echo esc_url( $card['image'] ); ?>" width="<?php echo (int) $card['width']; ?>" height="<?php echo (int) $card['height']; ?>" alt="<?php echo esc_attr( $card['name'] ); ?>" loading="lazy" decoding="async">
				<h2 class="specialists__name"><?php echo esc_html( $card['name'] ); ?></h2>
				<p class="specialists__role"><?php echo wp_kses_post( $card['role'] ); ?></p>
			<?php if ( ! empty( $card['link'] ) ) : ?>
			</a>
			<?php endif; ?>
		</article>
		<?php endforeach; ?>
	</div>
</div>
