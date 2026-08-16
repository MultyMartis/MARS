<?php
/**
 * Template part: components/fp02-slider-mobile-nav.php
 *
 * PROD-P08 — compact prev/next for non-Hero sliders (visible ≤767px via CSS).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$args = wp_parse_args(
	$args ?? array(),
	array(
		'class' => '',
	)
);

$extra_class = trim( (string) $args['class'] );
$root_class  = 'fp02-slider-nav';
if ( '' !== $extra_class ) {
	$root_class .= ' ' . $extra_class;
}
?>
<div class="<?php echo esc_attr( $root_class ); ?>" data-fp02-slider-nav>
	<button
		class="fp02-slider-nav__btn fp02-slider-nav__btn--prev"
		type="button"
		data-fp02-slider-prev
		aria-label="<?php echo esc_attr__( 'Предыдущий слайд', 'shpigovsky' ); ?>"
	>
		<span aria-hidden="true">‹</span>
	</button>
	<button
		class="fp02-slider-nav__btn fp02-slider-nav__btn--next"
		type="button"
		data-fp02-slider-next
		aria-label="<?php echo esc_attr__( 'Следующий слайд', 'shpigovsky' ); ?>"
	>
		<span aria-hidden="true">›</span>
	</button>
</div>
