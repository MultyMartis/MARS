<?php
/**
 * Template part: home/staff-photo.php
 *
 * V9-06E40: ACF image with theme asset fallback.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$image = shpigovsky_home_image_or_asset(
	'home_staff_photo_image',
	'img/content/pre-reviews/shpigovsky-staff-group.webp',
	'Команда специалистов реабилитационного центра',
	1139,
	443
);

$args            = isset( $args ) && is_array( $args ) ? $args : array();
$extra_classes   = isset( $args['class'] ) ? trim( (string) $args['class'] ) : '';
$section_classes = trim( 'home-staff-photo ' . $extra_classes );

?>
<section data-reveal class="<?php echo esc_attr( $section_classes ); ?>" aria-label="Команда центра">
  <div class="container">
    <div class="home-staff-photo__bleed">
      <img
        class="home-staff-photo__image"
        src="<?php echo esc_url( $image['url'] ); ?>"
        width="<?php echo esc_attr( (string) $image['width'] ); ?>"
        height="<?php echo esc_attr( (string) $image['height'] ); ?>"
        alt="<?php echo esc_attr( $image['alt'] ); ?>"
        loading="lazy"
        decoding="async"
      >
    </div>
  </div>
</section>
