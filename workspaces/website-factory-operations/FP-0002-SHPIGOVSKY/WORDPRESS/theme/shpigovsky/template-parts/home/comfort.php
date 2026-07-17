<?php
/**
 * Template part: home/comfort.php
 *
 * V9-06E21: block options with V9 static fallback.
 * V9-06E59-FIX01: decor separated from actual gallery container.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( is_front_page() && ! shpigovsky_home_list_enabled( 'home_comfort_visible' ) ) {
	return;
}

if ( function_exists( 'shpigovsky_is_services_hub_page' ) && shpigovsky_is_services_hub_page() && ! shpigovsky_services_hub_list_enabled( 'services_hub_comfort_visible' ) ) {
	return;
}

$section_id      = isset( $args['section_id'] ) ? (string) $args['section_id'] : '';
$heading_id      = isset( $args['heading_id'] ) ? (string) $args['heading_id'] : 'comfort-heading';
$comfort_heading = shpigovsky_get_comfort_heading();
$comfort_lead    = shpigovsky_get_comfort_lead();
$comfort_link    = shpigovsky_get_comfort_all_link_label();
$comfort_link_url = shpigovsky_get_comfort_all_link_url();
$gallery_items   = shpigovsky_get_comfort_gallery_items();
$decor_item      = shpigovsky_get_comfort_gallery_decor_item();

?>
<section data-reveal class="comfort"<?php echo '' !== $section_id ? ' id="' . esc_attr( $section_id ) . '"' : ''; ?> aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
  <div class="container">
    <div class="comfort__head">
      <h2 class="comfort__heading" id="<?php echo esc_attr( $heading_id ); ?>"><?php echo esc_html( $comfort_heading ); ?></h2>
      <a class="comfort__all-link" href="<?php echo esc_url( $comfort_link_url ); ?>">
        <span class="comfort__all-text"><?php echo wp_kses_post( $comfort_link ); ?></span>
        <span class="comfort__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
      </a>
    </div>

    <p class="comfort__lead"><?php echo wp_kses_post( $comfort_lead ); ?></p>

    <div class="comfort__gallery-stage">
      <?php if ( is_array( $decor_item ) && ! empty( $decor_item['url'] ) ) : ?>
        <?php
		$decor_width  = ! empty( $decor_item['width'] ) ? (int) $decor_item['width'] : 0;
		$decor_height = ! empty( $decor_item['height'] ) ? (int) $decor_item['height'] : 0;
		?>
      <div class="comfort__gallery-decor" aria-hidden="true">
        <img class="comfort__gallery-decor-image" src="<?php echo esc_url( $decor_item['url'] ); ?>"<?php echo $decor_width > 0 ? ' width="' . esc_attr( (string) $decor_width ) . '"' : ' width="auto"'; ?><?php echo $decor_height > 0 ? ' height="' . esc_attr( (string) $decor_height ) . '"' : ' height="auto"'; ?> alt="" loading="lazy" decoding="async">
      </div>
      <?php endif; ?>

      <div class="comfort__gallery">
        <?php foreach ( $gallery_items as $item ) : ?>
          <?php
			$item_classes = array( 'comfort__gallery-item' );

			if ( ! empty( $item['is_wide'] ) ) {
				$item_classes[] = 'comfort__gallery-item--wide';
			}

			$width_attr  = ! empty( $item['width'] ) ? (int) $item['width'] : 0;
			$height_attr = ! empty( $item['height'] ) ? (int) $item['height'] : 0;
			$tag         = ! empty( $item['fancybox'] ) ? 'a' : 'div';
			$href_attr   = ! empty( $item['fancybox'] ) ? ' href="' . esc_url( $item['url'] ) . '" data-fancybox="comfort"' : '';
			?>
        <<?php echo esc_html( $tag ); ?> class="<?php echo esc_attr( implode( ' ', $item_classes ) ); ?>"<?php echo $href_attr; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>>
          <img class="comfort__gallery-image" src="<?php echo esc_url( $item['url'] ); ?>"<?php echo $width_attr > 0 ? ' width="' . esc_attr( (string) $width_attr ) . '"' : ' width="auto"'; ?><?php echo $height_attr > 0 ? ' height="' . esc_attr( (string) $height_attr ) . '"' : ' height="auto"'; ?> alt="" loading="lazy" decoding="async">
        </<?php echo esc_html( $tag ); ?>>
        <?php endforeach; ?>
      </div>
    </div>
  </div>
</section>
