<?php
/**
 * Template part: home/rehabilitation-program.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * V9-06E31: program direction links to /o-centre/programma-lecheniya/* pages.
 * V9-06E41-FIX01: head/lead/intro from Home ACF with frontend fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_home_list_enabled( 'home_rehab_program_visible' ) ) {
	return;
}

$directions = shpigovsky_get_program_direction_items( 'home' );

$head = shpigovsky_home_text_or_fallback(
	'home_rehabilitation_program_head',
	'Программа центра включает 4&nbsp;направления'
);
$lead = shpigovsky_home_text_or_fallback(
	'home_rehabilitation_program_lead',
	'Не&nbsp;просто снимаем симптомы. Мы помогаем разобраться в&nbsp;том, что именно в&nbsp;жизни, истории привело к&nbsp;этой точке.'
);
$intro_1 = shpigovsky_home_text_or_fallback(
	'home_rehabilitation_program_intro_1',
	'Каждый человек приходит к&nbsp;нам со&nbsp;своей историей. Со&nbsp;своим сочетанием причин, обстоятельств и&nbsp;состояний, которые привели его туда, где он сейчас находится. Именно поэтому универсальных программ в&nbsp;нашем центре не&nbsp;существует.'
);
$intro_2 = shpigovsky_home_text_or_fallback(
	'home_rehabilitation_program_intro_2',
	'Программа реабилитации выстраивается из&nbsp;отдельных блоков&nbsp;— каждый из&nbsp;которых направлен на&nbsp;свой уровень работы: генетические предрасположенности, нейрологические паттерны, психологическое состояние и&nbsp;физическое восстановление тела. Вместе они создают целостный, по-настоящему индивидуальный маршрут&nbsp;— такой, который работает именно для вас.'
);

?>
<section data-reveal class="home-rehabilitation-program" aria-labelledby="home-rehabilitation-program-heading">
  <div class="container">
    <div class="home-rehabilitation-program__head">
      <h2 class="home-rehabilitation-program__heading" id="home-rehabilitation-program-heading"><?php echo wp_kses_post( $head ); ?></h2>
      <a class="home-rehabilitation-program__all-link" href="<?php echo esc_url( home_url( '/o-centre/programma-lecheniya/' ) ); ?>">
        <span class="home-rehabilitation-program__all-text">подробнее</span>
        <span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <p class="home-rehabilitation-program__lead"><?php echo wp_kses_post( $lead ); ?></p>

    <p class="home-rehabilitation-program__intro"><?php echo wp_kses_post( $intro_1 ); ?></p>

    <p class="home-rehabilitation-program__intro"><?php echo wp_kses_post( $intro_2 ); ?></p>

    <div class="home-rehabilitation-program__directions">
      <?php foreach ( $directions as $direction ) : ?>
      <article class="home-rehabilitation-program__direction">
        <div class="home-rehabilitation-program__direction--img">
        <a class="home-rehabilitation-program__direction-image-link" href="<?php echo esc_url( $direction['url'] ); ?>">
        <img
          class="home-rehabilitation-program__direction-image"
          src="<?php echo esc_url( $direction['image'] ); ?>"
          width="<?php echo (int) $direction['width']; ?>"
          height="<?php echo (int) $direction['height']; ?>"
          alt="<?php echo esc_attr( $direction['alt'] ); ?>"
          loading="lazy"
          decoding="async"
        >
        </a>
        </div>
        <div class="home-rehabilitation-program__direction--wrapper">
        <h3 class="home-rehabilitation-program__direction-title">
          <a class="home-rehabilitation-program__direction-title-link" href="<?php echo esc_url( $direction['url'] ); ?>"><?php echo esc_html( $direction['marker'] ); ?>&nbsp;— <?php echo esc_html( $direction['title'] ); ?></a>
        </h3>
        <p class="home-rehabilitation-program__direction-text"><?php echo wp_kses_post( $direction['text'] ); ?></p>
        <a class="home-rehabilitation-program__direction-more" href="<?php echo esc_url( $direction['url'] ); ?>">Подробнее&nbsp;&gt;</a>
        </div>
      </article>
      <?php endforeach; ?>
    </div>
  </div>
</section>
