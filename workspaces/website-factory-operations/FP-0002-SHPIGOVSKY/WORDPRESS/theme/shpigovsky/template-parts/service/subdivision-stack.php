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
<article <?php post_class( 'shpigovsky-skeleton__service shpigovsky-skeleton__service--subdivision' ); ?>>
	<?php
	get_template_part( 'template-parts/service/inner-hero' );
	get_template_part( 'template-parts/service/intro' );
	get_template_part( 'template-parts/components/program-cta-band' );
	?>
</article>
