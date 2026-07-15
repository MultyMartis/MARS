<?php
/**
 * Template part: home/why-us.php
 *
 * V9-06E40: ACF-wired with static V9 fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$heading = shpigovsky_home_text_or_fallback(
	'home_why_us_heading',
	'Нас выбирают за&nbsp;мультидисциплинарный подход к&nbsp;лечению'
);
$lead = shpigovsky_home_text_or_fallback(
	'home_why_us_lead',
	'У&nbsp;нас команда, а&nbsp;не&nbsp;конвейер. Каждый клиент получает полное внимание&nbsp;— психолога, нейропсихолога, специалиста по&nbsp;кинезиотерапии, специалиста по&nbsp;телесноориентированной терапии и&nbsp;координатора программы.'
);

$body_rows = array();
if ( shpigovsky_home_list_enabled( 'home_why_us_body_enabled' ) ) {
	$body_rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback(
			'home_why_us_body',
			shpigovsky_home_why_us_body_fallback_rows()
		)
	);
}

$link_rows = array();
if ( shpigovsky_home_list_enabled( 'home_why_us_items_enabled' ) ) {
	$link_rows = shpigovsky_home_filter_enabled_rows(
		shpigovsky_home_repeater_or_fallback(
			'home_why_us_items',
			shpigovsky_home_why_us_items_fallback_rows()
		)
	);
}

$icon_uri = shpigovsky_asset_uri( 'svg/external-link.svg' );

?>
<section data-reveal class="home-why-us @@class" aria-labelledby="home-why-us-heading">
  <div class="container">
    <h2 class="home-why-us__heading" id="home-why-us-heading"><?php echo wp_kses_post( $heading ); ?></h2>
    <p class="home-why-us__lead"><?php echo wp_kses_post( $lead ); ?></p>
    <?php if ( ! empty( $body_rows ) ) : ?>
    <div class="home-why-us__body-stack">
      <?php foreach ( $body_rows as $row ) : ?>
        <?php
			$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
			if ( '' === $text ) {
				continue;
			}
			?>
      <p class="home-why-us__body"><span><?php echo wp_kses_post( $text ); ?></span></p>
      <?php endforeach; ?>
    </div>
    <?php endif; ?>

        <?php if ( ! empty( $link_rows ) ) : ?>
        <div
          class="home-treatment-prevention__panel"
          data-accordion-panel
          id="home-why-us-services-panel"
          role="region"
          aria-labelledby="home-why-us-heading"
        >
          <ul class="home-treatment-prevention__service-list">
            <?php foreach ( $link_rows as $row ) : ?>
              <?php
				$item_title = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
				$item_url   = isset( $row['url'] ) ? trim( (string) $row['url'] ) : '';
				if ( '' === $item_title || '' === $item_url ) {
					continue;
				}
				?>
            <li class="home-treatment-prevention__service-list-item">
              <a
                class="home-treatment-prevention__service-item"
                href="<?php echo esc_url( $item_url ); ?>"
              >
                <span class="home-treatment-prevention__service-name"><?php echo esc_html( $item_title ); ?></span>
                <span class="home-treatment-prevention__service-leader" aria-hidden="true"></span>
                <span class="home-treatment-prevention__service-icon" aria-hidden="true"><img class="home-treatment-prevention__service-icon-image" src="<?php echo esc_url( $icon_uri ); ?>" width="20" height="20" alt=""></span>
              </a>
            </li>
            <?php endforeach; ?>
          </ul>
        </div>
        <?php endif; ?>

  </div>
</section>
