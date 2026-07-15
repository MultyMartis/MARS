<?php
/**
 * Template part: home/recovery-life.php
 *
 * V9-06E40: ACF-wired with static V9 fallbacks. Preserve E36 mobile CSS behavior.
 * V9-06E41: stage wrapper/inner + month labels.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$heading = shpigovsky_home_text_or_fallback(
	'home_recovery_life_heading',
	'Как меняется жизнь человека в&nbsp;процессе восстановления'
);
$highlight = shpigovsky_home_text_or_fallback(
	'home_recovery_life_highlight',
	'У&nbsp;нас команда, а&nbsp;не&nbsp;конвейер. Каждый клиент получает полное внимание&nbsp;— психолога, нейропсихолога, специалиста по&nbsp;кинезиотерапии, специалиста по&nbsp;телесноориентированной терапии и&nbsp;координатора программы.'
);

$intro_rows = array();
if ( shpigovsky_home_list_enabled( 'home_recovery_life_intro_enabled' ) ) {
	$intro_rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback(
			'home_recovery_life_intro',
			shpigovsky_home_recovery_life_intro_fallback_rows()
		)
	);
}

$stage_rows = array();
if ( shpigovsky_home_list_enabled( 'home_recovery_life_stages_enabled' ) ) {
	$stage_rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback(
			'home_recovery_life_stages',
			shpigovsky_home_recovery_life_stages_fallback_rows()
		)
	);
}

?>
<section data-reveal class="home-recovery-life" aria-labelledby="home-recovery-life-title">
  <div class="container">

    <div class="home-recovery-life__content">
      <h2 class="home-recovery-life__heading" id="home-recovery-life-title"><?php echo wp_kses_post( $heading ); ?></h2>

      <p class="home-recovery-life__highlight"><?php echo wp_kses_post( $highlight ); ?></p>

      <?php if ( ! empty( $intro_rows ) ) : ?>
      <div class="home-recovery-life__intro">
        <?php foreach ( $intro_rows as $row ) : ?>
          <?php
			$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $text ) {
				continue;
			}
			?>
        <p class="home-recovery-life__intro-text"><span><?php echo wp_kses_post( $text ); ?></span></p>
        <?php endforeach; ?>
      </div>
      <?php endif; ?>

    </div>
      <?php if ( ! empty( $stage_rows ) ) : ?>
      <ol class="home-recovery-life__stages">
        <?php
		$stage_index = 0;
		foreach ( $stage_rows as $stage ) :
			$stage_index++;
			$stage_title = isset( $stage['title'] ) ? trim( (string) $stage['title'] ) : '';
			$items_text  = isset( $stage['items_text'] ) ? (string) $stage['items_text'] : '';
			$items       = shpigovsky_home_lines_to_items( $items_text );
			$stage_label = isset( $stage['stage_label'] ) ? trim( (string) $stage['stage_label'] ) : '';
			if ( '' === $stage_label ) {
				$stage_label = sprintf(
					/* translators: %d: month number starting at 1 */
					__( '%d месяц', 'shpigovsky' ),
					$stage_index
				);
			}
			if ( '' === $stage_title && empty( $items ) ) {
				continue;
			}
			?>
        <li class="home-recovery-life__stage">
          <p class="home-recovery-life__stage-label"><?php echo esc_html( $stage_label ); ?></p>
          <div class="home-recovery-life__stage-inner">
            <?php if ( '' !== $stage_title ) : ?>
            <h3 class="home-recovery-life__stage-title"><?php echo wp_kses_post( $stage_title ); ?></h3>
            <?php endif; ?>
            <?php if ( ! empty( $items ) ) : ?>
            <ul class="home-recovery-life__stage-list">
              <?php foreach ( $items as $item ) : ?>
              <li class="home-recovery-life__stage-item"><?php echo wp_kses_post( $item ); ?></li>
              <?php endforeach; ?>
            </ul>
            <?php endif; ?>
          </div>
        </li>
        <?php endforeach; ?>
      </ol>
      <?php endif; ?>


  </div>
</section>
