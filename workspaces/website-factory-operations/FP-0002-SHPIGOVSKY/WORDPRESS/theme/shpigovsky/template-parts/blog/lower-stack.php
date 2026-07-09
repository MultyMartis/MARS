<?php
/**
 * Blog archive lower stack — V9-06E26B.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<div class="blog-lower-stack">
	<?php
	set_query_var( 'shpigovsky_program_cta_band', shpigovsky_get_blog_archive_cta_band() );
	get_template_part( 'template-parts/components/program-cta-band' );
	get_template_part( 'template-parts/blog/expert-quote' );
	?>
</div>
