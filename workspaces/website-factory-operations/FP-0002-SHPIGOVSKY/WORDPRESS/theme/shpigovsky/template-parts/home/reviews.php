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

get_template_part(
	'template-parts/shared/reviews-slider',
	null,
	array(
		'context'       => 'home',
		'limit'         => 10,
		'featured_only' => true,
		'section_class' => 'reviews',
		'show_heading'  => true,
		'show_all_link' => true,
	)
);
