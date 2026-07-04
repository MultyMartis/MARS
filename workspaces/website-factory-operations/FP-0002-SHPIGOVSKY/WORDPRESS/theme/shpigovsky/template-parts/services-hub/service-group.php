<?php
/**
 * Template part: services-hub/service-group.php
 *
 * Expects query var services_hub_group (array).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$group = get_query_var( 'services_hub_group', array() );

if ( ! is_array( $group ) || empty( $group['children'] ) ) {
	return;
}

$title          = isset( $group['title'] ) ? trim( (string) $group['title'] ) : '';
$lead_primary   = isset( $group['lead_primary'] ) ? trim( (string) $group['lead_primary'] ) : '';
$lead_secondary = isset( $group['lead_secondary'] ) ? trim( (string) $group['lead_secondary'] ) : '';
$modifier_class = isset( $group['modifier_class'] ) ? trim( (string) $group['modifier_class'] ) : '';
$section_id     = isset( $group['section_id'] ) ? trim( (string) $group['section_id'] ) : 'services-category-heading';
$cta_source     = isset( $group['cta_source'] ) ? trim( (string) $group['cta_source'] ) : 'services-hub';
$children       = $group['children'];
$gallery        = isset( $group['gallery'] ) && is_array( $group['gallery'] ) ? $group['gallery'] : array();

if ( '' === $title ) {
	return;
}

$cta_label = shpigovsky_get_site_option( 'default_button_label' );
$cta_label = '' !== $cta_label ? $cta_label : __( 'Записаться на консультацию', 'shpigovsky' );
?>
<section data-reveal class="services-category-hub <?php echo esc_attr( $modifier_class ); ?>" aria-labelledby="<?php echo esc_attr( $section_id ); ?>">
	<div class="container services-category-hub__container">
		<div class="services-category-hub__head">
			<h2 class="services-category-hub__heading" id="<?php echo esc_attr( $section_id ); ?>"><?php echo esc_html( $title ); ?></h2>
		</div>

		<?php if ( '' !== $lead_primary ) : ?>
			<p class="services-category-hub__lead"><?php echo wp_kses_post( $lead_primary ); ?></p>
		<?php endif; ?>

		<?php if ( '' !== $lead_secondary ) : ?>
			<p class="services-category-hub__lead services-category-hub__lead--secondary"><?php echo wp_kses_post( $lead_secondary ); ?></p>
		<?php endif; ?>

		<div class="services-category-hub__services">
			<?php
			foreach ( $children as $child ) {
				if ( ! is_array( $child ) ) {
					continue;
				}

				set_query_var( 'service_card_title', isset( $child['title'] ) ? $child['title'] : '' );
				set_query_var( 'service_card_url', isset( $child['url'] ) ? $child['url'] : '' );
				set_query_var( 'service_card_text', isset( $child['text'] ) ? $child['text'] : '' );
				get_template_part( 'template-parts/components/service-card' );
			}
			?>
		</div>

		<?php if ( ! empty( $gallery ) ) : ?>
			<div class="services-category-hub__gallery">
				<?php foreach ( $gallery as $image ) : ?>
					<?php
					if ( ! is_array( $image ) || empty( $image['url'] ) ) {
						continue;
					}
					?>
					<figure class="services-category-hub__gallery-item">
						<img
							class="services-category-hub__gallery-image"
							src="<?php echo esc_url( $image['url'] ); ?>"
							width="<?php echo isset( $image['width'] ) ? (int) $image['width'] : ''; ?>"
							height="<?php echo isset( $image['height'] ) ? (int) $image['height'] : ''; ?>"
							alt="<?php echo esc_attr( isset( $image['alt'] ) ? (string) $image['alt'] : '' ); ?>"
							loading="lazy"
						>
					</figure>
				<?php endforeach; ?>
			</div>
		<?php endif; ?>

		<div class="services-category-hub__actions">
			<button
				type="button"
				class="btn btn_dark btn--primary services-category-hub__cta"
				data-modal-open="consultation"
				data-modal-source="<?php echo esc_attr( $cta_source ); ?>"
				data-modal-title="<?php echo esc_attr( $cta_label ); ?>"
				data-modal-submit-text="<?php echo esc_attr( $cta_label ); ?>"
			>
				<?php echo esc_html( $cta_label ); ?>
			</button>
		</div>
	</div>
</section>
