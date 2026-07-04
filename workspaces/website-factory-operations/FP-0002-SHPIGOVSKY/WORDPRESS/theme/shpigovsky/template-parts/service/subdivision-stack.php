<?php
/**
 * Service subdivision stack orchestrator.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<article <?php post_class( 'shpigovsky-service shpigovsky-service--subdivision' ); ?>>
	<?php
	get_template_part( 'template-parts/service/inner-hero' );
	get_template_part( 'template-parts/service/subnav' );
	get_template_part( 'template-parts/service/children' );
	get_template_part( 'template-parts/service/mid-cta' );
	get_template_part( 'template-parts/service/program' );
	get_template_part( 'template-parts/service/stages' );
	get_template_part( 'template-parts/service/faq' );
	get_template_part( 'template-parts/components/final-form' );
	?>
</article>
