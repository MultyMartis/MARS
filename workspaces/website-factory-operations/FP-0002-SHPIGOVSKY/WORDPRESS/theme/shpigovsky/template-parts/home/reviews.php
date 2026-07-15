<?php
/**
 * Template part: home/reviews.php
 *
 * D9-R: thin wrapper around shared reviews slider include.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

// V9-06E46: Home toggle applies only on front page (do not hide section/hub reviews).
if ( is_front_page() && ! shpigovsky_home_list_enabled( 'home_reviews_visible' ) ) {
	return;
}

$slider_args = wp_parse_args(
	$args ?? array(),
	array(
		'context'       => 'home',
		'limit'         => 10,
		'featured_only' => true,
		'section_class' => 'reviews',
		'section_id'    => '',
		'show_heading'  => true,
		'show_all_link' => true,
	)
);

get_template_part( 'template-parts/shared/reviews-slider', null, $slider_args );
