<?php
/**
 * Template part: institutional/hero.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$page_id = (int) get_queried_object_id();
$hero    = shpigovsky_get_institutional_hero_context( $page_id );

get_template_part(
	'template-parts/shared/services-inner-hero-v2',
	null,
	array(
		'title_id'     => $hero['title_id'],
		'eyebrow'      => $hero['eyebrow'],
		'title'        => $hero['title'],
		'lead'         => $hero['lead'],
		'cta_label'    => $hero['cta_label'],
		'cta_source'   => $hero['cta_source'],
		'image_url'    => $hero['image']['url'],
		'image_alt'    => $hero['image']['alt'],
		'image_width'  => $hero['image']['width'],
		'image_height' => $hero['image']['height'],
	)
);
