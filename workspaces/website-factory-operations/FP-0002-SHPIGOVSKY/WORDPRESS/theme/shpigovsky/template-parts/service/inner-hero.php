<?php
/**
 * Template part: service/inner-hero.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id    = shpigovsky_get_current_service_id();
$variant    = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$title_id   = 'subdivision' === $variant ? 'service-subdivision-hero-title' : 'service-leaf-hero-title';
$hero_title = shpigovsky_get_service_hero_title( $post_id );
$hero_lead  = shpigovsky_get_service_field( $post_id, 'hero_lead' );
$eyebrow    = shpigovsky_get_service_field( $post_id, 'hero_eyebrow' );
$cta_label  = shpigovsky_get_service_field( $post_id, 'hero_cta_label' );
$image      = shpigovsky_get_service_hero_image( $post_id );
$img_url    = shpigovsky_acf_image_url( $image );
$img_alt    = shpigovsky_acf_image_alt( $image );

if ( '' === $img_url ) {
	$fallback = shpigovsky_get_service_default_hero_image( $variant );
	$img_url  = isset( $fallback['url'] ) ? $fallback['url'] : '';
	$img_alt  = isset( $fallback['alt'] ) ? $fallback['alt'] : '';
	$img_w    = isset( $fallback['width'] ) ? (int) $fallback['width'] : 1134;
	$img_h    = isset( $fallback['height'] ) ? (int) $fallback['height'] : 613;
} else {
	$img_w = 1134;
	$img_h = 613;
}

if ( '' === $eyebrow ) {
	$eyebrow = __( 'Заболевания, которые мы лечим', 'shpigovsky' );
}

if ( '' === $hero_title ) {
	$hero_title = get_the_title( $post_id );
}

if ( '' === $cta_label ) {
	$default = shpigovsky_get_site_option( 'default_button_label' );
	$cta_label = '' !== $default ? $default : __( 'Записаться на консультацию', 'shpigovsky' );
}

$cta_source = 'subdivision' === $variant ? 'service-subdivision-hero-v1' : 'service-leaf-hero-v1';
?>
<section data-reveal class="services-inner-hero-v2" aria-labelledby="<?php echo esc_attr( $title_id ); ?>">
	<div class="services-inner-hero-v2__shell">
		<?php if ( '' !== $img_url ) : ?>
			<div class="services-inner-hero-v2__media" aria-hidden="true">
				<img
					class="services-inner-hero-v2__image"
					src="<?php echo esc_url( $img_url ); ?>"
					width="<?php echo (int) $img_w; ?>"
					height="<?php echo (int) $img_h; ?>"
					alt="<?php echo esc_attr( $img_alt ); ?>"
				>
				<div class="services-inner-hero-v2__overlay"></div>
			</div>
		<?php endif; ?>

		<div class="services-inner-hero-v2__content">
			<div class="container services-inner-hero-v2__container">
				<div class="services-inner-hero-v2__copy">
					<p class="services-inner-hero-v2__eyebrow"><?php echo wp_kses_post( $eyebrow ); ?></p>
					<div class="services-inner-hero-v2__scene">
						<div class="services-inner-hero-v2__main">
							<h1 class="services-inner-hero-v2__title" id="<?php echo esc_attr( $title_id ); ?>"><?php echo esc_html( $hero_title ); ?></h1>
							<?php if ( '' !== $hero_lead ) : ?>
								<p class="services-inner-hero-v2__lead"><?php echo wp_kses_post( $hero_lead ); ?></p>
							<?php endif; ?>
						</div>
						<div class="services-inner-hero-v2__actions">
							<button
								class="btn btn_dark btn--primary services-inner-hero-v2__cta"
								type="button"
								data-modal-open="consultation"
								data-modal-source="<?php echo esc_attr( $cta_source ); ?>"
								data-modal-title="<?php echo esc_attr( $cta_label ); ?>"
								data-modal-submit-text="<?php echo esc_attr( $cta_label ); ?>"
							>
								<?php echo esc_html( $cta_label ); ?>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
