<?php
/**
 * Template part: services-hub/hero.php
 *
 * V9 services hub hero — services-inner-hero-v2 with theme asset fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$intro     = shpigovsky_get_services_hub_field( 'services_hub_intro' );
$eyebrow   = __( 'Заболевания, которые мы лечим', 'shpigovsky' );
$lead      = '' !== $intro ? $intro : __( 'Зависимость, тревога, нарушение пищевого поведения — у каждого из этих состояний есть своя биология, своя психология и своя точка, где что-то пошло не так. Нас интересует не только то, что происходит, но и почему это происходит именно с вами, именно сейчас.', 'shpigovsky' );
$title     = __( 'Лечение и профилактика', 'shpigovsky' );
$cta_label = shpigovsky_get_site_option( 'default_button_label' );
$cta_label = '' !== $cta_label ? $cta_label : __( 'Записаться на консультацию', 'shpigovsky' );
$hero_url  = shpigovsky_asset_uri( 'img/content/services/services-hero.webp' );
?>
<section data-reveal class="services-inner-hero-v2" aria-labelledby="services-inner-hero-v2-title">
	<div class="services-inner-hero-v2__shell">
		<div class="services-inner-hero-v2__media" aria-hidden="true">
			<img
				class="services-inner-hero-v2__image"
				src="<?php echo esc_url( $hero_url ); ?>"
				width="1400"
				height="628"
				alt=""
			>
			<div class="services-inner-hero-v2__overlay"></div>
		</div>

		<div class="services-inner-hero-v2__content">
			<div class="container services-inner-hero-v2__container">
				<div class="services-inner-hero-v2__copy">
					<p class="services-inner-hero-v2__eyebrow"><?php echo esc_html( $eyebrow ); ?></p>
					<div class="services-inner-hero-v2__scene">
						<div class="services-inner-hero-v2__main">
							<h1 class="services-inner-hero-v2__title" id="services-inner-hero-v2-title"><?php echo esc_html( $title ); ?></h1>
							<p class="services-inner-hero-v2__lead"><?php echo wp_kses_post( $lead ); ?></p>
						</div>
						<div class="services-inner-hero-v2__actions">
							<button
								class="btn btn_dark btn--primary services-inner-hero-v2__cta"
								type="button"
								data-modal-open="consultation"
								data-modal-source="services-hero-v2"
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
