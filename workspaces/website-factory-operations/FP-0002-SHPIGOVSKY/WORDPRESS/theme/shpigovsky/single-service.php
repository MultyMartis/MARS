<?php
/**
 * Service single — layout variant routes to stack partials.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

while ( have_posts() ) :
	the_post();

	$variant    = shpigovsky_get_service_layout_variant();
	$main_class = shpigovsky_get_service_main_class( $variant );
	?>
<main class="<?php echo esc_attr( $main_class ); ?>" id="main-content">
	<?php shpigovsky_load_service_template(); ?>
</main>
	<?php
endwhile;

get_footer();
