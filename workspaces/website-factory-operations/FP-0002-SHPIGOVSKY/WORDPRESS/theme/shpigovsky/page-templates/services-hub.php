<?php
/**
 * Template Name: Services Hub
 * Route family: /uslugi/
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();
?>
<main class="page-uslugi site-main site-main--services-hub" id="main-content">
	<?php
	get_template_part( 'template-parts/services-hub/hero' );
	get_template_part( 'template-parts/services-hub/service-groups' );
	get_template_part( 'template-parts/services-hub/rehabilitation-program' );
	get_template_part( 'template-parts/services-hub/faq' );
	get_template_part( 'template-parts/components/final-form' );
	?>
</main>
<?php
get_footer();
