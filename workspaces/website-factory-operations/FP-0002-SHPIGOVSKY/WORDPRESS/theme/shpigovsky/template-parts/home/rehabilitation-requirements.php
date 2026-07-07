<?php
/**
 * Template part: home/rehabilitation-requirements.php
 *
 * V9-06E21: block options with V9 static fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$heading        = shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_heading', 'Что нужно для прохождения реабилитации и лечения' );
$intro          = shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_intro', 'Мы гарантируем конфиденциальность, уважение к личности, поддержание комфортной, психологически безопасной атмосферы.' );
$steps          = shpigovsky_get_rehab_requirements_steps();
$cta_lead       = shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_cta_lead', 'Узнайте подробнее об условиях поступления и стоимости лечения по телефону горячей линии' );
$cta_phone      = shpigovsky_get_rehab_requirements_cta_phone();
$cta_button     = shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_cta_button_label', 'Записаться' );
$support_heading = shpigovsky_get_rehab_requirements_scalar( 'rehab_requirements_support_heading', 'Поддержка осуществляется на всех этапах:' );
$support_items  = shpigovsky_get_rehab_requirements_support_items();
$photo          = shpigovsky_get_rehab_requirements_photo();

?>
<section data-reveal class="home-rehabilitation-requirements" aria-labelledby="home-rehabilitation-requirements-heading">
  <div class="container">
    <h2 class="home-rehabilitation-requirements__heading" id="home-rehabilitation-requirements-heading"><?php echo wp_kses_post( $heading ); ?></h2>
    <p class="block-whith-red-line"><?php echo wp_kses_post( $intro ); ?></p>

    <ol class="home-rehabilitation-requirements__steps">
      <?php foreach ( $steps as $index => $step ) : ?>
      <li class="home-rehabilitation-requirements__step">
        <span class="home-rehabilitation-requirements__step-number" aria-hidden="true"><?php echo esc_html( sprintf( '%02d', $index + 1 ) ); ?></span>
        <div class="home-rehabilitation-requirements__step-body">
          <h3 class="home-rehabilitation-requirements__step-title"><?php echo wp_kses_post( $step['title'] ); ?></h3>
          <p class="home-rehabilitation-requirements__step-text"><?php echo wp_kses_post( $step['text'] ); ?></p>
        </div>
      </li>
      <?php endforeach; ?>
    </ol>

    <div class="home-rehabilitation-requirements__cta-band">
      <p class="home-rehabilitation-requirements__cta-lead"><?php echo wp_kses_post( $cta_lead ); ?></p>
      <a class="home-rehabilitation-requirements__cta-phone" href="<?php echo esc_url( $cta_phone['href'] ); ?>"><?php echo esc_html( $cta_phone['display'] ); ?></a>
      <button
        type="button"
        class="btn btn_dark btn--primary home-rehabilitation-requirements__cta-button"
        data-modal-open="consultation"
        data-modal-source="rehabilitation"
        data-modal-title="<?php echo esc_attr( $cta_button ); ?>"
        data-modal-submit-text="<?php echo esc_attr( $cta_button ); ?>"
      ><?php echo esc_html( $cta_button ); ?></button>
    </div>

    <div class="home-rehabilitation-requirements__support">
      <p class="home-rehabilitation-requirements__support-heading"><?php echo wp_kses_post( $support_heading ); ?></p>
      <ul class="home-rehabilitation-requirements__support-list">
        <?php foreach ( $support_items as $item ) : ?>
        <li class="home-rehabilitation-requirements__support-item"><?php echo wp_kses_post( $item ); ?></li>
        <?php endforeach; ?>
      </ul>
    </div>

    <div class="home-rehabilitation-requirements__photo-bleed">
      <img
        class="home-rehabilitation-requirements__photo"
        src="<?php echo esc_url( $photo['url'] ); ?>"
        width="<?php echo esc_attr( (string) $photo['width'] ); ?>"
        height="<?php echo esc_attr( (string) $photo['height'] ); ?>"
        alt="<?php echo esc_attr( $photo['alt'] ); ?>"
        loading="lazy"
        decoding="async"
      >
    </div>
  </div>
</section>
