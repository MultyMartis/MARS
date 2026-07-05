<?php
/**
 * Template part: home/faq.php
 *
 * D9-H: ACF wiring with static V9 fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$faq_heading = shpigovsky_home_text_or_fallback( 'home_faq_heading', 'Нас часто спрашивают' );
$acf_rows    = shpigovsky_get_home_repeater( 'home_faq_items' );
$faq_items   = ! empty( $acf_rows )
	? shpigovsky_home_normalize_faq_rows( $acf_rows )
	: shpigovsky_home_faq_fallback_items();

?>
<section data-reveal class="faq" aria-labelledby="faq-heading">
  <div class="container">
    <h2 class="faq__heading" id="faq-heading"><?php echo esc_html( $faq_heading ); ?></h2>

    <div class="faq__list" data-accordion>
      <?php foreach ( $faq_items as $index => $item ) : ?>
        <?php
		$item_number   = $index + 1;
		$is_expanded   = ! empty( $item['expanded'] );
		$panel_id      = 'faq-panel-' . $item_number;
		$trigger_id    = 'faq-trigger-' . $item_number;
		$answer_parts  = shpigovsky_home_faq_answer_paragraphs( $item['answer'] );
		$use_multiline = ! empty( $item['multiline'] ) || count( $answer_parts ) > 1;
		?>
      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button
            type="button"
            class="faq__question"
            data-accordion-button
            aria-expanded="<?php echo $is_expanded ? 'true' : 'false'; ?>"
            aria-controls="<?php echo esc_attr( $panel_id ); ?>"
            id="<?php echo esc_attr( $trigger_id ); ?>"
          >
            <span class="faq__question-label"><?php echo wp_kses_post( $item['question'] ); ?></span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div
          class="faq__answer-panel"
          data-accordion-panel
          id="<?php echo esc_attr( $panel_id ); ?>"
          role="region"
          aria-labelledby="<?php echo esc_attr( $trigger_id ); ?>"
          <?php echo $is_expanded ? '' : 'hidden'; ?>
        >
          <?php if ( $use_multiline ) : ?>
            <?php foreach ( $answer_parts as $part ) : ?>
              <p class="faq__answer"><?php echo wp_kses_post( $part ); ?></p>
            <?php endforeach; ?>
          <?php else : ?>
            <p class="faq__answer"><?php echo wp_kses_post( $item['answer'] ); ?></p>
          <?php endif; ?>
        </div>
      </div>
      <?php endforeach; ?>
    </div>
  </div>
</section>
