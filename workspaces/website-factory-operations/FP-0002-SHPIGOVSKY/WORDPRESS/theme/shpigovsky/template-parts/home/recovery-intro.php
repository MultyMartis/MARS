<?php
/**
 * Template part: home/recovery-intro.php
 *
 * D9-D / V9-06E40: ACF-wired with theme fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$intro_heading = shpigovsky_home_text_or_fallback(
	'home_recovery_intro_heading',
	'Шпиговский дом&nbsp;&mdash; восстановление, построенное вокруг человека'
);
$intro_lead_1 = shpigovsky_home_text_or_fallback(
	'home_recovery_intro_lead_1',
	'Мы&nbsp;убеждены, зависимость невозможно эффективно лечить по&nbsp;шаблону. За&nbsp;каждым случаем стоит уникальная история, особенности личности, семейной системы, биологии и&nbsp;жизненного опыта.'
);
$intro_lead_2 = shpigovsky_home_text_or_fallback(
	'home_recovery_intro_lead_2',
	'Поэтому в&nbsp;&laquo;Шпиговском Доме&raquo; мы&nbsp;создаём персонализированную программу восстановления, которая учитывает не&nbsp;только симптомы зависимости, но&nbsp;и&nbsp;её&nbsp;причины'
);

$intro_benefits = array();
if ( shpigovsky_home_list_enabled( 'home_recovery_intro_benefits_enabled' ) ) {
	$benefit_rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback(
			'home_recovery_intro_benefits',
			shpigovsky_home_recovery_intro_benefits_fallback_rows()
		)
	);
	foreach ( $benefit_rows as $row ) {
		$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
		if ( '' !== $text ) {
			$intro_benefits[] = $text;
		}
	}
	if ( empty( $intro_benefits ) ) {
		$intro_benefits = shpigovsky_home_recovery_intro_benefits_fallback();
	}
}

$intro_cards = shpigovsky_home_repeater_or_fallback(
	'home_intro_bands',
	shpigovsky_home_intro_bands_fallback_items()
);

?>
<section data-reveal class="home-recovery-intro" aria-labelledby="home-recovery-intro-heading">

  

  <div class="container">

    <div class="home-recovery-intro--wrapper">

      <div class="home-recovery-intro__content">
        <h2 class="home-recovery-intro__heading" id="home-recovery-intro-heading"><?php echo wp_kses_post( $intro_heading ); ?></h2>
        <p class="home-recovery-intro__lead"><span><?php echo wp_kses_post( $intro_lead_1 ); ?></span></p>
        <p class="home-recovery-intro__lead"><span><?php echo wp_kses_post( $intro_lead_2 ); ?></span></p>
        <?php if ( ! empty( $intro_benefits ) ) : ?>
        <ul class="home-recovery-intro__benefits">
          <?php foreach ( $intro_benefits as $benefit ) : ?>
          <li class="home-recovery-intro__benefits-item"><?php echo wp_kses_post( $benefit ); ?></li>
          <?php endforeach; ?>
        </ul>
        <?php endif; ?>
      </div>

      <ul class="home-recovery-intro__card-grid">
        <?php foreach ( $intro_cards as $card ) : ?>
          <?php
			$card_title = isset( $card['title'] ) ? trim( (string) $card['title'] ) : '';
			$card_text  = isset( $card['text'] ) ? trim( (string) $card['text'] ) : '';

			if ( '' === $card_title && '' === $card_text ) {
				continue;
			}
			?>
        <li class="home-recovery-intro__card">
          <span class="home-recovery-intro__card-icon" aria-hidden="true"><i class="fas fa-check"></i>
          <h3 class="home-recovery-intro__card-title"><?php echo wp_kses_post( $card_title ); ?></h3></span>
          <p class="home-recovery-intro__card-text"><?php echo wp_kses_post( $card_text ); ?></p>
        </li>
        <?php endforeach; ?>
      </ul>
    </div>

  </div>

</section>
