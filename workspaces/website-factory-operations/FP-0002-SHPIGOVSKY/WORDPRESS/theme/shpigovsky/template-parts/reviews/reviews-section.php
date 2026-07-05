<?php
/**
 * Template part: reviews/reviews-section.php
 *
 * D9-R: shared reviews slider on /otzyvy/ page.
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
		'context'       => 'reviews_page',
		'limit'         => 0,
		'featured_only' => false,
		'section_class' => 'reviews reviews--page',
		'show_heading'  => false,
		'show_all_link' => false,
	)
);
