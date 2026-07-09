<?php
/**
 * Blog single lower CTA stack — V9-06E26C.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$band = shpigovsky_get_article_cta_band( get_the_ID() );

if ( empty( $band['title'] ) && empty( $band['button_label'] ) ) {
	return;
}
?>
<div class="blog-article-lower-stack">
	<?php
	set_query_var( 'shpigovsky_program_cta_band', $band );
	get_template_part( 'template-parts/components/program-cta-band' );
	?>
</div>
