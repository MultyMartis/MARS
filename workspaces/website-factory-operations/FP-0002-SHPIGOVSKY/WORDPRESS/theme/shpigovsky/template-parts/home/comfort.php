<?php
/**
 * Template part: home/comfort.php
 *
 * V9-06E21: block options with V9 static fallback.
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

    <div class="comfort__gallery">
      <?php foreach ( $gallery_items as $item ) : ?>
        <?php
		$item_classes = array( 'comfort__gallery-item' );

		if ( ! empty( $item['is_decor'] ) ) {
			$item_classes[] = 'comfort__gallery-item_decor';
		}

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
</section>
