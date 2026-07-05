<?php
/**
 * Template part: home/hero.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$slides       = shpigovsky_get_home_repeater( 'home_hero_slides' );
$slide        = ! empty( $slides[0] ) && is_array( $slides[0] ) ? $slides[0] : array();
$hero_title   = isset( $slide['title'] ) ? trim( (string) $slide['title'] ) : '';
$hero_text    = isset( $slide['text'] ) ? trim( (string) $slide['text'] ) : '';
$hero_image   = isset( $slide['image'] ) ? $slide['image'] : null;
$hero_img_url = shpigovsky_acf_image_url( $hero_image );
$hero_img_alt = shpigovsky_acf_image_alt( $hero_image );
$hero_img_w   = 2230;
$hero_img_h   = 1246;

if ( '' === $hero_img_url ) {
	$hero_fallback = shpigovsky_get_home_hero_image_fallback();

	if ( ! empty( $hero_fallback['url'] ) ) {
		$hero_img_url = (string) $hero_fallback['url'];
		$hero_img_alt = (string) $hero_fallback['alt'];
		$hero_img_w   = ! empty( $hero_fallback['width'] ) ? (int) $hero_fallback['width'] : 2230;
		$hero_img_h   = ! empty( $hero_fallback['height'] ) ? (int) $hero_fallback['height'] : 1246;
	}
}

if ( '' === $hero_title ) {
	$hero_title = get_bloginfo( 'name', 'display' );
}

if ( '' === $hero_text ) {
	$hero_text = 'Центр профилактики и&nbsp;лечения зависимостей';
}

$cta_label = shpigovsky_get_site_option( 'default_button_label' );
$cta_label = '' !== $cta_label ? $cta_label : __( 'Записаться на консультацию', 'shpigovsky' );
?>
<section class="hero hero--home">
	<?php if ( '' !== $hero_img_url ) : ?>
		<div class="hero__media" aria-hidden="true">
			<img
				class="hero__image"
				src="<?php echo esc_url( $hero_img_url ); ?>"
				width="<?php echo esc_attr( (string) $hero_img_w ); ?>"
				height="<?php echo esc_attr( (string) $hero_img_h ); ?>"
				alt="<?php echo esc_attr( $hero_img_alt ); ?>"
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
