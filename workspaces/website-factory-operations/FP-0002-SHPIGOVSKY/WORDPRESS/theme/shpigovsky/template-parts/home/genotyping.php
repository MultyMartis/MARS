<?php
/**
 * Template part: home/genotyping.php
 *
 * V9-06E40: ACF-wired Home genotyping block (not the program page).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$heading = shpigovsky_home_text_or_fallback(
	'home_genotyping_heading',
	'Генотипирование&nbsp;— инструмент диагностики'
);
$link_text = shpigovsky_home_text_or_fallback( 'home_genotyping_link_text', 'подробнее' );
$link_url  = shpigovsky_home_text_or_fallback(
	'home_genotyping_link_url',
	home_url( '/uslugi/zavisimosti/profilakticheskiy-analiz/' )
);
$lead = shpigovsky_home_text_or_fallback(
	'home_genotyping_lead',
	'анализ, который позволяет увидеть индивидуальные генетические особенности системы регуляции настроения. Не&nbsp;угадать. Не&nbsp;предположить. Измерить.'
);

$body_rows = array();
if ( shpigovsky_home_list_enabled( 'home_genotyping_body_enabled' ) ) {
	$body_rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback(
			'home_genotyping_body',
			shpigovsky_home_genotyping_body_fallback_rows()
		)
	);
}

$subheading = shpigovsky_home_text_or_fallback(
	'home_genotyping_subheading',
	'Кому полезно генетическоее исследование особенностей зависимости'
);
$list_intro = shpigovsky_home_text_or_fallback(
	'home_genotyping_list_intro',
	'В&nbsp;нашей лаборатории мы исследуем полиморфизмы генов, участвующих в&nbsp;индивидуальной реакции мозга на&nbsp;вещества, на&nbsp;самоощущения. Определенная генетическая панель показывает риски, снимает социальную стигму и&nbsp;чувство вины, доказывая, что зависимость&nbsp;— это комплексное заболевание, а&nbsp;не&nbsp;просто отсутствие силы воли. Чаще всего для проведения этого исследования к&nbsp;нам обращаются:'
);

$list_rows = array();
if ( shpigovsky_home_list_enabled( 'home_genotyping_items_enabled' ) ) {
	$list_rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback(
			'home_genotyping_items',
			shpigovsky_home_genotyping_items_fallback_rows()
		)
	);
}

$cta_label = shpigovsky_home_text_or_fallback(
	'home_genotyping_cta_label',
	'Записаться на консультацию'
);

?>
<section data-reveal class="home-genotyping" aria-labelledby="home-genotyping-heading">
  <div class="container">
    <div class="home-genotyping__head">
      <h2 class="home-genotyping__heading" id="home-genotyping-heading"><?php echo wp_kses_post( $heading ); ?></h2>
      <a class="home-genotyping__all-link" href="<?php echo esc_url( $link_url ); ?>">
        <span class="home-genotyping__all-text"><?php echo esc_html( wp_strip_all_tags( $link_text ) ); ?></span>
        <span class="home-genotyping__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <p class="home-genotyping__lead"><?php echo wp_kses_post( $lead ); ?></p>

    <?php if ( ! empty( $body_rows ) ) : ?>
    <div class="home-genotyping__body">
      <?php foreach ( $body_rows as $row ) : ?>
        <?php
			$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $text ) {
				continue;
			}
			?>
      <p class="home-genotyping__text"><?php echo wp_kses_post( $text ); ?></p>
      <?php endforeach; ?>
    </div>
    <?php endif; ?>

    <div class="UNIVERSAL-requirements__support">
    <h3 class="home-genotyping__subheading"><?php echo wp_kses_post( $subheading ); ?></h3>
    <p class="home-genotyping__text"><?php echo wp_kses_post( $list_intro ); ?></p>
    <?php if ( ! empty( $list_rows ) ) : ?>
    <ul class="home-genotyping__list">
      <?php foreach ( $list_rows as $row ) : ?>
        <?php
			$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $text ) {
				continue;
			}
			?>
      <li class="home-genotyping__list-item"><?php echo wp_kses_post( $text ); ?></li>
      <?php endforeach; ?>
    </ul>
    <?php endif; ?>

    <div class="home-genotyping__actions">
      <button
        type="button"
        class="btn btn_dark btn--primary home-genotyping__cta"
        data-modal-open="consultation"
        data-modal-source="genotyping"
        data-modal-title="<?php echo esc_attr( wp_strip_all_tags( $cta_label ) ); ?>"
        data-modal-submit-text="<?php echo esc_attr( wp_strip_all_tags( $cta_label ) ); ?>"
      ><?php echo esc_html( wp_strip_all_tags( $cta_label ) ); ?></button>
    </div>

    </div>
    
  </div>
</section>
