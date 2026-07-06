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
$intro          = isset( $group['intro'] ) ? trim( (string) $group['intro'] ) : '';
$lead           = isset( $group['lead'] ) ? trim( (string) $group['lead'] ) : '';
$modifier_class = isset( $group['modifier_class'] ) ? trim( (string) $group['modifier_class'] ) : '';
$block_id       = isset( $group['block_id'] ) ? trim( (string) $group['block_id'] ) : '';
$section_id     = isset( $group['section_id'] ) ? trim( (string) $group['section_id'] ) : 'services-category-heading';
$icon           = isset( $group['icon'] ) ? trim( (string) $group['icon'] ) : '01';
$cta_source     = isset( $group['cta_source'] ) ? trim( (string) $group['cta_source'] ) : 'services-hub';
$children       = $group['children'];
$gallery        = isset( $group['gallery'] ) && is_array( $group['gallery'] ) ? $group['gallery'] : array();

if ( '' === $title ) {
	return;
}

if ( '' === $block_id ) {
	$block_id = str_replace( '-heading', '', $section_id );
}

$cta_label = isset( $group['cta_label'] ) ? trim( (string) $group['cta_label'] ) : '';
if ( '' === $cta_label ) {
	$cta_label = __( 'Записаться на консультацию', 'shpigovsky' );
}
?>
<section data-reveal class="services-category-section-v2 <?php echo esc_attr( $modifier_class ); ?>" id="<?php echo esc_attr( $block_id ); ?>" aria-labelledby="<?php echo esc_attr( $section_id ); ?>">
	<div class="container services-category-section-v2__container">
		<header class="services-category-section-v2__head">
			<div class="services-category-section-v2__head-main">
				<span class="services-category-section-v2__marker" aria-hidden="true"><?php echo esc_html( $icon ); ?></span>
				<div class="services-category-section-v2__head-copy">
					<h2 class="services-category-section-v2__heading" id="<?php echo esc_attr( $section_id ); ?>"><?php echo esc_html( $title ); ?></h2>
					<?php if ( '' !== $intro ) : ?>
						<p class="services-category-section-v2__intro"><?php echo wp_kses_post( $intro ); ?></p>
					<?php endif; ?>
				</div>
			</div>
		</header>

		<?php if ( '' !== $lead ) : ?>
			<p class="services-category-section-v2__lead"><?php echo wp_kses_post( $lead ); ?></p>
		<?php endif; ?>

		<div class="services-category-section-v2__services">
			<?php
			foreach ( $children as $child ) {
				if ( ! is_array( $child ) ) {
					continue;
				}

				set_query_var( 'service_card_title', isset( $child['title'] ) ? $child['title'] : '' );
				set_query_var( 'service_card_url', isset( $child['url'] ) ? $child['url'] : '' );
				set_query_var( 'service_card_text', isset( $child['text'] ) ? $child['text'] : '' );
				set_query_var( 'service_card_variant', 'v2' );
				get_template_part( 'template-parts/components/service-card' );
			}
			?>
		</div>

		<?php if ( ! empty( $gallery ) ) : ?>
			<div class="services-category-section-v2__gallery">
				<?php foreach ( $gallery as $image ) : ?>
					<?php
					if ( ! is_array( $image ) || empty( $image['url'] ) ) {
						continue;
					}
					?>
					<figure class="services-category-section-v2__gallery-item">
						<img
							class="services-category-section-v2__gallery-image"
							src="<?php echo esc_url( $image['url'] ); ?>"
							width="<?php echo isset( $image['width'] ) ? (int) $image['width'] : ''; ?>"
							height="<?php echo isset( $image['height'] ) ? (int) $image['height'] : ''; ?>"
							alt="<?php echo esc_attr( isset( $image['alt'] ) ? (string) $image['alt'] : '' ); ?>"
							loading="lazy"
						>
						<?php if ( ! empty( $image['caption'] ) ) : ?>
							<figcaption class="services-category-section-v2__caption"><?php echo esc_html( (string) $image['caption'] ); ?></figcaption>
						<?php endif; ?>
					</figure>
				<?php endforeach; ?>
			</div>
		<?php endif; ?>

		<div class="services-category-section-v2__actions">
			<button
				type="button"
				class="btn btn_dark btn--primary services-category-section-v2__cta"
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
