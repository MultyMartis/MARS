<?php
/**
 * Template part: home/treatment-prevention.php
 *
 * V9-06E32: accordion groups/links from published service CPT hierarchy.
 * V9-06E40: heading/lead from Home ACF with static fallbacks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! shpigovsky_home_list_enabled( 'home_treatment_prevention_visible' ) ) {
	return;
}

$groups = shpigovsky_get_home_service_accordion_groups();

if ( empty( $groups ) ) {
	return;
}

$icon_uri = shpigovsky_asset_uri( 'svg/external-link.svg' );
$heading  = shpigovsky_home_text_or_fallback(
	'home_treatment_prevention_heading',
	'Лечение и&nbsp;профилактика'
);
$lead = shpigovsky_home_text_or_fallback(
	'home_treatment_prevention_lead',
	'Мы работаем с&nbsp;зависимостью не&nbsp;как с&nbsp;проступком, а&nbsp;как с&nbsp;состоянием, у&nbsp;которого есть биологические, психологические и&nbsp;социальные причины.'
);

?>
<section data-reveal class="home-treatment-prevention" aria-labelledby="home-treatment-prevention-heading">

  <div class="container">

    <div class="home-treatment-prevention__head">

      <h2 class="home-treatment-prevention__heading" id="home-treatment-prevention-heading"><?php echo wp_kses_post( $heading ); ?></h2>

      <a class="home-treatment-prevention__all-link" href="<?php echo esc_url( home_url( '/uslugi/' ) ); ?>">

        <span class="home-treatment-prevention__all-text">Смотреть&nbsp;все</span>

        <span class="home-treatment-prevention__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>

      </a>

    </div>

    <p class="home-treatment-prevention__lead"><?php echo wp_kses_post( $lead ); ?></p>

    <div class="home-treatment-prevention__accordion" data-accordion>
      <?php foreach ( $groups as $group_index => $group ) : ?>
        <?php
			$group_title = isset( $group['title'] ) ? trim( (string) $group['title'] ) : '';
			$items       = isset( $group['items'] ) && is_array( $group['items'] ) ? $group['items'] : array();
			if ( '' === $group_title || empty( $items ) ) {
				continue;
			}
			$panel_num   = $group_index + 1;
			$panel_id    = 'home-treatment-prevention-panel-' . $panel_num;
			$trigger_id  = 'home-treatment-prevention-trigger-' . $panel_num;
			$is_open     = 0 === $group_index;
			?>
      <div class="home-treatment-prevention__item" data-accordion-item>

        <h3 class="home-treatment-prevention__item-title">

          <button
            type="button"
            class="home-treatment-prevention__toggle"
            data-accordion-button
            aria-expanded="<?php echo $is_open ? 'true' : 'false'; ?>"
            aria-controls="<?php echo esc_attr( $panel_id ); ?>"
            id="<?php echo esc_attr( $trigger_id ); ?>"
          >

            <span class="home-treatment-prevention__toggle-label"><?php echo esc_html( $group_title ); ?></span>

            <span class="home-treatment-prevention__toggle-icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>

          </button>

        </h3>

        <div
          class="home-treatment-prevention__panel"
          data-accordion-panel
          id="<?php echo esc_attr( $panel_id ); ?>"
          role="region"
          aria-labelledby="<?php echo esc_attr( $trigger_id ); ?>"
          <?php echo $is_open ? '' : 'hidden'; ?>
        >

          <ul class="home-treatment-prevention__service-list">
            <?php foreach ( $items as $item ) : ?>
              <?php
				$item_title = isset( $item['title'] ) ? trim( (string) $item['title'] ) : '';
				$item_url   = isset( $item['url'] ) ? trim( (string) $item['url'] ) : '';
				$children   = isset( $item['children'] ) && is_array( $item['children'] ) ? $item['children'] : array();
				if ( '' === $item_title || '' === $item_url ) {
					continue;
				}
				?>
            <li class="home-treatment-prevention__service-list-item">
              <a class="home-treatment-prevention__service-item" href="<?php echo esc_url( $item_url ); ?>">
                <span class="home-treatment-prevention__service-name"><?php echo esc_html( $item_title ); ?></span>
                <span class="home-treatment-prevention__service-leader" aria-hidden="true"></span>
                <span class="home-treatment-prevention__service-icon" aria-hidden="true"><img class="home-treatment-prevention__service-icon-image" src="<?php echo esc_url( $icon_uri ); ?>" width="20" height="20" alt=""></span>
              </a>
              <?php if ( ! empty( $children ) ) : ?>
              <ul class="home-treatment-prevention__service-list home-treatment-prevention__service-list--children">
                <?php foreach ( $children as $child ) : ?>
                  <?php
					$child_title = isset( $child['title'] ) ? trim( (string) $child['title'] ) : '';
					$child_url   = isset( $child['url'] ) ? trim( (string) $child['url'] ) : '';
					if ( '' === $child_title || '' === $child_url ) {
						continue;
					}
					?>
                <li class="home-treatment-prevention__service-list-item">
                  <a class="home-treatment-prevention__service-item" href="<?php echo esc_url( $child_url ); ?>">
                    <span class="home-treatment-prevention__service-name"><?php echo esc_html( $child_title ); ?></span>
                    <span class="home-treatment-prevention__service-leader" aria-hidden="true"></span>
                    <span class="home-treatment-prevention__service-icon" aria-hidden="true"><img class="home-treatment-prevention__service-icon-image" src="<?php echo esc_url( $icon_uri ); ?>" width="20" height="20" alt=""></span>
                  </a>
                </li>
                <?php endforeach; ?>
              </ul>
              <?php endif; ?>
            </li>
            <?php endforeach; ?>
          </ul>

        </div>

      </div>
      <?php endforeach; ?>
    </div>

  </div>

</section>
