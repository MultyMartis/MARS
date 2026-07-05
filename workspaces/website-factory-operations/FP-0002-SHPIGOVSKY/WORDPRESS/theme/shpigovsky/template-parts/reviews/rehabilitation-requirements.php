<?php
/**
 * Template part: reviews/rehabilitation-requirements.php
 *
 * Static V9 reviews page rehabilitation requirements — V9-06D9-W.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$phone_primary = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
$button_label  = shpigovsky_get_site_option( 'default_button_label' ) ?: 'Записаться';

set_query_var(
	'shpigovsky_program_cta_band',
	array(
		'title'        => 'Запишитесь на&nbsp;гостевой визит',
		'subtitle'     => 'Вы&nbsp;сможете все посмотреть и&nbsp;задать вопросы лично',
		'phone'        => $phone_primary ?: '8&nbsp;(925)&nbsp;183-64-64',
		'phone_hint'   => 'Или позвоните нам',
		'button_label' => $button_label,
		'source'       => 'reviews-rehabilitation-requirements-cta',
		'wrap_section' => false,
		'button_first' => true,
		'margin_flush' => true,
	)
);

?>
<section data-reveal class="reviews-rehabilitation-requirements" aria-labelledby="reviews-rehabilitation-requirements-heading">
  <div class="container reviews-rehabilitation-requirements__container">
    <h2 class="reviews-rehabilitation-requirements__heading" id="reviews-rehabilitation-requirements-heading">Что нужно для прохождения реабилитации и&nbsp;лечения</h2>
    <p class="reviews-rehabilitation-requirements__lead block-whith-red-line">Мы гарантируем конфиденциальность, уважение к&nbsp;личности, поддержание комфортной, психологически безопасной атмосферы.</p>

    <ol class="home-rehabilitation-requirements__steps reviews-rehabilitation-requirements__steps">
      <li class="home-rehabilitation-requirements__step">
        <span class="home-rehabilitation-requirements__step-number" aria-hidden="true">01</span>
        <div class="home-rehabilitation-requirements__step-body">
          <h3 class="home-rehabilitation-requirements__step-title">Связаться с&nbsp;нами</h3>
          <p class="home-rehabilitation-requirements__step-text">Расскажите нам о&nbsp;своей ситуации&nbsp;— в&nbsp;удобном для вас формате и&nbsp;в&nbsp;удобное время. Первый разговор ни&nbsp;к&nbsp;чему не&nbsp;обязывает, но&nbsp;часто становится началом перемен.</p>
        </div>
      </li>
      <li class="home-rehabilitation-requirements__step">
        <span class="home-rehabilitation-requirements__step-number" aria-hidden="true">02</span>
        <div class="home-rehabilitation-requirements__step-body">
          <h3 class="home-rehabilitation-requirements__step-title">Определить цели и&nbsp;программу</h3>
          <p class="home-rehabilitation-requirements__step-text">Вместе со&nbsp;специалистами центра мы разберёмся, что именно происходит, и&nbsp;составим программу, которая отвечает вашей ситуации.</p>
        </div>
      </li>
      <li class="home-rehabilitation-requirements__step">
        <span class="home-rehabilitation-requirements__step-number" aria-hidden="true">03</span>
        <div class="home-rehabilitation-requirements__step-body">
          <h3 class="home-rehabilitation-requirements__step-title">Выбрать категорию номера, период стационарного проживания</h3>
          <p class="home-rehabilitation-requirements__step-text">Комфорт среды&nbsp;— часть восстановления. Мы подберём условия проживания, которые подойдут именно вам, и&nbsp;согласуем удобные сроки.</p>
        </div>
      </li>
      <li class="home-rehabilitation-requirements__step">
        <span class="home-rehabilitation-requirements__step-number" aria-hidden="true">04</span>
        <div class="home-rehabilitation-requirements__step-body">
          <h3 class="home-rehabilitation-requirements__step-title">Начать реабилитацию и&nbsp;лечение</h3>
          <p class="home-rehabilitation-requirements__step-text">С&nbsp;первого дня рядом с&nbsp;вами будет команда специалистов. Здесь начинается то, ради чего вы пришли. Мы с&nbsp;вами&nbsp;— шаг за&nbsp;шагом, в&nbsp;вашем темпе.</p>
        </div>
      </li>
    </ol>

    <div class="reviews-rehabilitation-requirements__cta-wrap">
      <div class="reviews-rehabilitation-requirements__decor" aria-hidden="true"></div>
	  <?php get_template_part( 'template-parts/components/program-cta-band' ); ?>
    </div>

    <div class="home-rehabilitation-requirements__support reviews-rehabilitation-requirements__support">
      <p class="home-rehabilitation-requirements__support-heading">Поддержка осуществляется на&nbsp;всех этапах:</p>
      <ul class="home-rehabilitation-requirements__support-list">
        <li class="home-rehabilitation-requirements__support-item">Интервенция на&nbsp;лечение&nbsp;— мотивация вас или ваших близких;</li>
        <li class="home-rehabilitation-requirements__support-item">Круглосуточная поддержка психологов&nbsp;— в&nbsp;любое время будет оказана помощь;</li>
        <li class="home-rehabilitation-requirements__support-item">Занятия в&nbsp;мини-группах&nbsp;— эффективная работа с&nbsp;каждым;</li>
        <li class="home-rehabilitation-requirements__support-item">По&nbsp;договоренности, возможность удалённой работы в&nbsp;условиях стационара.</li>
      </ul>
    </div>

    <div class="home-rehabilitation-requirements__photo-bleed reviews-rehabilitation-requirements__photo-bleed">
      <img
        class="home-rehabilitation-requirements__photo reviews-rehabilitation-requirements__photo"
        src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp' ) ); ?>"
        width="1170"
        height="580"
        alt="Интерьер клиники"
        loading="lazy"
        decoding="async"
      >
    </div>
  </div>
</section>
