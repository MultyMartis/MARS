<?php
/**
 * Template part: services-hub/hero.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$intro     = shpigovsky_get_services_hub_field( 'services_hub_intro' );
$eyebrow   = __( 'Заболевания, которые мы лечим', 'shpigovsky' );
$tagline   = '' !== $intro ? $intro : __( 'Зависимость, тревога, нарушение пищевого поведения — у каждого из этих состояний есть своя биология, своя психология и своя точка, где что-то пошло не так.', 'shpigovsky' );
$title     = __( 'Лечение и профилактика', 'shpigovsky' );
$cta_label = shpigovsky_get_site_option( 'default_button_label' );
$cta_label = '' !== $cta_label ? $cta_label : __( 'Записаться на консультацию', 'shpigovsky' );
?>
<section data-reveal class="hero hero--inner">
	<div class="hero__content">
		<div class="hero__container">
			<div class="hero__panel">
				<div class="hero__content-inner">
					<p class="hero__eyebrow"><?php echo esc_html( $eyebrow ); ?></p>
					<p class="hero__tagline"><?php echo wp_kses_post( $tagline ); ?></p>
					<h1 class="hero__title"><?php echo esc_html( $title ); ?></h1>
				</div>
			</div>
			<div class="hero__actions">
				<button
					class="btn btn_dark btn--primary hero__button"
					type="button"
					data-modal-open="consultation"
					data-modal-source="services-hero"
					data-modal-title="<?php echo esc_attr( $cta_label ); ?>"
					data-modal-submit-text="<?php echo esc_attr( $cta_label ); ?>"
				>
					<?php echo esc_html( $cta_label ); ?>
				</button>
			</div>
		</div>
	</div>
</section>
