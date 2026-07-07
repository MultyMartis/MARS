<?php
/**
 * Template part: home/hero.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$slides     = shpigovsky_get_home_repeater( 'home_hero_slides' );
$slide      = ! empty( $slides[0] ) && is_array( $slides[0] ) ? $slides[0] : array();
$hero_title = isset( $slide['title'] ) ? trim( (string) $slide['title'] ) : '';
$hero_text  = isset( $slide['text'] ) ? trim( (string) $slide['text'] ) : '';
$hero_image = shpigovsky_get_home_hero_image();

if ( '' === $hero_title ) {
	$hero_title = 'Шпиговский дом';
}

if ( '' === $hero_text ) {
	$hero_text = 'Центр профилактики и&nbsp;лечения зависимостей';
}

$cta_label = shpigovsky_get_local_hero_cta_label( shpigovsky_get_front_page_id() );
?>
<section class="hero hero--home">
	<?php if ( '' !== $hero_image['url'] ) : ?>
		<div class="hero__media" aria-hidden="true">
			<img
				class="hero__image"
				src="<?php echo esc_url( $hero_image['url'] ); ?>"
				width="<?php echo esc_attr( (string) $hero_image['width'] ); ?>"
				height="<?php echo esc_attr( (string) $hero_image['height'] ); ?>"
				alt="<?php echo esc_attr( $hero_image['alt'] ); ?>"
			>
		</div>
	<?php endif; ?>

	<div class="hero__content">
		<div class="hero__container">
			<div class="hero__panel">
				<div class="hero__content-inner">
					<p class="hero__tagline"><?php echo wp_kses_post( $hero_text ); ?></p>
					<h1 class="hero__title"><?php echo esc_html( $hero_title ); ?></h1>
				</div>
			</div>
			<div class="hero__actions">
				<button
					class="btn btn_dark btn--primary hero__button"
					type="button"
					data-modal-open="consultation"
					data-modal-source="hero"
					data-modal-title="<?php echo esc_attr( $cta_label ); ?>"
					data-modal-submit-text="<?php echo esc_attr( $cta_label ); ?>"
				>
					<?php echo esc_html( $cta_label ); ?>
				</button>
			</div>
		</div>
	</div>
</section>
