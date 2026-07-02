<?php
/**
 * Service single — layout meta routes to stack partials.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="shpigovsky-skeleton shpigovsky-skeleton--service" id="main-content">
	<?php shpigovsky_render_breadcrumbs(); ?>
	<?php
	while ( have_posts() ) :
		the_post();
		shpigovsky_load_service_template();
	endwhile;
	?>
</main>
<?php
get_footer();
