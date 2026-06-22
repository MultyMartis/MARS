<?php
/**
 * Front page template.
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<?php get_template_part( 'template-parts/hero' ); ?>
<?php get_template_part( 'template-parts/services-teaser' ); ?>
<?php
get_template_part(
	'template-parts/faq',
	null,
	array(
		'faq_id'  => 'home-faq',
		'post_id' => get_queried_object_id(),
	)
);
?>
<?php get_template_part( 'template-parts/cta-global' ); ?>
<?php
get_footer();
