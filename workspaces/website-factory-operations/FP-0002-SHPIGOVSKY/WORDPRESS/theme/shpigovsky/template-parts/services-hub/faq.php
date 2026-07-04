<?php
/**
 * Template part: services-hub/faq.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$faq_items = shpigovsky_get_services_hub_repeater( 'services_hub_faq_items' );

if ( empty( $faq_items ) ) {
	return;
}
?>
<section data-reveal class="faq" aria-labelledby="services-hub-faq-heading">
	<div class="container">
		<h2 class="faq__heading" id="services-hub-faq-heading">
			<?php echo esc_html__( 'Нас часто спрашивают', 'shpigovsky' ); ?>
		</h2>

		<div class="faq__list" data-accordion>
			<?php foreach ( $faq_items as $index => $item ) : ?>
				<?php
				$question = isset( $item['question'] ) ? trim( (string) $item['question'] ) : '';
				$answer   = isset( $item['answer'] ) ? trim( (string) $item['answer'] ) : '';

				if ( '' === $question || '' === $answer ) {
					continue;
				}

				$panel_id   = 'services-hub-faq-panel-' . ( $index + 1 );
				$trigger_id = 'services-hub-faq-trigger-' . ( $index + 1 );
				$expanded   = 0 === $index;
				?>
				<div class="faq__item" data-accordion-item>
					<h3 class="faq__item-title">
						<button
							type="button"
							class="faq__question"
							data-accordion-button
							aria-expanded="<?php echo $expanded ? 'true' : 'false'; ?>"
							aria-controls="<?php echo esc_attr( $panel_id ); ?>"
							id="<?php echo esc_attr( $trigger_id ); ?>"
						>
							<span class="faq__question-label"><?php echo esc_html( $question ); ?></span>
							<span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
						</button>
					</h3>
					<div
						class="faq__answer-panel"
						data-accordion-panel
						id="<?php echo esc_attr( $panel_id ); ?>"
						role="region"
						aria-labelledby="<?php echo esc_attr( $trigger_id ); ?>"
						<?php echo $expanded ? '' : 'hidden'; ?>
					>
						<p class="faq__answer"><?php echo wp_kses_post( $answer ); ?></p>
					</div>
				</div>
			<?php endforeach; ?>
		</div>
	</div>
</section>
