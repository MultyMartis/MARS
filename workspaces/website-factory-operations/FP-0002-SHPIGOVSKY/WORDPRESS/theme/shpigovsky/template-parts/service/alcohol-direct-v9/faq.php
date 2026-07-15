<?php
/**
 * Service-leaf FAQ — ACF SoT (V9-06E47); visual parity with usluga-konechnaya-v1.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id    = shpigovsky_get_current_service_id();
$faq_items  = function_exists( 'shpigovsky_get_general_faq_items' )
	? shpigovsky_get_general_faq_items( $post_id )
	: array();
$section_id = 'service-leaf-faq';
$heading_id = 'service-leaf-faq-heading';
$heading    = function_exists( 'shpigovsky_general_text' )
	? shpigovsky_general_text( $post_id, 'service_general_faq_heading', __( 'Нас часто спрашивают', 'shpigovsky' ) )
	: __( 'Нас часто спрашивают', 'shpigovsky' );

if ( empty( $faq_items ) ) {
	return;
}
?>
<section data-reveal class="faq" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container">
		<h2 class="faq__heading" id="<?php echo esc_attr( $heading_id ); ?>">
			<?php echo esc_html( $heading ); ?>
		</h2>

		<div class="faq__list" data-accordion>
			<?php foreach ( $faq_items as $index => $item ) : ?>
				<?php
				$panel_id   = 'faq-panel-' . ( $index + 1 );
				$trigger_id = 'faq-trigger-' . ( $index + 1 );
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
							<span class="faq__question-label"><?php echo esc_html( $item['question'] ); ?></span>
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
						<?php foreach ( $item['answers'] as $answer ) : ?>
							<p class="faq__answer"><?php echo esc_html( $answer ); ?></p>
						<?php endforeach; ?>
					</div>
				</div>
			<?php endforeach; ?>
		</div>
	</div>
</section>
