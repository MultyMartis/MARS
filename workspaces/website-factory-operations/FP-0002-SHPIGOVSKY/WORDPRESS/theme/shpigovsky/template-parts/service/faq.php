<?php
/**
 * Template part: service/faq.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id   = shpigovsky_get_current_service_id();
$variant   = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$faq_items = shpigovsky_get_service_repeater( $post_id, 'faq_items' );

if ( empty( $faq_items ) ) {
	return;
}

$section_id = 'subdivision' === $variant ? 'service-subdivision-faq' : 'service-leaf-faq';
$heading_id = $section_id . '-heading';
?>
<section data-reveal class="faq" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container">
		<h2 class="faq__heading" id="<?php echo esc_attr( $heading_id ); ?>">
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

				$panel_id   = $section_id . '-panel-' . ( $index + 1 );
				$trigger_id = $section_id . '-trigger-' . ( $index + 1 );
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
