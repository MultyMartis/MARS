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
