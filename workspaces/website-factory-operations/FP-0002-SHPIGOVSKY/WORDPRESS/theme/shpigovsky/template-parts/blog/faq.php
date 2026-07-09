<?php
/**
 * Blog single FAQ — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$faq_items = shpigovsky_get_article_faq_items( get_the_ID() );

if ( empty( $faq_items ) ) {
	return;
}
?>
<section data-reveal class="faq blog-article-faq" aria-labelledby="blog-article-faq-heading">
	<div class="container">
		<h2 class="faq__heading" id="blog-article-faq-heading"><?php esc_html_e( 'Частые вопросы', 'shpigovsky' ); ?></h2>
		<div class="faq__list" data-accordion>
			<?php foreach ( $faq_items as $index => $item ) : ?>
				<?php
				$item_number = $index + 1;
				$panel_id    = 'blog-article-faq-panel-' . $item_number;
				$trigger_id  = 'blog-article-faq-trigger-' . $item_number;
				?>
				<div class="faq__item" data-accordion-item>
					<h3 class="faq__item-title">
						<button
							type="button"
							class="faq__question"
							data-accordion-button
							aria-expanded="false"
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
						hidden
					>
						<p class="faq__answer"><?php echo wp_kses_post( $item['answer'] ); ?></p>
					</div>
				</div>
			<?php endforeach; ?>
		</div>
	</div>
</section>
